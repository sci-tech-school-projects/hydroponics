import RPi.GPIO as GPIO
import time, datetime, calendar


class Auto_Watering():
    pin = 21
    time_froms = ["06:45:00" ]
    time_tos = ["07:00:00" ]

    def __init__(self):
        print("***** init Auto_Watering")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self._Flow_Water(2)

    def Main(self):
        while True:
            now = datetime.datetime.now()
            for time_from, time_to in zip(self.time_froms, self.time_tos):
                time_from = self.gen_datetime_from_time(time_from)
                time_to = self.gen_datetime_from_time(time_to)
                if (time_from < now < time_to):
                    print(time_from , now , time_to,sep=" ")
                    self._Flow_Water(20)
            time.sleep(900)

    def _Flow_Water(self, sec):
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(self.pin, GPIO.LOW)
        print("***** {} seconds watering done".format(sec))

    def gen_datetime_from_time(self, _time):
        """
        :param _time: write like "06:45:00"
        :return: datetime object
        """
        # str type
        _time = datetime.datetime.now().strftime("%Y-%m-%d") + " " + _time
        _time = time.strptime(_time, "%Y-%m-%d %H:%M:%S")
        # datetime type
        _time = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=calendar.timegm(_time))
        return _time



if __name__ == '__main__':
    AW = Auto_Watering()
    AW.Main()

