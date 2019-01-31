# Price Formatter

One of the frequent tasks in the development of the site - the output on the page of product prices. 
From the database comes a string of the form `3245.000000`.  It is necessary to bring it to a more visual form `3 245`.

The program has two interfaces:

- Software - to use it on the site
- Command Line Interface - to start in manual mode from the console

Code handles incorrect input with returning `None` value.

__Example of command line usage:__

```bash
$ python3 format_price.py 1234.123
1 234.12
```

__Example of usage in your script:__

```python
from format_price import format_price

format_price('3245.678') # 3 245.68
```

You could find more examples in `tests.py` file.

__Run tests:__

To run tests use next command:

`python3 tests.py -v`

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
