from brightway2 import *

print(list(projects))
bw2setup()
print(list(databases))
print(projects.dir)
projects.copy_project('my copy')
print(projects.current)
