from utils import get_input_file






if __name__ == '__main__':
    contents = get_input_file('10.txt')

    score_dict = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    close_to_open = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    open_to_close = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    complete_score_dict = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    valid_opens = '([{<'
    valid_closes = ')]}>'
    total_syntax_error = 0
    corrupted_lines = []
    completion_scores = []

    for line in contents:
        opens = []
       

        for c in line:
            if c in valid_opens:
                opens.append(c)
            elif c in valid_closes:
                if close_to_open[c] == opens[-1]:
                    opens.pop()
                else:
                    # print(f'Corrupted line found...{c} does not match {opens[-1]}')
                    # print(f'Rejecting line: {line}')
                    # print(f'This error is worth {score_dict[c]}')
                    total_syntax_error += score_dict[c]
                    corrupted_lines.append(line)
                    break
            else:
                # got something unknown
                raise('Received an unknown character: {c}')


    print(f'Total Syntax Error was: {total_syntax_error}')

    for line in corrupted_lines:
        contents.remove(line)

    for line in contents:
        opens = []
       
        for c in line:
            if c in valid_opens:
                opens.append(c)
            elif c in valid_closes:
                if close_to_open[c] == opens[-1]:
                    opens.pop()
                else:
                    print(f'Corrupted line found...{c} does not match {opens[-1]}')
                    print(f'Rejecting line: {line}')
                    raise

            else:
                # got something unknown
                raise('Received an unknown character: {c}')

        # print(f'*******Line complete*********')
        # print(line)
        # print(f'Remaining opens: {"".join(opens)}')
        
        fix = ""
        for c in "".join(opens)[::-1]:
            fix += open_to_close[c]

        completion_score = 0
        # print(f'Fix is: {fix}')

        for c in fix:
            completion_score *= 5
            completion_score += complete_score_dict[c]
        completion_scores.append(completion_score)
        
        # print(f'Score for fix is {completion_score}')
    
    completion_scores.sort()
    print(f'Completion score is: {completion_scores[len(completion_scores) // 2]}')