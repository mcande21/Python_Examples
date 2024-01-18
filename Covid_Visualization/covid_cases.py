# This function will display all states and print out a table
# of the cumulative number of cases on each day for that state

# well first I got to import some data
import covid_data

# using functions in that data set I can print out all states
covid_data.print_states()

# now I have to ask the user what state they want to know about
state = input("So what state you want to know about? ")

# checking to make sure that state is valid
if covid_data.valid_state(state) is False:
    print("That wasnt a state on the list, pal.")
    exit()
else:
    None

# Now I have to make sure how many entries are in the state
ID = covid_data.num_entries(state)

# Now having the entries I can use day to count up to that entry limit and total the number of cases
day = 0
for day in range(ID):
        cases = covid_data.cases_by_entry_id(state, day)

print("Alright so,", state, "has about", cases, "covid cases... sorry.")
