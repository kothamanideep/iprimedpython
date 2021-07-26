#list of objects


class students:
    def __init__(self,name,rollno,adminno):
        self.myname=name
        self.myrollno=rollno
        self.myadminno=adminno

obj=[]
obj.append(students("mani",11,3440))
obj.append(students("guru",12,3441))
obj.append(students("venky",13,3442))
print(obj[0].myname)
print(obj[0].myrollno)
print(obj[0].myadminno)


