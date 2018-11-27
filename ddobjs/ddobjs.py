

class DDPlayer(object):
    """
    list DDCharacters[]
    int path_points
    int service_points
    """
    def __init__(self):
        pass


class DDCharacter(object):
    """
    creation_date
    events attended
    species + subspecies
    list classes
    """
    def __init__(self):
        pass


class DDModifier(object):
    """
    requirements to access skill lists
        Species Lists:
            General:
                -Character IS species
            Side:
                -Character IS side

        Class Lists:
            General:
                -Character Has one side of class
            Class Side:
                -Character has specific side of class
            List Prestige:
                -Character has at least one side of class
                -Character has X events

        Universal:
            -Return True

        Universal Prestige:
            -Character has >=6 events

        Ritual lists:
            -Devotee skill related

        Individual Skills:
            -must have access to list skill is on
    """
    def __init__(self):
        pass


class ClassList(DDModifier):
    def __init__(self):
        super(ClassList, self).__init__()


class Skill(object):
    def __init__(self, name='Undefined'):
        self.name = name
        self.cost = None
        self.prof = False
        self.dirty_tricks = False
        self.freq = None
        self.type = None
        self.lists = []
        self.desc = None

    def load_dict(self, d):
        for key, val in d.items():
            if key in self.__dict__.keys():
                self.__dict__[key] = val

    def __repr__(self):
        r_string = self.name
        r_string += '\n'
        r_string += str(self.cost) + ' build\n'
        r_string += self.freq + ' ' + self.type + '\n'
        r_string += self.desc + '\n'
        r_string += 'lists:'
        for l in self.lists:
            r_string += ' ' + l
        r_string += '\n'
        return r_string
