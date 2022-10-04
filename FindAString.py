string = "ABCDCDC"
sub_string = "CDC"


count = 0
ret = 0
while count <= len(string):
    index = string.find(sub_string, count)
    if index != -1:
        ret += 1
        count = index
    count += 1

print(ret)
