import tkinter as tk
import joblib
import sklearn
# Load the model
model = joblib.load('/content/caffeine.csv')
# Define the function to check caffeine content

def predict_caffeine(drink, Volume, Calories, Coffee, EnergyDrinks, EnergyShots, SoftDrinks, Tea, Water):
    drink = mapping[drink]-1
    pre = mod.predict([[drink, Volume, Calories, Coffee, EnergyDrinks, EnergyShots, SoftDrinks, Tea, Water]])
    return "High Caffeine Content" if pre == 1 else "Low Caffeine Content"


# Create a tkinter window
'''window = tk.Tk()
window.title("Credit Card Fraud Detection System")

# Create input fields
amount_label = tk.Label(window, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(window)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

grade_label = tk.Label(window, text="Grade:")
grade_label.grid(row=1, column=0, padx=10, pady=10)
grade_entry = tk.Entry(window)
grade_entry.grid(row=1, column=1, padx=10, pady=10)

years_label = tk.Label(window, text="Years:")
years_label.grid(row=2, column=0, padx=10, pady=10)
years_entry = tk.Entry(window)
years_entry.grid(row=2, column=1, padx=10, pady=10)

ownership_label = tk.Label(window, text="Ownership:")
ownership_label.grid(row=3, column=0, padx=10, pady=10)
ownership_entry = tk.Entry(window)
ownership_entry.grid(row=3, column=1, padx=10, pady=10)

income_label = tk.Label(window, text="Income:")
income_label.grid(row=4, column=0, padx=10, pady=10)
income_entry = tk.Entry(window)
income_entry.grid(row=4, column=1, padx=10, pady=10)

age_label = tk.Label(window, text="Age:")
age_label.grid(row=5, column=0, padx=10, pady=10)
age_entry = tk.Entry(window)
age_entry.grid(row=5, column=1, padx=10, pady=10)

# Create the button to detect fraud
detect_button = tk.Button(window, text="Detect Fraud", command=detect_fraud)
detect_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create the label to display the result
result_label = tk.Label(window, text="")
result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)'''
# Create the Tkinter interface
root = tk.Tk()
root.title("Caffeine Content Predictor")

# Define the input widgets
drink_label = tk.Label(root, text="Drink:")
drink_entry = tk.Entry(root)

volume_label = tk.Label(root, text="Volume:")
volume_entry = tk.Entry(root)

calories_label = tk.Label(root, text="Calories:")
calories_entry = tk.Entry(root)

coffee_label = tk.Label(root, text="Coffee:")
coffee_entry = tk.Entry(root)

energy_drinks_label = tk.Label(root, text="Energy Drinks:")
energy_drinks_entry = tk.Entry(root)

energy_shots_label = tk.Label(root, text="Energy Shots:")
energy_shots_entry = tk.Entry(root)

soft_drinks_label = tk.Label(root, text="Soft Drinks:")
soft_drinks_entry = tk.Entry(root)

tea_label = tk.Label(root, text="Tea:")
tea_entry = tk.Entry(root)

water_label = tk.Label(root, text="Water:")
water_entry = tk.Entry(root)

# Define the output widget
output_label = tk.Label(root, text="Caffeine Prediction:")
output_text = tk.Text(root, height=1, width=30)

# Define the predict function
def predict():
    drink = drink_entry.get()
    volume = float(volume_entry.get())
    calories = float(calories_entry.get())
    coffee = float(coffee_entry.get())
    energy_drinks = float(energy_drinks_entry.get())
    energy_shots = float(energy_shots_entry.get())
    soft_drinks = float(soft_drinks_entry.get())
    tea = float(tea_entry.get())
    water = float(water_entry.get())
    result = predict_caffeine(drink, volume, calories, coffee, energy_drinks, energy_shots, soft_drinks, tea, water)
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, result)

# Start the main loop of the window
window.mainloop()