import random

health = 50

health_potion = random.randint(10,20)

if health + health_potion > 65:
    print("health capped!")
else:
      print(health + health_potion)
      
