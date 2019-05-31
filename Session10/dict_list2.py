ques1={
    'question': 'How many legs does an octopus have?',
    'A': '5 legs', 
    'B': '6 legs', 
    'C': '7 legs', 
    'D': '8 legs',
}
ques2={
    'question': 'How many nations in the world?',
    'A': 150,
    'B': 200,
    'C': 250,
    'D': 300,
}
quiz= [ques1, ques2]
point = 0

# for i in range(len(quiz)-1):
for i in ques1.values():
    print(i)
n= int(input('Your Answer: '))
if n == 8:
    print('You Are Right')
    point += 1
else:
    print('Try Again Later')

for i in ques2.values():
    print(i)
m= int(input('Your Answer: '))
if m == 250:
    print('You Are Right')
    point += 1
else:
    print('Try Again Later')


print('-'*15)
print('Bạn đúng: ', (point/2)*100, '%')
print('Your Score: ',point)