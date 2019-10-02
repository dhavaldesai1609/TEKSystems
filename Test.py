import unittest
import Geography as mainGeo


class MyTestCase(unittest.TestCase):
    city_name = "eesti"
    city_code = 372
    mainObj = mainGeo.Geography(name=city_name, code=city_code)

    city_name = "dsfgsfdg"
    city_code = 44444
    mainObj2 = mainGeo.Geography(name=city_name, code=city_code)

    def test_city(self):
        cname = self.mainObj.get_capital_city()
        self.assertEqual("Tallinn", cname)

    def test_city_negative(self):
        cname = self.mainObj2.get_capital_city()
        self.assertEqual("Invalid City name or City Not Found", cname)

    def test_code(self):
        ccode = self.mainObj.get_capital_city()
        self.assertEqual("Tallinn", ccode)

    def test_code_negative(self):
        ccode = self.mainObj2.get_capital_city()
        self.assertEqual("Invalid City name or City Not Found", ccode)



if __name__ == '__main__':
    unittest.main()
