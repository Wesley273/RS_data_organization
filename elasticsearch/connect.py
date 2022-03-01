# Import the client from the 'elasticsearch' module
from datetime import datetime

from elasticsearch import Elasticsearch

# Instantiate a client instance
client = Elasticsearch("http://localhost:9200")
# Call an API, in this example `info()`
print(client.info())
doc = {
    'author': 'author_name',
    'text': 'Interensting content...',
    'timestamp': datetime.now(),
}
resp = client.index(index="test-index", id=1, document=doc)
print(resp['result'])
client.delete(index="test-index")
