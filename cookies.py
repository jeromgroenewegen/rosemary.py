# Assemble utensils and ingredients
from kitchen import Rosemary
from kitchen.utensils import Bowl, BakingTray, Fridge, Oven, Plate
from kitchen.ingredients import Butter, Sugar, Egg, Salt, Flour, ChocolateChips, BakingPowder

# Preheat oven
oven = Oven.use(degrees = 175)

# Add and mix ingredients
bowl = Bowl.use(name = 'batter')
bowl.add(Butter.take(grams = 100))
for i in range(4):
    bowl.add(Sugar.take(grams = 50))
    bowl.mix()
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
    bowl.mix()
bowl.add(Salt.take('pinch'))
for i in range(10):
    bowl.add(Flour.take(grams = 30))
    bowl.add(ChocolateChips.take(grams = 20))
    bowl.mix()
bowl.add(BakingPowder.take('some'))
bowl.mix()

#Baking
tray = BakingTray.use(name = 'cookies')

for i in range(20):
    tray.add(bowl.take('1/20'))
Rosemary.taste(tray)

oven.add(tray)
oven.bake(minutes = 10)

plate = Plate.use()
cookies = tray.take()

plate.add(cookies)


Rosemary.serve(plate)