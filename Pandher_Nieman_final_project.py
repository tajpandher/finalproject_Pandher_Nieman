from graphics import *


def main():
   # name counter
   total_names = 0


   # each day and time slot counter
   total_monday_morning = 0
   total_monday_afternoon = 0
   total_monday_evening = 0


   total_tuesday_morning = 0
   total_tuesday_afternoon = 0
   total_tuesday_evening = 0


   total_wednesday_morning = 0
   total_wednesday_afternoon = 0
   total_wednesday_evening = 0


   total_thursday_morning = 0
   total_thursday_afternoon = 0
   total_thursday_evening = 0


   total_friday_morning = 0
   total_friday_afternoon = 0
   total_friday_evening = 0


   # list that keeps track of every time slot
   all_availability = []


   # open the file
   file = open("all_availability.txt", "r")


   # read each line, and create a name and time slots
   for line in file:
       # name will get the first list, time slots will get the second
       # strip() deals with the whitespace, split makes a list from a string based on a given character
       name, time_slots = line.strip().split(': ')
       total_names += 1


       # make a new list that has each time slot separated properly
       slots_list = time_slots.split(', ')
       # add those new lists to the all_availability list using the extend method
       # extend method adds a list to a list
       all_availability.extend(slots_list)


   # go through the big list and count each time slot
   for slot in all_availability:
       day = slot[0]
       time = slot[1]
       if day == 'M':
           if time == 'M':
               total_monday_morning += 1
           elif time == 'A':
               total_monday_afternoon += 1
           elif time == 'E':
               total_monday_evening += 1
       elif day == 'T':
           if time == 'M':
               total_tuesday_morning += 1
           elif time == 'A':
               total_tuesday_afternoon += 1
           elif time == 'E':
               total_tuesday_evening += 1
       elif day == 'W':
           if time == 'M':
               total_wednesday_morning += 1
           elif time == 'A':
               total_wednesday_afternoon += 1
           elif time == 'E':
               total_wednesday_evening += 1
       elif day == 'R':
           if time == 'M':
               total_thursday_morning += 1
           elif time == 'A':
               total_thursday_afternoon += 1
           elif time == 'E':
               total_thursday_evening += 1
       elif day == 'F':
           if time == 'M':
               total_friday_morning += 1
           elif time == 'A':
               total_friday_afternoon += 1
           elif time == 'E':
               total_friday_evening += 1


   # close the file
   file.close()


   # output how many users are available in each time slot
   print("There are", total_monday_morning, "people available on Monday morning.")
   print("There are", total_monday_afternoon, "people available on Monday afternoon.")
   print("There are", total_monday_evening, "people available on Monday evening.")
   print("There are", total_tuesday_morning, "people available on Tuesday morning.")
   print("There are", total_tuesday_afternoon, "people available on Tuesday afternoon.")
   print("There are", total_tuesday_evening, "people available on Tuesday evening.")
   print("There are", total_wednesday_morning, "people available on Wednesday morning.")
   print("There are", total_wednesday_afternoon, "people available on Wednesday afternoon.")
   print("There are", total_wednesday_evening, "people available on Wednesday evening.")
   print("There are", total_thursday_morning, "people available on Thursday morning.")
   print("There are", total_thursday_afternoon, "people available on Thursday afternoon.")
   print("There are", total_thursday_evening, "people available on Thursday evening.")
   print("There are", total_friday_morning, "people available on Friday morning.")
   print("There are", total_friday_afternoon, "people available on Friday afternoon.")
   print("There are", total_friday_evening, "people available on Friday evening.")



   # set up graphics window
   win = GraphWin("Availability", 1000, 300)


   # DOCUMENT THIS
   # build out the rectangles
   monday_morning_rect = Rectangle(Point(0, 0), Point(200, 100))
   monday_morning_rect.draw(win)
   monday_afternoon_rect = Rectangle(Point(0, 100), Point(200, 200))
   monday_afternoon_rect.draw(win)
   monday_evening_rect = Rectangle(Point(0, 200), Point(200, 300))
   monday_evening_rect.draw(win)


   tuesday_morning_rect = Rectangle(Point(200, 0), Point(400, 100))
   tuesday_morning_rect.draw(win)
   tuesday_afternoon_rect = Rectangle(Point(200, 100), Point(400, 200))
   tuesday_afternoon_rect.draw(win)
   tuesday_evening_rect = Rectangle(Point(200, 200), Point(400, 300))
   tuesday_evening_rect.draw(win)


   wednesday_morning_rect = Rectangle(Point(400, 0), Point(600, 100))
   wednesday_morning_rect.draw(win)
   wednesday_afternoon_rect = Rectangle(Point(400, 100), Point(600, 200))
   wednesday_afternoon_rect.draw(win)
   wednesday_evening_rect = Rectangle(Point(400, 200), Point(600, 300))
   wednesday_evening_rect.draw(win)


   thursday_morning_rect = Rectangle(Point(600, 0), Point(800, 100))
   thursday_morning_rect.draw(win)
   thursday_afternoon_rect = Rectangle(Point(600, 100), Point(800, 200))
   thursday_afternoon_rect.draw(win)
   thursday_evening_rect = Rectangle(Point(600, 200), Point(800, 300))
   thursday_evening_rect.draw(win)


   friday_morning_rect = Rectangle(Point(800, 0), Point(1000, 100))
   friday_morning_rect.draw(win)
   friday_afternoon_rect = Rectangle(Point(800, 100), Point(1000, 200))
   friday_afternoon_rect.draw(win)
   friday_evening_rect = Rectangle(Point(800, 200), Point(1000, 300))
   friday_evening_rect.draw(win)


   # add the text labels for each of the rectangles in the center
   monday_morning_text = Text(Point(100, 50), "MM")
   monday_morning_text.draw(win)
   monday_afternoon_text = Text(Point(100, 150), "MA")
   monday_afternoon_text.draw(win)
   monday_evening_text = Text(Point(100, 250), "ME")
   monday_evening_text.draw(win)


   tuesday_morning_text = Text(Point(300, 50), "TM")
   tuesday_morning_text.draw(win)
   tuesday_afternoon_text = Text(Point(300, 150), "TA")
   tuesday_afternoon_text.draw(win)
   tuesday_evening_text = Text(Point(300, 250), "TE")
   tuesday_evening_text.draw(win)


   wednesday_morning_text = Text(Point(500, 50), "WM")
   wednesday_morning_text.draw(win)
   wednesday_afternoon_text = Text(Point(500, 150), "WA")
   wednesday_afternoon_text.draw(win)
   wednesday_evening_text = Text(Point(500, 250), "WE")
   wednesday_evening_text.draw(win)


   thursday_morning_text = Text(Point(700, 50), "RM")
   thursday_morning_text.draw(win)
   thursday_afternoon_text = Text(Point(700, 150), "RA")
   thursday_afternoon_text.draw(win)
   thursday_evening_text = Text(Point(700, 250), "RE")
   thursday_evening_text.draw(win)


   friday_morning_text = Text(Point(900, 50), "FM")
   friday_morning_text.draw(win)
   friday_afternoon_text = Text(Point(900, 150), "FA")
   friday_afternoon_text.draw(win)
   friday_evening_text = Text(Point(900, 250), "FE")
   friday_evening_text.draw(win)


   # DOCUMENT THIS
   # logic for coloring the boxes
   if total_monday_morning / total_names > 0.5:
       monday_morning_rect.setFill("green")
   elif total_monday_morning / total_names < 0.5:
       monday_morning_rect.setFill("red")
   else:
       monday_morning_rect.setFill("lightblue")


   if total_monday_afternoon / total_names > 0.5:
       monday_afternoon_rect.setFill("green")
   elif total_monday_afternoon / total_names < 0.5:
       monday_afternoon_rect.setFill("red")
   else:
       monday_afternoon_rect.setFill("lightblue")


   if total_monday_evening / total_names > 0.5:
       monday_evening_rect.setFill("green")
   elif total_monday_evening / total_names < 0.5:
       monday_evening_rect.setFill("red")
   else:
       monday_evening_rect.setFill("lightblue")


   if total_tuesday_morning / total_names > 0.5:
       tuesday_morning_rect.setFill("green")
   elif total_tuesday_morning / total_names < 0.5:
       tuesday_morning_rect.setFill("red")
   else:
       tuesday_morning_rect.setFill("lightblue")


   if total_tuesday_afternoon / total_names > 0.5:
       tuesday_afternoon_rect.setFill("green")
   elif total_tuesday_afternoon / total_names < 0.5:
       tuesday_afternoon_rect.setFill("red")
   else:
       tuesday_afternoon_rect.setFill("lightblue")


   if total_tuesday_evening / total_names > 0.5:
       tuesday_evening_rect.setFill("green")
   elif total_tuesday_evening / total_names < 0.5:
       tuesday_evening_rect.setFill("red")
   else:
       tuesday_evening_rect.setFill("lightblue")


   if total_wednesday_morning / total_names > 0.5:
       wednesday_morning_rect.setFill("green")
   elif total_wednesday_morning / total_names < 0.5:
       wednesday_morning_rect.setFill("red")
   else:
       wednesday_morning_rect.setFill("lightblue")


   if total_wednesday_afternoon / total_names > 0.5:
       wednesday_afternoon_rect.setFill("green")
   elif total_wednesday_afternoon / total_names < 0.5:
       wednesday_afternoon_rect.setFill("red")
   else:
       wednesday_afternoon_rect.setFill("lightblue")


   if total_wednesday_evening / total_names > 0.5:
       wednesday_evening_rect.setFill("green")
   elif total_wednesday_evening / total_names < 0.5:
       wednesday_evening_rect.setFill("red")
   else:
       wednesday_evening_rect.setFill("lightblue")


   if total_thursday_morning / total_names > 0.5:
       thursday_morning_rect.setFill("green")
   elif total_thursday_morning / total_names < 0.5:
       thursday_morning_rect.setFill("red")
   else:
       thursday_morning_rect.setFill("lightblue")


   if total_thursday_afternoon / total_names > 0.5:
       thursday_afternoon_rect.setFill("green")
   elif total_thursday_afternoon / total_names < 0.5:
       thursday_afternoon_rect.setFill("red")
   else:
       thursday_afternoon_rect.setFill("lightblue")


   if total_thursday_evening / total_names > 0.5:
       thursday_evening_rect.setFill("green")
   elif total_thursday_evening / total_names < 0.5:
       thursday_evening_rect.setFill("red")
   else:
       thursday_evening_rect.setFill("lightblue")


   if total_friday_morning / total_names > 0.5:
       friday_morning_rect.setFill("green")
   elif total_friday_morning / total_names < 0.5:
       friday_morning_rect.setFill("red")
   else:
       friday_morning_rect.setFill("lightblue")


   if total_friday_afternoon / total_names > 0.5:
       friday_afternoon_rect.setFill("green")
   elif total_friday_afternoon / total_names < 0.5:
       friday_afternoon_rect.setFill("red")
   else:
       friday_afternoon_rect.setFill("lightblue")


   if total_friday_evening / total_names > 0.5:
       friday_evening_rect.setFill("green")
   elif total_friday_evening / total_names < 0.5:
       friday_evening_rect.setFill("red")
   else:
       friday_evening_rect.setFill("lightblue")



   # keeps window open until user closes it
   while True:
       click_point = win.getMouse()


main()

