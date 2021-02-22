
processors = ["Pentium", "Core", "Xeon", "Athlon", "Ryzen", "Threadripper"]
base_cores = [4, 2, 64]

processors.extend(base_cores)

print(processors)

processors.append("Radeon")

print(processors)

processors.insert(3, "XE")

print(processors)

processors.remove("Athlon")

print(processors)

print(processors.index("XE"))

print(processors.count("Athlon"))

processors.pop()

print(processors)

processors.clear()

print(processors)

base_cores.sort()

print(base_cores)

base_cores.reverse()

print(base_cores)

processors2 = processors.copy()

print(processors2)
