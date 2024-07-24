# Creación de base de datos geográfica del proyecto - GDB
Keywords: `geodatabase` `dataset` `relation` `table` `domain` `grid`

Cree una base de datos geográfica (file geodatabase) con grupos de capas o Datasets, e importe y reproyecte las capas y clases de entidad recopiladas y creadas en actividades anteriores.

<div align="center"><img src="graph/GDB.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Crear una base de datos geográfica para integrar la información espacial del caso de estudio.
* Agrupar en datasets, las capas recopiladas y producidas en el caso de estudio.


## Requerimientos

* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos. 
* [:notebook:Lectura](https://desktop.arcgis.com/es/arcmap/latest/manage-data/geodatabases/what-is-a-geodatabase.htm): Información general de las bases de datos, ESRI.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.


## 1. Creación de estructura (geodatabase y datasets)

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _GDB_ y establezca el CRS 9377. En el árbol de catálogo, localice la carpeta `\file\data\gdb\`, de clic derecho sobre la raíz de esta carpeta y seleccione la opción _New / File Geodatabase_ y nombre la base de datos como `SIGE`. Al crear la base de datos, automáticamente se asignará la extensión _.gdb_.

> Como puede observar, en ArcGIS Pro se pueden crear dos tipos de bases geográficas, las _File Geodatabase_ son bases de datos corporativas que utilizan múltiples archivos y que pueden procesar grandes volúmenes de información; por otra parte, las _Mobile Geodatabase_ son bases compactas que utilizan un archivo principal único (y en algunos casos archivos complementarios de indexación) y aunque pueden almacenar gran cantidad de tablas y clases de entidad, su eficiencia no es óptima. 

<div align="center"><img src="graph/ArcGISPro_NewFileGeodatabase.png" alt="R.SIGE" width="100%" border="0" /></div>

Al revisar el directorio de datos, encontrará que se han creado múltiples archivos con nombres similares y con diferentes extensiones.

<div align="center"><img src="graph/Windows11_GeodatabaseFolder.png" alt="R.SIGE" width="100%" border="0" /></div>

> Tenga en cuenta que ArcGIS Pro no ofrece conexiones a bases de datos en formato Microsoft Access .mdb, como sí lo realizaba ArcGIS for Desktop.

2. El siguiente paso es crear los conjuntos de datos o _Datasets_ que utilizará la base de datos, para ello, de clic en la raíz de la geodatabase _SIGE_,  seleccione la opción _New / Feature Dataset_, defina el CRS 9377. Crearemos los siguientes Datasets:

<div align="center">

| Dataset                                  | Descripción                                                                                                          | Fuente de datos                                                                                   |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| IGAC2013Cartografia                      | Información cartográfica IGAC 2013, utilizada en el diagnóstico del POT.                                             | \file\data\POT\ Anexo_Acuerdo_012_2013\ gdb\25899.gdb\CARTOGRAFIA                                 |
| IGAC2013EntidadTerritorialAdministrativa | Información de entidades territoriales y administrativas IGAC 2013, utilizada en el diagnóstico del POT.             | \file\data\POT\ Anexo_Acuerdo_012_2013\ gdb\25899.gdb\ ENTIDADES_TERRITORIALES_ Y_ADMINISTRATIVAS |
| IGAC2013Rural                            | Información geográfica zona rural IGAC 2013, utilizada en el diagnóstico del POT.                                    | \file\data\POT\ Anexo_Acuerdo_012_2013\ gdb\25899.gdb\RURAL                                       |
| IGAC2013Urbano                           | Información geográfica zona urbana IGAC 2013, utilizada en el diagnóstico del POT.                                   | \file\data\POT\ Anexo_Acuerdo_012_2013\ gdb\25899.gdb\URBANO                                      |
| POT2013Formulacion                       | Información geográfica adaptada o producida en la formulación del POT.                                               | \file\data\POT\ Anexo_Acuerdo_012_2013\ shp\                                                      |
| SIGE                                     | Importación de archivos de formas vectoriales en formato shapefile, creados en actividades anteriores de este curso. | \file\data\shp\                                                                                   |
| Temp                                     | Carpeta para volcado temporal de clases de entidad geográficas.                                                      | N/A                                                                                               |
|                                          |                                                                                                                      |                                                                                                   |

</div>

> En la raíz de la base de datos geográfica _SIGE_, importaremos las tablas _Registro1_ y _Registro2_ que serán renombradas como _IGAC2009Registro1_ e _IGAC2009Registro2_.

<div align="center"><img src="graph/ArcGISPro_NewDataset.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_NewDataset1.png" alt="R.SIGE" width="100%" border="0" /></div>

Una vez terminada la creación de los diferentes datasets, podrá observar su estructura en el _Catalog Pane_.

<div align="center"><img src="graph/ArcGISPro_NewDataset2.png" alt="R.SIGE" width="40%" border="0" /></div>


## 2. Importación de entidades

1. 

<div align="center"><img src="graph/ArcGISPro_NewDataset2.png" alt="R.SIGE" width="100%" border="0" /></div>



## 3. Importación de tablas

1.



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
| Avance **P3** | Esta actividad no requiere del desarrollo de elementos en el avance del proyecto final, los contenidos son evaluados en el quiz de conocimiento y habilidad.                                                                                                                                                                                                                                                                                        | 
| Avance **P3** | :compass:Mapa digital impreso _P3-1: xxxx_<br>Incluir xxxxx. Embebido dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                                                                                                                                          | 
| Avance **P3** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. | 

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Referencias

* https://desktop.arcgis.com/es/arcmap/latest/manage-data/geodatabases/what-is-a-geodatabase.htm


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