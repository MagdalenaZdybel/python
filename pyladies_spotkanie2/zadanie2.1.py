file = open('py1.2.txt').read()

print(file)

slo = {file}
slo[file] = '2'
print(slo)
