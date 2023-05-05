import json
import sys
import re
import copy

from datetime import datetime
from typing import List, Union, Tuple

sys.path.append('./result/parser')
from time_parser import TimeParser
from time_pattern import composed_pattern
sys.path.append('./result/normalizer')
from sentence_normalizer import normalizer

class TimeofPostParser(TimeParser):
    def __init__(self):
        super().__init__()
    
    def parse_hour_minute_today(self, value, key=None):
        time = self.parse_hour_minute(value)
        if time:
            return time
        
    def time_parser(self, raw_time):
        for key, pattern in composed_pattern.items():
            value = re.findall(pattern, raw_time)
            if value:
                result = getattr(TimeofPostParser, "parse_" + key)(self, value[0], key)

                return result
                       
class PostFormatter:
    def __init__(self) -> None:
        self.__time_parser = TimeofPostParser()
        self.__formatted_time_pattern = [
            "[\\d]{2}[ ]*[:][ ]*[\\d]{2}[ ]*[:][ ]*[\\d]{2}[ ]*[\\d]{2}[ ]*[-][ ]*[\\d]{2}[ ]*[-][ ]*[\\d]{4}",
            "[\\d]{2}[ ]*[:][ ]*[\\d]{2}[ ]*[:][ ]*[\\d]{2}[ ]*[\\d]{2}[ ]*[-][ ]*[\\d]{4}",
            "[\\d]{2}[ ]*[-][ ]*[\\d]{2}[ ]*[-][ ]*[\\d]{4}",
            "[\\d]{2}[ ]*[-][ ]*[\\d]{4}",
            "[\\d]{4}"
        ]
        self.__key_multiple_value = ['number', 'requirement', 'job_description', 'benefit:others']
        self.__key_benefit = ['benefit:ctxh', 'benefit:drl']
    
    def __get_hour_date(self, time_value: str) -> Tuple[List[str], List[str]]:
        res_hour = []
        res_date = []
        parts_of_time = time_value.split(',')
        for part in parts_of_time:
            res_parts = self.__time_parser.time_parser(part)
            if res_parts:
                res_parts = res_parts.split()
                for res_part in res_parts:
                    if ':' in res_part:
                        if len(res_part.split(':')) == 2:
                            res_part += ':00'
                        parts_of_hour = list(map(int, res_part.split(':')))
                        res_part = "{:02d}:{:02d}:{:02d}".format(*parts_of_hour)
                        if res_part not in res_hour:
                            res_hour.append(res_part)
                    else:
                        if res_part not in res_date and '/' in res_part:
                            parts_of_date = list(map(int, res_part.split('/')))
                            if len(parts_of_date) == 2:
                                res_part = "{:02}-{:04}".format(*parts_of_date)
                            else:
                                res_part = "{:02}-{:02}-{:04}".format(*parts_of_date)
                            res_date.append(res_part)
                    
        return res_hour, res_date

    def __get_time(self, time_start: str, time_end: str) -> List[List[str]]:
        res_time = []
        hours_time_start, date_time_start = self.__get_hour_date(time_start)
        hours_time_end, date_time_end = self.__get_hour_date(time_end)
        
        def get_time_end(hours_time_end, date_time_end, date_time_start):
            if len(hours_time_end) == 1 and len(date_time_end) == 1:
                time_end = hours_time_end[0] + ' ' + date_time_end[0]
            elif len(hours_time_end) == 1 and len(date_time_end) == 0:
                time_end = hours_time_end[0] + ' ' + date_time_start[0]
            elif len(hours_time_end) == 0 and len(date_time_end) == 1:
                time_end = date_time_end[0]
            else:
                time_end = ''
            return time_end
            
        # case: 1 hours - 1 date
        if len(hours_time_start) == 1 and len(date_time_start) == 1:
            time_start = hours_time_start[0] + ' ' + date_time_start[0]
            time_end = get_time_end(hours_time_end, date_time_end, date_time_start)
            res_time.append([time_start, time_end])
            
        # case: 2 hours - 1 date (Multiple shift per day)
        elif len(hours_time_start) >= 2:
            if len(date_time_start) == 1:
                if len(hours_time_end) == len(hours_time_end) and len(date_time_end) == 0:
                    for i, v in enumerate(hours_time_start):
                        start = v + ' ' + date_time_start[0]
                        end = hours_time_end[i] + ' ' + date_time_start[0]
                        res_time.append([start, end])
                        
        # case: have date only
        elif len(hours_time_start) == 0 and len(date_time_start) == 1:
            time_start = date_time_start[0]
            time_end = get_time_end(hours_time_end, date_time_end, date_time_start)
            res_time.append([time_start, time_end])
            
        return res_time

    def __get_ctxh_drl(self, benefit_value: str) -> List[float]:
        res_benefit = []
        parts_of_benefit = benefit_value.split(',')
        for part in parts_of_benefit:
            values = part.split()
            # case "0,5-1" -> "0 5 1"
            if len(values) == 3:
                values.pop(0)
                values[0] = '0.' + values[0]
            for value in values:
                res = float(value)
                if res not in res_benefit:
                    res_benefit.append(res)

        return res_benefit

    def __check_time_format(self, time: str) -> bool:
        for pattern in self.__formatted_time_pattern:
            pattern = re.compile(pattern)
            if pattern.match(time):
                return True
        return False
        
    def get_activities(self, posts: List[Dict[str, str]]) -> List[Dict[str, str]]:
        activity_result = []
        for post in posts:
                res_post = {}
                res_post['post_id'] = post['id']
                res_post['activity'] = {}

                time_start = post['activity'].get('time:start', '')
                time_end = post['activity'].get('time:end', '')
                res_time = self.__get_time(time_start, time_end)
                
                for k, v in post['activity'].items():
                    if k != 'time:start' and k != 'time:end':
                        if k in self.__key_multiple_value:
                            res_post['activity'][k] = list(map(lambda x: normalizer(x).strip(), v.split(',')))
                        elif k in self.__key_benefit:
                            res_post['activity'][k] = self.__get_ctxh_drl(v)
                        elif 'time' in k:
                            time_hours, time_date = self.__get_hour_date(v)
                            if time_date:
                                if self.__check_time_format(time_date[0]):
                                    res_post['activity'][k] = time_date[0]
                        else:
                            value = max(v.split(','), key=len).strip()
                            value = normalizer(value) if k != 'register:way' else value.replace('_', ' ')
                            if k == 'name':
                                res_post['activity'][k] = value
                            else:
                                res_post['activity'][k] = [value]
                                
                number_of_shifts = len(res_time)
                for index in range(number_of_shifts):
                    temp_post = copy.deepcopy(res_post)
                    
                    if number_of_shifts >= 2:
                        temp_post['activity']['name'] = "{} ca {}".format(temp_post['activity']['name'], index + 1)
                        
                    time = res_time[index]
                    if time[0]:
                        if self.__check_time_format(time[0]):
                            temp_post['activity']['time:start'] = time[0]
                    if time[1]:
                        if self.__check_time_format(time[1]):
                            temp_post['activity']['time:end'] = time[1]
                            
                    activity_result.append(temp_post)
        
        return activity_result
        
if __name__ == '__main__':
    with open('./slot_result/time.json', 'w', encoding='utf-8') as f_write:
        json_file = open('./slot_result/result_orig_gpt.json', 'r')
        posts = json.load(json_file)
        post_formatter = PostFormatter()
        activity_result = post_formatter.get_activities(posts)
        json.dump(activity_result, f_write, ensure_ascii=False)
            # break
    # print(time_parser.time_parser("16g00 10/3/2023"))
    