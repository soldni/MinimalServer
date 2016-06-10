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

## Throughput 

In my tests, it seems that the communication via sockets takes around 1 ms on localhost. So if the object you're trying to interface is substantially faster than that, it will impact its throughput significately. 

## A note about Python 2 / 3 interoperability

This module is a great way to use Python 2 modules in a Python 3 codebase. Just make sure to set `pickle_protocol=2` in both the client and the server. 
