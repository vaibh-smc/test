import streamlit as st
import pickle


model=pickle.load(open('model.pkl','rb'))
# side=st.sidebar
st.title("First Web App")
a=st.container()

with a:
    n1=st.number_input("Enter sepal_length ",)
    n2=st.number_input("Enter sepal_width ")
    n3=st.number_input("Enter petal length ")
    n4=st.number_input("Enter petal width ")

def predict(n1,n2,n3,n4):
    temp=[n1,n2,n3,n4]
    result= model.predict([temp])[0]
    return result
def fun(r):
    if r==0:
        return "setosa"
    elif r==1:
        return "Versicolor"
    else:
        return "Virginica"
if st.button("Predict"):
    r=predict(n1,n2,n3,n4)
    n=fun(r=r)
    st.success(f"The Flower is belongs to  {n} Faimly!!!")


    
    









