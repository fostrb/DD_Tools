class DDChar(object):
    def __init__(self):
        self.name = 'character'

        self.events = 1     # list access restriction
        self.race = None    # skill access restriction
        self.classes = []   # skill access restriction

    def initialize_lists(self):
        pass


class SkillList(object):
    def __init__(self, name=None):
        # name (Moonlighter:Trickster, Moonlighter:Spider, etc)
        self.name = name
        self.name = 'Moonlighter:General'

        # Benefits (Body, Stamina, profs)
        self.benefits = []

        # skill access


class Skill(object):
    def __init__(self):
        # name
        self.name = 'Hide'

        # requirements to take
        self.dt = False

        # int cost
        self.cost = 1

        # bool proficiency
        self.prof = False

        # frequency (permanent, recurrent, periodic, per-event)
        self.frequency = "Periodic"

        # type (atk, def, special, etc)
        self.type = "Special"

        # lists
        self.lists = ['Moonlighter:General', 'Rebel:Shadow', 'Soldier:Rifleman', 'Doomcaller:Adherent of the Left Hand Path', 'Highwayman:Pistoleer']


def cost_of_n_skill(skill, n):
    # how much is n purchases of skill
    b = skill.cost
    if not skill.prof:
        additional = sum(range(1, n))
    else:
        additional = sum(range(1, n)) * 2
    return n*b+additional


def cost_of_adding_n_skill(skill, n, num_already=0):
    total = 0
    for i in range(num_already+1, num_already+n+1):
        #print(i)
        total += (cost_of_nth_skill(skill, i))
        #print(total)
    return total


def cost_of_nth_skill(skill, n):
    b = skill.cost
    if not skill.prof:
        return b+n-1


if __name__ == '__main__':
    s = Skill()
    for n in range(1, 6):
        cost_of_n_skill(s, n)

    for n in range(1, 6):
        cost_of_nth_skill(s, n)

    print(cost_of_adding_n_skill(s, 4, 1))
