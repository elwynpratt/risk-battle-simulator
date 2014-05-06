### Intro and queries ###
print
print
print "Welcome to the Risk Play-By-Play Simulator"
print
while True:
	legit_number = 1
	attacker_number_response = raw_input("Enter attacker's force size: ")
	try:
		i = float(attacker_number_response)
	except ValueError, TypeError:
		print
		print "Please enter a valid number."
		legit_number = 0
	if legit_number == 1:
		if int(attacker_number_response) == 1:
			print
			print "You cannot attack with an army of one."
		elif int(attacker_number_response) < 1:
			print
			print "Please enter a valid response."
		else:
			attacker_number = int(attacker_number_response)
			break
	else:
		pass
	print
print
while True:
	attacker_stronghold_query = raw_input("Does the attacker occupy a stronghold? ").lower()
	if attacker_stronghold_query == "yes" or attacker_stronghold_query == "y":
		break
	if attacker_stronghold_query == "no" or attacker_stronghold_query == "n":
		break
	else:
		print
		print "Please enter a valid response."
		print
print
while True:
	attacker_capitol_query = raw_input("Attacking from capitol? ").lower()
	if attacker_capitol_query == "yes" or attacker_capitol_query == "y":
		break
	if attacker_capitol_query == "no" or attacker_capitol_query == "n":
		break
	else:
		print
		print "Please enter a valid response."
		print
print
while True:
	legit_number = 1
	defender_number_response = raw_input("Enter defender's force size: ")
	try:
		i = float(defender_number_response)
	except ValueError, TypeError:
		print
		print "Please enter a valid number."
		legit_number = 0
	if legit_number == 1:
		if int(defender_number_response) < 1:
			print
			print "Please enter a valid response."
		else:
			defender_number = int(defender_number_response)
			break
	else:
		pass
	print
print
while True:
	defender_stronghold_query = raw_input("Does the defender occupy a stronghold? ").lower()
	if defender_stronghold_query == "yes" or defender_stronghold_query == "y":
		break
	if defender_stronghold_query == "no" or defender_stronghold_query == "n":
		break
	else:
		print
		print "Please enter a valid response."
		print
print
while True:
	defender_capitol_query = raw_input("Defending from capitol? ").lower()
	if defender_capitol_query == "yes" or defender_capitol_query == "y":
		break
	if defender_capitol_query == "no" or defender_capitol_query == "n":
		break
	else:
		print
		print "Please enter a valid response."
		print
print
### pre-game assignments ###
import random
attacker_advantage = 0
defender_advantage = 0
if attacker_stronghold_query == "yes" or attacker_stronghold_query == "y":
	attacker_advantage = attacker_advantage + 1
if defender_stronghold_query == "yes" or defender_stronghold_query == "y":
	defender_advantage = defender_advantage + 1
if attacker_capitol_query == "yes" or attacker_capitol_query == "y":
	attacker_advantage = attacker_advantage + 1
if defender_capitol_query == "yes" or defender_capitol_query == "y":
	defender_advantage = defender_advantage + 1
attack_dice = 3
defend_dice = 2
### die roll ###
def AttackDieRoll_one():
    roll=int(random.randint(1,6))
    if roll == 1:
        outcome_one = 1
    elif roll == 2:
        outcome_one = 2
    elif roll == 3:
        outcome_one = 3
    elif roll == 4:
        outcome_one = 4
    elif roll == 5:
        outcome_one = 5
    elif roll == 6:
        outcome_one = 6
    return outcome_one
def AttackDieRoll_two():
    roll=int(random.randint(1,6))
    if roll == 1:
        outcome_two = 1
    elif roll == 2:
        outcome_two = 2
    elif roll == 3:
        outcome_two = 3
    elif roll == 4:
        outcome_two = 4
    elif roll == 5:
        outcome_two = 5
    elif roll == 6:
        outcome_two = 6
    return outcome_two
def AttackDieRoll_three():
    roll=int(random.randint(1,6))
    if roll == 1:
        outcome_three = 1
    elif roll == 2:
        outcome_three = 2
    elif roll == 3:
        outcome_three = 3
    elif roll == 4:
        outcome_three = 4
    elif roll == 5:
        outcome_three = 5
    elif roll == 6:
        outcome_three = 6
    return outcome_three
def DefendDieRoll_one():
    roll=int(random.randint(1,6))
    if roll == 1:
        outcome_one = 1
    elif roll == 2:
        outcome_one = 2
    elif roll == 3:
        outcome_one = 3
    elif roll == 4:
        outcome_one = 4
    elif roll == 5:
        outcome_one = 5
    elif roll == 6:
        outcome_one = 6
    return outcome_one
def DefendDieRoll_two():
    roll=int(random.randint(1,6))
    if roll == 1:
        outcome_two = 1
    elif roll == 2:
        outcome_two = 2
    elif roll == 3:
        outcome_two = 3
    elif roll == 4:
        outcome_two = 4
    elif roll == 5:
        outcome_two = 5
    elif roll == 6:
        outcome_two = 6
    return outcome_two
### highest number ###
def Attack_HighestNumber(number_of_die):
	if number_of_die == 3:
		ahn = 0
		roll1 = AttackDieRoll_one()
		ahn = roll1
		roll2 = AttackDieRoll_two()
		if roll2 > ahn:
			ahn = roll2
		else:
			ahn = ahn
		roll3 = AttackDieRoll_three()
		if roll3 > ahn:
			ahn = roll3
		else:
			ahn = ahn
		return ahn + attacker_advantage
	elif number_of_die == 2:
		ahn = 0
		roll1 = AttackDieRoll_one()
		ahn = roll1
		roll2 = AttackDieRoll_two()
		if roll2 > ahn:
			ahn = roll2
		else:
			ahn = ahn
		return ahn + attacker_advantage
	elif number_of_die == 1:
		ahn = 0
		roll1 = AttackDieRoll_one()
		ahn = roll1
		return ahn + attacker_advantage
def Defend_HighestNumber(number_of_die):
	if number_of_die == 2:
		dhn = 0
		roll1 = DefendDieRoll_one()
		dhn = roll1
		roll2 = DefendDieRoll_two()
		if roll2 > dhn:
			dhn = roll2
		else:
			dhn = dhn
		return dhn + defender_advantage
	elif number_of_die == 1:
		dhn = 0
		roll1 = DefendDieRoll_one()
		dhn = roll1
		return dhn + defender_advantage
### Encounter ###
def encounter(attack_diecount, defend_diecount):
	D = Defend_HighestNumber(defend_diecount)
	A = Attack_HighestNumber(attack_diecount)
	if D == A:
		return 0
	elif D > A:
		return 0
	elif D < A:
		return 1
### The Battle ###
print
print "---The Battle---"
print
print "Attacker: %s     Defender: %s" % (str(attacker_number), str(defender_number))
print
raw_input("Press enter to begin attacking ")
print
while True:
	if attacker_number == 3:
		attack_dice = 2
	elif attacker_number == 2:
		attack_dice == 1
	if defender_number == 1:
		defend_dice == 1
	result = encounter(attack_dice, defend_dice)
	if attacker_number == 1 or defender_number == 0:
		attacker_number_final = str(attacker_number)
		defender_number_final = str(defender_number)
		if attacker_number == 1:
			print "Attacker fails. Defender has %s soldiers standing." % (defender_number_final)
			print
			import subprocess
			audio_file = "/Users/elwynpratt/Documents/warhorn.mp3"
			return_code = subprocess.call(["afplay", audio_file])
		if defender_number == 0:
			print "Attacker is victorious with %s soldiers standing." % (attacker_number_final)
			print
			import subprocess
			audio_file = "/Users/elwynpratt/Documents/inceptionbutton.mp3"
			return_code = subprocess.call(["afplay", audio_file])
		break
	elif result == 1:
		defender_number = defender_number - 1
	elif result == 0:
		attacker_number = attacker_number - 1
	print "Attacker: %s     Defender: %s" % (str(attacker_number), str(defender_number))
	print
	raw_input("Press enter to continue attacking ")
	print