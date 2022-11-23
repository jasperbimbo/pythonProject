# Function  that  removes  repeated  characters from a string
from collections import OrderedDict


def remove_repeat_character(str):

        result = "".join(OrderedDict.fromkeys(str))

        print("Repeated Character has been removed:", result)


remove_repeat_character("Hello")
remove_repeat_character("Concatenate")