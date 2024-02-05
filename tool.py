#main_def="xyz"
def xyz():
    #logo_def="logo"
    def logo():
        MAGENTA = '\033[35m'
        RESET = '\033[0m'
        print(MAGENTA+"""
      
 ██████  ███████ ███████ ███████ ███    ██ ███████ ██ ██    ██ ███████     ██         
██    ██ ██      ██      ██      ████   ██ ██      ██ ██    ██ ██          ██         
██    ██ █████   █████   █████   ██ ██  ██ ███████ ██ ██    ██ █████       ██         
██    ██ ██      ██      ██      ██  ██ ██      ██ ██  ██  ██  ██          ██         
 ██████  ██      ██      ███████ ██   ████ ███████ ██   ████   ███████     ███████ ██ 
-----------------------------------------------------------------------    ----------                                                                               
"""+RESET)
    
    #options_def="options"
    def options():
        YELLOW = '\033[33m'
        GREEN = '\033[32m'
        RESET1 = '\033[0m'
        print(GREEN+"""
[1] Follow Facebook 
[2] Follow Twitter
[3] Visit Website 
[4] Exit 
"""+RESET1)
        
    def main():
        import os
        os.system("clear")
        logo()
        options()
        #user_input_line
        user_input = input("Enter Your Option :")
        #importing modules
        import os
        #back-end_work
        if user_input=="1":
            os.system('xdg-open https://www.facebook.com/teamclayhacker')
            os.system("exit")
        elif user_input=="2":
            os.system('xdg-open https://twitter.com/KaziR3685')
            os.system("exit")
        elif user_input=="3":
            os.system('xdg-open https://oghbnz.xyz')
            os.system("exit")
        elif user_input=="4":
            os.system("exit")
        else:
            print("wrong option seleted")
            os.system("exit")
    main()