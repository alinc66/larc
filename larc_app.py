import streamlit as st
import pandas as pd
import joblib
from PIL import Image

#Loading Our final trained Knn model 
model= open("LARC.pickle.dat", "rb")
knn_clf=joblib.load(model)


st.title("Neoadjuvant Chemoradiotherapy LARC Classification App")

#Loading images

setosa= Image.open('0.png')
versicolor= Image.open('1.png')

st.sidebar.title("Features")

#Intializing
parameter_list=['sex','pT','pN','i_limfatica','i_venoasa','i_perineurala','grading','varsta','RT_CHIR']
parameter_input_values=[]
parameter_default_values=['1','2','0','0','1','0','3','77','29']

values=[]

#Display
for parameter, parameter_df in zip(parameter_list, parameter_default_values):
	
	values= st.sidebar.slider(label=parameter, key=parameter,value=float(parameter_df), min_value=0.0, max_value=90.0, step=1.0)
	parameter_input_values.append(values)
	
input_variables=pd.DataFrame([parameter_input_values],columns=parameter_list,dtype=float)
st.write('\n\n')

if st.button("Click Here to Predict TRG"):
	prediction = knn_clf.predict(input_variables)
	st.image(setosa) if prediction == 0 else st.image(versicolor)
