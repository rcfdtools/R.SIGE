# Análisis de sub-zonas hidrográficas
Keywords: `colombia` `ideam` `hyfrologic-area` `station` `feature-envelope-to-polygon` `bounding-box`

A partir de la capa de zonificación hidrográfica de Colombia del IDEAM, seleccione y obtenga a partir del límite municipal, las subzonas hidrográficas con cubrimiento en la zona de estudio, exporte las sub-zonas identificadas, evalúe si las zub-zonas obtenidas permiten definir las subcuencas de los ríos principales identificados en el POT del municipio.

<div align="center"><img src="graph/SZH.png" alt="R.SIGE" width="100%" border="0" /></div>

> En la ilustración, _COD_ZH_ corresponde al código de la Zona Hidrográfica.


## Objetivos

* Estudiar la estructura general de la zonificación hidrográfica de Colombia.
* Crear una capa geográfica que delimite la zona geográfica de estudio.
* Crear el polígono regular del dominio espacial que envuelve la zona de estudio.
* Calcular el área y perímetro de la zona de estudio y su dominio espacial.

> El polígono regular permitirá en las siguientes actividades del curso, realizar la descarga de información satelital y seleccionar las estaciones hidroclimatológicas de la zona de estudio. 


## Requerimientos

* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.


## 1. Zonificación hidrográfica de Colombia

La zonificación hidrográfica de Colombia desde el punto de vista hidrológico, tiene sus inicios en el HIMAT mediante la Resolución 0337 del 1978, la cual establece que el país está conformado por cinco Áreas hidrográficas (1-Caribe, 2- Magdalena - Cauca, 3- Orinoco, 4- Amazonas y 5-Pacífico) que a su vez están divididas en Zonas Hidrográficas y subdivididas en Subzonas Hidrográficas. En ese entonces, el propósito de la zonificación fue de adoptar un sistema de codificación para estaciones Hidrometerológicas. Posteriormente, el IDEAM introduce esta zonificación para otros fines, tales como estudios y análisis hidrológicos relacionados con los informes ambientales, p. ej. el Índice de Aridez, el Escurrimiento y el Rendimiento Hídrico.[^1]

La zonificación de cuencas hidrográficas corresponde a tres niveles de jerarquía: áreas, zonas y subzonas hidrográficas. Las áreas hidrográficas corresponden a las regiones hidrográficas o vertientes que, en sentido estricto, son las grandes cuencas que agrupan un conjunto de ríos con sus afluentes que desembocan en un mismo mar. Ahora bien, en Colombia se distinguen cuatro vertientes, dos de ellas asociadas a ríos de importancia continental (vertiente del Orinoco y vertiente del Amazonas) y las vertientes del Atlántico y del Pacífico. Se delimita adicionalmente como áea hidrográfica la cuenca Magdalena-Cauca, que aunque tributa y forma parte de la vertiente del Atlántico, tiene importancia socioeconómica por su alto poblamiento y aporte al producto interno bruto.[^2]

<div align="center">

| AH  | Área Hidrográfica |
|-----|-------------------|
| 1   | Caribe            |
| 2   | Magdalena-Cauca   |
| 3   | Orinoco           |
| 4   | Amazonas          |
| 5   | Pacífico          |

</div>

<div align="center"><img src="graph/ZonaHidrografica2013.png" alt="R.SIGE" width="100%" border="0" /></div>

Las cuencas hidrográficas que entregan o desembocan sus aguas superficiales directamente de una área hidrográfica se denominaran zonas hidrográficas. Agrupan varias cuencas que se presentan como un subsistema hídrico con características de relieve y drenaje homogéneo y sus aguas tributan a través de un afluente principal hacia un área hidrográfica. Están integradas por cuencas de las partes altas, medias o bajas de una zona hidrográfica que captan agua y sedimentos de los tributarios de diferente orden tales como nacimientos de agua, arroyos, quebradas y ríos. Las cuencas que tributan sus aguas a su vez a las zonas hidrográficas se denomina subzonas hidrográficas. Ahora bien, respecto a la toponimia con que se identifican zonas y subzonas hidrográficas, a estas unidades se les asignó la toponimia de acuerdo con el nombre de la corriente más representativa o río principal o con el nombre heredado de la zonificación del HIMAT, que puede corresponder al espacio geográfico o región a la cual drenan las aguas superficiales.[^2]

<div align="center">

| AH  | Área Hidrográfica | ZH  | Zona Hidrográfica                  |
|-----|-------------------|-----|------------------------------------|
| 1   | Caribe            | 11  | Atrato - Darién                    |
| 1   | Caribe            | 12  | Caribe - Litoral                   |
| 1   | Caribe            | 13  | Sinú                               |
| 1   | Caribe            | 15  | Caribe - La Guajira                |
| 1   | Caribe            | 16  | Catatumbo                          |
| 1   | Caribe            | 17  | Islas del Caribe                   |
| 2   | Magdalena - Cauca | 21  | Alto Magdalena                     |
| 2   | Magdalena - Cauca | 22  | Saldaña                            |
| 2   | Magdalena - Cauca | 23  | Medio Magdalena                    |
| 2   | Magdalena - Cauca | 24  | Sogamoso                           |
| 2   | Magdalena - Cauca | 25  | Bajo Magdalena - Cauca - San Jorge |
| 2   | Magdalena - Cauca | 26  | Cauca                              |
| 2   | Magdalena - Cauca | 27  | Nechí                              |
| 2   | Magdalena - Cauca | 28  | Cesar                              |
| 2   | Magdalena - Cauca | 29  | Bajo Magdalena                     |
| 3   | Orinoco           | 31  | Inírida                            |
| 3   | Orinoco           | 32  | Guaviare                           |
| 3   | Orinoco           | 33  | Vichada                            |
| 3   | Orinoco           | 34  | Tomo                               |
| 3   | Orinoco           | 35  | Meta                               |
| 3   | Orinoco           | 36  | Casanare                           |
| 3   | Orinoco           | 37  | Arauca                             |
| 3   | Orinoco           | 38  | Orinoco Directos                   |
| 3   | Orinoco           | 39  | Apure                              |
| 4   | Amazonas          | 41  | Guainía                            |
| 4   | Amazonas          | 42  | Vaupés                             |
| 4   | Amazonas          | 43  | Apaporis                           |
| 4   | Amazonas          | 44  | Caquetá                            |
| 4   | Amazonas          | 45  | Yarí                               |
| 4   | Amazonas          | 46  | Caguán                             |
| 4   | Amazonas          | 47  | Putumayo                           |
| 4   | Amazonas          | 48  | Amazonas - Directos                |
| 4   | Amazonas          | 49  | Napo                               |
| 5   | Pacífico          | 51  | Mira                               |
| 5   | Pacífico          | 52  | Patía                              |
| 5   | Pacífico          | 53  | Tapaje - Dagua - Directos          |
| 5   | Pacífico          | 54  | San Juan                           |
| 5   | Pacífico          | 55  | Baudó - Directos Pacífico          |
| 5   | Pacífico          | 56  | Pacífico - Directos                |
| 5   | Pacífico          | 57  | Islas del Pacífico                 |

</div>

> En el presente análisis no se han incluido resultados para la ZH - zona hidrográfica 57, correspondiente a las Islas del Pacífico, debido a que la capa geográfica SZH - subzonas hidrográficas no contiene el polígono de delimitación. 


## 2. Obtención e identificación de subzonas hidrográficas

El proceso de delimitación se realiza a partir de la cobertura de Subzonas hidrográficas de Colombia, este mapa representa las unidades de análisis para el ordenamiento ambiental de territorio definidas por el IDEAM en convenio con el Instituto Geográfico Agustín Codazzi (IGAC), a escala 1:500.000. [^3]

1. Ingrese al portal https://www.colombiaenmapas.gov.co/, en el cuadro de búsqueda escriba _Zonificación Hidrográfica_ y realice la descarga del archivo de formas Shapefile correspondiente al año 2013. Guarde y descomprima el archivo obtenido en la carpeta `\file\data\IDEAM\`.

> La descarga permite obtener un archivo comprimido que contiene la capa geográfica en formato Shapefile, un mapa de muestra en formato .pdf, un mapa en formato .pdf y otros elementos complementarios.

<div align="center"><img src="graph/ColombiaMapasDescarga.png" alt="R.SIGE" width="100%" border="0" /></div>

Catálogo de objetos en Subzonas [^4]  

| Nombre       | Alias          | Definición                                                                   | Tipo de dato |
|--------------|----------------|------------------------------------------------------------------------------|--------------|
| OBJECTID     | OBJECTID       | Identificador de objeto geográfico.                                          | Texto        |
| Shape        | Shape          | Tipo de geometría.                                                           | Geometría    |
| COD_AH       | Código Area    | Código del Area hidrográfica a la que corresponde.                           | Entero       |
| COD_ZH       | Código Zona    | Código de la Zona hidrográfica a la que corresponde.                         | Entero       |
| COD_SZH      | Código Subzona | Código de Subzona hidrográfica a la que corresponde.                         | Entero       |
| NOM_AH       | Nombre Área    | Nombre del área hidrográfica a la que corresponde. Dominio Área Hidográfica. | Texto        |
| NOM_ZH       | Nombre Zona    | Nombre de la zona hidrográfica a la que corresponde.                         | Texto        |
| NOM_SZH      | Nombre Subzona | Nombre de la Subzona hidrográfica a la que corresponde.                      | Texto        |
| Shape_Length | Shape_Length   | Perímetro en las unidades del sistema de referencia espacial.                | Entero       |
| Shape_Area   | Shape_Area     | Área en las unidades del sistema de referencia espacial.                     | Entero       |
| RULEID       | RULEID         | Id único asignado por el sistema a la representación gráfica.                | Entero       |
| Override     | Override       | Representación gráfica.                                                      | Blob         |

2. En ArcGIS Pro, cree un proyecto nuevo en blanco en la ruta _D:\R.LTWB\\.map_ y nómbrelo como ArcGISPro o ArcGISProSection01. Automáticamente, serán generados el mapa de proyecto, la base de datos geográfica en formato .gdb, la carpeta para volcado de informes de registro de importación _ImportLog_ y la carpeta _Index_. Utilizando el Panel de catálogo y desde la sección _Folders_, realice la conexión a la carpeta _D:\R.LTWB_.

![R.LTWB](Screenshot/ArcGISPro3.0.0NewMapProject.png)

Agregue la capa de Subzonas Hidrográficas y simbolice por categorías de valores únicos o _Unique Values_ a partir del campo `NOM_ZH` correspondiente a la Zona Hidrográfica y rotule las zonas a partir del campo de atributos `COD_SZH` correspondiente a los códigos de las subzonas.

![R.LTWB](Screenshot/ArcGISPro3.0.0ZonaHidrografica2013.png)

Para el filtrado, desde las propiedades de la capa seleccione la pestaña _Definition Query_ y ensamble la expresión de filtrado o ingrese la instrucción SQL `COD_ZH = 28`.

![R.LTWB](Screenshot/ArcGISPro3.0.0ZonaHidrografica2013Query.png)

La disolución de los polígonos para la creación de la zona de estudio se realiza desde el panel de herramientas _Geoprocessing - Data Management Tools - Generalization - Dissolve_ que puede ser lanzado desde el menú _Analysis_ seleccionando la opción _Tools_.

![R.LTWB](Screenshot/ArcGISPro3.0.0ZonaHidrografica2013Dissolve.png)

Para cambiar el sistema de proyección de coordenadas, en las propiedades del mapa _Map_ de la tabla de contenidos _Contents_, seleccione la pestaña _Coordinate Systems_ y en la caja de búsqueda ingrese 103599, correspondiente a MAGNA-SIRGAS CMT12.

![R.LTWB](Screenshot/ArcGISPro3.0.0CRS103599.png)

Para la creación de campos de atributo, abra la tabla de atributos y de clic en la opción Add, agregue los campos Akm2, Pkm y ZH.

![R.LTWB](Screenshot/ArcGISPro3.0.0ZonaEstudioAddField.png)

Calcule la geometría de los campos numéricos y asigne el nombre de la zona en el campo ZH utilizando el texto 'ZH 2 - Cesar' sobre Python 3 como _Expression Type_.

![R.LTWB](Screenshot/ArcGISPro3.0.0ZonaEstudioCalculateGeometry.png)

Para la rotulación compuesta, utilice cualquiera de las siguientes instrucciones:

* Parser VBScript: `[ZH] &VbNewLine& "Área, km²: " & round( [Akm2], 2) &VbNewLine& "Perímetro, km: " & round( [Pkm], 2)`
* Parser Python: `[ZH] + "\nArea, km2: " +  [Akm2]  + "\nPerimetro, km: " + [Pkm]`
* Parser Arcade: `$feature.ZH + '\nÁrea, km²: ' + Round($feature.Akm2, 2) + '\nPerímetro, km: : ' + Round($feature.Pkm, 2)`

![R.LTWB](Screenshot/ArcGISPro3.0.0ZonaEstudioLabelArcade.png)

Utilizando la herramienta _Data Management Tools / Features / Feature Envelope to Polygon_, cree el polígono regular envolvente de la zona de estudio. 

![R.LTWB](Screenshot/ArcGISPro3.0.0ZonaEstudioEnvelope.png)


#### Instrucciones en QGIS (3.26.0)

Cree un mapa de proyecto, agregue la capa [Zonificacion_hidrografica_2013.shp](../../.shp/Zonificacion_Hidrografica_2013.zip) y guarde en la carpeta _.map_ como _R.LTWB.qgz_

El filtrado de entidades se realiza a través de la ventana de propiedades de la capa desde la pestaña _Source_ y el _Query Builder_.

![R.LTWB](Screenshot/QGIS3.26.0ZonaHidrografica2013Query.png)

El proceso de disolución se realiza utilizando la herramienta _Vector geometry - Dissolve_ del _Processing Toolbox_ que se carga oprimiendo la combinación de teclas <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> o desde la barra de menús _Processing_.

![R.LTWB](Screenshot/QGIS3.26.0ZonaHidrografica2013Dissolve.png)

Para cambiar el sistema de proyección, oprima la combinación de teclas <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> para acceder a la ventana de propiedades del proyecto y en la ventana _CRS_, ingrese en la casilla de filtro o búsqueda el valor 9377, correspondiente al sistema de referencia de coordenadas MAGNA-SIRGAS / Origen-Nacional. Seleccione y de clic en _Apply_ y _Ok_. En la parte inferior derecha de QGIS, podrá observar el sistema asignado como _EPSG: 9377_.

![R.LTWB](Screenshot/QGIS3.26.0CRS9377.png)

Nuevos campos de atributos pueden ser creados directamente desde las opciones del _Field Calculator_, p. ej. para el cálculo del área en km² se crea el campo Akm2 y se calcula la geometría con la expresión `$area / (1000*1000)`. Para el perímetro utilizar la expresión `$perimeter / 1000`.

![R.LTWB](Screenshot/QGIS3.26.0ZonaEstudioAddField.png)

La rotulación compuesta indicando la zona, área y perímetro se realiza con la siguiente expresión: `concat("ZH",  '\nÁrea, km²: ', round("Akm2",2), '\nPerímetro, km: ', round("Pkm", 2))`

![R.LTWB](Screenshot/QGIS3.26.0ZonaEstudioLabel.png)

El proceso de obtención del polígono perimetral se realiza con la herramienta _Vector geometry - Bounding boxes_ del _Processing Toolbox_ que se carga oprimiendo la combinación de teclas <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> o desde la barra de menús _Processing_.

![R.LTWB](Screenshot/QGIS3.26.0ZonaEstudioBoundingBoxes.png)


Ahora dispone de un polígono que podrá utilizar como máscara de selección para la obtención de información satelital o para la selección de estaciones dentro de la zona de estudio.



### Referencias

* https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/feature-envelope-to-polygon.htm
* https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/h-how-dissolve-data-management-works.htm
* https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/calculate-field.htm
* https://docs.qgis.org/2.18/en/docs/user_manual/processing_algs/qgis/vector_geometry_tools.html
* [PyCharm no sincroniza mis cambios en la nube - Archivos grandes rechazados en _Commit and Push_](https://github.com/rcfdtools/R.LTWB/discussions/40):lady_beetle:


### Control de versiones

| Versión    | Descripción                                                                                          | Autor                                      | Horas |
|------------|:-----------------------------------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2023.01.25 | Guión, audio, video, edición y publicación.                                                          | [rcfdtools](https://github.com/rcfdtools)  |   2   |
| 2022.08.11 | Inclusión de actividades complementarias.                                                            | [rcfdtools](https://github.com/rcfdtools)  |  0.5  |
| 2022.07.20 | Inclusión de diagrama de procesos.                                                                   | [rcfdtools](https://github.com/rcfdtools)  |  0.5  |
| 2022.07.09 | Inclusión de procedimiento para delimitación de la zona de estudio usando ArcGIS Pro.                | [rcfdtools](https://github.com/rcfdtools)  |   2   |
| 2022.07.08 | Inclusión de procedimiento para delimitación de la zona de estudio usando ArcGIS for Desktop y QGIS. | [rcfdtools](https://github.com/rcfdtools)  |  2.5  | 
| 2022.07.06 | Versión inicial con definición general del caso de estudio y mapas de referencia.                    | [rcfdtools](https://github.com/rcfdtools)  |   4   |


##

_R.LTWB es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](https://github.com/rcfdtools/R.LTWB/wiki/License)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [Anterior](../Requirement) | [:house: Inicio](../../Readme.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.LTWB/discussions/2) | [Siguiente](../../Section02) |
|----------------------------|-----------------------------------|----------------------------------------------------------------------------------|------------------------------|

[^1]: http://www.ideam.gov.co/web/agua/zonificacion-hidrografica
[^2]: http://documentacion.ideam.gov.co/openbiblio/bvirtual/022655/MEMORIASMAPAZONIFICACIONHIDROGRAFICA.pdf
[^3]: http://geoservicios.ideam.gov.co/geonetwork/srv/eng/catalog.search#/metadata/7696695f-ae9c-4780-a6d0-d3cd1808819a
[^4]: http://geoservicios.ideam.gov.co/CatalogoObjetos/queryByUUID?uuid=bcd645c9-0f11-4770-926e-1e1fdfbf5ce6

<div align="center"><a href="https://enlace-academico.escuelaing.edu.co/psc/FORMULARIO/EMPLOYEE/SA/c/EC_LOCALIZACION_RE.LC_FRM_ADMEDCO_FL.GBL" target="_blank"><img src="https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/CaseUse/.icons/IconCEHBotonCertificado.png" alt="R.LTWB" width="260" border="0" /></a></div>


##

<div align="center"><a href="http://www.escuelaing.edu.co" target="_blank"><img src="https://github.com/rcfdtools/R.TeachingResearchGuide/blob/main/CaseUse/.icons/Banner1.svg" alt="Support by" width="100%" border="0" /></a><sub><br>Este curso guía ha sido desarrollado con el apoyo de la Escuela Colombiana de Ingeniería - Julio Garavito. Encuentra más contenidos en https://github.com/uescuelaing</sub><br><br></div>