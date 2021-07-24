# Practise > Python > Date & Time > Time Delta
# https://www.hackerrank.com/challenges/python-time-delta/problem

from datetime import datetime, timedelta


def diffCalc(list1, timeObject, timeZone):
    if list1[5][0] == '+':
        return timeObject - timeZone
    else:
        return timeObject + timeZone


monthDict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
             'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

rounds = int(input())
for i in range(rounds):
    first_str = input()
    second_str = input()
    anlist1 = (first_str.split())
    anlist2 = (second_str.split())

    timeObject1 = datetime(year=int(anlist1[3]), month=int(monthDict[anlist1[2]]), day=int(anlist1[1]), hour=int(anlist1[4].split(':')[
        0]), minute=int(anlist1[4].split(':')[1]), second=int(anlist1[4].split(':')[2]))
    timeObject2 = datetime(year=int(anlist2[3]), month=int(monthDict[anlist2[2]]), day=int(anlist2[1]), hour=int(anlist2[4].split(':')[
        0]), minute=int(anlist2[4].split(':')[1]), second=int(anlist2[4].split(':')[2]))

    timeZone1 = timedelta(
        hours=int(anlist1[5][1:3]), minutes=int(anlist1[5][3:]))
    timeZone2 = timedelta(
        hours=int(anlist2[5][1:3]), minutes=int(anlist2[5][3:]))
    timeDiff = (diffCalc(anlist1, timeObject1, timeZone1)) - \
        (diffCalc(anlist2, timeObject2, timeZone2))
    print(int(timeDiff.total_seconds()))
