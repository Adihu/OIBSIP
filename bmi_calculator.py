def calculate_bmi():
    print("=== BMI CALCULATOR ===")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters (e.g., 1.75): "))
        
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be greater than zero.")
            return
        
        bmi = weight / (height ** 2)
        print(f"\nYour BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            category = "Normal weight"
        elif 25 <= bmi <= 29.9:
            category = "Overweight"
        else:
            category = "Obese"
            
        print(f"Health Category: {category}")
        
    except ValueError:
        print("Error: Please enter valid numeric numbers only.")

if __name__ == "__main__":
    calculate_bmi()