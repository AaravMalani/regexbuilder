import regexbuilder
import re
def test_1():
    assert re.search(regexbuilder.RegExBuilder().chars('abc').build(), 'dabc')
    assert re.search(regexbuilder.RegExBuilder().string('http').chars('s').modify(regexbuilder.Modifiers.ZERO_OR_ONE).string('://').group(regexbuilder.RegExBuilder().chars('a-zA-Z0-9').modify(regexbuilder.Modifiers.ONE_OR_MORE).chars(r'.')).modify(regexbuilder.Modifiers.ZERO_OR_MORE).chars('A-Za-z0-9').modify(regexbuilder.Modifiers.ONE_OR_MORE).chars('.').chars('A-Za-z').modify(regexbuilder.Modifiers.ONE_OR_MORE).group(regexbuilder.RegExBuilder().string('.').modify(regexbuilder.Modifiers.ZERO_OR_MORE)).build(), 'https://en.wikipedia.google.com/path')
    
