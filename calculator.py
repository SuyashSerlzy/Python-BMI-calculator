from customtkinter import*
app = CTk()
app.title("BMI Calculator")
app.geometry("450x250")
set_appearance_mode("dark")
def calculate_bmi():
    try:
        height = float(height_entry.get()) 
        weight = float(weight_entry.get())  
        bmi = weight / (height ** 2)  
        if bmi < 18.5:
            result = "Underweight"
        elif bmi < 24.9:
            result = "Normal weight"
        elif bmi < 29.9:
            result = "Overweight"
        else:
            result = "Obesity"
        result_label.configure(text=f"BMI: {bmi:.2f}\n{result}")
    except:
        result_label.configure(text="Enter valid numbers")
frame = CTkFrame(master=app, fg_color="black", border_width=2, border_color="gray")
frame.pack(expand=True)
CTkLabel(master = frame, text="Height (m):").pack(anchor = "center", pady = 5)
height_entry = CTkEntry(master=frame)
height_entry.pack(anchor="center")
CTkLabel(master=frame, text="Weight (kg):").pack(anchor="center", pady = 5)
weight_entry = CTkEntry(master = frame)
weight_entry.pack()
CTkButton(master = frame, text="Calculate", command=calculate_bmi, border_width = 2, fg_color="black", hover_color="gray").pack(pady=10, padx = 40)
result_label = CTkLabel(master = frame, text="")
result_label.pack()
app.mainloop()
