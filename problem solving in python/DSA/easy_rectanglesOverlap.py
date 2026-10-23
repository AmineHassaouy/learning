# Given two rectangles, find if the given two rectangles overlap or not.
# A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle.
# Two rectangles sharing a side are considered overlapping. (l1[] and r1[] are the extreme points of the first rectangle and l2[] and r2[] are the extreme points of the second rectangle).
def doOverlap(l1, r1, l2, r2):

    # If one rectangle is on left side of other
    if l1[0] > r2[0] or l2[0] > r1[0]:
        return False

    # If one rectangle is above other
    if l1[1] < r2[1] or l2[1] < r1[1]:
        return False

    return True


if __name__ == "__main__":

    # Test Case 1: Overlapping rectangles
    l1, r1, l2, r2 = [0, 10], [10, 0], [5, 5], [15, 0]
    print(str(doOverlap(l1, r1, l2, r2)).lower())

    # Test Case 2: Non-overlapping rectangles
    l3, r3, l4, r4 = [0, 2], [1, 1], [-2, 0], [0, -3]
    print(str(doOverlap(l3, r3, l4, r4)).lower())