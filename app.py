import streamlit as st
import random

# Título del test
st.title("Test de Geografía e Historia")

# Crear una lista de 100 preguntas
preguntas = [
    # 1-20
    {"pregunta": "¿Cuál es el río más largo del mundo?", "opciones": ["Nilo", "Amazonas", "Yangtsé", "Misisipi"], "respuesta_correcta": "Amazonas"},
    {"pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?", "opciones": ["1939", "1941", "1914", "1936"], "respuesta_correcta": "1939"},
    {"pregunta": "¿Cuál es el país más grande del mundo?", "opciones": ["China", "Canadá", "Rusia", "Estados Unidos"], "respuesta_correcta": "Rusia"},
    {"pregunta": "¿Cuál fue la civilización que construyó las pirámides de Giza?", "opciones": ["Romanos", "Griegos", "Egipcios", "Incas"], "respuesta_correcta": "Egipcios"},
    {"pregunta": "¿En qué continente se encuentra la Cordillera de los Andes?", "opciones": ["Asia", "África", "América del Sur", "Europa"], "respuesta_correcta": "América del Sur"},
    {"pregunta": "¿Cuál es la capital de Australia?", "opciones": ["Sídney", "Melbourne", "Canberra", "Perth"], "respuesta_correcta": "Canberra"},
    {"pregunta": "¿Cuál fue el primer presidente de los Estados Unidos?", "opciones": ["Abraham Lincoln", "George Washington", "John Adams", "Thomas Jefferson"], "respuesta_correcta": "George Washington"},
    {"pregunta": "¿Qué país fue el escenario principal de la Guerra de las Galias?", "opciones": ["Francia", "Alemania", "Reino Unido", "Italia"], "respuesta_correcta": "Francia"},
    {"pregunta": "¿En qué año llegó Cristóbal Colón a América?", "opciones": ["1492", "1491", "1493", "1500"], "respuesta_correcta": "1492"},
    {"pregunta": "¿Cuál es el desierto más grande del mundo?", "opciones": ["Sáhara", "Gobi", "Kalahari", "Atacama"], "respuesta_correcta": "Sáhara"},
    {"pregunta": "¿En qué año cayó el Muro de Berlín?", "opciones": ["1989", "1991", "1987", "1990"], "respuesta_correcta": "1989"},
    {"pregunta": "¿Qué país tiene el mayor número de islas en el mundo?", "opciones": ["Indonesia", "Suecia", "Filipinas", "Grecia"], "respuesta_correcta": "Suecia"},
    {"pregunta": "¿Qué país tiene la mayor población del mundo?", "opciones": ["India", "Estados Unidos", "China", "Brasil"], "respuesta_correcta": "China"},
    {"pregunta": "¿Cuál es la capital de Canadá?", "opciones": ["Ottawa", "Toronto", "Montreal", "Vancouver"], "respuesta_correcta": "Ottawa"},
    {"pregunta": "¿En qué año comenzó la Primera Guerra Mundial?", "opciones": ["1914", "1918", "1920", "1939"], "respuesta_correcta": "1914"},
    {"pregunta": "¿Cuál es la montaña más alta del mundo?", "opciones": ["K2", "Monte Everest", "Mont Blanc", "Kilimanjaro"], "respuesta_correcta": "Monte Everest"},
    {"pregunta": "¿Cuál fue la capital del Imperio Romano?", "opciones": ["Atenas", "Cartago", "Roma", "Constantinopla"], "respuesta_correcta": "Roma"},
    {"pregunta": "¿Cuál es el océano más grande del mundo?", "opciones": ["Océano Atlántico", "Océano Pacífico", "Océano Índico", "Océano Ártico"], "respuesta_correcta": "Océano Pacífico"},
    {"pregunta": "¿Qué ciudad fue destruida por la erupción del Monte Vesubio en el año 79 d.C.?", "opciones": ["Herculano", "Roma", "Nápoles", "Pompeya"], "respuesta_correcta": "Pompeya"},
    {"pregunta": "¿Qué isla nación es famosa por sus Moáis?", "opciones": ["Isla de Pascua", "Maldivas", "Hawái", "Seychelles"], "respuesta_correcta": "Isla de Pascua"},

    # 21-40
    {"pregunta": "¿En qué país se encuentra la Torre Eiffel?", "opciones": ["España", "Francia", "Italia", "Reino Unido"], "respuesta_correcta": "Francia"},
    {"pregunta": "¿Qué río cruza París?", "opciones": ["Tíber", "Danubio", "Sena", "Tajo"], "respuesta_correcta": "Sena"},
    {"pregunta": "¿En qué ciudad se encuentra el Coliseo?", "opciones": ["Roma", "Atenas", "París", "Estambul"], "respuesta_correcta": "Roma"},
    {"pregunta": "¿Cuál es el idioma más hablado en el mundo?", "opciones": ["Inglés", "Mandarín", "Español", "Hindi"], "respuesta_correcta": "Mandarín"},
    {"pregunta": "¿Qué país inventó el papel?", "opciones": ["India", "Grecia", "China", "Egipto"], "respuesta_correcta": "China"},
    {"pregunta": "¿En qué año se descubrió América?", "opciones": ["1492", "1489", "1500", "1495"], "respuesta_correcta": "1492"},
    {"pregunta": "¿Qué país es famoso por sus canales y tulipanes?", "opciones": ["Países Bajos", "Bélgica", "Dinamarca", "Suecia"], "respuesta_correcta": "Países Bajos"},
    {"pregunta": "¿Cuál es el río más largo de Europa?", "opciones": ["Rin", "Volga", "Danubio", "Loira"], "respuesta_correcta": "Volga"},
    {"pregunta": "¿En qué país se encuentra el Taj Mahal?", "opciones": ["India", "Pakistán", "Bangladés", "Nepal"], "respuesta_correcta": "India"},
    {"pregunta": "¿En qué país está la Gran Muralla?", "opciones": ["Japón", "China", "Mongolia", "Corea del Norte"], "respuesta_correcta": "China"},
    {"pregunta": "¿Quién fue el primer hombre en pisar la Luna?", "opciones": ["Buzz Aldrin", "Neil Armstrong", "Michael Collins", "Yuri Gagarin"], "respuesta_correcta": "Neil Armstrong"},
    {"pregunta": "¿Cuál es la capital de Japón?", "opciones": ["Pekín", "Tokio", "Seúl", "Osaka"], "respuesta_correcta": "Tokio"},
    {"pregunta": "¿En qué continente se encuentra Egipto?", "opciones": ["Asia", "África", "Europa", "América"], "respuesta_correcta": "África"},
    {"pregunta": "¿Qué país colonizó la mayor parte de América del Sur?", "opciones": ["Portugal", "Francia", "España", "Reino Unido"], "respuesta_correcta": "España"},
    {"pregunta": "¿Qué país es famoso por sus pirámides?", "opciones": ["México", "Perú", "Egipto", "Grecia"], "respuesta_correcta": "Egipto"},
    {"pregunta": "¿Cuál es el país más pequeño del mundo?", "opciones": ["Mónaco", "Malta", "Vaticano", "Liechtenstein"], "respuesta_correcta": "Vaticano"},
    {"pregunta": "¿En qué continente está ubicada Australia?", "opciones": ["Asia", "Oceanía", "América", "Europa"], "respuesta_correcta": "Oceanía"},
    {"pregunta": "¿Cuál es la capital de España?", "opciones": ["Barcelona", "Madrid", "Sevilla", "Valencia"], "respuesta_correcta": "Madrid"},
    {"pregunta": "¿En qué año se fundó la Organización de las Naciones Unidas (ONU)?", "opciones": ["1945", "1950", "1939", "1961"], "respuesta_correcta": "1945"},

    # 41-60
    {"pregunta": "¿Qué océano está al este de África?", "opciones": ["Pacífico", "Índico", "Atlántico", "Ártico"], "respuesta_correcta": "Índico"},
    {"pregunta": "¿Cuál es el país más poblado de África?", "opciones": ["Egipto", "Sudáfrica", "Nigeria", "Etiopía"], "respuesta_correcta": "Nigeria"},
    {"pregunta": "¿Qué país tiene la península ibérica junto a Portugal?", "opciones": ["Francia", "España", "Italia", "Alemania"], "respuesta_correcta": "España"},
    {"pregunta": "¿Cuál es el estado más grande de los Estados Unidos?", "opciones": ["California", "Alaska", "Texas", "Montana"], "respuesta_correcta": "Alaska"},
    {"pregunta": "¿En qué país se encuentra el Everest?", "opciones": ["India", "Nepal", "China", "Bután"], "respuesta_correcta": "Nepal"},
    {"pregunta": "¿Cuál es la capital de Brasil?", "opciones": ["São Paulo", "Río de Janeiro", "Brasilia", "Salvador"], "respuesta_correcta": "Brasilia"},
    {"pregunta": "¿En qué año llegó el hombre a la luna?", "opciones": ["1965", "1969", "1972", "1962"], "respuesta_correcta": "1969"},
    {"pregunta": "¿Qué país está al sur de los Estados Unidos?", "opciones": ["Canadá", "México", "Cuba", "Belice"], "respuesta_correcta": "México"},
    {"pregunta": "¿Cuál es el continente más frío?", "opciones": ["Europa", "América", "Asia", "Antártida"], "respuesta_correcta": "Antártida"},
    {"pregunta": "¿Cuál es la capital de Alemania?", "opciones": ["Munich", "Hamburgo", "Berlín", "Colonia"], "respuesta_correcta": "Berlín"},

    # 61-80
    {"pregunta": "¿Qué país tiene la mayor selva tropical?", "opciones": ["Brasil", "India", "Australia", "Sudáfrica"], "respuesta_correcta": "Brasil"},
    {"pregunta": "¿Cuál es el país con la economía más grande de Europa?", "opciones": ["Reino Unido", "Francia", "Alemania", "Italia"], "respuesta_correcta": "Alemania"},
    {"pregunta": "¿En qué año fue el descubrimiento de la tumba de Tutankamón?", "opciones": ["1922", "1918", "1930", "1912"], "respuesta_correcta": "1922"},
    {"pregunta": "¿Qué país tiene la bandera con una hoja de arce?", "opciones": ["Canadá", "Francia", "Australia", "Suecia"], "respuesta_correcta": "Canadá"},
    {"pregunta": "¿Cuál es la capital de Turquía?", "opciones": ["Estambul", "Ankara", "Izmir", "Bursa"], "respuesta_correcta": "Ankara"},
    {"pregunta": "¿Qué país es conocido como el país del sol naciente?", "opciones": ["China", "Japón", "Corea del Sur", "Vietnam"], "respuesta_correcta": "Japón"},
    {"pregunta": "¿Cuál es el país más grande de África?", "opciones": ["Nigeria", "Argelia", "Sudáfrica", "Egipto"], "respuesta_correcta": "Argelia"},
    {"pregunta": "¿Qué continente no tiene desiertos?", "opciones": ["Asia", "Europa", "África", "Antártida"], "respuesta_correcta": "Europa"},
    {"pregunta": "¿En qué país se encuentra el Kremlin?", "opciones": ["Rusia", "China", "Mongolia", "Kazajistán"], "respuesta_correcta": "Rusia"},
    {"pregunta": "¿Cuál es el río más largo de América del Norte?", "opciones": ["Misisipi", "Amazonas", "Missouri", "Bravo"], "respuesta_correcta": "Misisipi"},

    # 81-100
    {"pregunta": "¿En qué país se encuentra el Machu Picchu?", "opciones": ["Colombia", "Perú", "Ecuador", "Bolivia"], "respuesta_correcta": "Perú"},
    {"pregunta": "¿Cuál es el nombre de la famosa ópera de Sídney?", "opciones": ["Ópera de Melbourne", "Ópera de Queensland", "Ópera de Sídney", "Ópera de Perth"], "respuesta_correcta": "Ópera de Sídney"},
    {"pregunta": "¿Cuál es el mar más salado del mundo?", "opciones": ["Mar Muerto", "Mar Rojo", "Mar Mediterráneo", "Mar Caribe"], "respuesta_correcta": "Mar Muerto"},
    {"pregunta": "¿Qué país fue conocido anteriormente como Birmania?", "opciones": ["Laos", "Vietnam", "Myanmar", "Camboya"], "respuesta_correcta": "Myanmar"},
    {"pregunta": "¿Cuál es el único país del mundo que tiene una bandera cuadrada?", "opciones": ["Mónaco", "Suiza", "Nepal", "Vaticano"], "respuesta_correcta": "Vaticano"},
    {"pregunta": "¿Cuál es la isla más grande del mundo?", "opciones": ["Groenlandia", "Australia", "Nueva Guinea", "Borneo"], "respuesta_correcta": "Groenlandia"},
    {"pregunta": "¿En qué país se encuentra el Kilimanjaro?", "opciones": ["Tanzania", "Kenia", "Uganda", "Rwanda"], "respuesta_correcta": "Tanzania"},
    {"pregunta": "¿Qué país tiene la mayor población musulmana?", "opciones": ["Arabia Saudita", "India", "Indonesia", "Pakistán"], "respuesta_correcta": "Indonesia"},
    {"pregunta": "¿Cuál es la ciudad más poblada del mundo?", "opciones": ["Tokio", "Delhi", "Shanghái", "Nueva York"], "respuesta_correcta": "Tokio"},
    {"pregunta": "¿Cuál es el país más joven del mundo?", "opciones": ["Kosovo", "Sudán del Sur", "Timor Oriental", "Montenegro"], "respuesta_correcta": "Sudán del Sur"}
]

# 📘 **Nuevo: Seleccionar preguntas aleatorias y almacenarlas en `st.session_state`**
if 'preguntas_seleccionadas' not in st.session_state:  # 📘
    st.session_state['preguntas_seleccionadas'] = random.sample(preguntas, 5)  # 📘

# 📘 **Nuevo: Recuperar las preguntas seleccionadas de `session_state`**
preguntas_seleccionadas = st.session_state['preguntas_seleccionadas']  # 📘

# Contador de respuestas correctas
puntuacion = 0

# Diccionario para almacenar respuestas seleccionadas
respuestas_usuario = {}

# Mostrar preguntas
for i, pregunta in enumerate(preguntas_seleccionadas):
    st.subheader(f"Pregunta {i + 1}: {pregunta['pregunta']}")
    opciones = pregunta["opciones"]
    seleccion = st.radio(f"Selecciona una respuesta:", opciones, key=f"pregunta_{i}")
    respuestas_usuario[pregunta["pregunta"]] = seleccion

# Botón para enviar el test
if st.button("Enviar respuestas"):
    # Comprobar las respuestas y mostrar resultados
    for pregunta in preguntas_seleccionadas:
        if respuestas_usuario[pregunta["pregunta"]] == pregunta["respuesta_correcta"]:
            puntuacion += 1
            st.success(f"Correcto: {pregunta['pregunta']}")
        else:
            st.error(f"Incorrecto: {pregunta['pregunta']}. La respuesta correcta es {pregunta['respuesta_correcta']}")

    # Mostrar la puntuación final
    st.subheader(f"Tu puntuación: {puntuacion} / {len(preguntas_seleccionadas)}")
    if puntuacion == len(preguntas_seleccionadas):
        st.balloons()  # Si es perfecto, lanza globos 🎈
