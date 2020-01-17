alien_0 = { 'color' : 'green', 'points': 5, 'x position':0, 'y position':25, 'speed': 'slow'}
print('Original x position: ' + str(alien_0['x position']))

#move the alien to the right. 
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# the new position is the old position plus the increment.
alien_0['x position'] = alien_0['x position'] + x_increment

print("New x positition: " + str(alien_0['x position']))

print(alien_0) 

del alien_0['points']
print(alien_0)

