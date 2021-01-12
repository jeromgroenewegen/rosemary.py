# How many?
x = 16

# Assemble utensils and ingredients
from kitchen import Rosemary
from kitchen.utensils import Bowl, BakingTray, Fridge, Oven, Plate
from kitchen.ingredients import Butter, Sugar, Egg, Salt, Flour, ChocolateChips, BakingPowder

# Preheat oven
oven = Oven.use(degrees = 175)

# Add and mix ingredients
bowl = Bowl.use(name = 'batter')
bowl.add(Butter.take(grams = (100/16)*x))
for i in range(4):
    bowl.add(Sugar.take(grams = (50/16)*x))
    bowl.mix()
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
    bowl.mix()
bowl.add(Salt.take('pinch'))
for i in range(10):
    bowl.add(Flour.take(grams = (30/16)*x))
    bowl.add(ChocolateChips.take(grams = x))
    bowl.mix()
bowl.add(BakingPowder.take('some'))
bowl.mix()

#Baking
tray = BakingTray.use(name = 'cookies')
for i in range(16):
    tray.add(bowl.take(f'1/{x}'))
oven.add(tray)
oven.bake(minutes = 10)

# Serving the cookies
plate = Plate.use()
cookies = tray.take()

plate.add(cookies)

Rosemary.serve(plate)