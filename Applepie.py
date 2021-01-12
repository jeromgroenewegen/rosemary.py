# get ingredients
from kitchen import Rosemary
from kitchen.utensils import Oven, Fridge, Bowl, Plate, PieDish
from kitchen.ingredients import Water, Flour, Salt, Butter, Apple, Lemon, Sugar, Cornstarch, Cinnamon, Egg

# chill water
waterbowl = Bowl.use(name = 'water')
waterbowl.add(Water.take('a bit'))
fridge = Fridge.use()
fridge.add(waterbowl)

# pre heat ovem
oven = Oven.use(degrees = 180)

# mix ingredients for dough
bowl = Bowl.use(name = 'dough')
bowl.add(Flour.take(grams = 300))
bowl.add(Salt.take('teaspoon'))
bowl.mix()
for i in range(5):
    bowl.add(Butter.take(grams = 50))
    bowl.mix()
bowl.add(waterbowl.take())
bowl.mix()

fridge.add(bowl)

# make filling
apple = Apple.take()
for i in range(6):
    apple.peel()
    apple.slice()
lemon = Lemon.take()
LemonZest = lemon.zest()
LemonJuice = lemon.squeeze()

bowl2 = Bowl.use(name = 'filling')
bowl2.add(apple.take())
bowl2.add(Sugar.take(grams = 150))
bowl2.add(Cornstarch.take('spoon'))
bowl2.add(Salt.take('pinch'))
bowl2.add(Cinnamon.take('teaspoon'))
bowl2.add(LemonJuice.take('part'))
bowl2.add(LemonZest.take('part'))

# add filling and dough to dish
dish = PieDish.use(name = 'pie')
dish.add(bowl.take('3/4'))
dish.add(bowl2.take())
dish.add(bowl.take('1/4'))

# add topping
bowl3 = Bowl.use(name = 'topping')
egg = Egg.take()
egg.crack()
bowl3.add(egg)
bowl3.mix()

dish.add(bowl3.take())
dish.add(Sugar.take('spoon'))
dish.add(LemonZest.take('remainder'))

# put in oven
oven.add(dish)
oven.bake(minutes = 60)

# take out of oven
plate = Plate.use()
applepie = dish.take()
plate.add(applepie)

# serve
Rosemary.serve(plate)