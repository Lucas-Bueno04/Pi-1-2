from  typing import List
import random

class Randomize:

    @classmethod

    def draw(cls, list:List)->List:

        if len(list) >= 20:
            return random.sample(list, 20)
        
        else:
            return list
