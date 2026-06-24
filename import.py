from fredapi import Fred
fred = Fred(api_key='44ffecad7176178b4de2a1b476b4f617')
cpi = fred.get_series('CPIAUCNS')
print(cpi)