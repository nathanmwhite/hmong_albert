#!/usr/bin/python

# Text preprocessing script for Hmong ALBERT project
# Copyright (c) 2021 Hmong Medical Corpus Project
# Author : Nathan M. White <nathan.white1@my.jcu.edu.au>
"""
This script preprocesses texts for use with ALBERT.
It converts the text such that each sentence is on one line,
and paragraphs are separated by an empty space.
"""

import os
import re
import string
import sys

# Copyright notice
__copyright__ = "Copyright (c) 2021 Hmong Medical Corpus Project"

# project_url
__url__ = "https://corpus.ap-southeast-2.elasticbeanstalk.com/hminterface"

# author
__author__ = "Nathan M. White"
__author_email__ = "nathan.white1@my.jcu.edu.au"

def fix_line(line_in):
    """
    fix_line preprocesses a line to ensure spacing errors are removed
        and legal and website references are simplified
    @param line_in : string to preprocess
    returns : string that has undergone preprocessing
    """
    line = line_in
    # fix website addresses -- pull in from other sources
    line = re.sub(' ht ml ', ' html ', line)
#    line = re.sub(' ')
    # fix wrongly spaced Hmong words
    line = re.sub(' ci ali ', ' ciali ', line)
    line = re.sub(' ua s ', ' uas ', line)
    line = re.sub(' u as ', ' uas ', line)
    line = re.sub(' c oob ', ' coob ', line)
    line = re.sub(' dai m ', ' daim ', line)
    line = re.sub(' P hab ', ' Phab ', line)
    line = re.sub(' n tawv ', ' ntawv ', line)
    line = re.sub(' ntaw v ', ' ntawv ', line)
    line = re.sub(' l ossis ', ' lossis ', line)
    line = re.sub(' loss is ', ' lossis ', line)
    line = re.sub(' t au ', ' tau ', line)
    line = re.sub(' p hiajxwm ', ' phiajxwm ', line)
    line = re.sub(' ra u ', ' rau ', line)
    line = re.sub(' th iab ', ' thiab ', line)
    line = re.sub(' nt xiv ', ' ntxiv ', line)
    line = re.sub(' nr og ', ' nrog ', line)
    line = re.sub(' ta u ', ' tau ', line)
    line = re.sub(' losx ij ', ' losxij ', line)
    line = re.sub(' te j ', ' tej ', line)
    line = re.sub(' t ej ', ' tej ', line)
    line = re.sub(' Te j ', ' Tej ', line)
    line = re.sub(' la ixees ', ' laixees ', line)
    line = re.sub(' t xoj ', ' txoj ', line)
    line = re.sub(' tx aus ', ' txaus ', line)
    line = re.sub(' ntaw d ', ' ntawd ', line)
    line = re.sub(' ya m ', ' yam ', line)
    line = re.sub(' pa b ', ' pab ', line)
    line = re.sub(' p ab ', ' pab ', line)
    line = re.sub(' ne eg ', ' neeg ', line)
    line = re.sub(' tsa m ', ' tsam ', line)
    line = re.sub(' co v ', ' cov ', line)
    line = re.sub(' c ov ', ' cov ', line)
    line = re.sub(' Co v ', ' Cov ', line)
    line = re.sub(' u a ', ' ua ', line)
    line = re.sub(' mu ab ', ' muab ', line)
    line = re.sub(' m uab ', ' muab ', line)
    line = re.sub(' mua b ', ' muab ', line)
    line = re.sub(' txiavtxi m ', ' txiavtxim ', line)
    line = re.sub(' p hiaj ', ' phiaj ', line)
    line = re.sub(' pabc uam ', ' pabcuam ', line)
    line = re.sub(' txai s ', ' txais ', line)
    line = re.sub(' thia j ', ' thiaj ', line)
    line = re.sub(' r au ', ' rau ', line)
    line = re.sub(' c ov ', ' cov ', line)
    line = re.sub(' si v ', ' siv ', line)
    line = re.sub(' y uav ', ' yuav ', line)
    line = re.sub(' yua v ', ' yuav ', line)
    line = re.sub(' Nke eg ', ' Nkeeg ', line)
    line = re.sub(' ka wm ', ' kawm ', line)
    line = re.sub(' dejn um ', ' dejnum ', line)
    line = re.sub(' l os ', ' los ', line)
    line = re.sub(' lo s ', ' los ', line)
    line = re.sub(' xa v ', ' xav ', line)
    line = re.sub(' cu am ', ' cuam ', line)
    line = re.sub(' l ub ', ' lub ', line)
    line = re.sub(' xe eb ', ' xeeb ', line)
    line = re.sub(' x eeb ', ' xeeb ', line)
    line = re.sub(' ke v ', ' kev ', line)
    line = re.sub(' K ev ', ' kev ', line)
    line = re.sub(' q hov ', ' qhov ', line)
    line = re.sub(' Qho v ', ' Qhov ', line)
    line = re.sub(' tiv t haiv ', ' tiv thaiv ', line)
    line = re.sub(' thia b ', ' thiab ', line)
    line = re.sub(' y am ', ' yam ', line)
    line = re.sub(' u a hauj ', ' ua hauj ', line)
    line = re.sub(' n ev ', ' nev ', line)
    line = re.sub(' tiv thai v ', ' tiv thaiv ', line)
    line = re.sub(' h auv ', ' hauv ', line)
    line = re.sub(' t xiag ', ' txiag ', line)
    line = re.sub(' T us ', ' Tus ', line)
    line = re.sub(' Hli s ', ' Hlis ', line)
    line = re.sub( ' zo g ', ' zog ', line)
    line = re.sub(' t haum ', ' thaum ', line)
    line = re.sub(' th aum ', ' thaum ', line)
    line = re.sub(' tha um ', ' thaum ', line)
    line = re.sub(' thau m ', ' thaum ', line)
    line = re.sub(' ntxi v ', ' ntxiv ', line)
    line = re.sub(' H moob ', ' Hmoob ', line)
    line = re.sub(' ntsua s ', ' ntsuas ', line)
    line = re.sub(' m us ', ' mus ', line)
    line = re.sub(' t iv thaiv ', ' tiv thaiv ', line)
    line = re.sub(' T XOG ', ' TXOG ', line)
    line = re.sub(' tx og ', ' txog ', line)
    line = re.sub(' nt awv ', ' ntawv ', line)
    line = re.sub(' q og ', ' qog ', line)
    line = re.sub(' ya m ', ' yam ', line)
    line = re.sub(' ts hwm ', ' tshwm ', line)
    line = re.sub(' k om ', ' kom ', line)
    line = re.sub(' ts is ', ' tsis ', line)
    line = re.sub(' k ev ', ' kev ', line)
    line = re.sub(' n eeg ', ' neeg ', line)
    line = re.sub(' p ab ', ' pab ', line)
    line = re.sub(' t sev ', ' tsev ', line)
    line = re.sub(' ts ev ', ' tsev ', line)
    line = re.sub(' t om ', ' tom ', line)
    line = re.sub(' ntaw d ', ' ntawd ', line)
    line = re.sub(' ne eg ', ' neeg ', line)
    line = re.sub(' thi ab ', ' thiab ', line)
    line = re.sub(' co v ', ' cov ', line)
    line = re.sub(' hee v ', ' heev ', line)
    line = re.sub(' n ws ', ' nws ', line)
    line = re.sub(' MO B ', ' MOB ', line)
    line = re.sub(' m ob ', ' mob ', line)
    line = re.sub(' tx iav ', ' txiav ', line)
    line = re.sub(' txia v ', ' txiav ', line)
    line = re.sub(' pl aub ', ' plaub ', line)
    line = re.sub(' T U ', ' TU ', line)
    line = re.sub(' n yob ', ' nyob ', line)
    line = re.sub(' x av ', ' x av ', line)
    line = re.sub(' qhi a ', ' qhia ', line)
    line = re.sub(' q hia ', ' qhia ', line)
    line = re.sub(' qh ia ', ' qhia ', line)
    line = re.sub(' mu ab ', ' muab ', line)
    line = re.sub(' sa u ', ' sau ', line)
    line = re.sub(' t us ', ' tus ', line)
    line = re.sub(' yu av ', ' yuav ', line)
    line = re.sub(' Y a v ', ' Yav ', line)
    line = re.sub(' yogi b ', ' yog ib ', line)
    line = re.sub(' p haus ', ' phaus ', line)
    line = re.sub(' pl ab ', ' plab ', line)
    line = re.sub(' p l ab ', ' plab ', line)
    line = re.sub(' k oj ', ' koj ', line)
    line = re.sub(' t ab ', ' tab ', line)
    line = re.sub(' n o ', ' no ', line)
    line = re.sub(' t swv yim ', ' tswv yim ', line)
    line = re.sub(' xwm ye em ', ' xwm yeem ', line)
    line = re.sub(' ntx iv ', ' ntxiv ', line)
    line = re.sub(' t sw ', ' tsw ', line)
    line = re.sub(' z og ', ' zog ', line)
    line = re.sub(' Tx au ', ' Txau ', line)
    line = re.sub(' n tawm ', ' ntawm ', line)
    line = re.sub(' h u ', ' hu ', line)
    line = re.sub(' t hiab ', ' thiab ', line)
    line = re.sub(' ra u ', ' rau ', line)
    line = re.sub(' t shaj ', ' tshaj ', line)
    line = re.sub(' pu as ', ' puas ', line)
    line = re.sub(' U a ', ' Ua ', line)
    line = re.sub(' C ov ', ' Cov ', line)
    line = re.sub(' tshu aj ', ' tshuaj ', line)
    line = re.sub(' qh ov ', ' qhov ', line)
    line = re.sub(' tx wv ', ' txwv ', line)
    line = re.sub(' lo ssis ', ' lossis ', line)
    line = re.sub(' lw m ', ' lwm ', line)
    line = re.sub(' yua v ', ' yuav ', line)
    line = re.sub(' t uaj ', ' tuaj ', line)
    line = re.sub(' tua j ', ' tuaj ', line)
    line = re.sub(' ha ujlwm ', ' haujlwm ', line)
    line = re.sub(' Haujl wm ', ' Haujlwm ', line)
    line = re.sub(' haujl wm ', ' haujlwm ', line)
    line = re.sub(' haujlw m ', ' haujlwm ', line)
    line = re.sub(' i b ', ' ib ', line)
    line = re.sub(' H ais ', ' Hais ', line)
    line = re.sub(' h ais ', ' hais ', line)
    line = re.sub(' ha is ', ' hais ', line)
    line = re.sub(' hai s ', ' hais ', line)
    line = re.sub(' yee m ', ' yeem ', line)
    line = re.sub(' du a ', ' dua ', line)
    line = re.sub(' t es ', ' tes ', line)
    line = re.sub(' c ai ', ' cai ', line)
    line = re.sub(' ca i ', ' cai ', line)
    line = re.sub(' hli s ', ' hlis ', line)
    line = re.sub(' coo b ', ' coob ', line)
    line = re.sub(' Nta w m ', ' Ntawm ', line)
    line = re.sub(' ra ug ', ' raug ', line)
    line = re.sub(' p om ', ' pom ', line)
    line = re.sub(' sai b ', ' saib ', line)
    line = re.sub(' tu s ', ' tus ', line)
    line = re.sub(' l ees ', ' lees ', line)
    line = re.sub(' hnu b ', ' hnub ', line)
    line = re.sub(' nw s ', ' nws ', line)
    line = re.sub(' cai j ', ' caij ', line)
    line = re.sub(' txi m ', ' txim ', line)
    line = re.sub(' tx h eem ', ' txheem ', line)
    line = re.sub(' N TIAG ', ' NTIAG ', line)
    line = re.sub(' mua j ', ' muaj ', line)
    line = re.sub(' tsaw g ', ' tsawg ', line)
    line = re.sub(' ntsia b ', ' ntsiab ', line)
    line = re.sub(' nt au ', ' ntau ', line)
    line = re.sub(' txa is ', ' txais ', line)
    line = re.sub(' t ias ', ' tias ', line)
    line = re.sub(' ku j ', ' kuj ', line)
    line = re.sub(' s aib ', ' saib ', line)
    line = re.sub(' K ho ', ' Kho ', line)
    line = re.sub(' k ho ', ' kho ', line)
    line = re.sub(' kh o ', ' kho ', line)
    line = re.sub(' h ais ', ' hais ', line)
    line = re.sub(' q is ', ' qis ', line)
    line = re.sub(' nt awv ', ' ntawv ', line)
    line = re.sub(' ko m ', ' kom ', line)
    line = re.sub(' nta wm ', ' ntawm ', line)
    line = re.sub(' ntaw m ', ' ntawm ', line)
    line = re.sub(' f eem ', ' feem ', line)
    line = re.sub(' Fee m ', ' Feem ', line)
    line = re.sub(' n yuaj ', ' nyuaj ', line)
    line = re.sub(' ch aw ', ' chaw ', line)
    line = re.sub(' c haw ', ' chaw ', line)
    line = re.sub(' cha w ', ' chaw ', line)
    line = re.sub(' y eem ', ' yeem ', line)
    line = re.sub(' k iag ', ' kiag ', line)
    line = re.sub(' T hawj ', ' Thawj ', line)
    line = re.sub(' N eej ', ' Neej ', line)
    line = re.sub(' raw s ', ' raws ', line)
    line = re.sub(' ra ws ', ' raws ', line)
    line = re.sub(' q ab ', ' qab ', line)
    line = re.sub(' qa b ', ' qab ', line)
    line = re.sub(' koo m ', ' koom ', line)
    line = re.sub(' dh au ', ' dhau ', line)
    line = re.sub(' c uam ', ' cuam ', line)
    line = re.sub(' Xee v ', ' Xeev ', line)
    line = re.sub(' xee v ', ' xeev ', line)
    line = re.sub(' Tsa v ', ' Tsav ', line)
    line = re.sub(' Kw s ', ' Kws ', line)
    line = re.sub(' k ws ', ' kws ', line)
    line = re.sub(' tu g ', ' tug ', line)
    line = re.sub(' si s ', ' sis ', line)
    line = re.sub(' t sis ', ' tsis ', line)
    line = re.sub(' t wg ', ' twg ', line)
    line = re.sub(' xyu as ', ' xyuas ', line)
    line = re.sub(' m enyuam ', ' menyuam ', line)
    line = re.sub(' txhaw b ', ' txhawb ', line)
    line = re.sub(' ni as ', ' nias ', line)
    line = re.sub(' Nta ub ', ' Ntaub ', line)
    line = re.sub(' t ab ', ' tab ', line)
    line = re.sub(' n yiaj ', ' nyiaj ', line)
    line = re.sub(' tse g ', ' tseg ', line)
    line = re.sub(' t hem ', ' them ', line)
    line = re.sub(' h au ', ' hau ', line)
    line = re.sub(' ha u ', ' hau ', line)
    line = re.sub(' t hov ', ' thov ', line)
    line = re.sub(' zau m ', ' zaum ', line)
    line = re.sub(' p laws ', ' plaws ', line)
    line = re.sub(' hl i ', ' hli ', line)
    line = re.sub(' h li ', ' hli ', line)
    line = re.sub(' ntia v ', ' ntiav ', line)
    line = re.sub(' t eeb ', ' teeb ', line)
    line = re.sub(' tia v ', ' tiav ', line)
    line = re.sub(' k heej ', ' kheej ', line)
    line = re.sub(' kh eej ', ' kheej ', line)
    line = re.sub(' khe ej ', ' kheej ', line)
    line = re.sub(' khee j ', ' kheej ', line)
    line = re.sub(' sijh awm ', ' sijhawm ', line)
    line = re.sub(' r huav ', ' rhuav ', line)
    line = re.sub(' t xiaj ', ' txiaj ', line)
    line = re.sub(' ti b ', ' tib ', line)
    line = re.sub(' L ub ', ' Lub ', line)
    line = re.sub(' xua b ', ' xuab ', line)
    line = re.sub(' o b ', ' ob ', line)

    # replace legal references
    line = re.sub('(Cal \. )?Code Reg ?s \.( ,)? tit \. [0-9]{1,} , §{1,2} [0-9]{2,} \. [0-9]{1,}(( \( [A-Za-z1-9] \))|( thiab))*( , [0-9]{1,} \. [0-9]{1,}( \( [A-Za-z1-9] \))*)*',\
                  'Cal Code',\
                  line)
    line = re.sub('Cal \. Code Regs \. tit \. [0-9] , §{2} [0-9]{4} \. [0-9]{3} , [0-9]{4} \. [0-9]{3}', 'Cal Code', line)
    line = re.sub('Welf((are|( \.)) & Inst \.( Code)? § ?[0-9]{1,}( \. [0-9]{1,})*(( -)? \( [A-Za-z1-9] \))*)', 'Welfare Code', line)
    line = re.sub('Welf . & Inst . Code , ', '', line)
    # Matches pattern 42 C . F . R . §§ 438 . 402 ( c ) ( 3 ) ( ii ) and 438 . 406 ( b ) ( 3 )
    line = re.sub('[0-9]{1,} *C *\. *F *\. *R *\. *§§ *[0-9]{1,} *\. *[0-9]{1,} *( *\( *[A-Za-z0-9]{1,} *\) *)* *and *[0-9]{1,} *\. *[0-9]{1,} ( *\( *[A-Za-z0-9]{1,} *\) *)*', ' Code ', line)

    line = re.sub('[0-9]{1,} C \. F \. R \. §{1,2} ?[0-9]{1,3} ?\. ?[0-9]{1,3} ?& ?[0-9]{1,3} ?\. ?[0-9]{1,3}( ?\( ?[A-Za-z0-9]{1,3} ?\))*', ' Code ', line)
    line = re.sub('[0-9]{1,} C( ?\. ?)?[CF]( ?\. ?)?R( ?\.)? ?§{1,2}(§? ?[0-9]{1,}( ?\. ?[0-9]{1,})+((( ?\( ?[A-Za-z1-9]{1,3} ?\))*)|( ?(and)|( ?& ?))|( ?- ?))*)+', ' Code ', line)
    # Matches pattern §§300 . 110 & 300 . 114 . 2
    line = re.sub('§§ *[0-9]{1,} *\. *[0-9]{1,} *& *[0-9]{1,}( *\. *[0-9]{1,})*', ' Code ', line)
    # Matches pattern § 12300 . 4- 12301 . 1
    line = re.sub('§ *[0-9]{1,} *\. *[0-9]{1,} *- *[0-9]{1,} *\. *[0-9]{1,}', ' Code ', line)
    # Matches pattern § 12300 . 4 ( d ) ( 3 ) ( B ) ( i ) - ( iii )
    line = re.sub('§ *[0-9]{1,} *\. *[0-9]{1,}( *\( *[A-Za-z0-9]{1,} *\) *)* *- *\( *[A-Za-z0-9]{1,} *\)', ' Code ', line)
    line = re.sub('§{1,2}(§? *[0-9]{1,}( *\. *[0-9]{1,})+((( *\( *[A-Za-z1-9]{1,3} *\))*)|(( *and)|( *& *)|( *- *)))*)+', ' Code ', line)
    # 34 C . F . R . §§ 300 . 42 & 300 . 114 ( a ) ( 2 )
    # 20 U . S . C . § 1414 ( 3 ) ( B ) ( iii )

    # the following line may be obsolete: need to test
    line = re.sub('§{1,2} ?[0-9]{1,} ?\. ?[0-9]{1,}( \. [0-9]{1,})*(( ?-)? ?\( ?[A-Za-z1-9]{1,4} ?\))*', ' Code ', line)
    # Matches pattern MPP 30-757.173 (a) (2) thiab (3)
    line = re.sub('MPP *[0-9]{1,} *-[0-9]{1,} *\. *[0-9]{1,}(\( *[A-Za-z0-9]{1,} *\))* *thiab *\( *[A-Za-z0-9]{1,} *\)', ' Code ', line)
    # Matches pattern MPP 30- 172 . ( b ) ( 3 ) thiab ACL 98- 87
    line = re.sub('MPP *[0-9]{1,} *- *[0-9]{1,} *\.( *\( *[A-Za-z0-9]{1,} *\))* *thiab *ACL *[0-9]{1,} *- *[0-9]{1,}', ' Code ', line)
    # Matches pattern MPP 30-757; MPP 30-757.173 (a)
    line = re.sub('MPP *[0-9]{1,} *-[0-9]{1,} *; *MPP *[0-9]{1,} *-[0-9]{1,} *\. *[0-9]{1,} *(\( *[A-Za-z0-9]{1,} *\))*', ' Code ', line)
    # Matches pattern MPP 30- 757 . 173
    line = re.sub('MPP *[0-9]{1,} *- *[0-9]{1,} *\. *[0-9]{1,}( *\( *[A-Za-z0-9]{1,} *\))*', ' Code ', line)
    # Matches pattern MPP 30-701 (s) (1)
    line = re.sub('MPP *[0-9]{1,} *- *[0-9]{1,}( *\( *[A-Za-z0-9]{1,} *\))*', ' Code ', line)

    line = re.sub('MPP § [0-9]{1,}- [0-9]{1,} \. [0-9]{1,}', 'MPP Code', line)
    line = re.sub(' ?Code *\. ? § ?\.? ?[0-9]{1,}( \. [0-9]{1,})*(( -)? \( [A-Za-z1-9]{1,3} \))*', ' Code ', line)
    line = re.sub('§ ?[0-9]{1,}( ?\. ?[0-9]{1,})*(( -)? \( ?[A-Za-z1-9]{1,3} ?\))*', ' Code ', line)
#    line = re.sub(' [0-9]{1,2} C ?\. ?F ?\. ?R ?\. ?§ [0-9]{1,})*(( ?-)? ?\(? ?[A-Za-z1-9]{1,4} ?\)?)*
    line = re.sub('[0-9]{1,2} U ?\. ?S ?\. ?C', ' Code ', line)
    line = re.sub('U ?\. S ?\. C ?\. ?, ', '', line)
    line = re.sub('C ?\. F ?\. R ?\. ?, ', '', line)
    line = re.sub(' Code [0-9]{1,} ?\. ? [0-9]{1,}', ' Code ', line)
#    line = re.sub(' *Code *- *\( *[A-Za-z0-9]{1,3} *\)', ' Code ', line)

    # Replace problematic abbreviations
    line = re.sub('U ?\. ?C ?\.', 'UC', line)
    line = re.sub('U ?\. ?S ?\.', 'US', line)

    # Remove page and publication numbers in English
    line = re.sub('Page [0-9]{1,} of [0-9]{1,}( [0-9]{1,})?', '', line)
    line = re.sub(', Pub( ?\.)? # ?[0-9]{1,}( ?\. ?[0-9 ]{1,})?', 'Pub', line)
    line = re.sub('Pub( ?\.)? # ?[0-9]{1,}( ?\. ?[0-9]{1,})?', 'Pub', line)

    # Remove page numbers in Hmong
    line = re.sub('Nplooj [0-9]{1,} ntawm [0-9]{1,}', '', line)

    # Remove erroneous stray elements
    line = re.sub("'Medi-", '', line)
    line = re.sub('Vvlk6t Ir KUk', '', line)

    # Fix currency references
    # TODO: and remember to not split on one of these below
    line = re.sub('\. ?([0-9]) ([0-9])', '.\g<1>\g<2>', line)
    line = re.sub('([0-9]{1,}) ?\. ?([0-9]{2})', '\g<1>.\g<2>', line)

    # close hyphens in phone numbers
    line = re.sub('([0-9]{3})- ([0-9]{4})', '\g<1>-\g<2>', line)

    # close spaces in numbers with decimals
    line = re.sub('([0-9]) ?\. ?([0-9])', '\g<1>.\g<2>', line)

    # TODO: close spacing in URLs
    line = re.sub('http : / / www . ', 'http://www.', line)
    # deals with www.dss.cahwnet.gov
    line = re.sub('www *\. *dss *\. *cahwnet *\. *gov', 'www.website.net', line)
    line = re.sub('www ?\. ?[A-Za-z]{1,} ?\.( ?(ca|mn|wi) ?\.)? ?(htm|net|com|org|edu|gov)', 'www.website.net', line)
    line = re.sub('http[A-Za-z0-9.\-/: ]+?(net|NET|com|COM|org|ORG|edu|EDU|gov|GOV|us|US)', 'http://www.website.net', line)
    line = re.sub('www[A-Za-z0-9.\-/: ]+?(net|NET|com|COM|org|ORG|edu|EDU|gov|GOV|us|US)', 'www.website.net', line)
    line = re.sub('www[A-Za-z0-9.\-/: ]+?(net|NET|com|COM|org|ORG|edu|EDU|gov|GOV|us|US)[A-Za-z0-9.\-/: ]+?(htm|HTM|html|HTML|pdf|PDF)', 'www.website.net', line)
    line = re.sub('[A-Za-z0-9]{1,}( \. [A-Za-z0-9]{1,})*@[A-Za-z0-9]{1,} ?\. ?((ca|mn|wi) ?\. ?)? (htm|net|com|org|edu|gov|pdf|us)', 'email@website.net', line)

    # clear misguided spacing for punctuation;
    #  leave quotation marks alone due to ambiguity
    line = re.sub(' ([.,!?):;])', '\g<1>', line)
    line = re.sub('[(] ', '(', line)
    line = re.sub('([A-Za-z0-9])- ', '\g<1>-', line)

    # Remove table of contents dots
    line = re.sub('\.{10,}', '.', line)

    # Replace PDF-based erroneous use of '™'
    line = re.sub('™', "'", line)

    # close multiple spaces
    line = re.sub(' {2,}', ' ', line)

    line = re.sub('\. *\,* *Code *\.', '.', line) # Clear out "code" only references. 
    line = re.sub('\. *, *Code *\.', '.', line)
    line = re.sub('\. *Code *\.', '.', line)

    return line

def split_paragraphs(data_in):
    # TODO: check if delimitation logic matches the actual files
    # acceptable except for titles in KNH
    # need to check others
    """split_paragraphs finds paragraph delimitations based on whether a
    line ends in sentence-terminating punctuation.
    @param data_in : the raw data in the form of a list of strings
    returns : a list of lists representing paragraphs containing strings"""

    # check if final line has punctuation
    if data_in[-1][-1] not in ['.', '!', '?', '"']:
        final_punc = False
    elif data_in[-1][-1] == '"':
        if data_in[-1][-2] not in ['.', '!', '?']:
            final_punc = False
        else:
            final_punc = True
    else:
        final_punc = True

    paras = []
    current_para = []

    # loop through lines in data_in and append
    for line in data_in:
        current_para.append(line)
        if len(line) > 1:
            if line[-2:] in ['."', '!"', '?"', '. "', '! "', '? "']:
                paras.append(current_para)
                current_para = []
        if len(line) > 0:
            if line[-1] in ['.', '!', '?']:
                paras.append(current_para)
                current_para = []
    # if final element has no punctuation, append non-empty current_para
    if final_punc == False and len(current_para) > 0:
        paras.append(current_para)

    return paras

def split_sentences(paras_in, fix_line=False):
    """
    split_sentences splits paragraphs into sentences based on
    positions of punctuation.
    @param paras_in : list of strings representing paragraphs
    @param fix_line : boolean indicating whether line should be processed
        by fix_line function
    returns : list of lists where each list is a paragraph
        containing sentences as strings
    """
    paras_out = []
    for item in paras_in:
        current_para = []
        remaining_line = item
        if fix_line:
            remaining_line = fix_line(remaining_line)
        while True:
            re_to_match = '(?<![1-9])(?<![1-9] )(?<! [1-9] )(?<! [A-Fa-fv] )(?<! [A-Fa-fv])(?<!^[A-Fa-f])(?<!^[A-Fa-f] )(?<!www)[.!?]{1,} ?\)?"?(?!(htm|net|com|org|edu|gov|pdf|asp))'
            found = re.search(re_to_match, remaining_line)
            #if re.search('\. org/', remaining_line):
            #    print("It's working")
            # loop to prevent split on:
            #  1) numbers and amounts with decimal points inside
            #  2) periods in email addresses: TODO testing
            if found != None:
                pos = found.span()[1]
                current = remaining_line[pos-1]
                if len(remaining_line) > pos and current == '.':
                    while True:
                        _prev = remaining_line[pos-2]
                        # if the next position raises an exception, then end of string and no split found
                        try:
                            _next = remaining_line[pos]
                        except IndexError:
                            found = None
                            break
                        # logic here assumes that digit + period + digit is not to be split upon
                        if _prev in string.digits and _next in string.digits:
                            found = re.search(re_to_match, remaining_line[pos:])
                            if found == None: # if None, then there is no remaining relevant punctuation
                                break
                            pos = found.span()[1] + pos
                            first_test = True
                        else:
                            first_test = False
                        # TODO: check if superseded by email address simplification above
                        at_pos_prev = re.search('[A-Za-z0-9]{1,}@[A-Za-z0-9] ?\.$', remaining_line[:pos])
                        at_pos_next = re.search('^[A-Za-z0-9\. ]{1,}@', remaining_line[pos:])
                        if at_pos_prev != None or at_pos_next != None:
                            found = re.search(re_to_match, remaining_line[pos:])
                            if found == None:
                                break
                            pos = found.span()[1] + pos
                            second_test = True
                        else:
                            second_test = False
                        # this position is not a decimal point, so treat as regular punctuation
                        if not (first_test or second_test):
                            break
            # add if found is None in any case, as there is no remaining relevant punctuation
            if found == None:
                if len(remaining_line) > 0:
                    current_para.append(remaining_line)
                break
            # append up to the punctuation and slice the remaining
            #  and do not allow junk sequences into the final version
            if remaining_line[:pos] not in ['! "', 'Cal Code.']:
                current_para.append(remaining_line[:pos])
            if pos < len(remaining_line):
                remaining_line = remaining_line[pos:]
            else: # remaining_line is exhausted or zero-length string
                break
        paras_out.append(current_para)
    # clears out leading spaces and spaces before final punctuation, if they remain
    paras_final = []
    for para in paras_out:
        current_para = []
        for line in para:
            current_line = line.strip(' ')
            if len(current_line) > 1:
                # this may have already been superseded by the new logic in fix_line
                # TODO: check on this and revise
                if current_line[-2] == ' ' and current_line[-1] in ['.', '!', '?']:
                    current_para.append(current_line[:-2] + current_line[-1])
                else:
                    current_para.append(current_line)
            else:
                current_para.append(current_line)
        paras_final.append(current_para)
    return paras_final

def insert_lines(data_in):
    """
    insert_lines inserts empty lines between each paragraph.
    @param data_in : sequences of sentences grouped in paragraphs
    returns : a list of strings containing the full document
    """
    empty_lines = [[""]] * len(data_in)
    spaced_data = zip(data_in, empty_lines)
    spaced_data = [line for pair in spaced_data for line in pair][:-1]
    flattened_data = [line for series in spaced_data for line in series]
    return flattened_data

def preprocess_texts(filenames, filepath):
    processed_data_path = 'albert_first_preprocess'
    # e.g. albert_first_preprocess/pretrain/med_like/disabilityrightsCA
    target_path = re.sub('albert_raw_data', processed_data_path, filepath)

    for file in filenames:
        if os.path.isdir(file):
            continue
        f = open(file, 'r')
        data = f.readlines()
        f.close()
        data = [l.strip() for l in data]
        # find paragraphs based on [.!?] or combinations [."!"?"]
        while True:
            # file is in fact empty
            if len(data) == 0:
                empty = True
                break
            # truncate if final line is empty
            elif len(data[-1]) == 0:
                data = data[:-1]
            else:
                empty = False
                break
        if empty == True:
            continue
        paras = split_paragraphs(data)
        # join content within paragraphs and split on [.!?] and [."!"?"]
        paras = [' '.join(p) for p in paras]
        lines = split_sentences(paras)
        # insert extra line after each paragraph
        final_lines = insert_lines(lines)
        # save output data to file
        output_path = target_path + os.path.sep + file
        try:
            out_f = open(output_path, 'w')
        except OSError:
            print("OSError: path " + target_path + " does not exist.")
            raise
        else:
            for line in final_lines:
                out_f.write(line)
                out_f.write('\n')
            out_f.close()

def single_process_text(filename):
    """
    single_process_text preprocesses a single file
    @param filename : the path to the file to be preprocessed
    returns : a list of preprocessed lines
    """
    f = open(filename, 'r')
    data = f.readlines()
    data = [l.strip() for l in data]
    paras = split_paragraphs(data)
    paras = [' '.join(p) for p in paras]
    lines = split_sentences(paras)
    final_lines = insert_lines(lines)
    return final_lines

if __name__ == "__main__":
    # argv[1] should have the relative folder filepath
    filepath = sys.argv[1]
    try:
        os.chdir(filepath)
    except FileNotFoundError:
        print("The filepath %s does not refer to a folder that exists.", filepath)
    else:
        files = os.listdir(filepath)
        preprocess_texts(files, filepath)
