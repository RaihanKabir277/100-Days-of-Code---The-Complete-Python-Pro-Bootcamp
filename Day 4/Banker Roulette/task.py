import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))

last_index = len(friends)

random_index = random.randint(0, last_index-1)

print(friends[random_index])