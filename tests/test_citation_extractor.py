import pandas as pd
import os
from dotenv import load_dotenv
from rechtspraak_citations_extractor.citations_extractor import get_citations

load_dotenv()


def test_get_citations():
    try:
        _df = pd.read_csv("tests/rechtspraak_metadata.csv")
        _username = os.getenv("LIDO_USERNAME")
        _password = os.getenv("LIDO_PASSWORD")
        _df = get_citations(_df, username=_username, password=_password, threads=2)
        assert _df is not None
    except Exception as e:
        print(f"Error in test_get_citations: {e}")
        assert False
