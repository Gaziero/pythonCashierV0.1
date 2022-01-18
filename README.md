# pythonCashierV0.1
A kinda simple program, functions as a (very simple) cashier system.

WHY I'VE MADE THIS?
This is a simple project, I'm doing it to improve and test my knowledge in python while making something usefull.
My family have a little ice cream store, wich is where I work. I use a cashier system all the time, so I've decided I'd tryto make my own.
From the start I knew it wouldn't be easy, but also, that it would be fun.
It worked, i've learned a lot, discovered that I need to learn thousands times more, but that's cool, I'm aimming for it.
It was a great exercise, I plan on improving it.
  
HOW IT WORKS?
For now, it runs on the IDE, it isn't an app yet, I gotta build the interface.

products.py is where the data of all products is registered.
It consists on a list with dictionaries in it;
Every dictionary is a product, composed of its code, name, and price;
The code can be any int number >0;
The name can be whatever str you want, although, try to keep it under 30 characters long;
The price can be a int or float number, the system works best with values <1000.00.

modules.py is where all the custom modules are stored.
main.py is the core code.

The program runs on the IDE, it will keep asking for a product code;
If you insert a int number followed by *, E.g. 5*, the next code will be stored int the cart 5 times;
If you insert a code that doesn't match any product's code, the program will tell you that said code is nonexistent;
The program only accepts the input of int numbers (followed or not by an *), showing an Error message if invalid data is inserted;
Inserting 0 as a code will end the operation of adding products to the cart.
When the cart is closed, shows how much the total cost was and asks for the input of how much the user will pay.
Then, the program will exit.

In the background, the program has created a file name toPrint.txt.
This .txt is designed to be printed by a thermal printer on 80mm paper, the default font should be Consolas, regular, 8.

!WARNING! By default, the code prints the .txt automatically, if you dont wanna waste paper and ink on random stuff, comment it using a #, its on the last lines of main.py

This is my very first project, commit, and README. Hope I haven't done anything stupid. Hope you like my code.
Sorry for any typos or english errors.
