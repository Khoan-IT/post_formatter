import re
import dateparser as dp
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from time_pattern import composed_pattern


time_period = {
    'sáng': ['7:00', '11:00'],
    'trưa': ['11:00', '13:00'],
    'chiều': ['13:00', '17:00'],
    'tối': ['17:00', '20:00']
}

class TimeParser:
    def __init__(self):
        self.today = datetime.now().date()
        self.current_day = self.today.strftime("%d")
        self.current_month = self.today.strftime("%m")
        self.current_year = self.today.strftime("%Y")

    def time_parser(self, raw_time):
        for key, pattern in composed_pattern.items():
            value = re.findall(pattern, raw_time)
            if value:
                result = getattr(TimeParser, "parse_" + key)(self, value[0], key)

                return result

    def parse_time_period(self, value, key=None):
        return time_period.get(value, None)

    def parse_number_previous_day(self, value, key=None):
        return (
            self.today + timedelta(days=-int(value))
        ).strftime('%d/%m/%Y')

    def parse_previous_day(self, value=None, key=None):
        return (
            self.today + timedelta(days=-1)
        ).strftime('%d/%m/%Y')

    def parse_today(self, value=None, key=None):
        return self.today.strftime('%d/%m/%Y')

    def parse_the_next_day(self, value=None, key=None):
        return (
            self.today + timedelta(days=1)
        ).strftime('%d/%m/%Y')

    def parse_double_next_day(self, key=None, value=None):
        return (
            self.today + timedelta(days=2)
        ).strftime('%d/%m/%Y')

    def parse_triple_next_day(self, key=None, value=None):
        return (
            self.today + timedelta(days=3)
        ).strftime('%d/%m/%Y')

    def parse_number_next_day(self, value, key=None):
        return (
            self.today + timedelta(days=int(value))
        ).strftime('%d/%m/%Y')

    def parse_begin_of_previous_week(self, value, key=None):
        base_day = dp.parse("tuần trước").date()
        offset_to_monday = base_day.weekday() % 7
        return [
            (base_day - timedelta(days=offset_to_monday)).strftime('%d/%m/%Y'),
            (base_day - timedelta(days=offset_to_monday-2)).strftime('%d/%m/%Y')
        ]

    def parse_end_of_previous_week(self, value, key=None):
        base_day = dp.parse("tuần trước").date()
        offset_to_monday = base_day.weekday() % 7
        return [
            (base_day - timedelta(days=offset_to_monday-4)).strftime('%d/%m/%Y'),
            (base_day - timedelta(days=offset_to_monday-6)).strftime('%d/%m/%Y')
        ]

    def parse_all_previous_week(self, value, key=None):
        base_day = dp.parse("tuần trước").date()
        offset_to_monday = base_day.weekday() % 7
        return [
            (base_day - timedelta(days=offset_to_monday)).strftime('%d/%m/%Y'),
            (base_day - timedelta(days=offset_to_monday-6)).strftime('%d/%m/%Y')
        ]

    def parse_begin_of_current_week(self, value, key=None):
        base_day = self.today
        offset_to_monday = base_day.weekday() % 7
        return [
            (base_day - timedelta(days=offset_to_monday)).strftime('%d/%m/%Y'),
            (base_day - timedelta(days=offset_to_monday-2)).strftime('%d/%m/%Y')
        ]

    def parse_end_of_current_week(self, value, key=None):
        base_day = self.today
        offset_to_monday = base_day.weekday() % 7
        return [
            (base_day - timedelta(days=offset_to_monday-4)).strftime('%d/%m/%Y'),
            (base_day - timedelta(days=offset_to_monday-6)).strftime('%d/%m/%Y')
        ]

    def parse_all_current_week(self, value, key=None):
        base_day = self.today
        offset_to_monday = base_day.weekday() % 7
        return [
            (base_day - timedelta(days=offset_to_monday)).strftime('%d/%m/%Y'), 
            (base_day - timedelta(days=offset_to_monday-6)).strftime('%d/%m/%Y')
        ]

    def parse_begin_of_next_week(self, value, key=None):
        base_day = dp.parse("tuần sau").date()
        offset_to_monday = base_day.weekday() % 7
        return [
            (base_day - timedelta(days=offset_to_monday)).strftime('%d/%m/%Y'),
            (base_day - timedelta(days=offset_to_monday-2)).strftime('%d/%m/%Y')
        ]

    def parse_end_of_next_week(self, value, key=None):
        base_day = dp.parse("tuần sau").date()
        offset_to_monday = base_day.weekday() % 7
        return [
            (base_day - timedelta(days=offset_to_monday-4)).strftime('%d/%m/%Y'),
            (base_day - timedelta(days=offset_to_monday-6)).strftime('%d/%m/%Y')
        ]

    def parse_all_next_week(self, value=None, key=None):
        base_day = dp.parse("tuần sau").date()
        offset_to_monday = base_day.weekday() % 7
        return [
            (base_day - timedelta(days=offset_to_monday)).strftime('%d/%m/%Y'),
            (base_day - timedelta(days=offset_to_monday-6)).strftime('%d/%m/%Y')
        ]

    def parse_begin_of_previous_month(self, value=None, key=None):
        time = (self.today + relativedelta(months=-1)).strftime('/%m/%Y')
        return ['01'+time, '05'+time]

    def parse_end_of_previous_month(self, value=None, key=None):
        time = (self.today + relativedelta(months=-1)).strftime('/%m/%Y')
        return ['25'+time, '31'+time]

    def parse_all_previous_month(self, value, key=None):
        time = (self.today + relativedelta(months=-1)).strftime('%m/%Y')
        return time

    def parse_begin_of_current_month(self, value, key=None):
        time = self.today.strftime('/%m/%Y')
        return ['01'+time, '05'+time]

    def parse_end_of_current_month(self, value, key=None):
        time = self.today.strftime('/%m/%Y')
        return['25'+time, '31'+time]

    def parse_all_curent_month(self, value=None, key=None):
        time = self.today.strftime('%m/%Y')
        return time

    def parse_begin_of_next_month(self, value=None, key=None):
        time = (self.today + relativedelta(months=1)).strftime('/%m/%Y')
        return ['01'+time, '05'+time]

    def parse_end_of_next_month(self, value=None, key=None):
        time = (self.today + relativedelta(months=1)).strftime('/%m/%Y')
        return ['25'+time, '31'+time]

    def parse_all_next_month(self, value=None, key=None):
        time = (self.today + relativedelta(months=1)).strftime('%m/%Y')
        return time

    def parse_begin_of_month_number(self, value, key=None):
        time = '/{}/{}'.format(value, self.current_year)
        return ['01'+time, '05'+time]

    def parse_end_of_month_number(self, value, key=None):
        time = '/{}/{}'.format(value, self.current_year)
        return ['25'+time, '31'+time]
    
    def parse_all_number_month(self, value, key=None):
        time = '{}/{}'.format(value, self.current_year)
        return time

    def parse_begin_of_previous_year(self, value=None, key=None):
        time = (self.today + relativedelta(years=-1)).strftime('/%Y')
        return ['01'+time, '03'+time]

    def parse_end_of_previous_year(self, value=None, key=None):
        time = (self.today + relativedelta(years=-1)).strftime('/%Y')
        return ['10'+time, '12'+time]

    def parse_all_previous_year(self, value=None, key=None):
        time = (self.today + relativedelta(years=-1)).strftime('%Y')
        return time

    def parse_begin_of_current_year(self, value=None, key=None):
        time = self.today.strftime('/%Y')
        return ['01'+time, '03'+time]

    def parse_end_of_current_year(self, value=None, key=None):
        time = self.today.strftime('/%Y')
        return ['10'+time, '12'+time]

    def parse_all_current_year(self, value=None, key=None):
        time = self.current_year
        return time

    def parse_begin_of_next_year(self, value=None, key=None):
        time = (self.today + relativedelta(years=1)).strftime('/%Y')
        return ['01'+time, '03'+time]

    def parse_end_of_next_year(self, value=None, key=None):
        time = (self.today + relativedelta(years=1)).strftime('/%Y')
        return ['10'+time, '12'+time]
    
    def parse_all_next_year(self, value=None, key=None):
        time = (self.today + relativedelta(years=1)).strftime('%Y')
        return time

    def parse_day_month_year(self, value, key=None):
        pattern = [
            "ngày[ ]*(\\d\\d?)[ ]*tháng[ ]*(\\d\\d?)[ ]*năm[ ]*(\\d\\d\\d?\\d?)",
            "ngày[ ]*(\\d\\d?)[ ]*[/-][ ]*(\\d\\d?)[ ]*[/-][ ]*(\\d\\d\\d?\\d?)",
            "(\\d\\d?)[ ]*[/-][ ]*(\\d\\d?)[ ]*[/-][ ]*(\\d\\d\\d?\\d?)"
        ]
        
        time = None
        for item in pattern:
            data = re.findall(item, value)
            if data:
                data = data[0]
                time = "{}/{}/{}".format(data[0], data[1], data[2])

        return time

    def parse_month_year(self, value, key=None):
        pattern = [
            "tháng[ ]*(\\d\\d?)[ ]*năm[ ]*(\\d\\d\\d?\\d?)",
            "tháng[ ]*(\\d\\d?)[ ]*[/-][ ]*(\\d\\d\\d?\\d?)",
            "(\\d\\d?)[ ]*[/-][ ]*(\\d\\d\\d?\\d?)"
        ]

        time = None
        for item in pattern:
            data = re.findall(item, value)
            if data:
                time = "{}/{}".format(data[0][0], data[0][1])

        return time

    def parse_day_month(self, value, key=None):
        pattern = [
            "ngày[ ]*(\\d\\d?)[ ]*tháng[ ]*(\\d\\d?)",
            "ngày[ ]*(\\d\\d?)[ ]*[/-][ ]*(\\d\\d?)",
            "(\\d\\d?)[ ]*[/-][ ]*(\\d\\d?)"
        ]
        
        time = None
        for item in pattern:
            data = re.findall(item, value)
            if data:
                time = "{}/{}".format(data[0][0], data[0][1])  + "/{}".format(self.current_year)

        return time

    def parse_hour_minute_second(self, value, key=None):
        pattern = [
            "(\\d\\d?)[ ]*giờ[ ]*(\\d\\d?)[ ]*phút[ ]*(\\d\\d?)[ ]*giây",
            "(\\d\\d?)[ ]*[hg:][ ]*(\\d\\d?)[ ]*[mp:][ ]*(\\d\\d?)[ ]*[s]?"
        ]
        time = None
        for item in pattern:
            data = re.findall(item, value)
            if data:
                data = data[0]
                time = "{}:{}:{}".format(data[0], data[1], data[2])
        return time

    def parse_hour_minute(self, value, key=None):
        pattern = [
            "(\\d\\d?)[ ]*giờ[ ]*(\\d\\d?)?[ ]*[phút]?",
            "(\\d\\d?)[ ]*[hg:][ ]*(\\d\\d?)?[ ]*[mp]?"
        ]
        time = None
        for item in pattern:
            data = re.findall(item, value)
            if data:
                data = data[0]
                time = "{}:{}".format(data[0], data[1] if data[1] else "00")
                break
        return time

    def parse_day(self, value, key=None):
        return value

    def parse_month(self, value, key=None):
        return value
    
    def parse_year(self, value, key=None):
        return value

    def parse_hour(self, value, key=None):
        pattern = [
            "(\\d\\d?)[ ]*giờ",
            "(\\d\\d?)[ ]*[hg]"
        ]
        time = None
        for item in pattern:
            data = re.findall(item, value)
            if data:
                time = data[0]
                break
        return time
    
    def parse_hour_minute_today(self, value, key=None):
        time = self.parse_hour_minute(value)
        day = self.today.strftime('%d/%m/%Y')

        if time and day:
            return time + " " + day

    def parse_time_period_number_previous_day(self, value, key):
        time_period = self.parse_time_period(value[0])
        day = self.parse_number_previous_day(value[1])
        
        handled_time = [time_period[0] + " " + day, time_period[1] + " " + day] if time_period and day else None
        return handled_time
    
    def parse_time_period_previous_day(self, value, key):
        time_period = self.parse_time_period(value[0])
        day = self.parse_previous_day(value[1])
        
        handled_time = [time_period[0] + " " + day, time_period[1] + " " + day]
        return handled_time

    def parse_time_period_today(self, value, key=None):
        time_period = self.parse_time_period(value[0])
        day = self.parse_today()

        handled_time = [time_period[0] + " " + day, time_period[1] + " " + day]
        return handled_time

    def parse_time_period_the_next_day(self, value, key):
        time_period = self.parse_time_period(value[0])
        day = self.parse_the_next_day("the_next_day", value[1])
        
        handled_time = [time_period[0] + " " + day, time_period[1] + " " + day]
        return handled_time

    def parse_time_period_double_next_day(self, value, key=None):
        time_period = self.parse_time_period(value[0])
        day = self.parse_double_next_day()
        
        handled_time = [time_period[0] + " " + day, time_period[1] + " " + day]
        return handled_time
        
    def parse_time_period_triple_next_day(self, value, key=None):
        time_period = self.parse_time_period(value[0])
        day = self.parse_triple_next_day()
        
        handled_time = [time_period[0] + " " + day, time_period[1] + " " + day]
        return handled_time

    def parse_time_period_number_next_day(self, value, key=None):
        time_period = self.parse_time_period(value[0])
        day = self.parse_number_next_day(value[1])
        
        handled_time = [time_period[0] + " " + day, time_period[1] + " " + day] if time_period and day else None
        return handled_time

    def parse_time_period_day_month_year(self, value, key=None):
        time_period = self.parse_time_period(value[0])
        day = self.parse_day_month_year(value[1])
        
        handled_time = [time_period[0] + " " + day, time_period[1] + " " + day] if time_period and day else None
        return handled_time

    def parse_time_period_day_month(self, value, key=None):
        time_period = self.parse_time_period(value[0])
        day = self.parse_day_month(value[1])

        handled_time = [time_period[0] + " " + day, time_period[1] + " " + day] if time_period and day else None
        return handled_time

    def parse_time_period_day(self, value, key=None):
        time_period = self.parse_time_period(value[0])
        day = self.parse_day(value[1]) + "/{}/{}".format(self.current_month, self.current_year)

        handled_time = [time_period[0] + " " + day, time_period[1] + " " + day] if time_period and day else None
        return handled_time

    def parse_hour_minute_day_month_year(self, value, key=None):
        time = self.parse_hour_minute(value[0])
        day = self.parse_day_month_year(value[1])

        handled_time = (time + " " + day) if time and day else None
        return handled_time

    def parse_hour_minute_day_month(self, value, key):
        time = self.parse_hour_minute(value[0])
        day = self.parse_day_month(value[1])

        handled_time = (time + " " + day) if time and day else None
        return handled_time

    def parse_hour_minute_day(self, value, key):
        time = self.parse_hour_minute(value[0])
        day = self.parse_day(value[1]) + "/{}/{}".format(self.current_month, self.current_year)

        handled_time = (time + " " + day) if time and day else None
        return handled_time

    def parse_begin_of_month_number_year(self, value=None, key=None):
        time = self.parse_month_year(value)
        return ['01/'+time, '05/'+time]
