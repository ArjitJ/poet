from collections import namedtuple
from gym_minigrid.envs.mazeEnv import MazeEnv
from gym.utils import seeding

Env_config = namedtuple('Env_config', [
    'name',
    'lava_prob',
    'obstacle_lvl',
    'box_to_ball_prob',
    'door_prob',
    'wall_prob',
])


# Create a modified version of gym-minigrid that uses recursive division to create mazes
#  and mutable parameters to modify object placements, amount of walls, etc
class MiniGridCustom(MazeEnv):
    def __repr__(self):
        return "{}\n{}".format(self.__dict__, self.__dict__["np_random"].get_state())

    def __init__(self, env_config):
        self.set_env_config(env_config)
        self._seed()
        
        # size=3 corresponds to a 17x17 maze
        # size=2 corresponds to a 9x9 maze
        super().__init__(size=2, limit=2)
        

    def _seed(self,seed=None):
        self.env_seed = seed
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def set_env_config(self,env_config):
        self.config = env_config
        # print("env_config ", env_config)


    def reset(self):
        # Get specific probabilities from the env_config ranges
        self.lava_prob = self.np_random.uniform(*self.config.lava_prob)
        self.obstacle_level = self.np_random.uniform(*self.config.obstacle_lvl)
        self.box2ball = self.np_random.uniform(*self.config.box_to_ball_prob)
        self.door_prob = self.np_random.uniform(*self.config.door_prob)
        self.wall_prob = self.np_random.uniform(*self.config.wall_prob)
        
        # str1 = 'lava chosen from {} and set to {}\n'.format(self.config.lava_prob, self.lava_prob)
        # str2 = 'obs chosen from {} and set to {}\n'.format(self.config.obstacle_lvl, self.obstacle_level)
        # str3 = 'b2b chosen from {} and set to {}\n'.format(self.config.box_to_ball_prob, self.box2ball)
        # str4 = 'door chosen from {} and set to {}\n'.format(self.config.door_prob, self.door_prob)
        # str5 = 'wall chosen from {} and set to {}\n'.format(self.config.wall_prob, self.wall_prob)
        # print(str1+str2+str3+str4+str5,flush=True)
        return super().reset()
