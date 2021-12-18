import zenoBasic
import os

while True:
    text = input("zeno > ")

    

    result, error = zenoBasic.run(os.getcwd(), text)

    if error: print(error.as_string())
    else: print(result)

    
