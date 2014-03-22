import sys

class Codec(object):
    def __init__(self):
        self.key_map = [' ', None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.lookup = self.__build_dict__(self.key_map)

    def __build_dict__(self, key_map):
        out_dict = dict()
        for group in key_map:
            if not group:
                continue
            for char in group:
                out_dict[char] = ''.join([str(key_map.index(group)) for x in range(group.index(char) + 1)])
        return out_dict

    def encode(self, message):
        out_code = ''
        previous_code = None
        for char in message:
            code = self.lookup[char]
            if previous_code and previous_code[-1] == code[0]:
                out_code += ' '
            out_code += code
            previous_code = code
        return out_code

a = Codec()

with file(sys.argv[1]) as in_file:
    line_number = 0
    case_number = 0
    for line in in_file:
        line_number += 1
        if line_number == 1:
            total_cases = int(line)
            continue
        case_number += 1
        output = 'Case #' + str(case_number) + ': ' + a.encode(line.strip('\n'))
        print output
        with file('outfile.txt', 'a') as out_file:
            out_file.write(output + '\n')
