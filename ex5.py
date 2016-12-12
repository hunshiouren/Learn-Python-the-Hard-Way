name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
inch = 2.54 # cm
height_cm = height * inch
weight = 180 # lbs
pound = 0.45 # kg
weight_kg = weight * pound
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk ablout %s." % name
print "He's %d cms tall." % height_cm
print "He's %d kgs heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
age, height_cm, weight_kg, age + height_cm + weight_kg)
