spacelist = [1,3,2,6,8]
listlength = len(spacelist)
for item in spacelist:
    print(item)
print(listlength)
spacelist.sort()
spacelist.append("star")
print(spacelist)
print()
if 'star' in spacelist:
    print("yes, star in spacelist",spacelist)
print()
spacelist[3] = 'space suite'
print(spacelist)
print()
del spacelist[2]
print(spacelist)
print()
print("value poped is ",spacelist.pop(3))
print(spacelist)
print()
newlist = spacelist.copy()
print("new list is, ",newlist)
print()
thirdspacelist = spacelist + newlist
print(thirdspacelist)
