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

    # def _validate_dates_lenghts(self, date_start, date_end):
    #   start_date = map(str(date_start()))
    #   end_date = map(str(date_end()))
    #   if start_date or end_date != 10:
    #     raise Exception("Please type in proper datetimes")

    # raise Exception("Please enter a proper date format")

    def _validate_dates(self, date_start, date_end):
        date_start = datetime.strptime(date_start, "%Y-%m-%d")
        date_end = datetime.strptime(date_end, "%Y-%m-%d")
        self._validate_dates_order(date_start, date_end)
        # self._validate_dates_lenghts(date_start, date_end)
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

        bool_list = list(range(len(price)))
        for i in range(len(price)):
            if i == 0:
                bool_list[i] = 1
            elif price[i] > price[i - 1]:
                bool_list[i] = bool_list[i - 1] + 1
            # elif price[-1] > price[-1 - 1]:
            #   bool_list[-1] + 1
            else:
                bool_list[i] = 0

        index_max = bool_list.index(max(bool_list))
        index_min = index_max - max(bool_list) + 1
        value_increase = round(price[index_max] - price[index_min], 2)
        print(
            f"Longest consecutive period was from "
            f"{dates[index_min][:10]} to {dates[index_max][:10]} "
            f"with increase of: ${value_increase}"
        )

    def export(self, coin, date_start, date_end, file_format, filename=None):
        df = self._convert_to_df(coin, date_start, date_end)
        df = df.rename(columns={"time_close": "Date", "close": "Price"})
        if filename is None:
            filename = f"{coin}-{date_start}-{date_end}"

        if file_format == "csv":
            df.to_csv(f"{filename}.csv", index=False)
        elif file_format == "json":
            df.to_json(f"{filename}.json", orient="records")
        elif file_format == filename:
            raise Exception("Filename can't be named as file format")
            #   inne miejsce w pamieci wiec nie wywala błedu?
        else:
            raise Exception(
                "We don't support other types os saving files, "
                "please type format .json or .csv"
            )


if __name__ == "__main__":
    print("Examples")

# Example 1
# ch = CryptoHandler()
# ch.average_by_month("btc-bitcoin", "2014-01-01", "2015-01-01")
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
