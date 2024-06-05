import datetime
import json
from enum import Enum

from model.amenity import Amenity
from model.city import City
from data.IPersistenceManager import IPersistenceManager
from model.country import Country
from model.place import Place
from model.review import Review
from model.user import User
from datetime import datetime


class EntityType(Enum):
    COUNTRY = "country"
    PLACE = "place"
    REVIEW = "review"
    USER = "user"
    AMENITY = "amenity"
    CITY = "city"


class DataManager(IPersistenceManager):

    def __init__(self):
        """init attribute in memory
        attribute is private"""
        self.__user = {}
        self.__countries = {}
        self.__cities = {}
        self.__places = {}
        self.__amenity = {}
        self.__review = {}

        """from json file load data 
                save in attribute"""
        filename = 'data/' + EntityType.USER.value + '.json'
        with open(filename, "r") as f:
            self.__user = json.loads(f.read())

        filename = 'data/' + EntityType.COUNTRY.value + '.json'
        with open(filename, "r") as f:
            self.__countries = json.loads(f.read())

        filename = 'data/' + EntityType.CITY.value + '.json'
        with open(filename, "r") as f:
            self.__cities = json.loads(f.read())

        filename = 'data/' + EntityType.PLACE.value + '.json'
        with open(filename, "r") as f:
            self.__places = json.loads(f.read())

        filename = 'data/' + EntityType.AMENITY.value + '.json'
        with open(filename, "r") as f:
            self.__amenity = json.loads(f.read())

        filename = 'data/' + EntityType.REVIEW.value + '.json'
        with open(filename, "r") as f:
            self.__review = json.loads(f.read())

    def delete(self, entity_id, entity_type):
        filename = 'data/' + entity_type.value + '.json'
        try:
            with open(filename, "r") as f:
                if entity_type == EntityType.USER:
                    self.__user = json.loads(f.read())
        except FileNotFoundError:
            if entity_type == EntityType.USER:
                self.__user = {}

    def save(self, entity):
        if isinstance(entity, User):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'first_name': entity.first_name,
                'last_name': entity.last_name,
                'email': entity.email,
                'password': entity.password
            }
            # add data to memory
            self.__user['User'].append(new_entity)
            # flush json file
            filename = 'data/' + EntityType.USER.value + '.json'
            with open(filename, "w") as f:
                f.write(json.dumps(self.__user, indent=4))

        elif isinstance(entity, Review):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'commentor_user_id': entity.commentor_user_id,
                'place_id': entity.place_id,
                'feedback': entity.feedback,
                'rating': entity.rating
            }
            # add data to memory
            self.__review['Review'].append(new_entity)
            # flush json file
            filename = 'data/' + EntityType.REVIEW.value + '.json'
            with open(filename, "w") as f:
                f.write(json.dumps(self.__review, indent=4))   #4个缩进

        elif isinstance(entity, Place):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'name': entity.name,
                'description': entity.description,
                'address': entity.address,
                'latitude': entity.latitude,
                'longitude': entity.longitude,
                'number_of_rooms': entity.number_of_rooms,
                'bathrooms': entity.bathrooms,
                'price_per_night': entity.price_per_night,
                'max_guests': entity.max_guests
            }
            # add data to memory
            self.__places['Place'].append(new_entity)
            # flush json file
            filename = 'data/' + EntityType.PLACE.value + '.json'
            with open(filename, "w") as f:
                f.write(json.dumps(self.__places, indent=4))

        elif isinstance(entity, Amenity):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'name': entity.name
            }
            # add data to memory
            self.__amenity['Amenity'].append(new_entity)
            # flush json file
            filename = 'data/' + EntityType.AMENITY.value + '.json'
            with open(filename, "w") as f:
                f.write(json.dumps(self.__amenity, indent=4))

        elif isinstance(entity, Country):
            pass

        elif isinstance(entity, City):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'country_id': entity.country_id,
                'name': entity.name
            }
            # add data to memory
            self.__cities['Cities'].append(new_entity)
            # flush json file
            filename = 'data/' + EntityType.CITY.value + '.json'
            with open(filename, "w") as f:
                f.write(json.dumps(self.__cities, indent=4))

        else:
            raise TypeError("Unsupported entity type")

    def update(self, entity):
        if isinstance(entity, User):
            for idx, user in enumerate(self.__user['User']):
                if user['id'] == entity.id:
                    updated_user = {
                        'id': entity.id,
                        'created_at': entity.created_at,
                        'updated_at': entity.updated_at,
                        'first_name': entity.first_name,
                        'last_name': entity.last_name,
                        'email': entity.email,
                        'password': entity.password
                    }
                    self.__user['User'][idx] = updated_user
                    filename = 'data/' + EntityType.USER.value + '.json'
                    with open(filename, "w") as f:
                        f.write(json.dumps(self.__user, indent=4))
                    return updated_user
            return None

        elif isinstance(entity, Review):
            for idx, review in enumerate(self.__review['Review']):
                if review['id'] == entity.id:
                    updated_review = {
                        'id': entity.id,
                        'created_at': entity.created_at,
                        'updated_at': entity.updated_at,
                        'commentor_user_id': entity.commentor_user_id,
                        'place_id': entity.place_id,
                        'feedback': entity.feedback,
                        'rating': entity.rating
                    }
                    self.__review['Review'][idx] = updated_review
                    filename = 'data/' + EntityType.REVIEW.value + '.json'
                    with open(filename, "w") as f:
                        f.write(json.dumps(self.__review, indent=4))
                    return updated_review
            return None

        elif isinstance(entity, Place):
            for idx, place in enumerate(self.__places['Place']):
                if place['id'] == entity.id:
                    updated_place = {
                        'id': entity.id,
                        'created_at': entity.created_at,
                        'updated_at': entity.updated_at,
                        'name': entity.name,
                        'description': entity.description,
                        'address': entity.address,
                        'latitude': entity.latitude,
                        'longitude': entity.longitude,
                        'number_of_rooms': entity.number_of_rooms,
                        'bathrooms': entity.bathrooms,
                        'price_per_night': entity.price_per_night,
                        'max_guests': entity.max_guests
                    }
                    self.__places['Place'][idx] = updated_place
                    filename = 'data/' + EntityType.PLACE.value + '.json'
                    with open(filename, "w") as f:
                        f.write(json.dumps(self.__places, indent=4))
                    return updated_place
            return None

        elif isinstance(entity, Amenity):
            for idx, amenity in enumerate(self.__amenity['Amenity']):
                if amenity['id'] == entity.id:
                    updated_amenity = {
                        'id': entity.id,
                        'created_at': entity.created_at,
                        'updated_at': entity.updated_at,
                        'name': entity.name
                    }
                    self.__amenity['Amenity'][idx] = updated_amenity
                    filename = 'data/' + EntityType.AMENITY.value + '.json'
                    with open(filename, "w") as f:
                        f.write(json.dumps(self.__amenity, indent=4))
                    return updated_amenity
            return None

        elif isinstance(entity, Country):
            for idx, country in enumerate(self.__countries['Country']):
                if country['id'] == entity.id:
                    updated_country = {
                        'id': entity.id,
                        'created_at': entity.created_at,
                        'updated_at': entity.updated_at,
                        'name': entity.name,
                        'code': entity.code
                    }
                    self.__countries['Country'][idx] = updated_country
                    filename = 'data/' + EntityType.COUNTRY.value + '.json'
                    with open(filename, "w") as f:
                        f.write(json.dumps(self.__countries, indent=4))
                    return updated_country
            return None

        elif isinstance(entity, City):
            for idx, city in enumerate(self.__cities['City']):
                if city['id'] == entity.id:
                    updated_city = {
                        'id': entity.id,
                        'created_at': entity.created_at,
                        'updated_at': entity.updated_at,
                        'country_id': entity.country_id,
                        'name': entity.name
                    }
                    self.__cities['City'][idx] = updated_city
                    filename = 'data/' + EntityType.CITY.value + '.json'
                    with open(filename, "w") as f:
                        f.write(json.dumps(self.__cities, indent=4))
                    return updated_city
            return None

        else:
            raise TypeError("Unsupported entity type")

    def get(self, entity_id, entity_type):
        if entity_type == EntityType.USER:
            for user in self.__user['User']:
                if user['id'] == entity_id:
                    return user
            return None
        elif entity_type == EntityType.REVIEW:
            for review in self.__review['Review']:
                if review['id'] == entity_id:
                    return review
            return None
        elif entity_type == EntityType.PLACE:
            for place in self.__places['Place']:
                if place['id'] == entity_id:
                    return place
            return None
        elif entity_type == EntityType.AMENITY:
            for amenity in self.__amenity['Amenity']:
                if amenity['id'] == entity_id:
                    return amenity
            return None
        elif entity_type == EntityType.COUNTRY:
            for country in self.__countries['Country']:
                if country['id'] == entity_id:
                    return country
            return None
        elif entity_type == EntityType.CITY:
            for city in self.__cities['City']:
                if city['id'] == entity_id:
                    return city
            return None
        else:
            raise TypeError("Unsupported entity type")




