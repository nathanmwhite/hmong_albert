#!/bin/bash
#SBATCH -N 3
#SBATCH --job-name=hmong_albert_generate_pretraining
#SBATCH -n 3
#SBATCH -c 1
#SBATCH --mem=50000
#SBATCH --partition=gpu
#SBATCH --gres=gpu:tesla:2

# generate_pretraining_testing.sh
#
# original code Copyright (c) 2021 Nathan M. White
# with other code modified from ALBERT documentation
# with copyright belonging to the respective holders
#
# This script tests the generating pretraining examples approach
# that creates input to the ALBERT model architecture. The script
# generates examples of sequence lengths 128 and 512 for
# both cased and uncased data as found in the hmong_albert
# repository.
#
# The sequence lengths and max predictions hyperparameters
# are defined in accordance with Virtanen et al. (2019).
#
# Note that this script contains relative references such
# that it should be run from the top level hmong_albert
# repository folder. The ALBERT repository folder must be
# installed and available on $PYTHONPATH.
#
# Note also that this bash script is designed to run on
# a SLURM scheduler.

module load cuda/10.0.130
module load gnu7
module load openmpi3
module load anaconda/3.6
source activate /opt/ohpc/pub/apps/tensorflow_1.13

# Install ALBERT requirements
export ALBERT_PATH=../albert

pip install --user -r $ALBERT_PATH/requirements.txt

# Define sequence lengths and max predictions variables
export SHORT_SEQ=128
export LONG_SEQ=512
export MAX_PRED_SHORT=20
export MAX_PRED_LONG=77

# Define vocabulary file locations
export CASED_VOCAB=./sentencepiece_model_files/hm.cased_data.vocab
#export UNCASED_VOCAB=./sentencepiece_model_files/hm.uncased_data.vocab

# Define output file names
export SHORT_DATA_OUT=short_data.out
export LONG_DATA_OUT=long_data.out

# Check if pretrain_examples folder exists, and create if not
export CASED_PRETRAIN_OUT_PATH=./cased_data/pretrain_examples

if [ ! -d "$CASED_PRETRAIN_OUT_PATH" ]
then
	mkdir $CASED_PRETRAIN_OUT_PATH
fi

#SBATCH -o ./cased_data/pretrain_examples/short_data.out
#SBATCH -e ./cased_data/pretrain_examples/tensor_error.txt

# Cased data : generate for sequence lengths 128 and 512
export CASED_PRETRAIN_IN_PATH=./cased_data/pretrain

export PYTHONPATH=/scratch/jcu/nwhite/

srun -n2 --mpi=pmix_v2 python3 -m albert.create_pretraining_data \
	--input_file=$CASED_PRETRAIN_IN_PATH/sch_corpus/*.*,\
                     $CASED_PRETRAIN_IN_PATH/knh/*.*,\
                     $CASED_PRETRAIN_IN_PATH/med_like/childsupCA/*.*,\
                     $CASED_PRETRAIN_IN_PATH/med_like/disabilityrightsCA/*.* \
        --output_file=$CASED_PRETRAIN_OUT_PATH/$SHORT_DATA_OUT \
        --vocab_file=$CASED_VOCAB \
        --max_seq_length=$SHORT_SEQ \
        --max_predictions_per_seq=$MAX_PRED_SHORT
