calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_):
    count_calls()
    return string.lower() in (item.lower() for item in list_)

info = string_info("Lesson 3")
print(info)
info_1 = string_info("Python project")
print(info_1)
info_2 = string_info("Users asus")
print(info_2)

contains = is_contains("Lesson",["Python", "project", "asus"])
print(contains)
contains_1 = is_contains("asus", ["Python", "project", "asus"])
print(contains_1)
print(calls)