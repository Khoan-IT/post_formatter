import datetime
from dateutil import relativedelta


class TimeParser:
    def parse(self, text):
        time_parts = text.split()
        if len(time_parts) > 2:
            return
        
        dmy_parts = time_parts[-1].split('/')
        if len(dmy_parts) == 1:
            dmy_parts = time_parts[-1].split('-')

        dmy_parts.reverse()
        hms_parts = []
        if len(time_parts) > 1:
            if len(dmy_parts) < 3:
                return
            
            hms_parts = time_parts[0].split(':')

        hms_parts
        time_list = []
        for i in range(3):
            if i < len(dmy_parts):
                time_list.append(int(dmy_parts[i]))
                least_unit = i
            else:
                time_list.append(1)

        for i in range(3):
            if i < len(hms_parts):
                time_list.append(int(hms_parts[i]))
                least_unit = 3 + i
            else: 
                time_list.append(0)

        next_time_list = [0 for i in range(6)]
        next_time_list[least_unit] += 1

        try:
            cur_time = datetime.datetime(time_list[0], time_list[1], time_list[2], time_list[3], time_list[4], time_list[5])
            next_time = cur_time + relativedelta.relativedelta(
                years=next_time_list[0], months=next_time_list[1], days=next_time_list[2],
                hours=next_time_list[3], minutes=next_time_list[4], seconds=next_time_list[5]
            )

            return [cur_time, next_time]

        except:
            return None
        
    def to_string(self, datetime_obj):
        return datetime_obj.strftime('%H:%M:%S %d-%m-%Y')
        

class BenefitParser:
    def parse(self, text):
        words = text.split()
        res = []
        for word in words:
            if word.replace('.','',1).isdigit():
                res.append(float(word))

        return res