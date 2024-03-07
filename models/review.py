#!/usr/bin/python3
"""Defines the class Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review.

    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new Review.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """Return the string representation of the Review object."""
        return "[Review] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        """Return a dictionary representation of the Review object."""
        review_dict = self.__dict__.copy()
        review_dict["__class__"] = self.__class__.__name__
        review_dict["created_at"] = self.created_at.isoformat()
        review_dict["updated_at"] = self.updated_at.isoformat()
        review_dict["place_id"] = self.place_id
        return review_dict

    @property
    def text(self):
        """Getter method for text attribute."""
        return self.__text

    @text.setter
    def text(self, value):
        """Setter method for text attribute."""
        if not isinstance(value, str):
            raise TypeError("text must be a string")
        if len(value) != 1000:
            raise ValueError("text must be 1000 characters long")
        self.__text = value
