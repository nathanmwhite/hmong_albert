#!/usr/bin/python

# Byte-pair encoding demonstration script
# Copyright (c) 2021 Hmong Medical Corpus Project
# Author : Nathan M. White <nathan.white1@my.jcu.edu.au>
"""
This script runs a series of tests of the byte-pair
encoding model files for purposes of demonstration.
"""

import os

import sentencepiece as spm

# Copyright notice
__copyright__ = "Copyright (c) 2021 Hmong Medical Corpus Project"

# project_url
__url__ = "https://corpus.ap-southeast-2.elasticbeanstalk.com/hminterface"

# author
__author__ = "Nathan M. White"
__author_email__ = "nathan.white1@my.jcu.edu.au"

# central function of script
def run_demonstration():
    """Runs the demonstration of the byte-pair encoding files."""

    # set relative location of the model
    model_loc = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                             'sentencepiece_model_files')

    # load in the SentencePiece model file
    prc = spm.SentencePieceProcessor(model_file=os.path.join(model_loc, 'hm.model'))

    # begin demonstration attempts
    print('Qhov no yog kev siv :', prc.encode('Qhov no yog kev siv'))

    print('Qhov no yog kev siv; Nyob zoo ntiaj teb :', 
          prc.encode(['Qhov no yog kev siv', 'Nyob zoo ntiaj teb'], out_type=int))

    print('Qhov no yog kev siv :', prc.encode('Qhov no yog kev siv', out_type=str))

    for i in range(10):
        print('Qhov no yog kev siv : sample', i, ':')
        print(prc.encode('Qhov no yog kev siv',
                    out_type=str, 
                    enable_sampling=True,
                    alpha=0.1,
                    nbest_size=-1))

    print('Piece size :', prc.get_piece_size())

    print('Piece with index 2 :', prc.id_to_piece(2))

if __name__ == '__main__'
    run_demonstration()
