# You can define characters, animations and transforms in separate files!

# Any character can use this animation even if it's in a separate file!
transform idle_bob:
    yoffset 0
    ease 1 yoffset 15
    ease 1 yoffset 0
    repeat


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




