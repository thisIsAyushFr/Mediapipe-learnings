'''Write a small program with:

landmarks = [
    (0.52, 0.91),
    (0.50, 0.85),
    (0.48, 0.80),
    (0.45, 0.75),
    (0.42, 0.70)
]

Then:

Store landmarks[4] in a variable named thumb_tip.
Print the whole tuple.
Print only the X-coordinate.
Print only the Y-coordinate.'''

landmarks = [
    (0.52, 0.91),
    (0.50, 0.85),
    (0.48, 0.80),
    (0.45, 0.75),
    (0.42, 0.70)
]

thumb_tip = landmarks[4]

print(thumb_tip)
print(thumb_tip[0])
print(thumb_tip[1])