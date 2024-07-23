from colors import *
from psexpressions import StringValue, DictionaryValue, CodeArrayValue

#Mitchell Kolb

class PSOperators:
    def __init__(self):
        #stack variables
        self.opstack = []  #assuming top of the stack is the end of the list
        self.dictstack = []  #assuming top of the stack is the end of the list
        # The environment that the REPL evaluates expressions in.
        # Uncomment this dictionary in part2
        self.builtin_operators = {
            "add":self.add,
            "sub":self.sub,
            "mul":self.mul,
            "mod":self.mod,
            "eq":self.eq,
            "lt": self.lt,
            "gt": self.gt,
            "dup": self.dup,
            "exch":self.exch,
            "pop":self.pop,
            "copy":self.copy,
            "count": self.count,
            "clear":self.clear,
            "stack":self.stack,
            "dict":self.psDict,
            "string":self.string,
            "length":self.length,
            "get":self.get,
            "put":self.put,
            "getinterval":self.getinterval,
            "putinterval":self.putinterval,
            "search" : self.search,
            "begin":self.begin,
            "end":self.end,
            "def":self.psDef,
            "if":self.psIf,
            "ifelse":self.psIfelse,
            "for":self.psFor
        }
    #------- Operand Stack Helper Functions --------------
    
    """
        Helper function. Pops the top value from opstack and returns it.
    """
    def opPop(self):
        if len(self.opstack) > 0:
            x = self.opstack[len(self.opstack) - 1]
            self.opstack.pop(len(self.opstack) - 1)
            return x
        else:
            print("Error: opPop - Operand stack is empty")

    """
       Helper function. Pushes the given value to the opstack.
    """
    def opPush(self,value):
        self.opstack.append(value)

    #------- Dict Stack Helper Functions --------------
    """
       Helper function. Pops the top dictionary from dictstack and returns it.
    """  
    def dictPop(self):
        if len(self.dictstack) > 0:
            x = self.dictstack[len(self.dictstack) - 1]
            self.dictstack.pop(len(self.dictstack) - 1)
            return x
        else:
            print("Error: dictPop - dictionary stack is empty")

    """
       Helper function. Pushes the given dictionary onto the dictstack. 
    """   
    def dictPush(self,d):
        self.dictstack.append(d)

    """
       Helper function. Adds name:value pair to the top dictionary in the dictstack.
       (Note: If the dictstack is empty, first adds an empty dictionary to the dictstack then adds the name:value to that. 
    """  
    def define(self, name, value):
        if len(self.dictstack) == 0: #if dickstack is empty it adds an empty dict
            self.dictstack.append({})
        self.dictstack[-1][name] = value #adds the key:value pairs

    """
       Helper function. Searches the dictstack for a variable or function and returns its value. 
       (Starts searching at the top of the dictstack; if name is not found returns None and prints an error message.
        Make sure to add '/' to the begining of the name.)
    """
    def lookup(self,name):
        if name[0] != "/": #checks the / as the first char. Adds it if necessary
            name = "/" + name
        for d in reversed(self.dictstack):#A list isn't a stack so I start reversed and check the key and return the value if the correct pair is found
            if name in d:
                return d[name]
        print(f"Error: Key {name} not found")
        return None
    
    #------- Arithmetic Operators --------------

    """
       Pops 2 values from opstack; checks if they are numerical (int); adds them; then pushes the result back to opstack. 
    """  
    def add(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,float))  and (isinstance(op2,int) or isinstance(op2,float)):
                self.opPush(op1 + op2)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op1)
                self.opPush(op2)             
        else:
            print("Error: add expects 2 operands")

    """
       Pops 2 values from opstack; checks if they are numerical (int); subtracts them; and pushes the result back to opstack. 
    """ 
    def sub(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,float))  and (isinstance(op2,int) or isinstance(op2,float)):
                self.opPush(op2 - op1)#reveresed the op1 and op2 from add so it works with the test
            else:
                print("Error: sub - one of the operands is not a number value")
                self.opPush(op1)
                self.opPush(op2)             
        else:
            print("Error: sub expects 2 operands")


    """
        Pops 2 values from opstack; checks if they are numerical (int); multiplies them; and pushes the result back to opstack. 
    """
    def mul(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,float))  and (isinstance(op2,int) or isinstance(op2,float)):
                self.opPush(op1 * op2)
            else:
                print("Error: mul - one of the operands is not a number value")
                self.opPush(op1)
                self.opPush(op2)             
        else:
            print("Error: mul expects 2 operands")


    """
        Pops 2 values from stack; checks if they are int values; calculates the remainder of dividing the bottom value by the top one; 
        pushes the result back to opstack.
    """
    def mod(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,float))  and (isinstance(op2,int) or isinstance(op2,float)):
                self.opPush(op2 % op1)
            else:
                print("Error: mod - one of the operands is not a number value")
                self.opPush(op1)
                self.opPush(op2)             
        else:
            print("Error: mod expects 2 operands")

    """ Pops 2 values from stacks; if they are equal pushes True back onto stack, otherwise it pushes False.
          - if they are integers or booleans, compares their values. 
          - if they are StringValue values, compares the `value` attributes of the StringValue objects;
          - if they are DictionaryValue objects, compares the objects themselves (i.e., ids of the objects).
        
        """
    def eq(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) and isinstance(op2,int) or isinstance(op1,float) and isinstance(op2,float) or isinstance(op1,bool) and isinstance(op2,bool)):
                if (op1 == op2): # Compares the int, float, bool values
                    self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1,StringValue) and isinstance(op2,StringValue)):
                if op1.value == op2.value:  # Compare the string values
                    self.opPush(True)
                else:
                    self.opPush(False)
            elif isinstance(op1, DictionaryValue) and isinstance(op2, DictionaryValue):
                if id(op1) is id(op2):  # Compare the dict value of the objects
                    self.opPush(True)
                else:
                    self.opPush(False)
            else:
                print("Error: OP1 and OP2 are not equal or the same string value")
                self.opPush(False)
        else:
            print("Error: stack is empty")


    """ Pops 2 values from stacks; if the bottom value is less than the second, pushes True back onto stack, otherwise it pushes False.
          - if they are integers or booleans, compares their values. 
          - if they are StringValue values, compares the `value` attributes of them;
          - if they are DictionaryValue objects, compares the objects themselves (i.e., ids of the objects).
    """  
    def lt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) and isinstance(op2,int) or isinstance(op1,float) and isinstance(op2,float) or isinstance(op1,bool) and isinstance(op2,bool)):
                if (op1 > op2): # Compares the int, float, bool values
                    self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1,StringValue) and isinstance(op2,StringValue)):
                if op1.value > op2.value:  # Compare the string values
                    self.opPush(True)
                else:
                    self.opPush(False)
            elif isinstance(op1, DictionaryValue) and isinstance(op2, DictionaryValue):
                if id(op1) > id(op2):  # Compare the dict value of the objects
                    self.opPush(True)
                else:
                    self.opPush(False)
            else:
                print("Error: OP1 is not less than OP2")
                self.opPush(False)
        else:
            print("Error: stack is empty")


    """ Pops 2 values from stacks; if the bottom value is greater than the second, pushes True back onto stack, otherwise it pushes False.
          - if they are integers or booleans, compares their values. 
          - if they are StringValue values, compares the `value` attributes of them;
          - if they are DictionaryValue objects, compares the objects themselves (i.e., ids of the objects).
    """  
    def gt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) and isinstance(op2,int) or isinstance(op1,float) and isinstance(op2,float) or isinstance(op1,bool) and isinstance(op2,bool)):
                if (op1 < op2): # Compares the int, float, bool values
                    self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1,StringValue) and isinstance(op2,StringValue)):
                if op1.value < op2.value:  # Compare the string values
                    self.opPush(True)
                else:
                    self.opPush(False)
            elif isinstance(op1, DictionaryValue) and isinstance(op2, DictionaryValue):
                if id(op1) < id(op2):  # Compare the dict value of the objects
                    self.opPush(True)
                else:
                    self.opPush(False)
            else:
                print("Error: OP1 is not greater than OP2")
                self.opPush(False)
        else:
            print("Error: stack is empty")

    #------- Stack Manipulation and Print Operators --------------
    """
       This function implements the Postscript "pop operator". Calls self.opPop() to pop the top value from the opstack and discards the value. 
    """
    def pop (self):
        if (len(self.opstack) > 0):
            self.opPop()
        else:
            print("Error: pop - not enough arguments")

    """
       Prints the opstack and dictstack. The end of the list is the top of the stack. 
    """
    def stack(self):
        print(OKGREEN+"**opstack**")
        for item in reversed(self.opstack):
            print(item)
        print("-----------------------"+CEND)
        print(RED+"**dictstack**")
        for item in reversed(self.dictstack):
            print(item)
        print("-----------------------"+ CEND)


    """
       Copies the top element in opstack.
    """
    def dup(self):
        if len(self.opstack) > 0:
            op1 = self.opPop()
            op2 = op1
            if (isinstance(op1,int) or isinstance(op1,float) or isinstance(op1,bool) or isinstance(op1,StringValue)):
                self.opPush(op1)
                self.opPush(op2)
            #dups a dictionary. Doesn't say we need it in the dup function but the get_put_dict function needs it
            elif isinstance(op1, DictionaryValue):
                new_dict = DictionaryValue(op1.value) # Create a new DictionaryValue object with the same dictionary
                self.dictPush(op1)
                self.dictPush(new_dict)
                """elif isinstance(op1, DictionaryValue):
                new_dict = DictionaryValue(op1.value)
                for key, value in op1.value.items():
                    new_dict.value[key] = value
                self.opPush(op1)
                self.opPush(new_dict)"""
            else:
                print("inner loop. didnt dup right")
                self.opPush(op1)
            """
            
            """
            
        else:
            print("Error: didnt dup correctly")
        
    """
       Pops an integer count from opstack, copies count number of values in the opstack. 
    """
    def copy(self):        
        if len(self.opstack) > 0:
            count = self.opPop()
            if isinstance(count, int) and count >= 0:
                op_copy = self.opstack[-count:].copy()
                self.opstack.extend(op_copy)
            else:
                print("Error: Count is not a non-negative integer")
        else:
            print("Error: stack is empty")

    """
        Counts the number of elements in the opstack and pushes the count onto the top of the opstack.
    """
    def count(self):
        count = len(self.opstack) #counts the amount of values on the stack
        self.opPush(count) #pushes that value

    """
       Clears the opstack.
    """
    def clear(self):
        self.opstack[:] = [] #uses the slice notation to discard the values of the opstack
        
    """
       swaps the top two elements in opstack
    """
    def exch(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            self.opPush(op1)
            self.opPush(op2)
        else:
            print("exch messed up. nothing is pushed or popped")


    # ------- String and Dictionary creator operators --------------

    """ Creates a new empty string  pushes it on the opstack.
    Initializes the characters in the new string to \0 , i.e., ascii NUL """
    def string(self):
        size = self.opPop()
        if isinstance(size, int):
            string_value = StringValue('(' + '\x00' * size + ')')  # create a new empty string with size characters initialized to NUL
            self.opPush(string_value)
        else:
            print("Error: Size is not an integer string")

    """Creates a new empty dictionary  pushes it on the opstack """
    def psDict(self):
        size = self.opPop()
        if isinstance(size, int):
            self.opPush(DictionaryValue({}))
        else:
            print("Error: Size is not an integer psDict")

    # ------- String and Dictionary Operators --------------
    """ Pops a string or dictionary value from the operand stack and calculates the length of it. Pushes the length back onto the stack.
       The `length` method should support both DictionaryValue and StringValue values.
    """
    def length(self):
        value = self.opPop()  # pop the value from the opstack
        if isinstance(value, StringValue):
            length = len(value.value)
            length = length - 2 #gets rid of the () that come with the string
        elif isinstance(value, DictionaryValue):
            length = len(value.d)
        else:
            print("Error: length - Invalid type")
            return
        self.opPush(length)


    """ Pops either:
         -  "A (zero-based) index and an StringValue value" from opstack OR 
         -  "A `name` (i.e., a key) and DictionaryValue value" from opstack.  
        If the argument is a StringValue, pushes the ascii value of the the character in the string at the index onto the opstack;
        If the argument is an DictionaryValue, gets the value for the given `name` from DictionaryValue's dictionary value and pushes it onto the opstack
    """
    def get(self):
        value = self.opPop()
        key = self.opPop()

        if isinstance(key, StringValue):
            index = int(value)
            char = key.value[index+1]#adds +1 becuase lists start at 0
            if char == '\0':
                self.opPush(0)
            else:
                self.opPush(ord(char))
        elif isinstance(key, DictionaryValue):
            dictionary = key.value
            if value.value in dictionary:
                self.opPush(dictionary[value.value])
            else:
                print("Error: get - key not found in dictionary")
        else:
            print("Error: get - invalid arguments")
        
    """
    Pops either:
    - "An `item`, a (zero-based) `index`, and an StringValue value from  opstack", OR
    - "An `item`, a `name`, and a DictionaryValue value from  opstack". 
    If the argument is a StringValue, replaces the character at `index` of the StringValue's string with the character having the ASCII value of `item`.
    If the argument is an DictionaryValue, adds (or updates) "name:item" in DictionaryValue's dictionary `value`.
    ____________________________________
    SO as far as I understand it there are two versions. One where youre given a string and one where youre given a dict
    In String you are given an index and value and put is supposed to replace the string[index] character with the value inn memory and not push it onto the stack. There will be a dup before it so the stack won't lose reference
    In Dict you are given a key and value and put is supposed to create or update the in memeory dictionary
    
    """
    
    def put(self):
        
        """
        lengthOfOP = len(self.opstack)
        value = self.opPop()  # 51 - ascii for 3
        index = key =self.opPop()  # 4th index of the string or dict key reference
        myString = myDict = self.opPop()  # CptS451 string or dict reference 

        if (isinstance(value, int) and isinstance(index, int)):
        
        """
        lengthOfOP = len(self.opstack)
        value = self.opPop()  # 51 - ascii for 3
        index = self.opPop()  # 4th index of the string
        item = self.opPop()  # CptS451 string

        if isinstance(value, int):
            if isinstance(index, int):
                if self.dictstack:#checks if its empty
                    for my_dict in self.dictstack:
                        if item in my_dict.values():
                            #If its in this section that means that the argument is a DictionaryValue, and we will add (or update) "name:item" in DictionaryValue's dictionary `value`.
                            for key in my_dict:
                                if my_dict[key] == item:
                                    valueConvert = chr(value)  # converts 50 ascii to 2
                                    new_value = (str(item.value[:index+1]) + valueConvert + str(item.value[index+2:]))
                                    item.value = new_value  # Update the value attribute of the StringValue object with the new value
                                    my_dict[key] = item
                            break
                elif isinstance(item, StringValue):
                    # all values are type checked
                    if index < 0 or index >= len(item.value):
                        print("Error: put - Index out of bounds for StringValue")
                        self.opPush(item)
                        return
                    valueConvert = chr(value)  # converts 51 ascii to 3
                    new_value = (str(item.value[:index+1]) + valueConvert + str(item.value[index+2:]))
                    item.value = new_value  # Update the value attribute of the StringValue object with the new value
                    if lengthOfOP != len(self.opstack):
                        self.opPop()#This pops the Original CptS451 value out so when can place the new one in
                    self.opPush(item)
                else:
                    print("Error: item is not a StringValue")
            else:
                print("Error: index is not an int")
        else:
            print("Value is neither an int or StringValue. It's busted")
        
    


    """
    getinterval is a string only operator, i.e., works only with StringValue values. 
    Pops a `count`, a (zero-based) `index`, and an StringValue value from  opstack, and 
    extracts a substring of length count from the `value` of StringValue starting from `index`,
    pushes the substring back to opstack as a StringValue value. 
    """ 
    def getinterval(self):
        count = self.opPop() #value
        index = self.opPop() #index
        value = self.opPop() #item
        if isinstance(value, StringValue):#getinterval is a string only operator, i.e., works only with StringValue values. 
            if index >= 0 and index < len(str(value)) and count >= 0 and index+count <= len(str(value)):
                new_value = '(' + str(value.value[index+1:index+(count+1)]) + ')'
                self.opPush(StringValue(new_value))
            else:
                print("Error: put - Index out of bounds for StringValue")

    """
    putinterval is a string only operator, i.e., works only with StringValue values. 
    Pops a StringValue value, a (zero-based) `index`, a `substring` from  opstack, and 
    replaces the slice in StringValue's `value` from `index` to `index`+len(substring)  with the given `substring`s value. 
    """
    def putinterval(self):
        substring = self.opPop()
        index = self.opPop()
        value = self.opPop()

        if not isinstance(value, StringValue):
            print("Error: putinterval - Value must be a StringValue")
            return
        if not isinstance(substring, StringValue):
            print("Error: putinterval - Substring must be a StringValue")
            return
        if not isinstance(index, int):
            print("Error: putinterval - Index must be an integer")
            return
        if index < 0 or index >= len(value.value):
            print("Error: putinterval - Index out of range")
            return
        value_str = value.value[1:-1]  # remove parentheses from value
        substring_str = substring.value[1:-1]  # remove parentheses from substring
        new_value_str = value_str[:index] + substring_str + value_str[index+len(substring_str):]
        value.value = '(' + new_value_str + ')'  # add parentheses back to value
        #value.opPush() #I change the value of the variable that is being referenced and not push it back onto the stack


    """
    search is a string only operator, i.e., works only with StringValue values. 
    Pops two StringValue values: delimiter and inputstr
    if delimiter is a sub-string of inputstr then, 
       - splits inputstr at the first occurence of delimeter and pushes the splitted strings to opstack as StringValue values;
       - pushes True 
    else,
        - pushes  the original inputstr back to opstack
        - pushes False
    """
    def search(self):
         # Pop delimiter and inputstr from the stack
        delimiter = self.opPop()
        inputstr = self.opPop()
        length_str = inputstr.length()
        d_no_par = delimiter.value[1:-1] #takes off paraenthesis
        flag = True

        # Make sure both are strings
        if isinstance(delimiter, StringValue) and isinstance(inputstr, StringValue):
            for i in range(length_str): #from 0 to length of inputstr
                if inputstr.value[i] == d_no_par:
                    substringleft = StringValue(inputstr.value[:i] + ")")
                    substringright = StringValue("(" + inputstr.value[i+1:])
                    self.opPush(substringright)
                    self.opPush(delimiter)
                    self.opPush(substringleft)
                    self.opPush(True)
                    flag = False
                    break
        if flag == True:#This catches the case where passed parameters are not correct values and if the delimeter isn't in the stringvalue
            self.opPush(inputstr) # Push inputstr back to opstack
            self.opPush((False)) # Push False
            
        # else:
        #     self.opPush(inputstr) # Push inputstr back to opstack
        #     self.opPush((False)) # Push False
        #     print("Error: search - delimiter and inputstr must be StringValues")



    # ------- Operators that manipulate the dictstact --------------
    """ begin operator
        Pops a DictionaryValue value from opstack and pushes it's `value` to the dictstack."""
    def begin(self):
        dict_value = self.opPop()# pop a DictionaryValue object from the opstack
        if isinstance(dict_value, DictionaryValue):
            self.dictstack.append(dict_value.value) # push the 'value' attribute of the DictionaryValue object to the dictstack

        else:
            print("Error: begin - Top of stack is not a dictionary")

    """ end operator
        Pops the top dictionary from dictstack."""
    def end(self):
        if len(self.dictstack) > 0:
            self.dictstack.pop()
        else:
            print("Error: end - Dictionary stack is empty")
        
    """ Pops a name and a value from stack, adds the definition to the dictionary at the top of the dictstack. """
    def psDef(self):
        value = self.opPop()  # pop the value from the opstack
        name = self.opPop()  # pop the name from the opstack
        if len(self.dictstack) > 0:
            self.dictstack[-1][name] = value  # add the definition to the top dictionary in the dictstack
        else:
            self.dictstack.append({name: value})  # add the definition to a new dictionary at the top of the dictstack
            print("Error: psDef - Dictionary stack is empty")

#------------------------------------------------------------------------------------
#               PART 2               PART 2               PART 2               PART 2 
#------------------------------------------------------------------------------------
    # ------- if/ifelse Operators --------------
    """ if operator
        Pops a CodeArrayValue object and a boolean value, if the value is True, executes (applies) the code array by calling apply.
       Will be completed in part-2. 
    """
    def psIf(self):
        pass

    """ ifelse operator
        Pops two CodeArrayValue objects and a boolean value, if the value is True, executes (applies) the bottom CodeArrayValue otherwise executes the top CodeArrayValue.
        Will be completed in part-2. 
    """
    def psIfelse(self):
        pass


    #------- Loop Operators --------------
    """
       Implements for operator.   
       Pops a CodeArrayValue object, the end index (end), the increment (inc), and the begin index (begin) and 
       executes the code array for all loop index values ranging from `begin` to `end`. 
       Pushes the current loop index value to opstack before each execution of the CodeArrayValue. 
       Will be completed in part-2. 
    """ 
    def psFor(self):
        pass

    """ Cleans both stacks. """      
    def clearBoth(self):
        self.opstack[:] = []
        self.dictstack[:] = []

    """ Will be needed for part2"""
    def cleanTop(self):
        if len(self.opstack)>1:
            if self.opstack[-1] is None:
                self.opstack.pop()


