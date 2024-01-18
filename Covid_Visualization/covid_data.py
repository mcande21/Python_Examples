"""
Module to download and access NYT COVID Data

Kevin Angstadt
St. Lawrence University
CS-140-01 Spring 2021
"""

import codecs
import csv
import ssl
import urllib.request

__DATA_URL = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"

__covid = {}

# open the webpage containing all the data
context = ssl._create_unverified_context()
with urllib.request.urlopen(__DATA_URL, context=context) as __f:
    # decode the data from the file (note the charset from the data itself)
    __reader = csv.DictReader(codecs.iterdecode(__f, __f.headers.get_content_charset()), delimiter=',')

    # read each row of the data
    for __row in __reader:
        if __row['state'].lower() not in __covid:
            __covid[__row['state'].lower()] = []

        # add the entry for the specific state
        __covid[__row['state'].lower()].append({
            'date': __row['date'],
            'deaths': int(__row['deaths']),
            'cases': int(__row['cases'])
        })


def num_entries(state):
    """
    Provide the number of entries for the given state
    :param state: (string) proper name of the state
    :return: (int) total number of entries for the given state
    """
    return len(__covid[state.lower()])


def cases_on_date(state, date):
    """
    Return the cumulative number of cases recorded in the specified state
    on the given date
    :param state: (string) proper name of the state
    :param date: (string) date given in YYYY-MM-DD format
    :return: (int) cumulative number of cases
    """
    state = state.lower()
    entry = next(item for item in __covid[state] if item['date'] == date)
    return entry['cases']


def deaths_on_date(state, date):
    """
    Return the cumulative number of deaths recorded in the specified state
    on the given date
    :param state: (string) proper name of the state
    :param date: (string) date given in YYYY-MM-DD format
    :return: (int) cumulative number of deaths
    """
    state = state.lower()
    entry = next(item for item in __covid[state] if item['date'] == date)
    return entry['deaths']


def date_by_entry_id(state, id):
    """
    Return the date associated with the specified state
    for the given entry id
    :param state: (string) proper name of the state
    :param id: (int) entry to retrieve (starts at 0)
    :return: (string) the date in YYYY-MM-DD format
    """
    state = state.lower()
    return __covid[state][id]['date']


def cases_by_entry_id(state, id):
    """
    Return the cumulative number of cases recorded in the specified state
    for the given entry id
    :param state: (string) proper name of the state
    :param id: (int) entry to retrieve (starts at 0)
    :return: (int) cumulative number of cases
    """
    state = state.lower()
    return __covid[state][id]['cases']


def deaths_by_entry_id(state, id):
    """
    Return the cumulative number of deaths recorded in the specified state
    for the given entry id
    :param state: (string) proper name of the state
    :param id: (int) entry to retrieve (starts at 0)
    :return: (int) cumulative number of deaths
    """
    state = state.lower()
    return __covid[state][id]['deaths']


def valid_state(state):
    """
    Check if a state name is valid
    :param state: (string) proper name of the state
    :return: True if there is data for the state, False otherwise
    """
    state = state.lower()
    return state in __covid


def print_states():
    """
    Print the names of states included in the data
    :return: None
    """
    for state in sorted(__covid):
        print(state.title())

