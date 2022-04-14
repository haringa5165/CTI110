def feet_to_steps(user_feet):
    steps = user_feet / 2.5
    return int(steps)

if __name__ == '__main__':
    input_feet = float(input())
    steps = feet_to_steps(input_feet)
    print(int(steps))
    