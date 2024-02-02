little_key = False
package = True
sheriff = True
saloon = True
bank = True

print('''
               ▄▄▄█████▓██░ ██▓█████                 
               ▓  ██▒ ▓▓██░ ██▓█   ▀                 
               ▒ ▓██░ ▒▒██▀▀██▒███                   
               ░ ▓██▓ ░░▓█ ░██▒▓█  ▄                 
                 ▒██▒ ░░▓█▒░██░▒████▒                
                 ▒ ░░   ▒ ░░▒░░░ ▒░ ░                
                   ░    ▒ ░▒░ ░░ ░  ░                
                 ░      ░  ░░ ░  ░                   
▓█████▄▓█████ ██▓    ██▓██▒░  █▓█████ ██▀███▓██   ██▓
▒██▀ ██▓█   ▀▓██▒   ▓██▓██░   █▓█   ▀▓██ ▒ ██▒██  ██▒
░██   █▒███  ▒██░   ▒██▒▓██  █▒▒███  ▓██ ░▄█ ▒▒██ ██░
░▓█▄   ▒▓█  ▄▒██░   ░██░ ▒██ █░▒▓█  ▄▒██▀▀█▄  ░ ▐██▓░
░▒████▓░▒████░██████░██░  ▒▀█░ ░▒████░██▓ ▒██▒░ ██▒▓░
 ▒▒▓  ▒░░ ▒░ ░ ▒░▓  ░▓    ░ ▐░ ░░ ▒░ ░ ▒▓ ░▒▓░ ██▒▒▒ 
 ░ ▒  ▒ ░ ░  ░ ░ ▒  ░▒ ░  ░ ░░  ░ ░  ░ ░▒ ░ ▒▓██ ░▒░ 
 ░ ░  ░   ░    ░ ░   ▒ ░    ░░    ░    ░░   ░▒ ▒ ░░  
   ░      ░  ░   ░  ░░       ░    ░  ░  ░    ░ ░     
 ░                          ░                ░ ░     
''')
print("The year is 1899. Your name is Zedediah O'Range. Some say that the good ol' days are over now. You don't care. You only want the paycheck at the end of the day. Maybe the gunslingers time is up, but you're just a simple mercenary minding your own business. It is a day like any other. You've been commissioned to deliver some package to another town. You're on your way to the Saloon where you agreed to pick up the parcel. \nYou see a good looking lady gathering her belongings from a wagon on your way. What do you do? ")
choice1 = input("1.Offer help \n2.Ignore her \n")

if choice1 =="1":
  print("You nonchalantly fix your mustache and cowboy hat. \n-Well look at you, honeybum. You look like you're in a need of a strong man like myself. What do you say I help you and then you help me? \nShe gives you her most disgusted face and says: \n-Arthur, honey, I think this gentleman confused me with someone else. \nThen, from behind the wagon, the biggest bull of a man leans out and pierces a hole in you with his stare. \n-I give you one chance to get the hell out of my sight. \nWhat do you do? \n")
  choice2 = input("1.Run \n2.Fight \n")
  if choice2 == "1":
    print("That was a good decision. You mumble an apology and head straight to the Saloon.")
  else:
    print("You overestimated yourself. Big time. Arthur crushes your bones with his bare hands before you even get a chance to reach your weapon. You are dead. \nGAME OVER")
elif choice1 == "2": 
  print("You're a professional. You don't have time to flirt with ladies. Not when you're on a job. You head straight to the Saloon. \nHow do you enter the premises?")
  choice3 = input("1.Confidently \n2.Sneakily \n")
  if choice3 == "1":
   print("You kick open the door and walk in. You snatch a cigarette from some scared guy sitting near and take the biggest puff. Then you make the nastiest burp this Saloon has ever witnessed.")
  else:
    print("You walk into the Saloon without making any noise. You sneak around people who don't even notice your presence.")
  print("You spot the man you were supposed to meet with. You approach him and without any words he hands you over the package. It's not bigger than your fist, and it's adressed to the town of Dry Springs. There is a big red writing on it that says <DO NOT OPEN>. What do you do?")
  choice4 = input("1.Take it and leave immediately. \n2.Ask questions \n")
  if choice4 == "1":
    print("Professional, clean job. You are known for not asking too many questions. You take the package and leave the Saloon, you get on your Horse - Jolly Jumper - and head straight to Dry Springs.")
  else:
    print("-Where exactly should I leave the package? \nHe answers you with silence. \n-Okay, so you're one of THOSE. - you say and leave. - G'day sir.\nYou leave the Saloon, get on your horse - Jolly Jumper - and head straight to Dry Springs.")
    
  print("You only ever heard legends of Dry Springs. You've never been there yet. You travel for a few days and finally see ruined and loney town. Jolly Jumper starts to get nervous, but you calm him down. \n-I't okay, buddy. - you say. \nDry Springs looks like a ghost town. There is no sign of life, and there are only three buildings, each one of them is ruined. \nFirst one looks like a Sheriff's office. \nSecond one looks like a Saloon. \nThird one looks like a Bank. \nWhere do you go first? (note from dev: To have the best experience I strongly recommend going to the buildings in order,THANKS)")
  choice5 = input("1.Sheriff's Office \n2.Saloon \n3.Bank \n")
  if choice5 == "1":
    sheriff = False
    print("You walk into the Sheriff's office. It's a mess. There are a lot of dead bodies everywhere. At the desk there is a dead man with a sheriff's badge sticking out of his skull. What do you do?")
    choice6 = input("1.Look around for loot \n2.Leave the package on the desk \n3. Leave the building \n")
    if choice6 == "1":
      print("You look around. All the shelves are empty. You look under the desk. There is a small box. You open it. There is a small key inside. You figure it could be a key to some safe. You keep it. You also see a note on the floor, covered in blood. It says: \nI kept my promise. Now you keep yours. Come back for the prize. \nWhat do you do?")
      little_key = True
      choice7 = input("1.Leave the building \n2. Leave the package on the desk \n")
      if choice7 == "1":
        print("There is nothing else to see here. You leave the building. The building collapses behind you.")
      else:
        print("You carefully put the package on the desk, but as soon as you do that, the ceiling starts to crack. The building is going to collapse. You quickly take the package and run out of the Shreiff's Office.")
    elif choice6 == "2":
     print("You carefully put the package on the desk, but as soon as you do that, the ceiling starts to crack. The building is going to collapse. You quickly take the package and run out of the Shreiff's Office.")
    else: 
      print("This place is boring. You leave the building. The building collapses as you leave.")
  elif choice5 == "2":
    saloon = False
    print("You enter the remains of the Saloon. It's a complete bloodbath. Dead bodies everywhere, some of them half-eaten by cayotes. \nWhat do you do?")
    choice8 = input("1.Look around for loot \n2.Leave the package on the bar \n3. Leave the building \n")
    if choice8 == "1":
      print("You take a look around. All of the liquor lottles are shattered. You approach the bar and see a cash register destroyed and empty. Whoever has been here before must have taken everything precious. \nWhat do you do?")
      choice9 = input("1.Leave the building \n2.Leave the package on the bar \n")
      if choice9 == "1":
        print("There is nothing else to see here. You leave the building before you vomit from the stink of death.")
      else:
        print("You decided to leave the package on the bar. You then leave the Saloon")
        package = False
    if choice8 == "2":
      print ("Looks like a place you can leave the package on. Then you leave the Saloon.")
      package = False
    else:
      print("This place is boring. You leave the Saloon.")
      package = True 
  else:
    print("You enter the Bank. There is no one here, but you see a safe. \nWhat do you do?")
    choice10 = input("1.Try to open the safe \n2.Leave the building \n")
    if choice10 == "1":
      if little_key == False:
        print("The safe is massive. You try to open it. It's locked. You need a key. There is nothing more to see, so you leave the Bank.")
      else:
        print("You have a key from sheriff's office! You use it to open the safe. Inside you find a bag full of money. Do you take it?")
        choice11 = input("1.Take the bag \n2.Leave the bag \n")
        if choice11 == "1":
          print("Looks like no one else wants the money. You take the bag.")
        else:
          print("Who are you to steal from a bank? You leave the bag.")
      if package == True:
        print("You think to yourself, that maybe you should leave the package in the safe. Do you do that?")  
        choice12 = input("1.Leave the package \n2.Don't leave the package and leave the Bank \n")
        if choice12 == "1":
          package = False
          print("You leave the package in the safe. You then leave the Bank.")
        else:
          print("You leave the Bank.")
          
    if choice10 == "2":
      print("You're getting the hell out of here.")

  print("What do you do next?")
  if sheriff == False:
    choice13 = input("1.Go to the Saloon \n2.Go to the Bank \n")
    if choice13 == "1":
      saloon = False
      print("You enter the remains of the Saloon. It's a complete bloodbath. Dead bodies everywhere, some of them half-eaten by cayotes. \nWhat do you do?")
      choice8 = input("1.Look around for loot \n2.Leave the package on the bar \n3. Leave the building \n")
      if choice8 == "1":
        print("You take a look around. All of the liquor lottles are shattered. You approach the bar and see a cash register destroyed and empty. Whoever has been here before must have taken everything precious. \nWhat do you do?")
        choice9 = input("1.Leave the building \n2.Leave the package on the bar \n")
        if choice9 == "1":
          print("There is nothing else to see here. You leave the building before you vomit from the stink of death.")
        else:
          print("You decided to leave the package on the bar. You then leave the Saloon")
          package = False
      if choice8 == "2":
        print ("Looks like a place you can leave the package on. Then you leave the Saloon.")
        package = False
      elif choice8 == "3":
        print("This place is boring. You leave the Saloon.")
        package = True 
  
  print("What do you do next?")
  choice13 = input("1.Go to the Bank \n")
  if choice13 == "1":
    print("You enter the Bank. There is no one here, but you see a safe. \nWhat do you do?")
    choice10 = input("1.Try to open the safe \n2.Leave the building \n")
    if choice10 == "1":
      if little_key == False:
        print("The safe is massive. You try to open it. It's locked. You need a key. There is nothing more to see, so you leave the Bank.")
      else:
        print("You have a key from sheriff's office! You use it to open the safe. Inside you find a bag full of money. Do you take it?")
        choice11 = input("1.Take the bag \n2.Leave the bag \n")
        if choice11 == "1":
          print("Looks like no one else wants the money. You take the bag.")
        else:
              print("Who are you to steal from a bank? You leave the bag.")
    if package == True:
      print("You think to yourself, that maybe you should leave the package in the safe. Do you do that?")  
      choice12 = input("1.Leave the package \n2.Don't leave the package and leave the Bank \n")
      if choice12 == "1":
        package = False
        print("You leave the package in the safe. You then leave the Bank.")
      else:
        print("You leave the Bank.")
    else:
      print("You leave the Bank.")    

    if choice10 == "2":
      print("You're getting the hell out of here.")

  if package == True:
    print("You explored the town. But you still have a package and no idea what to do with it. You break down and open the package. It's a bomb. It explodes to your face and you die. They say the curiosity is the first step to hell, and you've just entered. \nGAME OVER")
  else:
    print("You explored the town, but you still have no idea what is going on. As you left the package in Dry Springs, you fulfilled the contract. You head back to your town. Another day, another slay. \nGAME OVER")
    
    
      
      
      