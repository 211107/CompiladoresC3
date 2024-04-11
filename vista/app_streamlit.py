import streamlit as st
import io
import sys
from ConversoModel import Converso
from analizadores.lexer import prueba
from analizadores.sintactico import parse_code
from analizadores.Semantico import Semantic

# Estilo CSS personalizado para el botón
custom_css = """
<style>
.button-custom {
    background-color: transparent;
    border: none;
    font-size: 24px;
    color: green;
}
</style>
"""

# Insertar el CSS personalizado en el HTML de Streamlit
st.markdown(custom_css, unsafe_allow_html=True)

def main():
    st.title("CodeSphere")

    # Solicitar al usuario ingresar el código
    data = st.text_area("Ingrese el código:")

    # Botón para iniciar el análisis
    if st.button("Ejecutar \u27A4", key="analizar", help="button-custom"): 
        # Realizar análisis léxico
        resultado_lexico = prueba(data)
        tokens = prueba(data)
        # Realizar análisis sintáctico
        resultado_sintactico = parse_code(data)

        # Obtener el árbol de sintaxis
        syntax_tree = parse_code(data)
    
        # Crear e iniciar el analizador semántico
        semantic = Semantic(data)
        result_semantico = semantic.apply()
        
        # Mostrar resultados en la interfaz
        st.header("Resultado del análisis léxico:")
        st.table(resultado_lexico)

        st.header("Resultado del análisis sintáctico:")
        vr = False
        if resultado_sintactico:
            st.success("El código es válido.")
            # Mostrar el árbol de sintaxis
            st.write(syntax_tree)
        else:
            st.error("El código es inválido.")
            vr = True


        st.header("Errores semánticos:")
        if (result_semantico is not None or vr ):
            if(vr):
                error_message = "Error de sintaxis"
            else:
                error_message = result_semantico
            st.error(error_message)
        else:
            st.success("No se encontraron errores semánticos.")

        # Realizar la conversión y ejecución del código
        conversor = Converso(data)
        codigo_converso = conversor.initConverso()
        print(codigo_converso)
        # Creamos un objeto para capturar la salida impresa
        captured_output = io.StringIO()

        # Redirigimos la salida estándar hacia nuestro objeto
        sys.stdout = captured_output
        
        # Ejecutamos el código
        if("main" in codigo_converso):
            codigo_converso =  codigo_converso +"\n" + "main()"        
        if(vr==False):
            exec(codigo_converso)

            # Recuperamos la salida impresa y la guardamos en una variable
            output_variable = captured_output.getvalue()

            # Restauramos la salida estándar
            sys.stdout = sys.__stdout__
        else:
            output_variable= "Se encuentran errores"

        # Mostramos la salida en la interfaz de Streamlit
        with st.expander("Consola \u25BE"):
            st.write(output_variable)

if __name__ == "__main__":
    main()
