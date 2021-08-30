import string
import re
reg = "[\s_\W]"; #\s đại diện cho kí tự space, \W đại diện cho những kí tự lạ, không phải alphanumeric
def alphanumeric(password):
    if(len(password) == 1): return False
    if(re.search(reg, password)):
        return False
    return True

# Day 1

    

    