#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    # Test pour liste vide
    def test_empty_list(self):
        self.assertIsNone(max_integer([]), "Max of empty list should be None")

    # Test pour une seule valeur
    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42, "Max of single element list should be the element itself")

    # Max au début
    def test_max_at_start(self):
        self.assertEqual(max_integer([9, 3, 5]), 9)

    # Max à la fin
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 3, 8]), 8)

    # Max au milieu
    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 7, 3]), 7)

    # Nombres négatifs
    def test_all_negative(self):
        self.assertEqual(max_integer([-10, -5, -20]), -5)

    # Mélange négatifs et positifs
    def test_mixed_signs(self):
        self.assertEqual(max_integer([-1, 0, 5, -3]), 5)

    # Liste avec des floats
    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.3, 0.7]), 2.3)

    # Liste avec répétitions
    def test_repetitions(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    # Liste avec un seul élément négatif
    def test_single_negative(self):
        self.assertEqual(max_integer([-7]), -7)

    # Test pour liste très grande
    def test_large_list(self):
        lst = list(range(1000))
        self.assertEqual(max_integer(lst), 999)

    # Test pour liste avec valeurs identiques mais mélangées
    def test_identical_mixed_positions(self):
        self.assertEqual(max_integer([5, 1, 5, 3, 5]), 5)

if __name__ == "__main__":
    unittest.main()
