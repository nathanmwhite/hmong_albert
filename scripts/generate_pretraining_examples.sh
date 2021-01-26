#!/bin/bash

pip install -r albert/requirements.txt

# check if pretrain_examples folder exists, and create if not
if [ ! -d "./cased_data/pretrain_examples" ]
then
	mkdir ./cased_data/pretrain_examples
fi

# cased data : generate for sequence lengths 128 and 512
python -m albert.create_pretraining_data \
	--input_file=./cased_data/pretrain/sch_corpus/*.*,\
                     ./cased_data/pretrain/knh/*.*,\
                     ./cased_data/pretrain/med_like/childsupCA/*.*,\
                     ./cased_data/pretrain/med_like/disabilityrightsCA/*.* \
        --output_file=./cased_data/pretrain_examples/short_data.out \
        --max_seq_length=128 \
        --max_predictions_per_seq=20

python -m albert.create_pretraining_data \
	--input_file=./cased_data/pretrain/sch_corpus/*.*,\
                     ./cased_data/pretrain/knh/*.*,\
                     ./cased_data/pretrain/med_like/childsupCA/*.*,\
                     ./cased_data/pretrain/med_like/disabilityrightsCA/*.* \
        --output_file=./cased_data/pretrain_examples/long_data.out \
        --max_seq_length=512 \
        --max_predictions_per_seq=77

# check if pretrain_examples folder exists, and create if not
if [ ! -d "./uncased_data/pretrain_examples" ]
then
	mkdir ./uncased_data/pretrain_examples
fi

# uncased data : generate for sequence lengths 128 and 512
python -m albert.create_pretraining_data \
	--input_file=./uncased_data/pretrain/sch_corpus/*.*,\
                     ./uncased_data/pretrain/knh/*.*,\
                     ./uncased_data/pretrain/med_like/childsupCA/*.*,\
                     ./uncased_data/pretrain/med_like/disabilityrightsCA/*.* \
        --output_file=./uncased_data/pretrain_examples/short_data.out \
        --max_seq_length=128 \
        --max_predictions_per_seq=20

python -m albert.create_pretraining_data \
	--input_file=./uncased_data/pretrain/sch_corpus/*.*,\
                     ./uncased_data/pretrain/knh/*.*,\
                     ./uncased_data/pretrain/med_like/childsupCA/*.*,\
                     ./uncased_data/pretrain/med_like/disabilityrightsCA/*.* \
        --output_file=./uncased_data/pretrain_examples/long_data.out \
        --max_seq_length=512 \
        --max_predictions_per_seq=77
