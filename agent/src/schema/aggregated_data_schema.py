from marshmallow import Schema, fields
from schema.accelerometer_schema import AccelerometerSchema
from schema.gps_schema import GpsSchema
from schema.traffic_schema import TrafficSchema


class AggregatedDataSchema(Schema):
    accelerometer = fields.Nested(AccelerometerSchema)
    gps = fields.Nested(GpsSchema)
    #cars = fields.Nested(TrafficSchema)
    cars = fields.Nested(TrafficSchema, attribute="traffic")
    timestamp = fields.DateTime("iso")
    user_id = fields.Int()
