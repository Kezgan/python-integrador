# Programación Concurrente - Trabajo Práctico Integrador

## Ejercicio

En un bar frente a una playa en una isla paradisíaca hay un barman que se encarga de armar tragos para los clientes que se están tomando unas vacaciones.


El barman va a su estante de bebidas, prepara la cantidad de tragos que se desea y los deja en la barra, listos para que venga un mesero y los lleve a la mesa indicada. El barman y los meseros van constantemente a la barra sin ningún tipo de orden a dejar o agarrar, respectivamente, tragos. Si un mesero va a la barra a buscar X cantidad de tragos y no están preparados se queda esperando, quizás junto con otros meseros, a que el barman los prepare y los deje listos.

## Beneficio/necesidad de la concurrencia

En este caso es necesaria la concurrencia para que los meseros puedan entregar los pedidos de manera rápida y eficaz, y al tener recursos compartidos debemos sincronizarlos para que "funcionen" de forma normal.