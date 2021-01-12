# How many?
x = 8

# Assemble utensils and ingredients
from kitchen import Rosemary
from kitchen.utensils import Bowl, Pan, Fridge, Plate
from kitchen.ingredients import Flour, Egg, Milk, Butter, Salt

# Add eggs to the bowl and whisk
bowl = Bowl.use(name='batter')
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.mix()

# Add a dash of salt
bowl.add(Salt.take('dash'))

# Add flour to the batter
for i in range(5):
    bowl.add(Flour.take(grams=(50/8)*x))
    bowl.mix()

# Add milk
for i in range(2):
    bowl.add(Milk.take(ml=(250/8)*x))
    bowl.mix()

# Get the pan
pan = Pan.use(name ='pancake')
plate = Plate.use()

# Cook 8 pancakes
for i in range(8):
    pan.add(Butter.take('slice'))
    pan.add(bowl.take((f'1/{x}')))
    for i in range(3):
        pan.cook(minutes=1/2)
        pan.flip()
    pan.cook(minutes=1/2)

    pancake = pan.take()
    plate.add(pancake)

# Serve the pancakes
Rosemary.serve(plate)