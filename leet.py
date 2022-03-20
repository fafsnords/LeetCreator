# usr/bin/python
# coding utf-8

import os
import time
import colorama
from colorama import Fore

colorama.init()

class leet:
   def __init__(self, title, image, codename, greetings, message, save, solo_style, team_style, solo_page, team_page):
       self.title = title
       self.image = image
       self.codename = codename
       self.greetings = greetings
       self.message = message
       self.save = save
       self.solo_style = open("design/solo.txt", "r").read()
       self.team_style = open("design/team.txt", "r").read()
       self.solo_page = '<!DOCTYPE html><html><head><title>{0}</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Syne+Mono&display=swap"><style>{1}</style></head><body><div><img src="{2}" class="logo"width="240px" height="200px"></img><h1 class="codename">{3}</h1><h3>{4}</h3></div></body></html>'
       self.team_page = '<!DOCTYPE html><html><head><title>{0}</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Creepster&family=Inspiration&family=Palette+Mosaic&family=Smooch+Sans:wght@100&family=Syne+Mono&display=swap"><style>{1}</style></head><body><div><img src="{2}" width="240px" height="200px"></img><h1 class="team">{3}</h1></br><h2>Greetings</h2><div class="cut"><h3><marquee>{4}</marquee></h3></div></br><h3>{5}</h3></div></body></html>'
   
   # for choosing a solo
   def solo(self):

       # check if save file is not empty write its deface code
       if self.save != "":
         with open("{0}.html".format(self.save), "w") as page:
              page.write(self.solo_page.format(self.title, self.solo_style, self.image, self.codename, self.message))
              print(Fore.GREEN + "\nVisit The Location of File You save\n")
              input()
         page.close()
       else:
         print(Fore.RED + "\nEnter a File Name to Save\n")
         input()

   # for choosing a team
   def team(self):

       # check if save file is not empty writes its deface code
       if self.save != "":
         with open("{0}.html".format(self.save), "w") as page:
              page.write(self.team_page.format(self.title, self.team_style, self.image, self.codename, self.greetings, self.message))
              print(Fore.BLUE + "\nVisit The Location of File You Save\n")
              input()
         page.close()
       else:
         print(Fore.RED + "\nEnter a File Name to Save\n")
         input()

def main():
    
    # the procedure
    def help():
        print(Fore.CYAN + "\n\n[+] Title:" + Fore.YELLOW + "Hacked By <your_codename or team>")
        print(Fore.CYAN +"[+] Logo:" + Fore.YELLOW + "http://127.0.0.1/logo.jpg or HOME/path/logo.jpg <better if logo is hosted try here https://imgbb.com/>")
        print(Fore.CYAN +"[+] Codename:" + Fore.YELLOW + "Hacked By <your_codename or team>")
        print(Fore.CYAN +"[+] Greetings:" + Fore.YELLOW + "rev | renzie | j4gu4r | rhoy | f8th  <as an example if you choose a team>")
        print(Fore.CYAN +"[+] Message:" + Fore.YELLOW + "<post your message>\n")
        print(Fore.CYAN +"[+] Save:" + Fore.YELLOW + "<your_filename> or /HOME/path/<your_filename> choose a path to save your file\n")
        input()

    banner = Fore.RED + """
                 :::        :::::::::: :::::::::: ::::::::::: 
                :+:        :+:        :+:            :+:      
               +:+        +:+        +:+            +:+       
              +#+        +#++:++#   +#++:++#       +#+        
             +#+        +#+        +#+            +#+         
            #+#        #+#        #+#            #+#          
           ########## ########## ##########     ###
           [+] CODED BY: REV
          """ + Fore.YELLOW + """
           [+] 1) Solo
           [+] 2) Team
           
           [+] 3) Help
           [+] 4) Main                                      
          """
    print(banner)

    while not False:

       choose = input(Fore.BLUE + "[+] Enter Choose:")

       # a validation to avoid jumped to other consoles
       if choose == "":
         continue
       if choose =="exit":
         break
       else:
         # if choosing a number 1 executed to solo
         if '1' in choose:
           time.sleep(1)
           title = input(Fore.CYAN + "\n\n[+] Title:")
           image = input(Fore.CYAN + "[+] Logo:")
           codename = input(Fore.CYAN + "[+] Codename:")
           message = input(Fore.CYAN + "[+] Message:")
           save = input(Fore.CYAN + "\n[+] save:")

           bind = leet(title, image, codename, 0, message, save, 0, 0, 0, 0)
           bind.solo()

         # if choosing number 2 executed to team
         elif '2' in choose:
           time.sleep(1)
           title = input(Fore.CYAN + "\n\n[+] Title:")
           image = input(Fore.CYAN + "[+] Logo:")
           codename = input(Fore.CYAN + "[+] Codename:")
           greetings = input(Fore.CYAN + "[+] Greetings:")
           message = input(Fore.CYAN + "[+] Message:")
           save = input(Fore.CYAN + "\n[+] Save:")

           bind = leet(title, image, codename, greetings, message, save, 0, 0, 0, 0)
           bind.team()

         # if choosing number 3 executed to help
         elif '3' in choose:
           time.sleep(1)
           help()

         # if choosing number 4 executed back to main # recursion
         elif '4' in choose:
           os.system("clear")
           time.sleep(1)
           main()
main()