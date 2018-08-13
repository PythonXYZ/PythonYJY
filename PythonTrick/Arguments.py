import argparse

parser = argparse.ArgumentParser(description='Process some arguments.')
parser.add_argument('Age', type = int, help = 'Your Age')
parser.add_argument('Name', type = str, help = 'Your Fullname')

args = parser.parse_args()

age = args.Age
name = args.Name

print(f'My name is {name} and I am {age} years old.')