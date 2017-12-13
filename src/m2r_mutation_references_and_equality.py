"""
This module demonstrates:
 1. MUTATION of an OBJECT via a direct assignment.
 2. MUTATION of an OBJECT via a function call.
 3. Two names that REFER to the same object.
 4. Re-assigning a new to refer to a NEW object.
 5. Two equality operators:   is   ==

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathaniel Nordquist.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg

########################################################################
# Students:  You will not write any code in this module,
#            but there ARE things TO DO below.
########################################################################

# ----------------------------------------------------------------------
# TODO: 2.
#  Step a:  READ the   mutate_point   function below.
#
#  Step b:  Note that the code in main has 5 parts numbered 1, 2, ... 5.
#    ** For EACH of those 5 parts: **
#
#    Step b1:  READ the code in that part.
#
#    Step b2:  PREDICT what  the code in that part will print
#                when it runs.
#
#    Step b3:  RUN this module and examine the output from that part.
#
#    Step b4:  See whether your prediction matched the actual output.
#                Ask questions as needed to resolve any differences.
#
#    Step b5:  When you believe that you understand ** ALL ** the code
#                in this module, ** ASKING QUESTIONS AS NEEDED, **
#                change the above TO DO to DONE.
# ----------------------------------------------------------------------


def mutate_point(point):
    """ Silly example, just to show mutation at work. """
    point.y = 77  # Mutates the  rg.Point  argument


def main():
    # ------------------------------------------------------------------
    # 1. Constructs an rg.Point, assigning its instance variables values.
    #    Then assigns an instance variable in the object a new value,
    #      thus MUTATING the OBJECT, because
    #      one of its INSTANCE VARIABLES was ASSIGNED a new value.
    # ------------------------------------------------------------------
    print('Showing mutation via assignment:')

    point = rg.Point(45, 100)

    print('Before:', point)
    point.y = 33

    # The next line shows that the INSIDES of   point   has changed.
    print('After: ', point)  # Look at what gets printed!

    # ------------------------------------------------------------------
    # 2. Mutates the object again, this time from within a function call
    # ------------------------------------------------------------------
    print()
    print('Showing mutation via a function call')
    print('(which does assignment):')

    print('Before:', point)
    mutate_point(point)

    # The next line shows that the INSIDES of   point   has changed.
    print('After: ', point)  # Look at what gets printed!

    # ------------------------------------------------------------------
    # 3. Assigns another variable to refer to the same rg.Point
    #       to which the    point   variable refers.
    #    That creates two NAMES (variables)
    #       that refer to the same OBJECT.
    #    When one mutates, so does the other.
    # ------------------------------------------------------------------
    print()
    print('Showing two NAMES that refer to the same OBJECT:')

    point2 = point

    print('Before:', point, point2)
    point2.x = 100
    print('After: ', point, point2)  # Note that  point.x  ALSO changed
    #> NOTE: point2.x AND point2.y changed! This is because point2.x IS point.x, and point.x was reassigned via
    # mutation.

    # ------------------------------------------------------------------
    # 4. Re-assigns the   point   variable to refer to another rg.Point.
    #      This is ASSIGNMENT and NOT mutation.
    # ------------------------------------------------------------------
    print()
    print('RE-ASSIGNING an object is  NOT  MUTATING the OBJECT:')

    print('Before:', point, point2)
    point = rg.Point(10, 6)
    print('Umm...After re-assignment:?', point, point2)  # Prints the two DIFFERENT rg.Points

    # ------------------------------------------------------------------
    # 5. Shows the difference between the   is   operator
    #      (two things refer to the same place in memory)
    #    and the   ==   operator (two things contain the same data).
    # ------------------------------------------------------------------
    print()
    print('Shows the difference between two operators')
    print('  -- a IS b  (do a and b refer to the same place in memory?')
    print('  -- a == b  (do a and b have the same data?)')
    print('Predict what will get printed by the following, if you can.')

    print()
    print('First, two Points are constructed.  See IS vs == in action:')

    point3 = rg.Point(100, 20)
    point4 = rg.Point(100, 20)

    print()
    print('Before: point3 and point4 are:', point3, point4)
    print('T or F: point3 is point4?', point3 is point4)
    print('T or F: point3 == point4?', point3 == point4)

    point3.fill_color = 'blue'
    print()
    print('After: point3 and point4 are:', point3, point4)
    print('Fillcolors are:', point3.fill_color, point4.fill_color)
    print('T or F: point3 is point4?', point3 is point4)
    print('T or F: point3 == point4?', point3 == point4)

    print()
    print('Second, another Point (point5) is assigned')
    print('to one of the existing ones (point3).')

    print()
    print('Here is the IS operator:')
    point5 = point3

    print('points3, 4 and 5 are:', point3, point4, point5)
    print('Fillcolors are:',
          point3.fill_color, point4.fill_color, point5.fill_color)
    print('T or F: point3 is point5?', point3 is point5)
    print('T or F: point3 is point4?', point3 is point4)
    print('T or F: point4 is point5?', point4 is point5)

    print()
    print('Now the == operator:')
    print('T or F: point3 == point5?', point3 == point5)
    print('T or F: point3 == point4?', point3 == point4)
    print('T or F: point4 == point5?', point4 == point5)

    print()
    print('Finally, a tricky one that your instruction will explain:')
    x = 'hello'
    y = 'hello'
    print()
    print('T or F: "hello" is "hello"?', x is y)
    # TODO: Ask: What the hell?
    print('T or F: "hello" == "hello"?', x == y)

    x = 1 * x
    y = 1 * y
    print()
    print('T or F: (1 * "hello") is (1 * "hello"?', x is y)
    print('T or F: (1 * "hello") == (1 * "hello"?', x == y)
    print('x, then y:', x, y)

    x = 2 * x
    y = 2 * y
    print()
    print('T or F: (2 * "hello") is (2 * "hello"?', x is y)
    print('T or F: (2 * "hello") == (2 * "hello"?', x == y)
    print('x, then y:', x, y)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

'''
# My question to fisher: 
# Why does the first print statement evaluate to True? The variable name x doesn’t seem (to me) to point to the same string instance with value <h e l l o>. I understand why x == y, since their string instances have the same value of <h e l l o>. What is happening in memory? Is there something in Python that just doesn’t bother making another instance of a string if a string with its same value already exists? Does it create a pointer without asking you? 
# 
# #CODE BLOCK 1# 
# print('Finally, a tricky one that your instruction will explain:')
# x = 'hello'
# y = 'hello'
# print()
# print('T or F: "hello" is "hello"?', x is y)
# # TODO: Ask: Why?? 
# print('T or F: "hello" == "hello"?', x == y)
# >>>T or F: "hello" is "hello"? True #***Why???***
# >>>T or F: "hello" == "hello"? True
# 
# Similarly, why would binary operations affect the IS evaluation? Why does x IS y evaluate to TRUE in Code Block 2, but not in Code Block 3? (I understand why they wouldn’t have an effect on the == evaluation; if the same operation is applied to both strings, they would have the same value.) 
# 
# #CODE BLOCK 2 # 
# x = 1 * x
# y = 1 * y
# print()
# print('T or F: (1 * "hello") is (1 * "hello"?', x is y)
# print('T or F: (1 * "hello") == (1 * "hello"?', x == y)
# >>> T or F: (1 * "hello") is (1 * "hello"? True
# >>>T or F: (1 * "hello") == (1 * "hello"? True
# 
# #CODE BLOCK 3 # 
# x = 2 * x
# y = 2 * y
# print()
# print('T or F: (2 * "hello") is (2 * "hello"?', x is y)
# print('T or F: (2 * "hello") == (2 * "hello"?', x == y)
# >>> T or F: (2 * "hello") is (2 * "hello"? False
# >>> T or F: (2 * "hello") == (2 * "hello"? True

 
'''
