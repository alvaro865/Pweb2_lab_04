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
    4.  join: Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual
        
        - ![Ejercicio 4](Imagenes/imagen3.png)
        
        - ![Ejercicio 4](Imagenes/imagen3_1.png)
        
    5.  up: Devuelve una nueva figura poniendo la figura recibida como argumento, encima de la figura actual
        
        - ![Ejercicio 5](Imagenes/imagen4.png)
        
        - ![Ejercicio 5](Imagenes/imagen4_1.png)
        
    6.  under: Devuelve una nueva figura poniendo la figura recibida como argumento, sobre la figura actual
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

            *    (a) ![(a)](imagenes/ejercicio_02_a.png)

            *    (b) ![(b)](imagenes/ejercicio_02_b.png)

            *    (c) ![(c)](imagenes/ejercicio_02_c.png)

            *    (d) ![(d)](imagenes/ejercicio_02_d.png)

            *    (e) ![(e)](imagenes/ejercicio_02_e.png)

            *    (f) ![(f)](imagenes/ejercicio_02_f.png)

            *    (g) ![(g)](imagenes/ejercicio_02_g.png)

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
