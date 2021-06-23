from flask import Flask, send_from_directory
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH,start_server
from pywebio.input import *
from pywebio.output import *
import argparse
import pickle
app=Flask(__name__)
model= pickle.load(open('model7.pkl','rb'))
def predict():
    gender=radio("Select your gender",["Male","Female"])
    if gender=="Male":
        g=1
    else:
        g=0
    married=radio("Marriage Status",["Yes","No"])
    if married=="Yes":
        m=1
    else:
        m=0
    dep=input("Enter number of dependents from 0 to 3",type=NUMBER)
    edu=radio("Educated?",["Yes","No"])
    if edu=="Yes":
        e=1
    else:
        e=0
    emp=radio("Are you self_employed",["Yes","No"])
    if emp=="Yes":
        s=1
    else:
        s=0
    income=input("Enter the applicant income",type=NUMBER)
    income1=input("Enter the co-applicant income",type=FLOAT)
    amt=input("Enter the loan amount",type=FLOAT)
    term=input("Enter the loan amount term",type=FLOAT)
    cr=input("Enter the credit history 0.0 or 1.0",type=FLOAT)
    area=radio("Choose the area",["Urban","Rural","Semiurban"])
    if area=="Urban":
        a=0
    elif area=="Rural":
        a=1
    else:
        a=2
    output=model.predict([[g,m,dep,e,s,income,income1,amt,term,cr,a]])
    output=int(output)
    if output=="1":
        put_text("You have taken a loan")
    else:
        put_text("No loan taken")
app.add_url_rule('/tool', 'webio_view',webio_view(predict),methods=['GET','POST','OPTIONS'])
if __name__=='__main__':
    arg=argparse.ArgumentParser()
    arg.add_argument("-p", "--port",default=8080)
    args=arg.parse_args()
    start_server(predict,port=args.port)
    #predict()