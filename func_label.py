def label(rate):
    percent=rate*10
    if(percent>70):
        s='very good'
    elif(percent>30):
        s='good'
    elif(percent>20):
        s='neutral'
    elif(percent>10):
        s='bad'
    else:
        s='very bad'
    return s
