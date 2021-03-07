from model import simulate, Model
from env import Env_config, minigridhard_custom
import sys
name = sys.argv[1]
import json
import numpy as np
model_json = json.load(open(name+'.env.json', 'rb'))
param_json = json.load(open(name+'.best.json', 'rb'))
mymodel = Model(minigridhard_custom)
mymodel.make_env(model_json['seed'], env_config=Env_config(**model_json['config']))
mymodel.set_model_params(param_json[0])
reward,time = simulate(mymodel, seed=np.random.RandomState(model_json['seed']).randint(1000000), num_episode=1, render_mode=True)
print(reward, time)