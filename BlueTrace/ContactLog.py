import time

timeFormat = "%d/%m/%Y %H:%M:%S"


class Log:
    def __init__(self, temp_id, start_time, expire_time):
        self.tempId = temp_id
        self.startTime = start_time
        self.expireTime = expire_time

    def __eq__(self, other):
        return self.tempId == other.tempId and self.startTime == other.startTime and self.expireTime == other.expireTime

    def __hash__(self):
        return hash((self.tempId, self.startTime, self.expireTime))

    def isValid(self):
        current_time = time.time()
        if txt2time(self.startTime) < current_time < txt2time(self.expireTime):
            return True
        else:
            return False

    def isLaterThan(self, log):
        return txt2time(self.startTime) > txt2time(log.startTime)


def txt2time(string):
    return time.mktime(time.strptime(string, timeFormat))


def time2txt(t):
    return time.strftime(timeFormat, time.localtime(t))


def generateLog(temp_id):
    return Log(temp_id, time2txt(time.time()), time2txt(time.time() + 900))


