import pandas

emps = pandas.read_csv('emps.csv', sep=';')

print('Wczytano', len(emps), 'rekordów')
print(type(emps))

print('Średnia pensja wszystkich:', emps["salary"].mean())
print('Średnia pensja wszystkich:', emps.salary.mean())
print('Średnia pensja programistów:', emps[emps.job_title == 'Programmer'].salary.mean())
print()

grupy = emps.groupby('job_title').salary.mean()
print(grupy)
print("============\n\n")

for job, avg in grupy.items():
    print(job, avg)
