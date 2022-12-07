import streamlit as st
#  streamlit run streamlit/main7.py

st.write("Aula")

st.markdown("# Davi")
# st.markdown("## Davi")
# st.markdown("### Davi")
# st.markdown("#### Davi")

st.title('Meu Title')
st.header("Meu Header")
st.subheader('Meu Subheader')

st.caption('Meu caption')

st.code("print('oi')", language='python')

st.latex('\int_a^b f(x) dx')


# '''
# # Passos Git

# - Iniciar repositório no Github;
# - Iniciar repositório local (dentro da pasta do projeto)
# ```
# git init
# ```
# - Adicionar arquivos para monitoramento do git
# ```
# git add .
# ```
# - Confirmar status
# ```
# git status 
# ```
# - Efetuar _commit_
# ```
# git commit -am <insira sua mensagem>
# ```
# - Adicionar git remote
# ```
# git remote add origin <url do repositório>
# ```
# - Enviar versão para o Github
# ```
# git push -u origin main
# ```
# '''