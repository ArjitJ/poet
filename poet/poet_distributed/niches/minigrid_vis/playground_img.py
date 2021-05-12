from model_emb import simulate, Model
from env import Env_config, minigridhard_custom
import sys

name = sys.argv[1]
import json
import numpy as np
model_json = json.load(open(name+'.env.json', 'rb'))
param_json = json.load(open(name+'.best.json', 'rb'))
mymodel = Model(minigridhard_custom)
seed = int(sys.argv[2]) if len(sys.argv) == 3 else model_json['seed']
mymodel.make_env(model_json['seed'], env_config=Env_config(**model_json['config']))
mymodel.env.render("human", highlight=False)
plt.savefig(name+'.png')
