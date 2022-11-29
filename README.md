# Inventory management system.
## Example of a Python based inventory management system that reads from a CSV style data file.

This inventory management system is a simple stand alone program that allows a user to read, update and delete entries in a file containing details of items.
For this example the program finds its form as a system for an imaginary footware outlet, however I can be easily adapted to provide useful output for any data.

### To run this file in Docker play ground open an instance and type: docker run -i admbjmn/inventory_management - The files is easier to interpret in VS code and will provide you with more functionality - ie: viewing generated files.

## __Key Components__

__Classes__

The shoe class takes information from the CSV file and and creates objects 
to be referenced within the main functionality of the program.
The class takes 5 values 
- the country where the stock is held
- the stock code
- the name of the product
- the cost of each item
- the quantity of items in stock


__Functions__
1. Read Shoe Data
2. Capture Shoes
3. View All
4. Re Stock
5. Search Shoe
6. Value Per Item
7. Highest Quantity

## Functions explained.

The Program starts with a Login function that refereences users and passwords from a separate textfile.
The program can be accessed by default with 
_username_: admin
_password_: adm1n

### Read Shoe Data
read_shoes_data reads all information from the inventory file and
uses the data to create Shoe objects and add them to the shoe_list
the function is called as soon as a successful log in has been
achieved, this then populates the shoes_list ready for use


### Capture Shoes
Capture shoes allows the user to input the required data for a new
object, the data is passed through the shoe calss and the new object
is appended to the shoe_list.
The new data is also automatically added to the inventory.txt


### View All
View all takes the shoes from the shoe_list and creates
a list of lists with the data for each shoe object.
the list shoe_data is then used to create a table to
usefully display all data from shoe_list


### Re Stock
The restock function allows the user to add stock to the shoe object
with the lowest stock count.
The shoe objects in shoe_list are compared for thier quantity and the
item with the lowest quantity is stored in a variable called -
lowest stok item.
the user is then asked if they would like to add more stock to this item
if the response is yes, the stock is updated and the new values are
updated on the inventory.txt


### Search Shoe
The search shoes function allows a user to input a value representing
the code of a shoe. the code is then tested against the entire shoe list 
and once the object is found the objects data is turned into a list and
printed using tabulate


### Value Per Item
The value per item function allows a user to see the total value 
of each item along with a total value of the entire inventory
the information is saved into a list in order to be able to
use tablulate to present the data.


### Highest Quantity
Highest qty function allows the user to find the shoe
object with the highest quantity and outputs the data 
to the user


## Instalation.
In its current state this program can be opened in any program editor and run using a python interpreter.
The program will run inside the console with instructions on screen.

## Basic Program flow.

Once logged in the user is presented with a main menu as follows:
![main menu](/images/main_menu.png)


By selecting one on the commands as instructed the user is then prompted with new istructions based on the selection.
EG:

![re stock](/images/re_stock.png)


By continuing to follow the prompts on screen tasks can be taken care of and the CSV file will be updated.
Any functions that do not need user input will be displayed on screen and the menu will be re shown for 
any further requests.
EG:

![view all](/images/view_all.png)


Once the user has finished the program can be closed from the main menu by typing exit.

_This program was made by adm.bjmn.
