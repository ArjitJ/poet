#!/bin/bash
# export PATH=/root/gym-minigrid:$PATH
if [ -z "$1" ]
then
    echo "Missing an experiment id"
    exit 1
fi
if [ -z "$2" ]
then
    echo "Setting iteration to default of 50000"
    ITR=50000
else
    ITR=$2
fi

experiment=poet_$1

mkdir -p poet_mini/$experiment/ipp
mkdir -p poet_mini/$experiment/logs

python3 -u minigrid_master.py \
  poet_mini/$experiment/logs \
  --init=random \
  --learning_rate=0.01 \
  --lr_decay=0.9999 \
  --lr_limit=0.001 \
  --batch_size=1 \
  --batches_per_chunk=48 \
  --eval_batch_size=1 \
  --eval_batches_per_step=5 \
  --master_seed=24582922 \
  --noise_std=0.01 \
  --noise_decay=0.999 \
  --noise_limit=0.01 \
  --normalize_grads_by_noise_std \
  --returns_normalization=centered_ranks \
  --stochastic \
  --envs lava obstacle box_to_ball door wall  \
  --max_num_envs=15 \
  --adjust_interval=4 \
  --propose_with_adam \
  --steps_before_transfer=25 \
  --num_workers 8 \
  --n_iterations=$ITR 2>&1 | tee poet_mini/$experiment/ipp/run.log
