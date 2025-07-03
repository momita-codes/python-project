def arithmetic_arranger(problems, answers=False):
    if len(problems) > 3:
        return "Error: Too many problems (maximum is 3)."

    operations = {
        '+': lambda nums: str(nums[0] + nums[1]),
        '-': lambda nums: str(nums[0] - nums[1]),
    }

    first_line = []
    second_line = []
    dashes = []
    answer_line = []

    for expression in problems:
        parts = expression.split()
        if len(parts) != 3:
            return "Error: Each problem must have two operands and an operator."

        operand1, operator, operand2 = parts

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if operator not in operations:
            return "Error: Operator must be '+' or '-'."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2

        first_line.append(operand1.rjust(width))
        second_line.append(operator + ' ' + operand2.rjust(width - 2))
        dashes.append('-' * width)

        if answers:
            result = operations[operator]([int(operand1), int(operand2)])
            answer_line.append(result.rjust(width))

    output = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes)
    if answers:
        output += '\n' + '    '.join(answer_line)

    return output


# --------- MAIN EXECUTION ---------

if __name__ == "__main__":
    print("Enter arithmetic problems separated by comma, semicolon, or space.")
    print("Example: 32+8, 1-3801; 9999+9999 523-49\n")

    raw_input_line = input("Enter problems: ").replace(';', ',').strip()
    raw_expressions = [exp.strip() for exp in raw_input_line.replace(',', ' ').split('  ') if exp.strip()]

    cleaned_problems = []
    for raw in raw_expressions:
        parts = []
        buffer = ''
        for char in raw:
            if char in '+-':
                if buffer:
                    parts.append(buffer.strip())
                parts.append(char)
                buffer = ''
            else:
                buffer += char
        if buffer:
            parts.append(buffer.strip())

        if len(parts) == 3:
            cleaned_problems.append(' '.join(parts))
        else:
            print(f"Skipping malformed input: {raw}")

    if not cleaned_problems:
        print("No valid problems found.")
    else:    
        print("\n Arranged Problems with Answers:\n")
        print(arithmetic_arranger(cleaned_problems, answers=True))
