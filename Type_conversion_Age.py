birth_year = input('Birth Year : ')
current_year = input('Current Year : ')
age = int(current_year) - int(birth_year)
print(age)
print(type(age))
print(type(birth_year + current_year))

#Exersie to convert weight in pound to KGS using USER input

w_pound = input('What is your weight (lbs) ? :  ')
w_kg = float(w_pound) * 0.45359 #Converstion in to float and multiplying the values
#Concatinating the value and string conversion to print the Statement
print('This is your weight in Kilograms : ' + str(w_kg) + ' kg' )
