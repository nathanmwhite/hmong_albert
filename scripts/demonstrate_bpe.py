#!/usr/bin/python

# this file runs a series of tests of the model
#   files for purposes of demonstration

import os

import sentencepiece as spm

model_loc = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                         'sentencepiece_model_files')

prc = spm.SentencePieceProcessor(model_file=os.path.join(model_loc, 'hm.model'))

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
