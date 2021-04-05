from collections import namedtuple
# import gym
from .minigrid_custom import MiniGridCustom, Env_config  # noqa
from gym_minigrid.wrappers import FullyObsWrapperWithDir


def make_env(env_name, seed, render_mode=False, env_config=None):
    if env_name.startswith("MiniGridCustom"):
        assert env_config is not None
        env = MiniGridCustom(env_config)
    else:
        # env = gym.make(env_name)
        raise Exception('Got env_name {}'.format(env_name))
    #     if render_mode and not env_name.startswith("Roboschool"):
    #         env.render("human")
    if (seed >= 0):
        env.seed(seed)
    env = FullyObsWrapperWithDir(env)
    # print("environment details")
    # print("env.action_space", env.action_space)
    # print("high, low", env.action_space.high, env.action_space.low)
    # print("environment details")
    # print("env.observation_space", env.observation_space)
    # print("high, low", env.observation_space.high, env.observation_space.low)
    # assert False

    return env


Game = namedtuple('Game', ['env_name', 'time_factor', 'input_size',
                           'output_size', 'layers', 'activation', 'noise_bias',
                           'output_noise'])

minigridhard_custom = Game(env_name='MiniGridCustom',
                           input_size=50,
                           output_size=6,
                           time_factor=0,
                           layers=[16, 16],
                           activation='softmax',
                           noise_bias=0.0,
                           output_noise=[False, False, False],
                           )
