---
title: "Python Basics: Batteries included! 🔋🔋🔋"
date: 2022-04-13
author: Tim Fischer <me@timfi.dev>
styles:
  style: gruvbox-dark
  margin:
    top: 3
    bottom: 0
  padding:
    top: 3
    bottom: 3
---

# _Batteries included?_

> The Python source distribution has long maintained the
> philosophy of “batteries included” – having a rich and
> versatile standard library which is immediately available,
> without making the user download separate packages. This
> gives the Python language a head start in many projects.

[– PEP 206 by A.M. Kuchling](https://peps.python.org/pep-0206/)

---

# Where?!

**HERE**: https://docs.python.org/3/library/index.html

- Text Processing: `string`, `re`, ...
- Fileaccess: `pathlib`, `os.path`, `tempfile`, ...
- Fileformats: `csv`, `json`, `html`, `xml`, (`toml`), ...
- Parallelism: `threading`, `multiprocessing`, `concurrent.futures`, ...
- Non-Blocking I/O: `asyncio`, `select`, `selectors`, ...
- Internet: `urllib`, `http`, `socketserver`, ...
- CLI: `optparse`, `argparse`, ...
- GUI: `tkinter`.

---

# Todays plan

## What happens when?

| When?         | What?                |
|:-------------:|:-------------------- |
| 13:15 - 14:30 | Intro & Acquisition  |
| 14:30 - 14:45 | *break*              |
| 14:45 - 16:00 | Exploration (& CLI?) |

## Structure of a _what_

1. Short Intro
2. Exercise description
3. Reading some documentation
4. Doing the exercise
5. If done with section
    1. then goto 1.
    2. else goto 2.

---

# Project of the day: Starwars-Thingy!

Let's use _SWAPI_, the starwars API!

> https://swapi.dev

---

# Downloading things...

## Goals

- Fire off a request to a given url
- Parse the response body as json

## Batteries:

- `urllib` [(docs)](https://docs.python.org/3/library/urllib.html)
- `json` [(docs)](https://docs.python.org/3/library/json.html)

---

# Downloading things...

## Template

```python
from urllib.request import urlopen
import json


def download_json(url):
    """Download a given url and parse its content as json.

    :param url: the url of the resource
    :type url: str

    :return: downloaded and parsed json
    :rtype: Any
    """
```

---

# Downloading things...

## Solution

```python
from urllib.request import urlopen
import json


def download_json(url):
    resp = urlopen(url)
    body = resp.read()
    return json.loads(body)
```

---

# Downloading _complicated_ things...

## Goals

- Retrieve a chain of things (e.g. https://swapi.dev/api/people)

## Batteries

- `download_json` (see previous)

---

# Downloading _complicated_ things...

## Template

```python
def download_chain(start):
    """Download all links in a given chain.

    :param start: first link in the chain
    :type start: str

    :return: list of all results in a chain
    :rtype: Any
    """
```

---

# Downloading _complicated_ things...

## Solution

```python
def download_chain(start):
    res = []
    url = start
    while url is not None:
        data = download_json(url)
        res.extend(data["results"])
        url = data["next"]
    return res
```

---

# Downloading _complicated_ things... (but more generic)

## Goals

- Retrieve a chain of things (e.g. https://swapi.dev/api/people)
- Expose some functionality via function parameters (*callbacks*)

## Batteries

- `download_json` (see previous)
- _higher order functions_

---

# Downloading _complicated_ things... (but more generic)

## Template

```python
def download_chain(chain_link, get_result, start):
    """Download all links in a given chain.

    :param chain_link: function to determin the next link in
                       a chain
    :type chain_link: Callable[[Any], str]

    :param chain_link: function to extract a list of relevant
                       data from each link
    :type chain_link: Callable[[Any], list[T]]

    :param start: first link in the chain
    :type start: str

    :return: list of all results in a chain
    :rtype: list[T]
    """
```

---

# Downloading _complicated_ things... (but more generic)

## Solution

```python
def download_chain(chain_link, get_result, start):
    res = []
    start = url
    while url is not None:
        data = download_json(url)
        res.extend(get_result(data))  # ← NEW! ✨
        url = chain_link(data)        # ← NEW! ✨
    return res
```

---

# Do things in parallel

## Goals

- Do a given task for a set of parameters *"in parallel"*

## Batteries

- `concurrent.futures` [(docs)](https://docs.python.org/3/library/concurrent.futures.html)

> ** ⚠ This is – a lot – more difficult! **

---

# Do things in parallel

## Template

```python
from concurrent.futures import ThreadPoolExecutor, as_completed


def do_parallel(task, args):
    """Do a single task for different inputs in parallel.

    :param task: function representing the task to do
    :type task: Callable[[Args], T]

    :param args: list of all argument sets to run
    :type args: list[Args]

    :return: dictionary of task results
    :rtype: dict[Args, T]
    """
```

---

# Do things in parallel

## Solution

```python
from concurrent.futures import ThreadPoolExecutor, as_completed


def do_parallel(task, args):
    res = {}
    with ThreadPoolExecutor() as pool:
        futs = {
            pool.submit(f, arg): arg
            for arg in args
        }
        for fut in as_completed(futs):
            res[futs[fut]] = fut.result()
    return res
```

---

   ╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴
# Interlude: the dreaded GIL...

## What?

**GIL**: The Global Interpreter Lock

## What??

Only one thread per process can use the python interpreter at a time!

## What???

Threads in python are good at doing _nothing_, i.e. blocking I/O.

   ╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴