#Lists
#Consider a list ( list = [] ). You can perform the following commands:
#1. insert i e : Insert integer at position .
#2. print : Print the list.
#3. remove e : Delete the first occurrence of integer .
#4. append e : Insert integer at the end of the list.
#5. sort : Sort the list.
#6. pop : Pop the last element from the list.
#7. reverse : Reverse the list.
#Initialize your list and read in the value of followed by lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#Input Format
#The first line contains an integer, , denoting the number of commands.
#Each line of the subsequent lines contains one of the commands described above.
#Constraints
#The elements added to the list must be integers.
#Output Format
#For each command of type print , print the list on a new line. 
#Sample Input 0
#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse 
#print
#Sample Output 0
#[6, 5, 10] [1, 5, 9, 10] [9, 5, 1]

if __name__ == '__main__':
    mainArr = []
    N = int(input())
    for seq in range(N):
        strinput = input()
        arrlist = strinput.split()
        defineDigit = arrlist[0]
        if defineDigit == 'insert':
            mainArr.insert(int(arrlist[1]), int(arrlist[2]))
        elif defineDigit == 'remove':
            mainArr.remove(int(arrlist[1]))
        elif defineDigit == 'append':
            mainArr.append(int(arrlist[1]))
        elif defineDigit == 'pop':
            mainArr.pop()
        elif defineDigit == 'sort':
            mainArr.sort()
        elif defineDigit == 'reverse':
            mainArr.reverse()
        elif defineDigit == 'print':
            print(mainArr)
