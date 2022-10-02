# What are command line arguments?
# Command line arguments are flags given to a program/script at runtime. They contain additional information for our program so that it can execute.

# Not all programs have command line arguments as not all programs need them. That being said, on this blog we make extensive use of command line arguments in our Python scripts and I’d even go so far to say that 98 % of the articles on this blog make use of them.

# Why do we use command line arguments?
# As stated, command line arguments give additional information to a program at runtime.

# This allows us to give our program different input on the fly without changing the code.

# installation
# pip install argparse


#                                           Getting Started
# Here is a file called index.py to demonstrate a very basic example of the structure and usage of the argparse library:

# Getting Started
# Import the library
# import argparse
# Create the parser
# parser = argparse.ArgumentParser()
# Add an argument
# parser.add_argument('--name', type=str, required=True)
# Parse the argument
# args = parser.parse_args()
# Print "Hello" + the user input argument
# print('Hello,', args.name)


#                           Positional Arguments
# Sometimes, you don’t want to use the flag’s name in the argument. You can use a positional argument to eliminate the need to specify the - -name flag before inputting the actual value. Below are two versions — the first without positional arguments(index.py), and the second using positional arguments(index.py)

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--x', type=int, required=True)
# parser.add_argument('--y', type=int, required=True)
# args = parser.parse_args()
# product = args.x * args.y
# print('Product:', product

# parser = argparse.ArgumentParser()
# parser.add_argument('x', type=int)
# parser.add_argument('y', type=int)
# args = parser.parse_args()
# product = args.x * args.y
# print('Product:', product)
# how to run python index.py 4 5

# Optional Arguments
# Optional arguments are useful if you want to give the user a choice to enable certain features. To add an optional argument, simply omit the required parameter in add_argument()

# parser = argparse.ArgumentParser()
# parser.add_argument('--name', type=str, required=True)
# parser.add_argument('--age', type=int)
# args = parser.parse_args()
# if args.age:
#   print(args.name, 'is', args.age, 'years old.')
# else:
#   print('Hello,', args.name + '!')

# multiple

# parser = argparse.ArgumentParser()
# parser.add_argument("--x", type=int, required=True, help="first integer value")
# parser.add_argument("--y", type=int, required=True,
#                     help="second integer value")

# args = vars(parser.parse_args())

# print("product of  x, y : {}".format((args['x']*args['y'])))

# Mutually Exclusive Arguments
# Another important argparse feature is mutally exclusive arguments. There are times that, depending on one argument, you want to restrict the use of another. This could be because the user should only need to use one of the arguments, or that the arguments conflict with each other. The method add_mutually_exclusive_group() let’s us do exactly that — add a group of arguments that are mutually exclusive.

# This next example, index.py, demonstrates how both arguments in a mutually exclusive group cannot be used at the same time.

# parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group()
# group.add_argument('--add', action='store_true')
# group.add_argument('--subtract', action='store_true')
# parser.add_argument('x', type=int)
# parser.add_argument('y', type=int)
# args = parser.parse_args()
# if args.add:
#   sum = args.x + args.y
#   print('Sum:', sum)
# elif args.subtract:
#   difference = args.x - args.y
#   print('Difference:', difference)


#                     Subparsers
# The last argparse feature I am going to discuss is subparsers. Subparsers are powerful in that they allow for different arguments to be permitted based on the command being run. For example, when using the git command, some options are git checkout, git commit, and git add. Each one of these commands requires a unique set of arguments, and subparsers allow you to distinguish between them

# parser = argparse.ArgumentParser()
# subparser = parser.add_subparsers(dest='command')
# login = subparser.add_parser('login')
# register = subparser.add_parser('register')
# login.add_argument('--username', type=str, required=True)
# login.add_argument('--password', type=str, required=True)
# register.add_argument('--firstname', type=str, required=True)
# register.add_argument('--lastname', type=str, required=True)
# register.add_argument('--username', type=str, required=True)
# register.add_argument('--email', type=str, required=True)
# register.add_argument('--password', type=str, required=True)
# args = parser.parse_args()
# if args.command == 'login':
#   print('Logging in with username:', args.username,
#         'and password:', args.password)
# elif args.command == 'register':
#   print('Creating username', args.username,
#         'for new member', args.firstname, args.lastname,
#         'with email:', args.email,
#         'and password:', args.password)

# pratice

# ap = argparse.ArgumentParser()
# ap.add_argument("-n", "--name", required=True)
# help("user name")

# args = vars(ap.parse_args())
# args = ap.parse_args()

# print(args.name)
# print("hi there! {}, nice to meet you".format(args['name']))


# parsing image
# import argparse
# import imutils
# import cv2
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--input", required=True,
#                 help="path to input image")
# ap.add_argument("-o", "--output", required=True,
#                 help="path to output image")
# args = vars(ap.parse_args())
# load the input image from disk
# image = cv2.imread(args["input"])
# convert the image to grayscale, blur it, and threshold it
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
#                         cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# loop over the contours and draw them on the input image
# for c in cnts:
# cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
# display the total number of shapes on the image
# text = "I found {} total shapes".format(len(cnts))
# cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
#             (0, 0, 255), 2)
# write the output image to disk
# cv2.imwrite(args["output"], image)

# multiple arugments
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--values', type=int, nargs=3)
# args = parser.parse_args()
# sum = sum(args.values)
# print('Sum:', sum)
