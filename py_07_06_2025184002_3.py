
votes = [0]*15
total_votes = 0
while True:
    try:
        number = int(input())
    except:
        break
    if number == 0:
        break
    elif 1<= number <=15:
        votes[number-1]+=1
        total_votes+=1
print(f'Total votes: {total_votes}')
for i in range( 15):
    if votes[i]>0:
        rate =votes[i]/total_votes*100
    print(f'# {i+1:2d} {votes[i]:7d} {rate:6.3f}')