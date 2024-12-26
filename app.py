import datetime

date = datetime.datetime.now()
format_date = date.strftime("%x")
using_app = True

def search_date():
    get_date = input("enter the date(MM/DD/YY): ")
    f=open("journal.txt","r")
    read_file = f.readlines()
    f.close()
    found = False

    for line in read_file:
        if get_date in line:
            print(line)
            found = True
    if not found:
        print("sorry we couldnt find any entries for that date")


def run_app():

    while using_app:





        start_menu = input("Welcome Back (new entry) (view previous) (exit) (search by date): ")

        if start_menu == "exit":
            print("okay bye")
            break

        elif start_menu =="new entry":
            add_text = input("Enter a journal entry: ")
            f = open("journal.txt", "a")

            confirm_entry = input("would you like to save this entry?(yes)/(no): ")

            if confirm_entry == "yes":

                f.write(f"{add_text} ")

                f.write(f"{format_date}\n")






            f.close()

            # f = open("journal.txt", "r")
            #
            # print(f.read())
        elif start_menu == "view previous":
            print("Here are your past entries: ")
            f = open("journal.txt", "r")

            print(f.read())
        elif start_menu == "search by date":
            search_date()







run_app()



