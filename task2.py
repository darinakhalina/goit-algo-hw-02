from collections import deque


def is_palindrome(s: str, ignore_chars=" .,?!'"):
    clean_str = "".join(char.lower() for char in s if char.lower() not in ignore_chars)
    char_queue = deque(clean_str)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True


def main():
    examples = [
        "A man, a plan, a canal, Panama!",
        "Madam, in Eden, I'm Adam.",
        "It's not a palindrome",
    ]

    for example in examples:
        is_palindrome_result = is_palindrome(example)
        palindrome_status = (
            "IS palindrome" if is_palindrome_result else "IS NOT palindrome"
        )
        print(f"'{example}' - {palindrome_status}")


if __name__ == "__main__":
    main()
