import sys
import collections


def checkIp(filename, ip):
    fp = open(filename, encoding='UTF-8')
    textLines = fp.readlines()
    fp.close()

    counter = collections.Counter()

    for line in textLines:
        words = line.split()
        if words[0] == ip:
                counter[words[0]] += 1
    
    if sum(counter.values()) == 0:
        counter[ip] = 0

    return counter

if __name__ == '__main__':
   
    counter = checkIp(sys.argv[1], "79.136.245.135")
    for ip in counter:
        print("Запросов с {} сделано -- {}".format(ip, counter[ip]))

    counter = checkIp(sys.argv[1], "127.0.0.1")
    for ip in counter:
        print("Запросов с {} сделано -- {}".format(ip, counter[ip]))
