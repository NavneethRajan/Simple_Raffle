drawbox = []
start = 0
drawing_trigger = 0


def raffle_entry():
    global drawbox;
    global start;


    name = raw_input("Please enter an entry name: ");


    ticket_value = False
    while ticket_value == False:
        try:
            tickets = int(input("Please enter the number of tickets purchased: "));
            ticket_value = True;
        except NameError:
            print("****ERROR: NUMBER OF TICKETS MUST BE NUMERIC. PLEASE ENTER AGAIN.****")

            
    print("****Adding %d tickets for %s to the raffle box!****" %(tickets, name));
    for i in range (tickets):
        drawbox.append(name);

    user_choice = False
    while user_choice == False:
        another_entry = raw_input("Would you like to make another entry? (y/n): ");
        if another_entry == "y":
            start = 0;
            user_choice = True
        elif another_entry == "n":
            final_confirm = 0
            while final_confirm == 0:
                final_answer = raw_input("Are you sure you want to finish submitting entries? (y/n): ")
                if final_answer == "y":
                    print("All entries submitted!");
                    start = 1;
                    user_choice = True;
                    final_confirm = 1;
                elif final_answer == "n":
                    final_confirm = 1;
                else:
                    print("Please enter either 'y' for yes or 'n' for no.")
                    
                
        else:
            print("Please enter either 'y' for yes or 'n' for no.")
    
    
def raffle_draw():
    global drawbox;
    final_list = drawbox;

    from random import shuffle;
    shuffle(final_list);

    from random import randint;
    winner = final_list[randint(0, len(drawbox))];

    print("****THE WINNER IS %s!" %(winner)); 
    
    



while start == 0:
    raffle_entry()

while start == 1:
    draw_choice = raw_input("Would you like to draw the raffle winner? (y/n)")
    if draw_choice == "y":
        print("****DRAWING***");
        drawing_trigger = 1;
        start = 2;
    elif draw_choice == "n":
        drawing_trigger = 0;
        start = 1;
    else:
         print("Please enter either 'y' for yes or 'n' for no.");

if start == 2:
    raffle_draw();

input("Press ENTER to exit")




