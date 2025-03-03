from dataclasses import dataclass

from datetime import datetime
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.traffic import Traffic

@dataclass
class AggregatedData:
    accelerometer: Accelerometer
    gps: Gps
    traffic: Traffic
    timestamp: datetime
    user_id: int
