# Network Analyst - Creación y configuración del network dataset
Keywords: `facilities` `emergencies`

En el dataset contenido en la GDB, crear el dataset para modelación de redes viales a partir de los ejes viales homologados. Acceda a las propiedades de la red y realize las configuraciones de conectividad, costos, sentidos viales, giros en U y vías con restricción vehicular.    

<div align="center"><img src="graph/NADataset.jpg" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Crear y configurar el network dataset
* Definir atributos de costos, giros permitidos y prohibidos, restricción vehicular y modos de transporte.


## Requerimientos

* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.


## 1. Importación de establecimientos educativos y homologación de atributos 

1. Abra el proyecto de ArcGIS Pro y el mapa _NetworkAnalyst_ creado en la actividad anterior. Importe a la GDB _RedVial_, la capa _\data\POT\Anexo_Acuerdo_012_2013\gdb\25899.gdb\CARTOGRAFIA\EDUCATIVO_ de la cartografía del POT, correspondiente a la localización de instituciones educativas y nombre cómo T25899Educacion. Agregue al mapa y simbolice utilizando el _Pushpin School_.

<div align="center"><img src="graph/ArcGISPro_AddLayer1.jpg" alt="R.SIGE" width="100%" border="0" /></div>







## Elementos requeridos en diccionario de datos

Agregue a la tabla resúmen generada en la actividad [Inventario de información geo-espacial recopilada del POT y diccionario de datos](../POTLayer/Readme.md), las capas generadas en esta actividad que se encuentran listadas a continuación:

| Nombre           | Descripción                                                            | Geometría | Registros | 
|------------------|------------------------------------------------------------------------|-----------|-----------| 
| T25899Educacion  | Localización de establecimientos educativos                            | Point 2D  | 74        | 
| T25899Emergencia | Localización de puntos de interes y centros de atención de emergencias | Point 2D  | 341       | 

> :bulb:Para funcionarios que se encuentran ensamblando el SIG de su municipio, se recomienda incluir y documentar estas capas en el Diccionario de Datos.


## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad     | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P7** | Para su caso de estudio, importe y homologue los centros educativos y de atención de emergencias.                                                                                                                                                                                                                                                                                                                                                   | 
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
| 2024.04.12 | Versión inicial con alcance de la actividad                | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.11.04 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   5   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../Hazard/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/46) | [Siguiente :arrow_forward:]() |
|--------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------|-------------------------------|

[^1]: 