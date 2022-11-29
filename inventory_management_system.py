from tabulate import tabulate
import copy

'''This Inventory Management system is a simple appication that 
enables a user to action a various set of functions on data in 
CSV style. Modelled for this purpose on an imaginary footware store.
'''

class Shoe:
    """The shoe class takes information and creates objects 
        to be referenced within the main functionality of the program.
        The class takes 5 values 
        The country where the stock is held
        The stock code
        The name of the product
        The cost of each item
        The quantity of items in stock
    """

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # get cost returns the cost of a shoe object as an integer
    def get_cost(self):
        return int(self.cost)

    # get quantity returns the quantity of a shoe object as an integer
    def get_quantity(self):
        return int(self.quantity)

    # __str__ returns each object as a string
    def __str__(self):
        return (f"{self.country},{self.code},{self.product},"
            +f"{self.cost},{self.quantity}")

#=============Shoe list===========
headers = ['Country','Code','Product','Cost','Quantity']
shoe_list = []
shoe_data = []

#==========Functions outside the class==============
def read_shoes_data():
    ''' read_shoes_data reads all information from the inventory file and
    uses the data to create Shoe objects and add them to the shoe_list
    the function is called as soon as a successful log in has been
    achieved, this then populates the shoes_list ready for use
    '''
    stock_form = None
    # initiate a while loop to house the try function
    while stock_form == None:
        try:
            # if file exist then read the file
            stock_form = open('inventory.txt','r')
            # start the file from the second line
            next(stock_form)
            # for lines in the stockform create a list and 
            # pass each list through the Shoe Class using the index
            # of the list as the values for each requirement.
            for lines in stock_form:
                lines = lines.strip().split(',')
                # each shoe is added to the shoe_list
                shoe_list.append(
                    Shoe(lines[0],lines[1],lines[2],lines[3],lines[4]))
        # if the file does not exist raise and error and inform the user
        except FileNotFoundError as error:
            print(
                'The Stock file was not found,'
                +' Please double check the folder')
            print(error, end= '\n')
        # if the file name has a value then it must 
        # always be closed after use.
        finally:
            if stock_form is not None:
                stock_form.close()

def capture_shoes():
    ''' Capture shoes allows the user to input the required data for a new
    object, the data is passed through the shoe calss and the new object
    is appended to the shoe_list.
    The new data is also automatically added to the inventory.txt
    '''
    shoe_list.append(Shoe(
        input("Please enter the country to alocate the stock to:\n"),
        "SKU"+ input("Please enter the product code for the item:\n"),
        input("Please enter the product name:\n"),
        input("Please enter the items cost:\n"),
        input("Please enter the current stock levels:\n")
        ))
    new_shoe_data = shoe_list[-1].__str__().split(',')
    stock_form = None
    while stock_form == None:
        try:
        # if file exist then print new_shoe_data
            stock_form = open('inventory.txt','a')
            stock_form.write(f"{','.join(new_shoe_data)}\n")
        # if the file does not exist raise
        # error and inform the user
        except FileNotFoundError as error:
            print(
                'The Stock file was not found,'
                +' Please double check the folder')
            print(error, end= '\n')
                # if the file name has a value then it must 
                # always be closed after use.
        finally:
                if stock_form is not None:
                    stock_form.close()
        # confirm success to the user
        print("\n++STOCK UPDATED++\n")
   

def view_all():
    '''View all takes the shoes from the shoe_list and creates
    a list of lists with the data for each shoe object.
    the list shoe_data is then used to create a table to
    usefully display all data from shoe_list
    '''
    for shoes in shoe_list:
        shoe_data.append(shoes.__str__().split(','))
    return tabulate(shoe_data, headers, tablefmt='outline') + '\n'


def re_stock(x):
    '''The restock function allows the user to add stock to the shoe object
    with the lowest stock count.
    The shoe objects in shoe_list are compared for thier quantity and the
    item with the lowest quantity is stored in a variable called -
    lowest stok item.
    the user is then asked if they would like to add more stock to this item
    if the response is yes, the stock is updated and the new values are
    updated on the inventory.txt
    '''
    # the shoes_list is deep copied in order to prevent any changes being made
    # to the shoe_list. this ensures it can be reused for other functions
    temp_list = copy.deepcopy(x)
    # if there is only on item in the temp list then it will be the 
    # item with lowest stock count
    if len(temp_list) == 1 :
        # this is then saved to the lowest stock item variable
        lowest_stock_item = temp_list[0]
        # in order to display the item in a table it must be in
        # list format
        lowest_stock_print_item = []
        lowest_stock_print_item.append(temp_list[0].__str__().split(','))
        # this list can then be printed useing tabulate
        print(f"The Item with the most stock is currently:\n")
        print(tabulate(lowest_stock_print_item,headers,tablefmt='outline'))
        # the user is then asked if they would like to update the stock
        selection_required = True
        while selection_required:
            selection = input(
            "\nWould you like to add more stock \
                for this item?(Yes/No):\n").upper()
            # if they choose yes the user is asked how much stock to add
            # this number is then added to the current stock count
            if selection == 'YES':
                lowest_stock_item.quantity = (lowest_stock_item.get_quantity() 
                + int(input("How many items to add?:")))
                # view all is then called to populate the shoe_data list
                view_all()
                # a new list item is then created with the updated 
                # re stocked item
                new_shoe_data = []
                new_shoe_data.append(lowest_stock_item.__str__().split(','))
                # the original item is then found in the shoes_list by
                # referenceing the items code. the item is then
                # replaced with the new information
                for index, item in enumerate(shoe_data):
                    if item[1] == new_shoe_data[0][1]:
                        index_to_replace = index
                shoe_data[index_to_replace] = new_shoe_data[0]
                # the newly updated shoe_data list is then written
                # to the inventory.txt file
                stock_form = None
                while stock_form == None:
                    try:
                    # if file exist then print shoe_data
                        stock_form = open('inventory.txt','w')
                        stock_form.writelines(f"{','.join(headers)}\n")
                        for lines in shoe_data:
                            stock_form.writelines(f"{','.join(lines)}\n")
                        # if the file does not exist raise
                        # error and inform the user
                    except FileNotFoundError as error:
                        print(
                            'The Stock file was not found,'
                            +' Please double check the folder')
                        print(error, end= '\n')
                    # if the file name has a value then it must 
                    # always be closed after use.
                    finally:
                        if stock_form is not None:
                            stock_form.close()
                            selection_required = False
                    print("\n++STOCK UPDATED++\n")
            # if the user choses not to update the function is exited
            elif selection =='NO':
                selection_required = False
            else:
                print("\n- Entry not recognised, Please Try again. -")
        ''' 
        while the temp list has more than 1 value the values are compared
        and the object with the higher stock count is removed from the 
        temp list. recursion is then used to whittle down the list until the
        remaining item is the one with the lowest stock quantity
        '''
    else:
        quantity_one = temp_list[-1].get_quantity()
        quantity_two = temp_list[-2].get_quantity()
        if quantity_one > quantity_two:
            del temp_list[-1]
            return(re_stock(temp_list))
        else:
            del temp_list[-2]
            return(re_stock(temp_list))


def search_shoe():
    '''the search shoes function allows a user to input a value representing
    the code of a shoe. the code is then tested against the entire shoe list 
    and once the object is found the objects data is turned into a list and
    printed using tabulate
    '''
    search_item = input(
        "Please enter the code for the item you wish to search for. SKU:\n")
    for shoes in shoe_list:
        if shoes.code == ("SKU"+ search_item):
            search_result = [shoes.__str__().split(',')]
    return(
        f"\nSearch result:"
        +f"\n{tabulate(search_result, headers, tablefmt = 'outline')}\n")


def value_per_item():
    '''The value per item function allows a user to see the total value 
    of each item along with a total value of the entire inventory
    the information is saved into a list in order to be able to
    use tablulate to present the data.
    '''
    stock_value = []
    total_stock_value = 0
    # for each object in the shoes_list the data is extracted 
    # and saved to the stock value list
    for shoes in shoe_list:
        stock_value.append(
            (shoes.country, shoes.product, shoes.code,
            # the value of staock is calulated using the 
            # get_cost and get_quantity methods inside Shoe
            shoes.get_cost() * shoes.get_quantity()))
        total_stock_value += shoes.get_cost() * shoes.get_quantity()
    # the table is then output to the user
    return(
        tabulate(stock_value, 
        headers = ["Country", "Shoe", "Code", "Stock Value"],
        tablefmt = 'outline') + '\nTotal value of all stock: '
        + str(total_stock_value)+'\n')

def highest_qty(x):
    '''Highest qty function allows the user to find the shoe
    object with the highest quantity and outputs the data 
    to the user
    '''
    # a deep copy of the shoes list is made so as to preserve
    # the original list
    temp_list = copy.deepcopy(x)
    # once the temp list only has one item then it will be the item
    # with the highest quantity and will be output to the user
    if len(temp_list) == 1 :
        # the info is saved to a list so that tabulate can be used
        highest_stock_item = []
        highest_stock_item.append( temp_list[0].__str__().split(','))
        return(f"\nThe Item with the most stock is currently:\n"
        +f"{(tabulate(highest_stock_item, headers, tablefmt='outline'))}\n"
        +f"This item should now be on sale.\n")
    # while the list has more than one value the last two objects are
    # compared and the one wit the lower quantity is removed from the list
    # recurrsion is then used to continue removing items.
    else:
        quantity_one = temp_list[-1].get_quantity()
        quantity_two = temp_list[-2].get_quantity()
        if quantity_one > quantity_two:
            del temp_list[-2]
            return(highest_qty(temp_list))
        else:
            del temp_list[-1]
            return(highest_qty(temp_list))

#==========Main Menu=============
# this login in block is stolen from my capstone L1T24
# username : admin
# password : adm1n

username_required = True
password_required = True
# open a loop for authenticating the username using username_required booleon
while username_required:
    with open('users.txt', 'r') as users:
        username = input("Please enter a valid username:\n")
        for lines in users:
            # I chose not to use a list here because I dont want
            # to create a passwords list aswell and store it
            # inside the active program. i just want to take
            # the password that is needed.
            # if a match is found
            if username in lines:
                    print('User confirmed')
                    username_required = False
                    # once a valid username is entered
                    # a username is no longer required
                    # the password for this user will always be 
                    # the next word on the same line.
                    # save the password using a split and an integer selection
                    true_password = [lines.split()[1]]
# once the username loop is closed a password is requested
# entered password must match true_password exactly
# start a loop for password authentiacation
while password_required:
    password = input("Please enter your password:\n")
    if password in true_password:  # if the password matches true_password
        print("\n- Login Successful. -")
        # once the correct password is entered 
        # password_required becomes false and closes the loop
        # login success becomes true
        password_required = False
        login_success = True
    # or else keep asking for password
    else:
        print("Password is incorrect, Please try again.")

# once login sequence has been completed the read_shoes_data
# function follows to populate the shoes_list
read_shoes_data()
while login_success:
    # a menu is presented to the user to choose a function
    menu = input('''Select one of the following \
        options below by typing the corresponding key word:

    add - Add new items to inventory
    view all - View inventory
    re stock - Re Stock low items
    search - Search item by SKU code
    value - View inventory value
    over stock - View highest stock items
    exit - Exit

    Type Selection here: ''').lower()

    if menu == "add":
        capture_shoes()
        '''once the function is complete the shoe_data list
        is deleted in order to ensure the list isnt compounded
        at each function use. it also ensures that the list is
        always up dated if multiple functions are used in one
        session and values are changed.
        '''
        shoe_data = []
    
    elif menu == "view all":
        print(view_all())
        shoe_data = []
    
    elif menu == "re stock":
        (re_stock(shoe_list))
        shoe_data = []
    
    elif menu == "search":
        print(search_shoe())

    elif menu == "value":
        print(value_per_item())
    
    elif menu == "over stock":
        print(highest_qty(shoe_list))

    elif menu == "exit":
        print("GOODBYE")
        exit()
    else:
        print("\n- Entry not recognised, Please Try again. -")