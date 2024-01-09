# Tier = [katze, hund, hase, schnecke, hamster, rennmaus]

# Tiernamen
name = ["Mia", "Patch", "Hop", "Eric", "Winnie", "Lilly"]

# Elternklasse für die Tiere
class Tier:
    def __init__(self, name, alter, geschlecht):
        self.name = name
        self.alter = alter
        self.geschlecht = geschlecht

# Klasse für die Hase
class Hase(Tier):
    def __init__(self, name, alter, geschlecht, lieblingsessen):
        super().__init__(name, alter, geschlecht)
        self.klang = "squeek"
        self.lieblingsessen = lieblingsessen

    def printLieblingsessen(self):
        print(f"\n{self.name}'s lieblingsessen ist {self.lieblingsessen}\n\n")