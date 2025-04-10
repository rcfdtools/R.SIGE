# Inventario de información geo-espacial recopilada del POT, diccionario y modelo de datos
Keywords: `pot` `data-gis-dictionaty` `shapefile` `feature-class` `layer` `grid` `tiff` `geodatabase` `gdb` `CRS` `envelope` `geotable`

En esta actividad se presenta una tabla resumen de la información geo-espacial (vectorial, ráster) y tablas anexas al POT.

<div align="center"><img src="graph/POTLayer.png" alt="R.SIGE" width="100%" border="0" /><br><br></div>


## Objetivos

* Revisar el contenido geográfico (geometría, límite espacial, número de vectores, CRS, tamaño del área envolvente) y los atributos contenidos en las diferentes capas utilizadas en la elaboración del POT en sus etapas de diagnóstico y formulación.
* Revisar las tablas de datos complementarias y su contenido.


## Requerimientos

* [:toolbox:Herramienta](https://www.microsoft.com/es/microsoft-365/excel?market=bz): Microsoft Excel 365.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.
* [:open_file_folder:POT_Layer.xlsx](POT_Layer.xlsx): libro para registro de capas, grillas y tablas recopiladas.


## 1. Especificaciones para revisión

En el libro de Microsoft Excel suministrado para el desarrollo de esta actividad, se registran los siguientes atributos:

| Columna              | Alcance de evaluación                                                                                                                                                                 |
|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Etapa                | Diagnóstico, Formulación, Implementación, Evaluación y seguimiento.                                                                                                                   |
| Tipo                 | Vector, Tabla, Ráster.                                                                                                                                                                |
| Dataset              | Nombre de GDB / Nombre del grupo de capas. Para archivos que no estén contenidos dentro de una GDB indicar el nombre de la carpeta que contiene el elemento.                          |
| Nombre               | Nombre del elemento. Para archivos que no estén contenidos dentro de una GDB incluir la extensión primaria, p. ej.: .shp, .tif, .dbf, dwg.                                            |
| Alias                | Nombre corto utilizado en listas de elementos sobre mapas. En caso de que no disponga de nombre corto, incluir el Nombre sin extensión.                                               |
| Descripción          | Evalúe la espacialidad de la capa y sus atributos para identificar que contiene y representa.                                                                                         |
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

> :bulb: Si su municipio no cuenta con información publicada en la plataforma _Colombia OT_, realice directamente la solicitud de información del POT a la Secretaría o Gerencia de Planeación.

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
| [:floppy_disk:25899.gdb.zip](../../file/data/POT/Anexo_Acuerdo_012_2013/gdb/25899.gdb.zip)                                                  | gdb       | 57464       |

</div>

> Renombre los archivos comprimidos con los nombres indicados en la tabla anterior. Se ha incluído en la lista la base de datos convertida a formato `.gdb`. 

3. En su repositorio de proyecto y dentro de la carpeta `\file\data\POT\Anexo_Acuerdo_012_2013\shp\`, guarde y descomprima los archivos vectoriales en formato Shapefile.

<div align="center"><img src="graph/Data_POT_shp.png" alt="R.SIGE" width="100%" border="0"/></div>

4. En su repositorio de proyecto y dentro de la carpeta `\file\data\POT\Anexo_Acuerdo_012_2013\gdb\`, guarde y descomprima la base de datos _25899.zip_ en formato Microsoft Database `.mdb`.

> Debido a que ArcGIS Pro no permite la apertura directa de archivos de bases de datos en formato `.mdb`, se ha convertido a formato `.gdb`. La conversión fue realizada desde la herramienta ArcGIS for Desktop creando una base de datos en blanco, un dataset con el CRS de una de las capas y luego importando las diferentes clases de entidad contenidas en la base `.mdb`.

<div align="center"><img src="graph/Data_POT_gdb.png" alt="R.SIGE" width="100%" border="0"/></div>


## 3. Visualización y consulta

Para la visualización preliminar y consulta de los datos geo-espaciales descargados y descomprimidos, siga este procedimiento:

1. En ArcGIS Pro, cree un proyecto nuevo en blanco con el nombre `ArcGISPro` y guarde dentro de la carpeta `\file\map`. Renombre el mapa inicial como _POTLayer_. Podrá observar que automáticamente se agrega al mapa la capa _Topographic_ que corresponde al mapa topográfico del mundo creado por ESRI.

<div align="center"><img src="graph/ArcGISPro_NewMap.png" alt="R.SIGE" width="100%" border="0"/></div>

2. En el menú _View_, de clic en el botón _Catalog Pane_ que activará el panel lateral derecho de su catálogo de datos. De clic derecho en la carpeta _Folders_, seleccione la opción _Add Folder Connection_ y seleccione su directorio de proyecto.

> Para ejemplificar este curso, la carpeta de proyecto es `C:\R.SIGE`.

<div align="center"><img src="graph/ArcGISPro_AddFolderConnection.png" alt="R.SIGE" width="100%" border="0"/></div>

3. Expanda el árbol de _Folders_, podrá observar que se encuentran dos carpetas asociadas. La carpeta `ArcGISPro` corresponde a la carpeta por defecto que se genera al crear un proyecto nuevo en ArcGIS Pro, y la carpeta _R.SIGE_ es la carpeta general del proyecto.

<div align="center"><img src="graph/ArcGISPro_Folders.png" alt="R.SIGE" width="100%" border="0"/></div>

4. En _R.SIGE_, expanda el arból de la carpeta _file_ hasta el subnivel `\data\POT\`, la carpeta del Acuerdo y las subcarpetas _shp_ y _gdb_. Podrá observar que se encuentran las diferentes capas descomprimidas y la base de datos. De clic derecho en la capa _BARRIOS.shp_ y seleccione la opción _Properties_.

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

> No se han incluído en la revisión las siguientes clases de entidad de la base de datos geográfica, debido a que no contienen entidades, o por que no se dispone de metadatos asociados que expliquen su contenido o propósito: AREA_HOMOGENEA_TIERRA, CONSTRUCCION_ANEXA_AMPLIACION, EDIFICACION_AMPLIACION, MANZANA_AMPLIACION, NOMENCLATURA_DOMICILIARIA_AMPLIACIONES, NOMENCLATURA_VIAL_AMPLIACIONES, TERRENO_PREDIO_RURAL_AMPLIACION, TERRENO_PREDIO_RURAL_Interse, TERRENO_PREDIO_RURAL_Interse1, TERRENO_PREDIO_RURAL_Interse2, AREA_COMUN_URBANA, TERRENO_PREDIO_URBANO_AMPLIACION.

### 3.1. Capas y tablas utilizadas en el diagnóstico

Propiedades comúnes:

* Data source: file\data\POT\Anexo_Acuerdo_012_2013\gdb\25899.gdb
* CRS: EPSG 3116 o MAGNA Origen Bogota Colombia, 2011.
* Fuente de datos: sin metadatos disponibles para verificación de fuentes originales de datos.
* Alias: igual al nombre de la capa, sin metadatos para asociación.


#### 3.1.1. Dataset - Cartografía

| GIS                                                        | Nombre              | Descripción                                                                                                                                                          | Geometría   | Registros | 
|------------------------------------------------------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-----------| 
| ![[R.SIGE]](graph/ArcGISPro_Layer_ANDENES.png)             | ANDENES             | Andenes zona urbana y centros poblados rurales próximos al área urbana                                                                                               | Línea 2D    | 766       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_ANDENES_CPR.png)         | ANDENES_CPR         | Andenes en centros poblados rurales próximos al área urbana                                                                                                          | Línea 2D    | 162       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_ANDENES_PERIMETRO.png)   | ANDENES_PERIMETRO   | Andenes en zona urbana central                                                                                                                                       | Línea 2D    | 604       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_ANOTACION.png)           | ANOTACION           | Puntos de interés rural                                                                                                                                              | Punto 2D    | 1851      | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_ANOTACION_URBANO.png)    | ANOTACION_URBANO    | Puntos de interés urbano                                                                                                                                             | Punto 2D    | 158       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_CURVAS_NIVEL.png)        | CURVAS_NIVEL        | Curvas de nivel, principales cada 200 metros y secundarias cada 50 metros.                                                                                           | Línea 2D    | 149       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_EDIFICACION_RURAL.png)   | EDIFICACION_RURAL   | Nodos de localización de edificaciones en la zona rural                                                                                                              | Punto 2D    | 1828      | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_EDUCATIVO.png)           | EDUCATIVO           | Nodos de localización de centros educativos                                                                                                                          | Punto 2D    | 74        | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_HIDROGRAFIA.png)         | HIDROGRAFIA         | Red hidrográfica                                                                                                                                                     | Línea 2D    | 305       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_HIDROGRAFIA_Buffer.png)  | HIDROGRAFIA_Buffer  | Rondas hídricas con aferencia de 30 metros a cada lado de las líneas de la red hidrográfica                                                                          | Polígono 2D | 305       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_HIDROGRAFIA_Buffer1.png) | HIDROGRAFIA_Buffer1 | Rondas hídricas con aferencia de 30 metros a cada lado de las líneas de la red hidrográfica y para tramo de drenaje mayoritariamente dentro del límite del municipio | Polígono 2D | 264       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_LIM_NBR.png)             | LIM_NBR             | Núcleo básico rural - Límites de vías y predios                                                                                                                      | Polígono 2D | 146       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_RONDAS.png)              | RONDAS              | Rondas hídricas                                                                                                                                                      | Polígono 2D | 5         | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_VIAS_CPR.png)            | VIAS_CPR            | Vías interconectoras desde el centro urbano y hacia centros poblados rurales - CPR                                                                                   | Línea 2D    | 200       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_VIAS_PERIMETRO.png)      | VIAS_PERIMETRO      | Vías perímetro urbano principal                                                                                                                                      | Línea 2D    | 604       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_VIAS_RURALES.png)        | VIAS_RURALES        | Vías rurales                                                                                                                                                         | Línea 2D    | 774       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_VIAS_URBANAS.png)        | VIAS_URBANAS        | Vías urbanas                                                                                                                                                         | Línea 2D    | 784       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_VIAS_URBANAS_Buffer.png) | VIAS_URBANAS_Buffer | Aferencia en vías urbanas a 20 metros y solo en 1 costado                                                                                                            | Polígono 2D | 784       | 


#### 3.1.2. Dataset - Entidades Territoriales

| GIS                                                           | Nombre                 | Descripción                                                            | Geometría   | Registros | 
|---------------------------------------------------------------|------------------------|------------------------------------------------------------------------|-------------|-----------| 
| ![[R.SIGE]](graph/ArcGISPro_Layer_BARRIOS.png)                | BARRIOS                | Barrios zona urbana                                                    | Polígono 2D | 49        | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_Centrospobladosrurales.png) | Centrospobladosrurales | Predios en centros poblados rurales                                    | Polígono 2D | 3615      | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_COMUNAS.png)                | COMUNAS                | Comunas urbanas                                                        | Polígono 2D | 4         | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_NBR.png)                    | NBR                    | Núcleo básico rural - Predios                                          | Polígono 2D | 282       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_NucleosBasicosRurales.png)  | NucleosBasicosRurales  | Núcleo básico rural - Límites de vías y predios                        | Polígono 2D | 146       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_PERIMETRO.png)              | PERIMETRO              | Perímetro urbano                                                       | Polígono 2D | 1         | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_PERIMETRO_CPR.png)          | PERIMETRO_CPR          | Perímetro de centros poblados rurales y asentamientos humanos cercanos | Polígono 2D | 26        | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_PERIMETRO_SymDiff.png)      | PERIMETRO_SymDiff      | Diferencias entre límite de perímetro urbano y predios                 | Polígono 2D | 14        | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_UNIDAD_MORFOLOGICA.png)     | UNIDAD_MORFOLOGICA     | Unidades morfológicas urbanas                                          | Polígono 2D | 37        | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_ZONA_URBANA.png)            | ZONA_URBANA            | Límite de zona urbana                                                  | Polígono 2D | 5         | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_ZONA_URBANA_EXPANSION.png)  | ZONA_URBANA_EXPANSION  | Límite zona urbana ajustada a partir de predios                        | Polígono 2D | 2         | 


#### 3.1.3. Dataset - Rural

| GIS                                                                      | Nombre                             | Descripción                            | Geometría   | Registros | 
|--------------------------------------------------------------------------|------------------------------------|----------------------------------------|-------------|-----------| 
| ![[R.SIGE]](graph/ArcGISPro_Layer_SECTOR_RURAL.png)                      | SECTOR_RURAL                       | Límite catastral zona rural            | Polígono 2D | 1         | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_TERRENO_PREDIO_RURAL.png)              | TERRENO_PREDIO_RURAL               | Predios rurales                        | Polígono 2D | 9554      | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_VEREDA.png)                            | VEREDA                             | Límites veredales                      | Polígono 2D | 14        | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_ZONA_HOMOGENEA_FISICA_RURAL.png)       | ZONA_HOMOGENEA _FISICA_RURAL       | Zonas homogéneas físicas rurales       | Polígono 2D | 58        | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_ZONA_HOMOGENEA_GEOECONOMICA_RURAL.png) | ZONA_HOMOGENEA _GEOECONOMICA_RURAL | Zonas homogéneas geoeconómicas rurales | Polígono 2D | 80        | 


#### 3.1.4. Dataset - Urbano

| GIS                                                                 | Nombre                        | Descripción                                                         | Geometría   | Registros | 
|---------------------------------------------------------------------|-------------------------------|---------------------------------------------------------------------|-------------|-----------| 
| ![[R.SIGE]](graph/ArcGISPro_Layer_CONSTRUCCION_ANEXA.png)           | CONSTRUCCION_ANEXA            | Construcciones anexas urbanas                                       | Polígono 2D | 7893      | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_EDIFICACION.png)                  | EDIFICACION                   | Edificaciones urbanas                                               | Polígono 2D | 33984     | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_Edificacion_Altura.png)           | Edificacion_Altura            | Predios con asociación de altura en edificación por número de pisos | Polígono 2D | 3165      | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_MANZANA.png)                      | MANZANA                       | Manzanas catastrales                                                | Polígono 2D | 711       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_NOMENCLATURA_DOMICILIARIA.png)    | NOMENCLATURA _DOMICILIARIA    | Líneas con identificación de nomenclatura de direcciones urbanas    | Línea 2D    | 15144     | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_NOMENCLATURA_VIAL.png)            | NOMENCLATURA_VIAL             | Nomenclatura de vías urbanas                                        | Línea 2D    | 593       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_SECTOR_URBANO.png)                | SECTOR_URBANO                 | Límite catastral zona urbana                                        | Polígono 2D | 1         | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_TERRENO_PREDIO_URBANO.png)        | TERRENO_PREDIO_URBANO         | Predios urbanos                                                     | Polígono 2D | 16750     | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_ZONA_GEOECONOMICA_URBANA.png)     | ZONA_GEOECONOMICA_URBANA      | Zonas homogéneas geoeconómicas urbanas                              | Polígono 2D | 107       | 
| ![[R.SIGE]](graph/ArcGISPro_Layer_ZONA_HOMOGENEA_FISICA_URBANA.png) | ZONA_HOMOGENEA _FISICA_URBANA | Zonas homogéneas físicas urbanas                                    | Polígono 2D | 107       | 


#### 3.1.5. Tablas

| GIS                                            | Nombre    | Descripción                                                   | Registros  | 
|------------------------------------------------|-----------|---------------------------------------------------------------|------------| 
| ![R.SIGE](graph/ArcGISPro_Table_Registro1.png) | Registro1 | Tabla registro catastral 1 con descriptores de predio         | 46305      | 
| ![R.SIGE](graph/ArcGISPro_Table_Registro2.png) | Registro2 | Tabla registro catastral 2 con descriptores de construcciones | 31599      | 



#### 3.1.6. Límites espaciales y observaciones

| Nombre                             | Límite norte | Límite sur | Límite este | Límite oeste | Área envolvente (ha) | Observaciones                                                                                                                                                                              |
|:-----------------------------------|:-------------|:-----------|:------------|:-------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ANDENES                            | 1049280.2    | 1044508.9  | 1006307.3   | 1013626.4    | 3492.1               | Corresponde a ejes viales con caracterización de si tienen andén o no y su estado, y no a líneas de anden en cada costado de vía, no se indica si el anden se ubica en ambos costados o no. |
| ANDENES_CPR                        | 1049010.3    | 1044930.9  | 1006307.3   | 1013626.4    | 2985.7               | Corresponde a ejes viales con caracterización de si tienen andén o no y su estado, y no a líneas de anden en cada costado de vía, no se indica si el anden se ubica en ambos costados o no. |
| ANDENES_PERIMETRO                  | 1049280.2    | 1044508.9  | 1007307.9   | 1010919.7    | 1723.3               | Corresponde a ejes viales con caracterización de si tienen andén o no y su estado, y no a líneas de anden en cada costado de vía, no se indica si el anden se ubica en ambos costados o no. |
| ANOTACION                          | 1062051.1    | 1041056.6  | 998300.3    | 1017124.8    | 39521.2              | Múltiples anotaciones sin nombre geográfico. Sin atributo de agrupamiento.                                                                                                                 |
| ANOTACION_URBANO                   | 1048899.7    | 1044931    | 1007586.8   | 1013415.2    | 2313.1               | Sin atributo de agrupamiento.                                                                                                                                                              |
| CURVAS_NIVEL                       | 1062553.5    | 1040000.8  | 997032.9    | 1019928.4    | 51635.6              | No se especifica el modelo digital de elevación a partir del cual fueron generadas.                                                                                                        |
| EDIFICACION_RURAL                  | 1062051.1    | 1041056.6  | 998300.3    | 1017124.8    | 39521.2              | Múltiples anotaciones sin nombre geográfico. Sin atributo de agrupamiento.                                                                                                                 |
| EDUCATIVO                          | 1054521.1    | 1042239.7  | 1001487.9   | 1015048      | 16653.7              | Nombres geográficos completos. Carácter y nivel incompletos.                                                                                                                               |
| HIDROGRAFIA                        | 1063045.1    | 1040394.3  | 997235.6    | 1018799.4    | 48843.8              | Red discontinua en varias zonas. Incluye nombres de algunos cauces principales. Sin pendiente media, ancho promedio del cauce.                                                             |
| HIDROGRAFIA_Buffer                 | 1063075.1    | 1040364.3  | 997205.6    | 1018829.4    | 49109.4              | Red discontinua en varias zonas. Incluye nombres de algunos cauces principales.                                                                                                            |
| HIDROGRAFIA_Buffer1                | 1063075.1    | 1040653.1  | 997838.4    | 1018829.4    | 47065.8              | Red discontinua en varias zonas. Incluye nombres de algunos cauces principales.                                                                                                            |
| LIM_NBR                            | 1055414.6    | 1042782.5  | 999980.9    | 1005864.1    | 7431.7               |                                                                                                                                                                                            |
| RONDAS                             | 1063075.1    | 1040364.3  | 997205.6    | 1018829.4    | 49109.4              | Red discontinua en varias zonas. Entidades multiparte.                                                                                                                                     |
| VIAS_CPR                           | 1050000.5    | 1043600    | 1006307.3   | 1013626.4    | 4684.6               | Contiene nombre de vía, tipo, estado y  clasificación. Sin indicación de sentido vial, restricción vehicular, velocidad permitida.                                                         |
| VIAS_PERIMETRO                     | 1050000.5    | 1043600    | 1007307.9   | 1012355.8    | 3230.9               | Contiene nombre de vía, tipo, estado y clasificación.                                                                                                                                      |
| VIAS_RURALES                       | 1062778      | 1040490.4  | 998888      | 1019492.2    | 45921.8              | Con atributos provenientes de CAD. Nombre solo en 3 entidades. Sin indicación de sentido vial, restricción vehicular, velocidad permitida.                                                 |
| VIAS_URBANAS                       | 1050000.5    | 1043600    | 1006307.3   | 1013626.4    | 4684.6               | Contiene nombre de vía, tipo, estado y  clasificación. Sin indicación de sentido vial, restricción vehicular, velocidad permitida.                                                         |
| VIAS_URBANAS_Buffer                | 1050014      | 1043580    | 1006292.3   | 1013646.4    | 4731.7               | Contiene nombre de vía, tipo, estado y  clasificación.                                                                                                                                     |
| BARRIOS                            | 1049014.3    | 1045711.5  | 1007244.5   | 1010930.5    | 1217.4               |                                                                                                                                                                                            |
| Centrospobladosrurales             | 1049510.3    | 1044899    | 1006360.5   | 1013665.4    | 3368.5               | Clasificación de predios por centro poblado incompleta.                                                                                                                                    |
| COMUNAS                            | 1049154.9    | 1044686.5  | 1007244.5   | 1010935.3    | 1649.2               | Sin código DANE, sin barrios asociados en todas las comunas.                                                                                                                               |
| NBR                                | 1055150.2    | 1042963.4  | 1000074.8   | 1005674.2    | 6823.9               |                                                                                                                                                                                            |
| NucleosBasicosRurales              | 1055414.6    | 1042782.5  | 999980.9    | 1005864.1    | 7431.7               |                                                                                                                                                                                            |
| PERIMETRO                          | 1049186      | 1045526.3  | 1007255.7   | 1010911.9    | 1338                 |                                                                                                                                                                                            |
| PERIMETRO_CPR                      | 1049509.1    | 1044898.8  | 1006394.1   | 1013668.8    | 3353.9               |                                                                                                                                                                                            |
| PERIMETRO_SymDiff                  | 1048343.9    | 1045689.2  | 1007944.1   | 1010802.1    | 758.7                |                                                                                                                                                                                            |
| UNIDAD_MORFOLOGICA                 | 1049105.5    | 1045545.6  | 1007244.5   | 1010935.3    | 1313.9               | Sin descripción de características arquitectónicas o morfológicas, solo se numeran.                                                                                                        |
| ZONA_URBANA                        | 1049105.5    | 1045545.6  | 1007244.5   | 1010935.3    | 1313.9               | Sin nombres.                                                                                                                                                                               |
| ZONA_URBANA_EXPANSION              | 1049154.9    | 1044686.5  | 1008032.9   | 1010748.1    | 1213.3               | Sin nombres.                                                                                                                                                                               |
| SECTOR_RURAL                       | 1062201.9    | 1040543.8  | 1040543.8   | 1040543.8    | 0                    |                                                                                                                                                                                            |
| TERRENO_PREDIO_RURAL               | 1062201.9    | 1040543.8  | 998131.3    | 1018799.4    | 44763                |                                                                                                                                                                                            |
| VEREDA                             | 1062201.9    | 1040543.8  | 998131.3    | 1018799.4    | 44763                |                                                                                                                                                                                            |
| ZONA_HOMOGENEA _FISICA_RURAL       | 1062201.9    | 1040543.8  | 998131.3    | 1018799.4    | 44763                |                                                                                                                                                                                            |
| ZONA_HOMOGENEA _GEOECONOMICA_RURAL | 1062201.9    | 1040543.8  | 998131.3    | 1018799.4    | 44763                | Sin campo descriptivo con criterio de homogenización.                                                                                                                                      |
| CONSTRUCCION_ANEXA                 | 1049085.9    | 1045726.3  | 1007262.8   | 1010866.6    | 1210.7               | Incluye descripción de usos.                                                                                                                                                               |
| EDIFICACION                        | 1049137.4    | 1045726.7  | 1007255.8   | 1010868.6    | 1232.2               | Incluye número de pisos                                                                                                                                                                    |
| Edificacion_Altura                 | 1049043.2    | 1045681.8  | 1007359.2   | 1010912.1    | 1194.3               | No incluye todos los predios urbanos con edificaciones.                                                                                                                                    |
| MANZANA                            | 1049185.9    | 1045526.3  | 1007255.8   | 1010912.1    | 1338                 |                                                                                                                                                                                            |
| NOMENCLATURA _DOMICILIARIA         | 1049061.9    | 1045709.5  | 1007261.2   | 1010870.1    | 1209.9               | Incluye texto descriptor.                                                                                                                                                                  |
| NOMENCLATURA_VIAL                  | 1049280.1    | 1045489.8  | 1007307.9   | 1010919.9    | 1369.1               |                                                                                                                                                                                            |
| SECTOR_URBANO                      | 1049185.9    | 1045526.3  | 1007255.8   | 1010912.1    | 1338                 |                                                                                                                                                                                            |
| TERRENO_PREDIO_URBANO              | 1049185.9    | 1045526.3  | 1007255.8   | 1010912.1    | 1338                 |                                                                                                                                                                                            |
| ZONA_GEOECONOMICA _URBANA          | 1049185.9    | 1045526.3  | 1007255.8   | 1010912.1    | 1338                 | Sin campo descriptivo con criterio de homogenización.                                                                                                                                      |
| ZONA_HOMOGENEA _FISICA_URBANA      | 1049185.9    | 1045526.3  | 1007255.8   | 1010912.1    | 1338                 |                                                                                                                                                                                            |


### 3.2. Capas utilizadas en la formulación

* Data source: \file\data\POT\Anexo_Acuerdo_012_2013\shp\
* CRS: EPSG 3116 o MAGNA Origen Bogota Colombia, 2011.
* Fuente de datos: sin metadatos disponibles para verificación de fuentes originales de datos.
* Alias: igual al nombre de la capa, sin metadatos para asociación.


#### 3.2.1. Capas shapefile

| GIS                                                                   | Nombre                            | Descripción                                                                                                       | Geometría   | Registros | 
|-----------------------------------------------------------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------|-----------| 
| ![R.SIGE](graph/ArcGISPro_Layer_BARRIOS_shp.png)                      | BARRIOS.shp                       | Barrios zona urbana                                                                                               | Polígono 2D | 49        | 
| ![R.SIGE](graph/ArcGISPro_Layer_COMUNAS_shp.png)                      | COMUNAS.shp                       | Comunas urbanas                                                                                                   | Polígono 2D | 4         | 
| ![R.SIGE](graph/ArcGISPro_Layer_EXP_URBANA_AJUSTADA_PREDIOS_shp.png)  | EXP_URBANA_AJUSTADA _PREDIOS.shp  | Límite zona de expansión urbana a partir de predios                                                               | Polígono 2D | 2         | 
| ![R.SIGE](graph/ArcGISPro_Layer_HIDROGRAFIA_shp.png)                  | HIDROGRAFIA.shp                   | Red hidrográfica                                                                                                  | Línea 2D    | 305       | 
| ![R.SIGE](graph/ArcGISPro_Layer_MOT_shp.png)                          | MOT.shp                           | Modelo de ocupación del territorio                                                                                | Polígono 2D | 80        | 
| ![R.SIGE](graph/ArcGISPro_Layer_ORDEN_VIAL_shp.png)                   | ORDEN_VIAL.shp                    | Orden vial rural                                                                                                  | Línea 2D    | 774       | 
| ![R.SIGE](graph/ArcGISPro_Layer_RIO_BOGOTA_shp.png)                   | RIO_BOGOTA.shp                    | Tramo Río Bogotá sobre municipio                                                                                  | Línea 2D    | 1         | 
| ![R.SIGE](graph/ArcGISPro_Layer_VEREDA_shp.png)                       | VEREDA.shp                        | Límites veredales                                                                                                 | Polígono 2D | 14        | 
| ![R.SIGE](graph/ArcGISPro_Layer_VIAS_shp.png)                         | VIAS.shp                          | Vías principales proyectadas                                                                                      | Línea 2D    | 15        | 
| ![R.SIGE](graph/ArcGISPro_Layer_VIAS_PERIMETRO_shp.png)               | VIAS_PERIMETRO.shp                | Vías perímetro urbano principal                                                                                   | Línea 2D    | 604       | 
| ![R.SIGE](graph/ArcGISPro_Layer_VIAS_PERIMETRO_URBANO_shp.png)        | VIAS_PERIMETRO _URBANO.shp        | Vías perímetro urbano y vías proyectadas. Incluye la zona urbana central, La Paz, Villa del Rosario y Barandillas | Línea 2D    | 761       | 
| ![R.SIGE](graph/ArcGISPro_Layer_VIAS_RURALES_shp.png)                 | VIAS_RURALES.shp                  | Vías rurales                                                                                                      | Línea 2D    | 774       | 
| ![R.SIGE](graph/ArcGISPro_Layer_VIAS_URBANAS_shp.png)                 | VIAS_URBANAS.shp                  | Vías urbanas                                                                                                      | Línea 2D    | 784       | 
| ![R.SIGE](graph/ArcGISPro_Layer_ZONA_URBANA_AJUSTADA_PREDIOS_shp.png) | ZONA_URBANA_AJUSTADA _PREDIOS.shp | Límite zona urbana ajustada a partir de predios                                                                   | Polígono 2D | 4         | 


#### 3.2.2. Límites espaciales y observaciones

| Nombre                            | Límite norte | Límite sur | Límite este | Límite oeste | Área envolvente (ha) | Observaciones                                                                                                                                                                                |
|-----------------------------------|--------------|------------|-------------|--------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BARRIOS.shp                       | 1049014.3    | 1045711.5  | 1007244.5   | 1010930.5    | 1217.4               |                                                                                                                                                                                              |
| COMUNAS.shp                       | 1049154.9    | 1044686.5  | 1007244.5   | 1010935.3    | 1649.2               | Sin código DANE, sin barrios asociados en todas las comunas.                                                                                                                                 |
| EXP_URBANA_AJUSTADA _PREDIOS.shp  | 1049186      | 1044897.4  | 1008014.7   | 1010777.5    | 1184.9               | Zona sur y oriental.                                                                                                                                                                         |
| HIDROGRAFIA.shp                   | 1063045.1    | 1040394.3  | 997235.6    | 1018799.4    | 48843.8              | Red discontinua en varias zonas. Incluye nombres de algunos cauces principales. Sin pendiente media, ancho promedio del cauce.                                                               |
| MOT.shp                           | 1062201.9    | 1040543.8  | 998131.3    | 1018799.4    | 44763                | Sin descripción del procedimiento de delimitación de cada categoría.                                                                                                                         |
| ORDEN_VIAL.shp                    | 1062201.9    | 1040543.8  | 998131.3    | 1018799.4    | 44763                | Con atributos provenientes de CAD. Nombre solo en 3 entidades. Sin indicación de sentido vial, restricción vehicular, velocidad permitida.                                                   |
| RIO_BOGOTA.shp                    | 1044274.2    | 1041161.9  | 1008907.3   | 1015090.5    | 1924.4               | Sin nombre, pendiente media, ancho promedio del cauce.                                                                                                                                       |
| VEREDA.shp                        | 1062201.9    | 1040543.8  | 998131.3    | 1018799.4    | 44763                |                                                                                                                                                                                              |
| VIAS.shp                          | 1049280.7    | 1045802.3  | 1008012.4   | 1010934      | 1016.2               | Con ancho de perfil transversal en metros en 11 entidades, con definición de tipo en 2 entidades. Sin nombre de vía, indicación de sentido vial, restricción vehicular, velocidad permitida. |
| VIAS_PERIMETRO.shp                | 1050000.5    | 1043600    | 1007307.9   | 1012355.8    | 3230.9               | Contiene nombre de vía, tipo, estado y clasificación.                                                                                                                                        |
| VIAS_PERIMETRO _URBANO.shp        | 1050076.1    | 1040688.4  | 1007307.9   | 1014935.2    | 7160.3               | Contiene nombre de vía, tipo, estado,  clasificación y destinación Sin indicación de sentido vial, restricción vehicular, velocidad permitida.                                               |
| VIAS_RURALES.shp                  | 1062201.9    | 1040543.8  | 998131.3    | 1018799.4    | 44763                | Con atributos provenientes de CAD. Nombre solo en 3 entidades. Sin indicación de sentido vial, restricción vehicular, velocidad permitida. Capa similar o idéntica a ORDEN_VIAL.shp.         |
| VIAS_URBANAS.shp                  | 1050000.5    | 1043600    | 1006307.3   | 1013626.4    | 4684.6               | Contiene nombre de vía, tipo, estado y  clasificación. Sin indicación de sentido vial, restricción vehicular, velocidad permitida.                                                           |
| ZONA_URBANA_AJUSTADA _PREDIOS.shp | 1049261.9    | 1045672.3  | 1007255.7   | 1012738.1    | 1967.9               |                                                                                                                                                                                              |


## 4. Análisis usando software libre - QGIS

En QGIS podrá realizar la visualización de los diferentes elementos siguiendo estos pasos:

1. Cree un projecto nuevo en blanco, menú Project / New. En el panel lateral denominado _Browser_, abra la carpeta donde están contenidos los archivos de proyecto, seleccione una de las capas y arrástrela al mapa, podrá observar que se ajusta automáticamente a la ventana.

<div align="center"><img src="graph/QGIS_NewMap.png" alt="R.SIGE" width="100%" border="0"/></div>

2. Desde el panel lateral _Layers_, de clic derecho en la capa y abra la tabla de atributos (Open Attribute Table). Utilizando el último botón de opciones de la ventana de tabla, podrá acoplarla a la parte inferior de la ventana. Podrá observar que esta capa contiene 49 registros.

<div align="center"><img src="graph/QGIS_LayerViewTable.png" alt="R.SIGE" width="100%" border="0"/></div>

3. Para consultar las propiedades de la capa, desde el panel lateral _Layers_, de clic derecho en la capa y seleccione la opción _Propiedades_ (Properties). Encontrará diferentes pestañas y en _Information_ podrá consultar un resumen general de la capa indicando la ruta de datos, tamaño en disco, sistema de proyección, campos de atributos, extensión espacial o límites y algunos metadatos complementarios.

<div align="center"><img src="graph/QGIS_LayerProperties.png" alt="R.SIGE" width="100%" border="0"/></div>


## 5. Diccionario y modelo de datos LADM_COL

El diccionario de datos, es un documento o un libro en el cual se establecen las especificaciones de los objetos espaciales y tablas geo-codificadas, manipulados en un Sistema de Información Geográfica. La aplicación de este documento es primordial para los procesos de producción, actualización, consulta, análisis y distribución de datos espaciales, debido a que se contribuye a mejorar su calidad y administración, evitando de esta manera ambiguedades e inconsistencias que puedan surgir en su interpretación.

> Metadatos (.xml): para complementar el diccionario de datos, se recomienda editar los metadatos asociados a cada elemento geográfico e incluir información relacionada con autores, licencia, restricciones de uso, versión, fecha de creación, fecha de actualización y demás información relevante.


### 5.1. Elementos descriptivos

En un diccionario de datos deben ser incluídos los siguientes grupos de elementos:

| Grupo              | Alcance                                                                                                                                             |
|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| Estructura         | Tabla hipervinculada a elementos (capas vectoriales, tablas, grillas) del diccionario con resumen de elementos.                                     |
| Capas geográficas  | Descripción detallada de las capas geográficas vectoriales incluyendo su nombre, descripción, fuente, geometría y catálogo de objetos o atributos.  |
| Tablas             | Descripción detallada de las tablas de atributos y su catálogo de objetos o atributos.                                                              |
| Dominios           | Descripción detallada de las tablas de dominio codificadas.                                                                                         |
| Grillas            | Descripción detallada de grillas ráster incluyendo nu nombre, descripción, fuente, formato, cubrimiento, temporalidad.                              |
| Setup              | Tablas para generación de listas desplegables para selección de atributos comunes en el diccionario.                                                |

> :bulb:Para las capas geográficas, tablas y grillas ráster, se recomienda incluir las columnas definidas en la tabla de recopilación utilizada en esta actividad. También pueden ser incluído el responsable de mantener la información actualizada de cada elemento, el nombre del dataset asociado, la escala de visualización y una ilustración geográfica.

Para el catálogo de objetos de capas y tablas, se deben incluir:

| Objeto       | Descripción                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nombre       | Nombre del campo de atributos. Se recomienda definir el nombre de los campos de elementos con no más de 10 caracteres alfanuméricos, lo anterior debido a que al realizar exportaciones desde bases de datos espaciales que permiten nombres largos, a archivos de formas geométricas en formato shapefile, el nombre de los campos es truncado a 10 caracteres porque son almacenados en archivos de DBase. |
| Tipo         | Tipo de datos: text, int, long, simple, double, date, boolean. Para campos asociados a geometrías y campos para cálculo de valores a partir de otros campos, se recomienda utilizar formato numérico doble.                                                                                                                                                                                                  |
| Tamaño       | Longitud del campo (hasta 255 caracteres). Aplica solo para campos tipo texto.                                                                                                                                                                                                                                                                                                                               |
| Descripción  | Descripción del contenido del campo.                                                                                                                                                                                                                                                                                                                                                                         |
| Dominio      | Si el campo se encuentra normalizado a través de un dominio (campo codificado con valores repetidos), debe ser incluído el nombre del dominio asociado.                                                                                                                                                                                                                                                      |
| Obligatorio  | Sí/No. Indicar si el campo debe contener siempre un valor.                                                                                                                                                                                                                                                                                                                                                   |

> :lady_beetle:En nombres de campos, deben evitarse el uso de caracteres diferentes a los contenidos en el idioma inglés, tales como: tildes y/o acentos, eñes, caracteres especiales (&*%$#@!+=) y espacios. No se recomienda que el nombre de los campos inicie con un número. 


### 5.2. Ejemplos

[:floppy_disk:](../../file/data/ANLA/DiccionarioDatosANLA.xlsx)Diccionario de datos Autoridad Nacional de Licencias Ambientales - ANLA  

<div align="center"><img src="graph/Excel_DiccionarioDatosANLA_Estructura.png" alt="R.SIGE" width="100%" border="0"/></div>
<div align="center"><img src="graph/Excel_DiccionarioDatosANLA_Capas.png" alt="R.SIGE" width="100%" border="0"/></div>
<div align="center"><img src="graph/Excel_DiccionarioDatosANLA_Tablas.png" alt="R.SIGE" width="100%" border="0"/></div>
<div align="center"><img src="graph/Excel_DiccionarioDatosANLA_Dominios.png" alt="R.SIGE" width="100%" border="0"/></div>
<div align="center"><img src="graph/Excel_DiccionarioDatosANLA_Grillas.png" alt="R.SIGE" width="100%" border="0"/></div><br>

[:floppy_disk:](../../file/data/UECIJG/DiccionarioDatosUECIJG.xlsx)Diccionario de datos Universidad Escuela Colombiana de Ingeniería - UECIJG (Versión en [.pdf](https://github.com/rcfdtools/R.AmazonChingaza/blob/main/DiccionarioDatos.pdf))

<div align="center"><img src="graph/Excel_DiccionarioDatosUECIJG_Estructura.png" alt="R.SIGE" width="100%" border="0"/></div>
<div align="center"><img src="graph/Excel_DiccionarioDatosUECIJG_Capas.png" alt="R.SIGE" width="100%" border="0"/></div>
<div align="center"><img src="graph/Excel_DiccionarioDatosUECIJG_Tablas.png" alt="R.SIGE" width="100%" border="0"/></div>
<div align="center"><img src="graph/Excel_DiccionarioDatosUECIJG_Grillas.png" alt="R.SIGE" width="100%" border="0"/></div>


### 5.3 Modelo de datos LADM_COL

Land Administration Domain Model (LADM), es un modelo conceptual que concreta una ontología y una semántica para la administración del territorio.

Consulta en https://www.icde.gov.co/datos-y-recursos/repositorio-modelos-ladm, las versiones oficiales y las versiones en desarrollo de los modelos y sub-modelos conceptuales, lógicos, y físicos derivados de LADM definidos para Colombia y denominados como LADM_COL.

En el caso específico de Planes de Ordenamiento Territorial, el [Ministerio de Vivienda, Ciudad y Territorio de Colombia - MVCT](https://www.minvivienda.gov.co/), ha dispuesto del siguiente modelo relacional, disponible en https://www.icde.gov.co/datos-y-recursos/repositorio-modelos-ladm/plan-de-ordenamiento-territorial-pot

<div align="center"><img src="graph/MVCT_LADM_COL_Diagrama_POT.jpeg" alt="R.SIGE" width="100%" border="0"/></div>

Este modelo contiene las especificaciones de diferentes objetos, tales como:

* COL_UnidadAdministrativaBasica
* COL_FuenteAdministrativa
* COL_FuenteEspacial
* COL_UnidadEspacial
* COL_DRR
* COL_Fuente
* COL_Interesado
* POT_UAB_ClasificacionSuelo
* POT_UAB_SueloProteccionUrbano
* POT_UAB_AreasActividad
* POT_UAB_TratamientoUrbanistico
* POT_UAB_SistemasGenerales
* POT_UAB_ZonificacionSueloRural
* POT_UAB_CentroPobladoRural
* POT_UAB_AreaCondicionRiesgo
* POT_UAB_AreaCondicionAmenaza
* POT_UAB_ZonificacionAmenaza
* POT_Municipio
* POT_FuenteAdministrativa
* POT_FuenteEspacial

Con relación a los dominios, se encuentran definidos:

* POT_AreaActividadTipo
* POT_SistemasGeneralesNivelTipo
* POT_FenomenoAmenazaTipo
* POT_ClasificacionSueloTipo
* POT_CategoriaAmenazaTipo
* POT_SistemasGeneralesEstadoTipo
* POT_TratamientoUrbanisticoTipo
* POT_UsoSueloRuralTipo
* POT_SistemasGeneralesTipo
* POT_CategoriaRuralTipo
* POT_PriorizacionTipo
* POT_SueloProteccionUrbanoTipo
* POT_MedidaIntervencionTipo
* COL_UnidadAdministrativaBasicaTipo
* POT_FuenteAdministrativaTipo
* COL_DocumentoTipo
* COL_InteresadoTipo
* COL_RelacionSuperficieTipo
* POT_RevisionTipo
* POT_PlanOrdenamientoTerritorialTipo
* COL_FuenteAdministrativaTipo
* COL_FormatoTipo
* COL_FuenteEspacialTipo
* COL_EstadoDisponibilidadTipo


## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad     | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P2** | Para su caso de estudio, descargue, descomprima y organice los diferentes datos (vectores, tablas, grillas) utilizados en la elaboración del POT. Revise todos los elementos y en el libro de Excel suministrado, registre los datos indicados en esta actividad. En el informe final y siguiendo el mismo orden de esta actividad, incluya tablas resumen y previsualizaciones de cada elemento. El libro de Excel con el resumen de todos los elementos recopilados se almacena en la carpeta \table.                                                             | 
| Avance **P2** | Opcional - Implemente el diccionario de datos de proyecto incluyendo todos los elementos geo-espaciales recopilados. Aunque su presentación no es obligatoria en el desarrollo de este curso, se recomienda su implementación y permanente actualización incluyendo todas las capas, tablas y grillas que iremos produciendo a lo largo del curso. En el caso particular de estudiantes que vayan a implementar o fortalecer el sistema de información geográfica de su municipio, se recomienda mantener y publicar las actualizaciones realizadas al diccionario. | 
| Avance **P2** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas.                                                                                                                 |

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Referencias

* www.colombiaot.gov.co
* [Diccionario de datos geográficos ENARGAS - Argentina](https://www.enargas.gob.ar/secciones/informacion-geografica/documentacion/Diccionario.pdf)
* https://www.anla.gov.co/01_anla/entidad/subdirecciones-y-oficinas/instrumentos-permisos-y-tramites-ambientales/sistema-de-informacion-geografica
* https://www.escuelaing.edu.co/es/


## Control de versiones

| Versión    | Descripción                                                | Autor                                      | Horas |
|------------|:-----------------------------------------------------------|--------------------------------------------|:-----:|
| 2024.03.07 | Versión inicial con alcance de la actividad                | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.07.04 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   8   |
| 2024.07.05 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   8   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../POTCartography/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/10) | [Siguiente :arrow_forward:](../CountyLimit/Readme.md) |
|----------------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------|

[^1]: 