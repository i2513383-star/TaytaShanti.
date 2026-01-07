'''import streamlit as st
from capaPresentacion.pPersona import PPersona
from capaPresentacion.pProducto import PProducto

def main():
    PPersona()

if __name__ == "__main__":
    main()

def main():
    PProducto()

if __name__ == "__main__":
    main()
''' 
    
import streamlit as st

from capaPresentacion.pPersona import PPersona
from capaPresentacion.pProducto import PProducto

def main():
    st.title("Sistema TAYTA SHANTY")

    opcion = st.sidebar.selectbox(
        "Seleccione una opción",
        ["Personas", "Productos"]
    )

    if opcion == "Personas":
        PPersona()
    elif opcion == "Productos":
        PProducto()

if __name__ == "__main__":
    main()
