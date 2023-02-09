import os, sys

path = sys.argv[1]
excepts = ["README.md", "test.md"]
items = sorted([x for x in os.listdir(path) if x.endswith('.md') and not x.startswith('_') and x not in excepts])
print("* [{}]({})".format("Home", "/"))
for item in items:
    print(format("* [{}]({})".format(item.capitalize().split(".")[0], item)))