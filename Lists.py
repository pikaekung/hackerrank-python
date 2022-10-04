input = [['insert', '0', '5'],
         ['insert', '1', '10'],
         ['insert', '0', '6'],
         ['print'],
         ['remove', '6'],
         ['append', '9'],
         ['append', '1'],
         ['sort'],
         ['print'],
         ['pop'],
         ['reverse'],
         ['print']]

arr = []
for i in range(len(input)):
    cmd = input[i][0]
    if cmd == 'insert':
        index = int(input[i][1])
        value = int(input[i][2])
        arr.insert(index, value)
    elif cmd == 'remove':
        index = int(input[i][1])
        arr.remove(index)
    elif cmd == 'append':
        value = int(input[i][1])
        arr.append(value)
    elif cmd == 'sort':
        arr.sort()
    elif cmd == 'pop':
        arr.pop()
    elif cmd == 'reverse':
        arr.reverse()
    elif cmd == 'print':
        print(arr)
