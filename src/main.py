import sys
from calc import apply_percent

price = float(sys.argv[1])
percent = float(sys.argv[2])


res = apply_percent(price, percent)
print(res)

#print(f'Price : {price}/ percent : {percent}')


