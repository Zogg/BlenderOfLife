import json
import subprocess
import golly as g

config = None
with open("config.json", "r") as f:
    config = json.load(f)

gen_nr = g.getstring("Enter the desired number of generations", "", "Go to generation")

generations = []
for gen in range(int(gen_nr)):
    clist = g.getcells(g.getselrect())
    clist = [(clist[i], clist[i + 1]) for i in range(0, len(clist), 2)]
    generations.append(clist)
    g.step()

with open(config['data_file'], "w") as f:
    json.dump(generations, f)

subprocess.call(['blender', '-b', '-P', config['blender_script']])
