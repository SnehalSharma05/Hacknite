class Spell():
    def __init__(self, name, damage, heal, effect):
        self.name = name
        self.damage = damage
        self.heal = heal
        self.effect = effect
    def __str__(self):
        return self.name


reducto = Spell("reducto", 50, 0, "Blasts solid objects into pieces")
stupefy = Spell("stupefy", 40, 0, "Stuns the target")
incendio = Spell("incendio", 50, 0, "Produces fire from the caster's wand")
expulso = Spell("expulso", 45, 0, "Causes objects to explode")
bombarda = Spell("bombarda", 60, 0, "Causes a small explosion on impact")
sectumsempra = Spell("sectumsempra", 70, 0, "Causes severe lacerations on the target")
confringo = Spell("confringo", 65, 0, "Causes objects to burst into flames when struck")
crucio = Spell("crucio", 100, 0, "Inflicts intense pain on the target")
fiendfyre = Spell("fiendfyre", 100, 0, "Uncontrollable fire that consumes everything in its path")
expelliarmus = Spell("expelliarmus", 30, 0, "Disarms the target")

# Creating objects for healing spells with negative damage
episkey = Spell("episkey", 0, 20, "Heals minor injuries")
vulnera_sanentur = Spell("vulnera_sanentur", 0, 50, "Heals wounds")

# Creating objects for defensive spells
expecto_patronum = Spell("expecto_patronum", 0, 0, "Summons a Patronus to ward off Dementors")
ridikkulus = Spell("ridikkulus", 0, 0, "Turns a Boggart into something humorous")
protego = Spell("protego", 0, 0, "Creates a magical barrier to deflect spells and physical objects")