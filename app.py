import streamlit as st

# Configuración del título de la página web
st.title("🧮 Suma y Multiplica")
st.write("Suma dos números y multiplica el resultado por un tercero.")

# Crear el formulario en la interfaz gráfica
st.subheader("1. Introduce los números")

# Casillas para ingresar datos (inputs visuales)
num1 = st.number_input("Primer número para sumar:", value=0.0, step=1.0)
num2 = st.number_input("Segundo número para sumar:", value=0.0, step=1.0)
multiplicador = st.number_input("Número por el cual multiplicar:", value=1.0, step=1.0)

# Botón interactivo para realizar el cálculo
if st.button("Calcular Resultado"):
    # Lógica matemática
    resultado_suma = num1 + num2
    resultado_final = resultado_suma * multiplicador
    
    # Mostrar los resultados con recuadros visuales en el Frontend
    st.success(f"✅ ¡Cálculo completado exitosamente!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Resultado de la Suma", value=f"{resultado_suma}")
    with col2:
        st.metric(label="Resultado Final (Multiplicado)", value=f"{resultado_final}")
