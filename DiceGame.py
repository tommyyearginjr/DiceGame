import random
import sys

die01 = list()
hand = list()

# Create a single die with six sides, labled 1-6.
for side in range(1,7):
    die01.append(side)

# Roll the die 5 times, and save the results to a list called 'hand'.
for roll in range(0,5):
    rollOutcome = random.choice(die01)
    hand.append(rollOutcome)

# Print out the results of the hand.
sys.stdout.write('RESULTS\t\t')
for outcome in hand:
    sys.stdout.write(str(outcome) + '\t')
print('\n')

sys.stdout.write('HOLD?\t\t')
for integer in range(0,5):
    sys.stdout.write(str(integer + 1) + '\t')
print('\n')
