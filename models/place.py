#!/usr/bin/python3
"""Defines the class, Place."""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place.

    Public class attributes:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name: string - empty string
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: (str) - empty list: it will be the list of
        Amenity.id later
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __str__(self):
        """Return the string representation of the Place object."""
        return "[Place] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        """Return a dictionary representation of the Place object."""
        place_dict = self.__dict__.copy()
        place_dict["__class__"] = self.__class__.__name__
        place_dict["created_at"] = self.created_at.isoformat()
        place_dict["updated_at"] = self.updated_at.isoformat()
        place_dict["city_id"] = self.city_id
        return place_dict
