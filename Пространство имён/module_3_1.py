calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    global calls
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    global calls
    count_calls()
    string = string.lower()
    for s in list_to_search:
        if s.lower() == string:
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)