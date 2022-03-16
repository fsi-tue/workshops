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
      > **⏰ This should take at most  5 minutes!**
   2. Introduce the required libraries and read through
      their documentation together with the participants.
      > **⏰ This should take at most 10 minutes!**
   3. Show the template and let the participants play with
      the problem a bit.
      > **⏰ This should take at most 10 minutes!**
   4. Demonstrate how *you* would have done it; or at least
      how the provided solutions do it.
      > **⏰ This should take at most 10 minutes!**

Each exercise should take **at most 35 minutes**! But most
will be shorter. 😉

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

### Exercise 01: Downloading things...

- Introduce the [Star Wars API](https://swapi.dev).
- Show `urllib` and dive into `urllib.request`
- Briefly discuss *context mangers*
- Show `json`

### Exercise 02: Downloading *complicated* things...

- Show the linked list result style of the API

### Exercise 03: Downloading *complicated* things... (but more generic)

- Briefly discuss *higher order functions*

### Exercise 04: Do things in parallel

- Briefly discuss the nature of computationally disjointed
  tasks
- Show `concurrent.futures` (stop shortly before the
  spoiling example, those who find it will have it easier
  but that's the point: #rtfm)

### GIL Interlude

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

### Exercise 05: Loading the entire data set

- now join together all the parts from before
- instead of writing `lambda`-functions directly show the
  participants the `functools` and `operator` libraries
- **This exercise will take longer than the preceding ones!**

### ⏰ Break

- *The QR Code is a rick roll. Keep that in mind...*