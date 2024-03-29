import streamlit as st
import pandas as pd
import seaborn as sns

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
    
    # Importer des données fictives pour l'exemple
    data = pd.DataFrame({
        'Pays': ['France', 'Allemagne', 'Espagne', 'Italie', 'Royaume-Uni'],
        'Population (millions)': [67, 83, 47, 60, 68]
    })
    
    # Afficher les données
    st.subheader('Données démographiques')
    st.write(data)
    
    # Afficher un graphique interactif avec seaborn
    st.subheader('Graphique de la population par pays')
    sns.barplot(x='Pays', y='Population (millions)', data=data)
    st.pyplot()
    
    # Bouton pour télécharger les données
    if st.button("Télécharger les données au format CSV"):
        csv = data.to_csv(index=False)
        st.download_button(
            label="Télécharger",
            data=csv,
            file_name='donnees_demographiques.csv',
            mime='text/csv'
        )

if __name__ == "__main__":
    main()
