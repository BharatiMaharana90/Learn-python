'''
FLAME test: Analyze your future relationship
https://www.wikihow.com/Play-%22Flame%22
'''
import sys, os, re

try:
 her = sys.argv[1]
 his = sys.argv[2]
except IndexError:
 print >> sys.stderr, "python %s her_name his_name" %sys.argv[0]
 exit(1)

her_l = set(her.rstrip().lower())
his_l = set(his.rstrip().lower())

rem=list(her_l ^ his_l)
# FLAME
test=list('0FLAME')
result={
 'F':'have Friendship',
 'L':'are in Love',
 'A':' have Affection',
 'M':'will have Marriage',
 'E':'are Enemies'
}
#print rem
if len(rem)%5==0:
 print "%s and %s %s \n\n"%(her,his,result[test[5]])
else:
 print "%s and %s %s \n\n"%(her,his,result[test[(len(rem)-5)]])
print 



