#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


#Codestarts from here

fname = input("Enter the name of the file:")

fhand = open(fname)

dict = dict()
list1= list()

for line in fhand:
     if line.startswith('From'):
        if line.startswith('From:'):
            continue
        else:
            word= line.split()
            list1.append(word[1])
            

for word in list1:
    dict[word] = dict.get(word,0)+1


HC = None            #HC-High count
HCW = None           #HCW- High count -word

for emailid,senttimes in dict.items():   #Using tuples by dict structure
    if HC is None or senttimes >HC:      
        HCW= word
        HC = senttimes
        
print(HCW,HC)


# In line 25 for first time Since HC is none, the value for maximum count 
# will be None, from second iteration onwards if value of "Senttimes" is higher 
#than none obviously then it will get replaced and words will also be replaced 
#since we iterate through both elements in tuples type.
