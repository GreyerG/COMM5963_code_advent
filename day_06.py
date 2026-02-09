import numpy as np
def count_light(input_text):
    m=1000
    n=1000
    light = np.zeros((m,n),dtype=int)
    instr = input_text.split('\n')

    for command in instr:
        temp = command.replace('turn on ','').replace('turn off ','').replace('toggle ','').replace(' through ',',').strip()
        print(temp)

        a, b, c, d = map(int, temp.split(','))

        if 'turn off' in command:
            light[a:c+1,b:d+1] = 0
            continue
        elif 'toggle' in command:
            light[a:c + 1, b:d + 1] ^= 1
            continue

        elif 'turn on' in command:
            light[a:c + 1, b:d + 1] = 1
            continue

    print(np.sum(light))


def count_bright(input_text):
    m = 1000
    n = 1000
    light = np.zeros((m, n), dtype=int)
    instr = input_text.split('\n')

    for command in instr:
        temp = command.replace('turn on ', '').replace('turn off ', '').replace('toggle ', '').replace(' through ',',').strip()

        a, b, c, d = map(int, temp.split(','))

        if 'turn off' in command:
            light[a:c+1,b:d+1]-=1
            for i in range(a,c+1):
                for j in range(b,d+1):
                    if light[i,j] < 0:
                        light[i,j] = 0
            continue

        elif 'toggle' in command:
            light[a:c + 1, b:d + 1] += 2
            continue

        elif 'turn on' in command:
            light[a:c + 1, b:d + 1] += 1
            continue
    print(np.sum(light))

if __name__ == '__main__':
    with open('input/day_06.txt','r') as file_object:
        input_text = file_object.read()
        count_light(input_text)
        count_bright(input_text)
