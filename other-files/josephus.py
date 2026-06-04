def castInt(i):
    while i != int(i):
        try:
            i = int(i)
        except:
            i = input("Please try a number: ")
    return i

def josephus(n, k):
    if n == 1:
        return 0
    
    return (josephus (n-1, k) + k) % n

p = castInt(input("Number of people: "))
s = castInt(input("Number of steps between kills: "))

print(josephus(p, s))