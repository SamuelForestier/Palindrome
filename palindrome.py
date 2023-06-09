import time

start_time = time.time()


def is_palindrome(product):
    """
    Checks if the given number is a palindrome.

    Args:
        product (int): The number to check for palindrome.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    return str(product) == str(product)[::-1]


def generate_palindrome(limit=999):
    """
    Generates the largest palindrome that can be made from the product of four 4-digit numbers
    that are greater than or equal to the limit.

    Args:
        limit (int): The minimum 4-digit number to consider for the product. Default is 1000.

    Returns:
        int: The largest palindrome made from the product of four 4-digit numbers that are greater than
        or equal to the limit.
        int: The number of palindrome products found.
    """
    max_palindrome = 0
    palindrome_finder = 0
    for i in range(9999, limit, -1):
        for j in range(i, limit, -1):
            for k in range(j, limit, -1):
                for l in range(k, limit, -1):
                    product = i * j * k * l
                    if product > max_palindrome and is_palindrome(product):
                        max_palindrome = product
                        palindrome_finder += 1
    return (max_palindrome, palindrome_finder)


def max_palindrome():
    """
    Finds the largest palindrome that can be made from the product of four 4-digit numbers
    where each number is between 9999 and 100 times the iteration variable.

    Returns:
        int: The largest palindrome that can be made from the product of four 4-digit numbers.
    """
    max_generated_palindrome = 0
    for i in range(99, 1, -1):
        (generated_palindrome, palindrome_finder) = generate_palindrome(i * 100)
        if generated_palindrome > max_generated_palindrome:
            max_generated_palindrome = generated_palindrome
        elif (
            generated_palindrome == max_generated_palindrome
            and generated_palindrome != 0
            and palindrome_finder > 1
        ):
            break
    return max_generated_palindrome


result = max_palindrome()

print(
    f"The largest palindrome that can be made from the product of four 4-digit numbers is {result}."
)

end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
