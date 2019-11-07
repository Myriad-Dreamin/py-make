# py-make

both python2 or python3 are ok to run this script

# Installation

# Get Started

```python
#!/usr/bin/env python3
from pymake import require, oqs, entry


def mqs(*_):
    print("Hello", end='')

# for shadow everything
class Makefile:

    @classmethod
    @require(mqs, *oqs('start2'))
    def start(cls, *_):
        print("World", end='')

    @classmethod
    def start2(cls, *_):
        print(" ", end='')

    @classmethod
    @require(mqs, *oqs('start', 'start2'))
    def all(cls, *_):
        print("!")

if __name__ == '__main__':
    entry(Makefile)
```

run in bash
```bash
>> ./makefile.py
Hello World!
```
