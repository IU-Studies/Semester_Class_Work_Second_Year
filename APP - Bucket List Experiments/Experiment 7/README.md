
# Regex Cheat Sheet and Explore character classes

# Regex Cheat Sheet

## 1. Basic Syntax

| Pattern  | Description                                  | Example                | Matches                              |
|----------|----------------------------------------------|------------------------|--------------------------------------|
| `.`      | Matches any single character                 | `a.c`                  | `abc`, `a1c`, but not `ac`          |
| `^`      | Matches the start of a string               | `^Hello`               | Matches `Hello World`, but not `Say Hello` |
| `$`      | Matches the end of a string                 | `World$`               | Matches `Hello World`, but not `World Hello` |
| `\d`     | Matches any digit                            | `\d{2}`                | Matches `12`, `99`, but not `ab`    |
| `\D`     | Matches any non-digit                        | `\D{3}`                | Matches `abc`, `xyz`, but not `123` |
| `\w`     | Matches any word character (alphanumeric + `_`) | `\w+`              | Matches `hello`, `world_123`        |
| `\W`     | Matches any non-word character               | `\W`                   | Matches `!`, `@`, `#`, etc.         |

## 2. Quantifiers

| Pattern   | Description                                         | Example                | Matches                              |
|-----------|-----------------------------------------------------|------------------------|--------------------------------------|
| `*`       | Matches 0 or more of the preceding element         | `a*`                   | Matches `""`, `a`, `aa`, `aaa`      |
| `+`       | Matches 1 or more of the preceding element         | `a+`                   | Matches `a`, `aa`, `aaa`, but not `""` |
| `?`       | Matches 0 or 1 of the preceding element            | `a?`                   | Matches `""` or `a`                  |
| `{n}`     | Matches exactly `n` times                          | `a{3}`                 | Matches `aaa`, but not `aa`          |
| `{n,}`    | Matches at least `n` times                         | `a{2,}`                | Matches `aa`, `aaa`, etc.           |
| `{n,m}`   | Matches between `n` and `m` times                  | `a{1,3}`               | Matches `a`, `aa`, or `aaa`         |

## 3. Character Classes

| Pattern        | Description                        | Example            | Matches                              |
|----------------|------------------------------------|--------------------|--------------------------------------|
| `[abc]`        | Matches any character in the set   | `[aeiou]`          | Matches `a`, `e`, `i`, `o`, `u`    |
| `[^abc]`       | Matches any character not in the set | `[^aeiou]`       | Matches `b`, `c`, `d`, etc.         |
| `[a-z]`        | Matches any lowercase letter       | `[A-Z]`            | Matches `A`, `B`, `C`, etc.         |
| `[0-9]`        | Matches any digit                  | `[a-zA-Z]`         | Matches `a`, `A`, `b`, `B`, etc.    |

## 4. Grouping and Capturing

| Pattern       | Description                              | Example                | Matches                              |
|---------------|------------------------------------------|------------------------|--------------------------------------|
| `(...)`       | Captures the group                       | `(abc)`                | Captures `abc`                       |
| `(?:...)`     | Non-capturing group                      | `(?:abc)`              | Matches `abc`, but does not capture   |
| `(?P<name>...)` | Named capturing group                  | `(?P<word>\w+)`       | Captures and names the group as `word` |

## 5. Assertions

| Pattern                   | Description                                           | Example              | Matches                             |
|---------------------------|-------------------------------------------------------|----------------------|-------------------------------------|
| `(?=...)`                 | Positive lookahead                                   | `\d(?= dollars)`     | Matches `5` in `5 dollars`         |
| `(?!...)`                 | Negative lookahead                                   | `\d(?! dollars)`     | Matches `5` in `5 euros`           |
| `(?<=...)`                | Positive lookbehind                                  | `(?<=\$)\d+`         | Matches `100` in `$100`            |
| `(?<!...)`                | Negative lookbehind                                  | `(?<!\$)\d+`         | Matches `100` in `100 euros`       |

## 6. Examples

- **Email Validation**: 
  ```regex
  ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
  ```

- **Phone Number (US)**: 
  ```regex
  ^\(\d{3}\) \d{3}-\d{4}$
  ```

- **URL Validation**: 
  ```regex
  ^https?://[^\s/$.?#].[^\s]*$
  ```

## Tips for Using Regex

1. **Test Regularly**: Use regex testing tools like [Regex101](https://regex101.com/) or [RegExr](https://regexr.com/) to test your patterns.
2. **Keep It Simple**: Avoid overly complex patterns that are hard to read. Break them down into smaller components if necessary.
3. **Use Comments**: If your regex is complex, consider adding comments to explain each part.

---

# Regular Expressions: Character Classes

Character classes in regular expressions allow you to define a set of characters that you want to match. Below are some common patterns using character classes:

## 1. Basic Character Class
- **Pattern**: `[abc]`
- This matches any single character that is either `a`, `b`, or `c`.
- **Example Match**:
  - String: "apple" → Match: `a`
  - String: "banana" → Match: `b`

## 2. Negated Character Class
- **Pattern**: `[^abc]`
- This matches any single character that is **not** `a`, `b`, or `c`.
- **Example Match**:
  - String: "apple" → Match: `p`
  - String: "banana" → Match: `n`
  - String: "cat" → Match: `t`

## 3. Range of Characters
- **Pattern**: `[a-z]`
- This matches any single lowercase letter from `a` to `z`.
- **Example Match**:
  - String: "hello" → Match: `h`, `e`, `l`, `o`
  - String: "123abc" → Match: `a`, `b`, `c`

## 4. Multiple Ranges
- **Pattern**: `[a-zA-Z0-9]`
- This matches any single alphanumeric character (lowercase letters, uppercase letters, or digits).
- **Example Match**:
  - String: "abcXYZ123" → Match: `a`, `b`, `c`, `X`, `Y`, `Z`, `1`, `2`, `3`

## 5. Combining Character Classes
- **Pattern**: `[a-zA-Z]`
- This matches any single letter, regardless of case.
- **Example Match**:
  - String: "Hello World" → Match: `H`, `e`, `l`, `l`, `o`, `W`, `o`, `r`, `l`, `d`

## Examples in Python

Here’s how you can implement these character classes using Python's `re` module:

```python
import re

# Define test strings
test_strings = ["apple", "banana", "hello", "cat", "123abc", "abcXYZ123"]

# Patterns
patterns = {
    "abc": r"[abc]",
    "not_abc": r"[^abc]",
    "lowercase": r"[a-z]",
    "alphanumeric": r"[a-zA-Z0-9]",
    "letters": r"[a-zA-Z]"
}

# Match patterns
for pattern_name, pattern in patterns.items():
    print(f"Matches for pattern {pattern_name}:")
    for string in test_strings:
        matches = re.findall(pattern, string)
        if matches:
            print(f"  String '{string}': {matches}")
