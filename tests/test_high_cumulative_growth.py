import pandas as pd
import pytest
from calculations import CryptoHandler

ch = CryptoHandler()


# rozne ceny
@pytest.fixture
def data_set_1():
    df = pd.DataFrame(
        {
            "time_close": [
                "2014-01-01T23:59:59Z",
                "2014-01-02T23:59:59Z",
                "2014-01-03T23:59:59Z",
                "2014-01-04T23:59:59Z",
                "2014-01-05T23:59:59Z",
                "2014-01-06T23:59:59Z",
                "2014-01-07T23:59:59Z",
            ],
            "close": [771.40, 802.39, 818.72, 859.51, 933.53, 953.29, 802.00],
        }
    )
    return df


# cena ciągle wzrasta
@pytest.fixture
def data_set_2():
    df = pd.DataFrame(
        {
            "time_close": [
                "2014-01-01T23:59:59Z",
                "2014-01-02T23:59:59Z",
                "2014-01-03T23:59:59Z",
                "2014-01-04T23:59:59Z",
                "2014-01-05T23:59:59Z",
                "2014-01-06T23:59:59Z",
                "2014-01-07T23:59:59Z",
            ],
            "close": [771.40, 781.39, 782.72, 791.51, 801.53, 811.29, 821.00],
        }
    )
    return df


# cena maleje
@pytest.fixture
def data_set_3():
    df = pd.DataFrame(
        {
            "time_close": [
                "2014-01-01T23:59:59Z",
                "2014-01-02T23:59:59Z",
                "2014-01-03T23:59:59Z",
                "2014-01-04T23:59:59Z",
                "2014-01-05T23:59:59Z",
                "2014-01-06T23:59:59Z",
                "2014-01-07T23:59:59Z",
            ],
            "close": [953.29, 923.17, 920.78, 859.51, 839.53, 824.29, 802.00],
        }
    )
    return df


# cena ciagle sie zmienia
@pytest.fixture
def data_set_4():
    df = pd.DataFrame(
        {
            "time_close": [
                "2014-01-01T23:59:59Z",
                "2014-01-02T23:59:59Z",
                "2014-01-03T23:59:59Z",
                "2014-01-04T23:59:59Z",
                "2014-01-05T23:59:59Z",
                "2014-01-06T23:59:59Z",
                "2014-01-07T23:59:59Z",
            ],
            "close": [452.12, 351.85, 691.85, 211.93, 340.07, 300.38, 400.76],
        }
    )
    return df


#
#
@pytest.fixture
def data_set_5():
    df = pd.DataFrame(
        {
            "time_close": [
                "2014-01-01T23:59:59Z",
                "2014-01-02T23:59:59Z",
                "2014-01-03T23:59:59Z",
                "2014-01-04T23:59:59Z",
                "2014-01-05T23:59:59Z",
                "2014-01-06T23:59:59Z",
                "2014-01-07T23:59:59Z",
            ],
            "close": [771.40, 802.39, 800.39, 798.51, 933.53, 953.29, 1000.00],
        }
    )
    return df


#
#

# Testy
def test_cumulative_growth_1(data_set_1):
    output_expected = ("2014-01-01T23:59:59Z", "2014-01-06T23:59:59Z", 181.89)
    date_min, date_max, value_increase = ch._high_cumulative_growth(data_set_1)
    output_tested = (date_min, date_max, value_increase)
    assert output_expected == output_tested


def test_cumulative_growth_2(data_set_2):
    output_expected = ("2014-01-01T23:59:59Z", "2014-01-07T23:59:59Z", 49.6)
    date_min, date_max, value_increase = ch._high_cumulative_growth(data_set_2)
    output_tested = (date_min, date_max, value_increase)
    assert output_expected == output_tested


def test_cumulative_growth_3(data_set_3):
    output_expected = ("2014-01-01T23:59:59Z", "2014-01-01T23:59:59Z", 0)
    date_min, date_max, value_increase = ch._high_cumulative_growth(data_set_3)
    output_tested = (date_min, date_max, value_increase)
    assert output_expected == output_tested


#
def test_cumulative_growth_4(data_set_4):
    output_expected = ("2014-01-01T23:59:59Z", "2014-01-01T23:59:59Z", 0)
    date_min, date_max, value_increase = ch._high_cumulative_growth(data_set_4)
    output_tested = (date_min, date_max, value_increase)
    assert output_expected == output_tested


def test_cumulative_growth_5(data_set_5):
    output_expected = ("2014-01-05T23:59:59Z", "2014-01-07T23:59:59Z", 66.47)
    date_min, date_max, value_increase = ch._high_cumulative_growth(data_set_5)
    output_tested = (date_min, date_max, value_increase)
    assert output_expected == output_tested


# def test_output_attributes(data_set_1):
#     output = ch.high_cumulative_growth(data_set_1)
#     assert isinstance(output, pd.DataFrame)
#     assert output.shape[1] == 1  # len(output.columns) == 1
#     assert output.columns == ["output"]

# test_cumulative_growth_1(data_set_1)
# test_cumulative_growth_2(data_set_2)
# test_cumulative_growth_3(data_set_3)
