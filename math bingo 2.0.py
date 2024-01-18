
# coding: utf-8

# In[1]:


def area_room():   
    #Area of a Room
    print('Welcome to the Room Area Calculator!')
    print('Ever wondered how much space your room occupies? Let find out!')
    
    #ask user to enter the length and width
    length=float(input('Please enter length here: '))
    width=float(input('Please enter width here: '))
    

    #display the values
    area=length*width
    print('Great! Your room has an area of',area)
    print('Thanks for using the Room Area Calculator!')

    print('*'*30)

def area_field():
    #Area of a field
    print('Welcome to the Field Area Calculator!')
    print('Fields come in all shapes and sizes. Lets figure out the area of yours!')
    #ask user to enter the length and width
    length=int(input('Please enter length here: '))
    width=int(input('Please enter width here: '))
    square_feet=43560
    #display the values
    area=length*width/square_feet
    print('Fantastic! The area of your field is',area)
    print('Thanks for using the Field Area Calculator!')
    print('*'*30)

def recycle_bot():
    #Bottle Deposits
    print('Welcome to the Recycling Refund Calculator!')
    print('Curious about how much you can get back for recycling? Lets find out!')
    value_less=0.10
    value_more=0.25
    #ask user to enter input
    less=int(input('Enter the number which is less than one litre: '))
    more=int(input('Enter the number which is more than one litre: '))
    refund=value_less*less+value_more*more
    print('Congratulations! Your recycling refund is',refund)
    print('Great job! Your efforts not only help the environment but also put some money back in your pocket.')
    print('*'*30)

def meal_cost():
    #Tax and Tip
    print('Welcome to the Fun Meal Cost Calculator!')
    print('Let me help you figure out the tax and tip for your delicious meal!')
    tax_rate=0.10
    tip_rate=0.18
    #ask user to enter cost
    cost=int(input('Enter the cost of your amazing meal: $'))
    #calculate the cost
    tax=cost*tax_rate
    tip=cost*tip_rate
    total=cost+tax+tip
    #display the output
    print('Calculating...')
    print('The Tax your meal cost',tax)
    print('The Tip your meal cost',tip)
    print('The Total Cost of your Fantastic Meal is: ',total)
    print('Enjoy your scrumptious meal!')
    
    print('*'*30)

def positive_integers():
    #sum of the first n positive integers
    print('Welcome to the Positive Integers Sum Calculator!')
    print('Lets make math more fun and exciting! This function helps you calculate')
    print('The sum of the first n positive integers, perfect for solving cool problems!')
    #ask the user to enter value in n variable
    n=int(input('Enter the value for n here: '))
    #compute the positive integers
    sum=(n)*(n+1)/2
    #display the output
    print('The sum of the first', n, 'positive integers is',sum)
    print('Wow! That was fun! Use this knowledge to conquer more math challenges!')
    print('*'*30)

def weight():
    #Widgets and Gizmos
    print('Welcome to the Weight Calculator!')
    print('Lets make weighing widgets and gizmos a blast!')
    print('This function will calculate the total weight with pinpoint accuracy!')

    #define vaiables
    widget=0.075
    gizmos=0.112
    #ask user to give his numbers
    user_widget=int(input('Please enter widget value here: '))
    user_gizmos=int(input('Please enter gizmos value here: '))
    #compute the total
    total_weight=(widget*user_widget)+(gizmos*user_gizmos)
    #display the output
    print('The total weight of the order: ',total_weight)
    print('Hooray! Youve just mastered the art of weighing widgets and gizmos!')
    print('*'*30)

def compound_interest():
    #Compound Interest
    print('Welcome to the Compound Interest Calculator!')
    print('Get ready to see your money grow over time!')
    print('Whether its savings accounts or investments, this tool makes it fun!')
    
    #ask the user to enter amount deposited
    user_deposit=int(input('Please enter the amount Deposited : '))
    interest=0.04
    n=int(input('enter the how many year you what here : '))
    #compute the vaules
    for i in range(1,n+1):
        amount=(user_deposit*(1+interest/100)**i)
        compound_int=(amount)-(user_deposit)
        #display the value
        print('Compound Interet for year',i,'is',round(compound_int,2))
    print('Woohoo! Watch your money grow! Invest wisely and enjoy the journey!')
    print('*'*30)
    
def arithmetic():
    #Arithmetic
    print('Welcome to the Fun Arithmetic Equation Generator!')
    print('Get ready for a magical journey through addition, subtraction, multiplication, division,')
    print('remainder, and logarithm!')

          #ask user to enter 2 variables a and b
    a=int(input('Enter the value for variable a:  '))
    b=int(input('Enter the value for variable b: '))
    sum=a+b
    print('Sum is',sum)
    difference=b-a
    print('Difference is',difference)
    product=a*b
    print('Product is',product)
    quotient=a//b
    print('Quotient is',quotient)
    remainder=a%b
    print('Remainder is',remainder)
    # log10(a)
    import math
    # Printing the log base 10 of a
    print ("Logarithm base 10 of a is : ",math.log2(a))
    result=a**b
    print('Result',result)
    print('Hooray! Youve just mastered the art of arithmetic! Keep rocking those equations!')
    print('*'*30)
    
def fuel_efficiency():
    #Fuel Efficiency
    print('Welcome to the Fuel Efficiency Converter!')
    print('Transforming fuel efficiency measures across borders!')
    print('Convert miles per gallon to Canadian units effortlessly!')
    #ask user to put value
    miles_per_gallon=float(input('Please enter value in miles/gallon here: '))
    #compute the value
    canadian_units=235.215/miles_per_gallon
    print('candian unit of fuel efficiency is',canadian_units)
    print('Fantastic! Now you can compare fuel efficiency globally! Drive on and save the planet!')
    

    print('*'*30)
    
def height_unit():    
    #Height Units
    print('Welcome to the Height Unit Converter!')
    print('Transforming height units for a heightier experience!')
    print('Convert feet and inches into centimeters effortlessly!')
    #take two values
    user_feet=int(input('number of feet: '))
    user_inches=int(input('number of inches: '))
    feet=12
    inche=2.54
    #compute the values
    centimeter=(user_feet*feet+user_inches)*inche
    #Display the values
    print('Centimeter=',round(centimeter,2))
    print('Fantastic! Now you can measure your height in centimeters and reach for the stars!')
    print('*'*30)
    
import tkinter as tk
#main window
window=tk.Tk()
#title change
window.title('Math Bingo')
#window size
window.geometry('580x450')
#label
tk.Label(window,text='Math Bingo',font=('Eras Bold ITC',20)).place(x=225,y=30)
#sublabel
tk.Label(window,text='Makes Math Easy and Fun!',font=('helvetica',10)).place(x=240,y=65)
#button
tk.Button(window,text='Room Space',width=20,height=2,command=area_room).place(x=50,y=130)
#button
tk.Button(window,text='Field Area',width=20,height=2,command=area_field).place(x=225,y=130)
#button
tk.Button(window,text='Refund',width=20,height=2,command=recycle_bot).place(x=400,y=130)
#button
tk.Button(window,text='Tax & Tip Calculator',width=20,height=2,command=meal_cost).place(x=50,y=200)
#button
tk.Button(window,text='Sum of Integers',width=20,height=2,command=positive_integers).place(x=225,y=200)
#button
tk.Button(window,text='Weight Calculator',width=20,height=2,command=weight).place(x=400,y=200)
#button
tk.Button(window,text='Compound Interest',width=20,height=2,command=compound_interest).place(x=50,y=275)
#button
tk.Button(window,text='Arithmetic Equation',width=20,height=2,command=arithmetic).place(x=225,y=275)
#button
tk.Button(window,text='Calculate Efficiency',width=20,height=2,command=fuel_efficiency).place(x=400,y=275)
#button
tk.Button(window,text='Height Conversion',width=20,height=2,command=height_unit).place(x=50,y=350)
#end loop
window.mainloop()

