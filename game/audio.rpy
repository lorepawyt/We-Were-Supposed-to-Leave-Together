# Audio system based on continuous-text-sounds by bamboocalc
# https://github.com/bamboocalc/continuous-text-sounds
# Extended by TamLin123 - https://github.com/TamLin123/renpy-character-speak-animate/
# MIT License


init python:
    import random, re

    _TAG = re.compile(r'{cps=(\d+)}')

# Automatic pauses between punctuation
    def typography(what):
        replacements = [
                ('. ','. {w=.2}'),   # Moderate pause after periods
                ('? ','? {w=.25}'),  # Long pause after question marks
                ('! ','! {w=.25}'),  # Long pause after exclamation marks
                (', ',', {w=.15}'),  # Short pause after commas
        ]
        for item in replacements:
            what = what.replace(item[0],item[1])
        return what
    config.say_menu_text_filter = typography

# Returns a character callback that plays sounds from a given folder
# and toggles a given store variable when the character is talking.
#
# Usage: define <asd> = Character("<CharName>", callback=make_text_sounds("<sounds_folder>", "<animation_toggle>"))
#
# The animation_toggle variable is optional; 
# to animate character talking, just set up a ConditionSwitch that checks that variable you pass in here.
    # image Chili = ConditionSwitch(
    #     "chili_talking == True", "Chili speak",
    #     "chili_talking == False", "Chili chill",
    # )

    def make_text_sounds(sound_folder, talking_var=None, channel=None):
        sounds = [f for f in renpy.list_files() if f.startswith(sound_folder) and (f.endswith(".ogg") or f.endswith(".wav"))]
        ch = channel or f"textsound_{sound_folder.strip('/').replace('/', '_')}"
        renpy.music.register_channel(ch, "sfx", False)

        def callback(event, interact=True, **kw):
            if event == "show":
                if talking_var:
                    setattr(store, talking_var, True)
                renpy.sound.stop(channel=ch)
                raw  = renpy.store._last_say_what or ""
                text = renpy.substitute(raw)
                cps  = (kw.get("slow_cps") or kw.get("cps") or renpy.store.preferences.text_cps)

                for chunk in _TAG.split(text):
                    if chunk.isdigit():
                        cps = int(chunk)
                        continue
                    pause = 0 if cps <= 0 else 1.0 / cps

                    for char in chunk:
                        if not char.isspace():
                            renpy.sound.queue(random.choice(sounds), channel=ch)
                        if pause:
                            renpy.sound.queue(f"<silence {pause}>", channel=ch)

            elif event in ("slow_done", "end"):
                if talking_var:
                    setattr(store, talking_var, False)
                renpy.sound.stop(channel=ch)

        return callback