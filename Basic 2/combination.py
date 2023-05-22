players=['sakib','tamim','musfiq']
age=[37,38,39]
age_combo=[]
# for player in players:
#     print(player)
#     for ag in age:
#         # print(player,ag)
#         age_combo.append([player,ag])
# print(age_combo)
age_combo2=[[player,ag] for player in players for ag in age]
print(age_combo2)
# []-->list ()-->tuple
""" 
import numpy as np

# Simulating throwing a fair coin
num_throw = 1000

# Generate random outcomes (0: tails, 1: heads)
coin_throws = np.random.randint(0, 2, num_throw)

# Count the number of heads and tails
num_heads = np.count_nonzero(coin_throws)
num_tails = num_throw - num_heads

# Calculate the probabilities
prob_heads = num_heads / num_throw
prob_tails = num_tails / num_throw

# Output the results
print(f"Number of heads: {num_heads}")
print(f"Number of tails: {num_tails}")
print(f"Probability of heads: {prob_heads:.2f}")
print(f"Probability of tails: {prob_tails:.2f}")

"""
""" 
all possible combintion
import itertools

players = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

age_combinations = list(itertools.product(players, ages))

print(age_combinations)

"""