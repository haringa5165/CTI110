red = int(input())
green = int(input())
blue = int(input())
smallest_value = 0

if (red < green) and (red < blue):
    smallest_value = red
elif (green < red) and (green < blue):
    smallest_value = green
else:
    smallest_value = blue

no_gray_r = red - smallest_value
no_gray_g = green - smallest_value
no_gray_b = blue - smallest_value

print(no_gray_r, no_gray_g, no_gray_b)
