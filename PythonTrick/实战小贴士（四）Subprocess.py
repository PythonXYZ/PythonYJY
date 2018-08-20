import subprocess

start1 = time.time()
subprocess.call(['Python', 'PandasOutput.py'])
end1 = time.time()
print(end1 - start1)

start2 = time.time()
subprocess.popen(['Python', 'PandasOutput.py'])
end2 = time.time()
print(end2 - start2)



