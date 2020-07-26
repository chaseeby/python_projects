alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# move alien to the right
# determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increase = 1
if alien_0['speed'] == 'medium':
    x_increase = 2
else:
    # this must be a fast alien
    x_increase = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increase

print(f"New position: {alien_0['x_position']}")
