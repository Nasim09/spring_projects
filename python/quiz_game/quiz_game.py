print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": 
    quit()

print("Okay! Let's play! :)")
score = 0

question1_answers = ["central prcoessing unit", "cpu"]

answer = input("What does CPU stand for? ").lower()
#if answer == "central processing unit" + "cpu":
if answer in question1_answers:
    print('Correct! ')
    score += 1
    score = score + 1
else:
    print("Incorrect!")

question2_answers = ["graphics processing unit", "gpu"]

answer = input("What does GPU stand for? ").lower()
if answer in question2_answers:
    print("Correct!")
    score += 1
    score = score + 1
else:
    print("Incorrect! ")

question3_answers = ["random access memory", "ram"]

answer = input("Whats does RAM stand for? ").lower()
if answer in question3_answers:
    print("Correct! ")
    score += 1
    score = score + 1
else: 
    print("Incorrect!")

question4_answers = ["power supply"]

answer = input("What does PSU stand for? ").lower()
if answer in question4_answers:
    print("Correct! ")
    score += 1
    score = score + 1
else: 
    print("Incorrect! ") 

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.") 