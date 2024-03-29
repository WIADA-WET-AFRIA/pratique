import streamlit as st
#import pandas as pd
#import seaborn as sns

def main():
    st.title('Application WIADA 2023')
    
    # Entrée du nom de l'utilisateur
    user = st.text_input("Entrer votre nom")
    
    # Bouton pour saluer l'utilisateur
    if st.button("Dis bonjour"):
        if user:
            st.write(f'Bonjour {user} !')
        else:
            st.write('Bonjour à tous !')
    
    

if __name__ == "__main__":
    main()
