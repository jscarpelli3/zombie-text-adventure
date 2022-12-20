# Create your own adventure with python here


# Story Setup.  Choice Point 1
def setup():
    print("-------------------------->\nZombies are swarming your neighborhood do you fight through them and try to escape your area, or stay inside and hide?")
    fight_or_hide = input(
        "\n\n\x1B[3mWill you fight or hide? (type 'fight' or 'hide' to continue) - \x1B[0m")
    if fight_or_hide == "fight" or fight_or_hide == "hide":
        start_adventure(fight_or_hide)
    else:
        setup()

# Choice Point 2A


def start_adventure(fight_or_hide):
    if fight_or_hide == "fight":
        print("\n-------------------------->\nYou grab a back pack of supplies and bat. You wrap some barbed wire around the fat end and head out. At first there aren't many zombies.  So it's easy to take them out one by one.  But all the sudden you hear cries for help from the alley.  Out runs a young kid begging you to help protect him.  Do you take him with you or do you tell him to run home?")
        a_take_or_leave = input(
            "\n\n\x1B[3mWill you take the kid with you or leave him? (type 'take' or 'leave' to continue) - \x1B[0m")
        if a_take_or_leave == "take" or a_take_or_leave == "leave":
            take_or_leave_fn(a_take_or_leave)
        else:
            start_adventure(fight_or_hide)
    elif fight_or_hide == "hide":
        print("\n-------------------------->\nYou quickly grab anything you can to barricade the windows and doors and you make sure to stay quiet.  All the sudden someone is banging on your door... a live human.  You look out and see a young kid.  Do you let him in or turn him away?")
        b_letin_or_shutout = input(
            "\n\n\x1B[3mWill you let the kid in or shut him out? (type 'let in' or 'shut out' to continue) - \x1B[0m")
        if b_letin_or_shutout == "let in" or b_letin_or_shutout == "shut out":
            letin_or_shutout(b_letin_or_shutout)
        else:
            start_adventure(fight_or_hide)


# Choice Point 3A1
# Following the FIGHT setup
def take_or_leave_fn(a_take_or_leave):
    if a_take_or_leave == "take":
        print("\n-------------------------->\nYou tell the kid to come along and stay behind you as you figh through zombies.  More and more zombies arrive causeing you to trip and fall as you attempt to fight them from 2 sides.  Do you demand that the kid come help you or do you throw him your bat and tell him to save himself?")
        a1_demandhelp_or_givebat = input(
            "\n\n\x1B[3m Will you demand help or give him your bat so he can save himself? (type 'demand' or 'give' continue) - \x1B[0m")
        if a1_demandhelp_or_givebat == "demand" or a1_demandhelp_or_givebat == "give":
            you_fall(a1_demandhelp_or_givebat)
        else:
            take_or_leave_fn(a_take_or_leave)
    elif a_take_or_leave == "leave":
        print("\n-------------------------->\nYou leave kid behind.  He's on his own.  Suddenly, many more Zombies descend up on you so you make a break for the nearest house. You bust a window and hop in to safety.  Turns out it's the kid's house. His parents are in there. Do you threaten them and force them into a room so that they don't know what you just did?  Or do you apologize?")
        a2_threaten_or_apologize = input(
            "\n\n\x1B[3mWill you threaten them to avoid taking responsibility for leaving their son to the zombies or will you apologize profusely? (type 'threaten' or 'apologize' continue) - \x1B[0m")
        if a2_threaten_or_apologize == "threaten" or a2_threaten_or_apologize == "apologize":
            deal_with_fam(a2_threaten_or_apologize)
        else:
            take_or_leave_fn(a_take_or_leave)


# Following DEMAND or GIVE BAT (Prints Result #1 or #2)
def you_fall(a1_demandhelp_or_givebat):
    if a1_demandhelp_or_givebat == "demand":
        print("\n-------------------------->\nYou demand he come help you.  So he rushes over but as he gets near you, a couple zombies grab him and he's gone, giving you a chance to run back to your home.  You live, but guilt ruins the rest of your life")
        restart = input(
            "\n\n\x1B[3mWould you like to restart the adventure? ('y' or 'n') - \x1B[0m")
        restrt(restart)
    elif a1_demandhelp_or_givebat == "give":
        print("\n-------------------------->\nYou toss him your bat and tell him to save himself.  Your last sight is the disgusting mouth of a zombie as it begins to rip into your neck.  But your last thought is that kid safe and sound back at home.")
        restart = input(
            "\n\n\x1B[3mWould you like to restart the adventure? ('y' or 'n') - \x1B[0m")
        restrt(restart)

# FOLLOWING Threaten or Apologize (Prints Result #3 or #4)


def deal_with_fam(threaten_or_apologize):
    if threaten_or_apologize == "threaten":
        print("-------------------------->\nYou're scared and so you threaten the family with your bat.  The mom is a jui jitsu black belt and beats the crap out of you with your own bat.  Then heads out to rescue her son.")
        restart = input(
            "\n\n\x1B[3mWould you like to restart the adventure? ('y' or 'n') - \x1B[0m")
        restrt(restart)
    elif threaten_or_apologize == "apologize":
        print("-------------------------->\nYou apologize for leaving their son behind and vow to go rescue  him.  The mother joins you and you both find him hiding in a garbage can.  After which the mother cracks you across the head with your own bat.  You live... but you have a concussion you'll never recover from.")
        restart = input(
            "\n\n\x1B[3mWould you like to restart the adventure? ('y' or 'n') - \x1B[0m")
        restrt(restart)


# FOLLOWING the HIDE Setup
def letin_or_shutout(letShut):
    if letShut == "let in":
        print("\n-------------------------->\nThe kid is scarred and is crying loudly. It's drawing the attention of the zombies.  Do you throw him out and tell him he needs to go find his parents or keep him calm and pomise him you'll help him find his parents later?")
        b1_throwout_or_calmdown = input(
            "\n\n\x1B[3mWill you throw the kid out because he is a risk or will you calm him down? (type 'throw out' or 'calm down' continue) - \x1B[0m")
        if b1_throwout_or_calmdown == "throw out" or b1_throwout_or_calmdown == "calm down":
            throwout_calmdown(b1_throwout_or_calmdown)
        else:
            letin_or_shutout(letShut)
    if letShut == "shut out":
        print("\n-------------------------->\nThe kid finally leaves your porch and gets swarmed immediately.  Do you go help him or stay safe inside?")
        b2_gohelp_or_staysafe = input(
            "\n\n\x1B[3mWill you risk your life to go safe him or stay save inside? (type 'go help' or 'stay safe' continue) - \x1B[0m")
        if b2_gohelp_or_staysafe == "go help" or b2_gohelp_or_staysafe == "stay safe":
            help_or_safe(b2_gohelp_or_staysafe)
        else:
            letin_or_shutout(letShut)

# FOLLOWING THROWOUT or CALM (Prints Result #5 or #6)


def throwout_calmdown(throw_calm):
    if throw_calm == "throw out":
        print("\n-------------------------->\nYou throw the kid out because he is risking your safety.  A swarm of zombies go after him and you live the rest of your life with the guilt of never knowing if he made it home")
        restart = input(
            "\n\n\x1B[3mWould you like to restart the adventure? ('y' or 'n') - \x1B[0m")
        restrt(restart)
    elif throw_calm == "calm down":
        print("\n-------------------------->\nYou calm the kid down with some positive talk and a promise that after the zombies move on you will help him reunite with his family.  He calms down, you ride out the hordes and then get him home the next morning.")
        restart = input(
            "\n\n\x1B[3mWould you like to restart the adventure? ('y' or 'n') - \x1B[0m")
        restrt(restart)


def help_or_safe(gohelp_staysafe):
    if gohelp_staysafe == "go help":
        print("\n-------------------------->\nYou run outside to help him just in time.  After dispatching the nearest zombies you grab him and take him inside.  He is grateful at first, but then yells at you for not letting him inside earlier.  He slaps you across the face.")
        restart = input(
            "\n\n\x1B[3mWould you like to restart the adventure? ('y' or 'n') - \x1B[0m")
        restrt(restart)
    elif gohelp_staysafe == "stay safe":
        print("\n-------------------------->\nYou watch him get taken by zombies.  You are safe.. but the guilt is crushing. In a stupor of self loathing you wander outside and sacrifice yourself to the horde and just before you go unconcious... you see the boy running away... he made it.  You saved him by distracting the zombies.")
        restart = input(
            "\n\n\x1B[3mWould you like to restart the adventure? ('y' or 'n') - \x1B[0m")
        restrt(restart)

# \x1B[3m \x1B[0m


def restrt(restart):
    if restart == "y":
        setup()
    elif restart == "n":
        print("\n-------------------------->\nOk Bye!")
    else:
        print("\n-------------------------->\nall you had to do was type one letter and you FAILED... so.... bye.")


# START ADVENTURE on Line 3
setup()


# # Zombies are swarming your neighborhood do you fight through them and try to escape your area, or stay inside and hide?

# fight_or_hide = ""

# # a - You try to escape by fighting (fight_or_hide is "fight")
# # You grab a back pack of supplies and bat. You wrap some barbed wire around the fat end and head out. At first there aren't many zombies.  So it's easy to take them out one by one.  But all the sudden you hear cries for help from the alley.  Out runs a young kid begging you to help protect him.  Do you take him with you or do you tell hiim to run home?

# a_take_or_leave = ""

# # b - You choose to stay home and hide (fight_or_hide is "hide")
# # You quickly grab anything you can to barricade the windows and doors and you make sure to stay quiet.  All the sudden someone is banging on your door... a live human.  You look out and see a young kid.  Do you let him in or turn hium away?

# b_letin_or_shutout = ""

# # a-1 You take the kid with you (a_take_or_leave is "take")
# # You tell the kid to come along and stay behind you as you figh through zombies.  More and more zombies arrive causeing you to trip and fall as you attempt to fight them from 2 sides.  Do you demand that the kid come help you or do you throw him your bat and tell him to save hiimself?

# a1_demandhelp_or_givebat = ""

# # a-2 You turned away the kind (a_take_or_leave is "leave")
# # You leave kid behind.  He's on his own.  So many more Zombies are coming that you make a break for the nearest house and bust a window to get in.  Turns out it's the kid's house. His parents are in there. Do you threaten them and force them into a room so that they don't know what you just did?  Or do you apologize?

# a2_threaten_or_apologize = ""

# # b-1 You let the kid in (letin_or_shutout is "let in")
# # The kid is scarred and is crying loudly. It's drawing the attention of the zombies.  Do you throw him out and tell hiim he needs to go find his parents or keep him calm and pomise him you'll help him find his parents later?

# b1_throwout_or_calmdown = ""

# # b-2 You shut the kid out (letin_or_shutout is "shutout")
# # The kid finally leaves your porch and gets swarmed immediately.  Do you go help him or stay safe inside?

# b2_gohelp_or_staysafe = ""

# # demandhelp
# a1_res1 = "You demand he come help you.  So he rushes over a couple zombies grab him and he's gone, giving you a chance to run back to your home"

# # givebat
# a1_res2 = "You toss him your bat and tell him to save himself.  Your last sight is the disgusting mouth of a zombie as it begins to rip into your neck.  But your last thought is that kid safe and sound back at home."

# # threaten
# a2_res1 = "You're scared and so you threaten the family with your bat.  The mom is a jui jitsu black belt and beats the crap out of you with your own bat.  Then heads out to rescue her son."

# # apologize
# a2_res2 = "You apologize for leaving their son behind and vow to go rescue him.  The mother joins you and you both find him hiding in a garbage can.  After which the mother crazks you across the head with your own bat.  You live... but you have a concussion you'll never recover from."

# # throwout
# b1_res1 = "You throw the kid out because he is risking your safety.  A swarm of zombies go after him and you live the rest of your life with the guilt of never knowing if he made it home"

# # calmdown
# b1_res2 = "You calm the kid down with some positive talk and a promise that after the zombies move on you will help him reunite with his family.  He calms down, you ride out the hordes and then get him home the next morning."

# b2_res1 = "You run outside to help him just in time.  After dispatching the nearest zombies you grab him and take him inside.  He is grateful at first, but then yells at you for not letting him inside earlier.  He slaps you across the face."

# b2_res2 = "You watch him get taken by zombies.  You are safe.. but the guilt is crushing.  In a stupor of self loathing you wander outside and sacrifice yourself to the horde and just before you go unconcious... you see the boy running away... he made it.  You saved him by distracting the zombies."
