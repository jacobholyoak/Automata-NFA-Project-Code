
def insert(Dictionary, key, value):
    #print('key = ',key)
    #print('value = ',value)
    Dictionary[key].append(value)
    #print(Dictionary[key])
    #print()

def Read_Input_NFA():
    #parse/read the file/input line for {{NFA tuple}, input string}
    #if input string is null then ask user for string, print if that string is accepted, and repeat until empty string is given
    file1 = open('C:\\Users\\Jacob School\\Documents\\Classes\\Theory of Autonama\\proj-1-machine.txt', 'r')
    count = 0
    while True:
        count += 1
        line = file1.readline()
        if not line:
            break
        if (count == 3):
            alphabet = line.replace(" ","").replace("(","").replace("),","").replace("\n","").split(",")
            print('alphabet = ',alphabet)
        elif (count == 4):
            K = line.replace(" ","").replace("(","").replace("),","").replace("\n","").split(",") 
            print('K = ',K)
            dictionary = {key: [] for key in K}
        elif (count == 5):
            s = line.replace(" ","").replace(",","").replace("\n","")
            print('s = ',s)
        elif (count == 6):
            F = line.replace(" ","").replace("(","").replace("),","").replace("\n","").split(",")
            print('F = ',F)
        elif (count == 7):
            Transitions = line.replace(" ","").replace("(","").replace(")","").replace("\n","").split(",")
            print('Transitions = ',Transitions)
            for i in range(int(len(Transitions)/3)):
                insert(dictionary, Transitions[3*i], [Transitions[3*i + 1],Transitions[3*i + 2]])
        elif (count == 9):
            B = line.replace(" ","") .replace("(","").replace(")","").replace("\n","").split(",")
            print('B = ', B)
    file1.close()

    if (len(B) == 1 and B[0] == ''):
        while True:
            Test_String = input("Please input a string: ")
            if (Test_String == ''):
                print('Bye bye.')
                break
            else:
                for i in range(0,len(B)):
                    Accepted = False
                    Accepted = Process_String_NFA(s,Test_String,0,dictionary,F,Accepted)
                    if (Accepted == True):
                        print(Test_String,' is accepted')
                    else:
                        print(Test_String,' is rejected')
    else:
        print('Input Tuple of Strings to Test: ', B)
        Accepted_Tuple = [[] for _ in range(len(B))]
        for i in range(0,len(B)):
            Accepted = False
            Accepted = Process_String_NFA(s,B[i],0,dictionary,F,Accepted)
            if (Accepted == True):
                print(B[i],' is accepted')
                Accepted_Tuple[i] = 'Accepted'
            else:
                print(B[i],' is rejected')
                Accepted_Tuple[i] = 'Rejected'
        print(Accepted_Tuple)
        

def Process_String_NFA(state, given_string,string_index, dictionary,F,Acception):
#     function to process all possible transitions for a given state and string
#     given a state to move from and a symbol for the next character in the input string, the function will process through
#     all possible transitions that exist for that symbol within that current state in the dictionary
    Accepted = Acception
    if (string_index == len(given_string)):
        if state in F:
            Accepted = True
    else:
        for i in range(len(dictionary[state])):
            if (dictionary[state][i][0] == given_string[string_index]):
                Accepted = Process_String_NFA(dictionary[state][i][1],given_string,string_index + 1, dictionary,F,Accepted)
    return Accepted


Read_Input_NFA()
