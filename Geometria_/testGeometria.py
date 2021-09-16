import unittest

from main import g
import model.Geometria as G
from view.View import View

class testGeometria(unittest.TestCase):





    @classmethod
    def setUpClass(cls):
        print('setUpClass() -> OK')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass() -> OK')

    def setUp(self):
        print('SetUp() -> OK')


    #TEST FUNCIONES AREAS
    def test_areaCuadrado(self):

        FIG = G.Geometria(2.00, 3.10, 4.0)
        RES = FIG.switch(1)
        self.assertEqual(RES,4)
        print('test_areaCuadrado() -> OK')



    #TESTS NOMBRES FIGURA
    def test_set_figuraName1(self):

        FIG = G.Geometria(2.00, 3.10, 4.0)
        FIG.set_figuraName(1)
        self.assertEqual(FIG.figuraName,'Cuadrado')
        print('test_set_figuraName1() -> OK')

    def test_set_figuraName2(self):

        FIG = G.Geometria(2.00, 3.10, 4.0)
        FIG.set_figuraName(2)
        self.assertEqual(FIG.figuraName,'Circulo')
        print('test_set_figuraName2() -> OK')


    def test_set_figuraName3(self):

        FIG = G.Geometria(2.00, 3.10, 4.0)
        FIG.set_figuraName(3)
        self.assertEqual(FIG.figuraName,'Tiangulo')
        print('test_set_figuraName3() -> OK')


    def test_set_figuraName4(self):
        FIG = G.Geometria(2.00, 3.10, 4.0)
        FIG.set_figuraName(4)
        self.assertEqual(FIG.figuraName, 'Rectangulo')
        print('test_set_figuraName4() -> OK')


    def test_set_figuraName5(self):
        FIG = G.Geometria(2.00, 3.10, 4.0)
        FIG.set_figuraName(5)
        self.assertEqual(FIG.figuraName, 'Pentagono')
        print('test_set_figuraName5() -> OK')

    def test_set_figuraName6(self):
        FIG = G.Geometria(2.00, 3.10, 4.0)
        FIG.set_figuraName(6)
        self.assertEqual(FIG.figuraName, 'Rombo')
        print('test_set_figuraName6() -> OK')

    def test_set_figuraName7(self):
        FIG = G.Geometria(2.00, 3.10, 4.0)
        FIG.set_figuraName(7)
        self.assertEqual(FIG.figuraName, 'Romboide')
        print('test_set_figuraName7() -> OK')

    def test_set_figuraName8(self):
        FIG = G.Geometria(2.00, 3.10, 4.0)
        FIG.set_figuraName(8)
        self.assertEqual(FIG.figuraName, 'Trapecio')
        print('test_set_figuraName8() -> OK')


    #TEST SWITCH
    def test_select(self):
        FIG = G.Geometria(2.00, 3.10, 4.0)
        FIG.set_figuraName(4)
        RES = View()
        RES.select(FIG)


    def tearDown(self):
        print('tearDown() -> OK')
