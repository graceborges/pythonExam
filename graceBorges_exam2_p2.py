#!/usr/bin/env python3
import sys

def main():

    if len(sys.argv) < 2:
        usage()
        return 0
    elif sys.argv[1] == 'default':
        f = open('/home/hvalle/submit/cs3030/files/sample_apache.log', 'rt')
    else:
        f = open(sys.argv[1])


    for line in f:     
        
        data = line.split('-')
        small = data[3].split()
        #print(small)
        print('Host:', data[0], '\tStatus: ', small[-2], '\tBytes Sent: ', small[-3])
        #print(data)


def usage():
    print('Usage: ./graceBorges_exam2_py2.py <some_log_file_I_included>')
    print('Just to let you know that if you just type in default it will show the file that was given to us in the assignment which then will be parsed through. Feel free to pass in another file instead')




if __name__ == '__main__':
    main()
