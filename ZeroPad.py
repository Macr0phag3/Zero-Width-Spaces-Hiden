#encoding: utf8
import re

def HideText(ClearText, HidenInfo):
    assert (len(ClearText) > 1)
    print 'ClearText:', ClearText
    print 'Hiden:', HidenInfo    
    ZeroPad = ['e2808b', 'e2808c'] # 0, 1
    BinHidenInfo = map(lambda x: ZeroPad[x == '1'], bin(int(HidenInfo.encode('hex'), 16))[2:])
    #print BinHidenInfo
    
    RawInfoSplit = re.findall('.', ClearText)
    
    length = min(len(RawInfoSplit) - 1, len(BinHidenInfo))
    Hiden = zip(RawInfoSplit[:length], BinHidenInfo[:length]) 
    HidenText = ''.join([c[0]+c[1].decode('hex') for c in Hiden]) + ''.join(BinHidenInfo[length:]).decode('hex') + ClearText[length:]
    print 'AfterHiden:', HidenText    
    return HidenText

def ShowHidenText(HidenText):
    print 'HidenText:', HidenText
    ClearText = ('%x' %int(''.join(re.sub('[\x00-\x7F]', '', HidenText)).encode('hex').replace('e2808b', '0').replace('e2808c', '1'), 2)).decode('hex')
    print 'HidenText:', ClearText
    return ClearText
    

ClearText = "Tr0y ask for your help!!"
HidenInfo = "SOS"

HidenText = HideText(ClearText, HidenInfo)
print '-'*50
ClearText = ShowHidenText(HidenText)








