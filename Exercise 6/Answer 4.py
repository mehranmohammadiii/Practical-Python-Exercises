from operator import contains
str1 = """
Today, Richard Rael and Tony Riggs tell the story of American astronomer edwin hubble.
He changed our ideas about the universe and how it developed.

Edwin hubble made his most important discoveries in the nineteen twenties. Today, other
astronomers continue the work he began. Many of them are using the Hubble space
telescope that is named after him.

Edwin Hubble was born in eighteen eighty-nine in Marshfield, Missouri. He spent his early
years in the state of Kentucky. Then he moved with his family to Chicago, Illinois. He
attended the University of Chicago. He studied mathematics and astronomy.
"""
strlist=str1.split(".")
for item in strlist :
    if contains(item,'edwin hubble') :
        print(item)
        strlist[strlist.index(item)]=item.replace('edwin hubble' , 'Edwin Hubble')
    elif contains(item,"edwin Hubble") :
        print(item)
        strlist[strlist.index(item)]=item.replace('edwin Hubble' , 'Edwin Hubble')
    elif contains(item,"Edwin hubble") :
        print(item)
        strlist[strlist.index(item)]=item.replace('Edwin hubble' , 'Edwin Hubble')
    elif contains(item,"Edwin Hubble") :
        print(item)
print()
print(''.join(strlist))

