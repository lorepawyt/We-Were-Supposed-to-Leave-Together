# The script of the game goes in this file.

init:
    image bg thefort  = "bg thefort.png"
    image bg dollyg  = "bg dollyg.png"
    image bg bedroom  = "bg bedroom.png"
    image bg kitchen  = "bg kitchen.png"
    image bg road  = "bg road.png"
    image bg gasstation = "bg gasstation.png"
    image bg gasstationinside = "bg gasstationinside.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Lacey = Character("Lacey")
define Sean = Character ("Sean")

# The game starts here.

label start:
"I don't make a habit of coming back home too often."
scene bg thefort
with fade
play music roadtrip
"Everyone glamorizes small town living. They talk about how quiet it is, and the stars at night, and how everybody knows their neighbors."
"They don't talk about how you gotta drive forty-five minutes just to get decent produce, though."
"...Or how there's meth heads living at the end of just about every holler."
scene bg dollyg
with fade
"It's even worse now. Back when I was growing up, there used to be all sorts of shops run by locals. Real mom and pop places with country charm."
"Now all you get are dollar stores and 'cash 4 gold' joints, or the occasional vape store."
"Sometimes you'll even have two different dollar stores right next to each other."
"It's especially weird since they're not even competing, they're all owned by the same company."
scene bg bedroom
with fade
"My parents are old now. Visiting them is like opening a time capsule."
"They still have my room how I left it, even if mom's using my closet to store her t-shirt press and endless rolls of vinyl."
"That's another small town staple: moms making side hustles or small businesses to bring in extra dough and somehow losing money in the process. I don't say anything about it, though."
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
"It's been awhile since I've driven a car, but apart from being a little jerky on the brakes, it goes fine."
"She is nearly out of gas, though."
"It's a bad habit of hers to play chicken with the 'low fuel' light. I pull into the local Pump & Dump."
scene bg gasstation
with fade
"This gas station's been on the verge of closing for as long as I can remember."
"It's a rundown piece of shit, and just like I remember, the card readers on the pumps don't work right. I walk into the store."
scene bg gasstationinside
with fade
"It stinks in here. It's a fun combo of burnt coffee, lemon-scented floor cleaner, and gasoline fumes that waft in every time the door opens."
"I'm waiting behind some fat dude in a trucker hat in line. His shirt's emblazoned with so many tough guy slogans that it somehow loops back around to being awesome."
"I kind of want one."
"The dude gets his comically oversized beef stick and his white boomer drink and shuffles off. I step up to the counter, somewhat listlessly."
show sean dress bored
with moveinleft
"Sean" "Can I get ten bucks on pump 3?"
"The woman behind the counter is busying herself on her phone and only gives me a cursory glance."
"I hear her very suddenly put down her phone."
show lacey work surprised
with moveinright
"???" "...Sean? Is that you?"
show sean dress huh at left
"I look up, a bit surprised to hear my name. My eyes lock with the woman behind the counter, and for a moment, I don't recognize her."
show sean dress surprised at left
"Sean" "Lacey? Holy shit. Wow! Uh, how have you been?"
"Lacey was my best friend growing up. She looks more or less the same than when I last saw her, but she's definitely gained a little bit of weight."
show lacey work smile at right
"Lacey" "Stayin' alive. You know how it is."
"There's a moment where neither of us say anything. We just kinda stare at each other like morons for a second. At least I feel like a moron."
"Lacey" "It's so surreal seeing you again, Sean. How long has it even been? Like seven years?"
"Sean" "Something like that. I uh, moved up North, or at least further up the river."
"She nods, and I think I detect a little sadness in her expression."
"Lacey" "Well, you look great, Sean. Really. You look uh...put together? Is that rude to say?"
"She laughs and I get a funny feeling in my chest. I haven't heard that laugh in so long."
"Sean" "Well, I hope I'm put together. I don't think the Sean factory is still in business."
"Lacey" "Very funny. I mean it, though. You always said you'd get outta here and make something of yourself. And look at you now. I never saw you in button-up shirts before."
"I did used to say that. But so did she. It was always the two of us together, until...well."
"Sean" "How's Ralphie doing? Are you guys, uh...still a thing?"
"Ralphie was a kid we occasionally hung out with growing up. I always liked Lacey, but I never could work up the nerve to tell her how I felt. Ralphie ended up asking her out in senior year."
"She even asked me if it was okay, and I said yes. I had so many opportunities to not be a little bitch, but I blew it. And then I had the nerve to be pissed at them after they started dating."
"Lacey" "Oh. Uh, no."
"She looks uncomfortable, like she hasn't been asked about this topic in a long while. She clears her throat before continuing."
"Lacey" "Ralphie's a good guy, but...ah, I don't want to say anything bad about him. It didn't work out."
"Selfishly, I want her to say something bad about him. I want to hear the whole story, and feel vindicated somehow."
"As if I didn't flake on my best friend because I was jealous."
"Sean" "When did that happen? I mean, the uh...the breakup."
"Lacey" "I mean, it's been years. I heard he's working for his dad's trucking company now or something."
"Sean" "Oh. Well, I'm sorry things didn't work out. Really. Even if I was a huge dickhead about you two."
"She looks out at the mostly empty parking lot, then back at me."
"Lacey" "I need a cigarette, Sean. You wanna go outside and talk?"
"We both step outside. She's the only one working, but it's also pretty dead right now."
"I probably should be getting those ingredients. It's why I left the house in the first place, but I can't bring myself to give a shit in that moment."
"She lights up a cigarette and takes a big inhale. No idea when she picked up the habit, she never smoked when I knew her."
"Lacey" "You here visiting your parents? How are they?"
"Sean" "They keep getting older, man. It's fucking me up. Apart from that, I'd say they're...I dunno, typical?"
"Lacey" "Well, I guess that's good. My parents are really into like, food truck stuff. Food trucking?"
"Sean" "No shit? Is that working out?"
"Lacey" "Not really. At least not yet. There's like, a ton of up-front stuff you gotta pay for before you can really get going. So you start in the hole for a lot of money."
"Money is hard to come by around here. Either you're a bored retiree with too much of the stuff, or you're broke. There isn't a lot of people in between."
"Sean" "You living with them? Your parents, I mean."
"Lacey" "Nah. Me and Ralphie rented a place at Shady Pines. When we broke up I was able to stay on the lease for it."
"Sean" "The trailer park?"
"It just kinda comes out of my mouth. I feel like an ass immediately."
"Sean" "I mean, not that there's anything wrong with that, Lace."
"She laughs, and I feel a little relieved."
"Lacey" "Yeah, I'm trailer trash now. It isn't so bad, though. I'm able to afford it working here, if just barely."
"It's a bit depressing, really. Lacey and I always used to talk about all the amazing things we'd do when we got out of Fairview."
"She wanted to be a tattoo artist. Did all this research about it too. "
"I wanted to be a game developer, but instead ended up as the IT guy for a local retail chain."
"Most days I'm on my phone unless someone needs their password reset, or the printer stops working."
"I guess neither of us got what we wanted in the end."
"Sean" "I missed you."
"I just blurt it out. Maybe it's the surprise of seeing her that's got me acting weird."
"Maybe it's my brain internally kicking me for not saying what I wanted to all those years ago. But I'm speaking now."
"Lacey" "I missed you too, Sean. I really regret how our friendship ended up."
"Sean" "There ain't nothing for you to regret, I was...I didn't know how to tell you how I felt. And I just made a total ass of myself."
"Lacey" "It's okay."
"It gets quiet again. I'm struggling with all the things I want to say to her. Where do I even start?"
"Lacey" "How long are you staying?"
"Sean" "Oh. Uh...a week. Then I gotta go back to work."
"She nods, as if mulling something over in her head. She takes out her phone from her pocket a moment later."
"Lacey" "Can I get your number? Maybe we can hang out again while you're here."
"I thought she had my number. I remembered that I'd changed it a few years back when I switched carriers."
"Had she ever tried to text me? I hadn't used Facespace in ages since I couldn't bear to look at her and Ralphie together."
"Sean" "Of course."
"I give her my number."
"Lacey" "Cool. Well, I gotta get back to work, Sean. It was really nice seeing you, though. Tell your parents I said hi, okay?"
"Sean" "Y-yeah, you too. Oh, uh--can I get ten bucks on pump 3?"
"I go to the Dolly G, then I'm back home with the gravy ingredients. I save the day, but the whole time I'm thinking about Lacey."
"We were supposed to leave together."
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

return