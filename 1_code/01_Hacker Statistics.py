# HACKER STATISTICS

# use hacker statistics to calculate your chances of winning a bet.

# Random numbers
# Play a dice game of climbing 100 steps of the Emprire Tower with your friend. Throw it 100 times. 
# If it's 1 or 2, you go down one step.
# If it's 3, 4 or 5, you'll go up one step.
# If it's a 6, you'll throw the dice again and walk up the resulting number of steps.
# You can not go lower than the ground level.
# You might have 0.1% chance to fall from the tower and start over again.
# Make a bet that you'll reach 60 steps after 100 time rolling the dice.
# Simulate the process thousands of time and see what's the probability you'll reach 60 steps.

# Random generators
# Import the Random sub-package from Numpy 
import numpy as np
# rand(): if you don't specify any arguments, it generates a random float between 0 and 1.
np.random.rand()
# Python generates pseudo-random numbers starting from a random seed.
# seed(): sets the random seed, so that your results are reproducible between simulations. 
np.random.seed(123)
np.random.rand()
np.random.rand() # result another number.
# Simulate a coin toss game
coin = np.random.randint(0, 2)
# randint(): randomly generates integers.
print(coin)
if coin == 0:
    print("heads")
else:
    print("tails")
# Simulate a dice
print(np.random.randint(1, 7))
# Roll the dice again
print(np.random.randint(1, 7))
# Suppose you're at the middle of the Empire Tower
step = 50
# Roll the dice
dice = np.random.randint(1, 7)
if dice <= 2:
    step = step - 1
elif dice <= 5:
    step = step + 1
else:
   step = step + np.random.randint(1, 7)
print(dice)
print(step)

# Random walk
# To record every step in a random walk, build a list with a for loop.
outcomes = [] # initialize an empty list
for x in range(10):  # run 10 times
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append("head")
    else:
        outcomes.append("tails")
print(outcomes) # this list is just a bunch of random steps, not a random walk.
# Create another list starting with 0
tails = [0]
for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)
print(tails) # this list tells how often tails appeared.
# Initialize a random walk for the dice game
random_walk = [0]
for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1, 7)
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)
    random_walk.append(step)
print(random_walk) 
# The result contains some minus steps. Fix this with max()
for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1, 7)
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)
    random_walk.append(step)
print(random_walk)
# Visualize the random walk with pyplot from matplotlib package
import matplotlib.pyplot as plt
plt.plot(random_walk)
plt.show()

# Distribution
# Each random walk will end up in a different final steps. Simulating this walk 1000 times will result 10000 final steps.
# Once we know the distribution of final steps, we can start calculating chances.
# E.g, increase the throw times of the coin toss game
final_tails = [0]
for x in range(100):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
print(final_tails) # each value represents the number tails appear every 10 tosses.
# All these values represent a distribution. Visualize it with histogram
plt.hist(final_tails, bins = 10)
plt.show() # reveals the distribution shape, but not yet smooth.
# Simulate the coin toss game 1000 times
final_tails = [0]
for x in range(1000):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
plt.hist(final_tails, bins = 10)
plt.show() # looks smoother
# Change the code to 10000 times of simulation
final_tails = [0]
for x in range(10000):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
plt.hist(final_tails, bins = 10)
plt.show() # the distribution starts to converge to a bell-shape like thereotical distribution.

# Simulate multiple walks
all_walks = []
for i in range(10):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step -1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        random_walk.append(step)
    all_walks.append(random_walk)
print(all_walks)
# Convert all_walks to Numpy array:
np_aw = np.array(all_walks)
# Plot and show
plt.plot(np_aw)
plt.show() # the plot does not look right, because all_walks is a list of lists.
# Transpose np_aw to convert the sub-lists into Numpy arrays, too. 
np_aw_t = np.transpose(np_aw) 
# Clear the previous plot and plot it again
plt.clf()
plt.plot(np_aw_t)
plt.show() # now every row in np_all_walks represents the position after 1 throw for the 10 random walks.
# There is still 0.1% of falling down. That calls for another random number generation.
# Generate a random float between 0 and 1. If this value is less than or equal to 0.001, you should reset step to 0.
all_walks = []
for i in range(250):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step -1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        if np.random.rand() <= 0.001: 
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show() # the plot shows you actually could fall a couple of times.
# Simulate the random walk 500 times
all_walks = []
for i in range(250):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step -1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        if np.random.rand() <= 0.001: 
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
np_aw_t = np.transpose(np.array(all_walks))
# Select the last row that contains the endpoint of all 500 random walks you've simulated. 
ends = np_aw_t[-1, :]
# Build a histogram to display the distribution of the end points
plt.hist(ends)
plt.show()