#!/usr/bin/env python3

import sys

# put all lines into list
lines = [line.strip() for line in sys.stdin]

# line 1 is always the length of road (1 ≤ roadLength ≤ 1000) in km
if 1 <= int(lines[0]) <= 1000:
    roadLength = int(lines[0])
else:
    sys.exit("The length of the road inputted was outside of the accepted range (1 <= road length <= 1000).")

# timer for output
timer = 0

# dictionary to store the traffic light values
trafficLights = {}

# trafficLightDistance is the distance of the traffic light from the start of the road in km.
# put all traffic light values into trafficLights dictionary
for line in lines[1:]:
    tokens = line.split()
    tokens = [int(token) for token in tokens]

    if 1 <= tokens[0] < roadLength and 1 <= tokens[1] <= 100 and 1 <= tokens[2] <= 100:
        trafficLightDistance, redAndGreen = tokens[0], tuple(tokens[1:])
        trafficLights[trafficLightDistance] = redAndGreen
    else:
        sys.exit(
            f'One of the inputs on the line containing "{line}" is outside of the accepted ranges for a traffic light.')

# print(trafficLights)

# distanceTravelled, add 1 to distanceTravelled whenever we move
distanceTravelled = 0
while distanceTravelled < roadLength:
    # add 1 to timer everytime we move 1 km
    timer += 1

    # check if there is a traffic light at our position
    if distanceTravelled in trafficLights:

        # timeRedOn and timeGreenOn tell us how long the red and green lights stay on for, in minutes.
        timeRedOn, timeGreenOn = trafficLights[distanceTravelled]

        # divide and modulus the time by the amount of time that red is on, put this into a tuple (would have used
        # divmod() but it didn't work)
        div = timer / timeRedOn
        mod = timer % timeRedOn
        divModResult = (div, mod)

        # check if our time is divisible by the amount of time  that the red light is on for, if it is then there is
        # a chance that the light could be red, do this by using div from before and seeing if it is not zero
        if div != 0:

            if divModResult[0] == 0:
                timer += divModResult[1]

            elif divModResult[1] <= timeGreenOn:
                timer += 1

    distanceTravelled += 1

print(timer)
