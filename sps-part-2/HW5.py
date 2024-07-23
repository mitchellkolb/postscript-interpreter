#Mitchell Kolb
#CPTS 355 - HW4 part 1 - Postscript interpreter


"""
opStack is a list but is used a stack 
    [0] index should be the bottom of the stack
    [1+] index shoulf be the top of the stack

dictstack is a list but is used a stack 
    [0] index should be the bottom of the stack
    [1+] index should be the top of the stack

If I want the top item of either stack I want the last item in the list.
.pop() returns the last item of a list in python
.append() adds an item to the end of a list
list[-1] works as well to get the last item
"""


#part 2 required library
import re


#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the helper functions to push and pop values on the opstack
# (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    if len(opstack) > 0:
        return opstack.pop()
    else:
        print("Error: opPop - Operand stack is empty")
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to
# define name, and to lookup a name

def dictPop():
    if len(dictstack) > 0:
        return dictstack.pop()
    else:
        print("Error: dictPop - Dictstack stack is empty")
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack.
    #Note that, your interpreter will call dictPush only when Postscript
    #“begin” operator is called. “begin” should pop the empty dictionary from
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    """
    Here is what I need to do with def so far cause I havent done psDef yet
    dictstack is a list and this function is given name and value.
    If dictstack list is empty it will add a dictionary which is empty then add the name and value to it as a key-value pair
    If dictstack list is NOT empty is will add name value to it as a key-value pair
    """
    if len(dictstack) == 0:
        dictPush({}) 
    current_dict = dictstack[-1] #gets the top of the stack list
    current_dict[name] = value #I don't have to push it back becuase I have it by reference so if I change it here it will be chnaged in the dictstack

    #add name:value pair to the top dictionary in the dictionary stack.
    #Keep the '/' in the name constant.
    #Your psDef function should pop the name and value from operand stack and
    #call the “define” function.

def lookup(name):
    """
    As stated in lecture/slides when there is a command /x 3 def which is then put in the dictstack lookup will be passed a name that doesn't have the / in front. but it is assumed that all defined stuff will have the /
    """
    if name[0] != "/": #checks the / as the first char. Adds it if necessary, its assumed to be here but im just covering all my bases
        name = "/" + name
    if len(dictstack) > 0:
        for dictionary in reversed(dictstack):
            if name in dictionary:
                return dictionary[name]
        print("Error: lookup - Nothing found in Dictstack to return")
    else:
        print("Error: lookup - Dictstack stack is empty")
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.



#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.
def add():
    if len(opstack) >= 2:
        value1 = opPop()
        value2 = opPop()
        if(isinstance(value1,int) or isinstance(value1,float))  and (isinstance(value2,int) or isinstance(value2,float)):
                opPush(value1 + value2)
        else:
            print("Error: add - one of the stack items is not a number value")
            opPush(value2)
            opPush(value1)             
    else:
        print("Error: add - add needs 2 numbers on the stack")


def sub():
    if len(opstack) >= 2:
        value1 = opPop()
        value2 = opPop()
        if(isinstance(value1,int) or isinstance(value1,float))  and (isinstance(value2,int) or isinstance(value2,float)):
                opPush(value2 - value1)
        else:
            print("Error: sub - one of the stack items is not a number value")
            opPush(value2)
            opPush(value1)             
    else:
        print("Error: sub - add needs 2 numbers on the stack")

def mul():
    if len(opstack) >= 2:
        value1 = opPop()
        value2 = opPop()
        if(isinstance(value1,int) or isinstance(value1,float))  and (isinstance(value2,int) or isinstance(value2,float)):
                opPush(value1 * value2)
        else:
            print("Error: mul - one of the stack items is not a number value")
            opPush(value2)
            opPush(value1)             
    else:
        print("Error: mul - add needs 2 numbers on the stack")

def div():
    if len(opstack) >= 2:
        value1 = opPop()
        value2 = opPop()
        if(isinstance(value1,int) or isinstance(value1,float))  and (isinstance(value2,int) or isinstance(value2,float)):
                try:
                    opPush(value2 / value1)
                except ZeroDivisionError:
                    print("Error: div - Can't divide by zero")
                    opPush(value2)
                    opPush(value1) 
        else:
            print("Error: div - one of the stack items is not a number value")
            opPush(value2)
            opPush(value1)             
    else:
        print("Error: div - add needs 2 numbers on the stack")

def mod():
    if len(opstack) >= 2:
        value1 = opPop()
        value2 = opPop()
        if(isinstance(value1,int) or isinstance(value1,float))  and (isinstance(value2,int) or isinstance(value2,float)):
                opPush(value2 % value1)
        else:
            print("Error: mod - one of the stack items is not a number value")
            opPush(value2)
            opPush(value1)             
    else:
        print("Error: mod - add needs 2 numbers on the stack")

def eq():
    if len(opstack) >= 2:
        value1 = opPop()
        value2 = opPop()
        result = False
        if(value1 is value2):
            result = True
        opPush(result)          
    else:
        print("Error: eq - add needs 2 numbers on the stack")

def lt():
    if len(opstack) >= 2:
        value1 = opPop()
        value2 = opPop()
        result = False
        if(value2 < value1):
            result = True
        opPush(result)          
    else:
        print("Error: lt - add needs 2 numbers on the stack")

def gt():
    if len(opstack) >= 2:
        value1 = opPop()
        value2 = opPop()
        result = False
        if(value2 > value1):
            result = True
        opPush(result)          
    else:
        print("Error: gt - add needs 2 numbers on the stack")

#--------------------------- 15% -------------------------------------
# String operators: define the string operators length, get, getinterval, put
def length():
    """
    As stated in the slides, length pops a string from the stack and pushes the length og the string onto the stack 
    This only works on strings
    """
    if len(opstack) >= 1:
        value1 = opPop()
        if(isinstance(value1,str)):
            if(value1[0] == '('):
                lengthNumber = (len(value1) - 2) #subtract 2 becuase of the assumed ( ) around the string
                opPush(lengthNumber)
            else:
                print("Error: length - top value on stack isn't formatted correctly. It needs () around it.")
                opPush(value1)  
        else:
            print("Error: length - top value on stack isn't a string")
            opPush(value1)             
    else:
        print("Error: length - Stack empty, needs 1 string on the stack")

def get():
    """
    As stated in the slides, get pops a string and index and psushes the ASCII values of the char at the index position onto the stack
    """
    if len(opstack) >= 2:
        index = opPop()
        stringVal = opPop()

        if(isinstance(stringVal,str) and isinstance(index,int)):
            if(stringVal[0] == '('):
                stringVal = stringVal[1:-1] #takes off () so indexing is correct
                length = len(stringVal)
                if index <= length:
                    char = stringVal[index]
                    ascii_value = ord(char)
                    opPush(ascii_value)
                else:
                    print("Error: get - index out of range")
                    opPush(stringVal) 
                    opPush(index) 
                    return
            else:
                print("Error: get - top value on stack isn't formatted correctly. It needs () around it.")
                opPush(stringVal) 
                opPush(index)  
                return
        else:
            print("Error: get - top values on stack aren't right types")
            opPush(stringVal) 
            opPush(index)            
            return
    else:
        print("Error: get - Stack empty, needs 2 string on the stack")
    

def getinterval():
    """
    As stated in the slides, getinterval pops a string, index, count from stack then returns the substring of string starting at index for count then pushes the substring on the stack at the end.
    EXAMPLE (CptS355) 0 3 getinterval   --> (Cpt)
    string   index    count   getinterval
    """
    if len(opstack) >= 3:
        count = opPop()
        index = opPop()
        stringVal = opPop()

        if(isinstance(stringVal,str) and isinstance(index,int) and isinstance(count, int)):
            if(stringVal[0] == '('):
                stringVal = stringVal[1:-1] #takes off () so indexing is correct
                length = len(stringVal)
                if length >= index and index >= 0:
                    stringVal =  '(' + stringVal[index:count] + ')'
                    opPush(stringVal)
                else:
                    print("Error: getinterval - index value is greater than string length")
                    opPush(stringVal) 
                    opPush(index)  
                    opPush(count)
                    return
                
            else:
                print("Error: getinterval - string value from stack isn't formatted correctly. It needs () around it.")
                opPush(stringVal) 
                opPush(index)  
                opPush(count)
                return
        else:
            print("Error: getinterval - values on stack aren't right types")
            opPush(stringVal) 
            opPush(index)  
            opPush(count)     
            return
    else:
        print("Error: getinterval - Stack not filled out, needs 3 items on the stack")


def put():
    char = opPop()  # Pop the asciichar from the stack
    index = opPop()  # Pop the index from the stack
    string = opPop()  # Pop the string from the stack

    if isinstance(string, str) and isinstance(index, int) and isinstance(char, int):
        if index >= 0 and index < len(string):
            modified_string = string[:index+1] + chr(char) + string[index+2:]  # Create a new string with the modified character

            # Replace the original string on the opstack/dictstack with the modified string
            if len(opstack) > 0:
                for i in range(len(opstack)):
                    if id(opstack[i]) == id(string):
                        opstack[i] = modified_string

            
            if len(dictstack) > 0:
                last_dictionary = dictstack[-1]
                for key, value in last_dictionary.items():
                    if id(value) == id(string):
                        last_dictionary[key] = modified_string
    
                
            """
            # Old Part 1 solution - This is not a solution that works like in ghostscript becuase in the scenario where you opPush v1 "(hi)" and v2 "(hi)" this function will change both but I only want it to work when v1 is dup() 

            try:
                opstack[opstack.index(string)] = modified_string
            except ValueError:
                print("Error: put - no duplicated value in stack")
                return
            """

        else:
            print("Error: put - index value is greater than string length")
            opPush(string) 
            opPush(index)  
            opPush(char)
    else:
        print("Error: put - values on stack aren't right types")
        opPush(string) 
        opPush(index)  
        opPush(char)



#--------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack
def dup():
    toBeDupped = opPop()
    opPush(toBeDupped)
    opPush(toBeDupped)

def copy():
    amount = opPop()
    opstack.extend(opstack[-amount:]) #I use a slice and the reverse amount that is requested so it takes it from the end of the list and I use .extend which adds those amount of vars back onto the list. 

def pop():
    if len(opstack) > 0:
        value = opPop()
        return value
    else:
        print("Error: Pop - Nothing to pop, stack is empty")

def clear2(): #This was my part1 clear but part2 clear is below
    opstack.clear()

def exch():
    topVar = opPop()
    secondVar = opPop()
    opPush(topVar)
    opPush(secondVar)

def roll():
    """
    rolls the top n elements on the stack around by the i times. 
        example: stack 1 2 3 4 5     5 2 roll -->  stack 4 5 1 2 3
    Should work on negatives too in the reverse direction
        example: stack 1 2 3 4 5     4 -2 roll -->  stack 1 4 5 2 3
    """
    print("--- Roll Start ---")
    
    i = opPop()  # Number of times to roll
    n = opPop()  # Number of elements to roll
    rollList = []
    
    if(isinstance(i, int) and isinstance(n,int)):
        for num in range(0,n,1):
            tempNum = opPop()
            checker = True

            if not isinstance(tempNum, int): # This trips the bool variable if any of the popped stack items arent ints
                checker = False

            rollList = [tempNum] + rollList

        if checker == False: #If the trip is false this puts all the stack back
            print("Error roll - Need the values on the opstack to be all int")
            for num in range(0,n,1):
                opPush(rollList[num])
            opPush(n)
            opPush(i)
        if i > 0: #This means we are rolling bot to top
            for num in range(0,i,1):
                rollList = [rollList[-1]] + rollList[:-1]
        elif i < 0:# This means we are rolling top to bot
            for num in range(0,(i*-1),1):
                rollList = rollList[1:] + [rollList[0]]
        for num in range(0,n,1):
            opPush(rollList[num])
    else:
        print("Error roll - Need the value on the opstack to be an int")
        opPush(n)
        opPush(i)

    

def stack():
    #print("-- STACK --")    #When i am using this I like to have stack print a barrier of word stack so I know where it starts
    print(*reversed(opstack), sep = '\n') # this prints off the opstack reversed becuase of the order of the stack where each item has its own line

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    if len(opstack) >= 1:
        value = opPop()
        if(isinstance(value, int)):
            opPush({})
        else:
            print("Error psDict - Need the value on the opstack to be an int")
            opPush(value)
    else:
        print("Error psDict - opstack is empty")
        opPush(value)

def begin():
    if len(opstack) >= 1:
        value = opPop()
        if(isinstance(value, dict)):
            dictPush(value)
        else:
            print("Error begin - Need the value on the opstack to be a dict")
            opPush(value)
    else:
        print("Error begin - opstack is empty")
        opPush(value)

def end():
    if len(dictstack) != 0:
        dictPop()
    else:
        print("Error end - dictstack is empty")

def psDef():
    if len(opstack) >= 2:
        value = opPop()  # pop the value from the opstack
        name = opPop()  # pop the name from the opstack
        try:
            define(name, value)
        except Exception: #This i think should cover most cases where it messes up and if it does it should put the opstack back to normal
            opPush(name)
            opPush(value)
    else:
        opLen = len(opstack)
        print("Error: psDef - Need two items in opstack. opStack length = %d" % (opLen))



#######################################################
####################  part 2 code  ####################
#######################################################

def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)


"""
# The it argument is an iterator. The sequence of return characters should
# represent a string of properly nested {} parentheses pairs, from which
# the leading '{' has been removed. If the parentheses are not properly
# nested, returns False.
def groupMatching1(it):
    res = []
    for c in it:
        if c == '}':
            return res
        else:
            # Note how we use a recursive call to group the inner matching
            # parenthesis string and append it as a whole to the list we are
            # constructing. Also note how we have already seen the leading
            # '{' of this inner group and consumed it from the iterator.
            res.append(groupMatching1(it))
    return False

# Function to parse a string of { and } braces. Properly nested parentheses
# are arranged into a list of properly nested lists.
def group(s):
    res = []
    it = iter(s)
    for c in it:
        if c=='}': #non matching closing parenthesis; return false
            return False
        else:
            res.append(groupMatching1(it))
    return res

"""

# complete this function
# The it argument is an iterator.
# The sequence of return characters should represent a list of properly nested
# tokens, where the tokens between '{' and '}' is included as a sublist. If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code array for the inner
            # paranthesis, it will be appended to the list we are constructing
            # as a whole.
            res.append(groupMatching2(it))
        else:
            try:
                res.append(int(c))
            except ValueError:
                res.append(c)
    return False


# Complete this function
# Function to parse a list of tokens and arrange the tokens between { and } braces
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested lists.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c == '}':
            return False
        elif c == '{':
            res.append(groupMatching2(it))
        elif c == 'true':
            res.append(True)
        elif c == 'false':
            res.append(False)
        else:
            try:
                res.append(int(c))
            except ValueError:
                res.append(c)
    return res



# Write the necessary code here; again write
# auxiliary functions if you need them. This will probably be the largest
# function of the whole project, but it will have a very regular and obvious
# structure if you've followed the plan of the assignment.
#
#def interpretSPS(code): # code is a code array
#    pass

"""
to run functions abstractly given a string value like dup within a function
     eval(string_value + "()")
"""
def interpretSPS(code):
    def interpretElement(element):

        if isinstance(element, str):
            if element.startswith('/'):  # Variable name
                opstack.append(element)
            elif element in dictstack[-1]:  # Variable lookup
                value = dictstack[-1][element]
                if isinstance(value, list):  # Function call
                    interpretSPS(value)
                else:
                    opstack.append(value)
            else:
                opstack.append(element)
        elif isinstance(element, list):  # Code array
            interpretSPS(element)
        else:
            opstack.append(element)

    for element in code:
        interpretElement(element)

    if opstack:    #  Prints the contents of the operand stack (if any)
        print("Output:", opstack)

    return dictstack     # Return the dictionary stack (if there is more to add to it)



# Copy this to your HW5.py file>
def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))


#clear opstack and dictstack
def clear():
    del opstack[:]
    del dictstack[:]


def psIf(): # it takes         bool  code-array   if
    code_array = opPop()
    bool_value = opPop()
    if(isinstance(code_array, str) or isinstance(bool_value, bool)):
        if(bool_value == True):
            interpretSPS(code_array) 
    else:
        opPush(bool_value)
        opPush(code_array)
        print("Error: if - code array or bool value is incorrect")

def psIfelse(): # it takes         bool  code-array(true)  code-array(false)  ifElse
    code_array_false = opPop()
    code_array_true = opPop()
    bool_value = opPop()
    if(isinstance(code_array_false, str) or (code_array_true, str) or isinstance(bool_value, bool)):
        if(bool_value == True):
            interpretSPS(code_array_true)
        else:
            interpretSPS(code_array_false) 
    else:
        opPush(bool_value)
        opPush(code_array_true)
        opPush(code_array_false)
        print("Error: ifElse - code arrayture/false or bool value is incorrect")

def psFor():# it takes         init    incr    final    code-array   for
    code_array = opPop()
    final = opPop()  #upper bound of the for loop
    increment = opPop()  #number of times the loop repeats
    init = opPop() #the starting cycle number
    if(isinstance(code_array, str) or (final, int) or (increment, int) or (init, int)):
        opPush(init)
        if(init <= final):
            interpretSPS(code_array)
            opPush(init + increment)
            opPush(increment)
            opPush(final)
            opPush(code_array)
            psFor()
    else:
        opPush(init)
        opPush(increment)
        opPush(final)
        opPush(code_array)
        print("Error: for - code_array, final, increment, init broke somehow, probably stack lineup is messed up")

#testing

input1 = """
        /square {
               dup mul
        } def
        (square)
        4 square
        dup 16 eq
        {(pass)} {(fail)} ifelse
        stack
        """

input2 ="""
    (facto) dup length /n exch def
    /fact {
        0 dict begin
           /n exch def
           n 2 lt
           { 1}
           {n 1 sub fact n mul }
           ifelse
        end
    } def
    n fact stack
    """

input3 = """
        /fact{
        0 dict
                begin
                        /n exch def
                        1
                        n -1 1 {mul} for
                end
        } def
        6
        fact
        stack
    """

input4 = """
        /lt6 { 6 lt } def
        1 2 3 4 5 6 4 -3 roll
        dup dup lt6 {mul mul mul} if
        stack
        clear
    """

input5 = """
        (CptS355_HW5) 4 3 getinterval
        (355) eq
        {(You_are_in_CptS355)} if
         stack
        """

input6 = """/pow2 {/n exch def (pow2_of_n_is) dup 8 n 48 add put 1 n -1 1 {pop 2 mul} for } def (Calculating_pow2_of_9) dup 20 get 48 sub pow2 stack
        """

answer6 = ['/pow2', '{', '/n', 'exch', 'def', '(Pow2_of_n_is)', 'dup', '8', 'n', '48',
'add', 'put', '1', 'n', '-1', '1', '{', 'pop', '2', 'mul', '}', 'for', '}',
'def', '(Calculating_pow2_of_9)', 'dup', '20', 'get', '48', 'sub', 'pow2',
'stack']

answer6REAL = ['/pow2', ['/n', 'exch', 'def', '(Pow2_of_n_is)', 'dup', 8, 'n', 48, 'add',
'put', 1, 'n', -1, 1, ['pop', 2, 'mul'], 'for'], 'def',
'(Calculating_pow2_of_9)', 'dup', 20, 'get', 48, 'sub', 'pow2', 'stack']

"""
groupTest = group("{{}{{}}}")
groupAnswer = [[[], [[]]]]
if groupTest == groupAnswer:
    print("Group: True")
else:
    print("Group: False")
"""
    


print(tokenize(input1))
print(parse(tokenize(input1)))

parseTest = parse(['b', 'c', '{', 'a', '{', 'a', 'b', '}', '{', '{', 'e', '}', 'a', '}', '}'])
parseAnswer = ['b', 'c', ['a', ['a', 'b'], [['e'], 'a']]]
if parseTest == parseAnswer:
    print("Parse1: True")
    print(parseTest)
    print("\n\n")
else:
    print("Parse1: False\n\n")


input_list = ['/pow2', '{', '/n', 'exch', 'def', '(Pow2_of_n_is)', 'dup', '8', 'n', '48', 'add', 'put', '1', 'n', '-1', '1', '{', 'pop', '2', 'mul', '}', 'for', '}', 'def', '(Calculating_pow2_of_9)', 'dup', '20', 'get', '48', 'sub', 'pow2', 'stack']
result = parse(input_list)
answerParse = ['/pow2', ['/n', 'exch', 'def', '(Pow2_of_n_is)', 'dup', 8, 'n', 48, 'add', 'put', 1, 'n', -1, 1, ['pop', 2, 'mul'], 'for'], 'def', '(Calculating_pow2_of_9)', 'dup', 20, 'get', 48, 'sub', 'pow2', 'stack']
print(result)
print(type(answerParse[1][5]))
print(type(result[1][5]))
if result[1][5] == answerParse[1][5]:
    print("Parse2: True")
else:
    print("Parse2: False")



#######################################################
####################  local tests  ####################
#######################################################

def test():
    # opPush("test")
    # opPush("test")
    # dup()
    # dupped = opPop()
    # orign = opPop()
    # other = opPop()
    # print(id(orign))
    # print(id(dupped))
    # print(id(other))
    stringNum = '5'
    print(stringNum.isdigit())
    
def testPut(): 
    opPush("(This is a test _)") 
    dup() 
    opPush("/s") 
    exch() 
    psDef() 
    dup() 
    opPush(15) 
    opPush(48) 
    put() 
    if lookup("s") != "(This is a test 0)" or opPop()!= "(This is a test 0)": 
        return False 
    return True

#test()
#print(testPut())


