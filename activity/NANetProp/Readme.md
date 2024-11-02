# Homologación de red vial urbana y rural
Keywords: `network-properties` `hierarchy` `oneway`

En la carpeta GDB cree una File Geodatabase y un dataset para la integración de la red vial. Importe al dataset las vías municipales y homologue a los atributos para modelación de redes viales. Seleccione todas las vías y ejecute la función Planarize que le permitira obtener tramos independientes entre intersecciones (recalcule longitudes y tiempos de viaje en cada tramo).

<div align="center"><img src="graph/NANetPro.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Crear una base de datos geográfica y un Network Dataset para simulación de redes vehiculares
* Homologar los atributos de la red vial municipal


## Requerimientos

* [:mortar_board:Actividad](../RoadSummary/Readme.md): Análisis estadístico de la red vial.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.


## 1. Procedimiento general en ArcGIS Pro

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _NetworkAnalyst_ y establezca el CRS 9377. Agregue al mapa la capa de la red vial municipal disponible en la ruta `\file\gdb\SIGE.gdb\Red_vial` y ajuste la simbología a valores únicos representando el campo de atributos `ZonaNombre`.  

<div align="center"><img src="graph/ArcGISPro_AddLayer1.jpg" alt="R.SIGE" width="100%" border="0" /></div>

2. Dentro de la carpeta `\file\GDB`, cree una File Geodatabase con el nombre _RedVial_ y un dataset llamado _ModeloVial_ asignando el CRS 9377.

<div align="center"><img src="graph/ArcGISPro_CreateGDB.jpg" alt="R.SIGE" width="100%" border="0" /></div>

3. Importe al dataset _ModeloVial_, la capa _Red_vial_. Desde el panel lateral izquierdo _Contents_, modifique la fuente de datos de cla capa _Red_vial_ hacia la ruta de la GDB del _ModeloVial_. Renombre como `T25899EjeVial`.

<div align="center"><img src="graph/ArcGISPro_GDBImportLines.jpg" alt="R.SIGE" width="100%" border="0" /></div>

4. En la tabla de atributos de la red vial, cree los siguientes atributos:

<div align="center">

| Atributo    | Descripción                                                                                                                | Tipo       |
|:------------|:---------------------------------------------------------------------------------------------------------------------------|:-----------|
| Name        | Nombre de la vía                                                                                                           | Text (255) |
| Class       | Clase de vía (Autopista, Calle, Camino, Carrera, Diagonal, Ferrea, Peatonal, Transversal, Sin Clase)                       | Text (255) |
| Meters      | Longitud de tramo en metros                                                                                                | Double     |
| kph         | Velocidad de tramo en kilómetros / hora                                                                                    | Double     |
| Oneway      | Sentido vial vector (TF, FT, N). To, From, Not                                                                             | Text (2)   |
| Hierarchy   | Jerarquía víal de 1 a n                                                                                                    | Long       |
| Func_Class  | Clasificador víal numérico en función de la clase y jerarquía                                                              | Long       |
| FT_Minutes  | Tiempo de viaje en minutos, desde a hacia o hacia desde. Calcular con la expresión FT_Minutes = (!Meters!/1000)/(!KPH!/60) | Double     |
| TF_Minutes  | Tiempo de viaje en minutos, hacia a desde. Calcular con la expresión FT_Minutes = (!Meters!/1000)/(!KPH!/60)               | Double     |

</div>

> Atributos complementarios: en caso de que la red vial incluya puentes, deprimidos, tramos sin pavimentar, zonas de paso peatonal y otros elementos importantes, deberá incluir estos atributos

<div align="center"><img src="graph/ArcGISPro_AddField1.jpg" alt="R.SIGE" width="100%" border="0" /></div>








## 2. Análisis usando software libre - QGIS

Para el desarrollo de las actividades desarrolladas en esta clase, se pueden utilizar en QGIS las siguientes herramientas o geo-procesos:

| Proceso            | Procedimiento                                                           |
|:-------------------|:------------------------------------------------------------------------|
| Simbología         | Modificable desde las propiedades de la capa en la pestaña _Symbology_. |
| Rotulado           | Modificable desde las propiedades de la capa en la pestaña _Labels_.    |

Ejemplo rótulo en QGIS: `'A(ha): ' ||  round("AGha", 2) || '\n' || 'P (m): ' ||  round("PGm", 2) `

[:notebook:QGIS training manual](https://docs.qgis.org/3.34/en/docs/training_manual/)  
[:notebook:Herramientas comúnmente utilizadas en QGIS](../QGIS.md)


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
| Avance **P7** | Esta actividad no requiere del desarrollo de elementos en el avance del proyecto final, los contenidos son evaluados en el quiz de conocimiento y habilidad.                                                                                                                                                                                                                                                                                        | 
| Avance **P7** | :compass:Mapa digital impreso _P7-1: xxxx_<br>Incluir xxxxx. Embebido dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                                                                                                                                          | 
| Avance **P7** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. | 

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Referencias

* [ArcGIS Pro - Network Analyst tutorials](https://pro.arcgis.com/en/pro-app/latest/help/analysis/networks/network-analyst-tutorials.htm)
* [ArcGIS Pro - Create a network dataset](https://pro.arcgis.com/en/pro-app/latest/help/analysis/networks/how-to-create-a-usable-network-dataset.htm)


## Control de versiones

| Versión    | Descripción                                                | Autor                                      | Horas |
|------------|:-----------------------------------------------------------|--------------------------------------------|:-----:|
| 2024.02.24 | Versión inicial con alcance de la actividad                | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.06.27 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   8   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../xxxx) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|---------------------|-------------------|---------------------------------------------------------------------------|---------------|

[^1]: 