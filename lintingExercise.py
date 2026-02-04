# Get 10/10 with pylint on this program.


def count(sequence, item):
  y = 0
  for n in sequence:
    if n == item:
      y += 1
  return y


def count_corrected(sequence, item):
    """Count how many times item appears in sequence."""
    y = 0
    for n in sequence:
        if n == item:
            y += 1
    return y
