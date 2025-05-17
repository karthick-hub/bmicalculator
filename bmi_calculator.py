def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in meters."""
    bmi = weight / (height ** 2)
    return bmi

def main():
    print("BMI Calculator")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 25:
            print("Category: Normal weight")
        elif 25 <= bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")
    except ValueError:
        print("Please enter valid numeric input.")

if __name__ == "__main__":
    main()
