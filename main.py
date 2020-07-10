Characters = {"A" : "Knight",
              "B" : "Enchanter",
              "C" : "Enchantress",
              "D" : "Elf",
              "E" : "Dwarf",
              "F" : "Archer"}

Begin = {"A" : "begin your journey",
         "B" : "buy suplies"}

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
    d2 = input("But you have another decition to make. Would you like to but a horse for 200 gold. this")