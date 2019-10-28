#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import dron

class TestDron(unittest.TestCase):

    def test_forward(self):
        dr = dron.Dron(6, 3)
        dr.identify_command('A')
        self.assertEqual(dr.posX, 0)
        self.assertEqual(dr.posY, 1)

    def test_rotate(self):
        dr = dron.Dron(6, 3)
        dr.identify_command('I')
        self.assertEqual(dr.degree, 180)
        self.assertEqual(dr.orientation, 'Occidente')
        dr.identify_command('D')
        dr.identify_command('D')
        self.assertEqual(dr.degree, 0)
        self.assertEqual(dr.orientation, 'Oriente')

    def test_error_forward(self):
        dr = dron.Dron(6, 3)
        cont = 0
        while cont < dr.maxPos:
            dr.forward()
            cont += 1
        self.assertEqual(dr.error, 1)

    #Error en el ejemplo del enunciado
    def test_enunciado(self):
        commands = 'AAAAIAAD'
        #Este si esta bien
        dr = dron.Dron(6, 3)
        for command in commands:
            dr.identify_command(command)
        self.assertEqual(dr.posX, -2)
        self.assertEqual(dr.posY, 4)
        self.assertEqual(dr.orientation, 'Norte')

        commands = 'DDAIAD'
        #Resultado del enunciado (-3,3) Sur
        for command in commands:
            dr.identify_command(command)
        self.assertEqual(dr.posX, -1)
        self.assertEqual(dr.posY, 3)
        self.assertEqual(dr.orientation, 'Sur')

        commands = 'AAIADAD'
        #Resultado del enunciado (-4,2) Oriente
        for command in commands:
            dr.identify_command(command)
        self.assertEqual(dr.posX, 0)
        self.assertEqual(dr.posY, 0)
        self.assertEqual(dr.orientation, 'Occidente')

if __name__ == "__main__":
    unittest.main()
