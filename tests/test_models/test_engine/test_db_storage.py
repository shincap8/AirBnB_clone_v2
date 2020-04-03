#!/usr/bin/python
"""Unittests for DBStorage class of AirBnb_Clone_v2"""
import unittest
import pep8
import os
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
import models
import MySQLdb


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db',
    "This test only work in DBStorage")
class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''
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

if __name__ == "__main__":
    unittest.main()
