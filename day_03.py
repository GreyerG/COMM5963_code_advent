def count_loc(input_text):
    x,y = 0,0
    s_loc = set()
    s_loc.add((0,0))
    for char in input_text:
        if char == '^':
            y += 1
        if char == 'v':
            y -= 1
        if char == '>':
            x += 1
        if char == '<':
            x -= 1
        s_loc.add((x,y))
    print (len(s_loc))


def count_sr_loc(input_text):
    x_s, y_s = 0, 0
    x_r, y_r = 0, 0
    s_loc = set()
    r_loc = set()
    s_loc.add((0,0))
    r_loc.add((0,0))
    santa = 1
    robot = 0
    for char in input_text:
        if santa == 1 :
            if char == '^':
                y_s += 1
            if char == 'v':
                y_s -= 1
            if char == '>':
                x_s += 1
            if char == '<':
                x_s -= 1
            s_loc.add((x_s, y_s))
            santa = 0
            robot = 1
            continue
        if robot == 1 :
            if char == '^':
                y_r += 1
            if char == 'v':
                y_r -= 1
            if char == '>':
                x_r += 1
            if char == '<':
                x_r -= 1
            r_loc.add((x_r, y_r))
            santa = 1
            robot = 0
            continue
    print(len(s_loc | r_loc))


if __name__ == '__main__':
    with open('input/day_03.txt','r') as file_object:
        input_text = file_object.read()
        count_loc(input_text)
        count_sr_loc(input_text)