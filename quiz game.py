print("Welcome to my computer")
response = input("Do you want to play quiz ? ")

if response.lower() !=  "yes":
    quit()

print("letss Playy")
score = 0
ans = input("what does CPU stands for ?")
if ans.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect")
ans = input("what does GPU stands for ?")
if ans.lower() == "graphical processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect")
ans = input("what does OS stands for ?")
if ans.lower() == "operating system":
    print("Correct!")
    score+=1
else:
    print("Incorrect")
ans = input("what does RAM stands for ?")
if ans.lower() == "rando access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect")
print("You scored "+str(score)+ " in quizz" )
