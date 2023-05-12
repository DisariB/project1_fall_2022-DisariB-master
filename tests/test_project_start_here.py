"""This is the starting test file"""
import pandas as pd
from app.stats import Statistics


def test_stats_pop_min():
    """tests functionality of pop_min"""
    data = {'state': ['Oklahoma', 'Florida', 'Utah', 'Michigan', 'North Carolina'],
            'pop': [100, 500, 300, 400, 2000]}
    my_dataframe = pd.DataFrame(data)
    assert Statistics.pop_min(my_dataframe) == 100


def test_stats_pop_count():
    """tests functionality of pop_count"""
    data = {'state': ['Oklahoma', 'Florida', 'Utah', 'Michigan', 'North Carolina'],
            'pop': [100, 500, 300, 400, 2000]}
    my_dataframe = pd.DataFrame(data)
    assert Statistics.pop_count(my_dataframe) == 5
