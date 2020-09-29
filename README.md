# Experimento Doble Rendija 💡

El experimento de la doble rendija fue realizado por primera vez en 1801 por Tomas Young, este comprobó un patrón de interferencias en la luz procedente de una
fuente lejana al difractarse en el paso por dos rejillas. El experimento también puede realizarse con electrones, protones o neutrones, produciendo patrones de
interferencia similares a los obtenidos cuando se realiza con luz.

Las partculas tienen un comportamiento similar a este:

![alt text](https://github.com/gabriela-castro-s/img/blob/master/doubleslitexplain.png?raw=true)

Para entender el resultado del experimento en la época aplicaron el principio de superposición cuántico en el que se afirma que las partículas (en este caso la luz) 
puede tomar dos o más valores de una determinada magnitud tambien conocida como "onda de posibilidades" que pasan por las dos ranuras para luego interferir con ella 
misma hasta que golpear la pared de impacto y que al ser monitoreado este se ve afectado a que se dice que este principio colapsa y solo lograremos observar una de
todos los posibles resultados.

En esta ocasión haremos una receración casera del experimento y posteriormente explicaremos cómo este nos ayuda a entender la teoría del multiverso.

## Materiales 🧰

Para realizar nuestro montaje experimental necesitaremos:

- Un laser
- Papel blanco
- Marcador negro
- Bisturí
- Plastilina

## Para recrearlo ⚙️

1. Con la hoja de papel y el marcador dibujamos un cuadrado en el centro de nuestra hoja y la coloreamos con el marcador. Con el bisturí realizamos el corte de las
rendijas, recuerda que entre más cerca queden los cortes es mejor.

![alt text](https://github.com/gabriela-castro-s/img/blob/master/doubleslit3.jpeg?raw=true)

2. Con nuestra plastilina hacemos un soporte para el laser como se observa a continuación.

![alt text](https://github.com/gabriela-castro-s/img/blob/master/doubleslit4.jpeg?raw=true)

3. Para realizar el montaje experimental de la manera más ecoamigable posible utilicé una lata que encontré en mi casa que tenía la forma perfecta para acomodar el
laser y las rendijas de la mejor manera, la apoyé en una mesa y reflejé el laser en el techo.

![alt text](https://github.com/gabriela-castro-s/img/blob/master/doubleslit1.jpeg?raw=true)

4. Con el laser encendido ubicamos la hoja para que cace con las rendijas y se refleje en el techo, debería verse así. Recuerda que para obtener mejores resultados
debes realizar el procedimiento en una habitación oscura.

![alt text](https://github.com/gabriela-castro-s/img/blob/master/doubleslit2.jpeg?raw=true)

Si desea ver el montaje experimental en video pudes hacer clic [aquí](https://www.youtube.com/watch?v=vUDKAd3yf9U).

## ¿Cómo nos ayuda a entender el multiverso? 🔬

Cada fotón es tangible en un universo e intangible en todos sus universos paralelos, este experimento nos permite entender la teoría del mulltiverso pues podemos
evidenciar partículas intangibles particionandoce entre si mismas así como las partículas tangibles lo que quiere decir que las partículas intangibles forman un
gran número de universos paralelos todos similares en composición al tangible y todos obedecen las mismas leyes físicas pero difieren en la posición de cada
partícula.

## Simulación cuántica 💻

Para realizar la simulación cuántica del sistema, este tendra una matriz de adyacencia asociada y un vector el cual representara el estado inicial del sistema,
donde sus posiciones representaran el peso de una conexion especifica entre componentes del sistema.

La matriz de adyacencía se representa así:

![alt text](https://github.com/gabriela-castro-s/img/blob/master/matrizadyacencia.jpeg?raw=true)

En la librería corresponde a:

```
matriz = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[0, 0], [-1 / math.sqrt(6), 1 / math.sqrt(6)], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
         [[0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [-1 / math.sqrt(6), 1 / math.sqrt(6)], [0, 0], [0, 0],[1, 0], [0, 0], [0,0]],
         [[0, 0], [0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
          [[0, 0], [0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
```

### Para utilizar la librería 📋

Es necesario que cuente con una calculadora para vectores, matrices y números imaginarios. En este repositorio se incluye un archivo de la libreria utilizada para
generar las simulaciones.

La libreria fue escrita en PyCharm, por lo que cualquier editor de phyton3 puede abrir la librería.

Si desea clonarlo puede realizar los siguientes pasos:

Para clonar el repositorio:

- Nos ubicamos en esta sección del repositorio y presionamos Code

![alt text](https://github.com/gabriela-castro-s/img/blob/master/cnyt1.png?raw=true)

- En la sección clonar, hacemos clic en el portapapeles para copiar el link del repositorio.

![alt text](https://github.com/gabriela-castro-s/img/blob/master/cnyt2.png?raw=true)

- Abrimos nuestro terminal y ubicamos la carpeta en la que queremos clonar el repositorio. 
Escribimos git clone y seguido ponemos el link que copiamos previamente. 

![alt text](https://github.com/gabriela-castro-s/img/blob/master/cnyt3.png?raw=true)

- El repositorio ha sido clonado.

![alt text](https://github.com/gabriela-castro-s/img/blob/master/cnyt4.png?raw=true)

### Ejecutando pruebas 🤓

En los archivos del repositorio se incluye [DoubleslitTest](https://github.com/gabriela-castro-s/Experimento-Doble-rendija/blob/master/DoubleslitTest.py), 
este contiene las pruebas para comprobar las probablidades de la matriz de adyacencia en su estado inicial.

Para ejecutarlas, después de clonar el repositorio, en su terminal:

- Abra la carpeta en la que se encuentra el repositorio
```
cd Experimento Doble Rendija

```
- Ejecute las pruebas con el comando

```
 python DoubleslitTest.py
```
## Construido con 🛠️

PyCharm 2020.2 (Community Edition)

## Autores ✒️

* **Gabriela Castro Santamaría** [gabriela-castro-s](https://github.com/gabriela-castro-s) 

## Bibliografía 📖

- Deutsh, David (1997). The Fabric of reality: The Science of Parallel Universes and its Implicatios. PENGUIN BOOKS, Chapter 2.
