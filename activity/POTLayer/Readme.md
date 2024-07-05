# Inventario de información geo-espacial recopilada 
Keywords: `DEM` `AgreeDEM`

En esta actividad se presenta una tabla resumen de la información geo-espacial (vectorial, ráster) y tablas anexas al POT.

<div align="center"><img src="graph/Gravity_anomalies_on_Earth.png" alt="R.SIGE" width="50%" border="0" /><sub><br>Tomado de: <a href="Public Domain, https://commons.wikimedia.org/w/index.php?curid=479365">https://commons.wikimedia.org</a></sub><br><br></div>


## Objetivos

* 


## Requerimientos

* [:open_file_folder:POT_Layer.xlsx](PoblacionDANE.xlsx): libro para registro de capas y grillas recopiladas del POT.
* [:toolbox:Herramienta](https://www.microsoft.com/es/microsoft-365/excel?market=bz): Microsoft Excel 365.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ArcGIS Pro de ESRI
* [:toolbox:Herramienta](https://qgis.org/): QGIS
* Datos recopilados


## 1. Especificaciones para revisión

En el libro de Microsoft Excel suministrado para el desarrollo de esta actividad, se registran los siguientes atributos:

| Columna              | Alcance de evaluación                                                                                                                                                                 |
|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Etapa                | Diagnóstico, Formulación, Implementación, Evaluación y seguimiento.                                                                                                                   |
| Tipo                 | Vector, Tabla, Ráster.                                                                                                                                                                |
| Dataset              | Nombre de GDB / Nombre del grupo de capas. Para archivos que no estén contenidos dentro de una GDB indicar el nombre de la carpeta que contiene el elemento.                          |
| Nombre               | Nombre del elemento. Para archivos que no estén contenidos dentro de una GDB incluir la extensión primaria, p. ej.: .shp, .tif, .dbf, dwg.                                            |
| Descripción          | Evalúe la espacialidad de la capa y sus atributos para identificar que contiene y representa.                                                                                         |
| Alias                | Nombre corto utilizado en listas de elementos sobre mapas. En caso de que no disponga de nombre corto, incluir el Nombre sin extensión.                                               |
| Geometría            | Punto 2D, Punto 3D, Línea 2D, Línea 3D, Polígono 2D, Polígono 3D, N/A o no aplica. Grillas ráster y tablas de datos no contienen geometría.                                           |
| Registros            | Total de entidades contenidas dentro de la tabla de atributos. Para grillas incluir en una fórmula el resultado obtenido de multiplicae el número de filas por el número de columnas. |
| Ruta local           | Ubicación local de la capa en disco local.                                                                                                                                            |
| Fuente de datos      | Fuente de datos original de la capa.                                                                                                                                                  |
| CRS                  | Sistema de proyección de coordenadas                                                                                                                                                  |
| Límite norte         | Extensión espacial al norte en metros o en grados decimales. Depende del sistema de coordenadas utilizado.                                                                            |
| Límite sur           | Extensión espacial al sur en metros o en grados decimales. Depende del sistema de coordenadas utilizado.                                                                              |
| Límite este          | Extensión espacial al este en metros o en grados decimales. Depende del sistema de coordenadas utilizado.                                                                             |
| Límite oeste         | Extensión espacial al oeste en metros o en grados decimales. Depende del sistema de coordenadas utilizado.                                                                            |                                                                                                                                               |
| Área envolvente (ha) | Tamaño del área envolvente en hectáreas `A = (Norte-Sur) * (Oeste-Este) / 10000`                                                                                                      |
| Observaciones        | Observaciones relacionadas con el contenido y su visualización.                                                                                                                       |


## 2. Descarga de información

Información geo-espacial del Plan de Ordenamiento Territorial Municipio de Zipaquirá, Acuerdo 012 de 2013 disponibles.

1. Ingrese a www.colombiaot.gov.co y de clic en la opción _Los POT del País_

<div align="center"><img src="graph/ColombiaOT_1.png" alt="R.SIGE" width="100%" border="0"/></div>

2. En el buscador de Colombia OT, realizar los siguientes filtros:

* Filtra por entidad territorial: Zipaquirá 
* Forma de representación: Cartografía
* Tipo: Dato

Luego, desde su navegador busque los resultados cuyo formato sea .zip y descargue estos archivos.

<div align="center"><img src="graph/ColombiaOT_2.png" alt="R.SIGE" width="100%" border="0"/></div>

<div align="center">

Listado de archivos obtenidos

| Archivo                                                                                                                                     | Formato   | Tamaño (KB) | 
|:--------------------------------------------------------------------------------------------------------------------------------------------|:----------|:------------|
| [:floppy_disk:Barrios.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Barrios.zip)                                                      | Shapefile | 19          |
| [:floppy_disk:Comunas.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Comunas.zip])                                                     | Shapefile | 7           |
| [:floppy_disk:Expansion_Urbana_Ajustada_Predios.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Expansion_Urbana_Ajustada_Predios.zip ) | Shapefile | 10          |
| [:floppy_disk:Hidrografia.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Hidrografia.zip)                                              | Shapefile | 263         |
| [:floppy_disk:ModeloOrdenamientoTerritorial.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/ModeloOrdenamientoTerritorial.zip)          | Shapefile | 1031        |
| [:floppy_disk:Orden_Vial.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Orden_Vial.zip)                                                | Shapefile | 184         |
| [:floppy_disk:Rio_Bogota.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Rio_Bogota.zip)                                                | Shapefile | 52          |
| [:floppy_disk:Vereda.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Vereda.zip)                                                        | Shapefile | 535         |
| [:floppy_disk:Vias.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Vias.zip)                                                            | Shapefile | 3           |
| [:floppy_disk:Vias_Perimetro.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Vias_Perimetro.zip)                                        | Shapefile | 64          |
| [:floppy_disk:Vias_Perimetro_Urbano.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Vias_Perimetro_Urbano.zip)                          | Shapefile | 77          |
| [:floppy_disk:Vias_Rurales.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Vias_Rurales.zip)                                            | Shapefile | 184         |
| [:floppy_disk:Vias_Urbanas.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Vias_Urbanas.zip)                                            | Shapefile | 73          |
| [:floppy_disk:Zona_Urbana_Ajustada_Predios.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/Zona_Urbana_Ajustada_Predios.zip)            | Shapefile | 29          |
| [:floppy_disk:25899.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/25899.zip)                                                          | mdb       | 57464       |
| [:floppy_disk:25899.gdb.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/shp/25899.gdb.zip)                                                  | gdb       | 57464       |

</div>

> Renombre los archivos comprimidos con los nombres indicados en la tabla anterior. Se ha incluído en la lista la base de datos convertida a formato `.gdb`. 

3. En su repositorio de proyecto y dentro de la carpeta `\file\data\POT\Anexo_Acuerdo_012_2013\shp\`, guarde y descomprima los archivos vectoriales en formato Shapefile.

<div align="center"><img src="graph/Data_POT_shp.png" alt="R.SIGE" width="100%" border="0"/></div>

4. En su repositorio de proyecto y dentro de la carpeta `\file\data\POT\Anexo_Acuerdo_012_2013\gdb\`, guarde y descomprima la base de datos _25899.zip_ en formato Microsoft Database `.mdb`.

> Debido a que ArcGIS Pro no permite la apertura directa de archivos de bases de datos en formato `.mdb`, se ha convertido a formato `.gdb`. La conversión fue realizada desde la herramienta ArcGIS for Desktop creando una base de datos en blanco, un dataset con el CRS de una de las capas y luego importando las diferentes clases de entidad contenidas en la base `.mdb`.

<div align="center"><img src="graph/Data_POT_gdb.png" alt="R.SIGE" width="100%" border="0"/></div>


## 3. Visualización y consulta de propiedades en ArcGIS Pro

Para la visualización preliminar y consulta de los datos geo-espaciales descargados y descomprimidos, siga este procedimiento:

1. En ArcGIS Pro, cree un proyecto nuevo en blanco con el nombre `ArcGISPro` y guarde dentro de la carpeta `\file\map`.

<div align="center"><img src="graph/ArcGISPro_NewMap.png" alt="R.SIGE" width="100%" border="0"/></div>

2. En el menú _View_, de clic en el botón _Catalog Pane_ que activará el panel lateral derecho de su catálogo de datos. De clic derecho en la carpeta _Folders_, seleccione la opción _Add Folder Connection_ y seleccione su directorio de proyecto.

> Para ejemplificar este curso, la carpeta de proyecto es `C:\R.SIGUE`.

<div align="center"><img src="graph/ArcGISPro_AddFolderConnection.png" alt="R.SIGE" width="100%" border="0"/></div>

3. Expanda el árbol de _Folders_, podrá observar que se encuentran dos carpetas asociadas. La carpeta `ArcGISPro` corresponde a la carpeta por defecto que se genera al crear un proyecto nuevo en ArcGIS Pro, y la carpeta _R.SIGUE_ es la carpeta general del proyecto.

<div align="center"><img src="graph/ArcGISPro_Folders.png" alt="R.SIGE" width="100%" border="0"/></div>

4. En _R.SIGUE_, expanda el arból de la carpeta _file_ hasta el subnivel `\data\POT\`, la carpeta del Acuerdo y las subcarpetas _shp_ y _gdb_. Podrá observar que se encuentran las diferentes capas descomprimidas y la base de datos. De clic derecho en la capa _BARRIOS.shp_ y seleccione la opción _Properties_.

<div align="center"><img src="graph/ArcGISPro_LayerProperties.png" alt="R.SIGE" width="100%" border="0"/></div>

En las propiedades de la capa podrá observar los siguientes contenidos:

* Source \ Data Source: fuente de datos y geometría.
* Source \ Extent: extensión espacial de la capa (top, bottom, left, right) en función del CRS de la capa.
* Source \ Spatial Reference: sistema de proyección de coordenadas - CRS. 
* Source \ Domain, Resolution and Tolerance: extensión máxima del dominio de proyección, resolución y tolerancias geométricas. 
* Indexes \ Attribute Index: campos de atributos indexados.  
* Indexes \ Spatial Index:  indice o llave espacial geométrica.

A través del clic derecho sobre el nombre de la capa, también podrá obtener la vista de metadatos que contiene la información detallada de la fuente de datos y sus autores si esta ha sido editada e incluída en un archivo `.xml`. 

<div align="center"><img src="graph/ArcGISPro_LayerMetadata.png" alt="R.SIGE" width="80%" border="0"/></div>

> Como observa, en ninguna de las propiedades anteriores podrá conocer el número de registros o entidades asociadas a cada capa.

5. Agregue la capa de Barrios, arrastrándola desde el _Catalog Pane_ al mapa, o a la tabla de contenido localizada a la izquierda y visualice las entidades contenidas. Para consultar la tabla de atributos, de clic derecho en la capa desde la tabla de contenido y seleccione la opción _Attribute Table_. En la parte inferior de la tabla podrá observar el total de registro o vectores contenidos en la capa. Seleccione en la tabla de atributos la capa y utilizando el rotulador de entidades disponible en el menú _Labeling_, rotule las entidades utilizando alguno de los atributos principales de la capa. Acceda a la simbología de la capa dando clic derecho en la tabla de contenido, remueva el relleno en polígonos y establezca los contornos de entidades en color negro.

<div align="center"><img src="graph/ArcGISPro_LayerViewTable.png" alt="R.SIGE" width="100%" border="0"/></div>

6. Para cada uno de los archivos Shapefile y de las Clases de Entidad contenidas en la base de datos `gdb`, consulte sus propiedades y registre los datos obtenidos en el Libro de revisión _POT_Layer.xlsx_.


### 3.1. Capas y tablas utilizadas en diagnóstico

Propiedades comúnes:

* Data source: file\data\POT\Anexo_Acuerdo_012_2013\gdb\25899.gdb
* CRS: EPSG 3116 o MAGNA Origen Bogota Colombia, 2011.
* Fuente de datos: sin metadatos disponibles para verificación de fuentes originales de datos.
* Alias: igual al nombre de la capa, sin metadatos para asociación de alias.

Dataset, geometría y registros

| Dataset                                     | Nombre                            | Descripción                                                                                                                                                          | Geometría   | Registros | 
|---------------------------------------------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-----------| 
| CARTOGRAFIA                                 | ANDENES                           | Andenes zona urbana y centros poblados rurales próximos al área urbana                                                                                               | Línea 2D    | 766       | 
| CARTOGRAFIA                                 | ANDENES_CPR                       | Andenes en centros poblados rurales próximos al área urbana                                                                                                          | Línea 2D    | 162       | 
| CARTOGRAFIA                                 | ANDENES_PERIMETRO                 | Andenes en zona urbana central                                                                                                                                       | Línea 2D    | 604       | 
| CARTOGRAFIA                                 | ANOTACION                         | Puntos de interés rural                                                                                                                                              | Punto 2D    | 1851      | 
| CARTOGRAFIA                                 | ANOTACION_URBANO                  | Puntos de interés urbano                                                                                                                                             | Punto 2D    | 158       | 
| CARTOGRAFIA                                 | CURVAS_NIVEL                      | Curvas de nivel, principales cada 200 metros y secundarias cada 50 metros.                                                                                           | Línea 2D    | 149       | 
| CARTOGRAFIA                                 | EDIFICACION_RURAL                 | Nodos de localización de edificaciones en la zona rural                                                                                                              | Punto 2D    | 1828      | 
| CARTOGRAFIA                                 | EDUCATIVO                         | Nodos de localización de centros educativos                                                                                                                          | Punto 2D    | 74        | 
| CARTOGRAFIA                                 | HIDROGRAFIA                       | Red hidrográfica                                                                                                                                                     | Línea 2D    | 305       | 
| CARTOGRAFIA                                 | HIDROGRAFIA_Buffer                | Rondas hídricas con aferencia de 30 metros a cada lado de las líneas de la red hidrográfica                                                                          | Polígono 2D | 305       | 
| CARTOGRAFIA                                 | HIDROGRAFIA_Buffer1               | Rondas hídricas con aferencia de 30 metros a cada lado de las líneas de la red hidrográfica y para tramo de drenaje mayoritariamente dentro del límite del municipio | Polígono 2D | 264       | 
| CARTOGRAFIA                                 | LIM_NBR                           | Núcleo básico rural - Límites de vías y predios                                                                                                                      | Polígono 2D | 146       | 
| CARTOGRAFIA                                 | RONDAS                            | Rondas hídricas                                                                                                                                                      | Polígono 2D | 5         | 
| CARTOGRAFIA                                 | VIAS_CPR                          | Vías interconectoras desce el centro urbano y hacias centros poblados rurales - CPR                                                                                  | Línea 2D    | 200       | 
| CARTOGRAFIA                                 | VIAS_PERIMETRO                    | Vías perímetro urbano principal                                                                                                                                      | Línea 2D    | 604       | 
| CARTOGRAFIA                                 | VIAS_RURALES                      | Vías rurales                                                                                                                                                         | Línea 2D    | 774       | 
| CARTOGRAFIA                                 | VIAS_URBANAS                      | Vías urbanas                                                                                                                                                         | Línea 2D    | 784       | 
| CARTOGRAFIA                                 | VIAS_URBANAS_Buffer               | Aferencia en vías urbanas a 20 metros y solo en 1 costado                                                                                                            | Polígono 2D | 784       | 
| ENTIDADES _TERRITORIALES _Y_ADMINISTRATIVAS | BARRIOS                           | Barrios zona urbana                                                                                                                                                  | Polígono 2D | 49        | 
| ENTIDADES _TERRITORIALES _Y_ADMINISTRATIVAS | Centrospobladosrurales            | Predios en centros poblados rurales                                                                                                                                  | Polígono 2D | 3615      | 
| ENTIDADES _TERRITORIALES _Y_ADMINISTRATIVAS | COMUNAS                           | Comunas urbanas                                                                                                                                                      | Polígono 2D | 4         | 
| ENTIDADES _TERRITORIALES _Y_ADMINISTRATIVAS | NBR                               | Núcleo básico rural - Predios                                                                                                                                        | Polígono 2D | 282       | 
| ENTIDADES _TERRITORIALES _Y_ADMINISTRATIVAS | NucleosBasicosRurales             | Núcleo básico rural - Límites de vías y predios                                                                                                                      | Polígono 2D | 146       | 
| ENTIDADES _TERRITORIALES _Y_ADMINISTRATIVAS | PERIMETRO                         | Perímetro urbano                                                                                                                                                     | Polígono 2D | 1         | 
| ENTIDADES _TERRITORIALES _Y_ADMINISTRATIVAS | PERIMETRO_CPR                     | Perímetro de centros poblados rurales y asentamientos humanos cercanos                                                                                               | Polígono 2D | 26        | 
| ENTIDADES _TERRITORIALES _Y_ADMINISTRATIVAS | PERIMETRO_SymDiff                 | Diferencias entre límite de perímetro urbano y predios                                                                                                               | Polígono 2D | 14        | 
| ENTIDADES _TERRITORIALES _Y_ADMINISTRATIVAS | UNIDAD_MORFOLOGICA                | Unidades morfológicas urbanas                                                                                                                                        | Polígono 2D | 37        | 
| ENTIDADES _TERRITORIALES _Y_ADMINISTRATIVAS | ZONA_URBANA                       | Límite de zona urbana                                                                                                                                                | Polígono 2D | 5         | 
| ENTIDADES _TERRITORIALES _Y_ADMINISTRATIVAS | ZONA_URBANA_EXPANSION             | Límite zona urbana ajustada a partir de predios                                                                                                                      | Polígono 2D | 2         | 
| RURAL                                       | SECTOR_RURAL                      | Límite catastral zona rural                                                                                                                                          | Polígono 2D | 1         | 
| RURAL                                       | TERRENO_PREDIO_RURAL              | Predios rurales                                                                                                                                                      | Polígono 2D | 9554      | 
| RURAL                                       | VEREDA                            | Límites veredales                                                                                                                                                    | Polígono 2D | 14        | 
| RURAL                                       | ZONA_HOMOGENEA_FISICA_RURAL       | Zonas homogéneas físicas rurales                                                                                                                                     | Polígono 2D | 58        | 
| RURAL                                       | ZONA_HOMOGENEA_GEOECONOMICA_RURAL | Zonas homogéneas geoeconómicas rurales                                                                                                                               | Polígono 2D | 80        | 
| URBANO                                      | CONSTRUCCION_ANEXA                | Construcciones anexas urbanas                                                                                                                                        | Polígono 2D | 7893      | 
| URBANO                                      | EDIFICACION                       | Edificaciones urbanas                                                                                                                                                | Polígono 2D | 33984     | 
| URBANO                                      | Edificacion_Altura                | Predios con asociación de altura en edificación por número de pisos                                                                                                  | Polígono 2D | 3165      | 
| URBANO                                      | MANZANA                           | Manzanas catastrales                                                                                                                                                 | Polígono 2D | 711       | 
| URBANO                                      | NOMENCLATURA_DOMICILIARIA         | Líneas con identificación de nomenclatura de direcciones urbanas                                                                                                     | Línea 2D    | 15144     | 
| URBANO                                      | NOMENCLATURA_VIAL                 | Nomenclatura de vías urbanas                                                                                                                                         | Línea 2D    | 593       | 
| URBANO                                      | SECTOR_URBANO                     | Límite catastral zona urbana                                                                                                                                         | Polígono 2D | 1         | 
| URBANO                                      | TERRENO_PREDIO_URBANO             | Predios urbanos                                                                                                                                                      | Polígono 2D | 16750     | 
| URBANO                                      | ZONA_GEOECONOMICA_URBANA          | Zonas homogéneas geoeconómicas urbanas                                                                                                                               | Polígono 2D | 107       | 
| URBANO                                      | ZONA_HOMOGENEA_FISICA_URBANA      | Zonas homogéneas físicas urbanas                                                                                                                                     | Polígono 2D | 107       | 
| N/A                                         | Registro1                         | Tabla registro catastral 1 con descriptores de predio                                                                                                                | N/A         | 46305     | 
| N/A                                         | Registro2                         | Tabla registro catastral 2 con descriptores de construcciones                                                                                                        | N/A         | 31599     | 

Límites espaciales y observacione

| Nombre                            | Límite norte   | Límite sur     | Límite este    | Límite oeste   | Área envolvente (ha) | Observaciones                                                                                                                                                                                 |
|-----------------------------------|----------------|----------------|----------------|----------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BARRIOS.shp                       | 1049014.279907 | 1045711.493713 | 1007244.523926 | 1010930.528931 | 1217.40864415292     |                                                                                                                                                                                               |
| COMUNAS.shp                       | 1049154.869873 | 1044686.484924 | 1007244.523926 | 1010935.286499 | 1649.17479315262     | Sin código DANE, sin barrios asociados en todas las comunas.                                                                                                                                  |
| EXP_URBANA_AJUSTADA_PREDIOS.shp   | 1049186.011156 | 1044897.407898 | 1008014.665958 | 1010777.4809   | 1184.86171615121     | Zona sur y oriental.                                                                                                                                                                          |
| HIDROGRAFIA.shp                   | 1063045.120117 | 1040394.31012  | 997235.56012   | 1018799.362122 | 48843.7581960229     | Red discontínua en varias zonas. Incluye nombres de algunos cauces principales. Sin pendiente media, ancho promedio del cauce.                                                                |
| MOT.shp                           | 1062201.8706   | 1040543.8239   | 998131.3158    | 1018799.3621   | 44762.9511963164     | Sin descripción del procedimiento de delimitación de cada categoría.                                                                                                                          |
| ORDEN_VIAL.shp                    | 1062201.8706   | 1040543.8239   | 998131.3158    | 1018799.3621   | 44762.9511963164     | Con atributos provenientes de CAD. Nombre solo en 3 entidades. Sin indicación de sentido vial, restricción vehicular, velocidad permitida.                                                    |
| RIO_BOGOTA.shp                    | 1044274.2144   | 1041161.9281   | 1008907.3291   | 1015090.4591   | 1924.36707901192     | Sin nombre, pendiente media, ancho promedio del cauce.                                                                                                                                        |
| VEREDA.shp                        | 1062201.8706   | 1040543.8239   | 998131.3158    | 1018799.3621   | 44762.9511963164     |                                                                                                                                                                                               |
| VIAS.shp                          | 1049280.672729 | 1045802.309972 | 1008012.379068 | 1010933.968323 | 1016.23472558434     | Con ancho de perifil transversal en metros en 11 entidades, con definición de tipo en 2 entidades. Sin nombre de vía, indicación de sentido vial, restricción vehicular, velocidad permitida. |
| VIAS_PERIMETRO.shp                | 1050000.450928 | 1043599.951477 | 1007307.88208  | 1012355.771301 | 3230.90121877195     | Contiene nombre de vía, tipo, estado y clasificación.                                                                                                                                         |
| VIAS_PERIMETRO_URBANO.shp         | 1050076.120117 | 1040688.380127 | 1007307.88208  | 1014935.190125 | 7160.3184750095      | Contiene nombre de vía, tipo, estado,  clasificación y destinación Sin indicación de sentido vial, restricción vehicular, velocidad permitida.                                                |
| VIAS_RURALES.shp                  | 1062201.8706   | 1040543.8239   | 998131.3158    | 1018799.3621   | 44762.9511963164     | Con atributos provenientes de CAD. Nombre solo en 3 entidades. Sin indicación de sentido vial, restricción vehicular, velocidad permitida. Capa similar o idéntica a ORDEN_VIAL.shp.          |
| VIAS_URBANAS.shp                  | 1050000.450928 | 1043599.951477 | 1006307.339905 | 1013626.410706 | 4684.57086436314     | Contiene nombre de vía, tipo, estado y  clasificación. Sin indicación de sentido vial, restricción vehicular, velocidad permitida.                                                            |
| ZONA_URBANA_AJUSTADA_PREDIOS.shp  | 1049261.875112 | 1045672.301915 | 1007255.695945 | 1012738.086262 | 1967.94413373953     |                                                                                                                                                                                               |
| ANDENES                           | 1049280.2325   | 1044508.9313   | 1006307.3399   | 1013626.4107   | 3492.1491290924      | Corresponde a ejes viales con caracterización de si tienen andén o no y su estado y no a lineas de anden en cada costado de vía, no se indica si el ande se ubica en ambos costados o no.     |
| ANDENES_CPR                       | 1049010.2681   | 1044930.8713   | 1006307.3399   | 1013626.4107   | 2985.73940004933     | Corresponde a ejes viales con caracterización de si tienen andén o no y su estado y no a lineas de anden en cada costado de vía, no se indica si el ande se ubica en ambos costados o no.     |
| ANDENES_PERIMETRO                 | 1049280.2325   | 1044508.9313   | 1007307.8821   | 1010919.7183   | 1723.31583952625     | Corresponde a ejes viales con caracterización de si tienen andén o no y su estado y no a lineas de anden en cada costado de vía, no se indica si el ande se ubica en ambos costados o no.     |
| ANOTACION                         | 1062051.1369   | 1041056.6217   | 998300.3069    | 1017124.8397   | 39521.19400025       | Múltiples anotaciones sin nombre geográfico. Sin atributo de agrupamiento.                                                                                                                    |
| ANOTACION_URBANO                  | 1048899.6587   | 1044931.0017   | 1007586.7963   | 1013415.1767   | 2313.08426731225     | Sin atributo de agrupamiento.                                                                                                                                                                 |
| CURVAS_NIVEL                      | 1062553.5381   | 1040000.8401   | 997032.8751    | 1019928.4009   | 51635.5878918609     | No se espeficica el modelo digital de elevación a partir del cual fueron generadas.                                                                                                           |
| EDIFICACION_RURAL                 | 1062051.1369   | 1041056.6217   | 998300.3069    | 1017124.8397   | 39521.19400025       | Múltiples anotaciones sin nombre geográfico. Sin atributo de agrupamiento.                                                                                                                    |
| EDUCATIVO                         | 1054521.0743   | 1042239.6693   | 1001487.8765   | 1015047.9737   | 16653.7045552566     | Nombres geográficos completos. Caracter y nivel incompletos.                                                                                                                                  |
| HIDROGRAFIA                       | 1063045.1201   | 1040394.3101   | 997235.5601    | 1018799.3621   | 48843.7581979619     | Red discontínua en varias zonas. Incluye nombres de algunos cauces principales. Sin pendiente media, ancho promedio del cauce.                                                                |
| HIDROGRAFIA_Buffer                | 1063075.1201   | 1040364.3101   | 997205.5601    | 1018829.3621   | 49109.4058699619     | Red discontínua en varias zonas. Incluye nombres de algunos cauces principales.                                                                                                               |
| HIDROGRAFIA_Buffer1               | 1063075.1201   | 1040653.1203   | 997838.4401    | 1018829.3621   | 47065.8448885816     | Red discontínua en varias zonas. Incluye nombres de algunos cauces principales.                                                                                                               |
| LIM_NBR                           | 1055414.5573   | 1042782.5241   | 999980.8757    | 1005864.0709   | 7431.67170884813     |                                                                                                                                                                                               |
| RONDAS                            | 1063075.1201   | 1040364.3101   | 997205.5601    | 1018829.3621   | 49109.4058699619     | Red discontínua en varias zonas. Entidades multiparte.                                                                                                                                        |
| VIAS_CPR                          | 1050000.4509   | 1043599.9515   | 1006307.3399   | 1013626.4107   | 4684.57082639581     | Contiene nombre de vía, tipo, estado y  clasificación. Sin indicación de sentido vial, restricción vehicular, velocidad permitida.                                                            |
| VIAS_PERIMETRO                    | 1050000.4509   | 1043599.9515   | 1007307.8821   | 1012355.7713   | 3230.90117958668     | Contiene nombre de vía, tipo, estado y clasificación.                                                                                                                                         |
| VIAS_RURALES                      | 1062778.0001   | 1040490.3801   | 998888.0035    | 1019492.1901   | 45921.8281349895     | Con atributos provenientes de CAD. Nombre solo en 3 entidades. Sin indicación de sentido vial, restricción vehicular, velocidad permitida.                                                    |
| VIAS_URBANAS                      | 1050000.4509   | 1043599.9515   | 1006307.3399   | 1013626.4107   | 4684.57082639581     | Contiene nombre de vía, tipo, estado y  clasificación. Sin indicación de sentido vial, restricción vehicular, velocidad permitida.                                                            |
| VIAS_URBANAS_Buffer               | 1050014.0175   | 1043579.9567   | 1006292.3221   | 1013646.4107   | 4731.66531809877     | Contiene nombre de vía, tipo, estado y  clasificación.                                                                                                                                        |
| BARRIOS                           | 1049014.279907 | 1045711.493713 | 1007244.523926 | 1010930.528931 | 1217.40864415292     |                                                                                                                                                                                               |
| Centrospobladosrurales            | 1049510.29248  | 1044899        | 1006360.474121 | 1013665.409912 | 3368.51954799212     | Clasificación de predios por centro poblado incompleta.                                                                                                                                       |
| COMUNAS                           | 1049154.869873 | 1044686.484924 | 1007244.523926 | 1010935.286499 | 1649.17479315262     | Sin código DANE, sin barrios asociados en todas las comunas.                                                                                                                                  |
| NBR                               | 1055150.223084 | 1042963.425476 | 1000074.76947  | 1005674.203918 | 6823.91743370383     |                                                                                                                                                                                               |
| NucleosBasicosRurales             | 1055414.557312 | 1042782.524109 | 999980.875671  | 1005864.070923 | 7431.67177629965     |                                                                                                                                                                                               |
| PERIMETRO                         | 1049186.011291 | 1045526.33728  | 1007255.696289 | 1010911.887695 | 1338.04686677803     |                                                                                                                                                                                               |
| PERIMETRO_CPR                     | 1049509.113281 | 1044898.787903 | 1006394.133301 | 1013668.833679 | 3353.87357700392     |                                                                                                                                                                                               |
| PERIMETRO_SymDiff                 | 1048343.895325 | 1045689.239685 | 1007944.131287 | 1010802.130493 | 758.700371132348     |                                                                                                                                                                                               |
| UNIDAD_MORFOLOGICA                | 1049105.500488 | 1045545.625305 | 1007244.523926 | 1010935.286499 | 1313.86540899681     | Sin descripción de características arquitectónicas o morfológicas, solo se numeran.                                                                                                           |
| ZONA_URBANA                       | 1049105.500488 | 1045545.625305 | 1007244.523926 | 1010935.286499 | 1313.86540899681     | Sin nombres.                                                                                                                                                                                  |
| ZONA_URBANA_EXPANSION             | 1049154.869873 | 1044686.484924 | 1008032.91272  | 1010748.114929 | 1213.25686841874     | Sin nombres.                                                                                                                                                                                  |
| SECTOR_RURAL                      | 1062201.8706   | 1040543.8239   | 1040543.8239   | 1040543.8239   | 0                    |                                                                                                                                                                                               |
| TERRENO_PREDIO_RURAL              | 1062201.8706   | 1040543.8239   | 998131.3158    | 1018799.3621   | 44762.9511963164     |                                                                                                                                                                                               |
| VEREDA                            | 1062201.8706   | 1040543.8239   | 998131.3158    | 1018799.3621   | 44762.9511963164     |                                                                                                                                                                                               |
| ZONA_HOMOGENEA_FISICA_RURAL       | 1062201.8706   | 1040543.8239   | 998131.3158    | 1018799.3621   | 44762.9511963164     |                                                                                                                                                                                               |
| ZONA_HOMOGENEA_GEOECONOMICA_RURAL | 1062201.8706   | 1040543.8239   | 998131.3158    | 1018799.3621   | 44762.9511963164     | Sin campo descriptivo con criterio de homogenización.                                                                                                                                         |
| CONSTRUCCION_ANEXA                | 1049085.867126 | 1045726.317871 | 1007262.824707 | 1010866.636475 | 1210.71831403446     | Incluye descripción de usos.                                                                                                                                                                  |
| EDIFICACION                       | 1049137.351074 | 1045726.693726 | 1007255.751282 | 1010868.599304 | 1232.21866534412     | Incluye número de pisos                                                                                                                                                                       |
| Edificacion_Altura                | 1049043.169495 | 1045681.832275 | 1007359.179871 | 1010912.083679 | 1194.25078089102     | No incluye todos los predios urbanos con edificaciones.                                                                                                                                       |
| MANZANA                           | 1049185.877075 | 1045526.349487 | 1007255.751282 | 1010912.083679 | 1338.04492777196     |                                                                                                                                                                                               |
| NOMENCLATURA_DOMICILIARIA         | 1049061.903076 | 1045709.535522 | 1007261.154297 | 1010870.147278 | 1209.86709721181     | Incluye texto descriptor.                                                                                                                                                                     |
| NOMENCLATURA_VIAL                 | 1049280.115906 | 1045489.797913 | 1007307.936279 | 1010919.914673 | 1369.05466971051     |                                                                                                                                                                                               |
| SECTOR_URBANO                     | 1049185.877319 | 1045526.349487 | 1007255.751282 | 1010912.083923 | 1338.04510627895     |                                                                                                                                                                                               |
| TERRENO_PREDIO_URBANO             | 1049185.877075 | 1045526.349487 | 1007255.751282 | 1010912.083679 | 1338.04492777196     |                                                                                                                                                                                               |
| ZONA_GEOECONOMICA_URBANA          | 1049185.877075 | 1045526.349487 | 1007255.751282 | 1010912.083679 | 1338.04492777196     | Sin campo descriptivo con criterio de homogenización.                                                                                                                                         |
| ZONA_HOMOGENEA_FISICA_URBANA      | 1049185.877075 | 1045526.349487 | 1007255.751282 | 1010912.083679 | 1338.04492777196     |                                                                                                                                                                                               |



### 3.2. Capas utilizadas en formulación

* Data source: \file\data\POT\Anexo_Acuerdo_012_2013\shp\
* CRS: EPSG 3116 o MAGNA Origen Bogota Colombia, 2011.
* Fuente de datos: sin metadatos disponibles para verificación de fuentes originales de datos.
* Alias: igual al nombre de la capa, sin metadatos para asociación de alias.




<div align="center">Visualización de elementos recopilados</div>

**BARRIOS.shp**: Formulación POT - Barrios zona urbana<br><img src='graph/ArcGISPro_Layer_BARRIOS_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**COMUNAS.shp**: Formulación POT - Comunas urbanas<br><img src='graph/ArcGISPro_Layer_COMUNAS_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**EXP_URBANA_AJUSTADA_PREDIOS.shp**: Formulación POT - Límite zona de expansión urbana a partir de predios<br><img src='graph/ArcGISPro_Layer_EXP_URBANA_AJUSTADA_PREDIOS_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**HIDROGRAFIA.shp**: Formulación POT - Red hidrográfica<br><img src='graph/ArcGISPro_Layer_HIDROGRAFIA_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**MOT.shp**: Formulación POT - Modelo de ocupación del territorio<br><img src='graph/ArcGISPro_Layer_MOT_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**ORDEN_VIAL.shp**: Formulación POT - Orden vial rural<br><img src='graph/ArcGISPro_Layer_ORDEN_VIAL_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**RIO_BOGOTA.shp**: Formulación POT - Tramo Río Bogotá sobre municipio<br><img src='graph/ArcGISPro_Layer_RIO_BOGOTA_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**VEREDA.shp**: Formulación POT - Límites veredales ajustados<br><img src='graph/ArcGISPro_Layer_VEREDA_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**VIAS.shp**: Formulación POT - Vías principales proyectadas<br><img src='graph/ArcGISPro_Layer_VIAS_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**VIAS_PERIMETRO.shp**: Formulación POT - Vías perímetro urbano principal<br><img src='graph/ArcGISPro_Layer_VIAS_PERIMETRO_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**VIAS_PERIMETRO_URBANO.shp**: Formulación POT - Vías perímetro urbano y vías proyectadas. Incluye la zona urbana central, La Paz, Villa del Rosario y Barandillas<br><img src='graph/ArcGISPro_Layer_VIAS_PERIMETRO_URBANO_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**VIAS_RURALES.shp**: Formulación POT - Vías rurales<br><img src='graph/ArcGISPro_Layer_VIAS_RURALES_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**VIAS_URBANAS.shp**: Formulación POT - Vías urbanas<br><img src='graph/ArcGISPro_Layer_VIAS_URBANAS_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>
**ZONA_URBANA_AJUSTADA_PREDIOS.shp**: Formulación POT - Límite zona urbana ajustada a partir de predios<br><img src='graph/ArcGISPro_Layer_ZONA_URBANA_AJUSTADA_PREDIOS_shp.png' alt='R.SIGE' width='100%' border='0' /><br><br>



## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad     | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P1** | Esta actividad no requiere del desarrollo de elementos en el avance P1 del proyecto final, los contenidos son evaluados en el quiz de conocimiento y habilidad.                                                                                                                                                                                                                                                                                     | 
| Avance **P1** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. |

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Compatibilidad

* Esta actividad puede ser desarrollada con cualquier software SIG que disponga de herramientas para de digitalización con opciones de encajado o snapping.
* 



## Referencias

* 


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