# python3

from tkinter import *
from tkinter import messagebox
from tkinter import Menu
import tkinter

class conversions(): # class used for the mathematical conversions
    def __init__(self):
       #can use enum or tuple here would be more ideal and cleanner?
       #bools to know what number system is being used
       is_bin,is_oct,is_dec,is_hex = False,False,False,True
       change_to_bin,change_to_oct,change_to_dec,change_to_hex = False,False,False,True
       return_value = 0
       self.return_value = return_value
       self.is_bin = is_bin
       self.is_oct = is_oct
       self.is_dec = is_dec
       self.is_hex = is_hex

       self.change_to_bin = change_to_bin
       self.change_to_oct = change_to_oct
       self.change_to_dec = change_to_dec
       self.change_to_hex = change_to_hex

    def set_base_num_sys(self,stringValue): #used to set numbersytem the input it
        if(stringValue == "bin"): 
            self.is_bin = True
            self.is_oct = False
            self.is_dec = False
            self.is_hex = False
            print("set to bin")
        elif(stringValue == "oct"): 
            self.is_bin = False
            self.is_oct = True
            self.is_dec = False
            self.is_hex = False
            print("set to oct")
        elif(stringValue == "dec"): 
            self.is_bin = False
            self.is_oct = False
            self.is_dec = True
            self.is_hex = False
            print("set to dec")
        elif(stringValue == "hex"): 
            self.is_bin = False
            self.is_oct = False
            self.is_dec = False
            self.is_hex = True
            print("set to hex")
    
    def set_answer_num_sys(self,stringValue): #used to set the number system the answer will be 
        if(stringValue == "bin"): 
            self.change_to_bin = True
            self.change_to_oct = False
            self.change_to_dec = False
            self.change_to_hex = False
            print("ans to bin")
        elif(stringValue == "oct"): 
            self.change_to_bin = False
            self.change_to_oct = True
            self.change_to_dec = False
            self.change_to_hex = False
            print("ans to oct")
        elif(stringValue == "dec"): 
            self.change_to_bin = False
            self.change_to_oct = False
            self.change_to_dec = True
            self.change_to_hex = False
            print("ans to dec")
        elif(stringValue == "hex"): 
            self.change_to_bin = False
            self.change_to_oct = False
            self.change_to_dec = False
            self.change_to_hex = True
            print("ans to hex")

    def reset_number_sys_base_to_dec(self, stringValue):#This will test the entered nnumber system and number are correct then translate to decimal sys
        if(self.is_bin == True):
            try:
                self.return_value = int(stringValue,2)
                return self.return_value #retruns int in decimal

            except:
                print("not a binary number") #tells console if inputed number isnt correct as expected. user will have to clear to continue or change the number sys
                return False #returns false instead of an int if inccorect
        
        elif(self.is_oct == True):
            try:
                self.return_value = int(stringValue,8)
                return self.return_value 

            except:
                print("not a Octal number")
                return False
        
        elif(self.is_dec == True):
            try:
                self.return_value = int(stringValue,10)
                return self.return_value 

            except:
                print("not a decimal number") 
                return False
        
        
        else: #is hex
            try:
                self.return_value = int(stringValue,16)
                return self.return_value 

            except:
                print("not a hex number")  
                return False
        
    def trans_to_req_num_sys(self,baseValue): #this will return the final answer in correct number system by taking in decimal number system and returns it as an int
        if(self.change_to_bin == True):
            self.return_value = bin(baseValue)
            return self.return_value
        
        elif(self.change_to_oct == True):
            self.return_value = oct(baseValue)
            return self.return_value
        
        elif(self.change_to_dec == True):
            return baseValue
        
        else:
            self.return_value = hex(baseValue)
            return self.return_value

class console_manager():#class used to hold the tkinter functions + string functions for console aka the visuals
    def __init__(self, arit = conversions()):
       #creating window
        window = Tk()
        window.title("Calculator")
        window.geometry("430x700") 
        #creating first string var for the input
        tk_console_string_input = tkinter.StringVar()
        input_to_tkString = ""
        tk_console_string_input.set("0")
        #creating second string var for output
        tk_console_string_output = tkinter.StringVar()
        output_to_tkString = ""
        tk_console_string_output.set("0")
        #frame 1 for buttons stating base
        Frame_base_num_sys = Frame(window,width=430, height=20)
        Frame_base_num_sys.pack()
        Frame_base_num_sys.pack_propagate(0) #used to set height of frame
        #frame 2 for input console
        Frame_console_input = Frame(window,width=420, height=140)
        Frame_console_input.pack()
        Frame_console_input.pack_propagate(0)
        #frame 3 for output console
        Frame_console_output = Frame(window,width=420, height=140, background="grey")
        Frame_console_output.pack()
        Frame_console_output.pack_propagate(0)
        #frame4 for buttons for output number system
        Frame_output_num_sys = Frame(window,width=430, height=20)
        Frame_output_num_sys.pack()
        Frame_output_num_sys.pack_propagate(0)
        #frame5 for buttons row1
        Frame_buttons_row_1 = Frame(window,width=430, height=70)
        Frame_buttons_row_1.pack()
        Frame_buttons_row_1.pack_propagate(0)
        #frame6 for buttons row2
        Frame_buttons_row_2 = Frame(window,width=430, height=70)
        Frame_buttons_row_2.pack()
        Frame_buttons_row_2.pack_propagate(0)
        #frame7 for buttons row3
        Frame_buttons_row_3 = Frame(window,width=430, height=70)
        Frame_buttons_row_3.pack()
        Frame_buttons_row_3.pack_propagate(0)
        #frame8 for buttons row4
        Frame_buttons_row_4 = Frame(window,width=430, height=70)
        Frame_buttons_row_4.pack()
        Frame_buttons_row_4.pack_propagate(0)
        #frame95 for buttons row5
        Frame_buttons_row_5 = Frame(window,width=430, height=70)
        Frame_buttons_row_5.pack()
        Frame_buttons_row_5.pack_propagate(0)
        
        #buttons in frame1
        base_bin_button = Button(Frame_base_num_sys, text = "Bin",width=9, height=20,font=("Arial", 14),command=lambda: [self.base_num_sys_set("bin"),self.highlight_base_button("bin")])
        base_bin_button.pack(side=LEFT)
        base_oct_button = Button(Frame_base_num_sys, text = "Oct",width=9,height=20, font=("Arial", 14),command=lambda: [self.base_num_sys_set("oct"),self.highlight_base_button("oct")])
        base_oct_button.pack(side=LEFT)
        base_dec_button = Button(Frame_base_num_sys, text = "Dec",width=9,height=20, font=("Arial", 14),command=lambda: [self.base_num_sys_set("dec"),self.highlight_base_button("dec")])
        base_dec_button.pack(side=LEFT)
        base_hex_button = Button(Frame_base_num_sys, text = "Hex",background="yellow",width=9,height=20, font=("Arial", 14),command=lambda: [self.base_num_sys_set("hex"),self.highlight_base_button("hex)")])
        base_hex_button.pack(side=LEFT)

        #label for console input frame number2
        console_label = Label(Frame_console_input, textvariable = tk_console_string_input,font=("Arial", 34),wraplength=420,anchor="se",justify="right") #prints out values and wraps to prevent number cut off
        console_label.grid(column=0, row=0)
        console_label.pack(side = TOP)  

        #label for the console output in frame number 3
        console_label = Label(Frame_console_output, textvariable = tk_console_string_output,background="grey",font=("Arial", 34),wraplength=420,anchor="se",justify="right") #prints out values
        console_label.grid(column=0, row=0)
        console_label.pack(side = TOP) 

        #buttons in frame4. intial number system is hex as its the biggest and allows for all values
        convert_to_bin_button = Button(Frame_output_num_sys, text = "To Bin",width=9, height=20,font=("Arial", 14),command=lambda: [self.answer_number_sys_set("bin"),self.highlight_convert_button("bin")])
        convert_to_bin_button.pack(side=LEFT)
        convert_to_oct_button = Button(Frame_output_num_sys, text = "To Oct",width=9,height=20, font=("Arial", 14),command=lambda: [self.answer_number_sys_set("oct"),self.highlight_convert_button("oct")])
        convert_to_oct_button.pack(side=LEFT)
        convert_to_dec_button = Button(Frame_output_num_sys, text = "To Dec",width=9,height=20, font=("Arial", 14),command=lambda: [self.answer_number_sys_set("dec"),self.highlight_convert_button("dec")])
        convert_to_dec_button.pack(side=LEFT)
        convert_to_hex_button = Button(Frame_output_num_sys, text = "To Hex",background="yellow",width=9,height=20, font=("Arial", 14),command=lambda: [self.answer_number_sys_set("hex"),self.highlight_convert_button("hex")])
        convert_to_hex_button.pack(side=LEFT)

        #buttons for numbers in frame 5
        button_0 =  Button(Frame_buttons_row_1, text = "0",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("0"))
        button_0.pack(side=LEFT)
        button_1 =  Button(Frame_buttons_row_1, text = "1",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("1"))
        button_1.pack(side=LEFT)
        button_2 =  Button(Frame_buttons_row_1, text = "2",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("2"))
        button_2.pack(side=LEFT)
        button_3 =  Button(Frame_buttons_row_1, text = "3",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("3"))
        button_3.pack(side=LEFT)
        
         #buttons for numbers in frame 6
        button_4 =  Button(Frame_buttons_row_2, text = "4",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("4"))
        button_4.pack(side=LEFT)
        button_5 =  Button(Frame_buttons_row_2, text = "5",width=9, height=70,font=("Arial", 14), command=lambda: self.to_input_console("5"))
        button_5.pack(side=LEFT)
        button_6 =  Button(Frame_buttons_row_2, text = "6",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("6"))
        button_6.pack(side=LEFT)
        button_7 =  Button(Frame_buttons_row_2, text = "7",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("7"))
        button_7.pack(side=LEFT)

        #buttons for numbers in frame 7
        button_8 =  Button(Frame_buttons_row_3, text = "8",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("8"))
        button_8.pack(side=LEFT)
        button_9 =  Button(Frame_buttons_row_3, text = "9",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("9"))
        button_9.pack(side=LEFT)
        button_A =  Button(Frame_buttons_row_3, text = "A",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("A"))
        button_A.pack(side=LEFT)
        button_B =  Button(Frame_buttons_row_3, text = "B",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("B"))
        button_B.pack(side=LEFT)

        #buttons for numbers in frame 8
        button_C =  Button(Frame_buttons_row_4, text = "C",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("C"))
        button_C.pack(side=LEFT)
        button_D =  Button(Frame_buttons_row_4, text = "D",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("D"))
        button_D.pack(side=LEFT)
        button_E =  Button(Frame_buttons_row_4, text = "E",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("E"))
        button_E.pack(side=LEFT)
        button_F =  Button(Frame_buttons_row_4, text = "F",width=9,height=70, font=("Arial", 14), command=lambda: self.to_input_console("F"))
        button_F.pack(side=LEFT)

        #buttons for numbers in frame 9
        button_clear =  Button(Frame_buttons_row_5, text = "Clear",width=19,height=70, font=("Arial", 14),command=lambda: self.clear_input())
        button_clear.pack(side=LEFT)
        button_answer =  Button(Frame_buttons_row_5, text = "Answer",width=19,height=70, font=("Arial", 14),command=lambda: self.calculate_answer())
        button_answer.pack(side=LEFT)
        
        self.window = window
        self.tk_console_string_input = tk_console_string_input
        self.tk_console_string_output = tk_console_string_output
        self.input_to_tkString = input_to_tkString
        self.output_to_tkString = output_to_tkString
        self.arit = arit
        
        self.base_bin_button = base_bin_button
        self.base_oct_button = base_oct_button
        self.base_dec_button = base_dec_button
        self.base_hex_button = base_hex_button

        self.convert_to_bin_button = convert_to_bin_button
        self.convert_to_oct_button = convert_to_oct_button
        self.convert_to_dec_button = convert_to_dec_button
        self.convert_to_hex_button = convert_to_hex_button

    def to_input_console(self,stringchar): #takes in a charcter/string and adds it the previous string. it then used to showcase this value in the input console label
        self.input_to_tkString += stringchar
        self.tk_console_string_input.set(self.input_to_tkString)
    
    def clear_input(self): #clears both the input of user and any output that may have already been calculated
        self.input_to_tkString = "0"
        self.tk_console_string_input.set(self.input_to_tkString)
        self.output_to_tkString = "0"
        self.tk_console_string_output.set(self.output_to_tkString)
    
    def to_output_console(self, answer_value): #simliar to input version but this adds to output console
        self.tk_console_string_output.set(str(answer_value))

    def base_num_sys_set(self,stringValue): #uses the arithmetic calculateer that was passed in as a parameter in the init stage to set the number system of the input
        self.arit.set_base_num_sys(stringValue)

    def highlight_base_button(self,button_to_highlight): #used to highlight the number system that is being entered
        if(button_to_highlight == "bin"):
            self.base_bin_button.configure(background="yellow") #loop function to clean up code can be used if have time
            self.base_oct_button.configure(background="white")
            self.base_dec_button.configure(background="white")
            self.base_hex_button.configure(background="white")
        elif(button_to_highlight =="oct"):
            self.base_bin_button.configure(background="white")
            self.base_oct_button.configure(background="yellow")
            self.base_dec_button.configure(background="white")
            self.base_hex_button.configure(background="white")
        elif(button_to_highlight == "dec"):
            self.base_bin_button.configure(background="white")
            self.base_oct_button.configure(background="white")
            self.base_dec_button.configure(background="yellow")
            self.base_hex_button.configure(background="white")
        else:
            self.base_bin_button.configure(background="white")
            self.base_oct_button.configure(background="white")
            self.base_dec_button.configure(background="white")
            self.base_hex_button.configure(background="yellow")

    def highlight_convert_button(self,button_to_highlight): # used to highlight the number system it will convert to 
        if(button_to_highlight == "bin"):
            self.convert_to_bin_button.configure(background="yellow") #loop function to clean up code can be used if have time
            self.convert_to_oct_button.configure(background="white")
            self.convert_to_dec_button.configure(background="white")
            self.convert_to_hex_button.configure(background="white")
        elif(button_to_highlight =="oct"):
            self.convert_to_bin_button.configure(background="white")
            self.convert_to_oct_button.configure(background="yellow")
            self.convert_to_dec_button.configure(background="white")
            self.convert_to_hex_button.configure(background="white")
        elif(button_to_highlight == "dec"):
            self.convert_to_bin_button.configure(background="white")
            self.convert_to_oct_button.configure(background="white")
            self.convert_to_dec_button.configure(background="yellow")
            self.convert_to_hex_button.configure(background="white")
        else:
            self.convert_to_bin_button.configure(background="white")
            self.convert_to_oct_button.configure(background="white")
            self.convert_to_dec_button.configure(background="white")
            self.convert_to_hex_button.configure(background="yellow")

    def answer_number_sys_set(self,stringValue): #used to set the nummber system used for the answer
        self.arit.set_answer_num_sys(stringValue)
    
    def calculate_answer(self): #calculates the answer
        self.output_to_tkString = self.arit.reset_number_sys_base_to_dec(self.input_to_tkString)    
        if(self.output_to_tkString == False): #if above returned false then user input was Incorrect 
            self.output_to_tkString = "Incorrect format"
            self.tk_console_string_output.set(self.output_to_tkString)
        else:
            self.output_to_tkString = self.arit.trans_to_req_num_sys(self.output_to_tkString)
            self.tk_console_string_output.set(self.output_to_tkString)
ProcessingUnit = conversions()
main_console = console_manager(ProcessingUnit)
main_console.window.mainloop()