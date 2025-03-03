from csv import reader
from datetime import datetime
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.traffic import Traffic
from domain.aggregated_data import AggregatedData
import config


class FileDatasource:
    def __init__(
        self,
        accelerometer_filename: str,
        gps_filename: str,
        traffic_filename: str,
    ) -> None:
        self.accelerometer_filename = "data/accelerometer.csv"
        self.gps_filename = "data/gps.csv"
        self.traffic_filename = "data/traffic.csv"
        self.accelerometer_data = None
        self.gps_data = None
        self.traffic_data = None

    def read(self) -> AggregatedData:
        
        if self.accelerometer_data is None or self.gps_data is None or self.traffic_data is None:
            raise ValueError("Data must be read first by calling startReading.")
        
        
        accelerometer = self.accelerometer_data.pop(0) 
        gps = self.gps_data.pop(0)  
        cars = self.traffic_data.pop(0)
        return AggregatedData(
            Accelerometer(accelerometer[0], accelerometer[1], accelerometer[2]),
            Gps(gps[0], gps[1]),
            Traffic(cars[0]),
            datetime.now(),
            config.USER_ID
        )

    def startReading(self, *args, **kwargs):
        self.accelerometer_data = self._read_csv(self.accelerometer_filename)
        self.gps_data = self._read_csv(self.gps_filename)
        self.traffic_data = self._read_csv(self.traffic_filename)

    def stopReading(self, *args, **kwargs):
        self.accelerometer_data = None
        self.gps_data = None
        self.traffic_data = None

    def _read_csv(self, filename: str):
        data = []
        with open(filename, newline='') as csvfile:
            csv_reader = reader(csvfile)
            for row in csv_reader:
                try:
                    data.append([float(val) for val in row])  
                except:
                    print("err")
        return data
