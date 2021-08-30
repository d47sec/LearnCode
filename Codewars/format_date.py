def format_duration(seconds):
    if(seconds == 0): return 'now'
    minutes, hours, days, years = 0, 0, 0, 0
    unit, value = [], []
    s, m, h, d, y, res = " second", " minute", " hour", " day", " year", ""
    while(seconds >= 60): minutes += 1; seconds -= 60
    while(minutes >= 60): hours += 1; minutes -= 60
    while(hours >= 24): days += 1; hours -= 24
    while(days >= 365): years += 1; days -= 365

    if(years > 0):
        if(years > 1):
            y += "s"
            unit.append(y)
            value.append(years)
        else:
            unit.append(y)
            value.append(years)
    
    if(days > 0):
        if(days > 1):
            d += "s"
            unit.append(d)
            value.append(days)
        else:
            unit.append(d)
            value.append(days)
    if(hours > 0):
        if(hours > 1):
            h += "s"
            unit.append(h)
            value.append(hours)
        else:
            unit.append(h)
            value.append(hours)
    if(minutes > 0):
        if(minutes > 1):
            m += "s"
            unit.append(m)
            value.append(minutes)
        else:
            unit.append(m)
            value.append(minutes)
    if(seconds > 0):
        if(seconds > 1):
            s += "s"
            unit.append(s)
            value.append(seconds)
        else:
            unit.append(s)
            value.append(seconds)
            
    
    i = len(unit) - 1
    while(i >= 0):
        res = str(value[i]) + unit[i] + res
        if(i == len(unit) - 1  and len(unit) > 1):
            res = ' and ' + res
        if(i < len(unit) - 1  and i > 0):
            res = ', ' + res
        i -= 1
    return res
    
     

# link: https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python/6098896fc0e2d4003d765740

# BEST PRACTICES

def format_duration(seconds):
    times = [("year", 60 * 60 * 365), ("day", 60 * 60 * 24), ("hour", 60 * 60), ("minute", 60), ("second", 1)]

    res = []
    if(seconds == 0): return "now"
    for name, sec in times:
        temp = seconds // sec
        if(temp):
            if(temp > 1):
                name += "s"
            res.append(str(temp) + " " +name)
        seconds = seconds % sec
    return ", ".join(res[:-1]) + ' and ' + res[-1] if(len(res) > 1) else res[0]

print(format_duration(3662))
