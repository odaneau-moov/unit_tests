import pandas as pd
import pytest


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        [
            {
                "ID": "1000002330",
                "name": "The Songs of Adelaide & Abullah",
                "category": "Poetry",
                "main_category": "Publishing",
                "currency": "GBP",
                "deadline": "2015-10-09 11:36",
                "goal": "1000",
                "launched": "2015-08-11 12:12",
                "pledged": "0",
                "state": "failed",
                "backers": "0",
                "country": "GB",
                "usd pledged": "0",
            },
            {
                "ID": "1000004038",
                "name": "Where is Hank?",
                "category": "Narrative Film",
                "main_category": "Film & Video",
                "currency": "USD",
                "deadline": "2013-02-26 00:20",
                "goal": "45000",
                "launched": "2013-01-12 00:20",
                "pledged": "220",
                "state": "failed",
                "backers": "3",
                "country": "US",
                "usd pledged": "220",
            },
        ]
    )
