
# Importing necessary libraries
import streamlit as st
import pandas as pd
import joblib
import sklearn
import imblearn

# Loading Model & feature name in:
model = joblib.load("Model.pkl")
feature_in = joblib.load("Features.pkl")

# Creating Prediction Function:
def prediction(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,
               LoanAmount,Credit_History,Property_Area,Loan_Amount_Term_category):
    
    # Creating data frame recive user input and deliver input to the model for preduction
    df = pd.DataFrame(columns=feature_in)
    df.at[0,'Gender'] = Gender
    df.at[0,'Married'] = Married
    df.at[0,'Dependents'] = Dependents
    df.at[0,'Education'] = Education
    df.at[0,'Self_Employed'] = Self_Employed
    df.at[0,'ApplicantIncome'] = ApplicantIncome
    df.at[0,'CoapplicantIncome'] = CoapplicantIncome
    df.at[0,'LoanAmount'] = LoanAmount
    df.at[0,'Credit_History'] = Credit_History
    df.at[0,'Property_Area'] = Property_Area
    df.at[0,'Loan_Amount_Term_category'] = Loan_Amount_Term_category
    
    result = model.predict(df)
    return result[0]
    
    
# Creating a main function involves designing a user interface for feature input using Streamlit. 
# Based on the input provided by the user, the model will make predictions.
def main():
    st.title("Loan Status Prediction Model")
    st.text("The model shows an accuracy score of approximately 77.6% for loan approval status \nduring testing.")
    st.text('''Analysis Sumary:\n
As a summary, we can say that applicants applying for a house loan with the\nfollowing characteristics have a chance of acceptance or rejection as follows:

* If they are married, have 2 or 0 dependents, have a high level of education or \ngraduates, fall into the medium or large CoapplicantIncome_category \n(greater than 1188), apply for a medium or small loan amount (less than or equal \nto 168,000), choose a medium or short loan term (less than or equal to 360 months), \nmeet the credit history guidelines (Credit_History == 1), and apply for a property \narea in a semi-urban area, applicants with these characteristics have a greater \nchance of loan approval or acceptance.\n
* If they are not married, have 1 or 3 dependents, have a low level of education \nor are not graduates, fall into the small CoapplicantIncome_category \n(less than or equal to 1188), apply for a large loan amount (greater than 168,000), \nchoose a long loan term (greater than 360 months), do not meet the credit history \nguidelines (Credit_History == 0), and apply for a property area in a rural area, \napplicants with these characteristics have a greater chance of their loan not being \napproved or not accepted.''')
    Gender = st.selectbox('Applicant Gender',['Male','Female'])
    Married = st.selectbox('Married Status', ['Yes','No'])
    Dependents = st.selectbox("Select Number of Dependents (*Notice: The maximum number '3' indicates '3 or more'.)", [0,1,2,3])
    Education = st.selectbox("Education Status", ['Graduate','Not Graduate'])
    Self_Employed = st.selectbox("Self_Employed Status",['No','Yes'])
    ApplicantIncome = st.number_input("Enter Applicant Income")
    CoapplicantIncome = st.number_input("Enter Coapplicant Income")
    LoanAmount = st.slider("Enter Loan Amont in Thousands", min_value=5, max_value=800, value= 100, step=1)
    Credit_History = st.selectbox("Enter Credit_History Status", [1,0])
    Property_Area = st.selectbox("Enter Property Area", ['Semiurban','Urban','Rural'])
    Loan_Amount_Term_category = st.selectbox('''Enter Loan Term Period:
    Short: ≤ 180 Months, Medium: 180 < Months ≤ 360, Long: > 360 Months''', ['Short','Medium','Long'])
    
    if st.button("Predict"):
        Results = prediction(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,
               LoanAmount,Credit_History,Property_Area,Loan_Amount_Term_category)
        loan_status_list = ["Sorry Your Loan Request Rejected" , "Your Loan Request Accepted"]
        st.text(loan_status_list[Results])

main()
