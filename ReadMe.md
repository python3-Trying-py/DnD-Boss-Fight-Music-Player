I will revise this later but first I want to get a basic working of the code written down

##Viewers

Viewers handles the gui elements. It creates and displays the buttons, gizmos, and whatnots

##Services

Services handles the the audio right now. If additional functions are added to the program(e.g. video player) then a new service will be added to services

##Models

Models handles all the logic, or as much as it can. If any logic needs to happen, such as list comprehension, it happens in models

##Controllers

Controllers bridges the gap between the 3 other sections of the program. It detects GUI input and calls on the proper logic and service.