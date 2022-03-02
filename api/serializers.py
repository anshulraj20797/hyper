from api import models
from rest_marshmallow  import Schema, fields
from api.models import Customer


# class CustomerSchema(Schema):
#     id = fields.Integer()
#     checked = fields.Boolean()
#     name = fields.Str()
#     type = fields.Str()
#     age = fields.Integer()
#     description = fields.Str()
#     date = fields.Date()

from rest_framework import serializers
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'