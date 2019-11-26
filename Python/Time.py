class Time:
    """Blueprint for a Time object"""
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0

    """Function to increment seconds"""
    def tick(self):
        self.__second += 1

        if (self.__second > 59) :
            self.__second = 0
            self.__minute += 1

            if (self.__minute > 59) :
                self.__minute = 0
                self.__hour += 1

                if (self.__hour > 23) :
                    self.__hour = 0


    """Function to set the time"""
    def set_time(self,hour,minute,second):
         self.set_hour(hour)
         self.set_minute(minute)
         self.set_second(second)

    """Function to print the time"""
    def print_time(self):
        print(self.__hour, ":",self.__minute,":",self.__second)


    """Setter function for Time variables"""
    def set_second(self,second):
        if (second >= 0 and second <= 59) :
           self.__second = second
        else :
            self.__second = 0

    def set_minute(self,minute):
        if (minute >= 0 and minute <= 59) :
            self.__minute = minute
        else :
            self.__minute = 0

    def set_hour(self,hour):
        if (hour >= 0 and hour <= 23) :
            self.__hour = hour
        else :
            self.__hour = 0


    """Getter function for Time variables"""
    def get_second(self):
        return self.__second
    def get_minute(self):
        return self.__minute
    def get_hour(self):
        return self.__hour
