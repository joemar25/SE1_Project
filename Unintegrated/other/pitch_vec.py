import numpy as np


def pitch_feedback(input_hz: float, min, max):
    if input_hz < min:
        return 'to low'
    if input_hz > max:
        return 'to to high'
    return 'keep it up'


gender: str = 'male'
input_hz: float = 90


ideal_male_hz: list[int] = [85, 180]
ideal_female_hz: list[int] = [165, 255]

if gender[0] == 'm':
    min = ideal_male_hz[0]
    max = ideal_male_hz[1]
else:
    min = ideal_female_hz[0]
    max = ideal_female_hz[1]

mid = (min + max) / 2
if input_hz == mid:
    grade: int = 99
elif input_hz >= min and input_hz <= max:
    grade: int = int(
        mid)-int(input_hz) if input_hz < mid else int(input_hz) - int(mid)
    grade: int = abs(100 - grade)
else:
    grade: int = 0

print(grade)
print(pitch_feedback(input_hz, min, max))

# for data in deduction:
#     low = data[1][0]
#     high = data[1][1]
#     print(f'low = {low} and high = {high}')

# test
# generated deduction
# deduction = 0
# while deduction < 100:
#     print(f'[{deduction}, [{min}, {max}]],')
#     min -= 1
#     max += 1
#     deduction += 1
