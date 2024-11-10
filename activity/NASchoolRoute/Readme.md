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


## 1. Ruta óptima global

Realice un análisis de ruta única óptima que permita recorrer las instituciones educativas y determine el tiempo y distancia total recorrida. Defina como tolerancia de búsqueda 1000 metros e indique cuáles instituciones no han sido cubiertas. Active las restricciones y modos de transporte establecidas sin permitir giros en U. Para las instituciones cubiertas determine la distancia hasta la red. Muestre el detalle de las instrucciones de recorrido

1. Abra el proyecto de ArcGIS Pro y el mapa _NetworkAnalyst_ creado previamente, en contents verifique que esté cargado el Network Dataset y selecciónelo. En el menú superior _Network Dataset Layer - Data_, seleccione la opción _Network Analysis / Route_.

<div align="center"><img src="graph/ArcGISPro_Route1.jpg" alt="R.SIGE" width="100%" border="0" /></div>

2. En el panel lateral _Contents_, seleccione _Stops_ en _Route_ y en el menú _Route Layer - Data_, de clic en _Import Stops_. En la ventana de importación de localizaciones, seleccione en _Input Locations_ la capa o feature class `T25899Educacion` y establezca la tolerancia de búsqueda en 1000 metros.

> Debido a que previamente se realizó la definición de atributos con nombres compatibles con esta herramienta y se realizó la configuración de del Dataset, automáticamente han sido asociados el campo de nombre y los elementos de criterio de búsqueda relacionados con la red vial y sus nodos.

<div align="center"><img src="graph/ArcGISPro_Route2.jpg" alt="R.SIGE" width="100%" border="0" /></div>
 
Luego de dar clic en aceptar, podrá observar que se han cargado las localizaciones de la red a resolver. Abra y explore la tabla de atributos, observará que la secuencia ha sido definida en el mismo orden de entidades de la capa de instituciones educativas. El campo `DistanceToNetworkInMeters` contiene el cálculo inicial de proximidad hasta el punto más cercano en la red.

<div align="center"><img src="graph/ArcGISPro_Route3.jpg" alt="R.SIGE" width="100%" border="0" /></div>

3. Para resolver la red optimizando la secuencia de viaje, en _Contents_ seleccione _Route_ y en el menu _Route Layer_ seleccione la opción Travel _Settings / Sequence / Find Best_ y luego de clic en _Run_. Podrá observar que se ha resuelto la ruta óptima. De clic en el expansor de la pentaña _Analysis_ para conocer qué instituciones educativas no pudieron ser resueltas, podrá observar que dos de ellas no cumplen con los criterios establecidos de solución.

<div align="center"><img src="graph/ArcGISPro_Route4.jpg" alt="R.SIGE" width="100%" border="0" /></div>

4. Para conocer la secuencia de barrido, los tiempos de viaje y las distancias acumuladas, revise las columnas de atributos `Sequence`, `Cumul_Minutes` y `Cumul_Meters`.

<div align="center"><img src="graph/ArcGISPro_Route5.jpg" alt="R.SIGE" width="100%" border="0" /></div>




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