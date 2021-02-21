import numexpr as ne

givenX = float (input("value x0: "))
xn = float (input ("Value x: "))
yn = float (input ("Value y: "))
h = float(input("Step: "))
method = int(input("Enter 1 for Modified Euler / 2 for Runge Kutta: "))
function = input("Enter differential equation as numexpr notation: ")

def f(x, y):
    function1 = ne.evaluate(function)
    return function1    

if (method == 1):
    def predictor(x, y, h): 
        y1predict = y + h * f(x, y) 
        return y1predict

    def corrector(x, y, x1, y1, h): 
        y1correct = y1

        while (abs(y1correct - y1) > 1): 
            y1 = y1correct
            y1correct = y + 0.5 * h * (f(x, y) + f(x1, y1))  
        return y1correct
  
    def modEuler(x, xn, y, h): 
        while (x < xn): 
            x1 = x + h 
            y1predict = predictor(x, y, h) 
            y1correct = corrector(x, y, x1, y1predict, h) 
            x = x1 
            y = y1correct
        print(y)
    modEuler(xn, givenX, yn, h)              
else:
    def rungeKutta(xn, yn, x, h): 
        step = (int)((x - xn)/h)   
        y = yn 
        for i in range(1, step + 1): 

            k1 = h * f(xn, y) 
            k2 = h * f(xn + 0.5 * h, y + 0.5 * k1) 
            k3 = h * f(xn + 0.5 * h, y + 0.5 * k2) 
            k4 = h * f(xn + h, y + k3) 
    
            y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
    
            xn = xn + h 
        return y 
    print (rungeKutta(givenX, yn, xn, h))