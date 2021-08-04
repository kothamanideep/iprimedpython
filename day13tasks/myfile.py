import csv
headercontent=["Name","Roll"]
StudentData=[{"Name":"mani","Roll":10},
{"Name":"arif","Roll":11},
{"Name":"guru","Roll":12},
{"Name":"venky","Roll":13}]

with open('student.csv','w+',encoding="UTF8",newline='') as s:
    writer=csv.DictWriter(s,fieldnames=headercontent)
    writer.writeheader()
    writer.writerows(StudentData)