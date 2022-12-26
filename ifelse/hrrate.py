hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r =  float(rate)

if h > 40:
    reg = h * r
    over = (h - 40.0) * (r * 1.5)
    xa = reg + over
    
else:
    xa = h * r
print(xa)    
    