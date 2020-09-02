# Lab 4 Unittest

import unittest
from LAB4 import *

# Unittest encryption test cases
class test_encrypt(unittest.TestCase):
    
    def test_values(self):
        self.assertEqual(encrypt("Hello world",12), "Tqxxa iadxp")
        self.assertEqual(encrypt("My name is Kellen Cheng",4), 
                         "Qc reqi mw Oippir Glirk")
        self.assertEqual(encrypt("I like Candy",25), "H khjd Bzmcx")
        
    def test_input(self):
        self.assertEqual(encrypt("asgesw", 29.1), "error")
        self.assertEqual(encrypt("asgesw", 0.5), "error")
        self.assertEqual(encrypt(3, 29), "error")
        
# Unittest decryption test cases
class test_decrypt(unittest.TestCase):
    
    def test_values(self):
        self.assertEqual(decrypt("Tqxxa iadxp",12), "Hello world")
        self.assertEqual(decrypt("Qc reqi mw Oippir Glirk",4), 
                         "My name is Kellen Cheng")
        self.assertEqual(decrypt("H khjd Bzmcx",25), "I like Candy")
        
    def test_input(self):
        self.assertEqual(decrypt("asgesw", 29.1), "error")
        self.assertEqual(decrypt("asgesw", 0.5), "error")
        self.assertEqual(decrypt(3, 29), "error")
