'''Student Grades Tracker: Create a dictionary where the keys are student names, and the values are their grades. Write a function that allows you to:

Add a new student and grade.
Update an existing student's grade.
Remove a student from the dictionary.
Find the student with the highest grade.'''

student_grade = {"Ritu": 4 , "Jyoti" : 1 , "Gitya": 3, "Vishwa": 2, "Rani": 6}
# new = input("enter new name ")
# grade = input("enter new grade ")
# student_grade.update({new:grade}) #Add a new student and grade
# student_grade.update({"Ritu":"A+"}) #Update an existing student's grade.
student_grade.pop("Jyoti") #Remove a student from the dictionary
max_student = min(student_grade, key=student_grade.get)  # Get the key of the highest value
max_grade = student_grade[max_student]
print(max_student, max_grade)
print(student_grade)

'''Product Inventory: Build a dictionary where the keys are product IDs, and the values are product details (e.g., name, price, stock). Then:

Write a function to update the stock of a product.
Write another function to display all products with stock less than 10.'''

product_inv  = {
    "ProdA" : {"Name": "nameA","Price" : "$34" ,"stock": 50},
    "ProdB" : {"Name": "nameB","Price" : "$30" ,"stock": 5}
}

product_inv["ProdA"]["stock"] = 60

products_in_stock = {}
if product_inv["ProdA"]["stock"] < 10:
    products_in_stock["ProdA"] = product_inv["ProdA"]
if product_inv["ProdB"]["stock"] < 10:
    products_in_stock["ProdB"] = product_inv["ProdB"]
print(products_in_stock)
