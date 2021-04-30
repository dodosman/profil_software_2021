from datetime import datetime

import pandas as pd
from coinpaprika import client as Coinpaprika


class CryptoHandler:
  def __init__(self):
    self.client = Coinpaprika.Client()

  def _validate_start_date(self, date_start):
    date_initial = datetime.strptime("2009-01-12", "%Y-%m-%d")
    if date_start < date_initial:
      raise Exception(f"Start date can't be earlier than: {date_initial}")

  def _validate_dates_order(self, date_start, date_end):
    if date_start > date_end:
      raise Exception("Start date can't be later than end date.")

  def _validate_dates_format(self, date_start, date_end):
    try:
      datetime.strptime(date_start, '%Y-%m-%d')
      datetime.strptime(date_end, '%Y-%m-%d')
    except ValueError:
      raise ValueError("Incorrect data format, should be YYYY-MM-DD")

  def _validate_dates(self, date_start, date_end):
    self._validate_dates_format(date_start, date_end)
    date_start = datetime.strptime(date_start, "%Y-%m-%d")
    date_end = datetime.strptime(date_end, "%Y-%m-%d")
    self._validate_dates_order(date_start, date_end)
    self._validate_start_date(date_start)

  def _create_start_end_times(self, date_start, date_end):
    self._validate_dates(date_start, date_end)
    self.start_time = f"{date_start}T00:00:00Z"
    self.end_time = f"{date_end}T00:00:00Z"
    return self

  def _check_if_coin_exists(self, coin):
    btc_ids = self.client.coins()
    coin_list = []
    for i in btc_ids:
      coin_list.append(i["id"])
    if coin not in coin_list:
      raise Exception("Given cryptocurrency does not exists")

  def _call_client(self, coin):
    self._check_if_coin_exists(coin)
    dict_prices = self.client.candles(
      coin, start=self.start_time, end=self.end_time
    )
    if not dict_prices:
      raise ValueError(
        "CoinPaprika returns empty list. No trading information "
        "is available for this coin at these dates"
      )
    return dict_prices

  def _convert_to_df(self, coin, date_start, date_end):
    self._create_start_end_times(date_start, date_end)
    dict_prices = self._call_client(coin)
    df_raw = pd.DataFrame(dict_prices)
    df = df_raw.filter(items=["time_close", "close"])
    return df

  def _modify_time_columns(self, df):
    df["year"] = pd.DatetimeIndex(df["time_close"]).year
    df["month"] = pd.DatetimeIndex(df["time_close"]).month
    df["month"] = df["month"].apply(lambda x: str(x) if x >= 10 else "0" + str(x))
    df["Date"] = df["year"].astype(str) + "-" + df["month"].astype(str)
    return df

  def average_by_month(self, coin, date_start, date_end):
    df_raw = self._convert_to_df(coin, date_start, date_end)
    df_prc = self._modify_time_columns(df_raw)
    df_gb = (
      df_prc.groupby("Date")["close"]
        .mean()
        .round(2)
        .reset_index(name="Average price ($)")
    )
    print(df_gb)
    return df_gb

  def high_cumulative_growth(self, coin, date_start, date_end):
    df = self._convert_to_df(coin, date_start, date_end)
    price = df["close"].squeeze()
    dates = df["time_close"].squeeze()

    bool_list = len(price)
    m = 1
    l = 1
    starting_index = 0
    for i in range(1, bool_list):
      if (price[i] > price[i - 1]):
        l = l + 1
      else:
        if (m < l):
          m = l
          starting_index = i - m
        l = 1
    if (m < l):
      m = l
      starting_index = price - m

    starting_date = dates[starting_index][:10]
    ending_date = dates[m + starting_index - 1][:10]
    value_increase = round(price[m + starting_index - 1] - price[starting_index], 2)

    print(
      f"Longest consecutive period was from "
      f"{starting_date} to {ending_date} "
      f"with increase of: ${value_increase}"
    )


def _verify_export_filename(self, filename):
  split_filename = filename.split('.')
  if "csv" in split_filename:
    raise Exception("Filename should not be named as a file type.")
  elif "json" in split_filename:
    raise Exception("Filename should not be named as a file type.")


def export(self, coin, date_start, date_end, file_format, filename=None):
  df = self._convert_to_df(coin, date_start, date_end)
  df = df.rename(columns={"time_close": "Date", "close": "Price"})

  if filename is None:
    filename = f"{coin}-{date_start}-{date_end}"
  else:
    self._verify_export_filename(filename)

  if file_format == "csv":
    df.to_csv(f"{filename}.csv", index=False)
  elif file_format == "json":
    df.to_json(f"{filename}.json", orient="records")
  else:
    raise Exception(
      "We don't support other types os saving files, "
      "please type format .json or .csv"
    )


if __name__ == "__main__":
  print("Examples")

# Example 1
ch = CryptoHandler()
ch.average_by_month("btc-bitcoin", "2014-01-01", "2015-01-01")
# ch.average_by_month("usdt-tether", "2021-01-01", "2021-05-01")
# ch.average_by_month("eth-ethereum", "2016-01-01", "2017-01-01")

# Example 2
# ch = CryptoHandler()
# ch.high_cumulative_growth("btc-bitcoin", "2015-01-01", "2016-01-01")
# ch.high_cumulative_growth("usdt-tether", "2021-01-01", "2021-05-01")
# ch.high_cumulative_growth("eth-ethereum", "2016-01-01", "2017-01-01")

# Example 3
# ch = CryptoHandler()
# ch.export("btc-bitcoin", "2015-01-01", "2016-01-01", "csv")
# ch.export("usdt-tether", "2021-01-01", "2021-05-01", "json")
