import streamlit as st
import joblib

def main():
    # Styling
    st.markdown(
        """
        <style>
        .header {
            background-color: lightblue;
            padding: 16px;
            border-radius: 10px;
            margin-bottom: 20px;
            display: flex;
            align-items: center; /* Center items vertically */
            justify-content: center; /* Center items horizontally */
        }
        .instruction {
            margin-bottom: 10px;
        }
        .label-italic {
            font-style: italic;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header
    st.markdown(
        """
        <div class="header">
            <h2 style="color:black; text-align:center">Campus Placement Prediction</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    model = joblib.load('model_campus_placement')

    # Gender Section
    st.subheader("Personal Information")
    gender = st.selectbox("*Sex*", ("Male", "Female"))
    gender_code = 1 if gender == "Male" else 0

    # 10th Section
    st.subheader("10th Standard")
    tenth_percentage = st.slider("*Enter Your 10th Percentage*", 0, 100)

    # 10th board
    tenth_board = st.selectbox("*10th Board*", ("Central", "Others"))
    tenth_board_code = 1 if tenth_board == "Central" else 0

    # 12th Section
    st.subheader("Higher Secondary Education")
    twelfth_percentage = st.slider("*Enter Your 12th Percentage*", 0, 100)

    # 12th board
    twelfth_board = st.selectbox("*12th Board*", ("Central", "Others"))
    twelfth_board_code = 1 if twelfth_board == "Central" else 0

    specialization = st.selectbox("*Specialization*", ("Science", "Commerce", "Arts"))
    specialization_code = {"Science": 2, "Commerce": 1, "Arts": 0}[specialization]

    # Degree Section
    st.subheader("Undergraduate Degree")
    degree_percentage = st.slider("*Enter Your Percentage*", 0, 100)

    # Field of degree education
    degree_field = st.selectbox("*Field of Degree Education*", ("Science & Technology", "Commerce & Management", "Others"))
    degree_field_code = {"Science & Technology": 2, "Commerce & Management": 1, "Others": 0}[degree_field]

    # Work Experience Section
    st.subheader("Work Experience")
    work_experience = st.selectbox("*Do You Have Any Work Experience?*", ("Yes", "No"))
    work_experience_code = 1 if work_experience == "Yes" else 0

    # Test Scores Section
    st.subheader("Rate Yourself on the basis of Communication skills")
    test_percentage = st.slider("*Enter*", 0, 100)

    # MBA specialization Section
    st.subheader("Member of which CLUBS/SOCIETIES")
    mba_specialization = st.selectbox("", ("Technical", "Non-Technical"))
    mba_specialization_code = 1 if mba_specialization == "Technical" else 0

    # MBA Percentage Section
    mba_percentage = st.slider("*Rate Yourself on the basis of on field experiences*", 0, 100)

    if st.button('Predict'):
        prediction = model.predict([[gender_code, tenth_percentage, tenth_board_code, 
                                     twelfth_percentage, twelfth_board_code, specialization_code,
                                     degree_percentage, degree_field_code, work_experience_code,
                                     test_percentage, mba_specialization_code, mba_percentage]])
        st.balloons()
        if prediction[0] == 1:
            st.success('High chances of campus placement!')
        else:
            st.error('Low chances of campus placement!')

if __name__ == '__main__':
    main()
