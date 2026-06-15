import random

a,b=map(int,input().split())
e=int(input())

k = 0
for i in range(100):
    random_roll = random.randint(1, 6)
    print(random_roll, end=f'-{i+1}번째 굴림 ')
    if random_roll % 2 == 0:
        k += b
    else:
        k += a
    if k == e:
        print()
        print(f'{k}로 생존')
        break
    if k > e:
        print()
        print(f'{k}로 사망')
        break
