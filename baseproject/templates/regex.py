import re
pattern ="python"
string_find = "hello python  how are you"
print("Re match....")
if re.match(pattern,string_find):
    print("{} found in {}".format(pattern,string_find))
else:
    print("{} not found in {}".format(pattern, string_find))

print("Re Search....")
if re.search(pattern, string_find):
    print("{} found in {}".format(pattern, string_find))
else:
    print("{} not found in {}".format(pattern, string_find))

print("Find all......")
print(re.findall(pattern, string_find))

# re.meta characers....
print("Meta chatacters.")
if(re.match("r..s","ras")):
    print("Matched")
else:
    print("not matched")

print("Character class.....")
pattern = "[A-Z][0-9][a-z]"
if(re.search(pattern,"A9a")):
    print("Matched")
else:
    print("Not Matched..")

print("Find and Replace.....")
new = re.sub("Hello","Python","Hello worl.  Hello merry..")
print(new)


