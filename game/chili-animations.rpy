# You can define characters, animations and transforms in separate files!
# Also: this file is safe to delete! 
# Just make sure you delte the Chili stuff from script.rpy too
define chili_talking = False

# The magic sauce; switches character image based on the condition of the variable 
image Chili = ConditionSwitch(
    "chili_talking == True", "Chili speak",
    "chili_talking == False", "Chili chill",
)

# idle
image Chili chill:
    "chili/chili chill.png"

# loops through frames like a GIF
define frame_delay = 0.1
image Chili speak:
    "chili/chili speak 1.png"
    pause frame_delay
    "chili/chili speak 2.png"
    pause frame_delay
    "chili/chili speak 3.png"
    pause frame_delay
    "chili/chili speak 4.png"
    pause frame_delay
    "chili/chili speak 5.png"
    pause frame_delay
    "chili/chili speak 6.png"
    pause frame_delay
    repeat




