import sys
import collections


def getTextLines(filename):
    fp = open(filename, encoding='UTF-8')
    textLines = fp.readlines()
    fp.close()

    return textLines


def checkIp(textLines, ip):

    counter = collections.Counter()

    for line in textLines:
        words = line.split()
        if words[0] == ip:
            counter[words[0]] += 1

    if sum(counter.values()) == 0:
        counter[ip] = 0

    return counter


def requestVal(textLines):

    counter = collections.Counter()

    for line in textLines:
        words = line.split()
        counter[words[0]] += 1

    return counter


def meanVal(textLines):

    ipSet = set()
    mean = 0
    for line in textLines:
        words = line.split()
        ipSet.add(words[0])

    if len(ipSet) != 0:
        mean = round(sum(1 for _ in textLines) / len(ipSet))

    return mean


if __name__ == '__main__':

    textLines = getTextLines(sys.argv[1])

    counter = checkIp(textLines, "79.136.245.135")
    for ip in counter:
        print("Запросов с {} сделано -- {}".format(ip, counter[ip]))

    counter = checkIp(textLines, "127.0.0.1")
    for ip in counter:
        print("Запросов с {} сделано -- {}".format(ip, counter[ip]))

    counter = requestVal(textLines)
    for word, cnt in counter.most_common(1):
        print("Максимальное число запросов с {} -- {}".format(word, cnt))

    counter = requestVal(textLines)
    n = 2
    for word, cnt in counter.most_common()[:-n-1:-1]:
        print("Минимальное число запросов с {} -- {}".format(word, cnt))

    meanRequest = meanVal(textLines)
    print("Среднее число запросов -- {}".format(meanRequest))
