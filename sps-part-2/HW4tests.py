import sys
import io
import unittest
from HW5 import *

class HW4Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testOpPush(self):
        opstack.clear()
        opPush("(Hello)")
        self.assertEqual(opstack[-1],"(Hello)")
    
    def testOpPush2(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opstack[-1],5)

    def testOpPop(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opPop(),5)
    
    def testDictPush(self):
        dictstack.clear()
        dictPush({})
        self.assertEqual(dictstack[-1],{})

    def testDictPop(self):
        dictstack.clear()
        dictPush({})
        dictPop()
        self.assertEqual(len(dictstack),0)

    def testDefine(self):
        dictstack.clear()
        define("/a",1)
        self.assertEqual(len(dictstack),1)

    def testLookup(self):
        dictstack.clear()  
        opPush("/n1")       
        opPush("(hornswaggle)")  
        psDef()
        self.assertEqual(lookup("n1"),"(hornswaggle)")

    def testAdd1(self):
        opstack.clear()     
        opPush(1)       
        opPush(2)       
        add()       
        self.assertEqual(opPop(),3)

    def testAdd2(self):
        opstack.clear()     
        opPush(3)
        opPush("(notanum)")
        add()       
        self.assertEqual(opPop(),"(notanum)")
        self.assertEqual(opPop(),3)

    def testSub1(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        sub()
        self.assertEqual(opPop(),1)
    
    def testSub2(self):
        opstack.clear()
        opPush(3)
        opPush(5)
        sub()
        self.assertEqual(opPop(),-2)
    
    def testMul1(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        mul()
        self.assertEqual(opPop(),6)

    def testMul2(self):
        opstack.clear()
        opPush(5)
        opPush(5)
        mul()
        self.assertEqual(opPop(),25)

    def testDiv1(self):
        opstack.clear()
        opPush(10)
        opPush(2)
        div()
        self.assertEqual(opPop(),5)
    
    def testDiv2(self):
        opstack.clear()
        opPush(10)
        opPush(0)
        div()
        self.assertEqual(opPop(),0)
    
    def testMod1(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        mod()
        self.assertEqual(opPop(),1)

    def testMod2(self):
        opstack.clear()
        opPush(10)
        opPush(2)
        mod()
        self.assertEqual(opPop(),0)

    def testEq1(self):
        opstack.clear()
        opPush("test")
        opPush("test")
        eq()
        self.assertEqual(opPop(),True)

    def testEq2(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        eq()
        self.assertEqual(opPop(),False)

    def testLt1(self):
        opstack.clear()
        opPush(2)
        opPush(3)
        lt()
        self.assertEqual(opPop(),True)

    def testLt2(self):
        opstack.clear()
        opPush('a')
        opPush('b')
        lt()
        self.assertEqual(opPop(),True)

    def testGt1(self):
        opstack.clear()
        opPush('a')
        opPush('b')
        gt()
        self.assertEqual(opPop(),False)

    def testGt2(self):
        opstack.clear()
        opPush(2)
        opPush(3)
        gt()
        self.assertEqual(opPop(),False)

    def testLength(self):
        opstack.clear()
        opPush("(Hello)")
        length()
        self.assertEqual(opPop(),5)

    def testGet(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        get()
        self.assertEqual(opPop(),ord('C'))

    def testGetInterval(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),"(Cpt)")

    def testGetInterval2(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(4)
        opPush(7)
        getinterval()
        self.assertEqual(opPop(),"(355)")

    def testPut(self):
        opstack.clear()
        opPush("(CptS355)")
        dup()
        opPush(0)
        opPush(48)
        put()
        self.assertEqual(opPop(),"(0ptS355)")

    def testDup(self):
        opstack.clear()
        opPush(3)
        dup()
        self.assertEqual(len(opstack),2)

    def testCopy(self):
        opstack.clear()
        opPush(7)
        opPush(8)
        opPush(9)
        opPush(2)
        copy()
        self.assertEqual(len(opstack),5) #before copy opstack [7,8,9,2] After [7,8,9,8,9]

    def testPop(self):
        opstack.clear()
        opPush(1)
        pop()
        self.assertEqual(len(opstack),0)
    
    def testClear(self):
        opstack.clear()
        opPush(1)
        clear()
        self.assertEqual(len(opstack),0)

    def testExch(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        exch()
        self.assertListEqual(opstack,[2,1])

    def testRoll1(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(2)
        opPush(3)
        roll()
        self.assertListEqual(opstack,[1,2,4,3])

    def testRoll2(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(5)
        opPush(4)
        opPush(-2)
        roll()
        self.assertListEqual(opstack,[1,4,5,2,3])

    def testStack(self):
        pass # unsure how to test print, maybe have it return instead
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        opPush(2)
        opPush(3)
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "3\n2\n")

    def testPsDict(self):
        opstack.clear()
        opPush(2)
        psDict()
        self.assertIsInstance(opPop(), dict)

    def testPsDef(self):
        opstack.clear()
        dictstack.clear()
        opPush(2)
        psDict()
        begin()
        opPush("/a")
        opPush(2)
        psDef()
        self.assertEqual(dictstack[-1],{"/a":2})

    def testParse(self):
        opstack.clear()
        input_list = ['/pow2', '{', '/n', 'exch', 'def', '(Pow2_of_n_is)', 'dup', '8', 'n', '48', 'add', 'put', '1', 'n', '-1', '1', '{', 'pop', '2', 'mul', '}', 'for', '}', 'def', '(Calculating_pow2_of_9)', 'dup', '20', 'get', '48', 'sub', 'pow2', 'stack']
        result = parse(input_list)
        answerParse = ['/pow2', ['/n', 'exch', 'def', '(Pow2_of_n_is)', 'dup', 8, 'n', 48, 'add', 'put', 1, 'n', -1, 1, ['pop', 2, 'mul'], 'for'], 'def', '(Calculating_pow2_of_9)', 'dup', 20, 'get', 48, 'sub', 'pow2', 'stack']
        self.assertEqual(result,answerParse)
        # print(result)
        # print(type(answerParse[1][5]))
        # print(type(result[1][5]))
        # if result[1][5] == answerParse[1][5]:
        #     print("Parse2: True")
        # else:
        #     print("Parse2: False")

if __name__ == '__main__':
    unittest.main()

