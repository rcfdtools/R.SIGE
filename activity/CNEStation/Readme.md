# Estudio de redes hidro-climatológicas
Keywords: `ideam` `weather-station` `display-xy-Data` `buffer` `merge` `bar-graph` `select-by-location` `statistics`

A partir de las tablas del Catálogo Nacional de Estaciones del IDEAM y otras entidades, cree un catálogo integrado de estaciones. A partir del límite de las zub-zonas hidrográfica, seleccione las estaciones con cubrimiento y al rededor de la zona de estudio, cree las siguientes capas y análisis: envolvente de límite municipal, aferencia de envolvente, marcado de estaciones, áreas aferentes, distancia entre estaciones y su densidad.

<div align="center"><img src="graph/CNEStation.png" alt="R.SIGE" width="100%" border="0" /></div>


## Objetivos

* Descargar el catálogo nacional de estaciones - CNE del IDEAM y de otras entidades de Colombia.
* Conocer las categorías de las estaciones hidro-climatológicas y qué tipo de observaciones realizan.
* Conocer los estados, tecnologías y niveles de aprobación de los datos en estaciones.
* Identificar los atributos contenidos en el catálogo de objetos del CNE.
* A partir de un polígono envolvente, seleccionar, exportar e integrar las estaciones del IDEAM y de otras entidades en un único catálogo.
* Analizar la cobertura espacial sobre la zona de estudio las estaciones obtenidas.
* Calcular la longitud hipotética de las series a partir de la fecha de instalación y suspensión de las estaciones utilizando Python Script.
* Calcular la longitud hipotética de las series dentro de una ventana de tiempo establecida a partir de las estaciones utilizando Python Script.
* Identificar, representar, graficar y analizar las longitudes hipotéticas de series para estaciones que contienen datos de precipitación, temperatura del aire cerca del suelo, evaporación potencial, nivel de lámina y caudal en ríos.


## Requerimientos

* [:mortar_board:Actividad](../SZH/Readme.md): Análisis de sub-zonas hidrográficas. Polígono que delimita la subzona hidrográfica del caso de estudio y polígono envolvente con aferencia. 
* [:mortar_board:Actividad](../POTLayer/Readme.md): Inventario de información geo-espacial recopilada del POT y diccionario de datos.
* [:toolbox:Herramienta](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview): ESRI ArcGIS Pro 3.3.1 o superior.
* [:toolbox:Herramienta](https://qgis.org/): QGIS 3.38 o superior.


## 1. Conceptos generales

### 1.1. Conceptos y atributos que componen el catálogo nacional de estaciones y especificaciones

El [Instituto de Hidrología, Meteorología y Estudios Ambientales - IDEAM](http://www.ideam.gov.co/) de Colombia, adscrito al [Ministerio de Medio Ambiente - Minambiente](https://www.minambiente.gov.co/), es la entidad nacional encargada registrar y mantener la información hidrometeorológica del país, incluida la localización y clasificación de la red de estaciones que hace parte del [Catálogo Nacional de Estaciones - CNE](http://dhime.ideam.gov.co/). A través del portal [DHIME](http://dhime.ideam.gov.co/atencionciudadano/) del IDEAM desde la pestaña _Recursos_, personas naturales o jurídicas, pueden obtener no solamente los catálogos, sino también las capas geográficas y los registros discretos registrados en cada estación.

Tomados directamente del catálogo de objetos del archivo [CNE_IDEAM.xls](http://dhime.ideam.gov.co/) v20240702 y tipos devueltos por Python / Pandas.

| Atributo             | Tipo        | Descripción                                                                                                                                                                                                                                    |
|:---------------------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBJECTID             | int64       | Identificador de objeto espacial proveniente de la GDB IDEAM.                                                                                                                                                                                  |
| CODIGO               | int64       | Código de la estación.                                                                                                                                                                                                                         |
| nombre               | object      | Nombre de la estación. Incluye el código de la estación entre corchetes.                                                                                                                                                                       |
| CATEGORIA            | object      | Categoría de la estación: Pluviométrica, Limnimétrica, Limnigráfica, Climática Ordinaria, Climática Principal, Pluviográfica, Meteorológica Especial, Agrometeorológica, Sinóptica Principal, Radio Sonda, Mareográfica, Sinóptica Secundaria. |
| TECNOLOGIA           | object      | Tecnología para captura, registro y transmisión: Convencional, Automática con Telemetría, Automática sin Telemetría.                                                                                                                           |
| ESTADO               | object      | Estado de funcionamiento: Activa, Suspendida, En Mantenimiento.                                                                                                                                                                                |
| FECHA_INSTALACION    | datetime64  | Fecha de instalación. FECHA_INST en archivos Shapefile.                                                                                                                                                                                        |
| altitud              | int64       | Altitud o cota sobre el nivel del mar en metros.                                                                                                                                                                                               |
| latitud              | float64     | Latitud en grados decimales.                                                                                                                                                                                                                   |
| longitud             | float64     | Longitud en grados decimales.                                                                                                                                                                                                                  |
| DEPARTAMENTO         | object      | Departamento o zonificación política. Equivalente a estados en otros países. DEPARTAMEN en archivos Shapefile.                                                                                                                                 |
| MUNICIPIO            | object      | Municipio o subzonificación política. Equivalente a condado en otros países.                                                                                                                                                                   |
| AREA_OPERATIVA       | object      | Área operativa que administra la estación. AREA_OPERA en archivos Shapefile.                                                                                                                                                                   |
| AREA_HIDROGRAFICA    | object      | Área hidrográfica a la cual pertenece. AREA_HIDRO en archivos Shapefile.                                                                                                                                                                       |
| ZONA_HIDROGRAFICA    | object      | Zona hidrográfica a la cual pertenece. ZONA_HIDRO en archivos Shapefile.                                                                                                                                                                       |
| observacion          | object      | Observaciones generales. observacio en archivos Shapefile.                                                                                                                                                                                     |
| CORRIENTE            | object      | Corriente, cauce o río próximo o sobre la cuál está localizada la estación.                                                                                                                                                                    |
| FECHA_SUSPENSION     | datetime64  | Fecha de suspensión. FECHA_SUSP en archivos Shapefile.                                                                                                                                                                                         |
| SUBZONA_HIDROGRAFICA | object      | Subzona hidrográfica a la cual pertenece.SUBZONA_HI en archivos Shapefile.                                                                                                                                                                     |
| ENTIDAD              | object      | Entidad encargada.                                                                                                                                                                                                                             |
| subred               | object      | Subred a la cual pertenece.                                                                                                                                                                                                                    |

> Los atributos presentados en la tabla, su tipo de escritura y notación han sido tomados del archivo original y no se encuentran normalizados a 11 caracteres para garantizar la compatibilidad con el formato .dbf. Se puede observar que los datos volcados en el archivo CNE_IDEAM.xls han sido generados utilizando la herramienta _Table to Table_ de ArcGIS desde una Geodatabase que permite la definición de atributos con más de 11 caracteres. 
> 
> Los atributos del catálogo nacional de estaciones y de otras entidades son equivalentes. Catálogos exportados a archivos de formas Shapefile utilizan máximo 10 caracteres en la definición de atributos.


### 1.2. Categorías de las estaciones

Definiciones generales del catálogo nacional de estaciones tomado de [Anexo 2 - Definiciones CNE](http://www.ideam.gov.co/documents/10182/557765/Definiciones+CNE.pdf) del IDEAM.

| Categoría                        | Abrv. | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:---------------------------------|:-----:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Estación Agrometeorológica       |  AM   | En esta estación se realizan observaciones meteorológicas y otras observaciones que ayudan a determinar las relaciones entre el clima, por una parte y la vida de las plantas y los animales por la otra. Incluye el mismo programa de observaciones de la estación climatológica principal, más registros de temperatura a varias profundidades (hasta un metro) y en la capa cercana al suelo (0, 10 y 20 cm sobre el suelo).                                                                                     |
| Estación Climatológica Ordinaria |  CO   | Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros y humedad primordialmente. Poseen muy poco instrumental registrador. Algunas llevan instrumentos adicionales tales como tanque de evaporación, heliógrafo y anemómetro.                                                                                                                                                                                                                |
| Estación Climatológica Principal |  CP   | Es aquella en la cual se hacen observaciones de precipitación, temperatura del aire, temperaturas máxima y mínima a 2 metros, humedad, viento, radiación, brillo solar, evaporación, temperaturas extremas del tanque de evaporación, cantidad de nubes y fenómenos especiales. Gran parte de estos parámetros se obtienen de instrumentos registradores.                                                                                                                                                           |
| Estación Limnigráfica            |  LG   | Estación donde se mide el nivel de una corriente hídrica mediante un aparato registrador de nivel y que grafica una curva llamada limnigrama.                                                                                                                                                                                                                                                                                                                                                                       |
| Estación Limnimétrica            |  LM   | Estación donde se mide el nivel de una corriente hídrica mediante un aparato (mira dividida en centímetros) que mide altura del agua, sin registrarla. Una persona toma el dato y lo registra en una libreta.                                                                                                                                                                                                                                                                                                       |
| Estación Mareográfica            |  MG   | Estaciones para observación del estado del mar. Mide nivel, temperatura y salinidad de las aguas marinas.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Estación Meteorológica especial  |  ME   | Estación instalada para realizar seguimiento a un fenómeno o un fin específico, por ejemplo, las heladas.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Estación Pluviográfica           |  PG   | Es aquella que registra en forma mecánica y continua la precipitación, en una gráfica que permite conocer la cantidad, duración, intensidad y periodo en que ha ocurrido la lluvia. Actualmente se utilizan los pluviógrafos de registro diario.                                                                                                                                                                                                                                                                    |
| Estación Pluviométrica           |  PM   | Es una estación meteorológica dotada de un pluviómetro o recipiente que permite medir la cantidad de lluvia caída entre dos observaciones consecutivas.                                                                                                                                                                                                                                                                                                                                                             |
| Estación Radio Sonda             |  RS   | La estación de radiosonda tiene por finalidad la medición directa de parámetros atmosféricos tales como temperatura del aire, presión atmosférica, humedad relativa y dirección y velocidad del viento en las capas altas de la atmósfera (tropósfera y baja estratósfera), mediante el rastreo, por medios electrónicos, de la trayectoria de un globo meteorológico que asciende libremente y que lleva un dispositivo con los sensores que miden y transmiten la señal con los datos.                            |
| Estación Sinóptica Principal     |  SP   | En este tipo de estación se efectúan observaciones de los principales elementos meteorológicos en horas convenidas internacionalmente. Los datos se toman horariamente y corresponden a nubosidad, dirección y velocidad de los vientos, presión atmosférica, temperatura del aire, tipo y altura de las nubes, visibilidad, fenómenos especiales, características de humedad, precipitación, temperaturas extremas, capas significativas de nubes, recorrido del viento y secuencia de los fenómenos atmosféricos. |
| Estación Sinóptica Secundaria    |  SS   | Al igual que en la estación anterior, las observaciones se realizan a horas convenidas internacionalmente y los datos corresponden comúnmente a visibilidad, fenómenos especiales, tiempo atmosférico, nubosidad, estado del suelo, precipitación, temperatura del aire, humedad del aire, presión y viento.                                                                                                                                                                                                        |
> Las abreviaturas contenidas en la columna Abrv., han sido definidas por [rcfdtools](https://github.com/rcfdtools) con el propósito de simplificar las cabeceras incluidas en la tabla de observaciones por tipo de estación.


### 1.3. Observaciones según la categoría de la estación :new:

En la siguiente tabla preliminar desarrollada por [rcfdtools](https://github.com/rcfdtools), se presentan los tipos de observaciones que pueden ser realizadas por las estaciones dependiendo de su categoría.

| Observación / Categoría                        | AM  | CO  | CP  | LG  | LM  | MG  | ME  | PG  | PM  | RS  | SP  | SS  |
|:-----------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Precipitación                                  | ✓   | ✓   | ✓   |     |     |     |     | ✓   | ✓   |     | ✓   | ✓   |
| Temperatura del aire cerca al suelo            | ✓   | ✓   | ✓   |     |     |     |     |     |     |     | ✓   | ✓   |
| Temperatura máxima del aire a 2 metros         | ✓   | ✓   | ✓   |     |     |     |     |     |     |     |     |     |
| Temperatura mínima del aire a 2 metros         | ✓   | ✓   | ✓   |     |     |     |     |     |     |     |     |     |
| Temperatura del aire en capa alta de atmósfera |     |     |     |     |     |     |     |     |     | ✓   |     |     |
| Temperatura extrema del tanque de evaporación  | ✓   |     | ✓   |     |     |     |     |     |     |     |     |     |
| Temperatura del suelo a varias profundidades   | ✓   |     |     |     |     |     |     |     |     |     |     |     |
| Temperatura del agua                           |     |     |     |     |     | ✓   |     |     |     |     |     |     |
| Temperaturas extremas                          |     |     |     |     |     |     |     |     |     |     | ✓   |     |
| Evaporación                                    | ✓   | ✓   | ✓   |     |     |     |     |     |     |     |     |     |
| Brillo solar                                   | ✓   |     | ✓   |     |     |     |     |     |     |     |     |     |
| Radiación solar                                | ✓   |     | ✓   |     |     |     |     |     |     |     |     |     |
| Humedad del aire cerca al suelo                | ✓   | ✓   | ✓   |     |     |     |     |     |     |     | ✓   | ✓   |
| Humedad relativa en capa alta de atmósfera     |     |     |     |     |     |     |     |     |     | ✓   |     |     |
| Humedad - Características                      |     |     |     |     |     |     |     |     |     |     | ✓   |     |
| Viento - Dirección                             | ✓   |     | ✓   |     |     |     |     |     |     |     | ✓   | ✓   |
| Viento - Velocidad                             | ✓   |     | ✓   |     |     |     |     |     |     |     | ✓   | ✓   |
| Viento - Recorrido                             | ✓   |     | ✓   |     |     |     |     |     |     |     | ✓   | ✓   |
| Viento - Dirección en capa alta de atmósfera   |     |     |     |     |     |     |     |     |     | ✓   |     |     |
| Viento - Velocidad en capa alta de atmósfera   |     |     |     |     |     |     |     |     |     | ✓   |     |     |
| Presión en capa alta de atmósfera              |     |     |     |     |     |     |     |     |     | ✓   |     |     |
| Presión atmosférica cercana al suelo           |     |     |     |     |     |     |     |     |     |     | ✓   | ✓   |
| Nubosidad - Octas                              | ✓   |     | ✓   |     |     |     |     |     |     |     | ✓   | ✓   |
| Nubosidad - Tipo                               |     |     |     |     |     |     |     |     |     |     | ✓   |     |
| Nubosidad - Altura de nubes                    |     |     |     |     |     |     |     |     |     |     | ✓   |     |
| Nubosidad - Capas significativas               |     |     |     |     |     |     |     |     |     |     | ✓   |     |
| Visibilidad                                    |     |     |     |     |     |     |     |     |     |     | ✓   | ✓   |
| Nivel lámina agua                              |     |     |     | ✓   | ✓   | ✓   |     |     |     |     |     |     |
| Heladas                                        |     |     |     |     |     |     | ✓   |     |     |     |     |     |
| Secuencia fenómenos atmosféricos               |     |     |     |     |     |     |     |     |     |     | ✓   | ✓   |
| Tiempo atmosférico                             |     |     |     |     |     |     |     |     |     |     |     | ✓   |
| Estado del suelo                               |     |     |     |     |     |     |     |     |     |     |     | ✓   |
| Salinidad agua marina                          |     |     |     |     |     | ✓   |     |     |     |     |     |     |
| Fenómenos especiales                           | ✓   |     | ✓   |     |     |     | ✓   |     |     |     | ✓   | ✓   |
| Tanque evaporación (no siempre)                |     | ✓   | ✓   |     |     |     |     |     |     |     |     |     |
| Heliógrafo (no siempre)                        |     | ✓   |     |     |     |     |     |     |     |     |     |     |
| Anenómetro (no siempre)                        |     | ✓   |     |     |     |     |     |     |     |     |     |     |


### 1.4. Estado de la estación

| Estado           | Descripción                                                                                                                                                                                 |
|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Activa           | Estación que se encuentra en operación y registra datos automáticos o tomados por un observador.                                                                                            |
| En mantenimiento | Estación que se encuentra en operación pero que temporalmente no registra datos automáticos o tomados por un observador por problemas en los equipos o como consecuencia de un siniestro.   |
| Suspendida       | Estación que se encuentra fuera de servicio de manera definitiva y no registra datos automáticos o tomados por un observador. Solo se puede consultar datos históricos en estas estaciones. |


### 1.5. Tecnología de la estación

| Tecnología                | Descripción                                                                                                                                                                                                                                                                                                                                 |
|:--------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Convencional              | Estación donde la toma del dato la efectúa un observador y la registra en una libreta para luego enviarla a los técnicos para que se capture y procesen estos datos.                                                                                                                                                                        |
| Automática con telemetría | Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de enviarlos de manera automática al centro de recepción por diferentes medios de transmisión (satelital, radiofrecuencia, GPRS, etc.)                                                                                     |
| Automática sin telemetría | Estación que obtiene los datos de manera automática mediante sensores de diferente tipo y que tiene la capacidad de almacenarlos en un dispositivo dentro de la misma estación. No puede enviar los datos de manera automática. Los datos debes ser obtenidos por una persona que se conecta al sitio donde la estación almacena los datos. |

> De acuerdo a la nota del Anexo 2 del IDEAM: se debe tener en cuenta que la red es de tipo dinámico; es decir, a través de su operación se han instalado y suspendido estaciones a lo largo del territorio nacional, conservando en todo caso los datos históricos registrados. Esto significa que la sumatoria de las estaciones del Catálogo corresponde al número total de estaciones que han hecho parte de la red a través de su historia de operación y registro de información.


## 2. Creación de catálogo integrado

1. Ingresar al portal _http://dhime.ideam.gov.co/atencionciudadano/_, aceptar los términos y condiciones para descargar información del Banco de Datos del IDEAM, dar clic en la pestaña de recursos y descargar el Catálogo nacional de estaciones en formato Microsoft Excel, el Catálogo nacional de otras entidades y el Glosario de variables. Opcionalmente, el catálogo puede ser descargado desde el portal del IDEAM desde [Solicitud de Información](http://www.ideam.gov.co/solicitud-de-informacion). Guarde los archivos de Microsoft Excel _CNE_IDEAM.xls y CNE_OE.xls en el directorio _\file\data\IDEAM\_.

<div align="center"><img src="graph/DHIMERecursos.png" alt="R.SIGE" width="100%" border="0" /></div>
<div align="center"><img src="graph/IDEAMSolicitudInformacion.png" alt="R.SIGE" width="100%" border="0" /></div>

> Para identificar versión de los archivos descargados, al final del nombre puede incluir en formato aaaammdd, la fecha correspondiente a la descarga. Para este ejemplo, utilizaremos 20240702. 

2. Desde Microsoft Excel, abra los archivos _CNE_IDEAM_20240702.xls y CNE_OE_20240702.xls, revise las cabeceras de estos archivos. Asegúrese de que en los archivos, la secuencia de las columnas y los nombres sean idénticos. Podrá observar que los nombres son idénticos, que en la tabla de las estaciones del catálogo nacional del IDEAM existe una columna adicional denominada _subred_ y que se han registrado 4503 y 4604 estaciones.

<div align="center"><img src="graph/Excel_CNE_20240702.png" alt="R.SIGE" width="100%" border="0" /></div>

3. Cree un nuevo archivo de Excel y guárdelo como _\file\table\CNE_Colombia_20240702.xlsx_, renombre la hoja como _CNE_Colombia_20240702_, agregue una columna al inicio con el nombre _CNESource_, copie en la misma hoja los registros de las dos tablas de atributos y normalice los nombres de las cabeceras a 10 caracteres. La tabla final deberá contener 9107 registros.

Utilice los siguientes nombres: `CNESource`, `Codigo`, `Nombre`, `Categoria`, `Tecnologia`, `Estado`, `FechaInst`, `Altitud`, `LatDD`, `LongDD`, `Depto`, `Municipio`, `AreaOperat`, `COD_AH`, `COD_ZH`, `Observ`, `Corriente`, `FechaSusp`, `COD_SZH`, `Entidad`, `Subred`.

> Tenga en cuenta que en la unión de las dos tablas, debe incluir la cabecera una única vez y que en la columna `CNESource` debe ingresar _CNE_ o _CNE_OE_ dependiendo de la fuente de catálogo utilizada.
> 
> La normalización a 10 caracteres es requerida para que en la creación de la capa geográfica, no se pierdan caracteres en los nombres de los atributos.
> 
> Para la correcta interpretación de cuando fueron instaladas y/o suspendidas las estaciones, asegúrese de establecer formato fecha en las columnas `FechaInst` y `FechaSusp`.
> 
> La columna de identificador de objeto espacial `OBJECTID`, puede ser eliminada debido a que corresponde al consecutivo utilizado en cada una de las tablas orígen.

<div align="center"><img src="graph/Excel_CNE_Colombia_20240702a.png" alt="R.SIGE" width="100%" border="0" /></div>

4. Realice las siguientes verificaciones:

* La columna `Codigo`, debe ser establecida en formato de texto.
* En los campos `FechaInst`, `FechaSusp`, `Altitud`, `LatDD`, `LongDD`, no deben existir comas, las separaciones decimales deberán ser establecidas en puntos, tanto en la tabla como en la configuración regional del panel de control de su sistema operativo. 
* Los campos `LatDD` y `LongDD` deben contener siempre valores. 




2. Abra el proyecto de ArcGIS Pro, creado previamente y desde el menú _Insert_ cree un nuevo mapa _New Map_, renombre como _CNEStation_ y establezca el CRS 9377. Agregue al mapa la capa del Modelo de Ocupación Territorial - MOT disponible en la información recopilada del POT en la ruta `\R.SIGE\file\data\POT\Anexo_Acuerdo_012_2013\shp\MOT.shp` y ajuste la simbología a valores únicos representando el campo de atributos `SUELO`.


3. Desde la carpeta _.shp_, agregue al mapa el archivo shapefile [CNE_IDEAM.shp](../../.shp/CNE_IDEAM.zip), [ZonaEstudio.shp](../../.shp/ZonaEstudio.zip) y [ZonaEstudioEnvelope.shp](../../.shp/ZonaEstudioEnvelope.zip). Modifique la simbología de representación de _ZonaEstudioEnvelope_ sin relleno - línea contorno rojo - grosor 3 y _ZonaEstudio_ sin relleno - línea contorno negro - grosor 2. Simbolice las estaciones con puntos color gris 30% - sin contorno - tamaño 6, rotular por el campo `CODIGO` y acercar a la zona de estudio. 

![R.LTWB](Screenshot/ArcGISPro3.0.0CNEMap.png)

> Tenga en cuenta que automáticamente ha sido asignado el sistema de coordenadas geográficas MAGNA al proyecto debido a que el Shapefile del CNE contiene integrado este sistema. En cuanto al número de estaciones, para la versión descargada a 20220731, el CNE se compone de 4476 estaciones.

4. Desde la carpeta _.datasets_, agregue el archivo _CNE_OE.xls_ que contiene la localización de estaciones de otras entidades de Colombia y abra la tabla de atributos, podrá observar que a fecha 20220731 la tabla contiene 4620 registros. Dando clic derecho en la tabla y seleccionando la opción _Display XY Data_, cree una capa de eventos geográficos para representar la localización de estas estaciones. Utilice el sistema de coordenadas _GCS_WGS_1984_.

![R.LTWB](Screenshot/ArcGISPro3.0.0CNEOEDisplayXYData.png)

Como puede observar en la ilustración, en el polígono envolvente de la zona de estudio existen múltiples estaciones del catálogo nacional del IDEAM y de otras entidades. 

> Para el cargue de archivos de Microsoft Excel en formato .xls, se requiere del [Driver de Microsoft Access Database Engine](https://www.microsoft.com/en-us/download/confirmation.aspx?id=54920)[^2].

7. Desde el menú _Map / Selection / Select By Location_, seleccione todas aquellas estaciones del catálogo nacional de estaciones y de otras entidades que se intersecan con la zona de estudio. Para la zona de estudio y la versión descargada de los catálogos, se han seleccionado 315 estaciones del CNE y 125 de otras entidades.

![R.LTWB](Screenshot/ArcGISPro3.0.0SelectByLocation.png)

8. Exporte las estaciones seleccionadas a nuevas capas geográficas, clic derecho en CNE_IDEAM / _Data / Export Features_ y nombre como _[CNE_IDEAM_ZE.shp](../../.shp/CNE_IDEAM_ZE.zip)_ dentro de la carpeta _.shp_. Repita este procedimiento para la capa de eventos de las estaciones de otras entidades y nombre como _[CNE_OE_ZE.shp](../../.shp/CNE_OE_ZE.zip)_.

![R.LTWB](Screenshot/ArcGISPro3.0.0CNE_IDEAM_ZEExportFeatures.png)  
![R.LTWB](Screenshot/ArcGISPro3.0.0CNE_OE_ZEExportFeatures.png)  
![R.LTWB](Screenshot/ArcGISPro3.0.0CNEZEExportFeaturesMap.png)

> En ArcGIS for Desktop, el procedimiento de exportación se realiza dando clic derecho en la capa y seleccionando la opción _Data / Export Data_. Para el caso de la capa de eventos de las estaciones de otras entidades, se recomienda primero exportar la capa de eventos en un archivo Shapefile y luego efectuar la selección y exportación de las estaciones de la zona de estudio.

9. Con la herramienta _Geoprocessing / Data Management Tools / General / Merge_, combine los archivos de formas _CNE_IDEAM_ZE.shp_ y _CNE_OE_ZE.shp_ en un único archivo y nombre como _[CNE_IDEAM_OE_ZE.shp](../../.shp/CNE_IDEAM_OE_ZE.zip)_. Asegúrese de marcar la casilla `Add source information to output` para obtener el campo de atributos `MERGE_SRC` que describe la capa fuente y de clic en la opción _Reset_ ubicada a la derecha de `Field Map` . La red de estaciones contendrá en total 440 estaciones (315 IDEAM + 125 otras entidades).

![R.LTWB](Screenshot/ArcGISPro3.0.0CNE_IDEAM_OE_ZEMerge.png)


## 3. Estudio de longitud hipotética de series

10. Una vez obtenida la red de estaciones integrada sobre la zona de estudio, es necesario estudiar la longitud hipotética de las series a partir de las fechas de instalación y suspensión registradas en el catálogo. 

> Este procedimiento es importante debido a que para la descarga de las series de datos registradas en las estaciones, es necesario primero conocer la homogeneidad en las longitudes hipotéticas de los registros que deberían tener las estaciones a partir de su fecha de puesta en operación y recolección de datos. Por ejemplo, si la mayoría de las estaciones tienen un registro continuo y actual de al menos 20 años y en las estaciones de la zona de estudio existen estaciones recientes o antiguas suspendidas con registros cortos (p. ej. 5 años), se podrían descartar estas estaciones del análisis, siempre y cuando no correspondan a estaciones en la zona de frontera geográfica de la zona en estudio.

En la capa _CNE_IDEAM_OE_ZE.shp_, crear los siguientes campos de atributos:

| Campo    | Tipo           | Descripción                                                                                 |
|:---------|:---------------|---------------------------------------------------------------------------------------------|
| LYearS   | Numérico doble | Campo para longitud hipotética de serie a partir de las fechas de instalación y suspensión. |
| LYearSTW | Numérico doble | Campo para longitud hipotética de serie a partir de una ventana de tiempo definida.         |

En la tabla de atributos dar clic en el botón _Field: Add_ y desde el modo de edición agregar los campos indicados, luego desde el Menú superior _Fields_, dar clic en _Save_. 

![R.LTWB](Screenshot/ArcGISPro3.0.0AddField.png)

> En ArcGIS for Desktop, desde las propiedades de la tabla de atributos seleccionar la opción _Add Field_.

**Cálculo independiente del campo LYears**

El cálculo del campo `LYearS` puede ser realizado dando clic en la cabecera del campo y seleccionando la opción _Calculate Field_ utilizando la instrucción Python 3 `(!FECHA_INST!-!FECHA_SUSP!)/365`, sin embargo, no podrá ser aplicada a estaciones que se encuentran suspendidas debido a que el campo fecha de suspensión contendrá valores nulos, por lo que Python devolverá un error y no realizará el cálculo solicitado. Igual sucede con el campo fecha de instalación cuando este se encuentra nulo, la operación de cálculo no podrá ser completada.

![R.LTWB](Screenshot/ArcGISPro3.0.0CalculareFieldLYearSError.png)

> En ArcGIS for Desktop puede usar la expresión VBScript `( [FECHA_SUSP] - [FECHA_INST] )/365`.

Para el correcto análisis de los campos fecha de instalación y fecha de suspensión, la configuración regional requerida debe ser definida desde el _Panel de Control / Region_, estableciendo el formato de fechas cortas como d/MM/yyyy.

![R.LTWB](Screenshot/Windows11ControlPanlRegionFormat.png)

Para realizar correctamente este cálculo, es necesario considerar la fecha final de los registros de las estaciones que se encuentran en operación, para este ejemplo, la fecha de corte corresponde al último día del año inmediatamente anterior correspondiente a 2021.12.31 considerando que para el análisis climatológico, únicamente utilizaremos datos de años cronológica o hidrológicamente completos. La longitud de series en años usando Python a través de Calculate Field para el campo LYearS, puede ser realizada a través de Code Block utilizando las siguientes instrucciones:

Pre-Logic Script Code para Python 2 sobre ArcGIS for Desktop y Python 3 sobre ArcGIS Pro: 
```
from datetime import datetime
date_format = '%d/%m/%Y'
tw_end_date = '31/12/2021' # Time window end
is_python3 = True # True for Python 3, False for Python2
if is_python3:
    tw_end_date = datetime.strptime(tw_end_date, date_format)
def len_years_serie(installation_date, suspension_date):
    if not installation_date:
        installation_date = tw_end_date
        suspension_date = tw_end_date
    if not suspension_date:
        suspension_date = tw_end_date
    if is_python3:
        diff_date = suspension_date - installation_date
    else:
        diff_date = datetime.strptime(suspension_date, date_format) - datetime.strptime(installation_date, date_format)
    return float(diff_date.days)/365
```

LYearS:
```
len_years_serie(!FECHA_INST!, !FECHA_SUSP!)
```

![R.LTWB](Screenshot/ArcGISPro3.0.0CalculareFieldLYearSPython.png)

> En ArcGIS for Desktop pude dar clic derecho sobre la cabecera del campo `LYearS` y seleccionar la opción _Field Calculator_ o desde _ArcToolBox / Data Management Tools / Fields / Calculate Field_.

![R.LTWB](Screenshot/ArcGISDesktop10.2.2CalculareFieldLYearSPython.png)
![R.LTWB](Screenshot/ArcGISDesktop10.2.2CalculareFieldLYearSPythonA.png)

> En el script, la variable booleana `is_python3` es utilizada para definir la versión de Python desde la cual se hace el llamado del Script.
> 
> Python 2 sobre ArcGIS for Desktop transfiere como texto las variables FECHA_INST y FECHA_SUSP en formato unicode, es por ello que deben ser convertidas a formato de fecha para poder calcular la diferencia en días. Cuando en la tabla de atributos las fechas son almacenadas como cadenas de texto, puede definir la variable `is_python3 = False` para realizar el cálculo de diferencias en Python 2 o 3.

De clic derecho en la cabecera del campo `LYearS` y seleccione la opción _Statistics_, obtendrá un resumen estadístico y una gráfica con las longitudes hipotéticas en años para cada estación. Como puede observar, la media de las longitudes es de 24.8 años con una alta desviación estándar correspondiente a 22.6 años y múltiples estaciones tienen registros cortos de menos de 10 años.

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSStatistics.png)

Utilizando la tecla <kbd>Ctrl</kbd> + <kbd>clic</kbd>, seleccione las barras correspondientes a los valores de la media y superiores, obtendrá que 158 estaciones contienen longitudes hipotéticas iguales o superiores a 38.3 años dentro y alrededor de la zona de estudio.    

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSStatisticsA.png)

**Cálculo simultáneo de campos LYears y LYearsTW**

Para realizar el cálculo de longitudes hipotéticas de series a partir de una ventana de tiempo definida, p. ej. del 01/01/1980 al 31/12/2021 correspondiente a 42.027397 años, utilizar el siguiente código.

Pre-Logic Script Code para Python 2 sobre ArcGIS for Desktop: 
```
from datetime import datetime
date_format = '%d/%m/%Y'
tw_start_date = '01/01/1980' # Time-window start. Use '' for set 01/01/1900
tw_end_date = '31/12/2021' # Time-window end. Use '' for use the current date and prevent over-time wrong suspension dates
if not tw_start_date: tw_start_date = '01/01/1900'
if not tw_end_date: tw_end_date = str(datetime.today().date())
def len_years_serie(installation_date, suspension_date):
    if installation_date:
        if datetime.strptime(installation_date, date_format) <= datetime.strptime(tw_start_date, date_format):
            tw_installation_date = tw_start_date
        else:
            tw_installation_date = installation_date
        if suspension_date:
            if datetime.strptime(suspension_date, date_format) >= datetime.strptime(tw_end_date, date_format):
                tw_suspension_date = tw_end_date
            else:
                tw_suspension_date = suspension_date
            diff_date = datetime.strptime(suspension_date, date_format) - datetime.strptime(installation_date, date_format)
            tw_diff_date = datetime.strptime(tw_suspension_date, date_format) - datetime.strptime(tw_installation_date, date_format)
        else:
            diff_date = datetime.strptime(tw_end_date, date_format) - datetime.strptime(installation_date, date_format)
            tw_diff_date = datetime.strptime(tw_end_date, date_format) - datetime.strptime(tw_installation_date, date_format)
        diff_date = float(diff_date.days)/365
        tw_diff_date = float(tw_diff_date.days)/365
        if diff_date < 0: diff_date = 0
        if tw_diff_date < 0: tw_diff_date = 0
    else:
        diff_date = 0
        tw_diff_date = 0
    return diff_date, tw_diff_date # First value is complete length. Second value is time window length
```

Pre-Logic Script Code para Python 3 sobre ArcGIS Pro: 
```
from datetime import datetime
date_format = '%d/%m/%Y'
tw_start_date = datetime.strptime('01/01/1980', date_format)# Time-window start. Use '' for set 01/01/1900
tw_end_date = datetime.strptime('31/12/2021', date_format) # Time-window end. Use '' for use the current date and prevent over-time wrong suspension dates
if not tw_start_date: tw_start_date = datetime.strptime('01/01/1900', date_format)
if not tw_end_date: tw_end_date = str(datetime.today().date())
def len_years_serie(installation_date, suspension_date):
    if installation_date:
        if installation_date <= tw_start_date:
            tw_installation_date = tw_start_date
        else:
            tw_installation_date = installation_date
        if suspension_date:
            if suspension_date >= tw_end_date:
                tw_suspension_date = tw_end_date
            else:
                tw_suspension_date = suspension_date
            diff_date = suspension_date - installation_date
            tw_diff_date = tw_suspension_date - tw_installation_date
        else:
            diff_date = tw_end_date - installation_date
            tw_diff_date = tw_end_date - tw_installation_date
        diff_date = float(diff_date.days)/365
        tw_diff_date = float(tw_diff_date.days)/365
        if diff_date < 0: diff_date = 0
        if tw_diff_date < 0: tw_diff_date = 0
    else:
        diff_date = 0
        tw_diff_date = 0
    return diff_date, tw_diff_date # First value is complete length. Second value is time window length
```

LYearS:
```
len_years_serie(!FECHA_INST!, !FECHA_SUSP!)[0]
```

LYearSTW:
```
len_years_serie(!FECHA_INST!, !FECHA_SUSP!)[1]
```

![R.LTWB](Screenshot/ArcGISDesktop10.2.2CalculareFieldLYearSTWPython.png)
![R.LTWB](Screenshot/ArcGISPro3.0.0CalculareFieldLYearSPythonA.png)
![R.LTWB](Screenshot/ArcGISPro3.0.0CalculareFieldLYearSTWPython.png)

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre todas aquellas estaciones cuya longitud hipotética de registro dentro de la ventana de tiempo sea mayor a cero `LYearSTW > 0`.

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWDefinitionQuery.png)

De clic derecho en la cabecera del campo `LYearSTW` y seleccione la opción _Statistics_, obtendrá un resumen estadístico y una gráfica con las longitudes hipotéticas en años para cada estación dentro de la ventana de tiempo establecida. Como puede observar, la media de las longitudes hipotéticas es de 29.8 años con una desviación estándar de 16.1 años. Utilizando la tecla <kbd>Ctrl</kbd> + <kbd>clic</kbd>, seleccione las barras del histograma a partir de la media, obtendrá 174 de 263 estaciones con registros iguales o superiores a 29.5 años de registro y podrá observar simultáneamente su localización dentro y alrededor de la zona de estudio.

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWStatistics.png)

Simbolice las estaciones por categoría a partir del campo `CATEGORIA` para las estaciones con longitudes hipotéticas dentro de la ventana de tiempo establecida y cree una gráfica de barras por categoría, podrá observar que el mayor número de estaciones corresponde a la categoría Pluviométricas.

![R.LTWB](Screenshot/ArcGISPro3.0.0BarGraphCategoria.png)


## 4. Identificación de estaciones con datos de precipitación

Las longitudes hipotéticas de registros en estaciones evaluadas previamente, corresponden a diferentes categorías. En el caso específico de la precipitación, los registros pueden ser obtenidos de estaciones Agrometeorológicas, Climatológicas Ordinarias, Climatológicas Principales, Pluviográficas, Pluviométricas, Sinópticas Principales y Sinópticas Secundarias.

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre las estaciones de las categorías indicadas y represente por símbolos graduados en 3 clases por cortes naturales a partir de las longitudes hipotéticas de series dentro de la ventana de tiempo calculada en el campo `LYearSTW`. Visualice a escala 1:2,250,000 (en monitores FHD 1920 x 1080p). Podrá observar que para las categorías indicadas se obtienen 325 estaciones.

Expresión SQL: `CATEGORIA IN ('Agrometeorológica', 'Climática Ordinaria', 'Climática Principal', 'Pluviográfica', 'Pluviométrica', 'Sinóptica Principal', 'Sinóptica Secundaria')`

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWRainQuery1.png)

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre todas aquellas estaciones cuya longitud hipotética de registro dentro de la ventana de tiempo sea mayor a 10, 15, 20, 25, 30, 35 años para las categorías indicadas y evalúe mediante una estadística sobre el campo `LYearSTW`, la media de las longitudes hipotéticas de las series y obtenga los estadísticos característicos.

Expresión SQL para series >= 10 años : `LYearSTW >= 10 And CATEGORIA IN ('Agrometeorológica', 'Climática Ordinaria', 'Climática Principal', 'Pluviográfica', 'Pluviométrica', 'Sinóptica Principal', 'Sinóptica Secundaria')`

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWRainQueryCategory.png)

| Series >= 10 y 25 años                                                                                                                                                                                                                                                                                                           | Series >= 15 y 30 años                                                                                                                                                                                                                                                                                                           | Series >= 20 y 35 años                                                                                                                                                                                                                                                                                                           |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Longitud hipotética en años >= 10<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 139<br>Media: 37.1 años<br>Mínimo: 10.3 años<br>Máximo: 42 años<br>Desv. Est.: 9 años<br>![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWRain10.png)    | Longitud hipotética en años >= 15<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 132<br>Media: 38.4 años<br>Mínimo: 15 años<br>Máximo: 42 años<br>Desv. Est.: 7.1 años<br>![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWRain15.png)    | Longitud hipotética en años >= 20<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 124<br>Media: 39.8 años<br>Mínimo: 22.1 años<br>Máximo: 42 años<br>Desv. Est.: 4.6 años<br>![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWRain20.png)  |
| Longitud hipotética en años >= 25<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 119<br>Media: 40.5 años<br>Mínimo: 26.6 años<br>Máximo: 42 años<br>Desv. Est.: 3.17 años<br>![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWRain25.png) | Longitud hipotética en años >= 30<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 116<br>Media: 40.8 años<br>Mínimo: 30.5 años<br>Máximo: 42 años<br>Desv. Est.: 2.54 años<br>![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWRain30.png) | Longitud hipotética en años >= 35<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 109<br>Media: 41.3 años<br>Mínimo: 35.1 años<br>Máximo: 42 años<br>Desv. Est.: 1.58 años<br>![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWRain35.png) |

Simbolice las estaciones por categorías y cree un gráfico de barras que represente las estaciones y la longitud hipotética de las series en la ventana de tiempo definida >= 10 años, ordene descendentemente. Podrá observar que mayoritariamente las estaciones pluviométricas y climáticas ordinarias son las que pueden contener los registros más extensos.

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWRainQueryCategoryGraph.png)

Para el desarrollo del caso de estudio, utilizaremos las estaciones con registros de precipitación cuyas longitudes hipotéticas sean >= a 10 años que mayoritariamente se encuentran en el último rango de cortes naturales con valores superiores a 26.649315 años. En actividades posteriores analizaremos el traslapo entre las series reales y evaluaremos que estaciones requerirán ser completadas y/o extendidas.

Utilizando la herramienta _Geoprocessing / Conversion Tools / To Geodatabase / Table to Table_, exporte en una tabla independiente las 139 estaciones obtenidas. Guarde la tabla en el directorio _D:\R.LTWB\\.datasets_ con el nombre CNE_IDEAM_OE_ZE_Precipitacion.dbf. Esta tabla será usada para manualmente descargar los registros de las estaciones desde el servicio DHIME del IDEAM.

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWRainTableToTable.png)


## 5. Identificación de estaciones con datos de temperatura del aire cerca al suelo

En el caso específico de la temperatura del aire cerca de la superficie del suelo, los registros pueden ser obtenidos de estaciones Agrometeorológicas, Climatológicas Ordinarias, Climatológicas Principales, Sinópticas Principales y Sinópticas Secundarias.

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre las estaciones de las categorías indicadas y represente por símbolos graduados en 3 clases por cortes naturales a partir de las longitudes hipotéticas de series dentro de la ventana de tiempo calculada en el campo `LYearSTW`. Visualice a escala 1:2,250,000 (en monitores FHD 1920 x 1080p). Podrá observar que para las categorías indicadas se obtienen 71 estaciones.

Expresión SQL: `CATEGORIA IN ('Agrometeorológica', 'Climática Ordinaria', 'Climática Principal', 'Sinóptica Principal', 'Sinóptica Secundaria')`

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWTemperatureAirQuery1.png)

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre todas aquellas estaciones cuya longitud hipotética de registro dentro de la ventana de tiempo sea mayor a 5 años para las categorías indicadas y evalúe mediante una estadística sobre el campo `LYearSTW`, la media de las longitudes hipotéticas de las series y obtenga los estadísticos característicos.

Expresión SQL para series >= 5 años : `LYearSTW >= 5 And CATEGORIA IN ('Agrometeorológica', 'Climática Ordinaria', 'Climática Principal', 'Sinóptica Principal', 'Sinóptica Secundaria')`

| Series >= 5 años                                                                                                                                                                                                                                                                                                                      |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Longitud hipotética en años >= 5<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 42<br>Media: 23.8 años<br>Mínimo: 5 años<br>Máximo: 42 años<br>Desv. Est.: 15.7 años<br>![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWTemperatureAir5a.png) |

Como observa, existen dentro y alrededor de la zona de estudio tan solo 42 estaciones con longitudes hipotéticas de registro superiores a 5 años, de las cuales 19 tienen longitudes por encima de la media.

> Es importante considerar que existen estaciones sobre y alrededor de la zona de estudio, sin embargo, un factor importante a considerar es el rango de elevaciones de las estaciones debido a la alta correlación que existe entre la temperatura del aire y la elevación.

Represente las estaciones por símbolos graduados a partir de la elevación, podrá observar que el rango disponible de elevaciones a partir del campo `altitud` registrado por el IDEAM, corresponde a valores entre 18 y 2256 m.s.n.m. y en la Serranía del Perijá al este de la zona de estudio, las elevaciones de terreno son mayores. De las 42 estaciones disponibles, tan solo 1 se encuentra por encima de los 2000 m.s.n.m.

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWTemperatureAirQueryElevation.png)

Simbolice las estaciones por categorías y cree un gráfico de barras que represente las estaciones y la longitud hipotética de las series en la ventana de tiempo definida >= 5 años, ordene descendentemente. Podrá observar que mayoritariamente las estaciones climáticas ordinarias y climáticas principales son las que pueden contener los registros más extensos.

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWTemperatureAirQueryCategoryGraph.png)

Utilizando la herramienta _Geoprocessing / Conversion Tools / To Geodatabase / Table to Table_, exporte en una tabla independiente las 42 estaciones obtenidas. Guarde la tabla en el directorio _D:\R.LTWB\\.datasets_ con el nombre CNE_IDEAM_OE_ZE_TemperaturaAire.dbf. Esta tabla será usada para manualmente descargar los registros de las estaciones desde el servicio DHIME del IDEAM.

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWTemperatureAirTableToTable.png)


## 6. Identificación de estaciones con datos de evaporación potencial

En el caso específico de la evaporación potencial, los registros pueden ser obtenidos de estaciones Agrometeorológicas, Climatológicas Ordinarias y Climatológicas Principales.

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre las estaciones de las categorías indicadas y represente por símbolos graduados en 3 clases por cortes naturales a partir de las longitudes hipotéticas de series dentro de la ventana de tiempo calculada en el campo `LYearSTW`. Visualice a escala 1:2,250,000 (en monitores FHD 1920 x 1080p). Podrá observar que para las categorías indicadas se obtienen 70 estaciones.

Expresión SQL: `CATEGORIA IN ('Agrometeorológica', 'Climática Ordinaria', 'Climática Principal')`

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWEvaporationQuery.png)

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre todas aquellas estaciones cuya longitud hipotética de registro dentro de la ventana de tiempo sea mayor a 5 años para las categorías indicadas y evalúe mediante una estadística sobre el campo `LYearSTW`, la media de las longitudes hipotéticas de las series y obtenga los estadísticos característicos.

Expresión SQL para series >= 5 años : `LYearSTW >= 5 And CATEGORIA IN ('Agrometeorológica', 'Climática Ordinaria', 'Climática Principal')`

| Series >= 5 años                                                                                                                                                                                                                                                                                                                   |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Longitud hipotética en años >= 5<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 41<br>Media: 24.2 años<br>Mínimo: 5 años<br>Máximo: 42 años<br>Desv. Est.: 15.6 años<br>![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWEvaporation5.png)  |

Como observa, existen dentro y alrededor de la zona de estudio tan solo 41 estaciones con longitudes hipotéticas de registro superiores a 5 años, de las cuales 19 tienen longitudes por encima de la media.

Simboloce las estaciones por categorías y cree un gráfico de barras que represente las estaciones y la longitud hipotética de las series en la ventana de tiempo definida >= 5 años, ordene descendentemente. Podrá observar que mayoritariamente las estaciones climáticas ordinarias y climáticas principales son las que pueden contener los registros más extensos.

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWEvaporationQueryCategoryGraph.png)

Utilizando la herramienta _Geoprocessing / Conversion Tools / To Geodatabase / Table to Table_, exporte en una tabla independiente las 41 estaciones obtenidas. Guarde la tabla en el directorio _D:\R.LTWB\\.datasets_ con el nombre CNE_IDEAM_OE_ZE_Evaporacion.dbf. Esta tabla será usada para manualmente descargar los registros de las estaciones desde el servicio DHIME del IDEAM.

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWEvaporationTableToTable.png)


## 7. Identificación de estaciones con datos de nivel de lámina de agua en ríos

Una vez sea realizado el balance hidrológico de largo plazo y se obtengan los caudales medios, estos podrán ser comparados con los registros medios de las series de caudales obtenidos a partir de los datos obtenidos en estaciones limnimétricas y/o limnigráficas. 

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre las estaciones de las categorías indicadas y represente por símbolos graduados en 3 clases por cortes naturales a partir de las longitudes hipotéticas de series dentro de la ventana de tiempo calculada en el campo `LYearSTW`. Visualice a escala 1:2,250,000 (en monitores FHD 1920 x 1080p). Podrá observar que para las categorías indicadas se obtienen 65 estaciones.

Expresión SQL: `CATEGORIA IN ('Limnimétrica', 'Limnigráfica')`

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWWaterLevelQuery.png)

Desde las propiedades de la capa _CNE_IDEAM_OE_ZE.shp_ y a través del _Definition Query_, filtre todas aquellas estaciones cuya longitud hipotética de registro dentro de la ventana de tiempo sea mayor a 5 años para las categorías indicadas y evalúe mediante una estadística sobre el campo `LYearSTW`, la media de las longitudes hipotéticas de las series y obtenga los estadísticos característicos.

Expresión SQL para series >= 5 años : `LYearSTW >= 5 And CATEGORIA IN ('Limnimétrica', 'Limnigráfica')`

| Series >= 5 años                                                                                                                                                                                                                                                                                                                 |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Longitud hipotética en años >= 5<br>Cubrimiento: sobre toda la zona de estudio<br>Estaciones encontradas: 65<br>Media: 37.3 años<br>Mínimo: 7.3 años<br>Máximo: 42 años<br>Desv. Est.: 10 años<br>![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWWaterLevel5.png) |

Como observa, existen dentro y alrededor de la zona de estudio 65 estaciones con longitudes hipotéticas de registro superiores a 5 años, de las cuales 51 tienen longitudes por encima de la media.

Simboloce las estaciones por categorías y cree un gráfico de barras que represente las estaciones y la longitud hipotética de las series en la ventana de tiempo definida >= 5 años, ordene descendentemente. Podrá observar que las estaciones limnimétricas y limnigráficas poseen registros extensos.

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWWaterLevelQueryCategoryGraph.png)

Utilizando la herramienta _Geoprocessing / Conversion Tools / To Geodatabase / Table to Table_, exporte en una tabla independiente las 65 estaciones obtenidas. Guarde la tabla en el directorio _D:\R.LTWB\\.datasets_ con el nombre CNE_IDEAM_OE_ZE_NivelCaudal.dbf. Esta tabla será usada para manualmente descargar los registros de las estaciones desde el servicio DHIME del IDEAM.

![R.LTWB](Screenshot/ArcGISPro3.0.0LYearSTWWaterLevelTableToTable.png)


## 8. Análisis usando software libre - QGIS

Para el desarrollo de las actividades desarrolladas en esta clase, se pueden utilizar en QGIS las siguientes herramientas o geo-procesos:

| Proceso                                         | Procedimiento                                                                                                                                                                                                       |
|:------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Simbología                                      | Modificable desde las propiedades de la capa en la pestaña _Symbology_.                                                                                                                                             |
| Rotulado                                        | Modificable desde las propiedades de la capa en la pestaña _Labels_.                                                                                                                                                |
| Cálculos geométricos o de campo                 | Directamente desde la tabla de atributos mediante el botón _Open Field Calculator_ o <kbd>Ctr</kbd>+<kbd>I</kbd>. La geometría de cálculo `$area` permite obtener el valor elipsoidal y `area` el valor proyectado. |
| Polígono envolvente (envelope o bounding boxes) | Herramienta disponible en el _Processing Toolbox / Vector Geometry / [Bounding boxes](https://docs.qgis.org/3.34/en/docs/user_manual/processing_algs/qgis/vectorgeometry.html#bounding-boxes)_.                     |
| Recorte de capas vectoriales (clip)             | Herramienta disponible en el _Processing Toolbox / Vector Overlay / [Clip](https://docs.qgis.org/3.34/en/docs/user_manual/processing_algs/qgis/vectoroverlay.html#clip)_.                                           |

Ejemplo rótulo en QGIS: `'A(ha): ' ||  round("AGha", 2) || '\n' || 'P (m): ' ||  round("PGm", 2) `

[:notebook:QGIS training manual](https://docs.qgis.org/3.34/en/docs/training_manual/)


## Elementos requeridos en diccionario de datos

Agregue a la tabla resúmen generada en la actividad [Inventario de información geo-espacial recopilada del POT y diccionario de datos](../POTLayer/Readme.md), las capas generadas en esta actividad que se encuentran listadas a continuación:

| Nombre                           | Descripción                                                                                                                                | Geometría   | Registros | 
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-------------|-----------| 
| SZH2120.shp                      | Polígono de la subzona hidrográfica 2120 correspondiente al Río Bogotá, obtenido a partir de la capa _Zonificacion_hidrografica_2013.shp_. | Polígono 2D | 1         | 
| SZH_Mpio25899_Clip.shp           | Intersección entre _Zonificacion_hidrografica_2013.shp_ y _Mpio25899_MOT2013.shp_.                                                         | Polígono 2D | 2         | 
| SZH2120_Envelope.shp             | Polígono envolvente al rededor de _SZH2120.shp_.                                                                                           | Polígono 2D | 1         | 
| SZH2120_Envelope_Buffer250m.shp  | Buffer o aferencia alrederor de la capa SZH2120_Envelope.shp.                                                                              | Polígono 2D | 1         | 

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

* http://dhime.ideam.gov.co/atencionciudadano/
* http://www.ideam.gov.co/solicitud-de-informacion
* [ArcGIS Pro tarda mucho tiempo en abrir mi proyecto](https://github.com/rcfdtools/R.LTWB/discussions/13):lady_beetle:


## Control de versiones

| Versión    | Descripción                                                             | Autor                                      | Horas |
|------------|:------------------------------------------------------------------------|--------------------------------------------|:-----:|
| 2024.03.18 | Versión inicial con alcance de la actividad.                            | [rcfdtools](https://github.com/rcfdtools)  |   4   |
| 2024.07.23 | Investigación, documentación y desarrollo para caso de estudio general. | [rcfdtools](https://github.com/rcfdtools)  |   6   |


_R.SIGE es de uso libre para fines académicos, conoce nuestra licencia, cláusulas, condiciones de uso y como referenciar los contenidos publicados en este repositorio, dando [clic aquí](LICENSE.md)._

_¡Encontraste útil este repositorio!, apoya su difusión marcando este repositorio con una ⭐ o síguenos dando clic en el botón Follow de [rcfdtools](https://github.com/rcfdtools) en GitHub._

| [:arrow_backward: Anterior](../POI/Readme.md) | [:house: Inicio](../../README.md) | [:beginner: Ayuda / Colabora](https://github.com/rcfdtools/R.SIGE/discussions/21) | [Siguiente :arrow_forward:](../CNEStation/Readme.md) |
|-----------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------------|

[^1]: http://dhime.ideam.gov.co/atencionciudadano/
[^2]: https://pro.arcgis.com/en/pro-app/latest/help/data/excel/prepare-to-work-with-excel-in-arcgis-pro.htm
