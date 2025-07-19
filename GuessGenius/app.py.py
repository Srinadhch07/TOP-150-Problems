import random
import tkinter as tk
from tkinter import messagebox
import google.generativeai as genai
import base64
import socket

unique_value = random.randint(0,50)
score_value = 0
life_lines = 5
hint = "Try a Wild guess in the range of 0-100!"

root = tk.Tk()
root.title("GuessGenius")
#root.attributes("-fullscreen",True)
#root.bind("<Escape>",lambda event:root.attributes("-fullscreen",False))
root.state("zoomed")


#Setting elements in middle
root.grid_rowconfigure(0,weight=0)
root.grid_rowconfigure(1,weight=0)
root.grid_rowconfigure(2,weight=0)
root.grid_rowconfigure(3,weight=0)
root.grid_rowconfigure(4,weight=0)

root.grid_columnconfigure(0,weight=1)



# Method for internet Connection

def is_internet_available():
	try:
		socket.create_connection(("8.8.8.8",53),timeout=3)
		return True
	except OSError:
		return False

# Hint generators

def offline_hint_generator():
	user_input = entry.get()
	user_input = int(user_input)
	difference = abs(user_input-unique_value)
	hint = f"Hint: The Differnce is {difference}"
	#hint_label.configure(text=hint)
	return hint


def hint_generator():
	prompt = f"""You are a hint generator for a number guessing game.  The secret number is between 1 and 9999.  Provide a creative and challenging hint that relates to the number, but doesn't give it away directly.  The hint should be something that requires research or knowledge to connect to the number.  Vary the types of hints you give (history, science ,math etc.)
Number to be guessed:{unique_value}
Score :{score_value}

Give is hints.
Now generate a hint for given  number.

Note:Do not Give answer. The hint should be very accurate to the number generated.
"""
	# Generate Hint
	convo.send_message(prompt)
	hint=str(convo.last.text).replace("**","")
	return hint

def hint_answer():
	global hint
	convo.send_message("The game is Over. Now tell me the and Explain about hint in not more than 2 lines.")
	explanation = str(convo.last.text).replace("**","")
	return explanation


def process_input():
	global score_value
	global unique_value
	global life_lines
	global hint
	
	try:
		user_input = entry.get()
		num1 = int(user_input)
		if num1 == unique_value:	
			output_label.config(text=f"You're Right",fg="blue",font=("Arial",10))
			score_value +=1
			score_output.config(text=f"Score: {score_value}")
			# Generate unique value to continue
			unique_value = random.randint(1,3)
			# Generator hint
			if is_internet_available():
				hint = hint_generator()
			else:
				hint = offline_hint_generator()
				print(hint)
			hint_label.config(text=hint)
		else:	
			life_lines -=1
			if life_lines <= 0:
				output_label.config(text=f"GAME OVER",fg="red",font=("Arial",30,"bold"))
				
				entry.grid_forget()
				process_button.grid_forget()
				if is_internet_available():
					explanation_label = tk.Label(root,text=hint_answer(),font=("Times New Roman",15,"bold"))
					explanation_label.grid(row=8,column=0,pady=10)
				

			else:
				life_line_label.config(text=f"Life lines :{life_lines}")
				output_label.config(text=f"Oops Wrong Number. You have more {life_lines}")

				if not is_internet_available():
					hint=offline_hint_generator()
					hint_label.config(text=hint)
					
		# clear the Entry field
		entry.delete(0,tk.END)
	except ValueError:
		messagebox.showerror("Value Check","Please enter a valid number")



	

#User Interface

#Ttile
title = tk.Label(root,text="GuessGenius",font=("Arial",50,"bold italic"))
title.grid(row=0,column=0,pady=100)

# Input Labels and Entry field
input_label =tk.Label(root,text="Guess the Number",font=("Arial",14,"bold"))
input_label.grid(row=1,column=0,pady=15)

entry = tk.Entry(root,width=10,font=("Arial",14),bd=5,relief="ridge")
entry.grid(row=2,column=0,pady=10)

#life line Label
life_line_label = tk.Label(root,text=f"Life lines :{life_lines}",font=("Arial",10))
#life_line_label.grid(rows=3,column=0,pady=10)

#Button to process input
process_button = tk.Button(root,text ="Check",font=("Arial",10,"bold"),fg="white",bg="green",command=process_input,width=15)
process_button.grid(row=4,column=0,pady=10)

#output Label
output_label = tk.Label(root,text="Welcome to GuessGenius",fg="blue",font=("Arial",10))
output_label.grid(row=5,column=0,pady=10)	

# Network Connetion check

if not is_internet_available():
	output_label.config(text="We're on offline mode.")
	
else:
	try:
		genai.configure(api_key=base64.b64decode(" QUl6YVN5Qmx2Z1VRaDVZTHo3QjhtanVMcUJlcjgtX0I1OUYxMWNF").decode('utf-8'))
		model = genai.GenerativeModel(
		model_name="gemini-1.5-flash")
		convo = model.start_chat(history=[])
		output_label.config(text="Welcome to GuessGenius")
		hint = hint_generator()
	except Exception:
		output_label.config(text="Server is busy! Try again later")


#Hint Label
hint_label = tk.Label(root,text=hint,font=("Arial",10))
hint_label.grid(row=6,column=0,pady=10)

#Score output
score_output = tk.Label(root,text ="Score: 0",fg="green",font=("Airal",30,"bold"))
score_output.grid(row=7,column=0,pady=10)






root.mainloop()