from typing import Tuple, List, Dict


class Choicify:
    """This is a utility class which returns tuple of choices
    calculates length of individual choices for use in CharField
    """

    def __init__(self, choices: Tuple) -> None:
        self.__choices = sorted(choices)

    def __dictify_choices(self, choices: Tuple) -> Dict:
        "Return length of dict_value for each choices"
        choices_to_dict = dict(choices) # convert tuple to dictionary
        count = {}
        for k, v in choices_to_dict.items():
            count[k] = len(k)
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
        return max(self.__dictify_choices(self.__choices))