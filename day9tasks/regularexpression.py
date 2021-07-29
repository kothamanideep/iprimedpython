import re
textinput=input("enter a text:")
val1=re.search("^the",textinput)
val=re.search("hello$",textinput)
if val:
    print("accepted")
else:
    print("rejected")