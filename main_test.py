#!/usr/bin/env python3
from package1.folder2.sum import summ as sum
from package1.folder1 import produce

if __name__ == '__main__':
    print('In main\n')

    print('Calling sum(2,5)...')
    s = sum(2,5)
    print('Sum of 2 and 5 is:',s,'\n')
    print('Calling produce(8)...')
    produce.produce(8)
    