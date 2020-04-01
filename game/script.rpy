# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Tom")
define r = Character("Racoon") 
define c = Character("Command")
define g = Character("Gotchi")
define m = Character("Mikki")
define w = Character("???")

transform half_height:
    ypos 1.5

label start:

    scene bg space

    "Space sure is vast."

    "Whereas most people would just see an endless black void..."
 
    "I see a lot of oportunities and aventures to be had."

    "Cosmic marvels, exploding stars, just a beautiful, endless playground to explore."

    scene bg window
    with dissolve

    r "Whew, this trip sure is taking long."

    r "I wonder how much longer until the probe arrives..."
     
#sonido de vibracion
    "BZZZ-BZZZ"

    "A vibration in my pocket perks me up, taking me away from my cosmic trance."

    "I slip my hand into my pocket, and take out a small ovoid device, its screen flashing with bright colours"

    show gotchi at right
    with moveinbottom

    g "Hey, why the long face, chump?"

    r "Can't I have some quality thinking time without you buzzing in every five minutes?"

    g "No can do, buddy! You're the one who took me along for the ride! Ahahahaha!"

    g "Now feed me! I'm hungry again!"

    r "Sigh..."

#sonido de presionar botones
    "I take the little thingamajig into my hands, pressing a couple of buttons and navigating various menus."

    r "Okay, I'll feed you, not like I have much else to do with my time now anyways."

    "It might not look like it but this is one of the latest advances in commercial AI tech."

    "A hybrid between a personal assistant and a virtual pet, all squashed in this neat little device."

    "This little guy particularly's called Gotchi, and he's been with me for the past few years."

    g "*munch munch*"

    g "Hey, did you get new food or something? This tastes great!"

    r "Well, I decided to spend a little a couple more steps than usual to get you something a little more gourmet this time!"

    "He's been the one keeping track of my agenda lately, and despite the spoiled machine he appears to be, he's dang good and efficient about it."

    "And of course, he keeps me company in moments like these."

    #Mas wea de contexto y personificacion del prota y Gotchi

    c "ATTENTION ALL PASSENGERS"

    c "ARRIVAL TO THE ISS DUE IN 5 MINUTES"

    c "PLEASE PREPARE FOR DOCKING AND FOLLOW ALL SAFETY PRECAUTIONS"

    r "Finally."

    hide gotchi
    with dissolve

    "Promptly I return to my seat, stashing Gotchi away in my pocket despite his 8-bit protests and observe through my window the docking process."
    
    #El docking

    "Finally, the probe's hatch opens, air rushing out as the pressure between rooms equalizes, the metal door moving to one side as it reveals the ISS interiors..."

    "...or so I thought"

    show tom shadow
    with moveinleft

    "A big silhouette stands behind the door, obscured by the backlights as it looms over me, slowly taking a step inside the ship..."

    r "Uhhh..."

    hide tom shadow

    scene bg pas
    show tom at left, half_height
    with dissolve

    t "Hey brat, how was the trip? Hehe."

    "A fiendish hyena blocks my path out the probe, armed with a mop"

    t "Ah shit, what kind of manners are these? Mama Tom taught you better..."

    "The big man offers an extended paw, looking at me expectantly and waiting for me to follow up on his handshake"

    t "What? I don't bite kiddo, and my hands sure are clean!"

    t "...I think"    
    
    "I finally snap out of my stupor and accept his handshake, trying to keep up with the brutal janitor's shaking"

    t "Thomas Santana here, but you can just call me Tom, kiddo."
    
    t "I'm the only janitor here in the ISS so, if you need some cleanup I'll come around, heh."

    "Tom, huh? Sounds like a breezy dude..."

    "We start walking down a hallway, various metallic doors opening and closing behind us as que go."

    t "So... for now my only task is to escort you to the ISS director's office, but you'll surely be seeing me around usually!"

    "Tom starts eyeing me up and down as we walk down the hallway. He doesn't seem to have the littlest bit of intent to disimulate the fact."

    t "Seeing as you're one of those coon types... I guess I'll have to clean up every time you assault the trashcan! HYAHYAHYA"

    t "..."

    t "Heh! Just kidding, kiddo. Brighten up a little, c'mon."

    t "Hey, brat... do you have some candies...?"

    "Not for you, asshole."

    t "This old bloodhound needs some sugar... something chewable perhaps."
    
    t "The food here is awful. It's just some dough shit without any taste, that shakes my head."

    t "This man needs some bite in his food! Taste it and feel it like a wild animal!"

    # Mas charla con Tom, un poco de caracterizacion, hay que hacer hablar mas al prota carajo

    t "Well, here we are Coony."

    scene bg entrada
    show tom at left, half_height
    with dissolve

    "We finally come to a stop, in front of a door quite unlike the others. This one has a wooden frame, nicely sculpted and sporting various decorations."

    t "Just try to stay level headed with Mr.J and you'll be A-Okay."

    "The hyena turns around as if to walk away, before squatting and whispering to my ear."

    t "Literally level-headed, if you catch my drift, shorty."

    hide tom
    with dissolve

    "Tom finally slaps my back rather strongly and walks away, whistling quite a jazzy tune."

    r "Okay... Deep breaths..."

    "I finally muster up my courage and lift my fist up, knocking as confidently on the victorian door as I can muster."

    "*KNOCK KNOCK KNOCK*"

    "After a few seconds, a voice finally answers from beyond the doors."

    w "Come in."

    # Se abre la puerta, entramos, esta Mikki en el escritorio y nos invita a sentarnos

    "I push gently on the door, opening it quite easily to my surprise"

    r "Huh, deceptively light."

    show mikki at center, half_height
    with dissolve

    m "So, you are the newest intern, the scholarship one."

    m "You seem like quite a promising one, provided you haven't skillfuly forged these academic records."

    "I'm sort of taken aback by the cat's sudden suggestion, before letting out a small nervous chuckle"

    r "Oh no no, ahaha...ha, I would never. Wouldn't have the skills for sucha a task either"

    m "Not with that attitude you don't"

    # This ends the world. The world ends with you. This is your end.

    return

