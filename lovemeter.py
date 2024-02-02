print("The Love Calculator is calculating your score...")
name1 = input("Enter your first and last name:\n") 
name2 = input("Enter your sweetheart's first and last name:\n") 

combined_names = name1 + name2
lowercase = combined_names.lower()
t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")
first_digit = t + r + u + e 

l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if score < 10:
  print(f"Your score is {score}, you guys suck.")
elif score < 20:
  print(f"Your score is {score}, you go together like coke and menthos.")
elif score < 30:
  print(f"Your score is {score}, you guys should rethink your life.")
elif score < 40:
  print(f"Your score is {score}, you will probably last one day before a disaster.")
elif score < 50:
  print(f"Your score is {score}, you guys can try being friends with benefits.")
elif score < 60:
  print(f"Your score is {score}, look at you two little lovebirds.")
elif score < 70:
  print(f"Your score is {score}, you guys can take a loan together.")
elif score < 80:
  print(f"Your score is {score}, you guys are a match made in heaven.")
elif score < 90:
  print(f"Your score is {score}, aren't you guys married already??.")
else:
  print(f"Your score is {score}, whoa there! Slow down because the flame of your love will set this city on fire.")

