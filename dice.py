import random

def roll_dice():
    return random.randint(1, 6)

# Initialize a dictionary to store the counts of each possible sum
sum_counts = {sum_val: 0 for sum_val in range(2, 13)}

# Simulate rolling the dice 100 times
num_rolls = 100
for _ in range(num_rolls):
    die1 = roll_dice()
    die2 = roll_dice()
    total_sum = die1 + die2
    sum_counts[total_sum] += 1

# Print the results in a tabular format
print("Sum\tCount")
print("-------------")
for sum_val, count in sum_counts.items():
    print(f"{sum_val}\t{count}")
