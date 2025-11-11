import streamlit as st
from ExpertMaladie import MaladieExpert, Symptome
from PIL import Image
import time

# -------------------- APPLICATION PRINCIPALE --------------------

st.title("**DIAGNOSTIC DES MALADIES CARDIO-VASCULAIRES**")
st.markdown("__________")
st.markdown("*Veuillez séléctionner les symptômes :*")

st.sidebar.title("**SYSTEME EXPERT MEDICAL**")
st.sidebar.write("*Cochez les symptômes du patient et cliquez sur le bouton pour diagnostiquer, prévenez les complications des maladies cardiovasculaires*")
#st.sidebar.image('C:\\Users\\windows 10\\Desktop\\AbelM\\Image.png',use_container_width=True)
st.sidebar.success("🟢**ESSAI** : Cochez les 10 premières cases pour diagnostiquer la **Cardipathie rhumatismale**")
st.sidebar.write("Conçu et réalisé par:")
st.sidebar.info("**Abel M.**")

with st.form('form1'):
    col1, col2 = st.columns(2)
    with col1:
            essouflement = st.checkbox("**Le patient a des essouflements**")
            fatigue = st.checkbox("**Le patient resent de la fatigue**")
            Arythmie = st.checkbox("**Le patient a une arythmie cardiaque**")
            douleurThorax = st.checkbox("**Le patient a une douleur thoracique**")
            evanouissement = st.checkbox("**Le patient a des evanouissements**")
            fievre = st.checkbox("**Le patient a une fièvre (Cas des rhumatismes aigus)**")
            gonflementArt = st.checkbox("**Le patient a des gonflements au niveau des articulations (Cas des rhumatismes aigus)**")
            nausee = st.checkbox("**Le patient a des nausées (Cas des rhumatismes aigus)**")
            crampe = st.checkbox("**Le patient a des crampes (Cas des rhumatismes aigus)**")
            vomissement = st.checkbox("**Le patient a des vomissements (Cas des rhumatismes aigus)**")
            vertige = st.checkbox("**Le patient a des vertiges**")
    with col2:
            sueur = st.checkbox("**Le patient a des transpirations**")
            angoisse = st.checkbox("**Le patient a des faiblesses et des angoisses**")
            douleurArt = st.checkbox("**Le patient ressent des douleurs articulaires**")
            raideurMat = st.checkbox("**Le patient a des raideurs matinales**")
            gonflementJambe = st.checkbox("**Le patient a des gonflements des jambes**")
            perteMob = st.checkbox("**Le patient a une perte de mobilité**")
            craquement = st.checkbox("**Le patient ressent des craquements**")
            souffle = st.checkbox("**Le patient a une perte de souffle cardiaque**")
            oedeme = st.checkbox("**Le patient a des oedèmes**")
            rythmeCard = st.checkbox("**Le patient a des rythmes cardiaques anormales**")
            peauPale = st.checkbox("**Le patient a une peau pâle et froide**")

    # méthode de l'outil de la barre de progression
    progress_container = st.empty()
    text_container = st.empty()
    # Bouton
    btn_soumettre = st.form_submit_button("**DIAGNOSTIC**")
    if btn_soumettre:
            my_bar = progress_container.progress(0) 
            #text_container.text("Veuillez patienter...")

              # 2. Simuler une opération longue pour la progression
            for percent_complete in range(100):
                   
                time.sleep(0.03) # la barre fait unepetite pose puis reprend le défilement 
                my_bar.progress(percent_complete + 1) # Mettre à jour la barre seule
                text_container.text(f"Analyse des symptômes en cours, Veuillez patienter...{percent_complete + 1}%")

              # Faire disparaître la barre de progression dès qu'elle atteint 100%
            my_bar.empty() # cette ligne fait disparaître la barre de progression dès qu'elle atteint 100% 
            text_container.empty()
              # 
            sante = MaladieExpert()
            sante.reset()
            sante.declare(Symptome(
                essouflement=essouflement,
                fatigue=fatigue,
                Arythmie=Arythmie,
                douleurThorax=douleurThorax,
                evanouissement=evanouissement,
                fievre=fievre,
                gonflementArt=gonflementArt,
                nausee=nausee,
                crampe=crampe,
                vomissement=vomissement,
                vertige=vertige,
                sueur=sueur,
                angoisse=angoisse,
                douleurArt=douleurArt,
                raideurMat=raideurMat,
                gonflementJambe=gonflementJambe,
                perteMob=perteMob,
                craquement=craquement,
                souffle=souffle,
                oedeme=oedeme,
                rythmeCard=rythmeCard,
                peauPale=peauPale
            ))
            sante.run()
            st.info(sante.resultat)
  
st.markdown(
         """
        <style>
        .stApp {
            background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-PbpvN8brQxhV2Cip9bIVwwthpbW4GfuC1Q&s");
            background-size: cover;
            background-repeat: no-repeat;
            background position:center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )   


