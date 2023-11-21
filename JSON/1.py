import json
# Список заполняется данными
filename = 'D:\\Тест прогсы\\py.test1\\py.test1-1\\JSON\\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    
# Вывод населенипя каждой страны за 2010 год.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country_name + ": " + population)