def calculate_bmi(height, weight):
  print("Height = " + str(height))
  print("Weight = " + str(weight))
  #Add code here to calculate BMI
  bmi = weight / (height * height)
  #Add code here to display calculate BMI
  print("BMI = " + str(bmi))

  if bmi <18.5:
    print("Underweight")
    return -1
  elif bmi < 25:
    print("Normal weight")
    return 0
  elif bmi >= 25:
    print("Overweight")
    return 1
# Test the function

calculate_bmi(1.73, 57)