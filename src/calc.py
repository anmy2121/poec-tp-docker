
def apply_percent(price: float, percent: float):
   if not isinstance(price, float):
      return f'Price (${price}) is not a number'

   if price < 0:
      return f'Price (${price}) is negative'

   if percent < 0 or percent > 100:
      return f'Percentage ({percent}%) is not within the bounds 0 to 100'

   final_percent = price * (1 + percent / 100)
   return final_percent





