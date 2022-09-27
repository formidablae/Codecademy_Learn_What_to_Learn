import textwrap
import random

# This function makes up the main body of the game and controls a players general flow through each of the options.
def health_inspector_kenny(visited):
	if visited == 0:
		print(textwrap.fill(lb +"Welcome Health Inspector Kenny.\nToday you have to inspect three restaraunts and give them ratings.", width=60) +"\nWhere would you like to go first?\n"+lb)
		choice = location_selector(locations)
		if locations[choice] == "Billy's Big Burgers":
			locations.remove("Billy's Big Burgers")
			visited += 1
			billys_grade = billys_burgers()
			print(textwrap.fill("You've finished inspecting \"Billy's Big Burgers\" and have given it a grade of {0}.".format(grades[billys_grade]), width=60))
			health_inspector_kenny(visited)
		elif locations[choice] == "Lucy's Lemonade and Licorice":
			locations.remove("Lucy's Lemonade and Licorice")
			visited += 1
			lucys_grade = lucys_lemonade()
			print(textwrap.fill("You've finished inspecting \"Lucy's Lemonade and Licorice\" and have given it a grade of {0}.".format(grades[lucys_grade]), width=60))
			health_inspector_kenny(visited)
		elif locations[choice] == "Laura's Luncheonette":
			locations.remove("Laura's Luncheonette")
			visited += 1
			lauras_grade = lauras_luncheonette()
			print(textwrap.fill("You've finished inspecting \"Laura's Luncheonette\" and have given it a grade of {0}.".format(grades[lauras_grade]), width=60))
			health_inspector_kenny(visited)
	elif visited < 3:
		print("Where do you want to go next?"+lbb)
		choice = location_selector(locations)
		if locations[choice] == "Billy's Big Burgers":
			locations.remove("Billy's Big Burgers")
			visited += 1
			billys_grade = billys_burgers()
			print(textwrap.fill("You've finished inspecting \"Billy's Big Burgers\" and have given it a grade of {0}.".format(grades[billys_grade]), width=60))
			health_inspector_kenny(visited)
		elif locations[choice] == "Lucy's Lemonade and Licorice":
			locations.remove("Lucy's Lemonade and Licorice")
			visited += 1
			lucys_grade = lucys_lemonade()
			print(textwrap.fill("You've finished inspecting \"Lucy's Lemonade and Licorice\" and have given it a grade of {0}.".format(grades[lucys_grade]), width=60))
			health_inspector_kenny(visited)
		elif locations[choice] == "Laura's Luncheonette":
			locations.remove("Laura's Luncheonette")
			visited += 1
			lauras_grade = lauras_luncheonette()
			print(textwrap.fill("You've finished inspecting \"Laura's Luncheonette\" and have given it a grade of {0}.".format(grades[lauras_grade]), width=60))
			health_inspector_kenny(visited)
	else:
		print(textwrap.fill(lb + "Congratulations! You've finished a day of fullfilling health inspecting. Head home, pop open your favorite beverage, turn on old reruns of America's Next Top Model, and enjoy your evening." + lbb, width=60))

# Helper functions
def location_selector(locations):
  for i in range(0,len(locations)):
    print("("+str(i+1)+") " + locations[i]+"\n")
  selection = chooser(locations)
  return selection

def chooser(locations):
  try:
    selection = int(input("Enter the number of your choice: ")) - 1
    if selection >= len(locations):
      print("Sorry, invalid selection. Please try again.")
      selection = chooser(locations)
    return selection
  except (NameError, SyntaxError):
    print("Sorry, invalid selection. Please try again.")
    selection = chooser(location)
  return selection

def responder():
  response = int(input("Enter the number of your choice: "))
  if response not in [1, 2]:
    print("Please enter a valid choice.")
    responder()
  return response

def format_text(text):
  print(textwrap.fill(lb + text, width=60, replace_whitespace=False) + lbb)
  
# Locations
def billys_burgers():
  # 3 = A, 2 = B, 1 = C, 0 = F
  billys_grade = 3
  areas = ["Dining Room", "Bar", "Kitchen"]
  print(textwrap.fill(lb + "You enter the rustic yet charming all-American diner \"Billy's Big Burgers\". Billy himself, a large swarthy man in a striped apron, comes up to you and gruffly shakes your hand.\n\"Welcome Mr. Health Inspector, please take a look around, let me know if you need anything.\" Billy retreats back to the kitchen, keeping an eye on you as he backs away. Seems like a pretty weird guy.", width=60, replace_whitespace=False))
  for i in range(len(areas)):
    print("What area of the restaraunt would you like to check?\n"+ lb)
    choice = location_selector(areas)
    if areas[choice] == "Dining Room":
      format_text("You enter the dining room and are immediately hit with the smell of unwashed laundry. \"Hmm, that's not a good sign\" you think to yourself. Upon inspecting several tables, you find stains all over most of the tablecloths. You peer under the top of one of the booths only to find more dried gum than an elementary school's cafeteria.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        billys_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Billy's Big Burgers is currently {1}".format(areas[choice], grades[billys_grade]) + lbb, width=60))
      areas.remove("Dining Room")
    elif areas[choice] == "Bar":
      format_text("Walking behind the bar, you see everything appears fairly organized and clean. You notice a small picture of a little girl next to the glasses. Billy notices you looking at the picture and comes over. \"That's my girl Sasha\", he taps the picture and looks directly in your eyes, \"she'd be really crushed if the restaurant didn't pass the health inspection. You wouldn't disappoint Sasha would you?\"")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        billys_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Billy's Big Burgers is currently {1}".format(areas[choice], grades[billys_grade]) + lbb, width=60))
      areas.remove("Bar")
    elif areas[choice] == "Kitchen":
      format_text("The first thing you see in the kitchen is a massive pile of dishes sitting in the sink. \"I haven't had a chance to clean those yet\", states Billy, standing in your way. Pushing past him you see more concerning things. Open packs of American cheese sitting on counters in the heat. A mysterious mound of grey meat sits on top of a cold grill. A strange orange fluid seems to be leaking from the bottom of the fridge. To top it off, you see an empty container of plastic gloves sitting above a workstation, stuffed with what appears to be used tissues.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        billys_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Billy's Big Burgers is currently {1}".format(areas[choice], grades[billys_grade]) + lbb, width=60))
      areas.remove("Kitchen")
  return billys_grade

def lauras_luncheonette():
# 3 = A, 2 = B, 1 = C, 0 = F
  lauras_grade = 3
  areas = ["Dining Room", "Bar", "Kitchen"]
  print(textwrap.fill(lb + "You pull up to \"Laura's Luncheonette\", a plain white building with fading blue paint on the window trim. Laura meets you outside, bouncing from one foot to the other, appearing quite nervous. She leads you inside and gestures wildy. \"Please, please, inspect away, inspect it all it's perfect I promise!\" She nods enthusiastically at you to begin.", width=60))
  for i in range(len(areas)):
    print("What area of the restaurant would you like to check?"+ lb)
    choice = location_selector(areas)
    if areas[choice] == "Dining Room":
      format_text("As you start to inspect the dining room you are interrupted as a family of mice dart across the room, running across your shoes. Clearly these mice are not afraid of people. Laura doesn't seem to notice the mice as she has begun frantically weaving between tables emptying ashtrays into a pocket on her apron.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        lauras_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Laura's Luncheonette is currently {1}".format(areas[choice], grades[lauras_grade]) + lbb, width=60))
      areas.remove("Dining Room")
    elif areas[choice] == "Bar":
      format_text("The bar is crowded with half finished drinks, some appear to have formed some sort of weird film on them. You want to inspect behind the bar but your foot gets stuck in something extremely sticky that is coating the floor. Oh boy, it's that kind of day.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        lauras_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Laura's Luncheonette is currently {1}".format(areas[choice], grades[lauras_grade]) + lbb, width=60))
      areas.remove("Bar")
    elif areas[choice] == "Kitchen":
      format_text("The 'kitchen' is actually a series of cafeteria tables filled with rusty hot plates surrounded by cupboards. This place looks more like a high school chemistry lab than it does an eating establishment. Upon opening one of the cupboards, you see several waterbugs quickly scamper out of the light. You've seen enough here, this is bad.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        lauras_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Laura's Luncheonette is currently {1}".format(areas[choice], grades[lauras_grade]) + lbb, width=60))
      areas.remove("Kitchen")
  return lauras_grade

def lucys_lemonade():
# 3 = A, 2 = B, 1 = C, 0 = F
  lucys_grade = 3
  areas = ["Dining Room", "Bar", "Kitchen"]
  print(textwrap.fill(lb + "Lucy's Lemonade in Licorice, a small hole in the wall restaraunt, is teeming with people waiting outside when you arrive. You push your way to front of the line and ask to speak to Lucy. A woman comes out, pauses to wash her hands, and then turns to you. \n\n \"Oh, I didn't expect an inspection today. Sorry for the crowd, we launched a brand new flavor of licorice today, Matcha! But everything should be in order, come in and look.\"", width=60, replace_whitespace=False))
  for i in range(len(areas)):
    print("What area of the restaraunt would you like to check?"+ lbb)
    choice = location_selector(areas)
    if areas[choice] == "Dining Room":
      format_text("You squeeze into the small dining room. All six of the tables are filled with customers, munching on pale green strands of licorice and drinking glasses of lemonade. 'Interesting color of licorice' you think to yourself 'must be the new flavor.' \n\n Despite being crowded, the waiters are moving through smoothly and the floors and tables seem quite clean. A group of patrons gets up to leave and the table is promptly wiped down and cleaned.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        lucys_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Lucy's Lemonade and Licorice is currently {1}".format(areas[choice], grades[lucys_grade]) + lbb, width=60))
      areas.remove("Dining Room")
    elif areas[choice] == "Bar":
      format_text("Dominating the wall behind the bar are rows and rows of jars of different flavors of licorice. Upon inspection, each jar is sparklingly clean and closed with an airtight seal. \n\nOn the bar itself lies three large glass barrels of lemonade. Next to the barrels are lines of cleaned glasses. You see the various lemonade garnishes properly refrigerated underneath the bartop.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        lucys_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Lucy's Lemonade and Licorice is currently {1}".format(areas[choice], grades[lucys_grade]) + lbb, width=60))
      areas.remove("Bar")
    elif areas[choice] == "Kitchen":
      format_text("In the kitchen you see a large strange machine. As you go to investigate it Lucy comes over to explain it's function. \"See here,\" she points at a row of nozzles, \"this is where the strands of licorice come out and this here twirls them.\" Cool, you think to yourself as you note that this machine is also very clean. In fact, everything in the kitchen seems spotless. You've never seen such a well-run lemonade and licorice establishment.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        lucys_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Lucy's Lemonade and Licorice is currently {1}".format(areas[choice], grades[lucys_grade]) + lbb, width=60))
      areas.remove("Kitchen")
  return lucys_grade

# Global Objects
lbb = "\n------------------------------------------------------------\n"
lb = "------------------------------------------------------------\n"
grades = ["F", "C", "B", "A"]
locations = ["Billy's Big Burgers", "Lucy's Lemonade and Licorice", "Laura's Luncheonette"]
# use clean_responses[randint(0,6)] to generate a random response 
clean_responses = ["It looks pretty clean", "Clean enough", "Very clean", "I'd eat food prepared here", "Cleaner than my house", "Squeaky clean", "The cleanest I've ever seen"]
dirty_responses = ["Oh god, it's so gross", "I can't breathe in here", "Quite dirty", "Very dirty", "Really disgusting", "Dirtier than a dumpster", "I wouldn't eat here"]
visited = 0

health_inspector_kenny(visited)
