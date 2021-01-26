#!/bin/bash

# TODO:
#  finish defining parameters for ALBERT training on cased data, seq length 128
#  define ALBERT training on cased data, seq length 512
#  conditional create directory for uncased output
#  define ALBERT training on uncased data, seq length 128 and 512
#  defensively deal with errors if inputs are missing

# set paths
export CASED_INPUT=./cased_data/pretrain_examples/short_data.out
export UNCASED_INPUT=./uncased_data/pretrain_examples/short_data.out

# install requirements
pip install -r albert/requirements.txt

# create output directory for cased data model
export CASED_OUTPUT=./cased_data/pretrain_output
if [ ! -d "./cased_data/pretrain_output" ]
then
	mkdir $CASED_OUTPUT
fi

# run pretraining for cased model, seq length 128
python -m albert.run_pretraining \
	--input_file=$CASED_INPUT \
	--output_dir=$CASED_OUTPUT \
	--init_checkpoint=... \
	--albert_config_file=... \
	--do_train \
	--do_eval
	--train_batch_size=... \
	--eval_batch_size=... \
	--max_seq_length=... \
	--max_predictions_per_seq=... \
	--optimizer=... \
	--learning_rate=... \
	--num_train_steps=... \
	--num_warmup_steps=... \
	--save_checkpoints_steps=...
