import pandas as pd
import pytest
from profil_software_2021.calculations import CryptoHandler
ch = CryptoHandler()




# @pytest.fixture
def data_set_1():
    df = pd.DataFrame({
      'time_close': [
        '2014-01-01T23:59:59Z', '2014-01-01T23:59:59Z',
        '2014-01-01T23:59:59Z','2014-01-02T23:59:59Z',
        '2014-01-03T23:59:59Z', '2014-01-04T23:59:59Z',
        '2014-01-05T23:59:59Z'
        ],
      'close': [
        771.40, 802.39, 818.72, 859.51, 933.53, 953.29, 802.00
        ]})
    return df

#
# # Cena maleje
# @pytest.fixture
# def data_set_2():
#     df = pd.DataFrame({"column_1": [5, 4, 3, 2, 1], "column_b": [5, 4, 3, 2, 1]})
#     return df
#
#
# # Cena stala
# @pytest.fixture
# def data_set_3():
#     df = pd.DataFrame({"column_1": [3, 3, 3, 3, 3], "column_b": [3, 3, 3, 3, 3]})
#     return df
#
#
# # Cena zmienia sie
# @pytest.fixture
# def data_set_5():
#     df = pd.DataFrame({"column_1": [5, 4, 3, 10, 20], "column_b": [5, 4, 3, 10, 20]})
#     return df
#
#
# # Edge case 1
# @pytest.fixture
# def data_set_4():
#     df = pd.DataFrame({"column_1": [3, 3, 3, np.nan, 3], "column_b": [3, 3, 3, 3, 3]})
#     return df
#
#

# Testy
def test_cumulative_growth_1(data_set_1):
    # output_expected = data_set_1()
    output_tested = ch._high_cumulative_growth(data_set_1())
    print(output_tested)
    # assert output_expected == output_tested


# def test_cumulative_growth_2(data_set_2):
#     output_expected = pd.DataFrame({"output": [8, 9, 10]})
#     output_tested = ch.high_cumulative_growth(data_set_2)
#     assert output_expected == output_tested
#
#
# def test_cumulative_growth_3(data_set_3):
#     output_expected = pd.DataFrame({"output": [5, 5, 5]})
#     output_tested = ch.high_cumulative_growth(data_set_3)
#     assert output_expected == output_tested
#
#
# def test_output_attributes(data_set_1):
#     output = ch.high_cumulative_growth(data_set_1)
#     assert isinstance(output, pd.DataFrame)
#     assert output.shape[1] == 1  # len(output.columns) == 1
#     assert output.columns == ["output"]

test_cumulative_growth_1(data_set_1)
