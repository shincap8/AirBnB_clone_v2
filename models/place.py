#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import models
import os


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ ids:list of Amenity ids
    """
    __tablename__ = "places"
    metadata = Base.metadata
    place_amenity = Table('place_amenity', metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review',
                               cascade='all, delete', backref='place')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False,
                                 back_populates='place_amenities')
    else:
        @property
        def reviews(self):
            """
            reviews
            """
            objects = models.storage.all()
            my_reviews = []
            for key, obj in objects.items():
                cl_obj = obj.__class__.__name__
                if cl_obj == 'Review':
                    if obj.place_id == self.id:
                        my_reviews.append(obj)
            return (my_reviews)

        @property
        def amenities(self):
            """
            amenities
            """
            objects = models.storage.all()
            my_amenities = []
            for key, obj in objects.items():
                cl_obj = obj.__class__.__name__
                if cl_obj == 'Amenity':
                    if obj.place_id == self.id:
                        my_amenities.append(obj)
            return (my_amenities)

            @amenities.setter
            def amenities(self, obj):
                """
                amenities
                """
                if obj.__class__.__name__ == 'Amenity':
                    amenity_ids.append(obj.id)
