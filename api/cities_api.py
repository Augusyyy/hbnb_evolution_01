from datetime import datetime
from flask_restx import Resource, Api, fields
from flask import Flask, jsonify, request
from api import cities_api
from model.city import City

city_model = cities_api.model('City', {
    'country_id': fields.String(required=True, description='Country id'),
    'name': fields.String(required=True, description='City name')
})


@cities_api.route("/")
class NewCity(Resource):
    @cities_api.expect(city_model)
    @cities_api.doc('creat new city')
    def post(self):
        pass

    @cities_api.doc('Retrieve all cities.')
    def get(self):
        pass


@cities_api.route('/<string:country_id>')
class Cities(Resource):
    @cities_api.doc('Retrieve details ofa specific city')
    def get(self, country_id):
        pass

    @cities_api.doc('Update an existing cities inform')
    @cities_api.expect(city_model)
    def put(self, country_id):
        pass

    @cities_api.doc('Delete a specific city')
    def delete(self, country_id):
        pass




