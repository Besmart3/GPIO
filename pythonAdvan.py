# names = ["kofi", "Ama", "adwoa", "Akosoa"]
# print(list(map(len, names)))
 
# def too_old(x): return x > 30
# ages = [22, 25, 29, 34, 56, 24, 12]
# filtered = list(filter(too_old, ages))
# print(filtered)

# items = [1, 2, 3, 4, 5]
# squares = map((lambda x: x ** 2), items)
# print(list(squares)) 

# def even_number(nambers:list(int)):
#     numbers = [1,56,234,87,4,76,24,69,90,135]
#     if
# (even_number = number%2 == 0 )
#     print(" Is even")
# filters and lambdas
 
def even_numbers_map_filter(numbers: list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 == 0, numbers))

# Example usage
# numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
# even_numbers_result = even_numbers_map_filter(numbers)
# print(even_numbers_result)  # Output: [56, 234, 4, 76, 24, 90]

# def even_numbers_with_filter_and_lambda(numbers: list[int]) -> list:

 # List of numbers
numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]

# Using `not` with a lambda function to get odd numbers
odd_numbers_lambda = list(filter(lambda x: not (x % 2 == 0), numbers))
print(odd_numbers_lambda)  # Output: [1, 87, 69, 135]


def odd_numbers(numbers: list[int]) -> list[int]:
   return list(filter(lambda x: not (x % 2 == 0), numbers))

numbers =[1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
odd_numbers_lambda = odd_numbers(numbers)
print(odd_numbers_lambda)

# Joined strings
from functools import reduce

def join_strings(words):
    return reduce(lambda item, running_total: item + " " + running_total, words)

# Example usage
words = ["hello", "world"]
helloworld = join_strings(words)  # "hello world"
print(helloworld)  # Output: "hello world"

# Comprehensions

# 1. Split the sentence into words and get lengths of words not equal to "the"
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
lengths_not_the = [len(word) for word in words if word != "the"]
print("Lengths of words not 'the':", lengths_not_the)

# 2. Create a list of only the positive numbers from the given list
numbers_positive = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_numbers = [num for num in numbers_positive if num > 0]
print("Positive numbers:", positive_numbers)
negative_numbers = [num for num in numbers_positive if num < 0]
print("Negative numbers:", negative_numbers)




# 3. Create a list containing only the even numbers from the given list
numbers_even = [12, 54, 33, 67, 24, 89, 11, 24, 47]
even_numbers = [num for num in numbers_even if num % 2 == 0]
print("Even numbers:", even_numbers)
odd_numbers = [num for num in numbers_even if not (num % 2 == 0)]
print("Odd numbers:", odd_numbers)

# 4. Create a list containing tuples of uppercase words and their lengths
words_tuple = ["hello", "my", "name", "is", "Sam"]
uppercase_length_tuples = [(word.upper(), len(word)) for word in words_tuple]
print("Uppercase and lengths:", uppercase_length_tuples)
lowercase_length_tuples = [(word.lower(), len(word)) for word in words_tuple]
print("Lowercase and lengths:", lowercase_length_tuples)



# Classes



from datetime import datetime

class Person:
    def __init__(self, name: str, date_of_birth: str):
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    
    def speak(self):
        print("hello")
    
    def walk(self):
        print("walking away")
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

class Student(Person):
    def __init__(self, name: str, date_of_birth: str, courses: list[str]):
        super().__init__(name, date_of_birth)  # Call the constructor of the Person class
        self.courses = courses
    
    def get_courses(self):
        return self.courses
    
    def speak(self):
        print("I'm so tired!")

# Example usage
if __name__ == "__main__":
    # Create a Person
    person = Person("Alice", "1990-05-15")
    print(person.get_name())  # Output: Alice
    print(person.get_age())   # Output: Age based on current date
    person.speak()            # Output: hello
    person.walk()             # Output: walking away

    # Create a Student
    student = Student("Bob", "2000-08-20", ["Math", "Science", "History"])
    print(student.get_name())  # Output: Bob
    print(student.get_age())    # Output: Age based on current date
    print(student.get_courses()) # Output: ['Math', 'Science', 'History']
    student.speak()             # Output: I'm so tired!
    student.walk()              # Output: walking away