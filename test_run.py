#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import run

class TestRoute(unittest.TestCase):

    def test_regex(self):
        dr = run.Dron(6, 10)
        route = run.Route(0)
        error, message = route.orders('12344',dr)
        self.assertEqual(error, 2)

    def test_normal_execution(self):
        dr = run.Dron(6, 10)
        route = run.Route(0)
        error, message = route.orders('AAIAA',dr)
        self.assertEqual(error, 0)

if __name__ == "__main__":
    unittest.main()
