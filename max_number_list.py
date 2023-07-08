if __name__ == '__main__':
    def function(op):
        n = int(input('10'))
    
        a = list(map(int, input().split()))
        a.sort()
        for i in a :
            while a[-1] == i:
                del a[-1]
            op = a
            return max(op)
function('op')
def functon(op):
  n = int(input())
  a = list(map(int, input().split()))
  a.sort()
  for i in a :
    while a[-1] == i:
      del i
      op = a
    return max(op)
functon('op')
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    lst = list(arr)
    scores = list()

    for i in lst:
        if i not in scores:
            scores.append(i)
        else :
            continue
    ordr = sorted(scores, reverse=True)
    print(ordr[1])
    n = 5
a = map(int, input().split())
list(a).sort()
b,a = set(a),list(a)
a[-2]

