import pandas as pd
from opendp.smartnoise.sql import PandasReader, PrivateReader
from opendp.smartnoise.metadata import CollectionMetadata

pums = pd.read_csv('PUMS.csv')
meta = CollectionMetadata.from_file('PUMS.yaml')

query = 'SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married'

reader = PandasReader(pums, meta)
private_reader = PrivateReader(reader, meta)

result = private_reader.execute(query)

print(result)
