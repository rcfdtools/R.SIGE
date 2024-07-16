# Plantilla para actividades
Keywords: `DEM` `AgreeDEM`

Conceptos de escala. Tomado como referencia los vectores de la red hidrográfica, la red vial y la base predial y utilizando como mapa base la imágen satelital mundial de ESRI o Google, realice la digitalización de un tramo de drenaje de al menos 1 kilómetro y luego digitalice las vías y predios próximos y/o que están ubicados lateralmente.

<div align="center"><img src="graph/AddedValue.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* 


## Requerimientos

* [:notebook:Lectura](../../file/ref/cartilla_pot.pdf): Lineamientos para el uso de información geográfica en el desarrollo del componente rural de los Planes de Ordenamiento Territorial.
* [:mortar_board:Actividad](../TopoBasic/Readme.md): Conceptos básicos de topografía, fotogrametría y fotointerpretación.
* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.


## 1. Conceptos generales de escala

Tomado o adaptado de: Lineamientos para el uso de información geográfica en el desarrollo del componente rural de los Planes de Ordenamiento Territorial, IGAC.[^1]

La escala (entendida como la relación existente entre la distancia en el terreno y su equivalente en el mapa) de la cartografía básica es un aspecto de gran relevancia a la hora de planear el ordenamiento del territorio, pues dependiendo de esta, es posible apreciar mayor o menor cantidad de elementos del paisaje. Así, a mayor escala, se aprecian más elementos y con mayor detalle, mientras que, a menor escala, la información será más general y con menor detalle.

La escala de la cartografía determina la forma y el tamaño en que se ven los elementos del paisaje. Un ejemplo claro de ello es la forma como se ven las construcciones. Cuando estas se representan en una escala general, se ven como puntos, y al aumentar la escala, las mismas aparecen como polígonos, siendo más grandes cuanto mayor es la escala.

<div align="center"><img src="graph/IGAC_ConceptoEscala.png" alt="R.SIGE" width="100%" border="0" /><sub><br>Tomado de: <a href="../../ref/cartilla_pot.pdf">Concepto de escala. IGAC, 2019</a></sub><br><br></div>

La cartografía básica de Colombia creada por el [Instituto Geográfico Agustín Codazzi - IGAC](https://www.igac.gov.co/), puede ser descargada desde www.colombiaenmapas.com a nivel general en escalas 1:500000 (Precisión planimétrica de 1000m y altimétrica de 100m), 1:100000 (Precisión planimétrica de 200m y altimétrica de 50m) y por planchas a escala 1:25000 (Precisión planimétrica de 50m y altimétrica de 25m). 

<div align="center"><img src="graph/CartografiaBasicaIGAC.png" alt="R.SIGE" width="100%" border="0" /></div>

Es de aclarar que, en el ámbito municipal, para el ejercicio del ordenamiento territorial, tradicionalmente se ha privilegiado el uso de cartografía a escala 1:25.000 para el sector rural y 1:5.000 o 1:2.000 en el sector urbano. Sin embargo, el IGAC recomienda que para la formulación y/o procesos de revisión y ajuste de los POT, la escala de la cartografía se defina en función de los procesos y dinámicas de cada territorio. En este sentido, se propone que para el suelo rural se contemplen factores como el área municipal, la pendiente, el tamaño de los predios, la densidad de la red hidrográfica y de la infraestructura vial, entre otros.

En la siguiente tabla se relaciona la escala ideal de trabajo recomendada a escala rural de acuerdo con las características mencionadas.

<div align="center">

| Escala    | Pendientes           | Densidad de la<br>red hidrográfica | Densidad de la infra-<br>estructura vial | Tamaño predios                    |
|-----------|----------------------|------------------------------------|------------------------------------------|-----------------------------------|
| 1:100.000 | Moderada: hasta 12%  | Baja: <3 km/km2                    | Baja: <3 km/km2                          | Latifundio: >200 Ha               |
| 1:25.000  | Montañosa: >12%      | Alta: >3 km/km2                    | Alta: >3 km/km2                          | Mediano a pequeño: De 10 a 200 Ha |
| 1:10.000  | Montañosa: >12%      | Alta: >3 km/km2                    | Alta: >3 km/km2                          | Minifundio: De 3 a 10 Ha          |
| 1:5.000   | Montañosa: >12%      | Alta: >3 km/km2                    | Alta: >3 km/km2                          | Microfundio: <3 Ha                |

</div>

Con base en la información de la tabla anterior, se recomienda que para el suelo rural de aquellos municipios localizados en las zonas montañosas, se utilice cartografía básica a escala 1:10.000 y para los ubicados sobre los valles interandinos y las costas Caribe y Pacífica, cartografía básica a escala 1:25.000. Por otro lado, para la mayoría de municipios del oriente del país, en donde existen características homogéneas de cobertura boscosa y territorios colectivos, se considera suficiente la cartografía a escala 1:100.000. 

Asimismo, teniendo en cuenta los factores mencionados en la anterior, se recomienda que para las áreas urbanas, de expansión urbana y centros poblados, se utilice información geográfica con escalas entre 1:1.000 y 1:5.000. Adicionalmente, para definir la escala, se deben tener en cuenta las dinámicas de urbanización y las relaciones del sistema de asentamientos, lo que permitirá un análisis detallado de la distribución de los procesos físicos, ambientales, y sociales que allí se presentan. Además, se debe contemplar la información catastral, de gran importancia y utilidad para el conocimiento de las estructuras y las dinámicas urbanas.


## 2. Digitalización de drenajes

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _Digitizing_, establezca el CRS 9377. Agregue al mapa la capa de drenajes disponible en la ruta `\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\shp\HIDROGRAFIA.shp`, ajuste la simbología y rotule a partir del campo `NOMBRE`.  

<div align="center"><img src="graph/ArcGISPro_Hidrografia_shp.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Desde el menú _Map_, cambie el mapa base por _Imagery_ y acérquese al mapa a escala 1:5000 en la coordenada: 4892883.22E, 2111592.87N. Como puede observar, la digitalización existente del Río Neusa, no representa con precisión el eje del cauce.

> Para la localización de la coordenada indicada puede dar clic derecho sobre cualquier zona del mapa, y utilizar la opción _Go To XY_.

<div align="center"><img src="graph/ArcGISPro_Hidrografia_RioNeusa1.png" alt="R.SIGE" width="100%" border="0" /></div>

> Si bien, según la recomendación del IGAC es utilizar información a escala 1:5000 para zonas rurales con características similares a las mostradas en la imagen, para este ejercicio, realizaremos la digitalización a escala 1:1000 del tramo comprendido entre la descarga del Río Susagua al Río Neusa, hasta la descarga en el Río Bogotá.

<div align="center"><img src="graph/ArcGISPro_Hidrografia_RioNeusa2.png" alt="R.SIGE" width="100%" border="0" /></div>

3. Para la creación de la nueva capa de drenajes, en el _Catalog Pane_ localizado en la parte derecha de la ventana de ArcGIS Pro, de clic derecho sobre la carpeta `\R.SIGE\file\shp\` y seleccione la opción _New / New Shapefile_. Nombre la nueva capa como _Drenaje.shp_.

<div align="center"><img src="graph/ArcGISPro_NewShapefile_Drenaje.png" alt="R.SIGE" width="50%" border="0" /></div>

Para esta nueva capa, defina la geometría tipo Polilínea, sin propiedades de medición (M), sin valores 3D (Z) y establezca el CRS 9377. Agregue la capa al mapa.

<div align="center"><img src="graph/ArcGISPro_NewShapefile_Drenaje1.png" alt="R.SIGE" width="50%" border="0" /></div>

Abra la tabla de atributos y cree los siguientes campos:

<div align="center">

| Campo       | Descripción                                                                                                                   |    Tipo    | Propiedad<br>ArcGIS Pro | 
|:------------|:------------------------------------------------------------------------------------------------------------------------------|:----------:|:-----------------------:| 
| DrenajeID   | Código de identificación del drenaje.                                                                                         |    Long    |           N/A           |
| DrenajeNom  | Nombre del drenaje.                                                                                                           | Text (100) |           N/A           |
| DrenajeSub  | Nombre del subtramo de drenaje.                                                                                               | Text (100) |           N/A           |
| CotaInicio  | Cota punto inicial en metros.                                                                                                 |   Double   |           N/A           |
| CotaFin     | Cota punto final en metros.                                                                                                   |   Double   |           N/A           |
| Pendiente   | Pendiente media del cauce, calculada a partir de la diferencia de cotas entre la longitud.                                    |   Double   |           N/A           |
| IndSinuoso  | Índice de sinuosidad, calculada a partir de la longitud del rio entre la longitud euclidiana entre el punto inicial y final.  |   Double   |           N/A           |
| LGm         | Longitud geodésica en metros                                                                                                  |   Double   |    Length (geodesic)    |

</div>

<div align="center"><img src="graph/ArcGISPro_Drenaje_AddField.png" alt="R.SIGE" width="50%" border="0" /></div>

4. Para la digitalización, acérquese a escala 1:1000 y en el menú _Edit_ de clic en 


> Se recomienda digitalizar los drenajes en el sentido del flujo.


Calcular el índice de sinuosidad.


## 3. Digitalización de predios



## 4. Digitalización de vías

Medianeras entre manzanas urbanas o predios


## 2. Análisis usando software libre - QGIS

Para el desarrollo de las actividades desarrolladas en esta clase, se pueden utilizar en QGIS las siguientes herramientas o geo-procesos:

| Proceso                                                                                                         | Procedimiento                                                                                                                                                                                                                                   |
|:----------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Simbología                                                                                                      | Modificable desde las propiedades de la capa en la pestaña _Symbology_.                                                                                                                                                                         |
| Rotulado                                                                                                        | Modificable desde las propiedades de la capa en la pestaña _Labels_.                                                                                                                                                                            |

Ejemplo rótulo en QGIS: `'A(ha): ' ||  round("AGha", 2) || '\n' || 'P (m): ' ||  round("PGm", 2) `


## Elementos requeridos en diccionario de datos

Agregue a la tabla resúmen generada en la actividad [Inventario de información geo-espacial recopilada del POT y diccionario de datos](../POTLayer/Readme.md), las capas generadas en esta actividad que se encuentran listadas a continuación:

| Nombre                           | Descripción                                                                                                                  | Geometría   | Registros | 
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------|-----------| 
|                                  |                                                                                                                              | Polígono 2D | 14        | 
|                                  |                                                                                                                              | Polígono 2D | 14        | 
|                                  |                                                                                                                              | Polígono 2D | 14        | 

> :bulb:Para funcionarios que se encuentran ensamblando el SIG de su municipio, se recomienda incluir y documentar estas capas en el Diccionario de Datos.



## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad     | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P1** | Esta actividad no requiere del desarrollo de elementos en el avance del proyecto final, los contenidos son evaluados en el quiz de conocimiento y habilidad.                                                                                                                                                                                                                                                                                        | 
| Avance **P1** | :compass:Mapa digital impreso _P1-1: xxxx_<br>Incluir xxxxx.<br>Embebido dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                                                                                                                                      | 
| Avance **P1** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. | 

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Referencias

* 


## Control de versiones

| Versión    | Descripción                                                | Autor                                      | Horas |
|------------|:-----------------------------------------------------------|--------------------------------------------|:-----:|
| 2024.02.24 | Versión inicial con alcance de la actividad                | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.06.27 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   8   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../RoadSummary/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|-------------------------------------------------------|-----------------------------------|--------------------------------------------------------------------------------------|-------------------------------|

[^1]: Lineamientos para el uso de información geográfica en el desarrollo del componente rural de los Planes de Ordenamiento Territorial