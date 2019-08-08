#!/usr/bin/env python3

# all possible words
words = ["about", "after", "again", "below", "could", "every", "first", "found", "great", "house", "large", "learn",
         "never", "other", "place", "plant", "point", "right", "small", "sound", "spell", "still", "study", "their",
         "there", "these", "thing", "think", "three", "water", "where", "which", "world", "would", "write"]

# get input from user
first = input("Input first column: \033[94m")
second = input("\033[0mInput second column: \033[94m")
third = input("\033[0mInput third column: \033[94m")
print("\033[0m")

# parse it
first = first.split(" ")
second = second.split(" ")
solve = []

# solve it
for word in words:
    if word[0] in first:
        if word[1] in second:
            if word[2] in third:
                solve.append(word)

# print all possible solutions
print("Possible solutions: " + "\033[92m" + ' '.join(solve) + "\033[0m")
