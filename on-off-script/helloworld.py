#!/usr/bin/env python
# helloworld.py
__version__ = "0.1.0"

import re
import requests

URL = "htps://en.wikipedia.org/wiki/HelloWorld_program"

def do_hello():
    """Print hello world."""
    result = requests.get(URL)
    print(re.findall('<title>(.*?)</title>', result.text)[0])

if __name__ == "__main__":
    main()
