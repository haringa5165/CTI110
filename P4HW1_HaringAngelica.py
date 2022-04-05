# CTI-110
# P4HW1 - Score List
# Angelica Haring
# April 5, 2022
#
# Get a number of scores the user would like to enter
# Create a loop to collect the number of scores
# Evaluate every score entered if valid, should be between 0 and 100
# If invalid, print the that it is INVALID and enter the correct score
# If valid scores entered, add score to the list and calculate average score
# Determine the letter grade for the calculated average score
# Print lowest score, score list dropping the lowest score,
#   average score in modified list, and letter grade
#

num_scores = int(input('How many scores do you want to enter? '))
print()
i = 1
total_scores = []

while i<=num_scores:
    print('Enter score',f'#{i}: ',end='')
    score = float(input())

    if score<0 or score>100:
        print()
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
    else:
        total_scores.append(score)
        i += 1
          
lowest_score = min(total_scores)
total_scores.remove(lowest_score)
score_avg = sum(total_scores)/len(total_scores)

if score_avg >= 90:
    grade = 'A'
elif score_avg >= 80:
    grade = 'B'
elif score_avg >= 70:
    grade = 'C'
else:
    grade = 'F'

print()
print()
print('--------------Results-----------')
print('Lowest Score  :', lowest_score)
print('Modified List :', total_scores)
print('Scores Average:', format(score_avg, ',.2f'))
print('Grade         :', grade)
print('----------------------------------')
