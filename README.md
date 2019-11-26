# robot_uprising


this mess of a repo is for robot uprising hackathon
the heroes of this story are me, iiro naumanen and niklas valuri

we don't usually code like this, don't worry.

## The tech

We used a EV3 Lego brick which we flashed with ev3dev, a linux based distro made for the EV3 to allow you to use other development tools than just the Lego's own language. We used Python 3.

## The tracks

We managed to complete the track, but not with full automation. There were 5 tracks of which 3 we automated.

Two of the tracks were done with recorded movement, which qualified as automated.

One of the automated tracks was made using a premade moveset. I built a tree-like moveset parser (bot_base.py) with some common actions for the robot, but due to time limitations we ended up using it in only one of the tracks. One of the moveset commands was to level the bot with a wall on its left to help guide the movement.

### Problems and solutions

The main problem we encountered was that the robot's movement relied heavily on the battery level of the robot. This means we had to make some adjustments to the movements. Two tricks were heavily used: 1) Building a back bumper for the robot so we could automate a backwards movement to level it with a back wall and 2) Programming the function to level the bot with the left wall to correct the angle of movement from time to time.

## Placement

To our surprise, we placed 9th out of 38. We had not expected such a good placement as we were there just to get some hackathon experience and have fun!
