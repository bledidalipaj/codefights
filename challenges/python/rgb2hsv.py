"""
Given some color in the rgb format, your task is to convert it into the hsv format. The result should be an array of three formatted numbers, where:

the first number is the Hue value rounded to the nearest integer;
the second number is the Saturation value in percent rounded to the 10th place;
the third number is the Value value in percent rounded to the 10th place.
Example

For rgb = [200, 125, 100], the output should be
rgb2hsv(rgb) = ["15", "50.0", "78.4"].

Input/Output

[time limit] 4000ms (py)
[input] array.integer rgb

An array of three integers representing the R, G, and B values of the color, respectively.

Constraints:
rgb.length = 3,
0 ≤ rgb[i] ≤ 255.

[output] array.string

An array of 3 strings representing the color in the HSV format as described above.

# Challenge' link: https://codefights.com/challenge/pESxR7nBYFjtZFWjk #
# How to convert rgb to hsv http://www.rapidtables.com/convert/color/rgb-to-hsv.htm #
"""
def rgb2hsv(rgb):
    r, g, b = map(float, rgb)
    r_prime = r / 255
    g_prime = g / 255
    b_prime = b / 255
    
    c_max = max(r_prime, g_prime, b_prime)
    c_min = min(r_prime, g_prime, b_prime)
    delta = c_max - c_min
    
    # hue calculation
    if delta == 0:
        hue = 0
    elif c_max == r_prime:
        hue = 0.6 * (((g_prime - b_prime) / delta) % 6)
    elif c_max == g_prime:
        hue = 0.6 * ((b_prime - r_prime) / delta + 2)
    else:
        hue = 0.6 * ((r_prime - g_prime) / delta + 4)
    hue *= 100
        
    # saturation calculation
    if c_max == 0:
        saturation = 0
    else:
        saturation = delta / c_max
    saturation *= 100
    
    value = c_max * 100
    return  ['{:.0f}'.format(hue), '{:.1f}'.format(saturation), '{:.1f}'.format(value)]