<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DE LABORATORIO</span><br />
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Python</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA INICIO::</td><td>16-May-2022</td><td>FECHA FIN:</td><td>20-May-2022</td><td>DURACIÓN:</td><td>04 horas</td>
</tr>
<tr>
<td>INTEGRANTES::</td><td>
<ul>
<li>Suasaca Pacompia Alvaro Gustavo</li>

</ul>
<td>NOTA</td><td></td><td></td><td></td>
</td>
</tr>
<tr><td colspan="6">RECURSOS:
    <ul>
        <li>https://www.w3schools.com/python/python_reference.asp</li>
        <li>https://docs.python.org/3/tutorial/</li>
    </ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTES:
<ul>
<li>Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</li>
</ul>
</td>
</<tr>
</tdbody>
</table>



## EJERCICIOS PROPUESTOS

-   La clase [Picture](Tarea-del-Ajedrez/picture.py) contará además con varios métodos que usted deberá implementar:
    1.  verticalMirror: Devuelve el espejo vertical de la imagen
        
        - ![Ejercicio 1](Imagenes/imagen1.png)
        
        - ![Ejercicio 1](Imagenes/imagen1_1.png)
        
    2.  horizontalMirror: Devuelve el espejo horizontal de la imagen
        
        - ![Ejercicio 2](Imagenes/imagen2.png)
        
        - ![Ejercicio 2](Imagenes/imagen2_1.png)
        
    3.  negative: Devuelve un negativo de la imagen
        
        - ![Ejercicio 3](Imagenes/imagen8.png)
        
        - ![Ejercicio 3](Imagenes/imagen8_1.png)
        
    4.  join: Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual
        
        - ![Ejercicio 4](Imagenes/imagen3.png)
        
        - ![Ejercicio 4](Imagenes/imagen3_1.png)
        
    5.  up: Devuelve una nueva figura poniendo la figura recibida como argumento, encima de la figura actual
        
        - ![Ejercicio 5](Imagenes/imagen4.png)
        
        - ![Ejercicio 5](Imagenes/imagen4_1.png)
        
    6.  under: Devuelve una nueva figura poniendo la figura recibida como argumento, sobre la figura actual
        
        - ![Ejercicio 6](Imagenes/imagen7.png)
        
        - ![Ejercicio 6](Imagenes/imagen7_1.png)
        
    7.  horizontalRepeat, Devuelve una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de n
        
        - ![Ejercicio 7](Imagenes/imagen5.png)
        
        - ![Ejercicio 7](Imagenes/imagen5_1.png)
        
    8.  verticalRepeat Devuelve una nueva figura repitiendo la figura actual debajo, la cantidad de veces que indique el valor de n
        
        - ![Ejercicio 8](Imagenes/imagen6.png)
        
        - ![Ejercicio 8](Imagenes/imagen6_1.png)

-   Tenga en cuenta que para implementar todos estos métodos, sólo deberá trabajar sobre la representación interna de un Picture, es decir su atributo img.

-   Ejercicios:

    -   Para resolver los siguientes ejercicios sólo está permitido usar ciclos, condicionales, definición de listas por comprensión, sublistas, map, join, (+), lambda, zip, append, pop, range.

        1.  Implemente los métodos de la clase Picture. Se recomienda que implemente la clase picture por etapas, probando realizar los dibujos que se muestran en la siguiente preguntas.
        2.  Usando únicamente los métodos de los objetos de la clase Picture dibuje las siguientes figuras (invoque a draw):

            *    (a) - ![Ejercicio 1a](Imagenes/ejercicio1.png)

            *    (b) - ![Ejercicio 1b](Imagenes/ejercicio2.png)

            *    (c) - ![Ejercicio 1c](Imagenes/ejercicio3.png)

            

#

## CUESTIONARIO
-   ¿Qué son los archivos *.pyc?

     Los archivos PYC son utilizados por el lenguaje de programación Python. PYC es un archivo ejecutable que contiene el código 
     de bytes compilado para un programa escrito en Python. Bytecode es un conjunto de instrucciones para que el intérprete ejecute 
     el programa.
     
-   ¿Para qué sirve el directorio __pycache__?

     Este es un archivo PYC su ventaja es que son las mismas que las de tener un lenguaje compilado en general: son más rápidos y mejoran 
     el tiempo de ejecución. Mientras que el código fuente del módulo no cambia, el intérprete de Python no va a interpretar el 
     módulo cada vez que un programa se ejecuta. Más bien, se usará la versión "lista" del código. Esto disminuye el tiempo utilizado 
     por la interpretación continua de los mismos archivos de origen.
     
-   ¿Cuáles son los usos y lo que representa el subguión en Python?
     
     En la nomenclatura defunciones y variables, indicando una importancia especifica.
        En este caso,  hay diferentes usos, que están regidos todos, por la convención PEP8, que es la que Python, recomienda como buenas practicas y utiliza.
        Estos pueden ser:

        - Un guión bajo (_) después de un nombre (class_)
            Se utiliza para evitar conflictos con palabras clave o con elementos integrados en Python.

        - Un guión bajo (_) antes de un nombre (_variable)
            En este caso indica que el nombre que sigue al guion es una clase, función, método o variable, con carácter 
            privado o interno, advirtiendo a quien acceda al código, este aspecto de su implementación.
            Una salvedad aquí, es que en Python las variables no son del todo privadas, y si siempre se podrá acceder a ellas.

        - Un doble guión bajo (__) antes de un nombre (__perro)
            En la documentación de Python, se especifica que ” cualquier mombre de la forma __spam se sustituye por 
            _NombreClase__spam”.Para nosotros, NombreClase(),  será el nombre de la clase  donde hemos colocado el 
            doble guión bajo (__).En definitiva, lo que hace Python en este caso, uno de los mas comunes, es manipular 
            el nombre de la clase, para evitar conflictos

        - Un doble guion bajo (__) antes y después de un nombre ( __casa__)
            Esta funcionalidad del guion,  se utiliza para indicar métodos específicos de Python, conocidos como métodos 
            mágicos, __init__, __file__ . Esta convención del lenguaje, es indicativa, normalmente podemos sobrescribir 
            alguno de estos métodos, dándole otro significado, (yo prefiero no hacerlo, pero es totalmente posible).
            Su objetivo no es otro, que evitar conflictos entre los métodos mágicos y algún método definido por nosotros, 
            al momento de escribir el código.

    Facilitando la legibilidad
    
        Podemos usar el guion bajo (_), para separar los dígitos de un número de modo que sea mas fácil leerlo. 
        Esta función es puramente decoradora y actúa un poco
        como el punto(.) que se añade en Excel a trabajar con datos en formato número.
        
    Para internacionalizar cadenas
    
        Tal y como sucede en C el guion bajo(_), se usa para indicar que una cadena es traducible.
        En Python con el uso de  la librería gettext, se aplica esta convención, también

    Ignorar valores
    
        Cuando deseamos ignorar valores  basta con asignar un guion bajo (_). Esta funcionalidad, es fabulosa y 
        puede utilizarse al recorrer arreglos, odesempaquetarlos.

    Almacenando el ultimo valor de interprete:
    
        El guion almacena el ultimo valor que expresa el interprete de Python, incluso nos permite realizar 
        diferentes operaciones matemáticas.

#

## REFERENCIAS
-   https://www.w3schools.com/python/python_reference.asp
-   https://docs.python.org/3/tutorial/

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
