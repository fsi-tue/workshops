---
title: "Python Basics: Batteries included! 🔋🔋🔋"
date: 2022-04-13
author: Tim Fischer <me@timfi.dev>
styles:
  style: gruvbox-dark
  margin:
    top: 2
    bottom: 0
  padding:
    top: 2
    bottom: 2
---

# Slide Centering and Scaling Guides

```
┏╾╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╼┳╾╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╼┓
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                     ╭╴┆╶╮                                     ┆
┣╾╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╼╋╾╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╼┫
┆                                     ╰╴┆╶╯                                     ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┆                                       ┆                                       ┆
┗╾╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╼┻╾╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╼┛
```

> This slide if for centering and scaling your terminal appropriately when using
> `lookatme`. This entire presentation is built to fit this exact scaling. Please
> ensure that the entire box above is visible without line wrapping. And that this
> block quote isn't visible.

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

---

# Todays plan

## Structure of a _what_

1. Short Intro
2. Do some exploratory exercises:
    1. Exercise description (≈1-2 min)
    2. Reading some documentation (≈5 min)
    3. Thinking/doing the exercise (≈5 min)
    4. Discuss solutions (≈5 min)

---

# Project of the day: What is the most unique Starwars Movie?

Let's use _SWAPI_, the starwars API!

> https://swapi.dev

---

# _Exercise 1:_ Downloading things...

## Goals

- Fire off a request to a given url
- Parse the response body as json

## Batteries:

- `urllib` [(docs)](https://docs.python.org/3/library/urllib.html)
- `json` [(docs)](https://docs.python.org/3/library/json.html)

---

# _Exercise 1:_ Downloading things...

## Template

```python
def download_json(url):
    """Download a given url and parse its content as json.

    :param url: the url of the resource
    :type url: str

    :return: downloaded and parsed json
    :rtype: Any
    """
```

---

# _Exercise 1:_ Downloading things...

## Solution

```python
def download_json(url):
    resp = urlopen(url)
    body = resp.read()
    return json.loads(body)
```

---

# _Exercise 2:_ Downloading _complicated_ things...

## Goals

- Retrieve a chain of things (e.g. https://swapi.dev/api/people)

## Batteries

- `download_json` (see previous)

---

# _Exercise 2:_ Downloading _complicated_ things...

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

# _Exercise 2:_ Downloading _complicated_ things...

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

# _Exercise 3:_ Downloading _complicated_ things... (but more generic)

## Goals

- Retrieve a chain of things (e.g. https://swapi.dev/api/people)
- Expose some functionality via function parameters (*callbacks*)

## Batteries

- `download_json` (see previous)
- _higher order functions_

---

# _Exercise 3:_ Downloading _complicated_ things... (but more generic)

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

# _Exercise 3:_ Downloading _complicated_ things... (but more generic)

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

# _Exercise 4:_ URLs are ugly data...

## Goals

- Get rid of those ugly URLs...

## Batteries

- `re` [(docs)](https://docs.python.org/3/library/re.html)

---

# _Exercise 4:_ URLs are ugly data...

## Template

```python
def url_to_id(string):
    """Extract the ID out of a given string.

    :param string: The string to extract the ID from.
    :type string: str

    :return: Either the extracted ID or the original string
    :rtype: str
    """
```

---

# _Exercise 4:_ URLs are ugly data...

## Solution

```python
def url_to_id(string):
    if (m := re.match(
        r"^https://swapi\.dev/api/[^/]+/(\d+)+/$",
        string
    )):
        return m.groups()[0]
    else:
        return string
```

---

# _Exercise 5:_ Cleaning up our data

## Goals

- Map the URL removal over all our data
- Transform from list to dictionary (keyed by ID)
- Rename "url"-field to "id"-field

## Batteries

- `url_to_id` (see previous)
- `isinstance` [(docs)](https://docs.python.org/3/library/functions.html#isinstance)
- `del` [(docs)](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement)
- _dictionary view objects_ [(docs)](https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects)

---

# _Exercise 5:_ Cleaning up our data

## Template

```python
def clean_data(data):
    """Clean up and transform a given data set.

    :param data: Data set to clean and transform
    :type data: list[Any]

    :return: Cleaned and transformed data set.
    :rtype: dict[str, Any]
    """
```

---

# _Exercise 5:_ Cleaning up our data

## Solution

```python
def clean_data(data):
    new = {}
    for obj in objs:
        for key, value in list(obj.items()):
            if isinstance(value, list):  #
                obj[key] = [
                    url_to_id(elem)
                    for elem in value
                ]
            elif key == "url":
                del obj["url"]
                obj["id"] = url_to_id(value)
        new[obj["id"]] = obj
    return new
```

---

# _Exercise 6:_ Doing things in parallel

## Goals

- Do a given task for a set of parameters *"in parallel"*

## Batteries

- `concurrent.futures` [(docs)](https://docs.python.org/3/library/concurrent.futures.html)

> ** ⚠ This is – a lot – more difficult! **

---

# _Exercise 6:_ Doing things in parallel

## Template

```python
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

# _Exercise 6:_ Doing things in parallel

## Solution

```python
def do_parallel(task, args):
    res = {}
    with ThreadPoolExecutor() as pool:
        futs = {
            pool.submit(task, arg): arg
            for arg in args
        }
        for fut in as_completed(futs):
            res[futs[fut]] = fut.result()
    return res
```

---

╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴

# Interlude: the dreaded GIL...

## What?

**GIL**: The Global Interpreter Lock

## What??

Only one thread per process can use the python interpreter at a time!

## What???

Threads in python are good at doing _literally nothing_, i.e. blocking I/O.

╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴

---

# _Exercise 7:_ Loading the entire data set

## Goals

- Download the entire data set based starting from the APIs root

## Batteries

- `download_json` (see previous)
- `download_chain` (see previous)
- `do_parallel` (see previous)
- `clean_data` (see previous)
- `functools` [(docs)](https://docs.python.org/3/library/functools.html)
- `operator` [(docs)](https://docs.python.org/3/library/operator.html)
- *default argument values* [(docs)](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)

---

# _Exercise 7:_ Loading the entire data set

## Template

```python
def download_starwars(root):
    """Download and clean the entire starwars data set.

    :param root: The APIs root url
    :type root: str

    :return: The starwars data set.
    :rtype: Any
    """
```

---

# _Exercise 7:_ Loading the entire data set

## Solution

```python
def download_starwars(root="https://swapi.dev/api"):
    endpoints = download_json(root)
    data = do_parallel(
        partial(
            download_chain,
            itemgetter("next"),
            itemgetter("results")
        ),
        endpoints.values()
    )
    data = {
        name: clean_data(data[endpoint])
        for name, endpoint in endpoints.items()
    }
    return data
```

---

╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴

# Interlude: Mutable Default Arguments...

## What?

Mutable default arguments **do not "reset" after a call**.

```python
def test(arg=[]):
    arg.append(1)
    print(arg)

test()  # → [1]
test()  # → [1,1]
```

## What??

Most common fix:

```python
def test(arg=None)   # ← NEW! ✨
    arg = arg or []  # ← NEW! ✨
    arg.append(1)
    print(arg)
```

╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴

---

# _Exercise 8:_ Loading the entire data set (but less annoying for swapi.dev)

## Goals

- Download the data and store it as a file
- Load the data from a file instead of downloading it if the
  file exists.

## Batteries

- `download_starwars` (see previous)
- `pathlib` [(docs)](https://docs.python.org/3/library/pathlib.html)
- `json` [(docs)](https://docs.python.org/3/library/json.html)
- `open` [(docs)](https://docs.python.org/3/library/functions.html#open)

---

# _Exercise 8:_ Loading the entire data set (but less annoying for swapi.dev)

## Template

```python
def load_starwars(path, root):
    """Download and clean the entire starwars data set.

    :param path: File path to JSON file.
    :type path: str

    :param root: The APIs root url
    :type root: str

    :return: The starwars data set.
    :rtype: Any
    """
```

---

# _Exercise 8:_ Loading the entire data set (but less annoying for swapi.dev)

## Solution

```python
def load_starwars(path="starwars.json", root="https://swapi.dev/api"):
    if Path(path).is_file():
        with open(path, "r") as f:
            return json.load(f)
    else:
        data = download_starwars(root)
        with open(path, "w+") as f:
            json.dump(data, f)
        return data
```

---


# ⏰ Break time!

```
                          ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄▄▄▄ ▄▄▄▄▄▄▄  
                          █ ▄▄▄ █ ▄  ▄▄█▄  ▀█ ▄ █ ▄▄▄ █  
                          █ ███ █ ██▄█ █ █▀▀▀█  █ ███ █  
                          █▄▄▄▄▄█ ▄▀▄ █▀▄ ▄▀█▀█ █▄▄▄▄▄█  
                          ▄▄▄▄  ▄ ▄▀ ▀ ▄▄▀▀███▀▄  ▄▄▄ ▄  
                          ▄▄█▄█▀▄▀▄▀   ▄▀ █ ▄▀█ ███ ▄▄▀  
                           █▄█▀▄▄▀ ▄ █▀██▄█▄▀▄▀▀▀▀▀▄▄ ▀  
                          █▀▄▀██▄ ▀▄█▀▄ █ █▀ ██▄▀█▄ ███  
                          █▀▄██ ▄ ▀ ▄▄▀ ▀▀▀ ▄ █▄▀▀█▄ █   
                          ▄▀▀▄▀ ▄▀██▄▄█ ▀█▄ ▀ ▀▀ █ ▀█▀   
                           ▄▀█▀▀▄▄▄▄▄▄█ █▄▀█▄███▄▄▄▄█    
                          ▄▄▄▄▄▄▄ ▀██▄█▄▄   ▀▄█ ▄ ██▀█▀  
                          █ ▄▄▄ █  ▀▄ ▄▀██▄▄▀ █▄▄▄█▀▄█▄  
                          █ ███ █ █ ▄█▀▄ ▀▀  ▀▀█ ▄▀▀▄ █  
                          █▄▄▄▄▄█ █  ▀  █▄█ ▀██  ▀ █ █   
```

---

# _Exercise 9:_ Who's the longest?!

## Goals

- Get the longest vehicle per class.
- Ignore those with unknown size.

## Batteries

- `max` [(docs)](https://docs.python.org/3/library/functions.html#max)

---

# _Exercise 9:_ Who's the longest?!

## Template

```python
def longest_vehicle(data):
    """Get longest vehicle per class.

    :param data: Starwars dataset

    :return: Vehicles counts per class.
    :rtype: Vehicle
    """
```

**⚠ Types are just to emphasize the exercise!**

---

# _Exercise 9:_ Who's the longest?!

## Solution

```python
def longest_vehicle(data):
    return max(
        (
            vehicle
            for vehicle in data["vehicles"].values()
            if vehicle["length"] != "unknown"
        ),
        key=lambda p: float(p["length"])
    )
```

---

╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴

# Interlude: Generators vs. Lists and the Choice of Comprehensions

## What?

List-Comprehensions create an entirely new list, i.e. they
materialize all results **immediately**.

```python
[ i*i for i in range(1_000_000_000_000) ]
```

## What??

This can and will lead to problems in big data sets!


## What???

Consider the use of Generator(-Comprehension)s for big data
sets!

```python
( i*i for i in range(1_000_000_000_000) )
```

They produce values one after another, considerably
shrinking the memory footprint.

╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴✄╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴

---

# _Exercise 10:_ Who's in what class?

## Goals

- Group all vehicles by their vehicles classes.

## Batteries

- `collections` [(docs)](https://docs.python.org/3/library/collections.html#collections.defaultdict)

---

# _Exercise 10:_ Who's in what class?

## Template

```python
def vehicles_by_class(data):
    """Get all vehicles grouped by their classes.

    :param data: Starwars dataset

    :return: Grouped vehicles
    :rtype: dict[VehicleClass, list[Vehicle]]
    """
```

**⚠ Types are just to emphasize the exercise!**

---

# _Exercise 10:_ Who's in what class?

## Solution

```python
def vehicles_by_class(data):
    res = defaultdict(list)
    for vehicle in data["vehicles"].values():
        res[vehicle["vehicle_class"]].append(vehicle)
    return res
```

---

# _Exercise 11:_ Who's the longest, but per class?!

## Goals

- Get the biggest vehicle per class.
- Ignore those with unknown size.

## Batteries

- `collections` [(docs)](https://docs.python.org/3/library/collections.html#collections.defaultdict)

---

# _Exercise 11:_ Who's the longest, but per class?!

## Template

```python
def longest_vehicle_per_class(data):
    """Get biggest vehicle per class.

    :param data: Starwars dataset

    :return: Vehicles counts per class.
    :rtype: dict[VehicleClass, Vehicle]
    """
```

**⚠ Types are just to emphasize the exercise!**

---

# _Exercise 11:_ Who's the longest, but per class?!

## Solution

```python
def longest_vehicle_per_class(data):
    res = defaultdict(lambda: {"length": "0"})
    for v in data["vehicles"].values():
        vclass = v["vehicle_class"]
        if (
            v["length"] != "unknown"
            and float(v["length"]) > float(res[vclass]["length"])
        ):
            res[vclass] = v
    return res
```

---

# _Exercise 12:_ How many are there?

## Goals

- Count the number of vehicles for all vehicle classes.

## Batteries

- `collections` [(docs)](https://docs.python.org/3/library/collections.html#collections.Counter)

---

# _Exercise 12:_ How many are there?

## Template

```python
def vehicles_per_class(data):
    """Count vehicles by their class.

    :param data: Starwars dataset

    :return: Vehicles counts per class.
    :rtype: dict[VehicleClass, int]
    """
```

**⚠ Types are just to emphasize the exercise!**

---

# _Exercise 12:_ How many are there?

## Solution

```python
def vehicles_per_class(data):
    return Counter(
        v["vehicle_class"]
        for v in data["vehicles"].values()
    )
```

---

# _Exercise 13:_ Group vehicles by films

## Goals

- Get all vehicles grouped by films.
- Use a "human readable" key format
    - e.g. `Episode ⟨𝘌𝘗𝘐𝘚𝘖𝘋𝘌#⟩: ⟨𝘛𝘐𝘛𝘓𝘌⟩`

## Batteries

- `collections` [(docs)](https://docs.python.org/3/library/collections.html#collections.defaultdict)
- *f-strings* [(docs)](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals)

---

# _Exercise 13:_ Group vehicles by films

## Template

```python
def vehicles_by_film(data):
    """Get all characters by film.

    :param data: Starwars dataset

    :return: Vehicles grouped by films.
    :rtype: dict[str, list[Vehicle]]
    """
```

**⚠ Types are just to emphasize the exercise!**

---

# _Exercise 13:_ Group vehicles by films

## Solution

```python
def vehicles_by_film(data):
    res = defaultdict(list)
    for film_id, film in data["films"].items():
        episode = (int(film_id) + 2) % 6 + 1
        key = f"Episode {episode}: {film['title']}"
        for vehicle_id in film["vehicles"]:
            res[key].append(data["vehicles"][vehicle_id])
    return res
```

---

# _Exercise 14:_ Group anything by films

## Goals

- Make the previous exercise more generic.
    - i.e. make it work for people, starships, etc. 

## Batteries

- `vehicles_by_film` (see previous)
- `collections` [(docs)](https://docs.python.org/3/library/collections.html#collections.defaultdict)

---

# _Exercise 14:_ Group anything by films

## Template

```python
def by_film(data, film_field, data_field):
    """Group things by film.

    :param data: Starwars dataset

    :param film_field: Name of "relation" field on a film.
    :type film_field: str

    :param data_field: Name of "data" field in dataset.
    :type data_field: str 

    :return: Things grouped by films.
    :rtype: dict[str, list[Thing]]
    """
```

**⚠ Types are just to emphasize the exercise!**

---

# _Exercise 14:_ Group anything by films

## Solution

```python
def by_film(data, film_field, data_field=None):
    data_field = data_field or film_field
    res = defaultdict(list)
    for film_id, film in data["films"].items():
        episode = (int(film_id) + 2) % 6 + 1
        key = f"Episode {episode}: {film['title']}"
        for vehicle_id in film[film_field]:
            res[key].append(data[data_field][vehicle_id])
    return res
```

---

# _Exercise 15:_ How unique is a category in a film?

## Goals

- Calculate the uniqueness of things in film.
- Show the results per film.

## Batteries

- `by_film` (see previous)
- `collections` [(docs)](https://docs.python.org/3/library/collections.html#collections.defaultdict)
- `statistics` [(docs)](https://docs.python.org/3/library/statistics.html#statistics.mean)
- `decimal` [(docs)](https://docs.python.org/3/library/decimal.html#decimal.Decimal)
- `round` [(docs)](https://docs.python.org/3/library/functions.html#round)

---

# _Exercise 15:_ How unique is a category in a film?

## Template

```python
def uniqueness_per_film(data, film_field, data_field):
    """Get the uniqueness a things in a film by films.

    :param data: Starwars dataset

    :param film_field: Name of "relation" field on a film.
    :type film_field: str

    :param data_field: Name of "data" field in dataset.
    :type data_field: str 

    :return: Uniqueness or things by films.
    :rtype: dict[str, list[Thing]]
    """
```

**⚠ Types are just to emphasize the exercise!**

---

# _Exercise 15:_ How unique is a category in a film?

## Solution

```python
def uniqueness_per_film(data, film_field, data_field=None):
    data_field = data_field or film_field
    return {
        film: round(mean(
            1 / Decimal(len(thing["films"]))
            for thing in things
        ), 2)
        for film, things in by_film(
            data,
            film_field,
            data_field
        ).items()
    }
```

---

# _Exercise 16:_ 𝗙𝗜𝗡𝗔𝗟𝗟𝗬! Which film is the "uniquest"?

## Goals

- Calculate which starwars film is the most unique.

## Batteries

- `uniqueness_per_film` (see previous)
- `max` [(docs)](https://docs.python.org/3/library/functions.html#max)
- *Python's Data Model* [(docs)](https://docs.python.org/3/reference/datamodel.html)

---

# _Exercise 16:_ 𝗙𝗜𝗡𝗔𝗟𝗟𝗬! Which film is the "uniquest"?

## Template

```python
def uniquest_film(data):
    """Get the uniquest film of them all!

    :param data: Starwars dataset

    :return: The name of the uniquest starwars film.
    :rtype: str
    """
```

---

# _Exercise 16:_ 𝗙𝗜𝗡𝗔𝗟𝗟𝗬! Which film is the "uniquest"?

## Solution

```python
def uniquest_film(data):
    inidivdual_uniquenesses = [
        uniqueness_per_film(data, "vehicles"),
        uniqueness_per_film(data, "starships"),
        uniqueness_per_film(data, "planets"),
        uniqueness_per_film(data, "species"),
        uniqueness_per_film(data, "characters", "people"),
    ]
    res = inidivdual_uniquenesses[0]
    for uniquenesses in inidivdual_uniquenesses[1:]:
        for key, value in uniquenesses.items():
            res[key] += value
    return max(
        res.keys(),
        key=res.__getitem__
    )
```
