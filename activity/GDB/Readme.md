# Creación de base de datos geográfica del proyecto - GDB
Keywords: `geodatabase` `dataset` `relation` `table` `domain` `grid`

Cree una base de datos geográfica (file geodatabase) con grupos de capas o Datasets, e importe y reproyecte las capas y clases de entidad recopiladas y creadas en actividades anteriores.

<div align="center"><img src="graph/GDB.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Crear una base de datos geográfica para integrar la información espacial del caso de estudio.
* Importar y agrupar en datasets, las capas recopiladas y producidas en el caso de estudio.


## Requerimientos

* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos. 
* [:notebook:Lectura](https://desktop.arcgis.com/es/arcmap/latest/manage-data/geodatabases/what-is-a-geodatabase.htm): Información general de las bases de datos, ESRI.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.


## 1. Creación de estructura (geodatabase y datasets)

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _GDB_ y establezca el CRS 9377. En el árbol de catálogo, localice la carpeta `\file\data\gdb\`, de clic derecho sobre la raíz de esta carpeta y seleccione la opción _New / File Geodatabase_ y nombre la base de datos como `SIGE`. Al crear la base de datos, automáticamente se asignará la extensión _.gdb_.

> Como puede observar, en ArcGIS Pro se pueden crear dos tipos de bases geográficas: las _File Geodatabase_ son bases de datos corporativas que utilizan múltiples archivos y que pueden procesar grandes volúmenes de información; por otra parte, las _Mobile Geodatabase_ son bases compactas que utilizan un archivo principal único (y en algunos casos archivos complementarios de indexación) y aunque pueden almacenar gran cantidad de tablas y clases de entidad, su eficiencia no es óptima. 

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

</div>

> En la raíz de la base de datos geográfica _SIGE_, importaremos las tablas _Registro1_ y _Registro2_ que serán renombradas como _IGAC2009Registro1_ e _IGAC2009Registro2_.

<div align="center"><img src="graph/ArcGISPro_NewDataset.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_NewDataset1.png" alt="R.SIGE" width="100%" border="0" /></div>

Una vez terminada la creación de los diferentes datasets, podrá observar su estructura en el _Catalog Pane_.

<div align="center"><img src="graph/ArcGISPro_NewDataset2.png" alt="R.SIGE" width="50%" border="0" /></div>


## 2. Importación de entidades

Para la importación debe tener en cuenta, que dos elementos (feature class, tabla, grilla) dentro de una misma base geográfica, no pueden tener el mismo nombre.

1. En el árbol de catálogo, identifique de las fuentes de datos a utilizar, cuáles de ellas tienen capas con nombres idénticos, p. ej., la capa _BARRIOS_ se encuentra en `\file\data\POT\Anexo_Acuerdo_012_2013\gdb\25899.gdb\ENTIDADES_TERRITORIALES_Y_ADMINISTRATIVAS` y en `\file\data\POT\Anexo_Acuerdo_012_2013\shp\`. Para todos los elementos duplicados, modifique el nombre agregando el dígito 1 al final, p. ej., _BARRIOS1_
 
* Elementos con nombres idénticos: BARRIOS, COMUNAS, VEREDA, VIAS_PERIMETRO, VIAS_RURALES.
* Renombra en carpeta shp como: BARRIOS1, COMUNAS1, VEREDA1, VIAS_PERIMETRO1, VIAS_RURALES1.

<div align="center"><img src="graph/ArcGISPro_Rename.png" alt="R.SIGE" width="60%" border="0" /></div>

2. Desde el _Catalog Pane_ y dando clic derecho sobre el dataset _IGAC2013Cartografia_, seleccione la opción _Import / Feature Class(es)_ e importe desde la fuente `\file\data\POT\Anexo_Acuerdo_012_2013\gdb\25899.gdb\CARTOGRAFIA`, todas las clases de entidad. 

<div align="center"><img src="graph/ArcGISPro_ImportFeatureClass.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_ImportFeatureClass1.png" alt="R.SIGE" width="100%" border="0" /></div>

> En el evento que existan errores de importación por duplicidad de nombres, en la parte inferior del panel de importación y en una ventana emergente, aparecerá un mensaje de error indicando cuáles elementos no pudieron ser incorporados.

3. Para verificar que la importación se haya realizado correctamente, agregue algunas de las capas al mapa.

<div align="center"><img src="graph/ArcGISPro_AddLayer.png" alt="R.SIGE" width="100%" border="0" /></div>

4. Repita el procedimiento anterior importando a cada dataset, los datos correspondientes desde las fuentes identificadas.

<div align="center">IGAC2013EntidadTerritorialAdministrativa<br><img src="graph/ArcGISPro_ImportFeatureClass2.png" alt="R.SIGE" width="50%" border="0" /></div><br>

<div align="center">IGAC2013Rural<br><img src="graph/ArcGISPro_ImportFeatureClass3.png" alt="R.SIGE" width="50%" border="0" /></div><br>

<div align="center">IGAC2013Urbano<br><img src="graph/ArcGISPro_ImportFeatureClass4.png" alt="R.SIGE" width="50%" border="0" /></div><br>

<div align="center">POT2013Formulacion<br><img src="graph/ArcGISPro_ImportFeatureClass5.png" alt="R.SIGE" width="50%" border="0" /></div><br>

<div align="center">SIGE<br><img src="graph/ArcGISPro_ImportFeatureClass6.png" alt="R.SIGE" width="50%" border="0" /></div><br>

> Recuerde que al realizar la importación de clases de entidad dentro de la base de datos y los dataset creados, todas las capas serán re-proyectadas al CRS 9377.

Agregue una cada desde cada dataset y verifique que los vectores se hayan importado correctamente.

<div align="center"><img src="graph/ArcGISPro_AddLayer1.png" alt="R.SIGE" width="100%" border="0" /></div>

5. Durante el proceso de importación de las clases de entidad, es posible que se incorporen algunos de los _Dominios_ asociados a las propiedades de sus tablas. Para consultarlos, de clic derecho en la base de datos geográficas _SIGE_ y seleccione la opción _Domains_. 

<div align="center"><img src="graph/ArcGISPro_Domains.png" alt="R.SIGE" width="100%" border="0" /></div>


## 3. Importación de tablas

1. Desde el _Catalog Pane_ y dando clic derecho sobre la raíz de la base de datos geográfica _SIGE_, seleccione la opción _Import / Table(s)_ e importe desde la fuente `\file\data\POT\Anexo_Acuerdo_012_2013\gdb\25899.gdb\`, las tablas _Registro1_ y _Registro2_.

<div align="center"><img src="graph/ArcGISPro_ImportTable1.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_ImportTable2.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Renombre las tablas como _IGAC2009Registro1_ e _IGAC2009Registro2_, agréguelas a la tabla de contenido y verifique que se encuentren los registros.

<div align="center"><img src="graph/ArcGISPro_ImportTable3.png" alt="R.SIGE" width="100%" border="0" /></div>


## 4. Análisis usando software libre - QGIS

Para el desarrollo de las actividades desarrolladas en esta clase, se pueden utilizar en QGIS las siguientes herramientas o geo-procesos:

| Proceso                                          | Procedimiento                                                                                                                                  |
|:-------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| Crear geodatabases (GDB) y datasets              | Directamente desde el panel _Browser_ y dando clic sobre un directorio, se pueden crear con la opción ESRI File Geodatabase.                   |
| Importación de entidades a una geodatabase (GDB) | Desde el panel _Layers_ y dando clic en _Export / Save Features As_, podrá exportar la capa dentro de una base de datos ESRI File Geodatabase. |

Ejemplo rótulo en QGIS: `'A(ha): ' ||  round("AGha", 2) || '\n' || 'P (m): ' ||  round("PGm", 2) `

[:notebook:QGIS training manual](https://docs.qgis.org/3.34/en/docs/training_manual/)  
[:notebook:Herramientas comúnmente utilizadas en QGIS](../QGIS.md)


## Elementos requeridos en diccionario de datos

Agregue a la tabla resúmen generada en la actividad [Inventario de información geo-espacial recopilada del POT y diccionario de datos](../POTLayer/Readme.md), las capas generadas en esta actividad que se encuentran listadas a continuación:

| Nombre            | Descripción                                                                                                                                                                                                      | Geometría   | Registros | 
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-----------| 
| Clases de entidad | No es necesario volver a incorporar en la tabla resumen y en el diccionario de datos, las clases de entidad y tablas importadas en la GDB debido a que ya se incorporaron y documentaron en entregas anteriores. | N/A         | N/A       | 

> :bulb:Para funcionarios que se encuentran ensamblando el SIG de su municipio, se recomienda incluir y documentar estas capas en el Diccionario de Datos.


## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad     | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P3** | Siguiendo el procedimiento descrito en esta actividad, cree una base de datos geográfica con diferentes dataset temáticos, e importe todas las clases de entidad y tablas recopiladas y producidas en actividades anteriores. Incluya capturas de pantalla detalladas de cada dataset con las clases de entidad y los dominios importados.                                                                                                                                                                                                                      | 
| Avance **P3** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. | 

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Referencias

* https://desktop.arcgis.com/es/arcmap/latest/manage-data/geodatabases/what-is-a-geodatabase.htm


## Control de versiones

| Versión    | Descripción                                                 | Autor                                      | Horas |
|------------|:------------------------------------------------------------|--------------------------------------------|:-----:|
| 2024.03.19 | Versión inicial con alcance de la actividad                 | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.06.24 | Investigación y documentación para caso de estudio general  | [rcfdtools](https://github.com/rcfdtools)  |   5   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../CNEStation/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/23) | [Siguiente :arrow_forward:]() |
|------------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------|-------------------------------|

[^1]: 