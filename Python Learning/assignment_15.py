#PF-Assgn-15
'''
 Write a python program to find and display the product of three positive integer values based on the rule mentioned below:

It should display the product of the three values except when one of the integer value is 7. In that case, 7 should not be included in the product and the values to its left also should not be included.
If there is only one value to be considered, display that value itself. If no values can be included in the product, display -1.

Note: Assume that if 7 is one of the positive integer values, then it will occur only once. Refer the sample I/O given below. 
'''
def find_product(num1,num2,num3):
    product=0
    #write your logic here
    product=1
    arr=[num1,num2,num3]
    for i in arr:
        product=product*i
        if(i==7):
            product=1    
    if product==1:
        product=-1
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(7,4,3)
print(product)