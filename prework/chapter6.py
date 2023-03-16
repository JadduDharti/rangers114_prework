alien_01 = {'color' : 'green' , 'points' : 5}

print(alien_01['color'])
print(alien_01['points'])

new_point = alien_01['points']
print("You just entered " + str(new_point) + " points!")
print(alien_01)
alien_01['x_p'] = 0
alien_01['y_p'] = 25

print(alien_01)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine 
if alien_0['speed'] == 'slow':
     x_increment = 1
elif alien_0['speed'] == 'medium':
 x_increment = 2
else:
 x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

del alien_0['x_position']
print(alien_0)



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

if name in friends:
   print(" Hi " + name.title() +", I see your favorite language is " +
favorite_languages[name].title() + "!")

for name in sorted(favorite_languages.keys()):
   print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
   print(language.title())