import os
from os.path import join as jph
import argparse
import time


def commenter(pfi_input, pfi_output, add_comments):

    assert os.path.exists(pfi_input)

    comment = False

    if add_comments == 'True':

        f1 = open(pfi_output, 'w')
        with open(pfi_input, 'r') as f_in:
            for line in f_in:

                if line.startswith('%c-end'):
                    comment = False

                if comment:
                    f1.write('% ' + line)
                else:
                    f1.write(line)

                if line.startswith('%c-start'):
                    comment = True

        f1.close()

    elif add_comments == 'False':

        f1 = open(pfi_output, 'w')
        with open(pfi_input, 'r') as f_in:
            for line in f_in:

                if line.startswith('%c-start'):
                    comment = True

                if comment:
                    # assert line.startswith('% ')
                    f1.write(line.replace('% ', ''))
                else:
                    f1.write(line)

                if line.startswith('%c-end'):
                    comment = False

        f1.close()

    else:
        raise IOError


def main():
    """
    Usage:
    python commenter.py -i <path to input.tex> -o <path to output.tex> -comment  # to add commments
    python commenter.py -i <path to input.tex> -o <path to output.tex> -uncomment  # to remove commments
    """
    parser = argparse.ArgumentParser(description='Add remove comments in tex file.')

    parser.add_argument('-i', '--input',
                        dest='in_tex',
                        type=str,
                        required=True,
                        help='input tex file.')

    # pfo_study_nifti_output
    parser.add_argument('-o', '--output',
                        dest='out_tex',
                        type=str,
                        required=True,
                        help='output tex file.')

    parser.add_argument('-comment',
                        dest='comment',
                        action='store_true',
                        help='add comments between c-start and c-end.')

    parser.add_argument('-uncomment',
                        dest='uncomment',
                        action='store_true',
                        help='remove comments between c-start and c-end.')

    args = parser.parse_args()
    print('Input:')
    print(args.in_tex, args.out_tex, args.comment, args.uncomment)
    if args.comment == args.uncomment:
        raise IOError
    if args.comment:
        print('Add comments to file {} into {}.'.format(args.in_tex, args.out_tex))
        commenter(args.in_tex, args.out_tex, 'True')
        time.sleep(3)  # add some suspacnce!
        print('Done!')
    else:
        print('Remove comments to file {} into {}.'.format(args.in_tex, args.out_tex))
        commenter(args.in_tex, args.out_tex, 'False')
        time.sleep(3)  # add some suspacnce!
        print('Done!')


if __name__ == "__main__":
    main()
