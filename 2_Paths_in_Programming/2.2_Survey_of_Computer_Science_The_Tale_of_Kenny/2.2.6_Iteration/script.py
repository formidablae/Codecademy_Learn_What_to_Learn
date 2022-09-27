on_the_griddle = [["eggs"], ["eggs"], ["eggs"], ["eggs"]]

def add_spinach(being_cooked):
	for item in being_cooked:
		item.append("spinach")
	print(being_cooked)
    
def add_mushrooms(being_cooked):
	for item in being_cooked:
		item.append("mushrooms")
	print(being_cooked)

def add_cheese(being_cooked):
	for item in being_cooked:
		item.append("cheese")
	print(being_cooked)
  
  
# Paste your code on the lines below:
add_spinach(on_the_griddle)
add_mushrooms(on_the_griddle)
add_cheese(on_the_griddle)
