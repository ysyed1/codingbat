def lone_sum(a, b, c):
    """Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum."""
    l = [a, b, c]
    result = 0
    for x in l:
        if l.count(x) == 1:
            result += x
    return result

def lone_sum(a, b, c):
  if a == b == c:
    return 0
  if b == c:
    return a
  if a == c:
    return b
  if a == b:
    return c  
  return a + b + c


print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))
