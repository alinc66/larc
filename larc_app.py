import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Loading Our final trained Knn model 
# model= open("LARC1.pickle.dat.pkl", "rb")
model= open("LARC.pickle.dat", "rb")
# xgb_clf=joblib.load(model)


#Caching the model for faster loading
@st.cache


# Define the prediction function
def predict(sex, pT, pN, i_limfatica, i_venoasa, i_perineurala, grading, varsta, RT_CHIR):
    #Predicting the categorial features

    if sex == 'Female':
        sex = 0
    elif sex == 'Male':
        sex = 1

    if pT == '0':
        pT = 0
    elif pT == '1':
        pT = 1
    elif pT == '2':
        pT = 2
    elif pT == '3':
        pT = 3
    elif pT == '4':
        pT = 4

    if pN == '0':
        pN = 0
    elif pN == '1':
        pN = 1
    elif pN == '2':
        pN = 2

    if i_limfatica == '0':
        i_limfatica = 0
    elif i_limfatica == '1':
        i_limfatica = 1

    if i_venoasa == '0':
        i_venoasa = 0
    elif i_venoasa == '1':
        i_venoasa = 1

    if i_perineurala == '0':
        i_perineurala = 0
    elif i_perineurala == '1':
        i_perineurala = 1

    if grading == '1':
        grading = 1
    elif grading == '2':
        grading = 2
    elif grading == '3':
        grading = 3
    elif grading == '4':
        grading = 4
    
 
    prediction = model.predict(pd.DataFrame([[sex, pT, pN, i_limfatica, i_venoasa, i_perineurala, grading, varsta, RT_CHIR]], columns=['Sex (M/F)', 'pT', 'pN', 'invazie limfatica', 'invazie venoasa', 'invazie perineurala', 'Grading', 'Varsta', 'RT-CHIR']))
    return prediction


st.title('Locally Advanced Rectal Cancer TRG Classification App Predictor')
st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")
st.header('Enter the features of the patient:')

sex = st.selectbox('Sex:', ['Female', 'Male'])
pT = st.selectbox('pT:', ['0', '1', '2', '3', '4'])
pN = st.selectbox('pN:', ['0', '1', '2'])
i_limfatica = st.selectbox('Invazie limfatica:', ['0', '1'])
i_venoasa = st.selectbox('Invazie venoasa:', ['0', '1'])
i_perineurala = st.selectbox('Invazie perineurala:', ['0', '1'])
grading = st.selectbox('Grading:', ['1', '2', '3', '4'])
varsta = st.number_input('Varsta in ani:', min_value=20.0, max_value=90.0, value=1.0)
RT_CHIR = st.number_input('RT-CHIR in zile:', min_value=20.0, max_value=90.0, value=1.0)


if st.button('Predict TRG'):
    price = predict(sex, pT, pN, i_limfatica, i_venoasa, i_perineurala, grading, varsta, RT_CHIR)
    st.success(f'The predicted TRG of the patient is ${price[0]:.2f} USD')
