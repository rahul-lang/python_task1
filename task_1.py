import pyttsx3
import os
import calendar
pyttsx3.speak("Welcome to M.A.P.")
pyttsx3.speak("Select from Menu below")
while True:
    
    print("\n Welcome!! \n 1.Web Services \n 2.Media Services \n 3.Text Editors \n 4.Tools  \n 5.Exit") 
    choice=input("Enter your choice in words ")
    if (("run"in choice)or("execute" in choice))and("web" in choice) :
        print("Checking your connectivity...")
        ip= "google.com"
        response=os.system("ping "+ip+" -n 1")
        print (ip, 'is up!')
        #while True:
        print("\n 1.Web Search \n 2.Gmail \n 3.LinkedIn \n 4.Exit \n")
        print("Give your requirement")
        ch1=input()
        if (("run"in ch1)or("execute" in ch1))and("search" in ch1):
            print("\n 1.Chrome \n 2.Firefox \n 3.Safari \n ")
            print("Give your requirement")
            wbr=input()
            os.system("start "+wbr)
        elif(("run"in ch1)or("execute" in ch1))and("gmail" in ch1):
            os.system("start chrome "+"www.gmail.com")
        elif(("run"in ch1)or("execute" in ch1))and ("linkedin" in ch1):
            os.system("start chrome "+ "www.linkedin.com")
        elif("exit"in ch1):
	     #pyttsx3.speak("Going back")
             continue
	    
        else:
            print("Wrong Input!! Please input from menu")
            
    elif(("run" in choice)or("execute" in choice))and ("media" in choice):
        print("Select ur fav media player \n 1.Windows Media Player \n 2.Spotify \n 3.Pot player \n 4.Exit \n")
        print("Give your requirement in words ")
        ch2=input()
        
        if(("run" in ch2)or("execute" in ch2))and("wmplayer" in ch2):
            os.system("start wmplayer")
        elif(("run" in ch2)or("execute" in ch2))and("spotify" in ch2):
            os.system("start spotify")
        elif(("run" in ch2)or("execute" in ch2))and("pot player" in ch2):
            os.system("start pot player")
       
        elif("exit"in ch2):
            pyttsx3.speak("Going back")
            continue
        else:
            print("Wrong choice!!Select from given option")
            
    elif(("run" in choice)or("execute"in choice))and("text editor" in choice):
        print("Select ur text editor \n 1.Notepad \n 2.Sublime \n 3.Atom \n 4.Wordpad \n 5.Exit \n")
        print("Give your requirement in words")
        ch3=input()
        
        if(("run"in ch3)or("execute" in ch3))and("notepad" in ch3):
            os.system("start notepad")
        elif(("run"in ch3)or("execute" in ch3))and("sublime" in ch3):
            os.system("start sublime")
        elif(("run"in ch3)or("execute" in ch3))and("atom"in ch3):
            os.system("start atom")
        elif(("run"in ch3)or("execute"in ch3))and("wordpad"in ch3):
            os.system("start wordpad")
        
        elif("5"in ch3)or("exit"in ch3):
            pyttsx3.speak("Going back")
            continue
        else:
	        print("Wrong choice!!Select from menu above")
    
    elif(("run"in choice)or("execute"in choice))and("tools"in choice):
        print("\n 1.Calculator \n 2.Calender \n 3.Command Prompt \n 4.Reverse String \n 5.Exit \n")
        print("Give your desired tool")
        ch4=input()
        if("calc"in ch4)or("calculator"in ch4):
            os.system("start calc")
        elif("cal"in ch4)or("calendar"in ch4):
            print("give year and month in numerical")
            yy=int(input("Enter your year "))
            mm=int(input("Enter the month "))
            if((mm>12)or(mm<1))and(yy<2000)or(yy>3000):
                print("Wrong input")
            else:
                print(calendar.month(yy,mm))
        elif(("cmd"in ch4)or("command"in ch4)or("prompt"in ch4)):
            os.system("start cmd")
        elif("reverse"in ch4):
            str=input("Enter your string ")
            str=str[::-1]
            print("Reverse String is " +str)
	       
        elif("exit"in ch4):
            pyttsx3.speak("Going back")
            continue
        else:
             print("Wrong choice!!Select from input above")
    elif("exit" in choice)or("5"in choice):
         pyttsx3.speak("Exiting!!Have a nice day")
	 print("Have a nice day")
         quit()

