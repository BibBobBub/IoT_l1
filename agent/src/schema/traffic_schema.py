from marshmallow import Schema, fields

class TrafficSchema(Schema):
    cars = fields.Int()
    #gps = fields.Nested(GpsSchema)
