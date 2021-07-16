# Practise > Python > Strings > Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(mainStr):
    vowels = 'AEIOU'
    kevScore = 0
    stuScore = 0
    for i in range(len(mainStr)):
        if mainStr[i] in vowels:
            kevScore += (len(mainStr)-i)
        else:
            stuScore += (len(mainStr)-i)

    if kevScore > stuScore:
        print("Kevin", kevScore)
    elif kevScore < stuScore:
        print("Stuart", stuScore)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
