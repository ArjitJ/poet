# Copyright (c) 2020 Uber Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import numpy as np

# GDD: Need version of this for our env config
def env2array(env):
    arr = np.zeros(10)
    arr[0:2] = env.lava_prob
    arr[2:4] = env.obstacle_lvl
    arr[4:6] = env.box_to_ball_prob
    arr[6:8] = env.door_prob
    arr[8:] = env.wall_prob
    return arr

# GDD: Need to rewrite for our env config
def euclidean_distance(nx, ny, normalize=False):

    x = np.array(env2array(nx), dtype=np.float32)
    y = np.array(env2array(ny), dtype=np.float32)

    diff = x - y
    

    return np.sqrt(np.sum(np.power(diff,2)))


def compute_novelty_vs_archive(archive, niche, k):
    distances = []
    normalize = False
    for point in archive.values():
        distances.append(euclidean_distance(point, niche, normalize=normalize))

    # Pick k nearest neighbors
    distances = np.array(distances)
    top_k_indicies = (distances).argsort()[:k]
    top_k = distances[top_k_indicies]
    return top_k.mean()
