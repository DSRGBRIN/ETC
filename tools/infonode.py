from flask import *
import sys
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    import platform
    name = platform.system() + "-" + platform.node()
    
app = Flask(__name__) 
@app.route('/') 
def home():
	return "Welcome to the "+ name +"!!"

@app.route('/info', methods = ['GET']) 
def backup():
    dt = []
    from subprocess import check_output
    if platform.system() == "Windows":
        out = check_output(["ipconfig", "-all"]).decode("utf-8")
        stro = out.replace("\r\n", "<br>").split("<br>")
        for i in range(len(stro)):
            if stro[i].find("v4 Address")>0:
                dt.append(stro[i])

    else:
        out = check_output(["ifconfig", "-a"]).decode("utf-8")
        stro = out.replace("\r\n", "<br>").split("<br>")
        for i in range(len(stro)):
            if stro[i].find("inet ")>0:
                dt.append(stro[i])
           
    print("<br>".join(dt))
    return "Info:<br>"+"<br>".join(dt)
		
if __name__ == '__main__': 
    print("6001")
    #app.run(host="0.0.0.0", port=9999, debug=True)
    app.run(host="127.0.0.1", port=9999, debug=True)
    
    
