name, salary = 'aman', 12500.56
print('Hello {0}, your salary is {1}'.format(name, salary))
print('Hello {n}, your salary is{s}'.format(n=name, s=salary))
print('Hello {:s}, your salary is {:.2f}'.format(name, salary))
print('Hello %s, your salary is %.2f'%(name, salary))