files = ['terran', 'elysian', 'aesir', 'boz', 'robot', 'android', 'cybrid', 'cryo', 'weed', 'zelnalak', 'mkai', 'oniri']

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
                                s.__dict__[key] = value
                    else:
                        print(s.name)
                        print("FAILURE")
                        exit()

lists = {}

for name, skill in skills.items():
    for lst in skill.lists:
        if lst not in lists:
            #print(lst)
            lists[lst] = []
        lists[lst].append(skill)
    if len(skill.lists) > 1:
        print(skill.name, skill.lists)

for l in lists:
    this_list = lists[l]
    print(l+'*'*40)
    for skill in this_list:
        print(skill.name)
