import unittest
from cities import describe_city

class CityTest(unittest.TestCase):
    def test_city(self):
        city_country = describe_city('Santiago', 'Chile', '')
        self.assertEqual(city_country, 'Santiago Chile ')
    
    def test_city_population(self):
        city_country = describe_city('portland', 'usa', 50000)
        self.assertEqual(city_country, 'Portland Usa 50000')


unittest.main()