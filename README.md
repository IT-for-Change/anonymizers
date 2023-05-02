# anonymizers

Utilities to perform simple reversible anonymization of personal identifiable data prior to sharing them with any other party. In this role, the process is more aptly called ID virtualization rather than ID anonymization.

## ID anonymization / virtualization

Any alpha-numerical identifiers, such as student roll numbers, employee numbers or pin/zip codes can be anonymized / virtualized as follows:

1. Prepare the list of identifiers as a plain text file, with one identifier per line. **There should be no header rows**
2. Name the file as **id.csv** 
3. Download the python script file **id-anon.py** and place it in the same directory as the IDs CSV file 
3. Run the python script using a Python 3 interpreter as:

`python3 id-anon.py`

4. The script produces an output file **id-after-anon.csv**. This file has a mapping of the original IDs to randomly generated IDs. Save this file in a secure location, granting access to it on need-basis only.

Wherever the identifiers are required to be shared, share the mapped random IDs instead.

See the samples directory for sample input and output files.
