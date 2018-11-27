import json
import random
import argparse


'''
TODO:
    Add argparse options for generating json, searching existing files, etc.
        -Move functionalies of __main__ to functions (and clean them up)

    Better define Skill Class
        -Maybe create classes for properties of Skill.

    Define Racial + (Class+Side) List classes
        -Racial lists hold skills and initial bonuses
        -Class lists/sides + Racial subtypes:
            -Doomcaller Requires Dirty Tricks
            -class Sides provide free proficiencies
                These don't count towards build cost of those profs next purchases.
            -Only one racial subtype can be picked up

    Other Lists (Universal, Universal Prestige, Prestige[class])

    Define Character Class
        ...
'''

files = ['terran', 'elysian', 'aesir', 'boz', 'robot', 'android', 'cybrid', 'cryo', 'weed', 'zelnalak', 'mkai', 'oniri', 'yana', 'mutant', 'maneater', 'universal']

skills = {}


class Skill(object):
    def __init__(self, name):
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
        rstr = self.name
        rstr += '\n'
        rstr += str(self.cost) + ' build\n'
        rstr += self.freq + ' ' + self.type + '\n'
        rstr += self.desc + '\n'
        rstr += 'lists:'
        for l in self.lists:
            rstr += ' ' + l
        rstr += '\n'
        return rstr


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--generate', action='store_true', help='Generate json files from skill list files.')
    parser.add_argument('general_search', default=[], nargs='*', action='store', help='Search all')
    args = parser.parse_args()

    for f in files:
        with open('racial/'+f) as fp:
            s = None
            for line in fp.readlines():
                try:
                    l = line.strip().split(':', 1)
                    if len(l) == 2:
                        key = l[0].lower().strip()
                        if key == 'name':
                            # new skill incoming
                            if s is not None:
                                skills[s.name] = s
                            skillname = l[1].strip()
                            if skillname in skills.keys():
                                s = skills[skillname]
                            else:
                                s = Skill(skillname)

                        # we already have a Skill, fill in the rest of it, or add
                        #   to it
                        elif s is not None:
                            if key in s.__dict__.keys():
                                value = l[1].strip()
                                if key == 'lists':
                                    s.lists.append(value.strip())
                                elif key == 'prof':
                                    if value.lower() in ['true', 't', '1', 'yes']:
                                        s.prof = True
                                elif key == 'cost':
                                    try:
                                        s.cost = int(value)
                                    except:
                                        s.cost = value
                                elif key in ['dirty_tricks', 'dt']:
                                    if value in ['true', 't', '1', 'yes']:
                                        s.dirty_tricks = True
                                elif key in ['freq', 'frequency']:
                                    s.freq = value.lower()
                                    if value not in ['periodic', 'per-event', 'recurrent', 'permanent']:
                                        print(s.name + ': '+  str(key) + ' = ' + str(value))
                                else:
                                    if key in s.__dict__.keys():
                                        s.__dict__[key] = str(value)
                                    else:
                                        raise Exception
                        else:
                            raise Exception
                except:
                    print("Failure to import skill from list file " + str(f))
                    exit()

to_file = {}

for name, skill in skills.items():
    s = {}
    for k, v in skill.__dict__.items():
        if '\\n' in str(v):
            strv = str(v).replace('\\n', '\n')
        else:
            strv = v
        s[k] = strv
    to_file[name] = s

with open('racial.json', 'w') as fp:
    json.dump(to_file, fp, indent=4)

with open('racial.json', 'r') as fp:
    new_skills = json.load(fp)

slist = []
for name, skill in new_skills.items():
    s = Skill(name)
    s.load_dict(skill)
    slist.append(s)

bad_reprs = []
for s in slist:
    print(s)
