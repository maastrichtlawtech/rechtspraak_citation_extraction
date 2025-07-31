import pandas as pd
import os
from dotenv import load_dotenv
from rechtspraak_citations_extractor.citations_extractor import get_citations, find_citations_for_case_graphdb, find_citations_for_cases_multithread_graphdb

load_dotenv()


def test_get_citations():
    try:
        _df = pd.read_csv("tests/rechtspraak_metadata.csv")
        _username = os.getenv("LIDO_USERNAME")
        _password = os.getenv("LIDO_PASSWORD")
        _df = get_citations(
            _df,
            username=_username,
            password=_password,
            threads=2,
            extract_opschrift=True,
        )
        assert _df is not None
    except Exception as e:
        print(f"Error in test_get_citations: {e}")
        assert False


def test_find_citations_for_case_graphdb():
    # Use a mock ECLI (replace with a real one for integration testing)
    ecli = "ECLI:NL:HR:2020:1234"
    incoming, outgoing, legislations = find_citations_for_case_graphdb(ecli)
    # Just check that the result is a tuple of lists
    assert isinstance(incoming, list)
    assert isinstance(outgoing, list)
    assert isinstance(legislations, list)


def test_find_citations_for_cases_multithread_graphdb():
    # Use mock ECLIs (replace with real ones for integration testing)
    df = pd.DataFrame({"ecli": ["ECLI:NL:HR:2020:1234", "ECLI:NL:HR:2021:5678"]})
    df_result = find_citations_for_cases_multithread_graphdb(df, threads=2)
    # Check that the expected columns are present
    assert "citations_incoming_graphdb" in df_result.columns
    assert "citations_outgoing_graphdb" in df_result.columns
    assert "legislations_cited_graphdb" in df_result.columns
