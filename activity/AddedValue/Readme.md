# Identificación de predios en plusvalía por cambio de clasificación o categoría de suelo
Keywords: `land-added-value` `land-appreciation` `land-betterment`

A partir de la combinación de predios con el mapa del Modelo de Ocupación Territorial - MOT, se realiza la identificación de predios rurales con cambio de categoría a expansión urbana, suburbano o urbano y/o por modificación de la zonificación de usos del suelo.

<div align="center"><img src="graph/Gravity_anomalies_on_Earth.png" alt="R.SIGE" width="100%" border="0" /><sub><br>Tomado de: <a href="Public Domain, https://commons.wikimedia.org/w/index.php?curid=479365">https://commons.wikimedia.org</a></sub><br><br></div>

En esta actividad, utilizaremos como referencia la zonificación urbana y rural definida en los registros catastrales de predios del IGAC, utilizados en el diagnóstico del estudio del Plan de Ordenamiento Territorial de la zona de estudio, e identificaremos a partir del cruce con el mapa del Modelo de Ocupación Territorial, los predios objeto de plusvalía por el efecto del primer hecho generador, correspondiente a la incorporación de suelo rural a suelo de expansión urbana o la consideración de parte del suelo rural como suburbano.

> :blue_heart:Para la evaluación del efecto plusvalía en su caso de estudio, se recomienda obtener la cartografía (predios, mapas de zonificación y bases de datos) de la primera adopción del plan de ordenamiento territorial y la siguiente correspondiente a la revisión y ajustes del POT; utilizando estos dos insumos, podrá identificar los predios objeto de plusvalía.


## Objetivos

* 


## Requerimientos

* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:toolbox:Herramienta](https://www.microsoft.com/es/microsoft-365/excel?market=bz): Microsoft Excel 365.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.
* [:open_file_folder:PoblacionDANE.xlsx](Plusvalia.xlsx): libro con hechos generadores y homologación de clasificación y categorías del suelo.


## 1. Conceptos generales de plusvalía

Según el Capítulo IX y el Artículo 73 de la Ley 388 de 1997 de Colombia y de conformidad con lo dispuesto por el artículo 82 de la Constitución Política, las acciones urbanísticas que regulan la utilización del suelo y del espacio aéreo urbano incrementando su aprovechamiento, generan beneficios que dan derecho a las entidades públicas a participar en las plusvalías resultantes de dichas acciones. Esta participación se destinará a la defensa y fomento del interés común a través de acciones y operaciones encaminadas a distribuir y sufragar equitativamente los costos del desarrollo urbano, así como al mejoramiento del espacio público y, en general, de la calidad urbanística del territorio municipal o distrital. Los concejos municipales y distritales establecerán mediante acuerdos de carácter general, las normas para la aplicación de la participación en la plusvalía en sus respectivos territorios.

Hechos generadores (adaptado para el desarrollo de esta actividad)

| # | Hecho                                                                                                                                                        | Aplicabilidad                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Incorporación de suelo rural a suelo de expansión urbana o la consideración de parte del suelo rural como suburbano.                                         | Cambio de clasificación de uso                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2 | Establecimiento o modificación del régimen o la zonificación de las subcategorías de usos del suelo, cuando se autorice el cambio de uso a uno más rentable. | Modificación de la zonificación de las categorías o subcategorías de uso.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 3 | Autorización de un mayor aprovechamiento del suelo en edificación, bien sea elevando el índice de ocupación o el índice de construcción, o ambos a la vez.   | Mayor edificabilidad, identificable en las fichas urbanísticas, entre la adopción inicial y la revisión y/o ajuste del POT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 4 | Participación por ejecución de obras públicas.                                                                                                               | Aunque no es un hecho generador directo, se puede evaluar el efecto plusvalía cuando se ejecuten obras públicas previstas en el plan de ordenamiento territorial o en los planes parciales o en los instrumentos que los desarrollen, y no se haya utilizado para su financiación la contribución de valorización, las correspondientes autoridades distritales, municipales o  metropolitanas ejecutoras, podrán determinar el mayor valor adquirido por los predios en razón de tales obras, y liquidar la participación que corresponde al respectivo municipio, distrito o área metropolitana. |

> El número total de metros cuadrados que se considerará como objeto de la participación en la plusvalía será, para el caso de cada inmueble, igual al área total del mismo destinada al nuevo uso o mejor aprovechamiento, descontada la superficie correspondiente a las cesiones urbanísticas obligatorias para espacio público de la ciudad, así como el área de eventuales afectaciones sobre el inmueble en razón del plan vial u otras obras públicas, las cuales deben estar contempladas en el plan de ordenamiento o en los instrumentos que lo desarrollen.
>
> :bulb:En este ejercicio, evaluaremos el hecho generador 1 correspondiente a la incorporación de suelo rural a suelo de expansión urbana o la consideración de parte del suelo rural como suburbano.  


## 2. Procedimiento general

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _Plusvalia_ y establezca el CRS 9377. Agregue al mapa la capa del Modelo de Ocupación Territorial - MOT (_MOT.shp_), la capa de predios rurales (TERRENO_PREDIO_RURAL) y predios urbanos (TERRENO_PREDIO_URBANO) disponibles en la información recopilada del POT en la ruta `\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\shp\`, ajuste la simbología del MOT a valores únicos representando el campo de atributos `SUELO` y rotule usando el mismo campo. Establezca simbología única en los predios utilizando solo su contorno. 

<div align="center">
Ajuste los colores del mapa utilizando los siguientes valores hexadecimales.<br>

| Categoría        | HEX color |
|------------------|-----------|
| Urbano           | #CDCDCD   |
| Expansión urbana | #D69DBE   |
| Suburbano        | #D6C29F   |
| Protección       | #74B273   |
| Rural            | #FFEABE   |

</div>

> :bulb:Como los colores ya fueron definidos en el mapa de la actividad anterior, puede copiar y pegar la capa incluyendo colores y rótulos.

<div align="center"><img src="graph/ArcGISPro_AddLayer1.png" alt="R.SIGE" width="100%" border="0" /></div>

2. 





## 3. Análisis usando software libre - QGIS

Para el desarrollo de las actividades desarrolladas en esta clase, se pueden utilizar en QGIS las siguientes herramientas o geo-procesos:

| Proceso                                                                                                         | Procedimiento                                                                                                                                                                                                                                   |
|:----------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Simbología                                                                                                      | Modificable desde las propiedades de la capa en la pestaña _Symbology_.                                                                                                                                                                         |
| Rotulado                                                                                                        | Modificable desde las propiedades de la capa en la pestaña _Labels_.                                                                                                                                                                            |

Ejemplo rótulo en QGIS: `'A(ha): ' ||  round("AGha", 2) || '\n' || 'P (m): ' ||  round("PGm", 2) `


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
| Avance **P2** | Esta actividad no requiere del desarrollo de elementos en el avance del proyecto final, los contenidos son evaluados en el quiz de conocimiento y habilidad.                                                                                                                                                                                                                                                                                        | 
| Avance **P2** | :compass:Mapa digital impreso _P1-1: xxxx_<br>(Incluir xxxxx. Embebidos dentro del informe final como una imágen y referenciados como anexo.                                                                                                                                                                                                                                                                                                        | 
| Avance **P2** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas. | 

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Referencias

* [Ley 388 de 1998, Colombia.](http://www.secretariasenado.gov.co/senado/basedoc/ley_0388_1997.html)



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