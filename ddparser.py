import json
import argparse
from ddobjs.ddobjs import *


def build_skills():
    # intake skills
    skills = {}
    files = ['terran', 'elysian', 'aesir', 'boz', 'robot', 'android', 'cybrid', 'cryo', 'weed', 'zelnalak', 'mkai', 'oniri', 'yana', 'mutant', 'maneater', 'universal']
    for f in files:
        with open('skills/racial/'+f) as fp:
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

                        # already have a Skill, fill in the rest of it, or add
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
                                        print(s.name + ': ' + str(key) + ' = ' + str(value))
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
    pass


if __name__ == '__main__':
    build_skills()
