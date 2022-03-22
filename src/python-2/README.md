Python Basics: Batteries included! 🔋🔋🔋
=========================================

_Author(s): timfi (SS22)_

This is a 2.5-3h exploration of the python standard library
in a workshop format. The core idea is to demonstrate the
both the depth and breath of the pythons batteries to the
participants. To achieve this the workshop uses the
[Star Wars API](https://swapi.dev) as a running example.

How to workshop
---------------

This workshop is split in to 3 (4 if you're fast) parts:

1. the introduction
2. data acquisition
3. data munging and exploration
4. building a CLI

The 3 latter segments have for easier and maybe even cleaner
counter parts in the python ecosystem, but the standard
library can do quite a bit on its own. They are built up as
follows:

1. Introduce the general segment, i.e. what is data
   acquisition and its possible technologies.
2. Do the segments exercises as follows:
   1. Introduce the exercise as a high level task.
      > **⏰ This should take at most 1-2 minutes!**
   2. Introduce the required libraries and read through
      their documentation together with the participants.
      > **⏰ This should take at most 5 minutes!**
   3. Show the template and let the participants play with
      the problem a bit.
      > **⏰ This should take at most 5 minutes!**
   4. Demonstrate how *you* would have done it; or at least
      how the provided solutions do it.
      > **⏰ This should take at most 5 minutes!**

Each exercise should take **at most 15 minutes**! But most
will be shorter. 😉 This is still a very tight schedule. If
the need arises you can – and be should – speed through some
of the easier exercises. Some candidates for this would be
01, 03, 06, 11, 12, and 14. They are marked with ⏭ in the
speaker notes below.

How to slides?!
---------------

The slides are built as a single markdown file which is
intended for use with [lookatme](https://pypi.org/project/lookatme/). But you can also
render them to HTML or PDF using [pandoc](https://pandoc.org/).
If you are to lazy to lookup the proper options for either
just use the provided `Makefile`…

**⚠ The PDF version is a bit wonky...**

Exercise Notes
--------------

### _Exercise 01:_ Downloading things... ⏭

- Introduce the [Star Wars API](https://swapi.dev).
- Show `urllib` and dive into `urllib.request`
- Briefly discuss *context mangers*
- Show `json`

### _Exercise 02:_ Downloading *complicated* things...

- Show the linked list result style of the API

### _Exercise 03:_ Downloading *complicated* things... (but more generic) ⏭

- Briefly discuss *higher order functions*

### _Exercise 04:_ URLs are ugly data...

- Briefly introduce `re` and focus a bit on capture groups
  (Do not introduce *all of regexs*, pleas just don't...)
- Show them `^https://swapi\.dev/api/[^/]+/(\d+)/$` and be
  done with it. ([demo](https://regexr.com/6hr3t))

### _Exercise 05:_ Cleaning up our data

- Briefly mention duck-typing and show them `isinstance`
- Discuss the _dictionary view objects_ and them "locking"
  the keys and size of a dictionary during iteration.
  (Escape this via `list(...)`!)
- Show them `del`!

### _Exercise 06:_ Doing things in parallel ⏭

- Briefly discuss the nature of computationally disjointed
  tasks
- Show `concurrent.futures` (stop shortly before the
  spoiling example, those who find it will have it easier
  but that's the point: #rtfm)

### _Interlude:_ the dreaded GIL...

- What is the GIL?
    - Global Interpreter Lock
    - Only one thread can use the python interpreter at a
      time.
- What does the GIL mean for threading in python?
    - Python threads in the same process can't run in
      parallel!
    - Multi-processing is recommended for CPU-bound work.
- Why does the GIL exist?
    - Because it makes the interpreter a lot easier to
      reason about!
- What are python threads actually still good for?
    - *Nothing*! Literally, they are masters at waiting
      around and doing basically nothing. Perfect for
      multiple potentially long running network requests!

### _Exercise 07:_ Loading the entire data set

- now join together all the parts from before
- instead of writing `lambda`-functions directly show the
  participants the `functools` and `operator` libraries
- show them default argument values

### _Interlude:_ Mutable Default Arguments...

- Show them the problem of using for example a list-object
  as a default argument.
- Show remedy via default `None`-values.
  (`arg = arg or ⟨default⟩`!)

### _Exercise 08:_ Loading the entire data set (but less annoying for swapi.dev)

- Briefly introduce file-I/O via `open`
- Show `json.load` and `json.dump` (notice the missing `s`
  at the end of each!)


### ⏰ Break

- *The QR Code is a rick roll. Keep that in mind...*

### _Exercise 09:_ Who's the longest?!

- Demonstrate `max` and "`argmax`" (i.e. `max(..., key=...)`)

### _Interlude:_ Generators vs. Lists and the Choice of Comprehensions

- List-Comprehensions materialize the whole result
- Generator-Comprehensions don't.
- Generators ≠ Lists!
- Generators are "special", i.e. they need to be "driven"
  externally through things like `for`-loops.

### _Exercise 10:_ Who's in what class?

- Grouping in linear time via dictionary of lists.
- During solution touch on `itertools.groupby` and its
  limitations; it only works properly on sorted iterables!

### _Exercise 11:_ Who's the longest, but per class?! ⏭

- Discuss the possibility of merging the solutions of
  exercises 09 and 10 and the runtime issues for large
  data sets this would produce.
- Instead show the participants the linear time solution.
- In conjunction show that `collections.defaultdict`
  strictly speaking doesn't take a type as an argument but
  rather a 0-ary "constructor function"!

### _Exercise 12:_ How many are there? ⏭

- Show the base "constructor" for `int`, i.e. `int() == 0`.
- Hit them with the switch-up, i.e. this is so common that
  there is a default implementation for this:
  `collections.Counter`.
- Briefly demonstrate the `Counter.most_common` method.

### _Exercise 13:_ Group vehicles by films

- Tell the participants that this exercise is why we moved
  from a list to dictionary for our data sets (direct access
  to elements via their ID!).
- Show the participants the required logic for getting the
  episode number from the ID: `(ID + 2) % 6 + 1`.

### _Exercise 14:_ Group anything by films ⏭

- This requires minimal changes to the previous exercise!
- Highlight those changes and default one of the two
  arguments!

### _Exercise 15:_ How unique is a category in a film?

- Discuss a possible measure of uniqueness of an object:
  `1 / ⟨number of films it appears in⟩`.
- Show them the `statistics.mean` method and mention that it
  is a performance tuned version that is type aware.
- Discuss floating point errors and move their attention to
  the `decimal` module.

### _Exercise 16:_ **FINALLY!** Which film is the "uniquest"?

- Tell the participants the formula for the uniqueness of a
  movie: `∑ₖ ⟨mean uniqueness of objects in category 𝑘⟩`.
- The solution should be:
  > "Episode 3: The Revenge of the Sith".