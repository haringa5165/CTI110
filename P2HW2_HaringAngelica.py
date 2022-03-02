# CTI-110
# P2HW2 - Score Avg
# Angelica Haring
# March 02, 2022
#
# Get series of seven scores from user
# Program store the scores in a list
# Program calculates the lowest score
# Program will drop lowest score from the list
# Program calculates score average
# Print Lowest Score, Modified List, and Scores Average
#
score_num1 = float(input('Enter score #1: '))
score_num2 = float(input('Enter score #2: '))
score_num3 = float(input('Enter score #3: '))
score_num4 = float(input('Enter score #4: '))
score_num5 = float(input('Enter score #5: '))
score_num6 = float(input('Enter score #6: '))
score_num7 = float(input('Enter score #7: '))
all_scores = [score_num1, score_num2, score_num3, score_num4, score_num5, score_num6, score_num7]
print()
print()
print('--------------Results-----------')
lowest_score = min(all_scores)
print('Lowest Score  :', lowest_score)
all_scores.remove(lowest_score)
print('Modified List :', all_scores)
score_avg = sum(all_scores)/len(all_scores)
print('Scores Average:', format(score_avg, ',.2f'))
print('----------------------------------')
