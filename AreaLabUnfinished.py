import math #lets use math module
import unittest # helps test small sections of code 

def circleArea(radius): 
    return radius*radius*math.pi

def rectArea(base, height):
    return base*height

def trapArea(base1, base2, height):
    return  height*(base1 + base2) / 2

def triArea(base,height):
    return base*height / 2
    
	
class MyTest(unittest.TestCase):# using TestCase class from unittest module 
    def testCircleArea(self):
        self.assertEqual(circleArea(5),25*math.pi)
        self.assertAlmostEqual(circleArea(7),49*math.pi)
        
    def testRectArea(self):
         self.assertEqual(rectArea(5,5),25)
         self.assertEqual(rectArea(10,10),100)
    def testTrapArea(self):
         self.assertEqual(trapArea(5,5,5), 5 * (5 + 5) / 2)
         self.assertEqual(trapArea(10,10,10), 10 * (10 + 10) / 2)
    def testTriArea(self):
         self.assertEqual(triArea(5,5),5*5/2)
         self.assertEqual(triArea(10,10),10*10/2)