
employees_file = open("employees", "a")
# Using "w" instead of "a" will not append, but overwrite the file.

employees_file.write("\nTobias - Developer")

employees_file.close()

jobs_file = open("employees1", "w")

jobs_file.write("\nBackup")

jobs_file.close()