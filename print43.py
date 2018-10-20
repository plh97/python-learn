# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# class 
# 太多了,不写了
class Scene(object):
    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit()



class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        pass
    
    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n---------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)



class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "You mon would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)



class CentralCorridor(Scene):
    def enter(self):
        print("The Gothons of Plant Percal #25 have invaded your ship and destroyed")
        print("your entire crew. You are the last surviving member and your last")
        print("mission is to get the mentron destruct bomb from the Weapons Armory,")
        print("put it in the bridge, and blow the ship up after getting into an escape pod.")
        print("\n")
    
    action = raw_input("> ")

    if(action == "shoot!"):
        print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
        print("His clown costume is flowing and moving around his body, which throws")
        print("off you ami, your laser hits his costume but miss him entirely.")
        print("This makes him fly into a rage and blast you repeatedly in the face until you are edead.")
        print("Then he eats you.")
        print("death")
    
    elif action == 'dodge!':
        print("Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks a laser past your head.")

    elif action == "tell a joke":
        print("Lucky for you they make you learn Gothon")
    else:
        print("DOES NOT COMPUTE!")
        return("centeral_corridor")


class LaserWeaponArmory(Scene):
    def enter(self):
        print("You)



class TheBridge(Scene):
    def enter(self):
        pass



class Map(object):

    def __init__(self, start_name):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()