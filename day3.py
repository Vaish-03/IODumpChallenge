#Program yto find volume of sphere and cylinder.
pi = 3.1459
r = float(input('Enter radius: '))
h= int(input("Enter hight: "))
vol_sphere = 4/3*pi* r**3
vol_cyl = pi*(r*r)*h
print('The volume of the sphere is: ',vol_sphere)
print('The volume of the cylinder is: ',vol_cyl)