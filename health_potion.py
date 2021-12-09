import random

health = 50

health_potion = random.randint(10,20)

upgrade = health + health_potion

if upgrade >= 70:
    print("health capped!")
else:
      print(upgrade)
      
