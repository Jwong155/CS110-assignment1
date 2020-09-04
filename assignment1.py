'''
Name: Jonathan Wong
email: jwong155@binghamton.edu
Section #B55
Assignment #1
'''

'''
ANALYSIS

RESTATEMENT:
  Ask a user how many people are in a room and output the total number of
  introductions if each person introduces themselves to every other person 
  once

OUTPUT to monitor:
  introductions (int) - when each person introduces themselves to every other
  person once
INPUT from keyboard:
  person_count (int)

GIVEN: 
  HALF (int) - 2

FORMULA:
  (person_count * (person_count - 1)) / HALF
'''

# CONSTANTS 
HALF = 2
INTRODUCTIONS_TOTAL = 0


# This program outputs the total number of introductions possible if each
# person in a room introduces themselves to every other person in the room 
# once, given the number of people in the room

def main():
  # Explain purpose of program to user
  print("Hello user, this is assignment 1! This program will ouput the " +
      "maximum introductions possible where each person introduces  " +
      "themselves to every other person in the room once, given the " +
      "number of people in the room.\n")

  
  # Ask user for number of people in room
  person_count_str = input("Please enter the amount of people present: ")
  
  # Convert str data to int
  person_count = int(person_count_str) 
  
  # Use the formula to compute the result
  # Changing / to // maintains an int output as requested
  introductions = (person_count * (person_count - 1)) // HALF
  
  # Display labeled and formatted introduction count
  print("Answer is ", introductions)
  
if __name__ == '__main__':
  main()

