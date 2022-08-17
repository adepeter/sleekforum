from typing import Tuple, List, Dict, ValuesView


class Choicify:
    """This is a utility class which returns tuple of choices
    calculates length of individual choices for use in CharField
    """

    def __init__(self, choices: Tuple) -> None:
        self.__choices = sorted(choices)

    def __dictify_choices(self, choices: Tuple) -> ValuesView:
        "Return length of dict_value for each choices"
        choices_to_dict = dict(choices) # convert tuple to dictionary
        count = {k: len(k) for k in choices_to_dict}
        return count.values()

    def to_dict(self):
        """Return key: value mapping"""
        return dict(self.__choices)


    @property
    def get_choices(self) -> List:
        "Return list of choice"
        return self.__choices

    def __len__(self) -> int:
        """Returns length of longest choice tuple"""
        return int(max(self.__dictify_choices(self.__choices)))
