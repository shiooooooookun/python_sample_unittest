#coding:utf-8
import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_add_num(self):
        print '----足し算関数処理----'
        self.assertEqual(10,main.add_num(3,4))

    def test_minus_num(self):
        print '----引き算関数処理----'
        self.assertEqual(10,main.minus_num(20,10))

    def test_multi_num(self):
        print '----掛け算関数処理----'
        self.assertEqual(100,main.multi_num(10,10))

    def test_divise_num(self):
        print '----割り算関数処理----'
        self.assertFalse(main.divise_num(0,0))
        self.assertFalse(main.divise_num(1,0))
        self.assertFalse(main.divise_num(0,1))
        self.assertEqual(10,main.divise_num(100,10))
        
    def test_is_positive(self):
        print '----正の数判定処理----'
        self.assertTrue(main.is_positive(2))
        self.assertFalse(main.is_positive(0))
        self.assertFalse(main.is_positive(-1))

    def test_linear_search(self):
        print '----線形探索処理----'
        arr = [12,3,4,4,2,5,2,2,5,6,67,12,9,1,40]
        index = 5
        self.assertTrue(main.linear_search(arr,index))
