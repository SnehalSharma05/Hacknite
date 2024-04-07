from assets.spells import *
class Enemy():
    def __init__(self, name, health, probability,spells,damage=0):
        self.name = name
        self.damage = damage
        self.health = health
        self.max_health = health
        self.prob = probability
        self.spells = spells

peter_pettigrew = Enemy("Peter Pettigrew", 170, 0.5,[reducto,stupefy,expelliarmus])
vincent_crabbe = Enemy("Vincent Crabbe", 160, 0.3,[stupefy,expelliarmus])
gregory_goyle = Enemy("Gregory Goyle", 165, 0.3,[stupefy,expelliarmus])
acromantula = Enemy("Acromantula", 200, 0.7,[],70)
lucius_malfoy = Enemy("Lucius Malfoy", 180, 0.6,[stupefy,reducto,expelliarmus,expulso,episkey])
igor_karkaroff = Enemy("Igor Karkaroff", 190, 0.6,[reducto,expulso,bombarda,incendio,episkey])
werewolf = Enemy("Werewolf", 220, 0.6,[],80)
fenrir_greyback = Enemy("Fenrir Greyback", 230, 0.7,[stupefy,reducto,expelliarmus,expulso,bombarda,confringo])
narcissa_malfoy = Enemy("Narcissa Malfoy", 180, 0.6,[stupefy,reducto,expelliarmus,expulso,episkey])
bellatrix_lestrange = Enemy("Bellatrix Lestrange", 220, 0.8,[reducto,expulso,bombarda,crucio,incendio,confringo,fiendfyre,vulnera_sanentur,episkey])
barty_crouch_jr = Enemy("Barty Crouch Jr.", 200, 0.7,[reducto,expulso,bombarda,incendio,crucio,confringo,vulnera_sanentur,episkey])
#dementor = Enemy("Dementor", 10000, 1)
#boggart = Enemy("Boggart", 10000, 1)
basilisk = Enemy("Basilisk", 300, 0.7,[],100)
severus_snape = Enemy("Severus Snape", 200, 0.7,[reducto,stupefy,expelliarmus,sectumsempra,confringo,fiendfyre,vulnera_sanentur,episkey])
voldemort = Enemy("Lord Voldemort", 400, 0.9,[incendio,expulso,bombarda,sectumsempra,confringo,crucio,fiendfyre,vulnera_sanentur,episkey])

def calculate_difficulty(enemy):
    return enemy.health * enemy.prob

enemies = [peter_pettigrew, vincent_crabbe, gregory_goyle, acromantula, lucius_malfoy, igor_karkaroff, werewolf, fenrir_greyback, narcissa_malfoy, bellatrix_lestrange, barty_crouch_jr, basilisk, severus_snape, voldemort]

# Sort the enemies based on their difficulty
enemies = sorted(enemies, key=calculate_difficulty, reverse=False)