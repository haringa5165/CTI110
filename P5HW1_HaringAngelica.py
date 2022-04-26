# Program collects number of scores and determine the letter grade for average score
# April 26, 2022
# CTI-110 P5HW1 - Score List
# Angelica Haring
#
# Get a number of scores the user would like to enter
# Create a function to collect the number of scores
# Create another function to drop lowest score and determine the average and letter grade
# Evaluate every score entered if valid, should be between 0 and 100
# If invalid, print the that it is INVALID and enter the correct score
# If valid scores entered, add score to the list and calculate average score
# Determine the letter grade for the calculated average score
# Print lowest score, score list dropping the lowest score,
#   average score in modified list, and letter grade
# Create program Menu Driven, asking user to make a choice
#
def collect_scores(x):
    total_score=[]
    for i in range(1,x+1):
        valid_score=int(input(f'Enter Score #{i}: '))
        if valid_score>=0 and valid_score<=100:
            total_score.append(valid_score)
        else:
            while valid_score<0 or valid_score>100:
                print('INVALID Score entered!!!!')
                print('Score should be between 0 and 100')
                valid_score=int(input(f'Enter Score #{i} '))
    return total_score

def evaluate(total_scores):
    print('')
    print('--------------Results-----------')
    lowest_score = min(total_scores)
    print('Lowest Score  :', format(lowest_score, ',.1f'))
    total_scores.remove(lowest_score)
    print('Modified List :', total_scores)
    score_avg = sum(total_scores)/len(total_scores)
    print('Scores Average:',f'{score_avg:.2f}')

    if score_avg >= 90:
        grade = 'A'
    elif score_avg >= 80:
        grade = 'B'
    elif score_avg >= 70:
        grade = 'C'
    elif score_avg >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print('Grade         :', grade)
    print('----------------------------------')  
    
while True:
    print('')
    print('----------MENU------------')
    print('1) Create Score List')
    print('2) Display Results')
    print('3) Exit')
    print('--------------------------')
    print('')
    choice1 = int(input('Enter choice: '))
        
    if choice1 == 1:
        n=int(input('How many scores do you want to enter? '))
        print('')
        total_scores=collect_scores(n)
        print('')
        print('----------MENU------------')
        print('1) Create Score List')
        print('2) Display Results')
        print('3) Exit')
        print('--------------------------')

        print('')
        choice2 = int(input('Enter choice: '))
        if choice2 == 1:
            print('List already created')
        elif choice2 == 2:
            evaluate(total_scores)
        else:
            print('')
            print('Program terminating....')
            print('Good Bye!')
            break

    elif choice1 == 2:
        print('Create list first')
        print('')

    elif choice1 == 3:
        print('')
        print('Program terminating....')
        print('Good Bye!')
        break

    else:
        print('')
        print('INVALID choice entered !!!!!')
        print('Choose from menu options please')
    

    
