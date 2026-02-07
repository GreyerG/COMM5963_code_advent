
def count_floor(input_text):
    count = 0
    for char in input_text:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
    print(count)


def count_basement(input_text):
    count = 0
    count_char = 0
    for char in input_text:
        if char == '(':
            count += 1
            count_char += 1
        if char == ')':
            count -= 1
            count_char += 1
        if count == -1:
            break
    print(count_char)

if __name__ == '__main__':
    with open('input/day_01.txt','r') as file_object:
        input_text = file_object.read()
    count_floor(input_text)
    count_basement(input_text)

