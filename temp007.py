import csv
from func_rating import rating
from func_label import label
filename="imdb_no_comment.csv"
csvfile=open(filename,'r')
csvreader = csv.reader(csvfile)
for row2 in csvreader:
    row=str(row2)
    l=row.split()
    for word in l:
        if (word=='education' or word=='study'): 
            with open('education.txt','a+') as f:
                f.write(row +"\t")
                g=rating(row)
                f.write(str(g)+"\t")
                f.write(label(g)+"\n")
        if (word=='actor' or word=='actress' or word=='action'):
            with open('actor.txt','a+') as f:
                f.write(row +"\t")
                g=rating(row)
                f.write(str(g)+"\t")
                f.write(label(g)+"\n")
        if (word=='story' or word=='screenplay' or word=='drama'):
            with open('story.txt','a+') as f:
                f.write(row +"\t")
                g=rating(row)
                f.write(str(g)+"\t")
                f.write(label(g)+"\n")
        if (word=='director' or word=='direction'):
            with open('director.txt','a+') as f:
                f.write(row +"\t")
                g=rating(row)
                f.write(str(g)+"\t")
                f.write(label(g)+"\n")
        if (word=='music' or word=='song'):
            with open('music.txt','a+') as f:
                f.write(row +"\t")
                g=rating(row)
                f.write(str(g)+"\t")
                f.write(label(g)+"\n")
        if (word=='stunt' or word=='action' or word=='stunt'):
            with open('stunt.txt','a+') as f:
                f.write(row +"\t")
                g=rating(row)
                f.write(str(g)+"\t")
                f.write(label(g)+"\n")
    
