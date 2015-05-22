# part of http://ThePythonGameBook.com
# source code: https://github.com/horstjens/ThePythonGameBook/blob/master/python/goblins/slowgoblins004.py
import random

max_roll = 100
min_roll = 10
hitpoints_stinky = 2000
hitpoints_grunty = 2000
combat_round = 0

print(" --- The Goblin Dice Duel ---")
print("game_round, Stinky, Grunty")
while (hitpoints_grunty > 0  and hitpoints_stinky > 0) :
    print("{0:2d} Stinky: {1:4d} Grunty: {2:4d}".format(combat_round, hitpoints_stinky, hitpoints_grunty))
    combat_round += 1
    hitpoints_grunty -= random.randint(min_roll,max_roll)
    hitpoints_stinky -= random.randint(min_roll,max_roll)

print("Game Over")

if hitpoints_stinky > hitpoints_grunty and hitpoints_stinky > 0:
    print("Stinky wins with {0:4d} life left".format(hitpoints_stinky))
elif hitpoints_grunty > hitpoints_stinky and hitpoints_grunty  > 0:
    print("Grunty wins with {0:4d} life left".format(hitpoints_grunty))
else:
    print("Nobody wins ?!")

print("thank you for playing Goblin Dice Duel. bye-bye!")