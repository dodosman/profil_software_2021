from coinpaprika import client as Coinpaprika

client = Coinpaprika.Client()

# List coins
btc = client.coins()

# for i in btc:
#   print(i["id"])

print(type(btc))
print(btc[0])
