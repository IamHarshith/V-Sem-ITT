import re
a = re.compile(r"\d{4}\s{1}\w?",re.I)
n = "1234 g1234 h"
if a.search(n):
    print "res"
