"""
Floyd's Tortoise and Hare algorithm
modified from https://kimsereylam.com/racket/python/2019/03/06/cycle-detection-with-floyd-tortoise-and-hare.html
designed for cycle detection

Input: list of edges
Output: whether or not there is a cycle
"""

N = int(input())
nodes = [(tuple(map(int,input().split()))) for _ in range(N-1)]

def next(parent):
  """
  Finding and updating the pointers with their next node
  """
  def find(nodes, parent):
    if (len(nodes) == 0):
        return None
    current = nodes[0]
    rest = nodes[1:]

    if current and current[0] == parent:
      return current[1]
    else:
      return find(rest, parent)
  return find(nodes, parent) 

def next_next(x):
  return next(next(x))

def meet(slow, fast, p1, p2, steps):
  """
  Define two pointers moving at different speeds.
  If these two pointers meet at a node, there is a cycle formed
  """
  p1 = slow(p1)
  p2 = fast(p2)
  steps = steps + 1

  if p1 == p2:
    return (p1, steps)
  else:
    return meet(slow, fast, p1, p2, steps)

def meet_result(slow, fast, p1, p2):
    result = meet(slow, fast, p1, p2, 0)
    if result[0] is not None:
        return "Yes"
    else:
        return "No"

print(meet_result(next, next_next, 1, 1))
