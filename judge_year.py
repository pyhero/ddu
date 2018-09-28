year_input = input('year: ')
while not year_input.isdigit():
    year_input = input('year: ')

year = int(year_input)

year_judge = year / 400
print(year, year_judge)

if isinstance(year_judge, int):
    print('Yes')
else:
    print('No')

