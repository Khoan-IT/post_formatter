import json
import pickle
import re
import copy


MAPPING_ABBERIVATIONS = [('mhx', 'mùa hè xanh'), ('đhqg', 'đại học quốc gia'), ('hcm', 'hồ chí minh'), 
                         ('ctv', 'cộng tác viên'), ('ctxh', 'công tác xã hội'), ('drl', 'điểm rèn luyện'), 
                         (' sv ', 'sinh viên'), ('kh&kt', 'khoa học và kỹ thuật'), ('ctđt', 'chương trình đào tạo'), 
                         ('nvqs', 'nghĩa vụ quân sự'), ('tnv', 'tình nguyện viên'), (' ktx ', 'ký túc xá'),
                         (' bk ', 'bách khoa'), (' cs ', 'cơ sở'), (' vp ', 'văn phòng'), (' mt ', 'máy tính'),
                         ('hcm', 'hồ chí minh'), ('&', 'và'), (' tn ', 'thanh niên'),(' sv ', 'sinh viên'), 
                         ('btc', 'ban tổ chức'), (' kh ', 'khoa học'), (' kt ', 'kỹ thuật'),
                         ('tp', 'thành phố'), ('tsv', 'tân sinh viên'), ('đh', 'đại học'),
                         ('tdtt', 'thể dục thể thao'), ('cs1', 'cơ sở 1'), ('cs2', 'cơ sở 2'),
                         ('ktmt', 'kỹ thuật máy tính'),
                        ]

ABBERIVATIONS, MEANING_ABBERIVATIONS = list(zip(*MAPPING_ABBERIVATIONS)) 


def contains_number(string):
    return any(char.isdigit() for char in string)

def _academicyear(m):
    return m.group(0).replace('k', ' khoá ')

def _year(m):
    return m.group(0).replace(' ', '-')

def _room(m):
    return m.group(0).replace('p', ' phòng ')

def _ward(m):
    return m.group(0).replace('p', ' phường ')

def _district(m):
    return m.group(0).replace('q.', ' quận ').replace('q', ' quận ')

def _city(m):
    return m.group(0).replace(' tp.', ' thành phố ').replace(' t.p', ' thành phố ').replace(' tx.', ' thị xã ').replace(' tt.', ' thị trấn ')

def regex(input):
    input = re.sub(re.compile(r'(^|\s)([p]\.?\s?[0-9]{3})'), _room, ' ' + input)  # P. 114 -> phòng 114
    # input = re.sub(re.compile(r'([0-9]+)\s([0-9]+)'), _year, ' ' + input)   # 2022 2023 -> 2022-2023
    input = re.sub(re.compile(r'(^|\s)(tp\.|t\.p\s|tp\.\s|tt\.|tx\.|tt\.\s|tx\.\s)[đâơôa-z]'), _city, ' '+ input)   # tp -> thành phố
    input = re.sub(re.compile(r'(^|\s)((p\s?[0-9]{1,2})|(p\.\s*([0-9]{1,2}|[a-zđ]{1,})))'), _ward, ' ' + input)
    input = re.sub(re.compile(r'(^|\s)((q\s?[0-9]{1,2})|(q\.\s*([0-9]{1,2}|[a-zđ]{1,})))'), _district, ' ' + input)
    input = re.sub(re.compile(r'(^|\s)(k[0-9]{2,4})'), _academicyear, ' ' + input)  # k18 -> khoá 18
    return input
    

def normalizer(string):
    string = string.replace('_', ' ').lower()
    for index, abb in enumerate(ABBERIVATIONS):
        string = string.replace(abb, " " + MEANING_ABBERIVATIONS[index] + " ")
    string = string.replace('.', '')    # Replace dot Ex: Q. 10, P. 14
    string = " ".join(string.split())
    string = " ".join(regex(string).split())
    
    return string