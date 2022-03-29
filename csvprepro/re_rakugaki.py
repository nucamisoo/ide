import re

# Matches only strings of one or more characters with double quotes as the first and last characters.
pattern = re.compile(r'^"{1}(?!").+"{1}$')
print(pattern.fullmatch('"'))          # None
print(pattern.fullmatch('""'))         # None
print(pattern.fullmatch('"""'))        # None
print(pattern.fullmatch('""""'))       # None
print(pattern.fullmatch('""hello"'))   # None
print(pattern.fullmatch('""hello""'))  # None
print(pattern.fullmatch('"hello"'))    # Match

pattern = re.compile(r'^"{1}(?P<content>(?=").+)"{1}$')
test_strings = ['',
#                '"',
                '""',
#                '"""',
                '""""',
#                '"""""',
                '"""""""',
                '"""""""""',
                '"""""""""""',
#               '"hello"',
                '""hello""',]

for test_string in test_strings:
    result = pattern.fullmatch(test_string)
    if result:
        result = result.group('content').replace('""', '"')
        print(f'{test_string} => {result}')
    else:
        print(f'{test_string} => None')


print('"hoge'.endswith('"'))
print('foo"bar'.endswith('"'))
print('"'.endswith('"'))
print('""'.endswith('"'))
print('hoge"'.endswith('"'))
print('"hoge"'.endswith('"'))
print('baz""'.endswith('"'))

