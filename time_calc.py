def to_min(h, m):
    return h*60+m

def to_hhmm(m):
    minus = False
    if m < 0:
        minus = True
        m = m * -1
    min = m%60
    hour = m//60
    if minus:
        return hour*-1, min*-1
    else:
        return hour, min
