filename = "enemiesRaw.txt"

with open(filename) as file:
    lines = [line.rstrip('\n') for line in file]

result = list(set((lines)))
result.sort()

print(len(result))
print("\n  - ".join(result))