#python .\python-exercises\dishonest-capacity-calculator.py
discrepancy = None
print('Enter TB or GB for the advertised unit:')
unit = input('>')

#calculate the amount that the advertised capacity lies:
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824

if discrepancy != None:
    discrepancy = 0
print('Enter the advertised capacity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

#calculate the real capacity, round it to the nearest hundredt hs,
#and convert it to a string so it can be concatenated:
real_capacity = str(round(advertised_capacity*discrepancy,2))

print('The actual capacity is '+real_capacity+' '+unit)