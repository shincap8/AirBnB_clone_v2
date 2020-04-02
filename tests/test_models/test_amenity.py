#!/usr/bin/python3
"""test for amenity"""
import unittest
import os
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.base_model import BaseModel
import models
import pep8


class TestAmenity(unittest.TestCase):
    """this will test the Amenity class"""
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Won't work in FileStorage")
    def test_amenity_dbstorage(self):
        my_state = State(name="Pennsylvania")
        my_city = City(state_id=my_state.id, name="Pittsburgh")
        my_self = User(email="jane@doe.com", password="janepwd")
        my_place1 = Place(user_id=my_self.id, city_id=my_city.id,
                          name="My Crib")
        my_place2 = Place(user_id=my_self.id,
                          city_id=my_city.id, name="My Lodge")
        amenity_1 = Amenity(name="Wifi")
        amenity_2 = Amenity(name="Cable")
        amenity_3 = Amenity(name="Air conditioner")
        my_place1.amenities.append(amenity_1)
        my_place1.amenities.append(amenity_2)
        my_place2.amenities.append(amenity_1)
        my_place2.amenities.append(amenity_2)
        my_place2.amenities.append(amenity_3)
        models.storage.save()
        if amenity_1.id in models.storage.all():
            self.assertEqual(amenity_1.name, "Wifi")
        if amenity_1.id in models.storage.all():
            self.assertEqual(amenity_2.name, "Cable")
        if amenity_1.id in models.storage.all():
            self.assertEqual(amenity_3.name, "Air conditioner")
        self.assertIn(amenity_1.id, my_place1.amenities)
        self.assertIn(amenity_2.id, my_place1.amenities)
        self.assertIn(amenity_1.id, my_place2.amenities)
        self.assertIn(amenity_2.id, my_place2.amenities)
        self.assertIn(amenity_3.id, my_place2.amenities)

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Won't work in DB")
    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.amenity

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Won't work in DB")
    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Won't work in DB")
    def test_pep8_Amenity(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Won't work in DB")
    def test_checking_for_docstring_Amenity(self):
        """checking for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Won't work in DB")
    def test_attributes_Amenity(self):
        """chekcing if amenity have attibutes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Won't work in DB")
    def test_is_subclass_Amenity(self):
        """test if Amenity is subclass of Basemodel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Won't work in DB")
    def test_attribute_types_Amenity(self):
        """test attribute type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Won't work in DB")
    def test_save_Amenity(self):
        """test if the save works"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Won't work in DB")
    def test_to_dict_Amenity(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
