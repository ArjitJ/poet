import sys
import os
import glob
import json


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 " + sys.argv[0] + " exp_dir [deleted_env_file]\ne.g.: python3 ./generate_startfrom_file.py /home/user/logs/poet_experiment <( egrep \"DELETED\" /home/user/ipp/poet_experiment/run.log )", file=sys.stderr)
        exit(1)
    logdir = sys.argv[1]
    logdir = logdir.rstrip('/')
    save_path, experiment = os.path.dirname(logdir), os.path.basename(logdir)
    save_file = os.path.join(save_path, experiment + ".json")
    print("json will be saved in file -", save_file)
    save_dict = {}
    json_files = glob.glob(os.path.join(logdir, '*best.json'))
    
    
    save_dict['path'] = save_path + '/'
    save_dict['exp_name'] = experiment
    save_dict['niches'] = {}
    deleted_envs = []
    if len(sys.argv) > 2:
        with open(sys.argv[2], 'r') as deleted_env_file:
            for line in deleted_env_file:
                deleted_envs.append(line.strip().split()[-1])
    print(deleted_envs)
    for env_file in map(os.path.basename, json_files):
        experiment, *niche_file = env_file.split('.')
        niche_name = ".".join(niche_file[:-2]) # except "best" and "json"
        if niche_name in deleted_envs:
            continue
        print(niche_name)
        save_dict['niches'][niche_name] = ".".join(niche_file)
    json.dump(save_dict, open(save_file, 'w'))
