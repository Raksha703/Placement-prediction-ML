import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
        <h2 style="color:black; text-align:center">Campus Placement Prediction</h2>
    </div>
        """
        
    st.markdown(html_temp, unsafe_allow_html=True)
    
    model = joblib.load('model_campus_placement')
    
    #gender
    s1=st.selectbox("Sex",("Male","Female"))
    if s1=="Male":
        p1=1
    else:
        p1=0
    
    #10th
    p2 = st.slider("Enter Your 10th Percentage",0,100)
    
    #10th board
    s2=st.selectbox("10th Board",("Central","Others"))
    if s2=="Central":
        p3=1
    else:
        p3=0
    
    #12th
    p4 = st.slider("Enter Your 12th Percentage",0,100)
    
    
    #12th board
    s3=st.selectbox("12th Board",("Central","Others"))
    if s3=="Central":
        p5=1
    else:
        p5=0
    
    #specialization in higher edu
    s4=st.selectbox("Specialzation in Higher Secondary Education",("Science","Commerce","Arts"))
    if s4=="Science":
        p6=2
    elif s4 == "Commerce":
        p6=1    
    else:
        p6=0
    
    
    #degree %
    p7 = st.slider("Enter Your Degree Percentage",0,100)
    
    
    #ug
    s5=st.selectbox("Under Graduation(Degree type)- Field of degree education",("Sci&Tech","Comm&Mgmt","Others"))
    if s5=="Sci&Tech":
        p8=2
    elif s5=="Comm&Mgmt":
        p8=1
    else:
        p8=0
    
    
    #work experience
    s6=st.selectbox("Work Experience",("Yes","No"))
    if s6=="Yes":
        p9=1
    else:
        p9=0
    
    
    #test %
    p10 = st.slider("Enter Your Test Percentage",0,100)
    
    
    #branch
    s7=st.selectbox("Work Experience",("Mkt&HR","Mky&Fin"))
    if s7=="Mkt&HR":
        p11=1
    else:
        p11=0
    
    
    #mba %
    p12 = st.slider("Enter Your MBA Percentage",0,100)    
    
    
    if st.button('Predict'):
        prediction = model.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]])
        st.balloons()
        st.success('Campus Placement Prediction '.format(round(prediction[0],2)))
    

if __name__ == '__main__':
    main()