# RegexBuilder: A functional wrapper for RegEx in Python.

## Installation
```sh
python -m pip install regexbuilder-py
# or
python -m pip install git+https://github.com/AaravMalani/regexbuilder
```

## Usage
```py
print(RegEx().start() \
       .string('http') \
       .chars('s').modify(Modifiers.ZERO_OR_ONE) \
       .string('://') \
       .group(RegEx() 
              .chars('a-zA-Z0-9') \
              .modify(Modifiers.ONE_OR_MORE) \
              .chars(r'.')) \
       .modify(Modifiers.ZERO_OR_MORE) \
       .chars('A-Za-z0-9').modify(Modifiers.ONE_OR_MORE) \
       .chars('.') \
       .chars('A-Za-z').modify(Modifiers.ONE_OR_MORE) \
       .group(RegEx().string('.')).build())
# $(?:http)[s]?(?:://)([a-zA-Z0-9]+[.])*[A-Za-z0-9]+[.][A-Za-z]+((?:.))
```