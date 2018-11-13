import json
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

if __name__ == '__main__':
    for f in files:
        with open(f) as fp:
            s = None
            for line in fp.readlines():
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
                                    s.cose = value
                            elif key in ['dirty_tricks', 'dt']:
                                if value in ['true', 't', '1', 'yes']:
                                    s.dirty_tricks = True
                            elif key in ['freq', 'frequency']:
                                s.freq = value.lower()
                                if value not in ['periodic', 'per-event', 'recurrent', 'permanent']:
                                    print(s.name + ': '+  str(key) + ' = ' + str(value))
                            else:
                                s.__dict__[key] = str(value)
                    else:
                        print(s.name)
                        print("FAILURE")
                        exit()

to_file = {}

for name, skill in skills.items():
    s = {}
    for k, v in skill.__dict__.items():
        s[k] = v
    to_file[name] = s


with open('racial.json', 'w') as fp:
    json.dump(to_file, fp, indent=4)


with open('racial.json', 'r') as fp:
    new_skills = json.load(fp)

for name, skill in new_skills.items():
    #print(name)
    if 'Negotiate' == name:
        print(skill['desc'])

'''
top_lists = {}
lists = {}


for name, skill in skills.items():
    for lst in skill.lists:
        top_list = lst.split(':')[0]
        low_list = lst.split(':')[1]
        if top_list not in top_lists.keys():
            top_lists[top_list] = {}
        if low_list not in top_lists[top_list].keys():
            llist = {}
            top_lists[top_list] = llist
        else:
            llist = top_lists[top_list]
        llist[name]=skill

for l, side in top_lists.items():
    print('-'*40)
    print(l)
    print('-'*40)
    print(side)
    for k, v in side.items():
        print(k)
'''
