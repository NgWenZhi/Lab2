print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
  print("display_main_menu")
  print("Enter some numbers separated by commas (e.g. 5, 32, 12, 4)")
        
def calc_average(stringlist):
  print("calc_average")
  total = 0.0
  for eachstr in stringlist:
     total = total + float(eachstr)

  average = total / len(stringlist)
  print("Average = ", average)
  return average

   

def find_min_max(stringlist):
    print("find_min_max")
    floatlist = [] #Define an empty list
    for eachstr in stringlist:
        floatlist.append(float(eachstr))
    
    floatlist.sort()
    print("MIN = ", floatlist[0])
    print("MAX = ", floatlist[-1])
    return (floatlist[0], floatlist[-1])

def get_user_input():
    print("get_user_input")
    inputstr = input()
    strlist = inputstr.split(",")
    print(strlist)
    return strlist


def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

def main():
    print("Ex3")
    display_main_menu()
    temp_list = get_user_input()
    calc_average(temp_list)
    find_min_max(temp_list)

if __name__ == "__main__":
 main()