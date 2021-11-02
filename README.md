# **Preposición del problema**

Eres parte del equipo de desarrollo de una aplicación de navegación para viajeros frecuentes (similar a Google Maps). La aplicación cuenta con un mapa que ayuda a los usuarios con instrucciones para  orientarlos cómo llegar del punto A al punto B. 

## **Se te solicita implementar una nueva funcionalidad que le permita al usuario ingresar:**
  1. El punto de partida 
  2. Destino
  3. El medio de transporte (Caminando, Carro o Trasporte Público) Obteniendo como resultado el tiempo que le tomará usando la ruta más rápida.

## **Ejemplo del resultado esperado:**
  Ingrese el punto de partida:
  Colonia Nápoles
  Ingrese el destino:
  El Ángel de la Independencia
  Ingrese el medio de trasporte:
  Caminando
  La ruta más rápida caminando desde Colonia Nápoles a El Ángel de la Independencia, le tomará 55
  minutos.

## **Consideraciones adicionales:**
  - La aplicación está evolucionando constantemente y el equipo de producto ya anticipó que se deberán agregar nuevas formas de trasporte en un futuro cercano (por ejemplo, bicicleta y taxi). 
  - Sin importar el origen y el destino ingresado por el usuario, los tiempos mostrados siempre deberán ser:
    o Cuando es Caminando: 55 minutos
    o Cuando es por Transporte Público: 35 minutos
    o Cuando es por Carro: 20 minutos
  - La solución debe ser escrita en Python.
  - Utilice programación orientada a objetos y patrones de diseño para la solución.
  - La interfaz de usuario no es relevante, la solución puede ser una aplicación de 
  consola/comandos.
  - Agregue todos los comentarios en el código que considere pertinentes para explicar la solución dada.

# Solución al problema

Dados los requerimientos se eligió un **patrón de diseño creacional**, ya que los patrones de creación proporcionan diversos mecanismos de creación de objetos, que aumentan la flexibilidad y la reutilización del código existente de una manera adecuada a la situación.

Dentro de esta categoría se seleccionó a **Builder Patterns** como arquitectura ya que permite producir diferentes tipos y representaciones de un objeto utilizando el mismo código de construcción. Se utiliza para la creación etapa por etapa de un objeto complejo combinando objetos simples.

