# Análisis estadístico de la red vial
Keywords: `road-summary` `summarize` `merge`

A partir de las capas orden vial y red vial urbana, contenidas en los anexos de formulación del POT, realice un análisis estadístico de longitud de vías por orden vial y longitud de vías urbanas por tipo.

<div align="center"><img src="graph/RoadSummary.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Integrar y homologar los vectores y atributos de la red vial urbana y rural en una única capa.
* Editar la geometría de los elementos contenidos en las capas urbanas y rurales, eliminando tramos superpuestos.
* Crear tablas y gráficos de análisis estadístico para evaluar el orden, estado y tipo de vías. 


## Requerimientos

* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:notebook:Lectura](https://edu.gcfglobal.org/es/estadistica-basica/): Conocimientos básicos en estadística.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.


## 1. Integración y ajuste de vías urbanas y rurales

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _RoadSummary_ y establezca el CRS 9377. Agregue al mapa desde la ruta `\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\shp\` las capas VIAS_PERIMETRO_URBANO.shp, ORDEN_VIAL.shp y MOT.shp, ajuste los colores para diferenciar las vías urbanas de las rurales y en el MOT, filtre la zona urbana y de expansión. 

<div align="center"><img src="graph/ArcGISPro_SimbologyUniqueValues1.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Verifique las vías en el contorno de la zona urbana, podrá observar que varios de los tramos rurales se extienden dentro de esta zona y que en la mayoría de los casos, en la red vial urbana, ya se encuentran digitalizados. Para integrar estas dos capas en una única capa de análisis, primero crearemos una copia de las capas para editar su contenido.

Desde la tabla de contenido y utilizando la herramienta _Data / Export Features_, exporte en la carpeta `\file\data\shp\`, las capas viales como _Vial_Urbano.shp_ y _Vial_Rural.shp_, asigne desde Environments el CRS 9377. En las vías rurales, conserve únicamente los atributos `Layer`, _ORDEN_VIAL_ y `VIAS_`. En la capa Vial_Urbano, elimine los campos `OBJECTID_1`, `SHAPE_Leng` y `LONGI`.  

<div align="center"><img src="graph/ArcGISPro_ExportFeatures1.png" alt="R.SIGE" width="100%" border="0" /></div>

3. Para las dos capas, cree los siguientes campos en la tabla de atributos:

| Campo      | Descripción                      | Tipo       | Propiedad ArcGIS Pro | 
|------------|----------------------------------|------------|----------------------| 
| ZonaNombre | Rural, Urbano                    | Text (100) | N/A                  |
| NombreVia  | Nombre de la vía                 | Text (100) | N/A                  |
| LGkm       | Longitud geodésica en kilómetros | Double     | Area (geodesic)      |

<div align="center"><img src="graph/ArcGISPro_AddField1.png" alt="R.SIGE" width="100%" border="0" /></div>

4. Con el calculador de campo o _Field Calculator_, en la capa de vías urbanas, asigne _Urbano_ en el campo `ZonaNombre` y establezca para todos los elementos en el campo `NombreVia`, los valores contenidos en el campo denominado `TEXTO`. Una vez asignados los nombres, elimine el campo `TEXTO`. 

> En este momento, no es necesario calcular la longitud de cada tramo debido a que es necesario editar y ajustar las vías localizadas en el contorno del perímetro urbano.

<div align="center"><img src="graph/ArcGISPro_VialUrbanoTable1.png" alt="R.SIGE" width="100%" border="0" /></div>

5. En la capa de vías rurales, asigne _Rural_ en el campo `ZonaNombre` y asigne los nombres de las vías tomando como referencia los valores contenidos en los campos `Layer` y `VIAS_`. una vez asignados los nombres, elimine los campos `Layer` y `VIAS_`. 

<div align="center"><img src="graph/ArcGISPro_VialRuralTable1.png" alt="R.SIGE" width="100%" border="0" /></div>

6. Utilizando las herramientas de edición disponibles en el menú _Edit_, elimine o recorte los tramos duplicados y divida los tramos urbanos y rurales de cada capa, a partir de los polígonos que delimitan la zona urbana y de expansión.

> Para facilitar el trabajo de edición y ajuste, en la tabla de contenido y en _List By Selection_, deje únicamente la capa Vial_Rural activa. Luego de terminada la edición rural, deje seleccionable solo la capa urbana hasta terminar de ajustar la capa.
> 
> Otra herramienta útil en el proceso de edición, es la herramienta de encajado o _Snapping_, se encuentra disponible en el menú _Edit_, deje activo, por ejemplo, el encajado por intersección y el de vértice.

Para el ejemplo mostrado en la ilustración, es necesario recortar y eliminar el tramo de la vía rural que se encuentra dentro de la zona urbana, debido a que ya se encuentra digitalizada en la capa _Vial_Urbano_. Para ello, utilizaremos la herramienta _Divide / Split_. 

<div align="center"><img src="graph/ArcGISPro_Edit1.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_Edit2.png" alt="R.SIGE" width="100%" border="0" /></div>

Repita este mismo procedimiento sobre todas las vías rurales que están sobre o que atraviesan el contorno urbano. Una vez terminada la edición rural, proceda con la revisión de las vías urbanas, asegúrese de que las vías urbanas y rurales se empalmen a partir de los nodos finales de sus tramos. Para facilitar la edición, puede ajustar el color y grosor de las vías rurales.

En la siguiente imagen, podrá visualizar una versión preliminar de las dos capas editadas, como observa, en la capa de vías urbanas se encuentran elementos correspondientes a las vías rurales y viceversa. Se ha seleccionado y resaltado el corredor férreo, para este análisis consideraremos este eje como parte de las vías rurales, así como la vía variante a Ubaté.

<div align="center"><img src="graph/ArcGISPro_Edit3.png" alt="R.SIGE" width="100%" border="0" /></div>

Para finalizar la edición y guardar los cambios, en el menú _Edit_ de clic en el botón _Save_.

7. Integración víal en una única capa. Utilizando la herramienta _Data Management Tools / Merge_, integre las dos redes viales en una única capa. Guarde en la carpeta `\file\data\shp\` como _Red_vial.shp_. En _Environmets_, establezca el CRS 9377. Abra la tabla de atributos.

<div align="center"><img src="graph/ArcGISPro_Merge.png" alt="R.SIGE" width="100%" border="0" /></div>

8. Simbolice la capa de unión por valores únicos a partir del campo _ZonaNombre_, podrá observar que es necesario redefinir la zona en varios tramos.

<div align="center"><img src="graph/ArcGISPro_SimbologyUniqueValues2.png" alt="R.SIGE" width="100%" border="0" /></div>

Seleccione los tramos a ajustar y desde la tabla de atributos asigne la zona.

<div align="center"><img src="graph/ArcGISPro_ZonaNombre1.png" alt="R.SIGE" width="100%" border="0" /></div>

Una vez terminada la reasignación de zonas, obtendremos la siguiente visualización de la red vial.

<div align="center"><img src="graph/ArcGISPro_ZonaNombre2.png" alt="R.SIGE" width="100%" border="0" /></div>

8. Para los análisis estadísticos a realizar, es necesario completar, homologar o ajustar los atributos definidos en la tabla de la capa integrada de vías, lo anterior debido a los ajustes realizados en la edición vectorial y porque no todas las vías contienen las definiciones de Tipo, Estado, Clasificación y Orden vial. Para este ejemplo, ajustaremos solo el atributo correspondiente a orden vial.

Utilizando la herramienta de selección por atributos disponible en el menú Map, seleccione todas las vías urbanas cuyo orden vial está vacío.

<div align="center"><img src="graph/ArcGISPro_SelectByAttributes1.png" alt="R.SIGE" width="100%" border="0" /></div>

Utilizando el calculador de campo, establezca `ORDEN_VIAL = "Vía Urbana"`.

<div align="center"><img src="graph/ArcGISPro_FieldCalculator1.png" alt="R.SIGE" width="100%" border="0" /></div>

Simbolice la capa por valores únicos utilizando el campo `ORDEN_VIAL`, establezca color negro y grosor 2 para todas las vías sin orden vial. Podrá observar que las vías ajustadas por zona, no contienen orden vial. Utilizando los ordenes viales de las vías próximas, establezca el orden víal sobre estas vías.

<div align="center"><img src="graph/ArcGISPro_SimbologyUniqueValues3.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_SimbologyUniqueValues4.png" alt="R.SIGE" width="100%" border="0" /></div>

Una vez finalizada la asignación, obtendrá la siguiente visualización de la capa.

<div align="center"><img src="graph/ArcGISPro_SimbologyUniqueValues5.png" alt="R.SIGE" width="100%" border="0" /></div>


## 2. Análisis estadístico

Para la obtención de estadísticos por campo de atributo, calcule en el campo `LGkm`, la longitud geodésica (CRS 9377) de cada tramo de vía en kilómetros, utilice para ello el _Geometry Calculator_.


### 2.1. Vías por orden

Desde la tabla de contenido, renombre la capa _Red_Vial_ a _Red Vial (Orden)_. Cree gráficos de análisis:

* Barras contando el número de tramos.

<div align="center"><img src="graph/ArcGISPro_OrdenVial_Chart_Count.png" alt="R.SIGE" width="100%" border="0" /></div>

* Barras totalizando la longitud de los tramos.

<div align="center"><img src="graph/ArcGISPro_OrdenVial_Chart_Long.png" alt="R.SIGE" width="100%" border="0" /></div>

Para generar una tabla con el resultado de los análisis, desde la tabla de atributos y sobre el campo _ORDEN_VIAL_, obtenga un resumen estadístico a través de la opción _Summarize_. Nombre como `\file\data\table\Red_Vial_Orden_Stat.dbf`

<div align="center"><img src="graph/ArcGISPro_OrdenVial_Summarize1.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/ArcGISPro_OrdenVial_Summarize2.png" alt="R.SIGE" width="100%" border="0" /></div>

### 2.2. Vías por tipo

Desde la tabla de atributos, cree una copia de la capa _Red Vial (Orden)_ y nombre como _Red Vial (Tipo)_. Ajuste la simbología por valores únicos a partir del campo `TIPO`. Podrá observar que múltiples vías no tienen asignada esta propiedad. Cree gráficos de análisis.

* Barras contando el número de tramos.

<div align="center"><img src="graph/ArcGISPro_Tipo_Chart_Count.png" alt="R.SIGE" width="100%" border="0" /></div>

* Barras totalizando la longitud de los tramos.

<div align="center"><img src="graph/ArcGISPro_Tipo_Chart_Long.png" alt="R.SIGE" width="100%" border="0" /></div>


### 2.3. Vías por estado

Desde la tabla de atributos, cree una copia de la capa _Red Vial (Orden)_ y nombre como _Red Vial (Estado)_. Ajuste la simbología por valores únicos a partir del campo `ESTADO`. Podrá observar que múltiples vías no tienen asignada esta propiedad. Cree gráficos de análisis.

* Barras contando el número de tramos.

<div align="center"><img src="graph/ArcGISPro_Estado_Chart_Count.png" alt="R.SIGE" width="100%" border="0" /></div>

* Barras totalizando la longitud de los tramos.

<div align="center"><img src="graph/ArcGISPro_Estado_Chart_Long.png" alt="R.SIGE" width="100%" border="0" /></div>


## 2. Análisis usando software libre - QGIS

Para el desarrollo de las actividades desarrolladas en esta clase, se pueden utilizar en QGIS las siguientes herramientas o geo-procesos:

| Proceso                                          | Procedimiento                                                                                                                                                                                                                                                         |
|:-------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Simbología                                       | Modificable desde las propiedades de la capa en la pestaña _Symbology_.                                                                                                                                                                                               |
| Rotulado                                         | Modificable desde las propiedades de la capa en la pestaña _Labels_.                                                                                                                                                                                                  |
| Edición geométrica para eliminación de elementos | Activar modo de edición en la capa o _Toggle Editing_, luego en la barra de edición seleccionar la herramienta _Vertex Tool_, oprimir y mantener la tecla <kbd>Shift</kbd>, seleccionar los nodos a eliminar, oprimir tecla <kbd>Delete</kbd>.                        |
| Fraccionar o segmentar una entidad (Split)       | Activar el modo de edición de la capa y activar la barra _[Advanced Digitizing Toolbar](https://docs.qgis.org/3.34/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html#advanced-digitizing)_ y las herramientas_Slipt Features_ o _Split Parts_. |
| Resumen estadístico (Summarize)                  | Disponible en _Processing Toolbox / Vector Analysis / [Statistics by categories](https://docs.qgis.org/3.34/en/docs/user_manual/processing_algs/qgis/vectoranalysis.html#statistics-by-categories)_.                                                                  |

Ejemplo rótulo en QGIS: `'A(ha): ' ||  round("AGha", 2) || '\n' || 'P (m): ' ||  round("PGm", 2) `


## Elementos requeridos en diccionario de datos

Agregue a la tabla resúmen generada en la actividad [Inventario de información geo-espacial recopilada del POT y diccionario de datos](../POTLayer/Readme.md), las capas generadas en esta actividad que se encuentran listadas a continuación:

| Nombre          | Descripción                                                                                              | Geometría | Registros | 
|-----------------|----------------------------------------------------------------------------------------------------------|-----------|-----------| 
| Vial_Urbano.shp | Copia depurada de la capa VIAS_PERIMETRO_URBANO.shp, utilizada en la formulación del POT.                | Línea 2D  | 764       | 
| Vial_Rural.shp  | Copia depurada de la capa ORDEN_VIAL.shp, utilizada en la formulación del POT.                           | Línea 2D  | 775       | 
| Red_vial.shp    | Integración de red vial urbana y rural a partir de las capas depuradas Vial_Urbano.shp y Vial_Rural.shp. | Línea 2D  | 1541      | 

> :bulb:Para funcionarios que se encuentran ensamblando el SIG de su municipio, se recomienda incluir y documentar estas capas en el Diccionario de Datos.


## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad     | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P1** | Esta actividad no requiere del desarrollo de elementos en el avance del proyecto final, los contenidos son evaluados en el quiz de conocimiento y habilidad.                                                                                                                                                                                                                                                                                        | 
| Avance **P1** | :compass:Mapa digital impreso _P1-1: xxxx_<br>Incluir xxxxx.<br>Embebido dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                                                                                                                                      | 
| Avance **P1** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. | 

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Referencias

* https://docs.qgis.org/3.34/en/docs/user_manual/processing_algs/qgis/vectoranalysis.html#statistics-by-categories
* https://docs.qgis.org/3.34/en/docs/user_manual/working_with_vector/editing_geometry_attributes.html#advanced-digitizing


## Control de versiones

| Versión    | Descripción                                                | Autor                                      | Horas |
|------------|:-----------------------------------------------------------|--------------------------------------------|:-----:|
| 2024.02.24 | Versión inicial con alcance de la actividad                | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.06.27 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   8   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../AddedValue/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/99999) | [Siguiente :arrow_forward:]() |
|------------------------------------------------------|-----------------------------------|--------------------------------------------------------------------------------------|-------------------------------|

[^1]: 