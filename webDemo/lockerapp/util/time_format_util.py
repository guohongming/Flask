__author__ = 'Guo'

def time_to_chinese(source):
    return source.strftime("%Y{y}-%m{m}-%d{d} %H{h}:%M{m}:%S{s}").format(y='年', m='月', d='日',h = '时',m='分',s='秒')