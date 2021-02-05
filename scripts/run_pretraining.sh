#!/bin/bash
#SBATCH -N 2
#SBATCH --job-name=hmong_albert_pretrain
#SBATCH -n 8
#SBATCH -c 1
#SBATCH --mem=50000
#SBATCH --partition=gpu
#SBATCH --gres=gpu:tesla-sxm2:8
#SBATCH -e pretraining_error.txt

# run_pretraining.sh
#
# original code Copyright (c) 2021 Nathan M. White
# with other code modified from ALBERT documentation
# with copyright belonging to the respective holders
#
# This script generates pretraining examples to serve
# as input to the ALBERT model architecture. The script
# pretrains a BERT model with examples of sequence lengths
# 128 for cased data as found in the hmong_albert
# repository.
# This script is intended to be followed by training on 
# cased data, size 512 for an additional 12,500 iterations.
#
# The sequence lengths and max predictions hyperparameters
# are defined in accordance with Virtanen et al. (2019).
#
# Note that this script contains relative references such
# that it should be run from the top level hmong_albert
# repository folder.
#
# Note also that this bash script is designed to run on
# a SLURM scheduler.

# TODO:
#  finish defining parameters for ALBERT training on cased data, seq length 128
#  define ALBERT training on cased data, seq length 512
#  conditional create directory for uncased output
#  define ALBERT training on uncased data, seq length 128 and 512
#  defensively deal with errors if inputs are missing

# Introduce modules and activate optimized environment
module load gnu7
module load cuda/10.0.130
module load anaconda/3.6
module load openmpi3
source activate /opt/ohpc/pub/apps/tensorflow_1.13

# Set paths
export CASED_INPUT=./cased_data/pretrain_examples/short_data.out
#export UNCASED_INPUT=./uncased_data/pretrain_examples/short_data.out

# Define $PYTHONPATH
export PYTHONPATH=/scratch/jcu/nwhite/

# install requirements
pip install -r albert/requirements.txt

# create output directory for cased data model
export CASED_OUTPUT=./cased_data/pretrain_output
if [ ! -d "$CASED_OUTPUT" ]
then
	mkdir $CASED_OUTPUT
fi

# run pretraining for cased model, seq length 128
srun -n3 --mpi=pmix_v2 python3 -m albert.run_pretraining \
	--input_file=$CASED_INPUT \
	--output_dir=$CASED_OUTPUT \
	--init_checkpoint=None \
	--albert_config_file=albert_config.json \
	--do_train \
	--do_eval
	--train_batch_size=4096 \
	--eval_batch_size=64 \
	--max_seq_length=128 \
	--max_predictions_per_seq=20 \
	--optimizer='lamb' \
	--learning_rate=.00176 \
	--num_train_steps=112500 \
	--num_warmup_steps=1250 \
	--save_checkpoints_steps=5000

# then run pretraining on the same model, seq length 512, max pred 77
# for 10% with no warmup steps; what to do with 'lamb' status?
