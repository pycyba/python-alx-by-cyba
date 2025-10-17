import pandas as pd

emps = pd.read_csv('emps.csv', sep=';')
grupy = emps.groupby('job_title').salary.agg(['count', 'mean', 'median', 'min', 'max'])

print(grupy)

print()
print("="*80)
print()

for job, stats in grupy.iterrows():
    print(job, stats['count'], stats['mean'], stats['median'], stats['min'], stats['max'])
