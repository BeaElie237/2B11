import streamlit as st
import time

# Configuration de la page
st.set_page_config(page_title="Git & GitHub Tutorial", page_icon=":computer:", layout="wide")

# CSS pour les animations
st.markdown("""
<style>
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.fadeIn {
    animation: fadeIn 2s;
}

@keyframes slideIn {
    from { transform: translateX(-100%); }
    to { transform: translateX(0); }
}

.slideIn {
    animation: slideIn 1.5s;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-30px); }
    60% { transform: translateY(-15px); }
}

.bounce {
    animation: bounce 2s infinite;
}
</style>
""", unsafe_allow_html=True)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choisissez une page", ["Accueil", "Git Basics", "GitHub Basics", "Formulaire"])

# Page d'accueil
if page == "Accueil":
    st.markdown('<h1 class="fadeIn">Bienvenue sur le Tutoriel Git & GitHub</h1>', unsafe_allow_html=True)
    st.markdown('<p class="slideIn">Ce site vous guide à travers les bases de Git et GitHub.</p>', unsafe_allow_html=True)
    st.image("https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png", width=100, caption="Git Logo")
    st.image("https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png", width=100, caption="GitHub Logo")

# Page Git Basics
elif page == "Git Basics":
    st.markdown('<h1 class="fadeIn">Git Basics</h1>', unsafe_allow_html=True)
    st.markdown('<p class="slideIn">Git est un système de contrôle de version distribué.</p>', unsafe_allow_html=True)
    st.markdown("""
    ### Commandes de base de Git:
    - `git init`: Initialise un nouveau dépôt Git.
    - `git clone <url>`: Clone un dépôt existant.
    - `git add <file>`: Ajoute des fichiers à l'index.
    - `git commit -m "message"`: Commit les changements avec un message.
    - `git push`: Pousse les commits vers le dépôt distant.
    - `git pull`: Met à jour le dépôt local avec les changements distants.
    """)

# Page GitHub Basics
elif page == "GitHub Basics":
    st.markdown('<h1 class="fadeIn">GitHub Basics</h1>', unsafe_allow_html=True)
    st.markdown('<p class="slideIn">GitHub est une plateforme d\'hébergement de code pour le contrôle de version et la collaboration.</p>', unsafe_allow_html=True)
    st.markdown("""
    ### Fonctionnalités de GitHub:
    - **Repositories**: Stockez votre code et son historique.
    - **Branches**: Travaillez sur différentes versions de votre projet.
    - **Pull Requests**: Proposez des changements et discutez-en.
    - **Issues**: Suivez les bugs et les tâches.
    - **Actions**: Automatisez vos workflows CI/CD.
    """)

# Page Formulaire
elif page == "Formulaire":
    st.markdown('<h1 class="fadeIn">Formulaire de Contact</h1>', unsafe_allow_html=True)
    st.markdown('<p class="slideIn">Remplissez ce formulaire pour nous contacter.</p>', unsafe_allow_html=True)
    
    with st.form("contact_form"):
        name = st.text_input("Nom")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Envoyer")
        
        if submitted:
            with st.spinner('Envoi en cours...'):
                time.sleep(2)  # Simulation d'un envoi
                st.success('Message envoyé avec succès!')
                st.balloons()  # Animation de ballons

# Footer
st.markdown("""
---
<div style="text-align: center; padding: 10px;">
    <p class="bounce">Merci d'avoir visité notre tutoriel Git & GitHub!</p>
</div>
""", unsafe_allow_html=True)