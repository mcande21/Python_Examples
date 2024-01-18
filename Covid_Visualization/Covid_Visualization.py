# This program will create a visualization of communicative covid
# cases in a specific state

# first I have to import the necessary mods
import covid_data
import pygame


# Now I have to ask the user what state they want to choose from and check if its valid
state = input("Alright now out of our lovely 50 states,what state do you want to see? ")
if not covid_data.valid_state(state):
    exit()

# Now I have to set up my pygame window and establish height and width
pygame.init()
window_width = 800
window_height = 600
win = pygame.display.set_mode((window_width, window_height))
# This will create a fun gradiant over the window
for y in range(window_height):
    for x in range(window_width):
        # calculate color as a proportion of the width
        val = 255 * y // window_height
        # all gray colors have equal R, G, and B values
        win.set_at((x,y), (val, val, val))


# Now I am asking the user if they want to visualize cases or deaths.
decider = input("Alright do you want to visualize the cases or deaths of your state? ")

# Now I am writing and if and else statement.
# if the user input is cases then it will assign values specific numbers
# if the user input is deaths then it will assign values different numbers
Numb = int(covid_data.num_entries(state))
old_plot = 0
max_slope = 0
mean_slope = 0
for ID in range(1, Numb):
    if decider == "deaths":
        plot = covid_data.deaths_by_entry_id(state, ID)
    elif decider == "cases":
        plot = covid_data.cases_by_entry_id(state, ID)
    slope = (plot - old_plot)
    old_plot = plot
    if slope > max_slope:
        max_slope = slope
        mean_slope += slope
mean_slope = int(mean_slope / Numb)

old_plot = 0
for ID in range(1, Numb):
    if decider == "deaths":
        plot = covid_data.deaths_by_entry_id(state, ID)
        max = covid_data.deaths_by_entry_id(state, (Numb - 1))
    elif decider == "cases":
        plot = covid_data.cases_by_entry_id(state, ID)
        max = covid_data.cases_by_entry_id(state, (Numb - 1))
    x = ID * window_width // Numb
    y = window_height - (plot * window_height // max)
    slope = (plot - old_plot)
    old_plot = plot
    val = (slope ** (1 / 3)) / (max_slope ** (1 / 3)) * 255
    # Im using a hard code as 2 because I do not want to the size to be determined by the window
    pygame.draw.circle(win, (val, val, val), (x, y), 2)
    pygame.display.update()

while True:
    # process all the events
    for event in pygame.event.get():
        # check the type of the event
        if event.type == pygame.QUIT:
            # the user clicked the x quit at the top right of the window
            # python has a function called exit that will quite the program
            exit()

pygame.display.update()
pygame_helper.wait_for_click()



