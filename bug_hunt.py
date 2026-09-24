
count = 1
total = 0

# BUG: Added the missing colon (:) after the while condition.
# The while statement must end with a colon.
while count <= 5:

    # BUG: The original condition was count < 5, which stopped at 4.
    # Changed it to count <= 5 so that 5 is included in the sum.
    total = total + count
    count = count + 1

# BUG: total is an integer, so it must be converted to a string
# before joining it with the text using +.
print("Sum of 1 to 5 is: " + str(total))