from datetime import datetime, date

from coinpaprika import client as Coinpaprika
client = Coinpaprika.Client()

start_time = input("What is a starting time ?: (Year-month-day format)")
end_time = input("What is an ending time in interval?: (Year-month-day format)")
date_start_time = datetime.strptime(start_time, '%Y-%m-%d')
date_end_time = datetime.strptime(end_time, '%Y-%m-%d')



time_open = []
def average_price_of_currency():

  btc = client.candles("btc-bitcoin", start=f"{start_time}T00:00:00Z", end=f"{end_time}T00:00:00Z")
  for array in btc:
    occurences = array['time_open']
    time_open.append(occurences[:10])
  print(len(time_open))
delta = date_end_time - date_start_time
print(delta.days)













# print("Date: ",array["time_open"][:10],"opening: ",array["open"], " ","closing: ", array['close'])
average_price_of_currency()





















#
# def validate_date(start_time, end_time ):
#     if len(start_time and end_time) == 10:
#       datetime.strptime(start_time and end_time, '%Y-%m-%d')
#       return True
#     else:
#       return False
#       validate_date(start_time, end_time)
#
#
# print(validate_date(start_time, end_time))

