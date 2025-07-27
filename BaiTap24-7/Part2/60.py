def count(s):
    return len(s)


def reverse(s):
    return s[::-1]


def check(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def correct(s):
    words = s.strip().split()
    words = [word.capitalize() for word in words]
    return " ".join(words)
