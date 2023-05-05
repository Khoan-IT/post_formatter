from typing import List
import re
import nltk
import json
import string
import underthesea
from pyvi import ViTokenizer

class V2PostNormalizer:
    def __init__(self):
        file = open('model/short_words.json')
        v2_short_words = json.load(file)
        self.__v2_short_words = v2_short_words

    # Functions in version 2.

    # Function normalize version 2.
    def v2_normalize(self, post: str) -> List[str]:
        sentences = self.v2_split_sentences(post)
        res = []
        for sentence in sentences:
            sentence = self.v2_remove_special_characters(sentence)
            sentence = self.v2_remove_emoji(sentence)
            sentence = self.v2_remove_punctuations(sentence)
            sentence = self.v2_replace_short_words(sentence)
            sentence = self.v2_get_lower_case(sentence)
            sentence = self.v2_strip(sentence)
            sentence = self.v2_tokenize(sentence)
            sentence = self.v2_remove_punctuations(sentence)
            if len(sentence) > 0:
                res.append(sentence)

        return res

    def v2_split_sentences(self, post: str) -> List[str]:
        res = []
        sentences = nltk.sent_tokenize(post)
        for sentence in sentences:
            sentence = sentence.replace('\n', ' ')
            # sents = sentence.split('\n')
            # for sent in sents:
            if len(sentence) > 0:
                res.append(sentence)

        return res

    def v2_get_lower_case(self, sentence: str) -> str:
        res = ''
        non_lower_case_characters = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b|(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+'
        words = sentence.split(' ')
        for word in words:
            if not re.match(non_lower_case_characters, word):
                word = word.lower()

            res += word + ' '

        return res

    def v2_remove_emoji(self, sentence: str) -> str:
        emoji = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002500-\U00002BEF"  # chinese char
                           u"\U00002702-\U000027B0"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  # dingbats
                           u"\u3030"
                           u"\u23F0"  # time icon
                           u"\u2022"  # •
                           u"\u201C"  # “
                           "]+", re.UNICODE)

        return re.sub(emoji, '', sentence)

    def v2_remove_special_characters(self, sentence) -> str:
        special_character = re.compile(
            '(#.+|(:\)+)|(:D+)|(:\(+)|(:\'\(+)|(:P+)|(O:\))|(3:\))|(o.O+)|(;\)+)|(:\/ )|(>:O)|(:O+)|(-_+-)|(:\*)|(^_+^)|(8-\)+)|(8\|+)|(>:\(+)|(:v+)|(:3+)|(\(y\))|(<\(\"\))|(\(^^^\))|(==+)|(:\|\])|(:poop:)|(:putnam:)|(<3+))')
        return re.sub(special_character, '', sentence)

    def v2_remove_punctuations(self, sentence: str) -> str:
        split_sentence = ' '.join(re.findall(
            r'#.+|\d{1,4}[/.:]\d{1,4}[/.:]?\d{0,4}|\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b|[\w]+&[\w]+|(?:https?://|]{0,1})(?:[-\w./]|(?:%[\da-fA-F]{2}))+[\w/]{1}|#[.]+|\w+|[^\s\w]', sentence))
        for punctuation in string.punctuation:
            if punctuation in [':', ',', '.']:
                continue
            while len(split_sentence) != len(split_sentence.replace(' '+punctuation+' ', ' ')):
                split_sentence = split_sentence.replace(
                    ' '+punctuation+' ', ' ')
            if len(split_sentence) < 2:
                if len(split_sentence) == 1 and split_sentence[0] == punctuation:
                    split_sentence = ''    
                continue
            if split_sentence[0] == punctuation and split_sentence[1] == ' ':
                split_sentence = split_sentence[1:]
            if split_sentence[-1] == punctuation and split_sentence[-2] == ' ':
                split_sentence = split_sentence[:-1]

        return split_sentence

    def v2_strip(self, sentence: str) -> str:
        return sentence.strip()

    def v2_replace_short_words(self, sentence: str) -> str:
        words = sentence.split(' ')
        replace_words = ''
        for word in words:
            if word in self.__v2_short_words.keys():
                replace_words += self.__v2_short_words[word] + ' '
                continue

            replace_words += word + ' '

        if len(replace_words) > 0:
            replace_words = replace_words[:-1]

        return replace_words

    def v2_tokenize(self, sentence) -> str:
        return underthesea.word_tokenize(sentence, format='text')