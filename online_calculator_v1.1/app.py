from flask import Flask, render_template, request

app = Flask(__name__)



# Home page function


@app.route("/")
def home():

    return render_template("index.html")
    
    
# Calculator function

@app.route("/math",methods=['POST'])
def online_calculator():

    if (request.method=="POST"):
    
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])

        if operation=="addition":
        
            result = num1+num2
            
        elif operation=="substraction":
        
            result = num1-num2


        elif operation=="multiplication":
        
            result = num1*num2
                
        elif operation=="division":
        
            result = num1/num2


        # Logging in CSV file

        f=open("log.csv",'a')
        f.write("data: "+","+str(operation)+","+str(num1)+","+str(num2)+","+str(result)+"\n")
        f.close()


        content={"num1":num1, "num2":num2, "result":result}

    
    return render_template("index.html", **content)

   
        

    
if __name__=="__main__":

    app.run(host="0.0.0.0",port=5000)
