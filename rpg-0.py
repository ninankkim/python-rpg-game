"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character:
    def __init__(self, health, power): 
        self.health = health
        self.power = power


    def alive(self):
        self.health > 0
        return self.health


class Hero(Character):

    def __init__ (self, health, power, armor):
        super().__init__(health, power)
        self.armor = armor

    def attack(self, goblin):
        #The hero attacks the goblin.
        goblin.health -= self.power
        print("The hero did %d damage to the Goblin." % self.power)
        #or you can print it like this
        #print(f"You did {self.power} damange to the goblin.")


    def alive(self):
        self.health > 0
        return self.health

    def status(self):
        print("You have %d health and %d power, and %d armor." % (self.health, self.power, self.armor))


class Goblin(Character):

    def attack(self, hero):
        #The goblin attacks the hero.
        hero.health -= self.power
        print("The goblin did %d damage to the you." % self.power)

    def alive(self):
        self.health > 0
        return self.health
    
    def status(self):
        print("The goblin have %d health and %d power." % (self.health, self.power))


def main():

    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    hero = Hero(10, 5, 20)
    goblin = Goblin(6,2)
    

    while goblin.alive() > 0 and hero.alive() > 0:
        hero.status()
        goblin.status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")

main()






