# Análisis veredal y límite territorial
Keywords: rural-limit geopolitical-limit rural-zone

En esta actividad evaluaremos los límites veredales y sus diferencias a partir del análisis de diferentes fuentes de información. Luego, crearemos el límite territorial municipal global que será utilizado para el recorte de la información geo-espacial obtenida en actividades posteriores.

<div align="center"><img src="graph/Gravity_anomalies_on_Earth.png" alt="R.SIGE" width="50%" border="0" /><sub><br>Tomado de: <a href="Public Domain, https://commons.wikimedia.org/w/index.php?curid=479365">https://commons.wikimedia.org</a></sub><br><br></div>


## Objetivos

* Evaluar los límites geopolíticos veredales e identificar sus diferencias.
* Crear el límite municipal global.


## Requerimientos

* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ArcGIS Pro de ESRI
* [:toolbox:Herramienta](https://qgis.org/): QGIS


## 1. Procedimiento general en ArcGIS Pro


### 1.1. Mapa veredal diagnóstico POT año 2010

1. Abra el proyecto de ArcGIS Pro creado en la actividad anterior y desde el menú _Insert_ cree un nuevo mapa _New Map_ y renombre como _CountyLimit_. Podrá observar que ahora disponemos de dos mapas en el panel del catálogo. 

<div align="center"><img src="graph/ArcGISPro_InsertNewMap.png" alt="R.SIGE" width="100%" border="0" /></div>

2. En la tabla de contenido o _Contents_, de clic derecho sobre el nombre del mapa _CountyLimit_, y seleccione la opción Propiedades o _Properties_. En la pestaña _Coordinate Systems_, busque, seleccione y asigne el sistema de proyección de coordenadas 9377, correspondiente al Orígen Único Nacional de Colombia.

<div align="center"><img src="graph/ArcGISPro_CoordinateSystem9377.png" alt="R.SIGE" width="100%" border="0" /></div>

3. Desde el Panel de Catálogo (_Catalog_) localizado a la derecha, cargue al mapa desde la ruta _\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\gdb\25899.gdb\Rural\_, la clase de entidad denominada _VEREDA_. De clic en el ícono de simbología de la capa y establezca borde negro y sin relleno.

<div align="center"><img src="graph/ArcGISPro_AddLayer_Vereda.png" alt="R.SIGE" width="100%" border="0" /></div>

4. Seleccione en _Contents_ la capa _VEREDA_, en la parte superior podrá observar que se activan opciones específicas para esta capa, vaya al menú _Labeling_ y establezca el rotulado de la capa utilizando a partir del nombre de la vereda.

<div align="center"><img src="graph/ArcGISPro_LayerLabelBasic.png" alt="R.SIGE" width="100%" border="0" /></div>

5. En el panel _Contents_, seleccione la capa, abra la tabla de atributos u oprima <kbd>Ctrl</kbd>+<kbd>T</kbd> y con la opción _Add_ agregue los siguientes campos y guarde las modificaciones realizadas en la tabla cerrando la ventana de modificación o mediante la opción guardar o _Save_ que aparece en el menú superior:

<div align="center">

| Campo | Descripción                   | Tipo    | Propiedad ArcGIS Pro        | 
|-------|-------------------------------|---------|-----------------------------| 
| APha  | Área planar en hectáreas      | Double  | Area                        |
| AGha  | Área geodésica en hectáreas   | Double  | Area (geodesic)             |
| PPm   | Perímetro planar en metros    | Double  | Perimeter length            |
| PGm   | Perímetro geodésico en metros | Double  | Perimeter length (geodesic) |

</div>

> Tenga en cuenta que al crear los campos no se calculan automáticamente estas propiedades geométricas.  
> Los valores planares corresponden a los calculados a partir de la proyección de la capa sobre un plano horizontal.  
> Los valores geodésicos corresponden a los calculados teniendo en cuenta la curvatura terrestre.

<div align="center"><img src="graph/ArcGISPro_TableAddField.png" alt="R.SIGE" width="100%" border="0" /></div>

En la tabla podrá observar que esta capa se compone de 14 entidades o veredas.

6. En la tabla de atributos y dando clic sobre el campo `APha`, seleccione la opción _Calculate Geometry_ que le permitirá calcular las propiedades geométricas asociadas a las entidades.

<div align="center"><img src="graph/ArcGISPro_CalculateGeometry.png" alt="R.SIGE" width="100%" border="0" /></div>

Calcule las propiedades solicitadas indicando las unidades de cálculo y el sistema de proyección 9377, correspondiente a MAGNA Orígen Único Nacional de Colombia.

> En actividades anteriores evidenciamos que el sistema de proyección de coordenadas de las capas recopiladas del POT es el 3116, correspondiente a MAGNA Sirgas Orígen Bogotá.  
> Tenga en cuenta que el cálculo de las propiedades geométricas puede variar entre sistemas de coordenadas, por lo cual, los valores calculádos automáticamente (por estar contenida la capa dentro de una GDB) en esta capa en los campos Shape_Area y Shape_length (a partir del CRS 3116), son diferentes a los obtenidos con el sistema 9377.

Incluya un campo adicional tipo entero largo con el nombre `Nodos` y desde el editor de geometría, calcule el número de nodos que componen cada entidad, utilizando para ello la propiedad geométrica número de vértices (_Number of Vertices_).

<div align="center"><img src="graph/ArcGISPro_CalculateGeometryRun.png" alt="R.SIGE" width="100%" border="0" /></div>

> :bulb:Recuerde que luego de incluir o modificar campos de atributos en tablas o capas, estos deben ser documentados en el diccionario de datos.

<div align="center"><img src="graph/ArcGISPro_Table1.png" alt="R.SIGE" width="100%" border="0" /></div>

7. Modifique el rótulo agregando el campo de área y perímetro geodésico, utilice una de las siguientes expresiones:

| Lenguaje | Sentencia                                                                                                                                       |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Arcade   | `$feature.nombre + textformatting.NewLine + "A (ha): " + Round($feature.AGha, 2) + textformatting.NewLine + "P (m):" + Round($feature.PGm, 2)`  |
| VBScript | `[nombre] & VbNewLine & "A (ha): " & Round([AGha],2) & VbNewLine & "P (m):" & Round([PGm], 2)`                                                  |
| Python   | `[nombre] + "\nA (ha): " + str(round(float([AGha]), 2)) + "\nP (m):" + str(round(float([PGm]), 2))`                                             |
| JScript  | `[nombre] + "\nA (ha): " + parseFloat([AGha]).toFixed(2) + "\nP (m):" + parseFloat([PGm]).toFixed(2)`                                           |


<div align="center"><img src="graph/ArcGISPro_LabelAdvanced1.png" alt="R.SIGE" width="100%" border="0" /></div>

8. En el panel lateral *Contents*, de clic derecho en _VEREDA_ y seleccione la opción _Create Chart / Bar Chart_, cree una gráfica en orden descendente para los valores de área geográfica, podrá observar que la vereda Páramo de Guerrero es la de mayor extensión.

<div align="center"><img src="graph/ArcGISPro_Vereda1Chart.png" alt="R.SIGE" width="100%" border="0" /></div>


### 1.2. Mapa veredal a partir de predios diagnóstico POT año 2010

Para iniciar, en el panel lateral _Contents_, apague la capa VEREDA.

1. Desde la misma ruta anterior _\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\gdb\25899.gdb\Rural\_, agregue la clase de entidad _TERRENO_PREDIO_RURAL_. Cambie la simbología a polígonos sin relleno.

<div align="center"><img src="graph/ArcGISPro_AddLayer_TerrenoPredioRural.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Abra la tabla de atributos e identifique el campo que contiene el código de identificación de vereda y cambie la simbología de representación de símbolo simple a valores únicos utilizando este campo. Podrá observar que los polígonos de predios de una misma vereda tienen el mismo color.

<div align="center"><img src="graph/ArcGISPro_Symbology_UniqueValues_TerrenoPredioRural.png" alt="R.SIGE" width="100%" border="0" /></div>

3. En el menú superior, de clic en el grupo _Analysis_ y de clic en _Tools_. Podrá observar que a la derecha aparece el panel _Geoprocessing_. En el campo de búsqueda, ingrese la palabra _Dissolve_, obtendrá diferentes resultados.

<div align="center"><img src="graph/ArcGISPro_Geoprocessing_Dissolve.png" alt="R.SIGE" width="100%" border="0" /></div>

4. En la ventana de resultados, seleccione la herramienta _Dissolve_ asociada al grupo _Data Management Tools_ e ingrese los parámetros definidos en la siguiente imagen. Nombre la capa como _Vereda_DiagnosticoPOT_TerrenoPredioRural.shp_

> Para la ruta de salida de todas las capas en formato shapefile a generar en este curso, utilizaremos la ruta _\R.SIGE\file\shp_.

<div align="center"><img src="graph/ArcGISPro_Geoprocessing_Dissolve_TerrenoPredioRural.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_Geoprocessing_Dissolve_TerrenoPredioRural_Zoom.png" alt="R.SIGE" width="100%" border="0" /></div>

> Como puede observar, se han creado 14 veredas, sin embargo, contienen regiones internas vacías debidas a los corredores viales que no se incluyen en las capas de predios catastrales como unidades prediales, por lo que será necesario editar la geometría de la capa y eliminar manualmente los nodos internos para crear una región contínua. Para este ejercicio, no eliminaremos estos nodos internos.

5. En la tabla de contenido, desplace el mapa _VEREDA_ y ubíquelo sobre el mapa de veredas creadas a partir de predios, podrá observar que existe correspondencia exterior en casi todas las zonas.

<div align="center"><img src="graph/ArcGISPro_Geoprocessing_Dissolve_TerrenoPredioRural_Check1.png" alt="R.SIGE" width="100%" border="0" /></div>

> Se recomienda recorrer todos los bordes perimetrales e identificar en que zonas existen diferencias importantes entre estas dos capas.

6. En la tabla de atributos, agregue los campos requeridos (APha, AGha, PPm, PGm, Nodos) y realice los cálculos geométricos utilizando el CRS 9377. 

Rotule la capa de veredas utilizando la expresión Arcade: `$feature.vereda_id + textformatting.NewLine + "A (ha): " + Round($feature.AGha, 2) + textformatting.NewLine + "P (m):" + Round($feature.PGm, 2)` 

> En la tabla de atributos podrá observar que a partir de la disolución hemos obtenido el conteo de predios en cada vereda, encontrando que la vereda Paso Ancho es la que tiene el mayor número de divisiones prediales con 2775 predios.

<div align="center"><img src="graph/ArcGISPro_LabelAdvanced2.png" alt="R.SIGE" width="100%" border="0" /></div>

> Como observa en la imagen, los valores de área de las veredas calculadas previamente son diferentes a los obtenidos a partir de predios. Para conocer el área correspondiente a vías + corredores de cauces + espacios públicos sin predio catastral, puede restar los valores de estas dos áreas.

En la tabla podrá observar que esta capa también se compone de 14 entidades o veredas.

<div align="center"><img src="graph/ArcGISPro_Table2.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_Vereda2Chart.png" alt="R.SIGE" width="100%" border="0" /></div>


### 1.3. Mapa veredal formulación POT año 2013

Desde la ruta _\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\shp\_, agregue la capa vectorial shapefile _VEREDA.shpL_, cambie la simbología, agregue y calcule los campos de atributos, y realice la rotulación. Siga el mismo procedimiento realizado en el numeral 1.1 de esta actividad.

Rótulo Arcade: `$feature.nombre + textformatting.NewLine + "A (ha): " + Round($feature.AGha, 2) + textformatting.NewLine + "P (m):" + Round($feature.PGm, 2)`

> Para diferenciar las capas de veredas, utilice diferentes colores de borde y desde la tabla de contenido renombre las capas. Por ejemplo, la capa _VEREDA_ de la formulación puede ser renombrada como _Veredas (2013 formulación POT)_. 

<div align="center"><img src="graph/ArcGISPro_LabelAdvanced3.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_Table3.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_Vereda3Chart.png" alt="R.SIGE" width="100%" border="0" /></div>


### 1.5. Mapa veredal DANE 2022

1. Desde la plataforma de https://www.colombiaenmapas.gov.co/, descargue la capa de veredas en formato shapefile de Colombia creada por el DANE. Obtendrá un archivo comprimido, descomprima y guarde en la carpeta _\R.SIGE\file\data\DANE\_ de su repositorio de datos. 

> Para la descarga se requiere de inicio de sesión de usuario utilizando por ejemplo una cuenta activa de Google.

<div align="center"><img src="graph/ColombiaMapa1.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ColombiaMapa2.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Desde la ruta de descompresión, cargue la capa de veredas de Colombia al mapa, cambie la simpobología de representación y abra la tabla de atributos.

<div align="center"><img src="graph/ArcGISPro_AddLayer_VeredaDANE.png" alt="R.SIGE" width="100%" border="0" /></div>

> En la tabla de atributos podrá observar que existen diferentes campos asociados a los municipios de Colombia.

3. Desde la tabla de contenido, de clic derecho en la capa y seleccione la opción de propiedades, de clic en la pestaña de creación de consultas o _Definition Query_ y establezca un filtro para nombre de municipio igual a Zipaquirá.

Query filter: `NOMB_MPIO = 'ZIPAQUIRÁ'`

Podrá observar que se obtienen 14 resultados correspondientes a las veredas del municipio del caso de estudio.

<div align="center"><img src="graph/ArcGISPro_QueryBuilder_VeredaDANE.png" alt="R.SIGE" width="100%" border="0" /></div>










### 1.4. Análisis de diferencias encontradas





https://www.colombiaenmapas.gov.co


### 


> Como observa, el área urbana no esta incluída en los límites geográficos de la capa, sin embargo, podrá calcular su área restando


## Elementos a incluir en el diccionario de datos

| Nombre                                       | Descripción                                                                                                                           | Geometría   | Registros | 
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------|-----------| 
| Vereda_DiagnosticoPOT_TerrenoPredioRural.shp | Veredas generadas a partir de la capa de predios \R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\gdb\RURAL\25899.gdbTERRENO_PREDIO_RURAL | Polígono 2D | 14        | 





## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad     | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P1** | Para su caso de estudio, evalúe las capas de veredas del diagnóstico y la formulación.                                                                                                                                                                                                                                                                                                                                                              | 
| Avance **P1** | A partir de la base predial utilizada en el diagnóstico y la formulación, cree la capa de veredas.                                                                                                                                                                                                                                                                                                                                                  | 
| Avance **P1** | Utilizando la base de datos predial más reciente, cree la capa de veredas.                                                                                                                                                                                                                                                                                                                                                                          | 
| Avance **P1** | Descargue y extraiga las veredas a partir de la última versión DANE disponible.                                                                                                                                                                                                                                                                                                                                                                     | 
| Avance **P1** | Compare todos los límites veredales obtenidos e identifique y evalúe en que zonas se han realizado mutaciones de suelo rural a urbano.                                                                                                                                                                                                                                                                                                              | 
| Avance **P1** | Cree diferentes perímetros urbanos a partir de la capas veredales y utilizando el mapa del modelo de ordenamiento territorial vigente, analice y explique sus diferencias.                                                                                                                                                                                                                                                                          | 
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

| [:arrow_backward: Anterior](../POTLayer/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|--------------------------------------------|-------------------|---------------------------------------------------------------------------|---------------|

[^1]: 