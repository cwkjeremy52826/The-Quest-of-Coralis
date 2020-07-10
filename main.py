Characters = {"A" : "Knight",
              "B" : "Enchanter",
              "C" : "Enchantress",
              "D" : "Elf",
              "E" : "Dwarf",
              "F" : "Archer"}

Begin = {"A" : "begin your journey",
         "B" : "buy suplies"}

Horse = {"A" : "buy a horse",
         "B" : "save your gold"}

Bandits = {"A" : "run",
           "B" : "stay"}

name = input('Hello! What is your name?\t')

ans = input("Welcome to Coralis " + name + ", a world of magic and quests! Do you want to go on an adventure?! Y or N\t")

if ans.upper() == "N":
  print("That makes me sad! But okay :(")
if ans.upper() == "Y":
  print("Then let us begin!")
  cha = input("What type of character would you like to be? Type A if you would like to be a nobel knight, B if you would like to to be a powerful enchanter, C for an incredible enchantress, D if you would like to be a stealthy elf, E if you would like to be a small, digging dwarf, or F if you would like to be an archer with pinpoint aim.\n")
  cha = cha.upper()
  print('Okay ' + name + ' the ' + Characters[cha] + ', are you ready?  Because the King of Coralis has a special mission for you. A disease has broken out and we need you to go to the Mountain of Granduer and find the sacred Rainbow Falls.  There, fill a pitcher of the water, it can cure any illness. Bring it back to the King so we may distribute it across the kingdom, but I must warn you. There are many dangers in the journey ahead of you. Bandits will attempt to steal from you on the road, climbing the mountain will be no easy feat, and there is legend of a magnifacent beast that guards Rainbow Falls. Well! You are ready to be on your way! Here is 500 gold to get you started! Good luck!\n')
  d1 = input("Your journey has begun! You must make your first choice! Do you just start out on the journey, or do you use your gold to buy suplies? Type A if you would like to just set off or type B if you want to buy suplies.\n")
  d1 = d1.upper()
  if d1 == "A":
    print("you have chosen to " + Begin[d1] + "!\n")
  if d1 == "B":
    print("Alright! Let's go " + Begin[d1] + "!\n")
    print("Okay, you have bought a coin pouch, a satchel, climbing meterials, a cloak, a water flask, and the pitcher. This cost you 215 gold.")
    d2 = input("But you have another decision to make. Would you like to buy a horse for 200 gold. This will reduce your travel time to the mountain by 1 1/2 days but you will not be able to bring it up the mountain. Type A if you would like to buy the horse and type B if you would like to save your gold.\n")
    d2 = d2.upper()
    if d2 == "A":
      print("You have chosen to " + Horse[d2] + "! Now lets hit the road.\n")
  print("You have left the city and all around you are green rolling hills. The journey goes quickly for the first day before you set up camp. You wake up the next morning and immediately hit the road again, but as you travel a thundering noise reaches your ears. As the sound gets louder you see 4 men clad in black riding towards you on scrawny looking horses, weapons raised.")
  if d2 == "A":
    d3 = input('Do you try to out run them on your horse or do you stay and see who those riders are? Type A if you want to run or type b if you want to stay.\n')
    d3 = d3.upper()
  else:
    print("You know you have no chance of running so you stop walking and turn towards the riders. As they near you recognize them for bandits")
  if d3 == "A":
      print("You are able to out run the men and get to safety. You made the right choice by " + Bandits[d3] + "ning. Those men were bandits who raid travelers every single day.")