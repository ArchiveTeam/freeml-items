import sys


def main(type_, start, end):
    assert start % 100 == 0
    assert end % 100 == 99
    with open('{}_{}-{}.txt'.format(type_, start, end), 'w') as f:
        f.write('\n'.join('{}:{}-{}'.format(type_, a, a+99) for a in range(start, end, 100)))
        f.write('\n')

if __name__ == '__main__':
    main(sys.argv[1], *[int(i) for i in sys.argv[2:]])

