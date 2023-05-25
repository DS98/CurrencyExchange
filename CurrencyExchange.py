yuan = float(input('What do you have left in yuan?: '))
yuan_rate = 0.14
yen = float(input('What do you have left in yen?: '))
yen_rate = 0.0072
won = float(input('What do you have left in won?: '))
won_rate = 0.00075

USD = yuan_rate * yuan + yen_rate * yen + won_rate * won
print(USD)
