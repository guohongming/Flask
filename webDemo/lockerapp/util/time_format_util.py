__author__ = 'Guo'

def time_to_chinese(source):
    return source.strftime('%Y{y}%m{m}%d{d}  %H:%M:%S').format(y='年', m='月', d='日')