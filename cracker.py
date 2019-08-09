#!/usr/bin/env python3

# all possible words
words = ["about", "after", "again", "below", "could", "every", "first", "found", "great", "house", "large", "learn",
         "never", "other", "place", "plant", "point", "right", "small", "sound", "spell", "still", "study", "their",
         "there", "these", "thing", "think", "three", "water", "where", "which", "world", "would", "write"]

# get input from user and parse it
first = input("Input\033[1m first\033[0m column: \033[94m").split(" ")
third = input("\033[0mInput\033[1m third\033[0m column: \033[94m").split(" ")
fifth = input("\033[0mInput\033[1m fifth\033[0m column: \033[94m").split(" ")
print("\033[0m")

# solve it
solve = []
for word in words:
    if word[0] in first:
        if word[2] in third:
            if word[4] in fifth:
                solve.append(word)

# print all possible solutions
print("Possible solutions: " + "\033[92m" + ", ".join(solve) + "\033[0m")
