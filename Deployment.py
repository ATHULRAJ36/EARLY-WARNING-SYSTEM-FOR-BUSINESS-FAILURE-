import streamlit as st
import joblib
model=joblib.load("EARLY_WARNING_SYSTEM_FOR_BUSINESS_FAILURE_DETECTION.pkl")
l1=joblib.load("lb1.pkl")
l2=joblib.load("lb2.pkl")
l3=joblib.load("lb3.pkl")
l4=joblib.load("lb4.pkl")
s=joblib.load("sc.pkl")

st.title("EARLY_WARNING_SYSTEM_FOR_BUSINESS_FAILURE_DETECTION")
st.write("Enter Data Description")

company_age=st.number_input('Enter company age')
revenue_growth=st.number_input('Enter revenue growth')
profit_margin=st.number_input('Enter profit margin')
debt_to_equity=st.number_input('Enter debt to equity')
current_ratio=st.number_input('Enter current ratio')
cash_flow=st.number_input('Enter cash flow')
interest_coverage=st.number_input('Enter interest coverage')
employee_count=st.number_input('Enter employee count')
market_volatility=st.number_input('Enter market volatility')
payment_delays=st.number_input('Enter payment delays')
industry=st.selectbox('Enter industry type',['Manufacturing','Retail','Healthcare','Construction','Logistics'])       
company_size=st.selectbox('Enter company size',['Small','Medium','Large'])
region=st.selectbox('Enter region',['South','North','West','East'])
ownership_type=st.selectbox('Enter ownership type',['Private','Public','Partnership','Startup'])

industry=l1.transform([industry])[0]
company_size=l2.transform([company_size])[0]
region=l3.transform([region])[0]
ownership_type=l4.transform([ownership_type])[0]
if st.button('predict'):
    result=model.predict(s.transform([[company_age,revenue_growth,profit_margin,debt_to_equity,current_ratio,cash_flow,interest_coverage,employee_count,
                                       market_volatility,payment_delays,industry,company_size,region,ownership_type]]))[0]
    if result == 0:
        output = 'Will not fail'
    else:
        output = 'Fail'
    st.success(f'the output is: {output}')
    
    
                                       
   
    
   