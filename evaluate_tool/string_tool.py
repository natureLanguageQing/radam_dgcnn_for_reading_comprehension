# coding:utf8

import re
import sys

from six import unichr

blank_regexp = re.compile(r'\s+')
punctuation = set()

main_path = '/'.join(sys.argv[0].split('/')[:-1])
if main_path:
    main_path += '/'

with open(main_path + "punctuation", "r") as file:
    for line in file:
        punctuation.add(line.strip())


def drop_punctuation(string, codec="utf8"):
    # print(string)
    """删除所有标点符号"""
    if not isinstance(string, str):
        ustring = string.decode(codec)
    else:
        ustring = string
    rstring = ""
    for uchar in ustring:
        if uchar not in punctuation:
            rstring += uchar
        else:
            rstring += " "
    return rstring.encode(codec, 'ignore')


def drop_punctuation_two(string: str, codec="utf8"):
    """删除所有标点符号"""
    rstring = ""
    for uchar in string:
        if uchar not in punctuation:
            rstring += str(uchar)
        else:
            rstring += " "
    return rstring.encode(codec, 'ignore')


def split_string(string, codec="utf8"):
    split_tokens = []
    # ustring = string.decode(codec, "ignore")
    for uchar in string:
        split_tokens.append(uchar.encode(codec, "ignore"))
    return split_tokens


def strQ2B(string, codec="utf8"):
    """全角转半角"""
    rstring = ""
    for uchar in string:
        if isinstance(uchar, str):
            inside_code = ord(uchar)
            if inside_code == 12288:  # 全角空格直接转换
                inside_code = 32
            elif 65281 <= inside_code <= 65374:  # 全角字符（除空格）根据关系转化
                inside_code -= 65248

            rstring += unichr(inside_code)
        return rstring.encode(codec, "ignore")
    else:
        return string


def strB2Q(string, codec="utf8"):
    """半角转全角"""
    ustring = string.decode(codec, "ignore")
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 32:  # 半角空格直接转化
            inside_code = 12288
        elif 32 <= inside_code <= 126:  # 半角字符（除空格）根据关系转化
            inside_code += 65248

        rstring += unichr(inside_code)
    return rstring


def filter_blank(string):
    string = string.decode("utf-8")
    return blank_regexp.sub('', string)


def filter_extra_blank(string):
    string = string.decode("utf-8")
    return blank_regexp.sub(' ', string)
# 不能在类字节码对象上使用字符串模式
