# profil software recruitment for Intern Python Developer at Profil Software

This project process historical data from external API for various cryptocurrencies. It uses Coinpaprika API.

## Technologies

Project was created with:
* `python` version
* `pandas` version 1.2.3
* `coinpaprika` API version 0.1.0
* `click` version 7.1.2

## Setup

```bash
pip install pandas coinpaprika click
```

## Cli :

* `average-by-month` - to calculate average price of currency by month for a given period
* `high-cumulative-growth` - to find the longest consecutive period in which price was increasing
* `export` - to export data for given period in one of selected format: csv or json

Additionally, one `bonus` task was completed to extended the cli functionality to **more than one cryptocurrency**.

## Examples


### **average-by-month**

```bash
python cli.py average-by-month --date_start "2014-01-01" --date_end "2015-01-01" --coin "btc-bitcoin"
```

```bash
python cli.py average-by-month --date_start "2021-01-01" --date_end "2021-05-01" --coin "usdt-tether"
```


### **high-cumulative-growth**

```bash
python cli.py high-cumulative-growth --date_start "2014-01-01" --date_end "2015-01-01" --coin "btc-bitcoin"
```

```bash
python cli.py high-cumulative-growth --date_start "2016-03-01" --date_end "2016-08-01" --coin "eth-ethereum"
```


### **export**

```bash
python cli.py export --date_start "2016-03-01" --date_end "2016-08-01" --coin "btc-bitcoin" --file_format "csv"
```

```bash
python cli.py export --date_start "2016-03-01" --date_end "2016-08-01" --coin "btc-bitcoin" --file_format "csv" --filename "make_money"
```

```bash
python cli.py export --date_start "2016-03-01" --date_end "2016-08-01" --coin "btc-bitcoin" --file_format "json"
```
