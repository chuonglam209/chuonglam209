n = 2
a = n*[0]
def print_board(b):
   l = len(b)
   for i in range(l):
      for j in range(l):
         if j == a[i]:
            print(1, end = " ")
         else:
            print(0, end = " ")
      print()
def possible(d, c):
   for i in range(d):
      # if a[i] == y or abs(i - x) == abs(a[i] - y):
      if a[i] == c  or c - d == a[i] - i or c + d == a[i] + i:
         return False
   return True
def gen(i, n):
   for j in range(n):
      if possible(i,j):
         a[i] = j
         if i == n - 1:
            print(a)
         gen(i+1, n)
gen(0, n)