from datetime import datetime
from datetime import date, timedelta
yesterday = date.today() - timedelta(days=1)

print(yesterday.strftime('%Y%m%d'))
print(type(yesterday.strftime('%Y%m%d')))


