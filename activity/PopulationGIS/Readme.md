# Representación geográfica de población, densidad poblacional, espacio público efectivo (EPE) y demanda de servicios públicos
Keywords: `population-gis` `public-space` `epe` `water-demand` `water-return` `proportional-symbol` `time-view` `dynamic-view`

A partir de la delimitación de límites geopolíticos internos y utilizando los datos de población proyectada, crear una representación visual dinámica de su crecimiento y la demanda de espacio público efectivo y servicios públicos domiciliarios.                          

<div align="center"><img src="graph/PopulationGIS.png" alt="R.SIGE" width="100%" border="0" /><sub><br>Tomado de: <a href="Public Domain, https://commons.wikimedia.org/w/index.php?curid=479365">https://commons.wikimedia.org</a></sub><br><br></div>


## Objetivos

* Representar el crecimiento poblacional municipal en el suelo urbano y rural definido en el Modelo de Ocupación Territorial - MOT, a partir de datos estadísticos y de proyección poblacional.
* Estimar el espacio público efectivo - EPE requerido en la zona urbana a partir de datos de población.
* Estimar la demanda de servicios de agua potable y retorno en aguas servidas residenciales.


## Requerimientos

* [:mortar_board:Actividad](../Population/Readme.md): Estudio poblacional: censos y proyecciones
* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:toolbox:Herramienta](https://www.microsoft.com/es/microsoft-365/excel?market=bz): Microsoft Excel 365.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.
* [:open_file_folder:PoblacionDANE_GIS.xlsx](PoblacionDANE_GIS.xlsx): libro para registro, distribución urbana y rural de población DANE censal y proyectada, cálculo de índices y caudales.


## 1. Obtención de polígono urbano y rural POT

1. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _PopulationGIS_ y establezca el CRS 9377. Agregue al mapa la capa del Modelo de Ocupación Territorial - MOT disponible en la información recopilada del POT en la ruta `\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\shp\MOT.shp` y ajuste la simbología a valores únicos representando el campo de atributos `SUELO`.  

<div align="center"><img src="graph/ArcGISPro_SymbologyUniqueValues_MOT_Suelo.png" alt="R.SIGE" width="100%" border="0" /></div>

2. Utilizando la herramienta _Data Management Tools / Dissolve_, disuelva los polígonos del Modelo de Ocupación Territorial - MOT a partir del campo de atributos `SUELO`. Guarde la capa o clase de entidad resultante dentro de la base de datos GDB temporal del mapa con el nombre `\file\map\ArcGISPro\ArcGISPro.gdb\MOT_UrbanoRural_Dissolve` y abra la tabla de atributos de la capa inicial y la capa disuelta. Podrá observar que de los 80 polígonos iniciales, hemos obtenido 5 zonas.

> El almacenamiento de la capa dentro de la GDB del mapa actual, le permitirá posteriormente realizar uniones de multiples registros y visualizaciones temporales.

<div align="center"><img src="graph/ArcGISPro_MOT_UrbanoRural_Dissolve_shp.png" alt="R.SIGE" width="100%" border="0" /></div>

3. Para la obtención de los polígonos, urbano (urbano y expansión) y rural (rural, protección y suburbano), es necesario realizar ahora una unión de entidades o Merge.

En la tabla de atributos de la capa disuelta, seleccione los registros correspondientes a urbano y expansión. Utilice la tecla <kbd>Shift</kbd> o la tecla <kbd>Ctrl</kbd> para la selección.

En el menú superior, de clic en _Edit_, expanda el grupo de opciones _Tools_ y seleccione la herramienta _Merge_.

<div align="center"><img src="graph/ArcGISPro_MOT_Merge1.png" alt="R.SIGE" width="100%" border="0" /></div>

En el panel lateral derecho, de clic en el botón _Merge_ para aceptar la fusión manual de estas dos áreas. En la tabla de atributos, modifique el nombre a _Urbano_ y rotule a partir del campo `SUELO`.

<div align="center"><img src="graph/ArcGISPro_MOT_Merge2.png" alt="R.SIGE" width="100%" border="0" /></div>

Repita el procedimiento anterior para integrar los polígonos _Rural, Protección y Suburbano_ y nombre como _Rural_. Ajuste la simpología para obtener una visualización adecuada.

<div align="center"><img src="graph/ArcGISPro_MOT_Merge3.png" alt="R.SIGE" width="100%" border="0" /></div>

> Como puede observar, el área urbana se compone de dos partes y en la tabla de atributos solo aparece un registro, este tipo de geometría se denomina _multiparte_. También podrá observar que en la zona rural existen rebordes internos correspondientes a errores de digitalización.

4. Utilizando el editor de vértices, elimine los nodos internos de la zona rural correspondientes a errores de digitalización o de construcción de la capa. Una vez eliminados, de clic en _Save_ en el menu _Edit_.

<div align="center"><img src="graph/ArcGISPro_MOT_EditVertices.png" alt="R.SIGE" width="100%" border="0" /></div>


## 2. Distribución de población censal urbana y rural

A partir de la información censal analizada en la actividad [Estudio poblacional: censos y proyecciones](../Population/Readme.md), se obtuvieron solo los datos consolidados de población del municipio, pero sin distinción en urbano o rural. En la tabla de recopilación de información SISBEN, registramos en 2000 y 2018, datos distribuídos de población por zonas en urbano, rural y centros poblados rurales; a partir de los porcentajes de distribución de estos valores, realizaremos la distribución de los datos censales DANE, tal como se muestra en el libro de Excel suministrado.

En la tabla de población del libro de Microsoft Excel suministrado para el desarrollo de esta actividad, se han incluído los siguientes atributos:

<div align="center">

| Columna | Descripción                                            |
|:--------|:-------------------------------------------------------|
| PTotal  | Población total municipal                              |
| PorcUrb | Porcentaje de población correspondiente al área urbana |
| PUrbana | Población urbana = población total por % urbano        |
| PRural  | Población rural = población total - población urbana   |

</div>

<div align="center"><img src="graph/Excel_PoblacionPorcentajeDistribucion.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/Excel_PoblacionDistribuida.png" alt="R.SIGE" width="70%" border="0" /></div>
<div align="center"><img src="graph/Excel_PoblacionDistribuidaChart.png" alt="R.SIGE" width="100%" border="0" /></div>


## 3. Análisis de densidad poblacional

Para el análisis de densidad poblacional, es necesario tener en cuenta la mutación del suelo rural a urbano a través del tiempo. Para este análisis, utilizaremos la población proyectada y las áreas obtenidas a partir del análisis realizado previamente a partir de las veredas DANE 2020.

En la tabla de población del libro de Microsoft Excel suministrado para el desarrollo de esta actividad, se han incluído los siguientes atributos:

<div align="center">

| Columna   | Descripción                                                                                                                                                               |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AreaUrbPL | Tamaño del área urbana en hectáreas a partir del total del área municipal menos el área rural.                                                                            |
| AreaRurPL | Tamaño del área rural en hectáreas proyectada linealmente. Utilizando la regresión, al menos se debe reservar 1 ha de suelo urbano para realizar los cálculos requeridos. |
| DensTotal | Densidad total municipal en habitantes / hectárea: población total / área total municipal.                                                                                |
| DensUrb   | Densidad urbana en habitantes / hectárea: población urbana / área urbana                                                                                                  |
| DensRur   | Densidad rural en habitantes / hectárea: población rural / área rural                                                                                                     |

</div>

<div align="center"><img src="graph/Excel_TipoSueloTendencia.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/Excel_DensidadPoblacional.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/Excel_DensidadPoblacionalChart.png" alt="R.SIGE" width="100%" border="0" /></div>


## 4. Análisis de espacio público efectivo urbano requerido - EPE

De acuerdo al [Ministerio de Vivienda de Colombia](https://minvivienda.gov.co/proyectos-de-espacio-urbano-y-territorial-sgr/espacio-publico), el índice mínimo efectivo de espacio público es de 15m² por habitante. Este indicador establece la relación entre el Espacio Público Efectivo frente a la población habitante; se define Espacio Público Efectivo como el “espacio público de carácter permanente, conformado por zonas verdes, parques, plazas y plazoletas”. [Documento CONPES 3718](https://www.minambiente.gov.co/wp-content/uploads/2021/10/Conpes-3718-de-2012.pdf), Bogotá 2012.

Este indicador muestra la suficiente o insuficiente disponibilidad de espacio público susceptible a la medición del déficit cuantitativo del espacio público de carácter permanente - Artículo 12 Decreto 1504 de 1998. El artículo 14 del mismo Decreto considera como índice mínimo de Espacio Público Efectivo de 15m².

Según la Organización Mundial de la Salud (OMS) el agrupamiento de las viviendas en zonas verdes y el fomento de vías peatonales mejoran la calidad del aire y estimulan la actividad física, al tiempo que reducen las lesiones y los efectos de la isla de calor urbana. De tal forma, dicha Organización fijó un indicador óptimo entre 10 m² y 15 m² de zonas verdes por habitante, con el fin de que estos mitiguen los impactos generados por la contaminación de las ciudades y cumplan una función de amortiguamiento. [^1]

En la tabla de población del libro de Microsoft Excel suministrado para el desarrollo de esta actividad, se han incluído los siguientes atributos:

<div align="center">

| Columna   | Descripción                                                                           |
|:----------|:--------------------------------------------------------------------------------------|
| EPEUrbHa  | Espacio público efectivo urbano requerido en ha: población urbana * 15 / 10000 |

</div>

<div align="center"><img src="graph/Excel_EPE.png" alt="R.SIGE" width="60%" border="0" /></div>
<div align="center"><img src="graph/Excel_EPEChart.png" alt="R.SIGE" width="100%" border="0" /></div>

> Este indicador también puede ser estimado para centros poblados en la implementación de planes parciales.


## 5. Análisis de demanda de agua potable y aguas servidas residenciales

Para la estimación del caudal total demandado de agua potable, utilizaremos como referencia los valores de dotación neta por habitante, establecidos en el [Título B del Reglamento Técnico del Sector de Agua Potable y Sanemamiento Básico - RAS](https://www.minvivienda.gov.co/sites/default/files/documentos/titulob-030714.pdf) de Colombia que hace parte de la Resolución 1096 del 17 de Noviembre de 2000. Para la estimación de los caudales domésticos retornados al sistema de alcantarillado utilizaremos los valores de referencia establecidos en el [Título D](https://www.minvivienda.gov.co/sites/default/files/documentos/titulo_d.pdf) del mismo reglamento.

> :bulb:Tenga en cuenta que la Resolución 0330 de 2017, por medio del cual se actualizó el reglamento de agua potable y saneamiento básico - RAS, ajustó los rangos de elevación de la zona estudio a partir de los cuales se definen los valores correspondientes a las dotaciones netas y coeficientes de retorno. Posteriormente y mediante la Resolución 799 de 2021, se realizaron ajustes complementarios a estas normas.

En la tabla de población del libro de Microsoft Excel suministrado para el desarrollo de esta actividad, se han incluido los siguientes atributos:

<div align="center">

| Columna   | Descripción                                                                                                                         |
|:----------|:------------------------------------------------------------------------------------------------------------------------------------|
| QAcuTotal | Caudal total municipal en lps-día demandado de sistemas de acueducto: población total * dotación neta / 86400                       |
| QAcuUrb   | Caudal urbano en lps-día demandado de sistemas de acueducto: población urbana * dotación neta / 86400                               |
| QAcuRur   | Caudal rural en lps-día demandado de sistemas de acueducto: población rural * dotación neta / 86400                                 |
| QAlcTotal | Caudal total municipal en lps-día retornado a sistemas de alcantarillado: caudal total municipal demandado * coeficiente de retorno |
| QAlcUrb   | Caudal urbano en lps-día retornado a sistemas de alcantarillado: caudal urbano demandado * coeficiente de retorno                   |
| QAlcRur   | Caudal rural en lps-día retornado a sistemas de alcantarillado: caudal rural demandado * coeficiente de retorno                     |

</div>

<div align="center">Parámetros generales<br><img src="graph/Excel_AguaPotSanBas_Parameters.png" alt="R.SIGE" width="80%" border="0" /></div><br>
<div align="center">Asignación del nivel de complejidad - Título A RAS<br><img src="graph/Excel_AguaPotSanBas_NivelComplejidad.png" alt="R.SIGE" width="90%" border="0" /></div><br>
<div align="center">Dotación neta por habitante y clima - Título B RAS (L/hab/día) y coeficientes de retorno aguas residuales domésticas QD - Título D RAS<br><img src="graph/Excel_AguaPotSanBas_DotacionRetorno.png" alt="R.SIGE" width="90%" border="0" /></div><br>
<div align="center"><img src="graph/Excel_AguaPotSanBas_DotacionChart.png" alt="R.SIGE" width="50%" border="0" /></div><br>
<div align="center">Caudales demandados y retornados<br><img src="graph/Excel_AguaPotSanBas.png" alt="R.SIGE" width="100%" border="0" /></div><br>
<div align="center"><img src="graph/Excel_AguaPotBasChart.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/Excel_AguaRetornadaChart.png" alt="R.SIGE" width="100%" border="0" /></div>

> Se considera como clima cálido aquella zona del territorio nacional que se encuentre por debajo de 1000 m.s.n.m. 


## 6. Visualización dinámica en ArcGIS Pro

1. Para la visualización en GIS, es necesario crear una copia de la tabla de población, organizando de forma apilada los resultados obtenidos. Para ello, es necesario crear una columna adicional denominada `Suelo` indicando si corresponde a Total, Urbano o Rural y ajustar la columna fecha incluyendo el día y el mes (`=CONCAT(C2,"/12/31")`).

> Los valores de densidad urbana entre los años 1905 y 1973, han sido modificados incluyendo el valor obtenido en 1985. Lo anterior debido a que a partir de la regresión, no se obtuvieron valores positivos urbanos.

<div align="center"><img src="graph/Excel_PoblacionGIS.png" alt="R.SIGE" width="70%" border="0" /></div>

2. En el mapa de ArcGIS Pro y desde el panel de catálogo localizado a la derecha, seleccione el archivo de Excel _PoblacionDANE_GIS.xlsx_ desde la ruta mostrada, expanda su contenido y seleccione la hoja _PoblacionGIS$_.

<div align="center"><img src="graph/ArcGISPro_ExcelDataPoblacionGIS.png" alt="R.SIGE" width="100%" border="0" /></div>

3. De clic derecho en la hoja _PoblacionGIS_ del libro de Excel y seleccione la opción _Export / Table to Table_.

<div align="center"><img src="graph/ArcGISPro_TableToTable.png" alt="R.SIGE" width="50%" border="0" /></div>

4. En _Table to Table_, en _Fields_, modifique el campo `Fecha` a formato _Date_ y defina como ruta de salida y nombre de tabla la ruta `\file\map\ArcGISPro\ArcGISPro.gdb\PopulationGIS`. Al terminar será cargada automáticamente la tabla al proyecto, abrala para verificar su contenido.

> Para utilizar campos tipo fecha y optimizar la visualización temporal de elementos, se recomienda guardar la tabla dentro de la base de datos GDB temporal del proyecto. (no requiere extensión)  
> El campo EPEUrbHa, también requiere ser ajustado a tipo numérico para su exportación.

<div align="center"><img src="graph/ArcGISPro_TableToTable1.png" alt="R.SIGE" width="100%" border="0" /></div>


5. Desde la tabla de contenido, seleccione la capa geográfica _MOT_UrbanoRural_Dissolve_, de clic derecho y seleccione la opción _Add Join_.

<div align="center"><img src="graph/ArcGISPro_AddJoin1.png" alt="R.SIGE" width="60%" border="0" /></div>

Establezca la siguiente unión, podrá observar que ahora la tabla de atributos de la disolución que tenía solo dos registros, ahora tiene 44 elementos y que los rótulos aparecen múltiples veces.

<div align="center"><img src="graph/ArcGISPro_AddJoin2.png" alt="R.SIGE" width="100%" border="0" /></div>

6. Ajuste el rótulo indicando el nombre del suelo y el valor de población.

Rótulo Arcado: `$feature['MOT_UrbanoRural_Dissolve.SUELO'] + textformatting.NewLine +"Año: "+ year($feature['PopulationGIS.Fecha']) + textformatting.NewLine +"Población: " + round($feature['PopulationGIS.Poblacion'], 0)`

<div align="center"><img src="graph/ArcGISPro_Label_Poblacion1.png" alt="R.SIGE" width="100%" border="0" /></div>

7. En la tabla de contenido, acceda a las propiedades de la capa y seleccione la pestaña _Time_, realice la configuración mostrada a continuación.

> Debido a que el intervalo de tiempo no es constante, es necesario marcar la casilla _View using unique items with the data_, esto permitirá realizar el salto de tiempo variable.

<div align="center"><img src="graph/ArcGISPro_Time1.png" alt="R.SIGE" width="60%" border="0" /></div>

En pantalla podrá observar que ahora aparece el deslizador de tiempo y que solo aparece un rótulo para cada entidad. En la parte superior de la pantalla, vaya al menu _Time_ y en la sección _Step_, seleccione la capa _MOT_UrbanoRural_Dissolve_. 

<div align="center"><img src="graph/ArcGISPro_Time2.png" alt="R.SIGE" width="100%" border="0" /></div>

Ahora, podrá activar la visualización de tiempo, observe que los rótulos y los registros de la tabla van cambiando a medida que avanza el tiempo.

8. Cambie la simbología de representación a símbolos proporcionales utilizando la variable _Población_ con símbolos entre 12 y 90 puntos de tamaño. De esta forma podrá comparar la proporcionalidad entre los valores urbanos y rurales. De clic en Play de la barra de tiempo y observe el resultado

<div align="center">Población por símbolos proporcionales<br><img src="graph/ArcGISPro_SymbologyProportional1.png" alt="R.SIGE" width="100%" border="0" /></div>

9. Realice el mismo análisis para las demás variables, modifique el rótulo incluyendo los valores de densidad, espacio público y caudales estimados.

Rótulo Arcade: `$feature['MOT_UrbanoRural_Dissolve.SUELO'] + textformatting.NewLine +"Año: "+ year($feature['PopulationGIS.Fecha']) + textformatting.NewLine +"Población: " + round($feature['PopulationGIS.Poblacion'], 0) + textformatting.NewLine + "Densidad (hab/ha): " + round($feature['PopulationGIS.Densidad'], 2) + textformatting.NewLine + "EPE (ha): " + round($feature['PopulationGIS.EPEUrbHa'], 2) + textformatting.NewLine + "QAcu (lps): " + round($feature['PopulationGIS.QAcu'], 2) + textformatting.NewLine + "QAlc (lps): " + round($feature['PopulationGIS.QAlc'], 2)`

<div align="center">Densidad por símbolos proporcionales<br><img src="graph/ArcGISPro_SymbologyProportional2.png" alt="R.SIGE" width="100%" border="0" /></div>

> Observe como la densidad urbana disminuye y como la rural se mantiene creciendo a un ritmo lento.

<div align="center">Demanda de agua potable por símbolos proporcionales<br><img src="graph/ArcGISPro_SymbologyProportional3.png" alt="R.SIGE" width="100%" border="0" /></div><br>
<div align="center">Caudal retornado a alcantarillado por símbolos proporcionales<br><img src="graph/ArcGISPro_SymbologyProportional4.png" alt="R.SIGE" width="100%" border="0" /></div>

> Observe como la demanda de servicios es creciente a través del tiempo.
>
> :bulb:Para la representación de valores totales, disuelva la capa del MOT en un único polígono o utilice los polígonos de límite territorial creados en la actividad anterior, cree un campo con el nombre `Suelo` y establezca su valor como _Total_, luego, realice la unión con la tabla de población y represente los valores obtenidos.


## 7. Análisis usando software libre - QGIS

Para el desarrollo de las actividades desarrolladas en esta clase, se pueden utilizar en QGIS las siguientes herramientas o geo-procesos:

| Proceso                                               | Procedimiento                                                                                                                                                                                                                                                                  |
|:------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Simbología                                            | Modificable desde las propiedades de la capa en la pestaña _Symbology_.                                                                                                                                                                                                        |
| Rotulado                                              | Modificable desde las propiedades de la capa en la pestaña _Labels_.                                                                                                                                                                                                           |
| Agregar campo                                         | Modificable desde las propiedades de la capa en la pestaña _Fields_ o desde la tabla de atributos.                                                                                                                                                                             |
| Disolución                                            | Se ejecuta desde el _Processing Toolbox / Vector Geometry / Dissolve_ o desde el menú _Vector / Geoprocessing Tools / [Dissolve](https://docs.qgis.org/3.34/en/docs/user_manual/processing_algs/qgis/vectorgeometry.html#dissolve)_.                                           |
| Edición geométrica para eliminación de zonas internas | Activar modo de edición en la capa o _Toggle Editing_, luego en la barra de edición seleccionar la herramienta _Vertex Tool_, oprimir y mantener la tecla <kbd>Shift</kbd>, seleccionar los nodos a eliminar, oprimir tecla <kbd>Delete</kbd>.                                 |
| Conversión de tablas                                  | Exportable desde las propiedades de la capa con _Export / Save Features As_, luego seleccionar el formato Comma Separated Values (CSV) o ESRI File Geodatabase o SpatialLite o SQLite, dependiendo de si dispone o no de una base de datos.                                    |
| Unión de tablas                                       | En las propiedades de capa geográfica, seleccionar la pestaña _Join_ y realizar la unión. Solo se mostrarán los registros correspondientes a la primer coincidencia encontrada. Para visualizar o representar otros valores, es necesario filtrar previamente la tabla a unir. |

Ejemplo rótulo en QGIS: `'A(ha): ' ||  round("AGha", 2) || '\n' || 'P (m): ' ||  round("PGm", 2) `

[:notebook:QGIS training manual](https://docs.qgis.org/3.34/en/docs/training_manual/)


## Elementos requeridos en diccionario de datos

Agregue a la tabla resúmen generada en la actividad [Inventario de información geo-espacial recopilada del POT y diccionario de datos](../POTLayer/Readme.md), las capas generadas en esta actividad que se encuentran listadas a continuación:

| Nombre                                                      | Descripción                                                                                                                       | Geometría   | Registros | 
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------|-----------| 
| \file\map\ArcGISPro\ArcGISPro.gdb\ MOT_UrbanoRural_Dissolve | Disolución polígonos MOT en área urbana y área rural.                                                                             | Polígono 2D | 2         | 
| \file\map\ArcGISPro\ArcGISPro.gdb\ PopulationGIS            | Tabla con resultados de proyección de población, área urbana y rural, densidad de población, espacio público efectivo y caudales. | N/A         | 66        | 

> :bulb:Para funcionarios que se encuentran ensamblando el SIG de su municipio, se recomienda incluir y documentar estas capas en el Diccionario de Datos.


## Actividades de proyecto :triangular_ruler:

En la siguiente tabla se listan las actividades que deben ser desarrolladas y documentadas por cada grupo de proyecto en un único archivo de Adobe Acrobat .pdf. El documento debe incluir portada (indicando el caso de estudio, número de avance, nombre del módulo, fecha de presentación, nombres completos de los integrantes), numeración de páginas, tabla de contenido, lista de tablas, lista de ilustraciones, introducción, objetivo general, capítulos por cada ítem solicitado, conclusiones y referencias bibliográficas.

| Actividad     | Alcance                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:--------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Avance **P2** | Realice el análisis de población urbana y rural, densidad, EPE y caudales desarrollado en esta actividad. En el análisis, verifique el nuevo alcance establecido en las Resoluciones 0330 de 2017 y 799 de 2021 del RAS, ajustando los valores establecidos de dotación neta y porcentaje de retorno.                                                                                                                                                 | 
| Avance **P2** | Disuelva el mapa MOT en un único polígono y realice el análisis de población total, densidad, EPE y caudales desarrollado en esta actividad.                                                                                                                                                                                                                                                                                                          | 
| Avance **P2** | Complemente la información censal poblacional de su municipio, incluyendo valores independientes en cada centro poblado rural y realice los mismos análisis realizados en esta actividad. El mapa de análisis debe contener el área urbana, el área rural excluyendo los centros poblados, y cada centro poblado en polígonos independientes. (Opcionalmente puede segmentar los análisis de la zona rural incluyendo las poblaciones de cada vereda) | 
| Avance **P2** | En una tabla y al final del informe de avance de esta entrega, indique el detalle de las sub-actividades realizadas por cada integrante de su grupo. Para actividades que no requieren del desarrollo de elementos de avance, indicar si realizo la lectura de la guía de clase y las lecturas indicadas al inicio en los requerimientos. Utilice las siguientes columnas: Nombre del integrante, Actividades realizadas, Tiempo dedicado en horas.   | 

> No es necesario presentar un documento de avance independiente, todos los avances de proyecto de este módulo se integran en un único documento.
> 
> En el informe único, incluya un numeral para esta actividad y sub-numerales para el desarrollo de las diferentes sub-actividades, siguiendo en el mismo orden de desarrollo presentado en esta actividad.


## Referencias

* [Nature Nearby - Accessible Natural Greenspace Guidance](http://www.ukmaburbanforum.co.uk/docunents/other/nature_nearby.pdf)
* https://www.minvivienda.gov.co/sites/default/files/documentos/titulob-030714.pdf
* https://www.cra.gov.co/normas-vigentes
* https://www.minvivienda.gov.co/viceministerio-de-agua-y-saneamiento-basico/reglamento-tecnico-sector/manuales


## Control de versiones

| Versión    | Descripción                                                | Autor                                      | Horas |
|------------|:-----------------------------------------------------------|--------------------------------------------|:-----:|
| 2024.07.09 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   8   |
| 2024.07.10 | Investigación y documentación para caso de estudio general | [rcfdtools](https://github.com/rcfdtools)  |   8   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../CountyLimit/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/12) | [Siguiente :arrow_forward:](../Layout/Readme.md) |
|-------------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------|--------------------------------------------------|

[^1]: Organización Mundial de la Salud. La salud en la economía verde. Los co-beneficios de la mitigación al cambio climático para la salud. Sector de la vivienda. 