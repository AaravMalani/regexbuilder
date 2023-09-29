from __future__ import annotations
import typing

class Modifiers:
    """A class containing RegEx modifiers"""
    ZERO_OR_MORE = '*' # Matches zero or more times (greedy)
    ONE_OR_MORE = '+' # Matches one or more times (greedy)
    ZERO_OR_ONE = '?' # Matches zero or one time (lazy)
    LAZY = '?' # Used after ZERO_OR_MORE or ONE_OR_MORE to make it lazy (match as few as possible).

class RegExBuilder:
    """The RegEx wrapper"""
    def __init__(self):
        self.__string = ''
        pass
    def start(self):
        """Set the position to the start of the string"""
        self.__string+='^'
        return self
    def end(self):
        """Set the position to the end of the string"""
        self.__string+='$'
        return self
    def group(self, regex : typing.Union[RegExBuilder, str], name : typing.Optional[str] = None, capturing: bool=True):
        """Add a group to the RegEx

        Args:
            regex (typing.Union[RegExBuilder, str]): The group's RegEx (either a RegExBuilder object or a string)
            name (typing.Optional[str], optional): The group's name (not set by default).
            capturing (bool, optional): True if the group is capturing. Defaults to True.
        """
        self.__string+='('
        if name:
            self.__string+=f'?<{name}>'
        elif not capturing:
            self.__string+='?:'
        
        if type(regex) is type(self):
            self.__string+= regex.build()
        else:
            self.__string+= regex
        self.__string+=')'
            
        return self
    def count(self, count: typing.Union[int, range, typing.Iterable[int], typing.SupportsIndex[int]]):
        """Sets the number of times the previous token (group or character) should appear

        Args:
            count (typing.Union[int, range, typing.Iterable[int], typing.SupportsIndex[int]]): The number of times the previous token should appear (A fixed number of times for an int, A number of times in the range of two fixed points if an iterable with two elements or a range is passed, or a number of times greater than a number if an iterable with one element is passed)
        """
        if type(count) is range:
            self.__string+='{'+str(count.start) + ', ' + str(count.stop)+'}'
        elif hasattr(count, '__index__'):
            if len(count) == 1:
                self.__string+='{'+str(count[0])+'}'
            else:
                self.__string+='{'+str(count[0])+', '+str(count[1])+ '}'
        elif hasattr(count, '__iter__'):
            self.__string+='\{' + str(next(count))+','
            try:
                self.__string+=' '+str(next(count))+'}'
            except StopIteration:
                self.__string+='}'
        else:
            self.__string+='{' + str(count) + '}'
            
        return self
    def modify(self, modifier : str):
        """Adds a modifier to the previous token (group or character).

        Args:
            modifier (str): The modifier (from regexbuilder.Modifiers)
        """
        self.__string+=modifier
        return self
    def either(self, re1: typing.Union[RegExBuilder, str], re2: typing.Union[RegExBuilder, str]):
        """Matches if either of the RegExs match (Disjunction)

        Args:
            re1 (typing.Union[RegExBuilder, str]): The first RegEx
            re2 (typing.Union[RegExBuilder, str]): The second RegEx

        Returns:
            _type_: _description_
        """
        re1 = re1.build() if type(re1) is type(self) else re1
        re2 = re2.build() if type(re2) is type(self) else re2

        self.__string+= '(?:'+re1+')|(?:'+re2+')'
        return self
    def chars(self, chars : str, invert: bool =False):
        """Matches if the next character to check in the string is in the list of characters in the "chars" argument.

        Args:
            chars (str): The list of characters to check for in the next character of the string (eg. a-zA-Z0-9 or abc)
            invert (bool, optional): If true, the RegEx matches if the next character is not in the list of characters. Defaults to False.
        """
        if not chars:
            self.__string+='.'
            return self
        if invert:
            self.__string+=f'[^{chars}]'
        else:
            self.__string+=f'[{chars}]'
        return self
    def string(self, string: str):
        """Matches if the remaining part of the string to check exactly starts with the given string

        Args:
            string (str): The string to check with
        """
        self.__string+='(?:'+string+')'
        return self
    
            
    def build(self) -> str:
        """Returns the RegEx

        Returns:
            str: Returns the final regular expression in a string form
        """
        return self.__string