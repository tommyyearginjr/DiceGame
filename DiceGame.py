import random
import sys
import os

# Clear the screen at start of game. (The following works with Ubuntu; appears elsewhere in code.)
os.system('clear')

# Create a single die with six sides, labled 1-6.
die01 = list()
for side in range(1,7):
    die01.append(side)

# Roll the die 5 times, and save the results to a list called 'hand'.
hand = list()
for roll in range(0,5):
    rollOutcome = random.choice(die01)
    hand.append(rollOutcome)

# Print out the results of the hand.
sys.stdout.write('RESULTS\t\t')
for outcome in hand:
    sys.stdout.write(str(outcome) + '\t')
print('\n')
sys.stdout.write('DISCARD?\t')
for integer in range(0,5):
    sys.stdout.write(str(integer + 1) + '\t')
print('\n')

# Create a way to discard rolls, and to re-roll and display the final results.
discard = raw_input('Enter which rolls to discard, if any, and press enter. Numbers only; no spaces or punctuation!! ("123", e.g.) ')
discardList = list()
for i in discard:
    discardList.append(i)
print(discardList)
os.system('clear')
for i in discardList:
    i = int(i)
    i = i - 1
    hand[i] = random.choice(die01)
sys.stdout.write('FINAL RESULTS\t\t')
for outcome in hand:
    sys.stdout.write(str(outcome) + '\t')
print('\n')
