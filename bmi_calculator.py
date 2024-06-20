import tkinter

window = tkinter.Tk()
window.minsize(width=400,height=300)
window.title("BMI Calculator")
window.config(padx=50,pady=50)

FONT = ("Arial",12,"normal") #Font appearance --> "normal" , "bold" , etc.
def calculate_BMI_score():
    window.update()
    remove_label_text()
    try:
        weight = float(weightEntry.get())
        height = float(heightEntry.get())
        height = float(height / 100) # converting from cm to meter
        if weight > 0 and height > 0:
            BMI = weight / pow(height,2)
            if BMI < 18.5:
                BMI_result(BMI, weightTypeList[0])
            elif BMI >= 18.5 and BMI <= 24.99:
                BMI_result(BMI, weightTypeList[1])
            elif BMI >= 25 and BMI <= 29.99:
                BMI_result(BMI, weightTypeList[2])
            elif BMI >= 30 and BMI <= 34.99:
                BMI_result(BMI, weightTypeList[3])
            elif BMI >= 35 and BMI <= 39.99:
                BMI_result(BMI, weightTypeList[4])
            elif BMI >= 40:
                BMI_result(BMI, weightTypeList[5])
        elif weight == 0 or height == 0:
            errors_value_taken(errorList[3])
        elif weight < 0 and height < 0:
            errors_value_taken(errorList[2])
        elif weight > 0 and height < 0:
            errors_value_taken(errorList[1])
        elif weight < 0 and height > 0:
            errors_value_taken(errorList[0])
    except:
        errors_value_taken(errorList[4])

weightLabel = tkinter.Label(text="Enter your Weight (kg)", font=FONT)
weightLabel.pack(side="top")

weightEntry = tkinter.Entry(width=20, font=FONT)
weightEntry.pack(side="top")

heightLabel = tkinter.Label(text="Enter your Height (cm)", font=FONT)
heightLabel.pack(side="top")

heightEntry = tkinter.Entry(width=20, font=FONT)
heightEntry.pack(side="top")

calculatorButton = tkinter.Button(text="Calculate", command=calculate_BMI_score)
calculatorButton.pack(side="top")

resultLabel = tkinter.Label(text="", font=FONT)
resultLabel.pack()
resultLabel2 = tkinter.Label(text="", font=FONT)
resultLabel2.pack()

weightTypeList = ["Underweight","Optimum range", "Overweight", "Class 1 obesity", "Class 2 obesity", "Class 3 obesity"]
errorList = ["Please enter your weight value as positive",
             "Please enter your height value as positive",
             "Please enter your features as positive",
             "Please enter your features greater than 0!",
             "Please enter your features as number!"]
def errors_value_taken(string):
    if string == errorList[4]:
        resultLabel.config(text=string)
        resultLabel.pack()
    else:
        resultLabel.config(text=string)
        resultLabel.pack()
def BMI_result(BMI,weightType):
    resultLabel.config(text=f"Your BMI score is: {BMI:.2f}")
    resultLabel2.config(text=f" You are {weightType} !")
def remove_label_text():
    resultLabel.config(text="")
    resultLabel2.config(text="")

window.mainloop()