#myfirstline
print("Hello Python World");

#string_print
name = "The first string...";
print(name);
print(name.title());
print(name.upper());
print(name.lower());

#combaning_two_string
first_name = "Dharti";
last_name = "Patel";
full_name = first_name + " " + last_name;
print(first_name);
print(last_name);
print(full_name);
print("Hello, " + full_name.title() + "!");

#Adding_whitespace_newline
print("\tpython");
print("Language\n\tPython\n\tJava");

#numbers
number = 20;
print(number);
message = "Happy " + str(number) + "th Birthday";
print(message);





#Chapternumber3

cars = ['BMW', 'Honda', 'toyato', 'Audi']
print(cars);
print(cars[0]);
print(cars[2].title());
print(cars[-1]);

my_car = "My first car was " + cars[1];
print(my_car);


motorcycle = ['Honda', 'suzuki', 'Hardly', 'Yamaha'];
print(motorcycle);

motorcycle[1] = "Ducati";
print(motorcycle);
motorcycle.append('Suzuki');
print(motorcycle);


house = [];
house.append('room');
house.append('kitchen');
house.append('bathroom');
print(house);
house.insert(1, 'Basement');
print(house);
del house[2];
print(house);

popped_house = house.pop();
print(popped_house);
print("My house has 2 " + popped_house);

motorcycle.remove('Honda');
print(motorcycle);

house.sort();
print(house);

cars.sort(reverse=True);
print(cars);

list_name = ['Jigar', 'Dharti', 'Vrund', 'Tom'];
print("Here is the original list:");
print(list_name);
print("Here is the sorted list:");
print(sorted(list_name));
print("Here is the original list again: ");
print(list_name);

list_name.reverse();
print(list_name);
print(len(list_name));


#ChaperNumber4
emps = ['John', 'David', 'Mary', 'Sam'];
for emp in emps:
    print(emp);
    print(emp.title() + " is good employee.");

print("That was my employees");

for value in range(1,6):
    print(value);

list_numbers = list(range(1,6));
print(list_numbers);

even = list(range(2,15,2));
print(even);

odd = list(range(1,15,2));
print(odd);

squares = [];

for value in range(1,6):
    square = value ** 2;
    squares.append(square);

print(squares);


digits = [1, 2, 3, 4, 5];
print(max(digits));
print(min(digits));
print(sum(digits));

games = ['football', 'basketball', 'baseball', 'running', 'cricket'];
print(games[0:2]);
print(games[:3]);
print(games[1:2]);
print(games[3:]);

for game in games[:4]:
    print(game.title());

copy_games = games[:];
print(copy_games);

