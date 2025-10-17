from employees import Employee

emp1 = Employee(100, 'Steven', 'King', 'President', 24000, '1997-06-17',
                  'Executive', '2004 Charade Rd', '98199', 'Seattle', 'United States of America')
print(emp1)

# metoda init rzutuje dane na odpowiednie typy nawet, jeśli przekażemy tekstowo
emp2 = Employee('100', 'Steven', 'King', 'President', '24000', '1997-06-17',
                  'Executive', '2004 Charade Rd', '98199', 'Seattle', 'United States of America')
print(emp2.salary * 12)
print(emp2.hire_date.year)
