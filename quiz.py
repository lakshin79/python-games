print("TRICKY QUIZ !!")

playing = input("Do you want to play?(yes/no) ")

if playing.lower() == "yes":
   print("LET'S BEGIN")
   score=0

   ans = input("What does JSON stands for? ")
   if ans.lower() == "javascript object notation":
      print("Correct !!")
      score+=1
   else:
      print("Wrong !!")

   ans = input("What does SPV stands for? ")
   if ans.lower() == "simple payment verification":
      print("Correct !!")
      score+=1
   else:
      print("Wrong !!")

   ans = input("What does ROM stands for? ")
   if ans.lower() == "read only memory":
      print("Correct !!")
      score+=1
   else:
      print("Wrong !!")

   ans = input("What does RAM stands for? ")
   if ans.lower() == "random access memory":
      print("Correct !!")
      score+=1
   else:
      print("Wrong !!")

   print("Your score : " + str(score) + " out of 4")

   if score == 0:
      print("BETTER LUCK NEXT TIME BUDDY :)")
   elif ((score == 1) or (score == 2)):
      print("Not bad")
   elif score == 3:
      print("Almost you are there !!")
   else:
      print("YOU GENIUS !!")
 

elif playing.lower()=="no":
   quit()

else:
   print("Kindly enter a valid input")
   quit()


     