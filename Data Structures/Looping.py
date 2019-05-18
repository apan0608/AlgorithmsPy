
def loop_dict():
    knights = {'gallahad': 'the pire', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)

loop_dict()

def loop_with_enumerate(): 
    print('loop with enumerate')
    for i, v in enumerate(['tie', 'tac', 'toe']):
        print(i, v)

loop_with_enumerate()

def using_zip():
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('what is your {}? It is {}'.format(q, a))

using_zip()

def loop_reverse():
    for i in reversed(range(1, 10, 2)):
        print(i)

loop_reverse()

def loop_sorted():
    for i in sorted(['apple', 'orange', 'apple', 'pear', 'orange']):
        print(i)

loop_sorted() 

string = ''
for i in range(5, 10):
    if i < 10:
        string += ('{} '.format(i))
    else: 
        string += '{}'.format(i)
 
print(string)