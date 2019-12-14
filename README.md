# Django Query Chunk
[![pypi](https://img.shields.io/pypi/v/django-query-chunk.svg)](https://pypi.org/pypi/django-query-chunk)

Django Query Chunk is used to split big queries into multiple chunks for prevent (too high) memory usage. The chunk function will split the query set into several isolated queries.


## Requirements
* **Python**: >=3.6
* **Django**: >=2.0


## Installation

```
pip install django-query-chunk
```


## Usage

```python
from query_chunk import chunk

chunk_size = 300

for book in chunk(Book.objects.all(), chunk_size):
    # process book
```