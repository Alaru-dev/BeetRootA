from datetime import date # take today date, need to all  methods
from string import Template # need to show Template Strings
# create variables
my_name = 'Roman'
today_date = date.today()

print('Good day %s! %s is a perfect day to learn some python.' % (my_name, today_date)) # "old school" method, I don`t know why but in article wrote that method is unstable
print(f'Good day {my_name}! {today_date} is a perfect day to learn some python.') #f-Strings method

str_for_print = 'Good day {my_name}! {today_date} is a perfect day to learn some python.'
print(str_for_print.format(my_name = my_name, today_date = today_date))  #“New Style” String Formatting (str.format)

templ_str = 'Good day $my_name! $today_date is a perfect day to learn some python.'
print(Template(templ_str).substitute(my_name = my_name, today_date = today_date)) #Template Strings (Standard Library)
