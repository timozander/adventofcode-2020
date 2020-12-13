from pathlib import Path
import numpy as np

# input_matrix = np.array([list(line) for line in lines])

file = ''
with open('input/' + Path(__file__).stem, "r") as text_file:
    file = text_file.read()

lines = [passport.replace('\n', ' ')
         for passport in file.split('\n\n')]


def combined_question_answers_count(group_str, fn=np.union1d):
    answers = group_str.split(' ')

    answer = list(answers[0])
    for i in range(1, len(answers)):
        answer = fn(answer, list(answers[i]))

    return len(answer)


p1_answers = [combined_question_answers_count(group) for group in lines]
p2_answers = [combined_question_answers_count(
    group, np.intersect1d) for group in lines]

print(f'Part 1: {sum(p1_answers)}')
print(f'Part 2: {sum(p2_answers)}')
