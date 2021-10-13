class crypto:

    def encrypt(self):
        from os import path, getcwd
        from time import time
        from random import randint
        from tkinter import Tk, filedialog

        Tk().withdraw()  # Removing the TK window

        # Asking for user input into a file
        file_loc = filedialog.askopenfilename(initialdir=getcwd(), title="Select a File")

        # Checking if the file exists
        if (file_loc == ""):
            print("ERROR: No file selected\n\n")
            return
        elif path.exists(file_loc):
            print("Requested file exists\n")
        else:
            print("ERROR: No such file exists\n\n")
            return

        #  Starting timer
        time_start = time()

        # Opening file and getting length
        main_file = open(file_loc, "r")
        doc = main_file.read()
        size = len(doc)

        # Generating seed
        a = randint(1, 9)
        b = randint(1, 9)
        c = randint(1, 9)
        d = randint(1, 9)
        seed = str(a) + str(b) + str(c) + str(d)
        seed = int(seed)
        print("Your file seed: ", seed, "\n")

        encry_str = ""
        while size >= len(encry_str):
            seed = seed * seed
            encry_str = encry_str + str(seed)

        encry_file = ""
        for i in range(size):
            letter = doc[i]
            v = ord(letter)
            adder = encry_str[i]
            adder = int(adder)
            v += adder
            b = chr(v)
            encry_file += b

        main_file.close()
        temp_file = open(file_loc, "w")
        temp_file.write(encry_file)
        temp_file.close()

        print("Encryption done\n")

        time_end = time()
        time_elapsed = time_end - time_start
        print("TIME TAKEN: \n", time_elapsed)

    def decrypt(self):
        from os import path, getcwd
        from time import time
        from tkinter import Tk, filedialog

        Tk().withdraw()  # Removing the TK window

        # Asking for user input into a file
        file_loc = filedialog.askopenfilename(initialdir=getcwd(), title="Select a File")

        # Checking if the inputted file exists
        if (file_loc == ""):
            print("ERROR: No file selected\n\n")
            return
        elif path.exists(file_loc):
            print("Requested file exists\n")
        else:
            print("ERROR: No such file exists\n\n")
            return

        main_file = open(file_loc, "r")
        doc = main_file.read()
        size = len(doc)

        seed = int(input("Please Enter The File Seed: "))

        time_start = time()

        new = ""
        while size >= len(new):
            seed = seed * seed
            new = new + str(seed)

        p = ""
        for i in range(size):
            letter = doc[i]
            v = ord(letter)
            subtract = new[i]
            subtract = int(subtract)
            v -= subtract
            b = chr(v)
            p += b

        main_file.close()
        temp_file = open(file_loc, "w")
        temp_file.write(p)
        temp_file.close()

        print("Decryption done \n")

        time_end = time()
        time_elapsed = time_end - time_start
        print("Time Taken: \n", time_elapsed)

    def main(self):
        print("*" * 60)
        print("\t\t\tCrypto")
        print("*" * 60)

        while True:
            print("\tCrypto Menu:")
            print("\t1 for Encrypting")
            print("\t2 for Decrypting")
            print("\t3 for Exiting Program")

            user_choice = input("Enter your choice: ")

            if (not(user_choice.isdigit())):
                print("\nERROR: Wrong Input, Please Enter Again\n\n")
                continue

            user_choice = int(user_choice)

            if (user_choice == 1):
                print("\nEncrypting Selected:- \n")
                self.encrypt()
                continue

            elif (user_choice == 2):
                print("\nDecrypting Selected:- ")
                self.decrypt()
                continue

            elif (user_choice == 3):
                confirm_exit = input("\nAre you sure you want to quit? (Y/N): ")

                while (True):
                    confirm_exit = input()
                    if (confirm_exit == "Y" or confirm_exit == "y"):
                        print("\nExiting Program ............ ")
                        input()
                        return
                    elif (confirm_exit == 'N' or confirm_exit == 'n'):
                        break
                    elif (confirm_exit == ''):
                        print("\nERROR: No input detected, Please Enter Again\n")
                    else:
                        print("\nERROR: ", confirm_exit, "is not a valid input, Please Enter Again\n")

            else:
                print("\nERROR: Wrong Input, Please Enter Again\n\n")
                continue


a = crypto()
a.main()
