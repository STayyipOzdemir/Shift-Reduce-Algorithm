def get_input():
    text = input("Enter a string: ")
    return text.replace(" ", "")

def apply_rule(stack, rule_num):
    if rule_num == 6:
        index = stack.index('id')
        stack[index] = 'F'
    elif rule_num == 5:
        index = stack.index('(')
        stack[index:index + 5] = ['F']
    elif rule_num == 4:
        index = stack.index('F')
        stack[index] = 'T'
    elif rule_num == 3:
        index = stack.index('T')
        stack[index:index + 5] = ['T']
    elif rule_num == 2:
        index = stack.index('T')
        stack[index] = 'E'
    elif rule_num == 1:
        index = stack.index('E')
        stack[index:index + 5] = ['E']

def parse(input_string, tablo_parse, kural_reduce):
    tokens = [char if char != 'i' else 'id' for char in input_string if char != 'd']
    stack = [0]
    i = 0
    cikti = ""

    while stack[0] != 'acc':
        top = stack[-1]
        token = tokens[i] if i < len(tokens) else '$'

        if token not in tablo_parse[top]:
            print("INVALID string entered. SYNTAX ERROR!")
            return

        a = tablo_parse[top][token]

        if a[0] == "s":
            stack.extend([token, int(a[1:])])
            cikti += token + " "
            i += 1
        elif a[0] == "r":
            rule_num = int(a[1:])
            stack.pop()
            apply_rule(stack, rule_num)
            kural_reduce_result = kural_reduce[stack[-2]][stack[-1]]
            stack.append(kural_reduce_result)
        elif a == 'acc':
            print("VALID string entered. ACCEPTED!")
            return
        else:
            print("INVALID string entered. SYNTAX ERROR!")
            return
    print(cikti)
if __name__ == "__main__":
    tablo_parse = {
        0: {'id': 's5', '(': 's4'},
        1: {'+': 's6', '$': 'acc'},
        2: {'+': 'r2', '*': 's7', ')': 'r2', '$': 'r2'},
        3: {'+': 'r4', '*': 'r4', ')': 'r4', '$': 'r4'},
        4: {'id': 's5', '(': 's4'},
        5: {'+': 'r6', '*': 'r6', ')': 'r6', '$': 'r6'},
        6: {'id': 's5', '(': 's4'},
        7: {'id': 's5', '(': 's4'},
        8: {'+': 's6', ')': 's11'},
        9: {'+': 'r1', '*': 's7', ')': 'r1', '$': 'r1'},
        10: {'+': 'r3', '*': 'r3', ')': 'r3', '$': 'r3'},
        11: {'+': 'r5', '*': 'r5', ')': 'r5', '$': 'r5'}
    }
    kural_reduce = {
        0: {'E': 1, 'T': 2, 'F': 3},
        4: {'E': 8, 'T': 2, 'F': 3},
        6: {'T': 9, 'F': 3},
        7: {'F': 10}
    }
    input_text = get_input()
    parse(input_text, tablo_parse, kural_reduce)
