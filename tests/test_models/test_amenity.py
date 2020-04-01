#!/usr/bin/python3
"""test for amenity"""
import unittest
import os
from models.amenity import Amenity
from models.states import State
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """this will test the Amenity class"""

    def test_amenity_dbstorage:
        my_state = State(name="Pennsylvania")
        my_city = City(state_id=my_state.id, name="Pittsburgh")
        my_self = User(email="jane@doe.com", password="janepwd")
        my_place1 = Place(user_id=my_self.id,
                            city_id=my_city.id, name="My Crib")
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
        storage.save()
        self.assertEqual(amenity_1.name, "Wifi")
        self.assertEqual(amenity_2.name, "Cable")
        self.assertEqual(amenity_3.name, "Air conditioner")
        self.assertIn(amenity_1.id, my_place1)
        self.assertIn(amenity_2.id, my_place1)
        self.assertIn(amenity_1.id, my_place2)
        self.assertIn(amenity_2.id, my_place2)
        self.assertIn(amenity_3.id, my_place2)

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.amenity

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Amenity(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Amenity(self):
        """checking for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """chekcing if amenity have attibutes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_Amenity(self):
        """test if Amenity is subclass of Basemodel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """test attribute type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def test_save_Amenity(self):
        """test if the save works"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
