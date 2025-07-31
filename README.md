## Rechtspraak citations
This library contains a function that aqcuires citation data for Rechtspraak cases using the LIDO.

## Version
Python 3.9

## Contributors

<!-- readme: contributors,gijsvd -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/Cloud956">
            <img src="https://avatars.githubusercontent.com/u/24865274?v=4" width="100;" alt="Cloud956"/>
            <br />
            <sub><b>Piotr Lewandowski</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/shashankmc">
            <img src="https://avatars.githubusercontent.com/u/3445114?v=4" width="100;" alt="shashankmc"/>
            <br />
            <sub><b>shashankmc</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/gijsvd">
            <img src="https://avatars.githubusercontent.com/u/31765316?v=4" width="100;" alt="gijsvd"/>
            <br />
            <sub><b>gijsvd</b></sub>
        </a>
    </td>
</tr>
</table>
<!-- readme: contributors,gijsvd -end -->

## How to install?
<code>pip install rechtspraak_citations_extractor</code>

## What are the functions?
<li><b>Rechtspraak Citations Extractor</b>
<ol>
    <li><code>get_citations</code></li>
    Gets all the data about case law citing/being cited and the legislations cited from the cases 
    in passed on DataFrame of case metadata. Requires a valid DataFrame object with a column titled 'ecli'. Returns the same Dataframe object,
     with 3 additional columns containing JSON strings of citation information.
</ol> </li>

## What are the parameters?
<ol>
    <li><strong>get_citations(dataframe = None, username = '', password = '', threads = 2)</strong></li>
    <strong>Parameters:</strong>
    <ul>
        <li><strong>dataframe: Pandas DataFrame object, required</strong></li>
        A Dataframe object, which must have a column titled 'ecli'. 
        The code extracts citations for each separate ECLI in the column. 
        A Dataframe with Rechtspraak data can be aqcuired via the rechtspraak extractor - https://pypi.org/project/rechtspraak-extractor
        <br>Default: None
        <li><strong>username: string, required, default ''</strong></li>
        The username that together with the password can be used to log into LIDO.
        <li><strong>password: string, required, default ''</strong></li>
        The password that together with the username can be used to log into LIDO.
        <li><strong>threads: int, optional, default 1</strong></li>
        Option for multi-threading of LiDO requests - not recommended to go above 2, as LiDO breaks connections when overwhelmed.
    </ul>
</ol>


## Examples
```
import rechtspraak_extractor as rex
import rechtspraak_citations_extractor as rex_citations
-----------------------------------------------------------------------------------------------------------------------

# To get the rechtspraak data in a dataframe:
df = rex.get_rechtspraak(max_ecli=100, sd='2022-08-01', save_file='y')  # Gets 100 ECLIs from 1st August 2022
df = get_rechtspraak_metadata(save_file='n',dataframe=df)
# To get the citations:
df_with_citaitons = rex_citations.get_citations(df,'username','password')
```

## New Feature: GraphDB/SPARQL Citation Extraction

This library now supports extracting citation data for Rechtspraak cases directly from a GraphDB (triple store) using SPARQL queries, as an alternative to the LIDO API. This is useful if you have loaded the LiDO data into a local or remote GraphDB instance (e.g., using the provided TTL file).

### Available Functions
- `find_citations_for_case_graphdb(ecli)`
  - Extracts incoming/outgoing case citations and legislation citations for a single ECLI using SPARQL.
- `find_citations_for_cases_multithread_graphdb(dataframe, threads=1)`
  - Extracts citations for all ECLIs in a DataFrame using multithreading.

### Parameters
- **ecli**: The ECLI string for the case you want to extract citations for.
- **dataframe**: A Pandas DataFrame with a column named 'ecli'.
- **threads**: Number of threads to use for batch extraction (default: 1).

### GraphDB Endpoint Configuration
By default, the endpoint is set to `http://localhost:7200/repositories/rechtspraak`. You can change this in `citations_extractor.py`:
```python
GRAPHDB_ENDPOINT = "http://localhost:7200/repositories/rechtspraak"  # Change as needed
```
If your GraphDB requires authentication, set `GRAPHDB_USERNAME` and `GRAPHDB_PASSWORD` as well.

### Example Usage
```python
from rechtspraak_citations_extractor.citations_extractor import find_citations_for_case_graphdb, find_citations_for_cases_multithread_graphdb
import pandas as pd

ecli_examples = ["ECLI:NL:HR:2020:1234", "ECLI:NL:HR:2021:5678"]
df = pd.DataFrame({"ecli": ecli_examples})

# Single case extraction
for ecli in ecli_examples:
    incoming, outgoing, legislations = find_citations_for_case_graphdb(ecli)
    print(f"ECLI: {ecli}")
    print("  Incoming:", incoming)
    print("  Outgoing:", outgoing)
    print("  Legislations:", legislations)

# Batch extraction (multithreaded)
df_result = find_citations_for_cases_multithread_graphdb(df, threads=2)
print(df_result)
```

### Notes
- The SPARQL queries assume a certain schema for ECLI and citation relationships. You may need to adjust the queries in `citations_extractor.py` if your GraphDB uses different predicates or structures.
- Both LIDO and GraphDB extraction methods can be used side by side.

## License
[![License: Apache 2.0](https://img.shields.io/github/license/maastrichtlawtech/extraction_libraries)](https://opensource.org/licenses/Apache-2.0)

Previously under the [MIT License](https://opensource.org/licenses/MIT), as of 28/10/2022 this work is licensed under a [Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0).
```
Apache License, Version 2.0

Copyright (c) 2022 Maastricht Law & Tech Lab

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
