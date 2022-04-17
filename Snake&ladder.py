import random
Ladder = {1: 38, 4: 14, 8: 31, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99} 
snake= {32: 10, 34: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78}
pos1 = 0
pos2 = 0
def move (pos):
    dice = random.randint(1,6)
    print(f"Dice: {dice}")
    pos= pos + dice
    if pos in snake:
        print("Bitten By snake")
        pos=snake[pos]
        print(f"Position:{pos}")
    elif pos in Ladder:
        print("Climbed by Ladder")
        pos = Ladder[pos]
        print(f"Position:{pos}")
    else :
        print(f"Position:{pos}")
    print("/n")
    return pos
             
while True:
   A = input("Player 1 Enter \"A\" to throw dice: ")
   pos1= move (pos1)
   if pos1 >= 100:
       print("Game Over!!!\nPlayer 1 Wins.")
       break
    
   B = input("Player 2 Enter \"B\" to throw dice: ")
   pos2= move (pos2)
   if pos2 >= 100:
       print("Game Over!!!\nPlayer 2 Wins.")
       break
    
 
