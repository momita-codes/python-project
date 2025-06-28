def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes = ""
    results = ""

    for i, problem in enumerate(problems):
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_len = max(len(num1), len(num2)) + 2
        top = num1.rjust(max_len)
        bottom = operator + num2.rjust(max_len - 1)
        dash = '-' * max_len

        if operator == '+':
            result = str(int(num1) + int(num2)).rjust(max_len)
        else:
            result = str(int(num1) - int(num2)).rjust(max_len)

        spacer = "    " if i < len(problems) - 1 else ""

        first_line += top + spacer
        second_line += bottom + spacer
        dashes += dash + spacer
        results += result + spacer

    arranged_problems = first_line + "\n" + second_line + "\n" + dashes
    if display_answers:
        arranged_problems += "\n" + results

    return arranged_problems

# Add this at the bottom
if __name__ == "__main__":
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    print(arithmetic_arranger(problems, display_answers=True))
