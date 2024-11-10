# Network Analyst - Estudio de rutas de transporte escolar
Keywords: `school` `route` `network-solve` `facilities`

Realice un análisis de ruta única óptima que permita recorrer las instituciones educativas y determine el tiempo y distancia total recorrida. Defina como tolerancia de búsqueda 1000 metros e indique cuáles instituciones no han sido cubiertas. Active las restricciones y modos de transporte establecidas sin permitir giros en U. Para las instituciones cubiertas determine la distancia hasta la red. Muestre el detalle de las instrucciones de recorrido. Realice un análisis de ruta óptima por categoría de institución educativa que permita recorrer las instituciones educativas y determine los tiempos y distancias totales recorridas por cada ruta. Resuelva el recorrido de la red simulando un accidente en una localización específica, compare los tiempos y distancias con los obtenidos anteriormente. Resuelva el recorrido de la red simulando cierre completo en el centro histórico. 

<div align="center"><img src="graph/NASchoolRoute.jpg" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Resolver rutas escolares generales y por categorías
* Resolver redes simulando eventos de bloqueo


## Requerimientos

* [:mortar_board:Actividad](../NADataset/Readme.md): Creación y configuración del network dataset.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.


## 1. Creación y configuración de la red de análisis

1. Abra el proyecto de ArcGIS Pro y el mapa _NetworkAnalyst_ creado previamente. En el Dataset `ModeloVial` contenido en la GDB, de clic derecho y seleccione la opción _Create Network Dataset_, nombre como `ModeloVial_ND` y seleccione el feature class `T25899EjeVialPlanarize`. En caso de que su red corresponda a líneas 3D o haya incluido atributos para pasos elevados o deprimidos, seleccione la opción `Elevation Fields`. Remueva el Network Dataset del mapa para que se puedan modificar sus propiedades.

<div align="center"><img src="graph/ArcGISPro_CreateNetworkDataset1.jpg" alt="R.SIGE" width="100%" border="0" /></div>




## Elementos requeridos en diccionario de datos

Agregue a la tabla resúmen generada en la actividad [Inventario de información geo-espacial recopilada del POT y diccionario de datos](../POTLayer/Readme.md), las capas generadas en esta actividad que se encuentran listadas a continuación:

| Nombre         | Descripción    | Geometría      | Registros      | 
|----------------|----------------|----------------|----------------| 
| (No requerido) | (No requerido) | (No requerido) | (No requerido) | 

> :bulb:Para funcionarios que se encuentran ensamblando el SIG de su municipio, se recomienda incluir y documentar estas capas en el Diccionario de Datos.


## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad     | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P7** | Para su caso de estudio, cree, configure y verifique que se creen los nodos de intersección de la red vehicular que permita explorar sus propiedades.                                                                                                                                                                                                                                                                                               | 
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
| 2024.04.13 | Versión inicial con alcance de la actividad                | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.11.04 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |  3   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../NADataset/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/47) | [Siguiente :arrow_forward:]() |
|-----------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------|-------------------------------|

[^1]: 