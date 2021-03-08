import unittest

from questions.binary_search import *


class QuestionTestCase(unittest.TestCase):

    # 27
    def test_count_specific_number(self):
        self.assertEqual(count_specific_number([7, 2], [1, 1, 2, 2, 2, 3]), 4)
        self.assertEqual(count_specific_number([7, 4], [1, 1, 2, 2, 2, 3]), -1)

    # 28
    def test_find_fixed_point(self):
        # wilhe
        self.assertEqual(find_fixed_point(5, [-15, 6, 1, 3, 7]), 3)
        self.assertEqual(find_fixed_point(7, [-15, -4, 2, 8, 9, 13, 15]), 2)
        self.assertEqual(find_fixed_point(7, [-15, -4, 3, 8, 9, 13, 15]), -1)
        # 재귀
        self.assertEqual(find_fixed_point_reculsive(5, [-15, 6, 1, 3, 7]), 3)
        self.assertEqual(find_fixed_point_reculsive(7, [-15, -4, 2, 8, 9, 13, 15]), 2)
        self.assertEqual(find_fixed_point_reculsive(7, [-15, -4, 3, 8, 9, 13, 15]), -1)

    # 29. 공유기 설치
    def test_install_router(self):
        home_count, router_count = 5, 3
        home_coordinates: list = [1, 2, 8, 4, 9]
        self.assertEqual(install_router(home_count, router_count, home_coordinates), 3)
