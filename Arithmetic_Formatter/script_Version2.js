function arithmeticArranger(problems, displayAnswers = false) {
  if (problems.length > 5) {
    return "Error: Too many problems.";
  }

  let firstLine = '';
  let secondLine = '';
  let dashes = '';
  let results = '';

  for (let i = 0; i < problems.length; i++) {
    let problem = problems[i].trim();
    if (!problem) continue;
    let parts = problem.split(/\s+/);

    if (parts.length !== 3) {
      return "Error: Invalid problem format.";
    }

    let [num1, operator, num2] = parts;

    if (!['+', '-'].includes(operator)) {
      return "Error: Operator must be '+' or '-'.";
    }

    if (!/^\d+$/.test(num1) || !/^\d+$/.test(num2)) {
      return "Error: Numbers must only contain digits.";
    }

    if (num1.length > 4 || num2.length > 4) {
      return "Error: Numbers cannot be more than four digits.";
    }

    let maxLen = Math.max(num1.length, num2.length) + 2;
    let top = num1.padStart(maxLen, ' ');
    let bottom = operator + num2.padStart(maxLen - 1, ' ');
    let dash = '-'.repeat(maxLen);

    let result;
    if (operator === '+') {
      result = String(Number(num1) + Number(num2)).padStart(maxLen, ' ');
    } else {
      result = String(Number(num1) - Number(num2)).padStart(maxLen, ' ');
    }

    let spacer = (i < problems.length - 1) ? '    ' : '';

    firstLine += top + spacer;
    secondLine += bottom + spacer;
    dashes += dash + spacer;
    results += result + spacer;
  }

  let arranged = firstLine + '\n' + secondLine + '\n' + dashes;
  if (displayAnswers) {
    arranged += '\n' + results;
  }

  return arranged;
}

document.getElementById('arrangerForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const lines = document.getElementById('problems').value.trim().split('\n').filter(Boolean);
  const showAnswers = document.getElementById('showAnswers').checked;
  const output = arithmeticArranger(lines, showAnswers);
  document.getElementById('output').innerText = output;
});