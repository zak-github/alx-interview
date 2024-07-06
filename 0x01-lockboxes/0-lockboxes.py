#!/usr/bin/python3
"""lockboxes
"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened
    """

    available_boxes = list(range(len(boxes)))
    visited_boxes = []
    queue = [0]

    while len(queue) != 0:
        key = queue.pop(0)

        # Check if key has a box
        if key in available_boxes:
            if key in visited_boxes:
                # skip key
                continue
            else:
                # Add keys in the box to queue
                queue.extend(boxes[key])
                visited_boxes.append(key)
        else:
            # skip key
            continue

        # optimise by checking if all boxes have been unlocked
        # but queue is not empty
        if (set(visited_boxes) == set(available_boxes)):
            return True

    return set(visited_boxes) == set(available_boxes)
