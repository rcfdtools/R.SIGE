# Conceptos básicos de topografía, fotogrametría y fotointerpretación
Keywords: `Topography` `Photogrammetric`

La topografía se trata de la medición de las características físicas o geométricas de la Tierra. Los levantamientos topográficos se clasifican a menudo por el tipo de datos estudiados o por los instrumentos o métodos utilizados. Algunos ejemplos son los estudios geodésicos, geológicos, topográficos, hidrográficos, terrestres, geofísicos, de suelos, de minas y de ingeniería.[^1]

<div align="center"><img src="graph/Gravity_anomalies_on_Earth.png" alt="R.SIGE" width="50%" border="0" /><sub><br>Tomado de: <a href="Public Domain, https://commons.wikimedia.org/w/index.php?curid=479365">https://commons.wikimedia.org</a></sub><br><br></div>


## Objetivos

* Entender conceptos básicos de topografía y sus ramas derivadas.
* Entender su aplicación y utilidad.
* Entender las diferencias entre planimetría y altimetría. 


## Requerimientos

* Lectura de [Conceptos básicos de geografía](https://www.esri.com/es-es/geographic-approach/overview).
* Lectura de [Geografía y Gobierno](https://www.esri.com/es-es/geographic-approach/case-studies/government).



## ¿Qué es la Topografía?[^2]

La topografía es una ciencia que estudia el conjunto de procedimientos para determinar las posiciones relativas de los puntos sobre la superficie de la tierra y debajo de la misma, mediante la combinación de las medidas según los tres elementos del espacio: 

* Distancia
* Elevación
* Dirección

> La topografía explica los procedimientos y operaciones del trabajo de campo, los métodos de cálculo o procesamiento de datos y la representación del terreno en un plano o dibujo topográfico a escala. La combinación de estos elementos se denomina Levantamiento topográfico.


## Ramas principales de la topografía

Las 3 ramas principales de la topografía son la geodesía, la fotogrametría y la topografía plana.

> Tenga en cuenta que la definición de estas ramas puede variar de un autor a otro y que estas 3 ramas han sido utilizadas para ilustrar esta actividad.


### A.Geodesia[^2]

Trata de las mediciones de grandes extensiones de terreno, por ejemplo, para crear la carta geográfica de un país, para establecer fronteras y límites internos, para la determinación de líneas de navegación en ríos y lagos, etc. Estos levantamientos tienen en cuenta la verdadera forma de la tierra y requieren de gran precisión. 

Cuando la zona no es demasiado extensa, se puede obtener la precisión requerida considerando la tierra como una esfera perfecta, pero si dicha superficie es muy grande debe adoptarse la verdadera forma elipsoidal de la superficie terrestre.

<div align="center"><img src="graph/WGS84_mean_Earth_radius.svg" alt="R.SIGE" width="50%" border="0" /><sub><br>Tomado de: <a href="https://commons.wikimedia.org/wiki/File:WGS84_mean_Earth_radius.svg">https://commons.wikimedia.org</a></sub><br><br></div>

> Los levantamientos de grandes ciudades se hacen bajo el supuesto de que la tierra es perfectamente esférica. Este tipo de levantamiento está catalogado como de alta precisión e incluye el establecimiento de los puntos de control primario o puntos geodésicos, que son puntos debidamente materializados sobre la superficie de la tierra, es decir, con posiciones y elevaciones conocidas, las cuales son de gran importancia y trascendencia por constituir puntos o redes de apoyo y referencia confiables para todos los demás levantamientos de menor precisión. Los puntos fijados geodésicamente (levantamiento de control), como por ejemplo los vértices de triangulación, constituyen una red a la que puede referirse cualquier otro levantamiento sin temor a error alguno en distancias horizontal o vertical o en dirección, derivado de la diferencia entre la superficie de referencia y la verdadera superficie de la tierra. 


#### Red geodésica de control

Los levantamientos de alta precisión  requieren del establecimiento de puntos de control primario o puntos geodésicos, que son puntos debidamente materializados sobre la superficie de la tierra, es decir, con posiciones y elevaciones conocidas, las cuales son de gran importancia y trascendencia por constituir puntos o redes de apoyo y referencia confiables para todos los demás levantamientos de menor precisión.

<div align="center"><img src="graph/Ubersicht_der_Stationen.png" alt="R.SIGE" width="70%" border="0" /><sub><br>Tomado de: <a href="https://commons.wikimedia.org/wiki/File:%C3%9Cbersicht_der_Stationen.PNG">https://commons.wikimedia.org</a></sub><br><br></div>


#### Sistema global de navegación por satélite - GNSS[^3]

Los sistemas de navegación por satélite transmiten información de geolocalización altamente precisa a los dispositivos y receptores GNSS para determinar su ubicación actual, tales como GPS, GLONASS y Galileo.

<div align="center"><img src="graph/Archeological_research_at_the_Bilsk_hillfort.png" alt="R.SIGE" width="100%" border="0" /><sub><br>Tomado de: <a href="https://commons.wikimedia.org/wiki/File:%D0%97%D0%B9%D0%BE%D0%BC%D0%BA%D0%B0_%D0%B2%D0%B0%D0%BB%D1%96%D0%B2_%D0%91%D1%96%D0%BB%D1%8C%D1%81%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B8%D1%89%D0%B0_(%D0%9F%D0%BE%D0%BE%D0%BB%D1%82%D0%B0%D0%B2%D1%89%D0%B8%D0%BD%D0%B0)_%D0%B2%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BC_GNSS-%D0%BF%D1%80%D0%B8%D0%B9%D0%BC%D0%B0%D1%87%D0%B5%D0%BC.jpg">https://commons.wikimedia.org</a></sub><br><br></div>

GNSS significa Sistema global de navegación por satélite y se utiliza para describir cualquier sistema de navegación por satélite con cobertura global. Los sistemas de navegación por satélite transmiten información de geolocalización altamente precisa a los dispositivos y receptores GNSS para determinar su ubicación actual.

> En la mayoría de partes del mundo, es habitual hacer referencia a la navegación global como GPS (Sistema de posicionamiento global). En la práctica, el GPS es un sistema especial basado en Norteamérica. Hay un número creciente de sistemas de navegación por satélite disponibles para el público internacional. Se recomienda utilizar el término GNSS para describir todos los sistemas, ya que es el término más representativo internacionalmente.

<div align="center"><img src="graph/GNSS.png" alt="R.SIGE" width="60%" border="0" /><sub><br>Tomado de: <a href="www.swisstopo.admin.ch">www.swisstopo.admin.ch</a></sub><br><br></div>

<div align="center"><img src="graph/DGPS_Reference_Station.png" alt="R.SIGE" width="40%" border="0" /><sub><br>Ejemplo de una estación de referencia GNSS<br>Tomado de: <a href="https://commons.wikimedia.org/wiki/File:DGPS_Reference_Station.jpg">https://commons.wikimedia.org</a></sub><br><br></div>

## B.Fotogrametría[^2]

Es la disciplina que utiliza las fotografías para la obtención de mapas de terrenos. Los levantamientos fotogramétricos comprenden la obtención de datos y mediciones precisas a partir de fotografías del terreno tomadas con cámaras especiales u otros instrumentos sensores, ya sea desde aviones o drones (fotogrametría aérea) o desde puntos elevados del terreno (fotogrametría terrestre) y que tiene aplicación en trabajos topográficos. Se utilizan los principios de la perspectiva para la proyección sobre planos a escala, de los detalles que figuran en las fotografías. Los trabajos fotogramétricos deben apoyarse sobre puntos visibles y localizados por métodos de triangulación topográfica o geodésicos que sirven de control tanto planimétrico como altimétrico.

<div align="center"><img src="graph/Topografia-Con-Drones-Visual-Drone-t2.png" alt="R.SIGE" width="40%" border="0" /><sub><br>Ejemplo de una estación de referencia GNSS<br>Tomado de: <a href="https://visualdrone.co/">Tomado de: https://visualdrone.co/</a></sub><br><br></div>

> El trabajo consiste en esencia en tomar fotografía desde dos o más estaciones adecuadas y utilizarlas después para obtener los detalles del terreno fotografiado, tanto en planta como en alzado o perfil. 


## Actividades complementarias :pencil2:

En la siguiente tabla se listan las actividades complementarias que deben ser desarrolladas y documentadas por el estudiante en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (mostrar nombre completo, código y enlace a su cuenta de GitHub), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.


| Actividad | Alcance |
|:---------:|:--------|
|     1     | ....    | 


## Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas para de digitalización con opciones de encajado o snapping.
* 



## Referencias

* https://globalgpssystems.com/gnss/gnss-constellations-how-they-work-and-how-they-improve-gps
* https://pro.arcgis.com/es/pro-app/latest/help/mapping/device-location/gnss-and-location-devices.htm 


## Control de versiones

| Versión    | Descripción     | Autor                                      | Horas |
|------------|:----------------|--------------------------------------------|:-----:|
| 2022.07.20 | Versión inicial | [rcfdtools](https://github.com/rcfdtools)  |   0   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](../xxxx) | [Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente]() |
|---------------------|-------------------|---------------------------------------------------------------------------|---------------|

[^1]: https://support.esri.com/es-es/gis-dictionary/surveying
[^2]: https://www.ecomexico.net/
[^3]: https://pro.arcgis.com/es/pro-app/latest/help/mapping/device-location/gnss-and-location-devices.htm