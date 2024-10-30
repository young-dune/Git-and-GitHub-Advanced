A, B = map(int, input().split())
result = A*B

#유클리드 호제법
while B:
    if A > B:
        A, B = B, A
    B %= A

print(result // A)