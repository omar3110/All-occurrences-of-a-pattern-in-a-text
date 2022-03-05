text = input("Enter a text: ")
pattern = input("Enter a pattern: ")


def occurences(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    print('Pattern occurrences: ', count)


occurences(text, pattern)

####################### Documentation #######################

'''
Step 1: Taking inputs of Text And Pattern from user

Step 2: Inputed values are stored in 2 arguements text and 
pattern in 'occurences' function

Step 3: In 'occurences' function a count variable with initial 
value 0 is declared to count pattern occurences

Step 4: A for loop iterates with i in range of subtraction of 
text value's length to pattern value's length. For an instance,
suppose, text = "papapma" and pattern = "pap". Here text value's 
length is 7 and pattern value's length is 3 which means 7-3 = 4
and 4 is the range of for loop.

Step 5: Every time i iterates in range it enters in if condition
and follow this condition text[i:i+len(pattern)] == pattern. Suppose,
text = "papapma" and pattern = "pap" and their length are 7 and 3 
respectively. So it follows this sequences,
            papapma[0:3] == pap, count = 1  ; where i = 0 
            papapma[1:4] == pap, count = 1  ; where i = 1
            papapma[2:5] == pap, count = 2  ; where i = 2
            papapma[3:6] == pap, count = 2  ; where i = 3
            papapma[4:7] == pap, count = 2  ; where i = 4
    
Following above sequences this algorithm checks every 3 indexes with pattern 
and if pattern matches with text 3 indexes' slice the count variable increases
by 1

Step 6: After completed iterations count variable gives final output by the print 
function to the terminal

'''
