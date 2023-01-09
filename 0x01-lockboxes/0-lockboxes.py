#!/usr/bin/python3
""" method that determines if all the boxes can be opened; """


def canUnlockAll(boxes):
    """eturn True if all boxes can
        be opened, else return False.
    """
    unlocked = [0]  # la première boîte (numéro 0) est déverrouillée
    while True:
        new_boxes = []
        for box in unlocked:
            for key in boxes[box]:
                if key not in unlocked:
                    new_boxes.append(key)
        if not new_boxes:
            break
        unlocked.extend(new_boxes)
    return len(unlocked) == len(boxes)
