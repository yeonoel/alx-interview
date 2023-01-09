#!/usr/bin/python3
""" method that determines if all the boxes can be opened; """


def canUnlockAll(boxes):
    """eturn True if all boxes can
        be opened, else return False.
    """
    n = len(boxes)
    keys = boxes[0]
    Locked_box = [False] + [True] * (n - 1)
    for key in keys:
        if ((key < n)) and (Locked_box[key] is True):
            Locked_box[key] = False
            keys.extend(boxes[key])
    return not any(Locked_box)
