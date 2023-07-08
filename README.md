# assign1hackersFindtheRunnerUpScore
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is[2,3,6,6,5] . The maximum score is6 , second maximum is5 . Hence, we print 5 as the runner-up score.
if __name__ == '__main__':
    def functon(op):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        for i in a :
            while a[-1] == i:
                del a[-1]
            op = a
            return max(op)
functon(op)
     
5
1 2 6 5 6
6

def functon(op):
  n = int(input())
  a = list(map(int, input().split()))
  a.sort()
  for i in a :
    while a[-1] == i:
      del i
      op = a
    return max(op)
functon(op)
     
5 
1 2 6 5 6
5
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
     
5 
1 2 6 5 6
5

n = 5
a = map(int, input().split())
list(a).sort()
b,a = set(a),list(b)
a[-2]

