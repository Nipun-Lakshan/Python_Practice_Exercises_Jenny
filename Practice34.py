# Coding Exercise 10
print()
print("Love Calculator")
print("===============")
print()
name_1 = input("Enter Boy's Name  :- ")
name_2 = input("Enter Girl's Name :- ")
name = (name_1 + " + " + name_2).lower()
print()
true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love = name.count("l") + name.count("o") + name.count("v") + name.count("e")
love_score = int(str(true) + str(love))
if (love_score < 10 or love_score > 90):
    print(
        f"Your score is {love_score} and you go together like coke and mentos!"
    )
elif (love_score >= 40 and love_score <= 50):
    print(f"Your score is {love_score} and you are alright together!")
else:
    print(f"Your score is {love_score}!")
