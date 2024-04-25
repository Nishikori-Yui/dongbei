def print_fibonacci_sequence(n):
    if n < 1:
        raise ValueError("Invalid input! Please enter a positive integer.")

    fibonacci_sequence = []
    current = 0
    next_num = 1

    fibonacci_sequence.append(current + next_num)

    for _ in range(2, n+1):
        current, next_num = next_num, current + next_num
        fibonacci_sequence.append(next_num)

    return ', '.join(map(str, fibonacci_sequence))

print("Checking result for 0:")
try:
    print(print_fibonacci_sequence(0))
except ValueError as e:
    print(e)

print("Checking result for 15:")
print(print_fibonacci_sequence(15))

# 僅供娛樂而沒有完全對應原文的代碼