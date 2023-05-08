import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Loading Our final trained Knn model 
# model= open("LARC1.pickle.dat", "rb")
model= open("LARC.pickle.dat", "rb")
gb_clf=joblib.load(model)


st.title("Neoadjuvant Radiochemotherapy for Locally Advanced Rectal Cancer Classification App")

#Loading images

setosa= Image.open('setosa.png')
versicolor= Image.open('versicolor.png')

st.sidebar.title("Features")

#Intializing
parameter_list=['Sex (F,M)','pT (0,1,2,3,4)','pN (0,1,2)','invazie limfatica (0,1)','invazie venoasa (0,1)','invazie perineurala (cm)','grading (1,2,3,4)','varsta (ani)','RT-CHIR (zile)']
parameter_input_values=[]
parameter_default_values=['1.0','0.0','0.0','0.0','0.0','0.0','2.0','64.0','33.0']

values=[]

#Display
for parameter, parameter_df in zip(parameter_list, parameter_default_values):
	
	values= st.sidebar.slider(label=parameter, key=parameter,value=float(parameter_df), min_value=0.0, max_value=100.0, step=1.0)
	parameter_input_values.append(values)
	
input_variables=pd.DataFrame([parameter_input_values],columns=parameter_list,dtype=float)
st.write('\n\n')

if st.button("Click Here to Classify"):
	prediction = gb_clf.predict(input_variables)
	st.image(setosa) if prediction == 0 else st.image(versicolor)
