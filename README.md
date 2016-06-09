# Minimal Server

This library serves a very simple purpose: have a simple client/server pair to "serve" a Python (2 & 3) object.

Have you ever had to deal with a python object that takes *forever* to initiate? Maybe you need it to call it once in another script, but you can't bear the time it takes to initialize it.
This module comes handy in these situations. It works as follows:

Server script:

```python

from MinimalServer import run_server

obj = SlowInitObject(...)   # An instance of the object
run_server(obj, host='localhost', port=4444)
```

Client script:

```python
from MinimalServer import MinimalClient
client = MinimalClient(SlowInitObject,      # Pass the class, not the instance!
    host='localhost', port=4444)

client.foo(...)        # Call any public method of SlowInitObject
```

Easy, right?
