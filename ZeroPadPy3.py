# encoding: utf8
# 零宽字符插入头部
import codecs
from typing import Union


def HideText(ClearText:Union[bytes,str], HidenInfo:Union[bytes,str])->str:
    # add header
    if isinstance(HidenInfo, str):
        HidenInfo = bytes(HidenInfo, encoding='utf-8')
    if isinstance(ClearText,bytes):
        ClearText = str(ClearText, encoding='utf-8')

    ZeroPad = ['e2808b', 'e2808c']  # 0, 1
    BinHidenInfo = ''.join(list(map(lambda x: codecs.decode(ZeroPad[x == '1'],'hex').decode('utf-8'), bin(int(codecs.encode(HidenInfo, 'hex'), 16)))))
    return  BinHidenInfo+ClearText


def ShowHidenText(HidenText:Union[str,bytes])->str:
    if isinstance(HidenText,str):
        HidenText = bytes(HidenText, encoding='utf-8')

    # str to hex
    a = codecs.encode(HidenText, 'hex').decode(encoding='utf-8')
    _i1 = a.rindex('e2808b')
    _i2 = a.rindex('e2808c')
    _max_index = max(_i1, _i2) + 6

    _binary_string = a[:_max_index].replace('e2808b', '0').replace('e2808c', '1')
    b = codecs.decode('%x' % int(_binary_string, 2), 'hex').decode('utf-8')
    return b



ClearText = "Tr0y ask for your help!!"
HidenInfo = "SOS"

HidenText = HideText(ClearText, HidenInfo)
print(HidenText)
ClearText = ShowHidenText(HidenText)
print(ClearText)
