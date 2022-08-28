
print("Welcome to my computer game")
questions = ["ques1", "ques2", "ques3"]

for q in questions:

  playing = input("do you want to play? ").lower()
  if playing != "yes":
    quit()
    print("okay lets play:)")
    Score = 0


  ques1 =input("what does CPU stand for ? ").lower()
  if ques1 == "central processing unit":
    print ("correct ")
    Score += 1
  else:
    print("INcorrect")
  
  
  ques2 =input("what does GPU stand for ? ").lower()
  if ques2 == "Graphic processing unit":
    print ("correct ")
    Score += 1
  else:
    print("INcorrect")
  
  ques3 =input("what does PSU stand for ? ").lower()
  if ques3 == "Power Supply unit":
    print ("correct ")
    Score += 1
  else:
    print("INcorrect")
  
print("you've got "+ str(Score) + " questions correct")
playagain = input("do you want to play again ").lower()
if playagain != "yes":
  quit()
  print("come lets play")
else:
  print("bye bye")
  # quit()
  

  
    
  
  
  
  
