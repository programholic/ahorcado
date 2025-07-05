import streamlit as st
import random

# Arte del ahorcado
hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

# Palabras posibles
words = (
    "oso", "tigre", "león", "gato", "perro", "ratón", "jirafa", "elefante", "mono", "caballo",
    "zorro", "conejo", "vaca", "cerdo", "oveja", "lobo", "ardilla", "murciélago", "mapache", "nutria",
    "pato", "cisne", "águila", "halcón", "búho", "pájaro", "pingüino", "gallina", "gallo", "pavo",
    "pavo-real", "serpiente", "lagarto", "cocodrilo", "tortuga", "rana", "sapo", "pez", "delfín", "ballena",
    "tiburón", "foca", "pulpo", "calamar", "estrella-de-mar", "caballito-de-mar", "camaleón", "iguana", "flamenco", "abeja",
    "avispa", "mosca", "mosquito", "mariposa", "libélula", "cigarra", "grillo", "caracol", "lombriz", "cangrejo",
    "langosta", "gamba", "camarón", "almeja", "ostra", "medusa", "erizo-de-mar", "anémona", "coral", "escarabajo",
    "hormiga", "termita", "cucaracha", "araña", "escarabajo", "mantis", "escarabajo-pelotero", "puma", "pantera", "lince",
    "chita", "camello", "dromedario", "ciervo", "alce", "reno", "búfalo", "antílope", "cabra", "oveja",
    "asno", "mula", "ganso", "pato", "gallina", "cuervo", "gorrión", "golondrina", "loro", "canario",
    "avestruz", "emu", "koala", "canguro", "wombat", "ornitorrinco", "ratón-marsupial", "zarigüeya", "oso-hormiguero", "perezoso"
)

# Inicialización
if "word" not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.guessed = []
    st.session_state.errors = 0
    st.session_state.win = False
    st.session_state.lost = False

# Función para mostrar arte
def show_hangman(errors):
    return "\n".join(hangman_art[errors])

# Encabezado
st.title("🕹️ Juego del Ahorcado - Animales")

# Mostrar arte del ahorcado
st.text(show_hangman(st.session_state.errors))

# Mostrar palabra con guiones
display_word = " ".join([letter if letter in st.session_state.guessed else "_" for letter in st.session_state.word])
st.markdown(f"### Palabra: {display_word}")

# Mostrar letras ya adivinadas
st.write(f"Letras adivinadas: {', '.join(st.session_state.guessed)}")

# Ingreso de letra
if not st.session_state.win and not st.session_state.lost:
    letra = st.text_input("Escribe una letra:", max_chars=1)

    if letra and letra.isalpha():
        letra = letra.lower()
        if letra in st.session_state.guessed:
            st.warning("¡Ya intentaste con esa letra!")
        elif letra in st.session_state.word:
            st.session_state.guessed.append(letra)
            if all(char in st.session_state.guessed for char in st.session_state.word):
                st.session_state.win = True
        else:
            st.session_state.guessed.append(letra)
            st.session_state.errors += 1
            if st.session_state.errors >= 6:
                st.session_state.lost = True

# Resultado
if st.session_state.win:
    st.success(f"¡Ganaste! La palabra era: {st.session_state.word}")
elif st.session_state.lost:
    st.error(f"¡Perdiste! La palabra era: {st.session_state.word}")

# Botón para reiniciar
if st.button("🔁 Jugar otra vez"):
    st.session_state.word = random.choice(words)
    st.session_state.guessed = []
    st.session_state.errors = 0
    st.session_state.win = False
    st.session_state.lost = False
