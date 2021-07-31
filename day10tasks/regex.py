# ^hello"   matches any string that start with hello
#"hello$"   matches any string that end with hello
# "^hello$"  matches any string that starts and end with hello
# "hello"    matches any string that contains hello
# {}         to specify range
#  ()         for group
import re
var="ab"
regex=re.search("a?b+$",var)
# v=re.search("hello*",var)
# v1=re.search("hello+",var)
# v2=re.search("hello?",var)
print(regex)
