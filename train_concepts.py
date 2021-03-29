from coinpaprika import client as Coinpaprika

client = Coinpaprika.Client()

btc = client.candles("btc-bitcoin", start="2012-12-01T00:00:00Z", end="2013-12-01T00:00:00Z")
# for key,value in btc.items():
time_open = []
# l =list(time_open)
# for array in btc:
#   occurences = array['time_open']
#   print(occurences[:10])
for array in btc:
  occurences = array['time_open']

  time_open.append(occurences[:10])
print(len(time_open))
