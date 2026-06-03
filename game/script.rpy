#this is how i made the game it's rly easy wow

init:
    image bg thefort  = "bg thefort.png"
    image bg dollyg  = "bg dollyg.png"
    image bg bedroom  = "bg bedroom.png"
    image bg kitchen  = "bg kitchen.png"
    image bg road  = "bg road.png"
    image bg gasstation = "bg gasstation.png"
    image bg gasstationinside = "bg gasstationinside.png"
    image bg sidegasstation = "bg sidegasstation.png"
    image bg grossroom = "bg grossroom.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

screen persistent_object():
    # 'add' displays the image, 'align' positions it (x, y)
    add "thursday.png" align (0.95, 0.05) # Top right corner

image implore = Movie(channel="movie_dp", play="images/implore.webm")
image loredance = Movie(channel="movie_dp", play="images/loredance.webm")

# delete this! ------------------------------------------------------------------------------------------------
# define a character, attach a callback for speaking sounds and lipsync 
# syntax: define <whatever> = Character("<Character Name>", callback=make_text_sounds("<sounds folder>", "<animation toggle>"))
define c = Character("Chili", callback=make_text_sounds("audio/chili/", "chili_talking"))
# ------------------------------------------------------------------------------------------------------------

# can also be used without the animation toggle if you just want the sounds
define e = Character("Lacey", color="#40E0D0", callback=make_text_sounds("audio/lacey/"))
define m = Character ("Sean", color="#ff8d33", callback=make_text_sounds("audio/sean/"))


transform stopTalking:
    zoom 1
    matrixcolor SaturationMatrix(1)
    ease 0.33 zoom 0.95 matrixcolor SaturationMatrix(0.66)

transform startTalking:
    zoom 0.95
    matrixcolor SaturationMatrix(0.66)
    ease 0.33 zoom 1 matrixcolor SaturationMatrix(1)

# The game starts here.

label start:
show screen persistent_object
"I don't make a habit of coming back home too often."
scene bg thefort
with fade
play music roadtrip
show screen persistent_object

## TEMP! Added chili talking for example, delete the `c` at the start of the line to make it go away. -----
show Chili at idle_bob with easeinleft: ## animation example
    xpos 0.6 ypos 0.2
c "Everyone glamorizes small town living."
c "They talk about how quiet it is, and the stars at night, and how everybody knows their neighbors."
c "They don't talk about how you gotta drive forty-five minutes just to get decent produce, though."
c "...Or how there's meth heads living at the end of just about every holler."
## --------------------------------------------------------------------------------------------------------

scene bg dollyg
with fade
"It's even worse now."
"Back when I was growing up, there used to be all sorts of shops run by locals. Real mom and pop places with country charm."
"Now all you get are dollar stores and 'cash 4 gold' joints, or the occasional vape store."
"Sometimes you'll even have two different dollar stores right next to each other."
"It's especially weird since they're not even competing, they're all owned by the same company."
"Wait until I tell you about the different syrup companies. It's a conspiracy."
scene bg bedroom
with fade
"My parents are old now. Visiting them is like opening a time capsule."
"They're not decrepit enough to need a stair lift or anything, but I'm worried the candy dish full of caramels will come out any day now."
"They still have my room how I left it, even if mom's using my closet to store her t-shirt press and endless rolls of vinyl."
"That's another small town staple: moms making side hustles or small businesses to bring in extra dough and somehow losing money in the process."
"I keep my mouth shut about it, though."
scene bg kitchen
with fade
"There's a turkey cooking in the oven. My mom does some forbidden witchcraft that somehow involves root beer?"
"I have no fucking clue, but it always tastes amazing. I let her cook."
"I'm prepared for endless questions about how I'm doing, and potential romantic partners, which I will inevitably try to parry."
"However, I'm informed we're out of ingredients for the gravy."
"Turkey and mashed potatoes without gravy obviously cannot come to pass."
"I valiantly offer to take the family car to the local Dolly G to save the day."
scene bg road
with fade
"My mom drives an enormous SUV with a third row seat, as if she's still ferrying a bunch of kids to school."
"It's been awhile since I've driven a car. It's not that I don't want one, but finding a place to park it in the city is a nightmare."
"Apart from being a little jerky on the brakes, the drive goes fine."
"Mom is nearly out of gas, though."
"It's a bad habit of hers to play chicken with the 'low fuel' light. I pull into the local Pump & Dump."
scene bg gasstation
with fade
"This gas station's been on the verge of closing for as long as I can remember."
"It's a rundown piece of shit, and just like I remember, the card readers on the pumps don't work right. I walk into the store."
scene bg gasstationinside
with fade
"It stinks in here. It's a fun combo of burnt coffee, lemon-scented floor cleaner, and gasoline fumes that waft in every time the door opens."
"It's honestly kinda nostalgic. Even unpleasant things can bring back memories."
"I shoplifted in here for the first time. It was a Take 6 bar."
"I felt so bad about it that I almost threw up. Ended up sneaking it back into the store."
show fatguy with dissolve
"I'm waiting behind some fat dude in a trucker hat in line."
"His shirt's emblazoned with so many oddly-specific tough guy slogans that it somehow loops back around to being awesome."
"I kind of want one."
hide fatguy with dissolve
"The dude gets his comically oversized beef stick and his white boomer drink and shuffles off. I step up to the counter, somewhat listlessly."
show sean dress bored
with easeinleft
"Sean" "Can I get ten bucks on pump 3?"
"The woman behind the counter is busying herself on her phone and only gives me a cursory glance."
"Then I feel her staring at me."
"She suddenly puts down her phone, and the movement draws my eye."
show sean dress bored at stopTalking
show lacey work surprised
with easeinright

# TEMP speaking example -------------------------------------------------
e "...Sean? Is that you?" 
"I look up, a bit surprised to hear my name. For a moment, I don't recognize the person greeting me."
"It hits me like a truck a second later."
show lacey work surprised at stopTalking
show sean dress surprised at startTalking
m "Lacey? Holy shit. Wow! Uh, how have you been?"
"Lacey was my best friend growing up. She looks more or less the same as when I last saw her, but she's definitely gained a little bit of weight."
show sean dress surprised at stopTalking
show lacey work smile at startTalking
e "Stayin' alive. You know how it is."
show lacey work smile at stopTalking
"There's a moment where neither of us say anything. We just kinda stare at each other like morons for a second. At least I feel like a moron."
show lacey work talk at startTalking
e "It's so surreal seeing you again, Sean. How long has it even been? Like seven years?"
show lacey work talk at stopTalking
show sean dress wince at startTalking
m "Something like that. I uh, moved up North, or at least further up the river."
show sean dress wince at stopTalking
"She nods, and I think I detect a little sadness in her expression."
show lacey work smile at startTalking
"Lacey" "Well, you look great, Sean. Really. You look uh...put together? Is that rude to say?"
show lacey work smile at stopTalking
"She laughs and I get a funny feeling in my chest. I haven't heard that laugh in so long."
show sean dress joke at startTalking
m "Well, I hope I'm put together. I don't think the Sean factory is still in business."
# -------------------------------------------------------------------------------

show sean dress joke at stopTalking
show lacey work laugh at startTalking
"Lacey" "Very funny. I mean it, though. You always said you'd get outta here and make something of yourself. And look at you now. I never saw you in button-up shirts before."
show lacey work laugh at stopTalking
"I did used to say that. But so did she. It was always the two of us together, until...well."
show sean dress joke wince at startTalking
"Sean" "How's Ralphie doing? Are you guys, uh...still a thing?"
show sean dress joke wince at stopTalking
"Ralphie was a kid we occasionally hung out with growing up."
"I always liked Lacey, but I never could work up the nerve to tell her how I felt."
"Ralphie ended up asking her out in senior year."
"She even asked me if it was okay, and I said yes. I had so many opportunities to not be a little bitch, but I blew it."
"And then I had the nerve to be pissed at them after they started dating."
show lacey work uncomfortable at startTalking
"Lacey" "Oh. Uh, no."
show lacey work uncomfortable at stopTalking
"She looks uncomfortable, like she hasn't been asked about this topic in a long while. She clears her throat before continuing."
show lacey work uncomfortable 2 at startTalking
"Lacey" "Ralphie's a good guy, but...ah, I don't want to say anything bad about him. It didn't work out."
show lacey work uncomfortable 2 at stopTalking
"Selfishly, I want her to say something bad about him. I want to hear the whole story, and feel vindicated somehow."
"As if I didn't flake on my best friend because I was jealous."
show sean dress uncomfortable at startTalking
"Sean" "When did that happen? I mean, the uh...the breakup."
show sean dress uncomfortable at stopTalking
show lacey work talk at startTalking
"Lacey" "I mean, it's been years. I heard he's working for his dad's trucking company now or something."
show lacey work talk at stopTalking
show sean dress wince at startTalking
"Sean" "Oh. Well, I'm sorry things didn't work out. Really. Even if I was a huge dickhead about you two."
show sean dress wince at stopTalking
"She looks out at the mostly empty parking lot, then back at me."
show lacey work uncomfortable at startTalking
"Lacey" "I need a cigarette, Sean. You wanna go outside and talk?"
scene bg sidegasstation
with fade
"We both step outside. She's the only one working, but it's also pretty dead right now."
"I probably should be getting those ingredients. It's why I left the house in the first place, but I can't bring myself to give a shit in that moment."
"She lights up a cigarette and takes a big inhale. No idea when she picked up the habit, she never smoked when I knew her."
"Smoking is nasty, but there is no denying that it makes you look cool. It's a painful fact of life."
show lacey work smoking smile
with easeinright
"Lacey" "You here visiting your parents? How are they?"
show lacey work smoking smile at stopTalking
show sean dress wince
with easeinleft
"Sean" "They keep getting older, man. It's fucking me up. Apart from that, I'd say they're...I dunno, typical?"

# idle animation test!! ----------------------------------
show sean dress wince idle at stopTalking
# --------------------------------------------------------

show lacey work smoking talk at startTalking
"Lacey" "Well, I guess that's good. My parents are really into like, food truck stuff. Food trucking?"
show lacey work smoking talk at stopTalking
show sean dress neutral at startTalking
"Sean" "No shit? Is that working out?"
show sean dress neutral at stopTalking
show lacey work smoking frown at startTalking
"Lacey" "Not really. At least not yet. There's like, a ton of up-front stuff you gotta pay for before you can really get going. So you start in the hole for a lot of money."
show lacey work smoking frown at stopTalking
"Money is hard to come by around here."
"Either you're a bored retiree with too much of the stuff, or you're broke."
"There aren't a lot of people in between."
show sean dress neutral 2 at startTalking
"Sean" "You living with them? Your parents, I mean."
show sean dress neutral 2 at stopTalking
show lacey work smoking talk at startTalking
"Lacey" "Nah. Me and Ralphie rented a place at Shady Pines. When we broke up I was able to stay on the lease for it."
show lacey work smoking talk at stopTalking
show sean dress surprised at startTalking
"Sean" "The trailer park?"
show sean dress surprised at stopTalking
"It just kinda comes out of my mouth. I feel like an ass immediately."
show sean dress surprised 2 at startTalking
"Sean" "I mean, not that there's anything wrong with that, Lace."
show sean dress surprised 2 at stopTalking
"She laughs, and I feel a little relieved."
show lacey work smoking laugh at startTalking
"Lacey" "Yeah, I'm trailer trash now. It isn't so bad, though. I'm able to afford it working here, if just barely."
show lacey work smoking laugh at stopTalking
"It's a bit depressing, really. Lacey and I always used to talk about all the amazing things we'd do when we got out of Fairview."
"She wanted to be a tattoo artist. Did all this research about it too. "
"I wanted to be a game developer, but instead ended up as the IT guy for a local retail chain."
"Most days I'm on my phone unless someone needs their password reset, or the printer stops working."
"I guess neither of us got what we wanted in the end."
show sean dress uncomfortable at startTalking
"Sean" "I missed you."
show sean dress uncomfortable at stopTalking
"I just blurt it out. Maybe it's the surprise of seeing her that's got me acting weird."
"Maybe it's my brain internally kicking me for not saying what I wanted to all those years ago. But I'm speaking now."
show lacey work smoking uncomfortable at startTalking
"Lacey" "I missed you too, Sean. I really regret how our friendship ended up."
show lacey work smoking uncomfortable at stopTalking
show sean dress neutral handup at startTalking
"Sean" "There ain't nothing for you to regret, I was...I didn't know how to tell you how I felt. And I just made a total ass of myself."
show sean dress neutral handup at stopTalking
show lacey work smoking frown at startTalking
"Lacey" "It's okay."
show lacey work smoking frown at stopTalking
"It gets quiet again. I'm struggling with all the things I want to say to her. Where do I even start?"
show lacey work smoking talk at startTalking
"Lacey" "How long are you staying?"
show lacey work smoking talk at stopTalking
show sean dress neutral at startTalking
"Sean" "Oh. Uh...a week. Then I gotta go back to work."
show sean dress neutral at stopTalking
"She nods, as if mulling something over in her head. She takes out her phone from her pocket a moment later."
show lacey work smoking lookphone at startTalking
"Lacey" "Can I get your number? Maybe we can hang out again while you're here."
show lacey work smoking lookphone at stopTalking
"I thought she had my number. I remembered that I'd changed it a few years back when I switched carriers."
"Had she ever tried to text me? I hadn't used Facespace in ages since I couldn't bear to look at her and Ralphie together."
show sean dress bored phone at startTalking
"Sean" "Of course."
show sean dress bored phone at stopTalking
"I give her my number."
show lacey work smoking lookphone smile at startTalking
"Lacey" "Cool. Well, I gotta get back to work, Sean. It was really nice seeing you, though. Tell your parents I said hi, okay?"
show lacey work smoking lookphone smile at stopTalking
show sean dress nervous phone at startTalking
"Sean" "Y-yeah, you too. Oh, uh--can I get ten bucks on pump 3?"
scene bg dollyg
with fade
"I go to the Dolly G, then I'm back home with the gravy ingredients. I save the day, but the whole time I'm thinking about Lacey."
"We were supposed to leave together."
play music chicken
scene bg grossroom
with fade
show loredance:
    xalign 0.5 yalign 0.2
"Lorepaw" "Wowie kazowie! Thanks for playing this funny little demo disk! For the Gay Station home entertainment system!"
hide loredance
show buffpaw with dissolve
"Lorepaw" "I hope you liked it! More importantly, I hope you see my autistic vision..."
"Lorepaw" "This is the end of the demo! If you're sad about that, don't be! I'll be putting out more soon."
hide buffpaw with dissolve
show implore:
    xalign 0.5 yalign 0.2
"Lorepaw" "If you're already supporting me on Patreon, thanks! If not, I implore you to reconsider."
hide implore
show mockup with dissolve:
    xalign 0.5 yalign 0.2
show whoa with dissolve
"Lorepaw" "If I can fund doing this full-time, and continue working at the freakish pace I've been the last 3-4 days, good things will happen!"
"Lorepaw" "Anyway, thanks! Mwah! Eat your vegetables! Don't trust magicians!"
"THE END. (for now...)"
return
"In the morning, I'm having breakfast with my parents. I decide to mention that I saw Lacey yesterday."
"Mom and dad seem a little cagey about something. I decide to pry, and I find out something a little concerning."
"Mom" "Well, I heard that she got arrested a few years ago."
"Sean" "What? Arrested?! What for?"
"Mom" "Well...it was in the papers, sweetheart. If I remember correctly, she got a DUI and then was resisting arrest."
"The words hit me like a brick. Lacey? Doing something like that?"
"It almost was too ridiculous to believe."
"Sean" "You're fucking with me, right?"
"Dad" "Language, son."
"I groan."
"Sean" "You're pulling my leg, right?"
"She shook her head. Rumors spread like wildfire in a town like this, where everyone knew everyone else."
"I wouldn't have believed a rumor. The fact that it had been in the paper gave me pause, though."
"Sean" "She asked if I wanted to hang out while I was here. I uh...damn, maybe I don't know her so well anymore."
"Mom" "Well, people change, sweetheart."
"Maybe. I guess it could be possible that the sweet possum I grew up with is a nutjob now."
"I at least want to hear the story out of her own mouth, though."
"The rest of the day passes quickly. I'm dragged to the local auction at night."
"I'm not sure what possesses old folks to start doing wacky shit like this."
"Last time I was home, they were into buying storage lockers. I'd never seen the garage more full of useless junk."
"They bid on a 24 pack of Gaelic Breeze soap bars and lose. The bid war is surprisingly entertaining though."
"We come home and, an hour or so later, I'm in my old bed for the first time in a long time."
"I think about how much bigger this room used to feel when I was a kid."
"How me and Lacey used to play on that car city carpet that everybody somehow had."
"Or that old plastic castle set with the knights...the one with the boulder cannon. That shit was so sweet."
"I remember taking turns playing video games. We'd try to beat them all in one sitting because I didn't have a memory card."
"My chest feels tight. It's funny how just seeing someone's face again can bring so many thoughts and memories flooding back."
"I think I really did love her at one point."
"..."
"In the morning, I decide to shoot Lacey a text."
"I had the urge to do it last night, but there's that unspoken rule that you're NOT supposed to do that. Under any circumstances. I think."
"Is that still a thing?"
"text goes here. talks about how the auction was scary and cutthroat, jokingly. asks when she wants to meet up"
"She doesn't respond right away. I have breakfast with my parents and talk about what my siblings are up to."
"My older brother is trying to become an electrician. My younger sister just left to go to college herself."
"It dawns on me that this is the first time I've come to visit where I haven't gotten to kick it with at least one sibling."
"If it feels weird for me, it probably feels mega weird for my parents."
"It's around lunch time when I get a text back from Lacey."
"insert text message overlay thing here. lacey sayin shit like 'wow im glad u survived. hang tonite?"
"I feel a little bit apprehensive. I guess the news my parents dropped on me has me a little shook up."
"sure lol text message wow"