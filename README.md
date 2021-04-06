# profil software recruitment for Intern Python Developer at Profil Software

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [CLI](#cli)

## General info
This project process historical data from external API for various cryptocurrencies. It uses Coinpaprika API.

## Technologies
Project is created with:
* Pandas version 1.2.3
* Coinpaprika API version 0.1.0
* Click  version 7.1.2

## Setup
$ pip install Pandas
$ pip install Coinpaprika
$ pip install Click

## CLI :
* To calculate average price of currency by month for given period: ` average-by-month`
* To find longest consecutive period in which price was increasing: ` high-cumulative-growth`
* To export data for given period in one of selected format csv or json: ` export`

## average-by-month
Required parameters:
* --date_start description: enter a starting date to show the range of avg price
* --date_end description: enter an ending date to show the range of avg price

## high-cumulative-growth
Required parameters:
* --date_start description: enter a starting date to show the range of high cumulative growth
* --date_end description: enter an ending date to show the range of high cumulative growth

## export
Required parameters:
* --date_start description: enter a starting date to show the range of avg price
* --date_end description: enter an ending date to show the range of avg price
* --format description: enter a format of saved file, could be csv or json.
* --filename description: enter a name for a saved file.
