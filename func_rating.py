import re
def rating(comment):
    words=comment.split()
    rate=0
    count=1
    for w in words:
        if (w.find('worst')!=-1):
            count+=1
            if(re.match('(.*not.*worst)',w)):
                rate=rate+4
            else:
                rate=rate-10
        if (w.find('worse')!=-1):
            count+=1
            if(re.match('(.*not.*worse)',w)):
                rate=rate+4
            else:
                rate=rate-7
        if (w.find('awful')!=-1):
            count+=1
            if(re.match('(.*not.*awful)',w)):
                rate=rate+6
            else:
                rate=rate-9
        if (w.find('terrible')!=-1):
            count+=1
            if(re.match('(.*not.*terrible)',w)):
                rate=rate+5
            else:
                rate=rate-8
        if (w.find('bad')!=-1):
            count+=1
            if(re.match('(.*not.*bad)',w)):
                rate=rate+5
            else:
                rate=rate-5
        if (w.find('cool')!=-1):
            count+=1
            if(re.match('(.*not.*cool)',w)):
                rate=rate-4
            else:
                rate=rate+3
        if (w.find('good')!=-1):
            count+=1
            if(re.match('(.*not.*good)',w)):
                rate=rate-5
            else:
                rate=rate+5
        if (w.find('creative')!=-1):
            count+=1
            if(re.match('(.*not.*creative)',w)):
                rate=rate-7
            else:
                rate=rate+8
        if (w.find('amazing')!=-1):
            count+=1
            if(re.match('(.*not.*amazing)',w)):
                rate=rate-3
            else:
                rate=rate+10
        if (w.find('fascinating')!=-1):
            count+=1
            if(re.match('(.*not.*fascinating)',w)):
                rate=rate-4
            else:
                rate=rate+8
        if (w.find('artful')!=-1):
            count+=1
            if(re.match('(.*not.*artful)',w)):
                rate=rate-6
            else:
                rate=rate+9
        if (w.find('great')!=-1):
            count+=1
            if(re.match('(.*not.*great)',w)):
                rate=rate-5
            else:
                rate=rate+10
        if (w.find('fabulous')!=-1):
            count+=1
            if(re.match('(.*not.*fabulous)',w)):
                rate=rate-4
            else:
                rate=rate+10
        if (w.find('impressive')!=-1):
            count+=1
            if(re.match('(.*not.*impressive)',w)):
                rate=rate-4
            else:
                rate=rate+10
    rate=rate/count
    return rate
