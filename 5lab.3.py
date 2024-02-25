def brackets(s):
    m = 0
    for c in s:
        if c == '(':
            m += 1
        elif c == ')':
            m -= 1
        if m < 0:
            return False
        if c == '{':
            m += 1
        elif c == '}':
            m -= 1
        if m < 0:
            return False
        if c == '[':
            m += 1
        elif c == ']':
            m -= 1
        if m < 0:
            return False
        if c == '<':
            m += 1
        elif c == '>':
            m -= 1
        if m < 0:
            return False
    return m == 0
