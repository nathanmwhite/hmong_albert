import os
import re
import sys

def process_text(filename, cased=False):
    replacement_pairs = [(' lb', ' Ib'),
                         ('(?<=[aeiowhH])rn(?=[.,!? ])', 'm'),
                         ('rnlaug', 'mlaug'),
                         ('rnuag', 'muag'),
                         (' pooh', ' poob'),
                         ('ii', 'li'),
                         (' Ii', ' li'),
                         (' B(?!([ae]r|ea|ang))', ' Np'),
                         (' b(?!([ae]r|ea|ang))', ' np'),
                         (' G(?!(AIN|eo|er))', ' Nk'),
                         (' g(?!(ain|eo|er))', ' nk'),
                         (' J(?!(un|ap))', ' Nts'),
                         (' j(?!(un|ap))', ' nts'),
                         (' nyh', ' hny'),
                         (' Nyh', ' Hny'),
                         (' nhy', ' hny'),
                         (' Nhy', ' Hny')]

    f = open(filename, 'r+')
    input_ = f.readlines()
    output = []
    for line in input_:
        line_out = line
        for item in replacement_pairs:
            if cased == True:
                replacement = item[1]
            else:
                replacement = item[1].lower()
            line_out = re.sub(item[0], replacement, line_out)
        output.append(line_out)
    f.seek(0)
    f.write(''.join(output))
    f.close()

if __name__ == '__main__':
    try:
        cased_val = sys.argv[1]
    except IndexError:
        print('Need to specify case value: -c or -u')
    if cased_val == '-c':
        cased = True
    elif cased_val == '-u':
        cased = False
    else:
        raise ValueError('Case value not valid: ' + cased_val)
    if os.path.basename(os.getcwd()) == 'knh':
        filenames = os.listdir()
        for file in filenames:
            process_text(file, cased)
    else:
        raise IOError('Wrong folder to complete text preprocessing: ' +\
                      str(os.getcwd()))
    
