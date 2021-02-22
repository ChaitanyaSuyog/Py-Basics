
jobs_file = open("jobs", "r")

for employee in jobs_file.readlines():
    print(employee)

jobs_file.close()
