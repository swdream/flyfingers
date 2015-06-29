import argparse

import flyfingers


def parse_args():
    parser = argparse.ArgumentParser(description=flyfingers.__doc__)
    sparsers = parser.add_subparsers(dest='subparser_name')
    sub_parser = sparsers.add_parser('run', help='start flyfingers')
    sub_parser.add_argument('run')
    sub_parser.set_defaults(func=getattr(flyfingers, 'run'))
    args = parser.parse_args()

    args.func(args.run)


if __name__ == '__main__':
    parse_args()
