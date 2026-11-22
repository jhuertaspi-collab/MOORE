# Guía de estudio: Genética y Biología Molecular

> Medicina, Universidad Nacional de Colombia, 2026. Basada en las diapositivas de clase de los profesores **Oscar Ortega-Recalde**, **Sandra Yaneth Ospina Lagos** y **Mauricio Rey Buitrago**, verificada contra fuentes primarias y ampliada con lo necesario para entender cada tema.
> Última actualización: 22 de noviembre de 2026. Todas las clases están en este archivo; sus tarjetas están en un solo mazo de Anki, [`Genetica_Biologia_Molecular.apkg`](Genetica_Biologia_Molecular.apkg).

---

## Cómo usar esta guía

| Símbolo | Significado |
|---|---|
| 📌 | Idea clave de la clase. Si solo repasas algo, que sea esto. |
| ➕ | **Ampliación**: no está en las diapositivas, pero ayuda a entender o es típica de examen. |
| ⚠️ | Trampa frecuente o confusión típica. |
| ✅ | **Verificación**: la diapositiva tiene un error, un dato desactualizado o un matiz; aquí está la versión correcta con su fuente. |
| 🩺 | Correlación clínica. |
| 💊 | Terapia o farmacología. |
| 🧠 | Mnemotecnia. |
| *(Diap. N)* | Diapositiva de la clase donde está el contenido. |

Cada capítulo tiene la misma estructura: **lo esencial en un minuto** → desarrollo por diapositivas → **verificación de datos** → **autoevaluación** con respuestas desplegables → glosario → referencias. Cada capítulo empieza con su propio índice y termina con un enlace para volver aquí.

Es un archivo largo: para moverte, usa el índice general de abajo o el índice de encabezados que GitHub muestra en la parte superior del archivo.

---

## Índice general

| # | Capítulo | Docente | Tarjetas en el mazo |
|---|---|---|---|
| 1 | [Introducción a la bioinformática y medicina genómica](#1-introducción-a-la-bioinformática-y-medicina-genómica) | O. Ortega-Recalde | 66 |
| 2 | [Genética del desarrollo](#2-genética-del-desarrollo) | O. Ortega-Recalde | 84 |
| 3 | [Ciclo celular: fases, motor molecular y puntos de control](#3-ciclo-celular-fases-motor-molecular-y-puntos-de-control) | S. Y. Ospina Lagos | 125 |
| 4 | [Errores innatos del metabolismo](#4-errores-innatos-del-metabolismo-eim) | S. Y. Ospina Lagos | 108 |
| 5 | [Mecanismos de reparación del ADN](#5-mecanismos-de-reparación-del-adn-de-la-lesión-molecular-a-la-clínica) | S. Y. Ospina Lagos | 366 (cloze, pregunta-respuesta y casos clínicos) |
| 6 | [Genética del cáncer: biología molecular, hallmarks y perspectivas terapéuticas](#6-genética-del-cáncer-biología-molecular-hallmarks-y-perspectivas-terapéuticas) | S. Y. Ospina Lagos | 156 |
| 7 | [Técnicas de biología molecular](#7-técnicas-de-biología-molecular) | M. Rey Buitrago | 142 |
| | **Total** | | **1.047** |

**Anexos**: [A. Conexiones entre clases](#anexo-a-conexiones-entre-clases) · [B. Tabla transversal de enfermedades](#anexo-b-tabla-transversal-de-enfermedades) · [C. Fe de erratas consolidada](#anexo-c-fe-de-erratas-consolidada) · [D. Cómo estudiar con el mazo de Anki](#anexo-d-cómo-estudiar-con-el-mazo-de-anki) · [E. Cómo crecerá esta guía](#anexo-e-cómo-crecerá-esta-guía)

**Ruta sugerida**: ciclo celular → reparación del ADN (continúa directamente desde los puntos de control) → genética del cáncer (integra las dos anteriores) → genética del desarrollo → errores innatos del metabolismo. La bioinformática y las técnicas de biología molecular son transversales: estudia las técnicas temprano, porque las demás clases las usan (FISH, PCR, NGS), y usa la bioinformática para buscar en OMIM, dbSNP o Ensembl cada enfermedad.

---

## 1. Introducción a la bioinformática y medicina genómica

> Clase del Prof. **Oscar Ortega-Recalde** (MD, MSc, PhD), Universidad Nacional de Colombia, 2026.
> Las citas *(Diap. N)* siguen la numeración de las diapositivas de la clase. Los símbolos 📌 ➕ ⚠️ ✅ 🩺 🧠 se explican al [inicio de la guía](#cómo-usar-esta-guía).

---

### Índice (capítulo 1)

- [Lo esencial en un minuto](#lo-esencial-en-un-minuto-capítulo-1)
- [1.1 Definiciones](#11-definiciones-diap-36)
- [1.2 ¿Por qué importan la bioinformática y la medicina genómica?](#12-por-qué-importan-la-bioinformática-y-la-medicina-genómica-diap-710)
- [1.3 Alfabetización en programación](#13-alfabetización-en-programación-diap-11)
- [1.4 Lenguajes de programación y algoritmos](#14-lenguajes-de-programación-y-algoritmos-diap-1317)
- [1.5 Recursos para aprender](#15-recursos-para-aprender-diap-1819)
- [1.6 Definiciones comunes en bioinformática](#16-definiciones-comunes-en-bioinformática-diap-2128)
- [1.7 Bases de datos en ciencias biomédicas](#17-bases-de-datos-en-ciencias-biomédicas-diap-3148)
- [1.8 Aplicaciones en la clínica](#18-aplicaciones-en-la-clínica-diap-4959)
- [✅ Verificación de datos de la clase](#-verificación-de-datos-de-la-clase-capítulo-1)
- [Autoevaluación](#autoevaluación-capítulo-1)
- [Glosario](#glosario-capítulo-1)
- [Referencias](#referencias-capítulo-1)

---

### Lo esencial en un minuto (capítulo 1)

📌 Si solo repasas algo de esta clase, que sea esto:

1. **Bioinformática**: ciencia interdisciplinaria que investiga, desarrolla y aplica **métodos computacionales** a las ciencias biológicas. Nace de la intersección entre **ciencias de la computación** y **biología**.
2. **Medicina genómica**: usa **información genética a gran escala** para mejorar la atención de pacientes y poblaciones.
3. Las **tecnologías *high-throughput*** generan grandes volúmenes de datos; analizarlos exige bioinformática y permite generar **nuevas hipótesis biomédicas**.
4. Un **algoritmo** es una serie de pasos específicos y precisos para resolver un problema. Un **lenguaje de programación** es el conjunto de reglas para comunicarle ese algoritmo a una máquina.
5. ¿Qué lenguaje aprender? **Depende del usuario y de la tarea**. **Python** y **R** son los más usados en bioinformática.
6. **Higiene de datos**: homogeneidad, datos atómicos, identificador único por registro, sin redundancia, cada variable con su unidad.
7. **Bases de datos primarias** (repositorios de lo que envía el autor, redundantes, sin vocabulario controlado) frente a **secundarias** (curadas por expertos, no redundantes, con vocabulario controlado).
8. Bases clave: **NCBI** (PubMed, MeSH, Nucleotide, Protein, dbSNP), **Ensembl** (EMBL-EBI) y **OMIM** (fenotipos y genes mendelianos, creada por **Victor McKusick**).
9. El **exoma** es ~1–2 % del genoma; su secuenciación permitió al profesor identificar **variantes bialélicas (heterocigosis compuesta) en *HERC1*** en una forma sindrómica de sobrecrecimiento y discapacidad intelectual.
10. La **inteligencia artificial** y los modelos estadísticos integran datos clínicos y genéticos: ejemplo, el predictor de severidad de COVID-19 que combina edad, sexo, comorbilidades y el polimorfismo ***LZTFL1* rs11385942** (población colombiana).

---

### 1.1 Definiciones *(Diap. 3–6)*

#### Contenido de la clase *(Diap. 3)*

1. Definición y utilidad en ciencias biomédicas.
2. Lenguajes de programación y algoritmos.
3. Definiciones comunes en bioinformática.
4. Bases de datos en ciencias biomédicas.
5. Aplicaciones en la clínica.

La frase de apertura *(Diap. 2)*, de C. William Pollard, resume la idea de la clase: la información solo es útil si está **organizada, procesada y disponible** para quien debe tomar decisiones; si no, es una carga.

#### ¿Qué es la bioinformática? *(Diap. 5)*

📌 **Ciencia interdisciplinaria encargada de la investigación, desarrollo y aplicación de métodos computacionales en ciencias biológicas.**

```
   Ingenierías                                     Medicina
   Matemáticas    ( Ciencias de la  ∩  Biología )   Genética
   Estadística    (  computación    BIOINFORMÁTICA)  Microbiología
```

- Del lado computacional aportan: **ingenierías, matemáticas y estadística**.
- Del lado biológico aportan: **medicina, genética y microbiología**.

#### ¿Qué es la medicina genómica? *(Diap. 6)*

📌 Disciplina que utiliza **información genética a gran escala** para mejorar el cuidado de la salud y la atención clínica de **pacientes y grupos poblacionales**.

➕ **Genética frente a genómica**

| | Genética | Genómica |
|---|---|---|
| Objeto | Genes individuales y su herencia | El genoma completo y la interacción entre genes y con el ambiente |
| Escala | Uno o pocos genes | Miles de genes a la vez (datos a gran escala) |
| Ejemplo | Estudiar *CFTR* en un paciente con sospecha de fibrosis quística | Secuenciar el exoma o el genoma de un niño sin diagnóstico |

---

### 1.2 ¿Por qué importan la bioinformática y la medicina genómica? *(Diap. 7–10)*

#### La cadena del dato *(Diap. 7)*

```
Tecnologías high-throughput → Gran cantidad de datos → Análisis de datos biológicos complejos → Nuevas hipótesis biomédicas
```

*High-throughput* (alto rendimiento) se refiere a técnicas que procesan miles o millones de muestras o moléculas a la vez: secuenciadores de nueva generación, microarreglos, espectrometría de masas.

#### El flujo de información genética y las ómicas *(Diap. 8)*

```
ADN  →  ARN  →  Proteína  →  Metabolitos
Genómica  Transcriptómica  Proteómica  Metabolómica
```

- La diapositiva atribuye al genoma humano **20.000–25.000 genes**. ✅ Esa es la estimación de 2004; las anotaciones actuales (GENCODE, Ensembl) cuentan **~19.000–20.000 genes codificantes de proteínas**. Cada nivel "aguas abajo" es más numeroso: hay muchos más transcritos (empalme alternativo) y proteínas (modificaciones postraduccionales) que genes.
- **Genotipo → fenotipo**: el fenotipo resulta de la integración de las capas moleculares (genoma, epigenoma, transcriptoma, proteoma, metaboloma) **y de la exposición ambiental**. Por eso un mismo genotipo puede dar fenotipos distintos (salud o enfermedad).

#### Margaret Oakley Dayhoff y el crecimiento de GenBank *(Diap. 9)*

- **Margaret Oakley Dayhoff (1925–1983)** publicó en **1965** el ***Atlas of Protein Sequence and Structure***, la primera recopilación sistemática de secuencias de proteínas: en la práctica, la primera base de datos biológica. Se la considera pionera de la bioinformática.
  - ➕ También creó el **código de una letra** de los aminoácidos y las **matrices PAM** de sustitución de aminoácidos, que todavía se usan para alinear secuencias.
- La gráfica muestra el **número de secuencias reportadas en GenBank**, que crece de forma exponencial: el cuello de botella dejó de ser producir datos y pasó a ser analizarlos.

#### ¿Por qué importa la medicina genómica? *(Diap. 10)*

La clase parte de la **enfermedad mendeliana** (una variante en un gen, en una persona entre muchas) y la ubica en un ciclo de aplicaciones de la genómica a lo largo de la vida, tanto en la línea germinal como en tejidos somáticos:

- Diagnóstico de **enfermedades mendelianas**.
- Diagnóstico rápido en la **UCI neonatal**.
- **Tamizaje prenatal no invasivo** (ADN fetal libre en sangre materna).
- **Farmacogenómica** (elegir fármaco y dosis según el genotipo).
- **Cáncer** (variantes somáticas del tumor y predisposición germinal).
- **Puntajes de riesgo poligénico** (enfermedades comunes).

---

### 1.3 Alfabetización en programación *(Diap. 11)*

Aprender a programar es:

- Una **habilidad útil en múltiples escenarios**.
- De **curva de aprendizaje gradual**: no se requiere ser experto.
- Una fuente de **nuevas perspectivas para resolver problemas**.

---

### 1.4 Lenguajes de programación y algoritmos *(Diap. 13–17)*

#### ¿Qué es un lenguaje de programación? *(Diap. 13–14)*

📌 Dos definiciones de la clase, complementarias:

- **Conjunto de reglas que permiten a un computador comunicar qué operaciones realizar** *(Diap. 13)*. Notas manuscritas de la clase: es la *forma de dar instrucciones a un equipo* (una lavadora o un horno microondas también reciben instrucciones); *para una tarea más compleja se requieren instrucciones más específicas*.
- **Conjunto de reglas para comunicar un algoritmo a una máquina** *(Diap. 14)*.

#### ¿Qué es un algoritmo? *(Diap. 14)*

📌 **Serie de pasos específicos y precisos para resolver un problema de interés.**

Ejemplo de la clase, "preparar huevos revueltos":

1. Revolver los huevos.
2. Calentar una sartén.
3. Agregar aceite.
4. Agregar los huevos y revolver.
5. Servir los huevos revueltos.

El "algoritmo del éxito" de la diapositiva lo traduce a código: `while (noSuccess) { tryAgain(); if (Dead) break; }`. Muestra tres ideas básicas de programación: un **ciclo** (`while`), una **acción** que se repite y una **condición** (`if`) que detiene el ciclo.

#### Lenguaje natural frente a lenguaje de programación *(Diap. 15)*

| Elemento | Lenguaje natural (humano) | Lenguaje de programación |
|---|---|---|
| Palabras | "Casa", "Oso", "Jugar" | `X`, `Y`, `Z` (variables, funciones) |
| Símbolos | `,` | `>=` |
| Reglas gramaticales | Sujeto + verbo | `.` `()` `:` (sintaxis) |

Ambos tienen vocabulario, símbolos y gramática. La diferencia es que la máquina no tolera ambigüedad: una coma fuera de lugar detiene el programa.

#### ¿Qué lenguaje aprender? *(Diap. 16–17)*

- Hay cientos de lenguajes; los *rankings* (por ejemplo, el de IEEE Spectrum de 2023) ubican a **Python** en el primer lugar.
- 📌 **Depende del usuario y de la tarea.** **Python y R son útiles y ampliamente utilizados en bioinformática.**
- La diapositiva 17 cita a la bioinformática Maria Nattestad: la "verdadera" bioinformática consiste en usar la herramienta correcta para el trabajo, y R cubre la mayoría de las necesidades de un biólogo.

➕ **Para qué se usa cada uno en la práctica**

| Lenguaje | Fortalezas en bioinformática | Herramientas típicas |
|---|---|---|
| **R** | Estadística, gráficos, análisis de expresión génica | Bioconductor, ggplot2, Shiny (aplicaciones web) |
| **Python** | Propósito general, manejo de archivos grandes, aprendizaje automático | Biopython, pandas, scikit-learn |
| **Bash** (línea de comandos) | Encadenar programas, manejar archivos en servidores | `grep`, `awk`, ejecución de *pipelines* |

---

### 1.5 Recursos para aprender *(Diap. 18–19)*

| Tipo de recurso | Páginas de la clase | Comentario |
|---|---|---|
| Cursos masivos en línea (MOOC) | coursera.org, edx.org, khanacademy.org | Coursera ofrece el programa de la U. de Michigan *Ciencia de los datos aplicada con Python* *(Diap. 19)* |
| Aprendizaje interactivo | codecademy.com, codeschool.com | ✅ Code School ya no existe como plataforma independiente (fue absorbida por Pluralsight) |
| Problemas bioinformáticos | **rosalind.info** | Ejercicios de programación con datos biológicos reales, por niveles |
| Datos de laboratorio | — | Practicar con los propios datos |
| Foros web | **biostars.org**, seqanswers.com | Biostars es el foro de preguntas y respuestas más activo de bioinformática |
| Organizaciones internacionales | **elixir-europe.org** | Infraestructura europea de datos y formación en ciencias de la vida |
| Blogs y listas | ged.msu.edu/angus/bioinformatics-courses.html | ✅ Enlace antiguo: su autor (C. Titus Brown) dejó Michigan State; puede no funcionar |
| Aprender R dentro de R | **swirlstats.com** (*swirl*) *(Diap. 19)* | Paquete que enseña R y ciencia de datos desde la propia consola de R |

---

### 1.6 Definiciones comunes en bioinformática *(Diap. 21–28)*

#### Texto plano frente a texto enriquecido *(Diap. 21)*

| | Texto plano | Texto enriquecido (con formato) |
|---|---|---|
| Qué contiene | Solo caracteres. Nota de la clase: *"no hay datos adicionales al texto"* (sin colores, imágenes ni formato) | Texto más información de formato (fuentes, colores, imágenes, tablas) |
| Ejemplos | `.txt`, `.csv`, `.tsv`, archivos FASTA | `.docx`, `.pdf`, un afiche |
| Uso en bioinformática | Es el formato que leen los programas | Útil para humanos, difícil de procesar por máquinas |

#### Matriz de datos frente a hoja de cálculo *(Diap. 22)*

- **Matriz de datos**: tabla en **formato de texto plano** (nota manuscrita de la clase), con filas y columnas separadas por un delimitador (coma, tabulación).
- **Hoja de cálculo** (Excel, por ejemplo): tabla con formato, colores, fórmulas y celdas combinadas. Cómoda para ver, pero se presta a errores al analizar.
- ➕ Error clásico: Excel convierte nombres de genes en fechas (*SEPT2* → "2-sep", *MARCH1* → "1-mar"). Fue tan frecuente que en 2020 el comité de nomenclatura renombró esos genes (*SEPTIN2*, *MARCHF1*).

#### Higiene de datos *(Diap. 23)*

📌 Cinco reglas:

1. **Homogeneidad** de los datos (mismo formato en toda la columna).
2. Todos los datos deben ser **atómicos** (no divisibles): una sola unidad de información por celda.
3. Cada registro debe tener un **identificador único**.
4. **No** debe existir **información redundante**.
5. Cada variable debe tener una **unidad explícita**.

- **Variables = columnas**. **Registros = filas** (cada fila es una observación, por ejemplo un paciente).

➕ Ejemplo de tabla "sucia" y "limpia":

| ❌ Sucia | | ✅ Limpia | | | |
|---|---|---|---|---|---|
| **Paciente** | **Presión** | **id** | **pas_mmHg** | **pad_mmHg** | **edad_años** |
| Juan, 45 años | 120/80 | P001 | 120 | 80 | 45 |
| Juan, 45 años | 120/80 | P002 | 135 | 85 | 62 |

En la versión sucia, "Juan, 45 años" mezcla dos datos (no es atómico), la presión "120/80" junta dos variables, no hay unidad, no hay identificador y la fila está repetida.

#### Sistema operativo y línea de comandos *(Diap. 24)*

- **Sistema operativo**: programa base que administra el computador. En bioinformática predominan los de la familia **UNIX**: **Linux** y **macOS**.
- **Línea de comandos** (terminal, *shell*, Bash): interfaz de texto para dar órdenes al sistema operativo. Casi todas las herramientas bioinformáticas se ejecutan así.

#### Supercomputador, clúster y nube *(Diap. 25–26)*

| Concepto | Qué es | Ejemplo de la clase |
|---|---|---|
| **Supercomputador** | Máquina con capacidad de cálculo enorme | **Frontier** (Oak Ridge National Laboratory, Departamento de Energía de EE. UU.) |
| **Clúster de computadores** | Varios computadores conectados por una red (Ethernet) que trabajan como uno solo: un **nodo maestro** reparte el trabajo entre **nodos esclavos** (trabajadores) | Clúster universitario |
| **Computación en la nube** | Uso de servidores remotos por internet, pagando por uso | Amazon Web Services, Google Cloud, Microsoft Azure |

✅ Frontier fue el **primer supercomputador exaescala** (2022) y lideró el TOP500 hasta noviembre de 2024. En la lista de noviembre de 2026 ocupa el **3.er lugar**, detrás de LineShine (China) y El Capitan (EE. UU.).

#### Pseudocódigo, script y *pipeline* *(Diap. 27–28)*

- **Pseudocódigo**: el algoritmo escrito en lenguaje casi natural, sin la sintaxis estricta de un lenguaje (por ejemplo, "Función obtenerEdad: pedir edad, guardar en variable, devolver"). Sirve para planear.
- **Script (código)**: el programa escrito en un lenguaje concreto (R, Python) que la máquina ejecuta.
- **Pipeline o flujo de trabajo**: secuencia de pasos (programas) encadenados donde la salida de uno es la entrada del siguiente. Se representa con un **diagrama de flujo**:

| Símbolo | Significado |
|---|---|
| Óvalo | Inicio o fin |
| Flecha | Dirección del flujo |
| Paralelogramo | Entrada o salida de datos |
| Rectángulo | Proceso |
| Rombo | Decisión (sí/no) |

Ejemplo de la clase: "La lámpara no funciona" → ¿está enchufada? (no → enchufarla) → ¿el bombillo está fundido? (sí → cambiarlo; no → reparar la lámpara).

➕ **Formatos de archivo que verás en un *pipeline* de exoma**: **FASTQ** (lecturas crudas del secuenciador con su calidad) → alineamiento contra el genoma de referencia → **BAM** (lecturas alineadas) → llamado de variantes → **VCF** (lista de variantes) → anotación y filtrado. **FASTA** guarda secuencias sin calidad (por ejemplo, el genoma de referencia).

---

### 1.7 Bases de datos en ciencias biomédicas *(Diap. 31–48)*

#### Definición *(Diap. 31)*

📌 **Base de datos biomédica**: colección **organizada (estructurada)** de información relacionada con las ciencias biomédicas.

- Datos pertenecientes a un **mismo contexto**.
- **Almacenamiento sistemático** para su posterior uso.
- Pueden ser **físicas** (una biblioteca, un archivo de historias clínicas) o **electrónicas**.

#### Características de una base de datos *(Diap. 32)*

📌 **Estructurada · Indexable · Actualizada periódicamente · Con referencias cruzadas.**

🧠 *"E-I-A-R"*: **E**structurada, **I**ndexable, **A**ctualizada, **R**eferencias cruzadas.

#### Bases de datos relacionales *(Diap. 33)*

- Organizan la información en **tablas relacionadas** entre sí (modelo relacional). Ejemplo de la clase: una tabla de usuarios (`id`, `username`…), una de publicaciones (`tweets`) y una de seguidores (`following`) que conecta usuarios entre sí.
- ➕ Cada tabla tiene una **clave primaria** (identificador único de cada fila) y las tablas se enlazan mediante **claves foráneas** (la columna `from_user` apunta al `id` de la tabla de usuarios). Por eso la higiene de datos exige identificadores únicos.
- El **NCBI** funciona con este modelo: PubMed, revistas de texto completo, secuencias de nucleótidos, estructuras 3D, taxonomía, mapas y genomas, secuencias de proteínas y OMIM están enlazados entre sí.

#### Primarias frente a secundarias *(Diap. 34–35)*

| | Bases de datos **primarias** | Bases de datos **secundarias** |
|---|---|---|
| Qué son | Repositorios primarios de información | Repositorios **curados** |
| Redundancia | **Redundantes** (la misma secuencia puede estar muchas veces) | **No redundantes** |
| Control editorial | Lo tiene **quien somete** los archivos | Información complementaria **validada por un experto o comité** |
| Vocabulario | **No** controlado; anotación variable de los hallazgos | **Controlado** |
| Acceso | — | Generalmente de dominio público |
| Ejemplos | GenBank, ENA, DDBJ (secuencias de nucleótidos) | UniProtKB/Swiss-Prot, RefSeq, OMIM |

⚠️✅ La diapositiva 35 muestra el **PDB** como ejemplo de base secundaria. Muchas fuentes lo clasifican como **primaria**, porque archiva las estructuras tal como las depositan los investigadores (aunque el wwPDB las valida). Para el examen usa la clasificación de la clase, pero conoce el matiz.

#### Bases de datos de referencia *(Diap. 36)*

| Base | Qué contiene |
|---|---|
| **NCBI** | Centro de bases de datos del gobierno de EE. UU.: PubMed, GenBank, dbSNP, ClinVar, Gene, entre otras |
| **Ensembl** | Navegador y anotación de genomas de vertebrados y organismos modelo (EMBL-EBI) |
| **OMIM** | Catálogo de genes humanos y fenotipos mendelianos |
| **HGMD** | *Human Gene Mutation Database*: variantes germinales publicadas asociadas a enfermedad (versión completa por suscripción) |
| **PDB** | *Protein Data Bank*: estructuras tridimensionales de proteínas y ácidos nucleicos |
| **DDBJ** | *DNA Data Bank of Japan*. ➕ Con GenBank (EE. UU.) y ENA (Europa) forma la INSDC, que intercambia secuencias a diario |
| **GTEx** | *Genotype-Tissue Expression*: expresión génica en decenas de tejidos humanos y su relación con variantes (eQTL) |
| **Human Cell Atlas** | Mapa de referencia de todos los tipos celulares humanos (transcriptómica de célula única) |

#### NCBI *(Diap. 37–41)*

- **NCBI** (*National Center for Biotechnology Information*): recurso **administrado por el gobierno de EE. UU.** enfocado en información biotecnológica. ➕ Fundado en 1988, forma parte de la Biblioteca Nacional de Medicina (NLM) de los NIH.
- Recursos que muestra la clase:
  - **PubMed** *(Diap. 38)*: buscador de literatura biomédica.
  - **MeSH** (*Medical Subject Headings*) *(Diap. 39)*: **vocabulario controlado** de la NLM con el que se indexan los artículos de PubMed. Buscar con términos MeSH recupera artículos aunque usen sinónimos.
  - **Nucleotide** y **Protein** *(Diap. 40)*: secuencias de ácidos nucleicos y de proteínas.
  - **dbSNP** *(Diap. 41)*: variantes cortas (SNV, pequeñas inserciones y deleciones), cada una con un identificador **rs**. El ejemplo de la clase, **rs113993960**, es la deleción de 3 nt (delCTT) en *CFTR* (cromosoma 7) conocida como **F508del**, la variante más frecuente en fibrosis quística.

#### Ensembl *(Diap. 42–45)*

- Proyecto científico del **EBI** (*European Bioinformatics Institute*, parte de EMBL) que provee un **recurso centralizado** para genetistas, biólogos moleculares y otros investigadores que estudian el **genoma de vertebrados y otros organismos modelo**. ➕ Se lanzó en 1999 como proyecto conjunto del EBI y el Wellcome Sanger Institute.
- La clase muestra la página del gen ***BRCA2***: ubicación, **transcritos** alternativos (codificantes y no codificantes), estructura de exones e intrones y la **secuencia** del gen.

#### OMIM *(Diap. 46–48)*

- Creador: **Victor Almon McKusick (1921–2008)**, considerado padre de la genética médica.
- ***Mendelian Inheritance in Man* (MIM)**: catálogo impreso desde **1966** (12 ediciones).
- ***Online Mendelian Inheritance in Man* (OMIM)**: versión en línea desde **1987**.
- Estadísticas *(Diap. 47, actualizadas al 7 de noviembre de 2023)*: más de 27.000 entradas, distribuidas en descripciones de genes, de fenotipos y mixtas, y por tipo de herencia (autosómica, ligada al X, ligada al Y, mitocondrial).
- Ejemplo *(Diap. 48)*: **#100800 ACONDROPLASIA (ACH)**. El símbolo **#** indica que el fenotipo tiene base molecular conocida: heterocigosidad para una variante en ***FGFR3*** (receptor 3 del factor de crecimiento de fibroblastos), locus 4p16.3, herencia autosómica dominante.

➕ **Cómo leer los símbolos de OMIM** (pregunta frecuente)

| Símbolo | Significado |
|---|---|
| `*` | Gen con secuencia conocida |
| `+` | Gen y fenotipo en una misma entrada |
| `#` | Fenotipo con base molecular conocida |
| `%` | Fenotipo mendeliano (o locus) con base molecular desconocida |
| (sin símbolo) | Otros, sobre todo fenotipos con sospecha de base mendeliana |
| `^` | Entrada eliminada o trasladada |

🧠 **#** = "*hashtag*": el fenotipo ya está "etiquetado" con su gen. **%** = "porcentaje incompleto": falta el gen. **\*** = "estrella": el gen.

---

### 1.8 Aplicaciones en la clínica *(Diap. 49–59)*

#### Análisis de exoma *(Diap. 50–52)*

- 📌 Nota de la clase: en el **análisis de exoma solo se secuencia el exoma**, que es **~1 % (1–2 %) del genoma humano**.
- El **exoma** es el conjunto de **exones** (las partes de los genes que quedan en el ARNm maduro). La diapositiva usa la analogía de una manzana: el exoma es apenas una tajada (~1 %) del total, pero concentra gran parte de las variantes patogénicas conocidas de las enfermedades mendelianas.
- La imagen de la derecha *(Diap. 52)* es un visor de lecturas alineadas (tipo IGV): cada barra gris es una lectura del secuenciador; una variante aparece como un cambio de color en la misma posición en muchas lecturas.

#### Caso de investigación: *HERC1* *(Diap. 51, 53–55)*

- **Ortega-Recalde et al., 2015** (*Clinical Genetics*): **mutaciones bialélicas en *HERC1*** en una **forma sindrómica de sobrecrecimiento y discapacidad intelectual**.
- Encontrar la variante causal es **buscar una aguja en un pajar** *(Diap. 53)*: el exoma de una persona tiene decenas de miles de variantes, y se filtran paso a paso hasta quedar unas pocas candidatas.
  - ➕ Filtros típicos: calidad de la lectura → frecuencia en población (descartar las comunes) → efecto en la proteína (cambio de aminoácido, codón de parada, empalme) → predicción de patogenicidad → modelo de herencia → segregación en la familia → plausibilidad del gen.
- Árbol genealógico *(Diap. 54)*: los padres son portadores sanos, cada uno de una variante distinta; los **dos hijos afectados heredaron ambas** y el hermano sano solo una:
  - *HERC1* c.13559G>A (p.Gly4520Glu): cambio de aminoácido (*missense*).
  - *HERC1* c.2625G>A (p.Trp875Ter): codón de parada prematuro (*nonsense*).
  - 📌 Esto es **heterocigosis compuesta**: dos alelos mutados **distintos** del mismo gen (herencia autosómica recesiva). Se confirmó con secuenciación de Sanger (los electroferogramas muestran los dos picos superpuestos en cada posición).
- *(Diap. 55)* Trabajos posteriores: una variante de sitio de empalme en ***HERC2*** asociada a discapacidad intelectual sindrómica con macrocefalia y dismorfismo facial, y una revisión sobre cómo las ubiquitina-ligasas HERC grandes regulan la vía de las MAPK.

#### Inteligencia artificial y *big data* *(Diap. 56)*

- La implementación de **herramientas de inteligencia artificial** en el análisis de información médica es **cada vez mayor** (Zhavoronkov et al., *Nature Aging*, 2021).
- Fuentes de *big data* en salud: genoma, transcriptoma, proteoma, metaboloma, imágenes, fotos y videos, actividad física, exámenes de sangre y comportamiento. Redes neuronales profundas integran estos datos en el tiempo para estimar el estado de salud o enfermedad.

#### Predictor de severidad de COVID-19 en Colombia *(Diap. 57–59)*

- **Angulo-Aguado et al., *Frontiers in Medicine*, 2022**: asociación entre el polimorfismo ***LZTFL1* rs11385942** (locus **3p21.31**, alelo de inserción) y la **severidad de la COVID-19** en población colombiana.
- Diseño de **casos y controles**: **controles** = pacientes no hospitalizados; **casos** = pacientes hospitalizados (graves), con seguimiento clínico completo.
- Modelo final (regresión logística) *(Diap. 58)*:

```
score ajustado = 1 / (1 + e^-( -4,72 + 0,082·edad + 0,92·masculino + 1,51·comorbilidad + 1,4·[3p21.31 WT/INS] ))
```

- El puntaje separa bien a casos de controles (gráfica de cajas) y se publicó como **aplicación web hecha en R con Shiny** *(Diap. 59)*.

➕ **Cómo leer el modelo** (no está en la clase, pero aclara la fórmula)

- La función `1 / (1 + e^-x)` (logística) convierte cualquier número en una probabilidad entre 0 y 1.
- Cada coeficiente β es un logaritmo de *odds*; **e^β es el *odds ratio* (OR)**:
  - Comorbilidad: e^1,51 ≈ **4,5**.
  - Genotipo WT/INS en 3p21.31: e^1,4 ≈ **4,1**.
  - Sexo masculino: e^0,92 ≈ **2,5**.
  - Edad: e^0,082 ≈ **1,09 por año** (cada año aumenta las *odds* ~9 %).
- Idea clave: una sola variante genética aporta un riesgo comparable al de tener una comorbilidad, y se suma a los factores clínicos clásicos.

---

### ✅ Verificación de datos de la clase (capítulo 1)

| Diapositiva | Dice | Verificación |
|---|---|---|
| 8 | 20.000–25.000 genes | Estimación de 2004. Hoy: ~19.000–20.000 genes codificantes de proteínas (GENCODE/Ensembl) |
| 18 | codeschool.com | Plataforma absorbida por Pluralsight; ya no funciona como sitio independiente |
| 18 | ged.msu.edu/angus/… | Enlace antiguo; su autor ya no está en Michigan State |
| 25 | Frontier | Correcto. Fue el primer exaescala (2022); en noviembre de 2026 es el n.º 3 del TOP500 ([TOP500, nov. 2026](https://top500.org/news/top500-leadership-holds-steady-new-system-turnover-falls-historic-low/)) |
| 35 | PDB como base secundaria | Discutible: muchas fuentes la consideran primaria (archivo de estructuras depositadas) |
| 41 | rs113993960 | Corresponde a *CFTR* F508del (delCTT, cromosoma 7) |
| 46 | MIM 1966, OMIM 1987 | Correcto |
| 48 | #100800 acondroplasia, *FGFR3* | Correcto |

---

### Autoevaluación (capítulo 1)

<details><summary>1. ¿Qué dos disciplinas se intersecan para formar la bioinformática?</summary>

Ciencias de la computación y biología.
</details>

<details><summary>2. Diferencia entre algoritmo y lenguaje de programación.</summary>

El algoritmo es la serie de pasos precisos para resolver un problema. El lenguaje de programación es el conjunto de reglas con que se le comunica ese algoritmo a una máquina.
</details>

<details><summary>3. Un compañero guarda en una celda "Ana Gómez, 34 años, F". ¿Qué regla de higiene de datos viola?</summary>

La de datos **atómicos**: una celda debe contener un solo dato. Lo correcto es separar nombre, edad (con su unidad) y sexo en columnas distintas y asignar un identificador único.
</details>

<details><summary>4. ¿Por qué GenBank es una base primaria y OMIM una secundaria?</summary>

GenBank recibe lo que envían los investigadores (el autor controla el registro, hay redundancia y no hay vocabulario controlado). OMIM es curada por expertos, no redundante y usa vocabulario controlado.
</details>

<details><summary>5. En OMIM, ¿qué significa una entrada con "#" y otra con "%"?</summary>

"#": fenotipo con base molecular conocida. "%": fenotipo mendeliano con base molecular aún desconocida.
</details>

<details><summary>6. ¿Qué significa heterocigosis compuesta? Usa el caso HERC1.</summary>

El paciente tiene dos variantes patogénicas **distintas** en el mismo gen, una en cada alelo (una heredada de cada padre). En el caso HERC1: p.Gly4520Glu y p.Trp875Ter.
</details>

<details><summary>7. En el modelo de COVID-19, ¿cuál es el OR aproximado del genotipo 3p21.31 WT/INS?</summary>

e^1,4 ≈ 4: las *odds* de enfermedad grave son unas cuatro veces mayores, ajustando por edad, sexo y comorbilidad.
</details>

<details><summary>8. ¿Qué porcentaje del genoma es el exoma?</summary>

Aproximadamente 1–2 %.
</details>

---

### Glosario (capítulo 1)

| Término | Definición |
|---|---|
| **Algoritmo** | Serie de pasos específicos y precisos para resolver un problema |
| **Base de datos relacional** | Base organizada en tablas enlazadas por identificadores |
| **Clúster** | Conjunto de computadores en red que trabajan como uno solo (nodo maestro + nodos trabajadores) |
| **dbSNP** | Base del NCBI de variantes cortas, identificadas con "rs" |
| **Exoma** | Conjunto de exones del genoma (~1–2 %) |
| **Heterocigosis compuesta** | Dos variantes distintas del mismo gen, una en cada alelo |
| ***High-throughput*** | Tecnologías que generan datos masivos en paralelo |
| **MeSH** | Vocabulario controlado de la NLM para indexar PubMed |
| ***Pipeline*** | Secuencia de pasos de análisis encadenados |
| **Pseudocódigo** | Algoritmo escrito en lenguaje casi natural |
| **Script** | Programa escrito en un lenguaje de programación concreto |
| **Texto plano** | Archivo que solo contiene caracteres, sin formato |

---

### Referencias (capítulo 1)

De la clase:

- Ortega-Recalde O, et al. Biallelic HERC1 mutations in a syndromic form of overgrowth and intellectual disability. *Clin Genet.* 2015;88(4):e1-3.
- Zhavoronkov A, et al. *Nature Aging.* 2021.
- Angulo-Aguado M, et al. Association between the LZTFL1 rs11385942 polymorphism and COVID-19 severity in Colombian population. *Front Med.* 2022.
- Dayhoff MO. *Atlas of Protein Sequence and Structure.* 1965.

Usadas en la verificación:

- TOP500, lista de noviembre de 2026: <https://top500.org/news/top500-leadership-holds-steady-new-system-turnover-falls-historic-low/>
- OMIM, guía de símbolos y estadísticas: <https://www.omim.org>
- Wickham H. Tidy data. *J Stat Softw.* 2014;59(10).

[↑ Volver al índice general](#índice-general)

---

## 2. Genética del desarrollo

> Clase del Prof. **Oscar Ortega-Recalde** (MD, PhD), Universidad Nacional de Colombia, 2026.
> Las citas *(Diap. N)* siguen la numeración de las diapositivas de la clase. Los símbolos 📌 ➕ ⚠️ ✅ 🩺 🧠 se explican al [inicio de la guía](#cómo-usar-esta-guía).

---

### Índice (capítulo 2)

- [Lo esencial en un minuto](#lo-esencial-en-un-minuto-capítulo-2)
- [2.1 Introducción](#21-introducción-diap-26)
- [2.2 Fertilización, epigenética y gastrulación](#22-fertilización-epigenética-y-gastrulación-diap-711)
- [2.3 Principios de las familias de genes del desarrollo](#23-principios-de-las-familias-de-genes-del-desarrollo-diap-1218)
- [2.4 Morfógenos y patrones de desarrollo temprano](#24-morfógenos-y-patrones-de-desarrollo-temprano-diap-1922)
- [2.5 Superfamilia TGF-β](#25-superfamilia-tgf-β-diap-2427)
- [2.6 Genes homeobox (HOX)](#26-genes-homeobox-hox-diap-2832)
- [2.7 Genes PAX](#27-genes-pax-diap-3335)
- [2.8 Otras familias génicas: SOX, TBX, dedos de zinc, RAS-MAPK, FGFR](#28-otras-familias-génicas-diap-3637)
- [2.9 Principios de dismorfología](#29-principios-de-dismorfología-diap-3950)
- [✅ Verificación de datos de la clase](#-verificación-de-datos-de-la-clase-capítulo-2)
- [Autoevaluación](#autoevaluación-capítulo-2)
- [Glosario](#glosario-capítulo-2)
- [Referencias](#referencias-capítulo-2)

---

### Lo esencial en un minuto (capítulo 2)

1. **Genética del desarrollo**: rama de la genética que estudia **cómo los genes controlan el desarrollo embrionario**.
2. El desarrollo humano tiene tres estadios: **preembrionario, embrionario y fetal**.
3. La memoria epigenética se **borra en dos periodos**: en el **embrión preimplantatorio** y en las **células germinales primordiales**.
4. **Gastrulación**: la blástula se convierte en gástrula; el disco **bilaminar** (epiblasto, hipoblasto) pasa a **trilaminar** (ectodermo, mesodermo, endodermo). La **organogénesis** forma los órganos a partir de esas capas.
5. Muchos genes del desarrollo son **factores de transcripción** organizados en **redes regulatorias** conservadas en la evolución; sus mutaciones causan **malformaciones aisladas o síndromes**.
6. **Morfógeno**: sustancia cuya **distribución no uniforme** gobierna el patrón de desarrollo de un tejido (concepto de **Alan Turing**).
7. Familias clave y su enfermedad modelo: **TGF-β** (osteogénesis imperfecta XIII, *BMP1*), **HOX** (mano-pie-genital, *HOXA13*), **PAX** (aniridia, *PAX6*), **TBX** (Holt-Oram, *TBX5*).
8. **Dismorfología**: estudia las anomalías estructurales congénitas. Mecanismos: **malformación** (defecto intrínseco primario), **deformación** (fuerza mecánica sobre tejido normal), **disrupción** (destrucción de tejido normal), **displasia** (organización celular anormal).
9. Patrones: **malformación aislada**, **asociación** (VACTERL), **secuencia** (Pierre Robin) y **síndrome** (Down, Marfan).
10. ~**3 %** de los recién nacidos vivos tiene malformaciones significativas. **Tres o más anomalías menores** → ~**90 %** tiene una anomalía mayor: hay que buscarla.

---

### 2.1 Introducción *(Diap. 2–6)*

#### Definición *(Diap. 4)*

📌 **Rama de la genética que estudia cómo los genes controlan el desarrollo embrionario.** Se estudia tanto el **desarrollo normal** como sus **alteraciones**. Las imágenes de la clase muestran moscas (*Drosophila*) mutantes, por ejemplo con patas en lugar de antenas.

La portada *(Diap. 1)* muestra el mismo fenotipo ocular (aniridia) en humano, ratón, pez cebra y mosca: un gen del desarrollo (*PAX6*) está tan conservado que su mutación produce defectos del ojo en especies muy distintas (ver [2.7](#27-genes-pax-diap-3335)).

La cita de apertura *(Diap. 2)* es el párrafo final de *El origen de las especies*: "Hay grandeza en esta concepción de la vida…". ✅ La diapositiva la fecha en 1942, pero el libro es de **1859** (Darwin vivió entre 1809 y 1882).

#### Del cigoto al organismo *(Diap. 5)*

- El organismo humano se origina de **un cigoto** y llega a tener **~200 tipos celulares** diferentes.
- ✅ La diapositiva habla de "10.000 billones de células" (10¹⁶). La estimación aceptada hoy es **~3,7 × 10¹³ (37,2 billones)** en un adulto (Bianconi et al., 2013), la misma cifra que usa la clase de ciclo celular. Libros antiguos daban 10¹⁴.
- La placa de la sonda Pioneer 10 (con dos figuras humanas) ilustra el resultado final de ese programa de desarrollo.

#### Estadios del desarrollo *(Diap. 6)*

| Estadio | Periodo aproximado | Qué ocurre |
|---|---|---|
| **Preembrionario** | Fecundación → semanas 2–3 | Segmentación, mórula, blastocisto, implantación, disco bilaminar |
| **Embrionario** | Semanas 3–8 | Gastrulación, neurulación y **organogénesis** |
| **Fetal** | Semana 9 → nacimiento | Crecimiento y maduración de órganos ya formados |

🩺 ➕ Por eso el **periodo embrionario** es el de mayor riesgo de malformaciones por teratógenos: es cuando se forman los órganos. En las dos primeras semanas rige la regla del **"todo o nada"**: el embrión muere o se recupera sin secuelas.

---

### 2.2 Fertilización, epigenética y gastrulación *(Diap. 7–11)*

#### Fertilización *(Diap. 7)*

📌 Proceso en el cual **un único espermatozoide ingresa al oocito**.

- La diapositiva compara un **oocito maduro** (con **cuerpo polar** visible) y uno **inmaduro** (sin cuerpo polar).
- ➕ El oocito ovulado está detenido en **metafase II**; el primer cuerpo polar indica que completó la meiosis I. La fecundación dispara el fin de la meiosis II (sale el segundo cuerpo polar) y la reacción cortical, que impide la entrada de más espermatozoides (poliespermia).

#### Pérdida de la memoria epigenética *(Diap. 8)*

📌 La metilación del ADN se **borra en dos periodos del desarrollo** (Lee et al., *Cell Stem Cell*, 2014):

1. **Embrión preimplantatorio** (cigoto → blastocisto): desmetilación global. Después de la implantación, el epiblasto vuelve a metilarse y se fijan los linajes somáticos.
2. **Células germinales primordiales (CGP)**: segunda ola, más profunda. ➕ Aquí también se borran las **marcas de impronta**, que luego se restablecen según el sexo durante la gametogénesis. En la primera ola, en cambio, las improntas se conservan.

🩺 ➕ Errores en estas etapas explican trastornos de impronta como Beckwith-Wiedemann, Prader-Willi o Angelman, y el aumento leve de algunos de ellos con técnicas de reproducción asistida.

#### Epigenética *(Diap. 9)*

📌 Área encargada del estudio de los **cambios hereditarios en la expresión génica que no involucran cambios en la secuencia del ADN**. "Epi" = "por encima de".

- Un **mismo genoma** da linajes celulares tan distintos como músculo, glóbulo rojo y neurona, porque cada linaje tiene **marcas epigenéticas** distintas (metilación del ADN, modificaciones de histonas) que encienden o apagan genes.

#### Gastrulación *(Diap. 10)*

📌 Proceso por el cual una **blástula** genera una **gástrula**.

```
Disco bilaminar                  Disco trilaminar
 epiblasto      ── gastrulación ──►   ectodermo
 hipoblasto     (línea primitiva)     mesodermo
                                      endodermo
```

- ➕ En humanos ocurre en la **semana 3**: células del **epiblasto** migran por la **línea primitiva** y forman las tres capas germinales. La notocorda y la placa neural aparecen en este momento.

#### Organogénesis *(Diap. 11)*

📌 Formación de los diferentes **órganos** a partir de las **capas germinales**.

➕ **Derivados de las capas germinales** (pregunta típica)

| Capa | Derivados principales |
|---|---|
| **Ectodermo** | Sistema nervioso (tubo neural), epidermis, pelo, uñas, glándulas cutáneas, esmalte dental, cristalino, adenohipófisis |
| **Cresta neural** (del ectodermo) | Melanocitos, médula suprarrenal, ganglios y células de Schwann, cartílago y hueso craneofacial, odontoblastos |
| **Mesodermo** | Músculo (esquelético, liso, cardiaco), hueso y cartílago, dermis, corazón, vasos y sangre, riñón, gónadas, corteza suprarrenal |
| **Endodermo** | Epitelio del tubo digestivo y respiratorio, hígado, páncreas, tiroides, paratiroides, timo, epitelio de la vejiga |

---

### 2.3 Principios de las familias de genes del desarrollo *(Diap. 12–18)*

#### Tres ideas generales *(Diap. 12)*

1. Existe un **gran número de familias de genes** involucradas en el desarrollo embrionario normal.
2. Se han estudiado en **especies modelo** (mosca, pez cebra, ratón), lo que permitió identificar **vías moleculares o cascadas conservadas** a través de la evolución.
3. Mutaciones en estos genes pueden causar **malformaciones aisladas o formas sindromáticas**.

#### Factores de transcripción *(Diap. 13)*

- Varios genes del desarrollo son **factores de transcripción (TF)** o participan en la **regulación de la expresión génica**.
- Sin TF, la ARN polimerasa transcribe poco. Con ellos (proteínas de unión al ADN en promotores y potenciadores, *enhancers*, más coactivadores), la transcripción de un gen concreto se activa en el tejido y el momento correctos.

#### Ejemplo: malformación mano-pie hendida 1 (ectrodactilia) *(Diap. 14–15)*

| | |
|---|---|
| Frecuencia (según la clase) | 1:90.000 recién nacidos vivos |
| Herencia | **Autosómica dominante**; gen ***DLX5***. Pueden existir otros genes comprometidos o causas no genéticas |
| Clínica | **Afalangia terminal o adactilia (ectrodactilia)**, displasia ectodérmica, labio y paladar hendido |
| Etiología molecular | Mutaciones en ***DLX5*** o en sus **regiones regulatorias** |
| Manejo | Quirúrgico (paladar hendido, extremidades) y odontológico |
| Modelos | Ratones *knockout* de *Dlx5/6* y *Msx2* reproducen la ectrodactilia (Vieux-Rochas et al., 2013) |

- **Ectrodactilia** = ausencia de los radios centrales de manos o pies, que dejan una hendidura en forma de "pinza de langosta".
- ⚠️✅ La tríada **ectrodactilia + displasia ectodérmica + labio/paladar hendido** corresponde al **síndrome EEC**, y el caso que cita la diapositiva (Bharati et al., 2020) es precisamente un síndrome EEC. La causa más frecuente del EEC es ***TP63***. La **SHFM1** "pura" se debe a alteraciones de la región 7q21.3 (*DLX5/DLX6* y sus potenciadores) y puede acompañarse de sordera neurosensorial. MedlinePlus estima la frecuencia de las malformaciones mano-pie hendida en 1 por cada 8.500–25.000 nacimientos.
- 🧠 Lo que sí ilustra bien el ejemplo: una mutación en una **región regulatoria** (no en el gen) basta para causar la malformación, porque altera **dónde y cuándo** se expresa el TF.

#### Los procesos del desarrollo *(Diap. 16)*

El desarrollo normal es una **serie compleja y altamente coordinada de pasos secuenciales y bucles de retroalimentación**, controlada por **redes regulatorias** de genes. Regula estos procesos celulares:

| Proceso | ➕ Qué es | Ejemplo |
|---|---|---|
| **Inducción** | Un grupo de células cambia el destino de otro mediante señales | La notocorda induce la placa neural |
| **Segmentación** | División del eje corporal en unidades repetidas | Somitas, segmentos de *Drosophila* |
| **Migración** | Desplazamiento de células a su sitio final | Cresta neural, células germinales primordiales |
| **Diferenciación** | Adquisición de una identidad especializada | Mioblasto → fibra muscular |
| **Apoptosis** | Muerte celular programada | Separación de los dedos; si falla → sindactilia |

#### Reprogramación celular por factores de transcripción *(Diap. 17–18)*

- 📌 **Premio Nobel de Fisiología o Medicina 2012**: **John B. Gurdon** y **Shinya Yamanaka**, "por el descubrimiento de que las células maduras pueden ser reprogramadas para volverse pluripotentes".
  - ➕ Gurdon (1962): transfirió el núcleo de una célula intestinal de renacuajo a un óvulo enucleado de rana y obtuvo renacuajos normales. El núcleo de una célula diferenciada conserva toda la información.
  - ➕ Yamanaka (2006 en ratón; 2007 en humano): **cuatro factores de transcripción** (OCT3/4, SOX2, KLF4 y c-MYC) convierten fibroblastos en **células madre pluripotentes inducidas (iPSC)**.
- La diapositiva 18 muestra el artículo de 2007 (*Cell* 131:861–872): fibroblastos humanos adultos → iPSC → neuronas, cardiomiocitos y teratomas con tejidos de las tres capas germinales (prueba de pluripotencia).
- Idea clave: los TF del desarrollo no solo construyen el embrión; bastan unos pocos para **reescribir la identidad** de una célula adulta.

---

### 2.4 Morfógenos y patrones de desarrollo temprano *(Diap. 19–22)*

#### Morfógenos *(Diap. 19)*

📌 **Morfógeno**: sustancia cuya **distribución no uniforme** gobierna el patrón de desarrollo del tejido durante la **morfogénesis**.

- **Alan Turing (1912–1954)** propuso el concepto en ***The Chemical Basis of Morphogenesis*** (1952): sustancias que reaccionan y difunden pueden generar patrones espontáneamente.
- ➕ Cómo funciona: el morfógeno sale de una fuente y forma un **gradiente de concentración**. Las células leen la concentración local: por encima de un umbral activan unos genes y por debajo otros (modelo de la "bandera francesa" de Wolpert).
- ➕ Ejemplos: **Bicoid** (eje anteroposterior de *Drosophila*), **Sonic hedgehog** desde la zona de actividad polarizante (identidad de los dedos), **ácido retinoico**, **BMP** y **Wnt**.

#### Nobel 1995 y la cascada de segmentación de *Drosophila* *(Diap. 20–22)*

- 📌 **Premio Nobel de Fisiología o Medicina 1995**: **Edward B. Lewis** (1918–2004), **Christiane Nüsslein-Volhard** (1942) y **Eric F. Wieschaus** (1947), "por sus descubrimientos sobre el control genético del desarrollo embrionario temprano".
- Nüsslein-Volhard y Wieschaus, ***Mutations affecting segment number and polarity in Drosophila*** (*Nature* 287, 30 de octubre de 1980): mutagenizaron moscas en masa y clasificaron las larvas según cómo se alteraban sus segmentos.
- Lewis estudió los **genes homeóticos** (complejo *bithorax*).

📌 **La cascada jerárquica** *(Diap. 22)*: cada nivel regula al siguiente y el embrión se divide en regiones cada vez más finas.

| Nivel | Qué hace | Ejemplo |
|---|---|---|
| 1. **Genes de efecto materno** | Gradientes de ARNm/proteína depositados por la madre en el huevo; definen los ejes | *bicoid* |
| 2. **Genes *gap*** | Dividen el embrión en grandes regiones; su pérdida deja "huecos" de varios segmentos | *hunchback*, *Krüppel* |
| 3. **Genes de regla par** (*pair-rule*) | Patrón de 7 bandas; su pérdida elimina segmentos alternos | *even-skipped*, *fushi tarazu* |
| 4. **Genes de polaridad segmentaria** | Definen la parte anterior y posterior de cada segmento | *engrailed*, *wingless*, *hedgehog* |
| 5. **Genes homeóticos (Hox)** | Dan **identidad** a cada segmento (qué estructura forma) | *Antennapedia*, *Ultrabithorax* |

🧠 **"Mamá Gap Para Polaridad Homeótica"**: Materno → *Gap* → *Pair-rule* → Polaridad segmentaria → Homeóticos.

*(Diap. 23: actividad de quiz en clase.)*

---

### 2.5 Superfamilia TGF-β *(Diap. 24–27)*

#### Qué es *(Diap. 24–25)*

📌 **33 miembros** identificados, constituidos por **factores de crecimiento y citoquinas**:

- **BMP** (*bone morphogenetic proteins*) y **GDF** (*growth differentiation factors*).
- **TGF-β**, **activinas**, **Nodal** y **miostatina**.

Participan en un gran número de procesos celulares y del desarrollo: proliferación, migración, formación de hueso, especificación del eje dorsoventral, gastrulación, crecimiento celular y metástasis, dendritogénesis y transporte axonal.

➕ **Señalización (lo que muestra el esquema de la Diap. 24)**

```
Ligando (dímero) → receptor tipo II (Ser/Thr cinasa) → fosforila receptor tipo I (ALK)
  → fosforila R-SMAD:  SMAD2/3 (TGF-β, activina, Nodal)  |  SMAD1/5/8 (BMP)
  → R-SMAD + SMAD4 (co-SMAD) → núcleo → transcripción de genes diana
  (SMAD6/7 inhiben la vía)
```

➕ **Enfermedades por la vía TGF-β** (útiles para conectar con otras clases)

| Gen | Enfermedad |
|---|---|
| *TGFBR1/2*, *SMAD3* | Síndrome de Loeys-Dietz (aneurismas) |
| *ACVR1* (ALK2), ganancia de función | Fibrodisplasia osificante progresiva |
| *ENG*, *ACVRL1* (ALK1) | Telangiectasia hemorrágica hereditaria |
| *SMAD4*, *BMPR1A* | Poliposis juvenil |
| *MSTN* (miostatina), pérdida de función | Hipertrofia muscular |

#### Ejemplo: osteogénesis imperfecta tipo XIII *(Diap. 26–27)*

| | |
|---|---|
| Incidencia | OI (todas las formas): 6–7 por 100.000 |
| Herencia | **Autosómica recesiva** |
| Clínica | Escleras ligeramente azules, deficiencia grave del crecimiento, osteoporosis limítrofe, **alto riesgo de fracturas (10–15 por año)**, deformidad ósea grave |
| Etiología molecular | ***BMP1*** |
| Manejo | Sintomático: ortopedia, rehabilitación, otorrinolaringología, pediatría y **bifosfonatos** |

- ➕ Mecanismo: la proteína BMP1 es la **proteinasa C del procolágeno**. Corta el propéptido C del procolágeno tipo I; sin ese corte las fibrillas de colágeno se ensamblan mal y el hueso es frágil.
- ⚠️✅ **BMP1 no pertenece a la superfamilia TGF-β**, a pesar de su nombre. Es una **metaloproteasa de zinc de la familia astacina** que se purificó junto con las BMP verdaderas en extractos de hueso. Se relaciona con la vía TGF-β porque procesa proteínas que la regulan (libera BMP de su inhibidor cordina y activa miostatina).
- 💊 Los **bifosfonatos** inhiben la resorción ósea por osteoclastos y reducen las fracturas.

---

### 2.6 Genes homeobox (HOX) *(Diap. 28–32)*

#### Concepto *(Diap. 28–29)*

📌 **Genes homeóticos**: relacionados con la **identidad de los segmentos**. **Especifican el destino celular** y ayudan a establecer los **patrones embrionarios tempranos**.

- ➕ El **homeobox** es una secuencia de **180 pb** que codifica un **homeodominio de 60 aminoácidos** que se une al ADN (hélice-giro-hélice). Las proteínas HOX son factores de transcripción.
- **Mutantes clásicos de *Drosophila*** (*Diap. 28*):
  - ***Antennapedia***: crecen **patas en lugar de antenas**.
  - ***Ultrabithorax***: el tercer segmento torácico se transforma en el segundo y la mosca tiene **cuatro alas** (dos pares) en lugar de dos alas y dos balancines.
- Una **mutación homeótica** transforma una parte del cuerpo en otra: la estructura es normal, pero aparece en el sitio equivocado.

#### HOX en humanos *(Diap. 30)*

- 📌 Los humanos tenemos **39 genes HOX** en **4 *clusters***: ➕ *HOXA* (7p15), *HOXB* (17q21), *HOXC* (12q13) y *HOXD* (2q31).
- 📌 **Colinearidad**: el orden de los genes en el cromosoma coincide con el orden de su expresión a lo largo del eje anteroposterior. Los genes del extremo 3′ se expresan antes y en regiones más anteriores; los del 5′, después y más atrás.
- **Alta conservación evolutiva**: el mismo orden existe en la mosca y en el ratón.
- La clase señala que las mutaciones en estos genes **conducen a menudo a letalidad fetal**. ➕ Matiz: los síndromes HOX humanos conocidos son compatibles con la vida y afectan sobre todo extremidades y genitales (*HOXA13*, *HOXD13*), en parte porque los genes parálogos de distintos *clusters* se compensan entre sí.

#### Ejemplo: síndrome mano-pie-genital *(Diap. 31–32)*

| | |
|---|---|
| Incidencia | Muy baja, no estimada |
| Herencia | **Autosómica dominante** |
| Clínica | **Acortamiento del primer y quinto dedo**; **hipospadias** en hombres; **útero bicorne** en mujeres |
| Etiología molecular | Mutaciones en ***HOXA13*** (en el homeodominio, según el caso de Imagawa et al., 2014) |
| Manejo | Sintomático; urología |

- 🧠 *HOXA13* se expresa en las partes **distales** de las extremidades (manos, pies) y en el seno urogenital: por eso un solo gen afecta **manos, pies y genitales**.
- ➕ Pariente cercano: *HOXD13* causa **sinpolidactilia**.

---

### 2.7 Genes PAX *(Diap. 33–35)*

#### Concepto *(Diap. 33–34)*

- 📌 ***Paired-box***: secuencia de ADN **altamente conservada** que codifica un **dominio de unión al ADN regulador de la transcripción** de ~130 aminoácidos (✅ la cifra exacta es 128).
- Estructura de PAX3: dominio *paired* (PB), homeodominio (HD) y región rica en prolina, serina y treonina (PST). Los dos primeros forman el **dominio de unión al ADN (DBD)**; la región PST es el **dominio de transactivación (TAD)**.
- 📌 **9 genes PAX** en humanos, relacionados con varias enfermedades genéticas.

➕ **PAX y enfermedad**

| Gen | Enfermedad |
|---|---|
| *PAX2* | Síndrome renal-coloboma |
| *PAX3* | **Síndrome de Waardenburg** tipos 1 y 3 (sordera, mechón blanco, heterocromía); fusión PAX3-FOXO1 en rabdomiosarcoma alveolar |
| ***PAX6*** | **Aniridia**; síndrome WAGR (deleción 11p13 que incluye *WT1* y *PAX6*) |
| *PAX8* | Hipotiroidismo congénito (disgenesia tiroidea) |
| *PAX9* | Oligodoncia (agenesia dental) |

#### PAX6 y la aniridia *(Diap. 35)*

- 📌 **Mutaciones en *PAX6* causan aniridia** (ausencia total o parcial del iris), un fenotipo que se puede **recapitular en diversos modelos**: humano, ratón (*Small eye*), pez cebra y *Drosophila* (*eyeless*).
- ➕ La aniridia es **autosómica dominante** por **haploinsuficiencia**: una sola copia funcional no basta.
- ➕ *PAX6* es el "gen maestro" del ojo: su expresión forzada en patas o alas de *Drosophila* produce ojos ectópicos (Gehring, 1995).

---

### 2.8 Otras familias génicas *(Diap. 36–37)*

📌 Otras familias involucradas en el desarrollo *(Diap. 36)*:

| Familia | ➕ Ejemplos y enfermedades |
|---|---|
| **SOX** (*SRY-type HMG box*) | *SRY* (determinación testicular), *SOX9* (displasia campomélica con reversión sexual), *SOX10* (Waardenburg tipo 4 con Hirschsprung) |
| **T-box (TBX)** | ***TBX5* (Holt-Oram)**, *TBX1* (rasgos del síndrome de deleción 22q11.2), *TBX3* (síndrome cubital-mamario) |
| **Dedos de zinc** | *GLI3* (Greig, Pallister-Hall), *WT1* (tumor de Wilms) |
| **Transducción de señales (vía RAS-MAPK)** | RASopatías: Noonan (*PTPN11*), neurofibromatosis tipo 1 (*NF1*), Costello (*HRAS*) |
| **Receptores de FGF (FGFR)** | *FGFR3* (acondroplasia), *FGFR2* (Apert, Crouzon) |

#### Ejemplo: síndrome de Holt-Oram (HOS) *(Diap. 37)*

| | |
|---|---|
| Prevalencia | 0,7–1 por 100.000 recién nacidos vivos |
| Herencia | **Autosómica dominante** |
| Clínica | **Cardiopatía congénita** (➕ sobre todo comunicación interauricular e interventricular), **anomalías de miembros superiores** (➕ radio, pulgar, huesos del carpo) y **alteraciones de la conducción cardiaca** |
| Gen | ***TBX5*** (identificado en 1997) |
| Modelo | Ratones con un solo alelo funcional de *Tbx5* reproducen el síndrome (Bruneau et al., 2001) |

🧠 **"Corazón y mano" = Holt-Oram = TBX5.** Los miembros inferiores no se afectan.

*(Diap. 38: actividad de quiz en clase.)*

---

### 2.9 Principios de dismorfología *(Diap. 39–50)*

#### Definiciones *(Diap. 39)*

- 📌 **Dismorfología**: área que estudia las **anomalías o malformaciones estructurales congénitas** (presentes al nacimiento).
- 📌 **Dismórfico**: describe **hallazgos físicos que no se encuentran normalmente** en individuos de la **misma edad o ancestría**. La comparación con la familia y el grupo étnico evita "sobrediagnosticar" rasgos normales.

#### Los cuatro mecanismos *(Diap. 40–43)*

| Mecanismo | Definición de la clase | ¿El tejido era normal? | Ejemplos | ➕ Pronóstico y recurrencia |
|---|---|---|---|---|
| **Malformación (anomalía)** | **Defecto estructural primario** por una **alteración intrínseca** en la formación del tejido; ocurre a menudo **antes de las 10 semanas** | No: nunca se formó bien | Labio y paladar hendido (queilopalatosquisis), ectrodactilia | Variable; depende de la causa (genética o multifactorial) |
| **Deformación** | Tejido **normal** alterado por **fuerzas mecánicas anormales** (distorsión) | Sí | Oligohidramnios → artrogriposis | Suele mejorar al retirar la fuerza; recurrencia baja |
| **Disrupción** | **Destrucción** de un tejido que era **previamente normal** | Sí | **Bandas amnióticas** (amputaciones, constricciones) | Recurrencia baja (causa extrínseca) |
| **Displasia** | **Organización celular anormal** de un tejido que produce cambios estructurales | No: el tejido está mal organizado en todas partes | **Displasias esqueléticas** | A menudo genética |

🧠 **Pregúntate dos cosas**: ¿el tejido se formó bien al principio? (no → malformación o displasia; sí → deformación o disrupción). Si se formó bien, ¿lo **presionaron** (deformación) o lo **rompieron** (disrupción, del inglés *disruption*, ruptura)? Si no se formó bien, ¿falla un **órgano o estructura** (malformación) o la **organización celular de un tejido** en todo el cuerpo (displasia)?

⚠️ Diferencia examinable entre deformación y disrupción: en ambas el tejido era normal, pero en la **deformación se distorsiona** (presión) y en la **disrupción se destruye** (banda, isquemia).

#### Los patrones *(Diap. 44–47)*

| Patrón | Definición | Ejemplo de la clase |
|---|---|---|
| **Malformación aislada** | **No** existen otras malformaciones asociadas | Braquidactilia, válvula aórtica bicúspide |
| **Asociación** | Grupo de malformaciones que ocurren juntas **más de lo esperado por azar**, **sin un patrón etiológico unificado o conocido** | **VACTERL** |
| **Secuencia** | Patrón de múltiples anomalías que resultan de **una única anomalía primaria** (en cascada) | **Pierre Robin** |
| **Síndrome** | **Patrón reconocible** de malformaciones o hallazgos, a menudo con una **causa molecular subyacente conocida** | Síndrome de Down, síndrome de Marfan |

**VACTERL** *(Diap. 45)*: **V**ertebrales (defectos), **A**tresia anal, **C**ardiacos (defectos), **T**raqueo**E**sofágica (fístula), **R**enales (anomalías), **L**imb = extremidades (anomalías). ➕ Se sugiere con 3 o más.

**Secuencia de Pierre Robin** *(Diap. 46)*:

```
Factor mecánico → flexión de la mandíbula → micrognatia → glosoptosis (lengua cae hacia atrás)
               → obstrucción de la vía aérea superior → problemas respiratorios (± paladar hendido en U)
```

⚠️ La clase define la secuencia como cascada desde "una única malformación primaria". ➕ El evento inicial también puede ser una deformación (como en este ejemplo, por compresión) o una disrupción. Otro ejemplo clásico es la **secuencia de Potter**: oligohidramnios (por agenesia renal) → hipoplasia pulmonar, facies de Potter y deformidades de extremidades.

#### Impacto de las malformaciones *(Diap. 48)*

- Alrededor del **3 % de los recién nacidos vivos** tiene malformaciones congénitas significativas.
- Son responsables de una proporción importante de las **muertes neonatales e infantiles** (➕ en EE. UU., ~20 % de las muertes infantiles).
- Son causa importante de **hospitalización pediátrica**.
- Son **signos de patologías genéticas subyacentes**.

#### Anomalías mayores frente a menores *(Diap. 49)*

| | Mayores | Menores |
|---|---|---|
| Gravedad | **Severas**: alteran la funcionalidad y **requieren manejo** médico o quirúrgico | **Primariamente cosméticas** |
| Distribución | Aisladas o en varios sistemas | Ocurren de manera variable en la **población normal** |
| Utilidad | — | **Útiles para el diagnóstico** (pistas de un síndrome) |
| Ejemplo | Espina bífida (mielomeningocele) | Fosita o apéndice preauricular |

#### Prevalencia de anomalías menores *(Diap. 50)*

| Hallazgo | Frecuencia en recién nacidos | Riesgo de anomalía mayor asociada |
|---|---|---|
| **Una** anomalía menor | **15 %** | **3 %** |
| **Dos** anomalías menores | Menos comunes | **11 %** |
| **Tres o más** anomalías menores | No usuales (**1 %**) | **90 %** |

- **42 %** de los casos de **déficit cognitivo idiopático** tienen **tres o más anomalías**; el **80 %** de ellas son menores.
- **71 %** de las anomalías menores están en **cabeza, cuello y manos**.

🩺 ➕ Aplicación práctica: un recién nacido con 3 o más anomalías menores debe estudiarse en busca de una anomalía mayor oculta (ecocardiograma, ecografía renal, valoración por genética). El examen físico dismorfológico empieza por **cabeza, cuello y manos**.

🧠 **"1-2-3 → 3-11-90"**: una, dos, tres anomalías menores → 3 %, 11 %, 90 % de riesgo de anomalía mayor.

---

### ✅ Verificación de datos de la clase (capítulo 2)

| Diapositiva | Dice | Verificación |
|---|---|---|
| 2 | Darwin (1942) | *El origen de las especies* es de **1859**; Darwin murió en 1882 |
| 5 | 10.000 billones de células | Estimación actual: **~3,7 × 10¹³** (37,2 billones; Bianconi 2013) |
| 14 | Ectrodactilia + displasia ectodérmica + fisura = SHFM1 (*DLX5*) | Esa tríada es el **síndrome EEC** (*TP63* en la mayoría); el caso citado es un EEC ([Bharati 2020](https://pubmed.ncbi.nlm.nih.gov/32257456/)). SHFM1 = región 7q21.3 (*DLX5/DLX6*) |
| 26–27 | OI XIII dentro de la superfamilia TGF-β | *BMP1* es una **metaloproteasa astacina** (proteinasa C del procolágeno), **no** un miembro TGF-β ([NCBI GTR](https://www.ncbi.nlm.nih.gov/gtr/genes/649); [Martínez-Glez 2012](https://pubmed.ncbi.nlm.nih.gov/22052668/)) |
| 33 | Dominio *paired* de 130 aa | 128 aa |
| 37 | TBX5: "Yi Li et al., *Nature*, 1997" | La revista es *Nature Genetics* (Li QY et al., 1997;15:21-29) |
| 41 | "Artogrifosis" | **Artrogriposis** |
| 46 | "Glosoptsis" | **Glosoptosis** |

---

### Autoevaluación (capítulo 2)

<details><summary>1. ¿Qué diferencia la primera ola de desmetilación (embrión preimplantatorio) de la segunda (células germinales primordiales)?</summary>

En la primera se conservan las marcas de impronta; en las CGP se borran también las improntas, que se restablecen según el sexo en la gametogénesis.
</details>

<details><summary>2. Ordena la cascada de segmentación de Drosophila.</summary>

Efecto materno (*bicoid*) → *gap* (*hunchback*) → regla par (*even-skipped*, *fushi tarazu*) → polaridad segmentaria (*engrailed*) → homeóticos (*Antennapedia*, *Ultrabithorax*).
</details>

<details><summary>3. Una mosca tiene patas donde deberían estar las antenas. ¿Qué tipo de gen está mutado?</summary>

Un gen homeótico (Hox): *Antennapedia*. La estructura es normal pero aparece en el segmento equivocado.
</details>

<details><summary>4. Recién nacido con oligohidramnios por rotura prematura de membranas y pie equinovaro. ¿Malformación, deformación o disrupción?</summary>

Deformación: un tejido normal distorsionado por fuerzas mecánicas (falta de líquido amniótico).
</details>

<details><summary>5. Niño con amputación congénita de dos dedos y anillos de constricción en la pierna. ¿Mecanismo?</summary>

Disrupción por bandas amnióticas: destrucción de tejido que se había formado normalmente.
</details>

<details><summary>6. ¿Por qué VACTERL es una asociación y no un síndrome?</summary>

Porque sus anomalías ocurren juntas más de lo esperado por azar, pero sin una causa etiológica unificada conocida.
</details>

<details><summary>7. Mujer con útero bicorne y pulgares cortos; su hijo tiene hipospadias. ¿Gen sospechoso?</summary>

*HOXA13* (síndrome mano-pie-genital, autosómico dominante).
</details>

<details><summary>8. Niño con comunicación interauricular, pulgar trifalángico y bloqueo AV. ¿Síndrome y gen?</summary>

Holt-Oram, *TBX5*.
</details>

<details><summary>9. Un recién nacido tiene tres anomalías menores. ¿Qué probabilidad hay de una anomalía mayor y qué haces?</summary>

~90 %. Buscar activamente la anomalía mayor (ecocardiograma, ecografía renal, valoración por genética).
</details>

---

### Glosario (capítulo 2)

| Término | Definición |
|---|---|
| **Asociación** | Anomalías que coinciden más de lo esperado sin causa unificada conocida |
| **Colinearidad** | Correspondencia entre el orden de los genes HOX en el cromosoma y su orden de expresión en el eje corporal |
| **Deformación** | Distorsión de un tejido normal por fuerzas mecánicas |
| **Displasia** | Organización celular anormal dentro de un tejido |
| **Disrupción** | Destrucción de un tejido previamente normal |
| **Ectrodactilia** | Ausencia de los radios centrales de manos o pies |
| **Epigenética** | Cambios heredables de expresión génica sin cambio de secuencia del ADN |
| **Gastrulación** | Paso de blástula a gástrula; formación de las tres capas germinales |
| **Homeobox** | Secuencia de 180 pb que codifica el homeodominio (60 aa) de unión al ADN |
| **iPSC** | Célula madre pluripotente inducida por factores de transcripción |
| **Malformación** | Defecto estructural primario por alteración intrínseca del desarrollo |
| **Morfógeno** | Sustancia cuya distribución no uniforme establece el patrón de un tejido |
| **Secuencia** | Cascada de anomalías derivadas de una sola anomalía primaria |
| **Síndrome** | Patrón reconocible de anomalías, a menudo con causa molecular conocida |

---

### Referencias (capítulo 2)

De la clase:

- Turnpenny P, Ellard S, Cleaver R. *Emery's Elements of Medical Genetics and Genomics.* Elsevier.
- Lee HJ, Hore TA, Reik W. Reprogramming the methylome: erasing memory and creating diversity. *Cell Stem Cell.* 2014.
- Takahashi K, et al. Induction of pluripotent stem cells from adult human fibroblasts by defined factors. *Cell.* 2007;131:861-872.
- Turing AM. The chemical basis of morphogenesis. *Phil Trans R Soc Lond B.* 1952;237:37-72.
- Nüsslein-Volhard C, Wieschaus E. Mutations affecting segment number and polarity in *Drosophila*. *Nature.* 1980;287:795-801.
- Martínez-Glez V, et al. *Hum Mutat.* 2012;33:343-350 (BMP1 y OI recesiva).
- Imagawa E, et al. *Am J Med Genet A.* 2014 (*HOXA13*).
- Li QY, et al. *Nat Genet.* 1997;15:21-29; Bruneau BG, et al. *Cell.* 2001 (*TBX5*).

Usadas en la verificación:

- Bianconi E, et al. An estimation of the number of cells in the human body. *Ann Hum Biol.* 2013;40:463-471.
- Bharati A, et al. EEC syndrome: a case report. *Case Rep Dent.* 2020. <https://pubmed.ncbi.nlm.nih.gov/32257456/>
- NCBI Genetic Testing Registry, gen *BMP1*: <https://www.ncbi.nlm.nih.gov/gtr/genes/649>
- MedlinePlus Genetics: *Split-hand/foot malformation*.

[↑ Volver al índice general](#índice-general)

---

## 3. Ciclo celular: fases, motor molecular y puntos de control

> Clase de la Prof. **Sandra Yaneth Ospina Lagos** (MD, MSc), Facultad de Medicina, Universidad Nacional de Colombia, tercer semestre, 2026.
> Las citas *(Diap. N)* siguen la numeración de las diapositivas. Los símbolos 📌 ➕ ⚠️ ✅ 🩺 💊 🧠 se explican al [inicio de la guía](#cómo-usar-esta-guía).
> Conecta directamente con el capítulo 5, [reparación del ADN](#5-mecanismos-de-reparación-del-adn-de-la-lesión-molecular-a-la-clínica) (puntos de control, ATM/ATR, p53, BRCA).

---

### Índice (capítulo 3)

- [Lo esencial en un minuto](#lo-esencial-en-un-minuto-capítulo-3)
- [3.1 Teoría celular y por qué dividirse](#31-teoría-celular-y-por-qué-dividirse-diap-35)
- [3.2 Las fases del ciclo y su duración](#32-las-fases-del-ciclo-y-su-duración-diap-79)
- [3.3 Fase G1 y el estado G0](#33-fase-g1-y-el-estado-g0-diap-1114)
- [3.4 Fase S: el genoma se copia una sola vez](#34-fase-s-el-genoma-se-copia-una-sola-vez-diap-1516-19)
- [3.5 Fase G2](#35-fase-g2-diap-17)
- [3.6 Fase M: mitosis y citocinesis](#36-fase-m-mitosis-y-citocinesis-diap-18)
- [3.7 El experimento de fusión celular](#37-el-experimento-de-fusión-celular-diap-20)
- [3.8 El motor: CDK y ciclinas](#38-el-motor-cdk-y-ciclinas-diap-2226)
- [3.9 Los seis niveles de regulación de las CDK](#39-los-seis-niveles-de-regulación-de-las-cdk-diap-2734)
- [3.10 El ciclo como sistema de osciladores](#310-el-ciclo-como-sistema-de-osciladores-diap-35)
- [3.11 Mitógenos y punto de restricción](#311-mitógenos-y-punto-de-restricción-diap-3839)
- [3.12 Puntos de control](#312-puntos-de-control-diap-4042)
- [3.13 Respuesta al daño del ADN y p53](#313-respuesta-al-daño-del-adn-y-p53-diap-4345)
- [3.14 Punto de control del huso (SAC)](#314-punto-de-control-del-huso-sac-diap-46)
- [3.15 Tres frenos sobre el mismo motor](#315-tres-frenos-sobre-el-mismo-motor-diap-47)
- [3.16 microARN](#316-microarn-diap-48-51)
- [3.17 Quiescencia frente a senescencia](#317-quiescencia-frente-a-senescencia-diap-49)
- [3.18 Mapa integrador e ideas clave](#318-mapa-integrador-e-ideas-clave-diap-5052)
- [3.19 ➕ Del ciclo celular a la clínica](#319--del-ciclo-celular-a-la-clínica)
- [✅ Verificación de datos de la clase](#-verificación-de-datos-de-la-clase-capítulo-3)
- [Autoevaluación](#autoevaluación-capítulo-3)
- [Glosario](#glosario-capítulo-3)
- [Referencias](#referencias-capítulo-3)

---

### Objetivos de aprendizaje (capítulo 3) *(Diap. 3)*

1. **Describir las fases** G1, S, G2, M y G0: qué ocurre en cada una y cuánto dura.
2. **Explicar el motor del ciclo**: cómo las ciclinas y las CDK impulsan el paso entre fases.
3. **Integrar las señales**: cómo los mitógenos y la vía Rb–E2F comprometen a la célula a dividirse.
4. **Analizar los puntos de control**: sensores, transductores y efectores que detienen el ciclo ante errores.

La diapositiva 2 (una orquesta) resume la idea: muchos instrumentos (proteínas) deben entrar en el momento exacto y en el orden correcto, bajo un director.

---

### Lo esencial en un minuto (capítulo 3)

1. **Interfase = G1 + S + G2** (~95 % del ciclo). En una célula humana en cultivo el ciclo dura ~24 h: **G1 11 h, S 8 h, G2 4 h, M 1 h**.
2. **G1 es la fase más variable** y la que decide: continuar, esperar o salir a **G0**.
3. Las **CDK** están siempre presentes; lo que **oscila son las ciclinas**. Secuencia: **D–CDK4/6 (G1) → E–CDK2 (G1/S) → A–CDK2 (S) → A/B–CDK1 (G2/M)**.
4. La actividad de las CDK se regula en **seis niveles**: unión de ciclina, fosforilación activadora (CAK), fosforilación inhibidora (Wee1), desfosforilación activadora (Cdc25), inhibidores (CKI: INK4 y CIP/KIP) y proteólisis (SCF y APC/C).
5. **Punto de restricción (R)**: mitógenos → ciclina D → **fosforilación de Rb → liberación de E2F** → genes de fase S. Tras cruzarlo, la célula completa el ciclo aunque se retiren los mitógenos.
6. **El ADN se replica una sola vez**: el licenciamiento (carga de MCM) solo ocurre con **CDK baja (G1)** y el disparo con **CDK alta (S)**.
7. **Puntos de control**: G1/S, intra-S, G2/M y huso (SAC). Lógica **sensor → transductor → efector**.
8. **Daño del ADN**: **ATM → CHK2 → p53 → p21** (arresto G1/S) y **ATR → CHK1 → Cdc25 inactiva** (arresto intra-S y G2/M).
9. **p53**, "guardián del genoma": sin daño, **MDM2** lo degrada; con daño, se fosforila, se estabiliza e induce **p21** (arresto), **reparación** o **PUMA/BAX/NOXA** (apoptosis). **p53 no es una CKI.**
10. **SAC**: un solo cinetocoro sin unir activa MAD2/BUBR1/BUB3, que inhiben **APC/C–Cdc20**. Al unirse todos, el APC/C degrada **securina** y **ciclina B**, la **separasa** corta la cohesina y empieza la anafase.
11. **G0 (quiescencia) es reversible; la senescencia no.**

---

### 3.1 Teoría celular y por qué dividirse *(Diap. 3–5)*

#### ¿Qué es una célula? *(Diap. 4)*

📌 **Unidad estructural, funcional y de origen** de todos los seres vivos: el sistema más pequeño, delimitado por una membrana, capaz de mantener la vida de forma independiente y de reproducirse.

#### Línea de tiempo *(Diap. 4)*

| Año | Quién | Aporte |
|---|---|---|
| 1665 | **Robert Hooke** | Ve "celdas" en el corcho y acuña el término **célula** (*Micrographia*) |
| 1674 | **Anton van Leeuwenhoek** | Con lentes propias observa los primeros **microorganismos vivos** |
| 1831 | **Robert Brown** | Describe el **núcleo** como estructura constante de la célula |
| 1838 | **Matthias Schleiden** | Botánico: todas las **plantas** están formadas por células |
| 1839 | **Theodor Schwann** | Zoólogo: los **animales** también. Nace la teoría celular |
| 1855 | **Rudolf Virchow** | **"Omnis cellula e cellula"**: toda célula viene de otra (con Robert Remak, 1852) |
| 1882 | **Walther Flemming** | Describe la **mitosis** y nombra la **cromatina** |

🧠 **"Hooke ve, Leeuwenhoek mira, Brown nuclea, Schleiden planta, Schwann anima, Virchow hereda, Flemming divide."**

#### Postulados de la teoría celular moderna *(Diap. 4)*

1. Todos los seres vivos están formados por **una o más células**.
2. La célula es la **unidad estructural y funcional** de la vida.
3. Toda célula procede de **otra preexistente por división**, y transmite la información hereditaria.

📌 El **postulado 3** es la base de la clase: el ciclo celular es el mecanismo que lo hace posible.

#### ¿Por qué es importante dividirse? *(Diap. 5)*

| Cifra | Significado |
|---|---|
| **37,2 billones** (3,72 × 10¹³) | Células en un adulto, todas derivadas de **un solo cigoto** (Bianconi et al., 2013) |
| **~330.000 millones/día** | Células que se renuevan cada día (~**3,8 millones por segundo**) (Sender y Milo, 2021) |
| **~86 %** de ese recambio | Son **células sanguíneas**; **~12 %**, epitelio intestinal |

Cuatro funciones de la división celular:

1. **Reproducción**: en unicelulares, dividirse es reproducirse.
2. **Desarrollo y crecimiento**: divisiones repetidas convierten al cigoto en un adulto.
3. **Recambio normal**: piel, intestino y médula ósea se renuevan continuamente.
4. **Reparación**: cicatrizar heridas y consolidar fracturas exige proliferación local.

*(Diap. 10, video de HHMI BioInteractive)*: si los reguladores del ciclo fallan, el organismo termina con **muy pocas o demasiadas células** (degeneración o cáncer).

---

### 3.2 Las fases del ciclo y su duración *(Diap. 7–9)*

#### Crecer, copiar, verificar y dividir *(Diap. 7)*

| Fase | Duración típica (célula humana en cultivo, ~24 h) | Qué ocurre |
|---|---|---|
| **G1** | **11 h** | **Crecimiento y decisión**: aumenta de tamaño, sintetiza ARN, proteínas y organelos, y decide si se divide |
| **S** | **8 h** | **Síntesis**: se replica todo el ADN **una sola vez**; cada cromosoma queda con **dos cromátidas hermanas** |
| **G2** | **4 h** | **Preparación**: sigue creciendo, verifica la replicación y sintetiza lo necesario para la mitosis |
| **M** | **1 h** | **Mitosis + citocinesis**: reparte las dos copias del genoma y divide el citoplasma en dos células hijas |

📌 **Interfase = G1 + S + G2 (~95 % del ciclo).** Las células que no se dividen salen a **G0** (quiescencia).

🧠 **"Crecer–Copiar–Comprobar–Cortar"**: G1–S–G2–M.

#### La duración varía de minutos a años *(Diap. 8)*

| Célula | Duración del ciclo |
|---|---|
| Célula embrionaria de rana | **30 min** |
| Levadura | 1,5–3 h |
| Epitelio intestinal | ~12 h |
| Fibroblasto humano en cultivo | ~20 h |
| Célula humana típica | ~24 h |
| Hepatocito humano | **~1 año** |

- 📌 **G1 es la fase más variable**: explica casi todas las diferencias de duración entre tipos celulares.
- **S, G2 y M son más constantes**: S ≈ 6–8 h, G2 ≈ 2–6 h, mitosis + citocinesis ≈ 1 h.
- **Embriones tempranos**: ciclos rápidos **S–M casi sin G1 ni G2**. No crecen; solo dividen el enorme citoplasma del huevo.

#### Duración de las fases según el tipo celular *(Diap. 9)*

| Célula | Ciclo total | G1 | S | G2 + M |
|---|---|---|---|---|
| Humano en cultivo (fibroblastos, células ováricas y de pulmón) | 18–20 h | 2–10 h | 6–7 h | 2,5–3 h |
| Humano in vivo (médula ósea; epitelio de colon, recto y estómago) | 18–48 h | 2–33 h | 10–12 h | 2–5 h |
| Ratón (íleon, duodeno, glándula mamaria, folículo piloso, colon) | 10–71 h | 1,3–45 h | 7–22 h | 1,4–4 h |
| Rata (criptas duodenales, hepatocitos) | 10–47 h | 2,2–28 h | 7–16 h | 1,2–3,5 h |

📌 **Lectura clave**: la columna de **G1 tiene el rango más amplio** (1,3 a 45 h). La célula "decide" en G1 si continúa, espera o sale a G0 según las señales del entorno; por eso es la fase **más regulada y más variable**.

---

### 3.3 Fase G1 y el estado G0 *(Diap. 11–14)*

#### Fase G1: crecimiento y decisión *(Diap. 11)*

- **Inicio**: inmediatamente después de la mitosis anterior.
- **Crecimiento**: aumentan el volumen celular y la actividad metabólica; se duplican los organelos.
- **Preparación de S**: síntesis de nucleótidos y enzimas de replicación, y ensamblaje de los **complejos de prerreplicación (pre-RC)** en los orígenes.
- **Motor**: **ciclina D–CDK4/6** y, al final de G1, **ciclina E–CDK2**.
- **Punto de restricción (R)**: tras cruzarlo, la célula queda **comprometida a completar el ciclo aunque se retiren los mitógenos**.

📌 **Punto de control G1/S: ¿reposo o división?** Verifica:

- ✓ ADN sin daño.
- ✓ Tamaño celular suficiente.
- ✓ Nutrientes y mitógenos presentes.

**Si no se cumplen**: la célula se **detiene para reparar**, **sale a G0** o, si el daño es irreparable, entra en **apoptosis**.

#### Esquema resumen de las transiciones *(Diap. 12)*

```
Señales de crecimiento → ciclina D–CDK4/6 → fosforila Rb → libera E2F → genes de fase S
                                                         → ciclina E–CDK2 → entrada en S
                                    (p21 bloquea a ciclina E–CDK2)
Transición G2/M: ciclina B–CDK1 → mitosis.  Si CDK1–ciclina B queda inactiva → arresto G2/M
```

✅ La imagen de la diapositiva 12 tiene texto ilegible generado automáticamente ("EPFF Efecsa gene de S"); debe leerse **"E2F activa genes de fase S"**.

#### G0 y clasificación de las células por su capacidad de dividirse *(Diap. 13–14)*

📌 Al final de G1 la célula puede **abandonar el ciclo y entrar en G0** cuando recibe una **señal de diferenciación** o cuando **faltan recursos**. **G0 no es inactividad**: la célula mantiene un metabolismo activo y cumple su función.

| Tipo | Comportamiento | Ejemplos |
|---|---|---|
| **Permanentes** | Salen del ciclo **de forma definitiva** al diferenciarse (especialización estructural extrema) | **Neuronas**, **cardiomiocitos**, **fibras musculares esqueléticas**, **eritrocitos** (sin núcleo) |
| **Estables (quiescentes)** | Permanecen en G0 pero **pueden volver a G1** con el estímulo adecuado | **Hepatocitos** (el hígado se regenera tras una hepatectomía), **linfocitos** en reposo activados por antígeno, **fibroblastos** durante la cicatrización |
| **Lábiles** | **Ciclan continuamente** para renovar el tejido | **Epitelios** de piel e intestino, **progenitores de médula ósea** (eritroblastos, megacariocitos, leucoblastos), **células goniales** (espermatogonias) |

🩺 ➕ Consecuencias clínicas:
- Un **infarto** de miocardio o un **ACV** deja cicatriz porque cardiomiocitos y neuronas son permanentes (➕ los cardiomiocitos se renuevan a menos del 1 % por año en el adulto).
- La **quimioterapia** afecta sobre todo a los tejidos lábiles: médula ósea (citopenias), mucosa intestinal (mucositis, diarrea) y folículo piloso (alopecia).
- El músculo esquelético se regenera parcialmente gracias a sus **células satélite**, aunque la fibra madura no se divide.

---

### 3.4 Fase S: el genoma se copia una sola vez *(Diap. 15–16, 19)*

#### Qué ocurre en S *(Diap. 15)*

- **Replicación**: se sintetiza una copia completa del ADN nuclear (**de 2C a 4C**).
- **Histonas**: su transcripción y traducción aumentan intensamente para empaquetar el ADN nuevo en nucleosomas.
- **Resultado**: cada cromosoma queda formado por **dos cromátidas hermanas unidas por cohesinas**. ⚠️ El **número de cromosomas no cambia** (sigue siendo 46 en humanos): se duplica el contenido de ADN, no el número de cromosomas.
- **Centrosoma**: también se duplica durante S.
- **Motor**: **ciclina E–CDK2 dispara el inicio**; **ciclina A–CDK2 sostiene** la replicación.

📌 **Punto de control intra-S: ¿está el ADN sin problemas?** Las horquillas de replicación se vigilan de forma continua. Si se detienen o el ADN se daña (**estrés replicativo**), **ATR–CHK1** frena el disparo de nuevos orígenes y da tiempo a reparar. Verifica que no haya errores durante la copia y que **cada origen dispare una sola vez**.

#### ¿Por qué el ADN se replica solo una vez por ciclo? *(Diap. 16, 19)*

📌 Porque cargar la helicasa y activarla son pasos separados que requieren niveles **opuestos** de actividad CDK.

| Paso | Momento | Qué pasa |
|---|---|---|
| **1. Licenciamiento** | **G1, CDK baja** | **ORC** se une al origen; **Cdc6** y **Cdt1** cargan **MCM2-7** como doble hexámero = **complejo pre-RC "licenciado"** |
| **2. Disparo** | **Fase S, CDK alta** | **CDK + DDK (Cdc7)** activan la **helicasa CMG**; dos horquillas avanzan en direcciones opuestas |
| **3. Bloqueo del re-licenciamiento** | **S, G2 y M** | La **CDK alta fosforila Cdc6** (que se exporta o degrada) **y ORC**, impidiendo cargar nuevas MCM. La **geminina secuestra a Cdt1** hasta que el **APC/C la degrada al final de la mitosis**; en la siguiente G1 el ciclo se reinicia |

🧠 **"Licencia con CDK baja, dispara con CDK alta."** Un origen que ya disparó no puede volver a cargar MCM mientras la CDK siga alta. La única forma de "renovar la licencia" es pasar por la mitosis, cuando el APC/C baja la CDK y destruye la geminina.

✅ El esquema de la diapositiva 19 está generado automáticamente y tiene etiquetas confusas ("CC" dentro de MCM). Usa la tabla de arriba, que coincide con la diapositiva 16.

➕ En la fase S, Cdt1 también se degrada por la ubiquitina-ligasa CRL4-Cdt2, acoplada a PCNA: otra capa de seguridad.

🩺 ➕ Si el control falla, partes del genoma se copian dos veces (**re-replicación**): amplificaciones génicas y estrés replicativo, típicos de células tumorales.

---

### 3.5 Fase G2 *(Diap. 17)*

- **Crecimiento**: continúa el aumento de volumen y la síntesis de proteínas.
- **Preparación**: síntesis de **tubulina** y otras moléculas para la mitosis; **maduración de los centrosomas**.
- **Cromatina**: comienza su **condensación**.
- **Motor**: **ciclina A–CDK1** estabiliza y activa a **ciclina B–CDK1** (**factor promotor de la mitosis, MPF**), que se acumula **inactivo** hasta el final de G2.

📌 **Punto de control G2/M: ¿el equipamiento está completo?**

- ✓ ADN completamente replicado.
- ✓ ADN sin daño.
- ✓ Componentes celulares suficientes.

**Si hay daño**: ATR/ATM → CHK1/CHK2 **inactivan a Cdc25** y la célula **no entra en mitosis** hasta reparar (CDK1 conserva su fosfato inhibidor).

---

### 3.6 Fase M: mitosis y citocinesis *(Diap. 18)*

| # | Etapa | Qué ocurre |
|---|---|---|
| 1 | **Profase** | Los cromosomas se **condensan**; los centrosomas se separan y empieza a formarse el **huso** |
| 2 | **Prometafase** | Se **rompe la envoltura nuclear**; los microtúbulos se unen a los **cinetocoros** |
| 3 | **Metafase** | Los cromosomas se **alinean en la placa ecuatorial**. Aquí actúa el **punto de control del huso** |
| 4 | **Anafase** | Se **separan las cromátidas hermanas** y migran a polos opuestos |
| 5 | **Telofase** | Los cromosomas se **descondensan** y se forma de nuevo la **envoltura nuclear** |
| 6 | **Citocinesis** | El **anillo contráctil de actina y miosina** divide el citoplasma en dos |

🧠 **"PPMATC"**: **P**or **P**rimera **M**ano **A**lguien **T**oca el **C**ello (profase, prometafase, metafase, anafase, telofase, citocinesis).

📌 **Motor**: **ciclina B–CDK1 (MPF)** dispara:
- La **condensación de la cromatina** (vía **condensinas**).
- La **ruptura de la envoltura nuclear** (fosforila las **láminas**).
- El **armado del huso**.

📌 **Para salir de la mitosis**, el **APC/C degrada la ciclina B** y la actividad de CDK1 cae por debajo del umbral. Sin esa caída, la célula no puede descondensar los cromosomas ni rehacer el núcleo.

---

### 3.7 El experimento de fusión celular *(Diap. 20)*

**Rao y Johnson (1970)** fusionaron células en mitosis con células en otras fases. El citoplasma mitótico forzó la **condensación prematura de los cromosomas (PCC)** de la otra célula, y su aspecto reveló en qué fase estaba:

| Fusión | Aspecto de los cromosomas de la célula no mitótica | Interpretación |
|---|---|---|
| **G1 + M** | Largos y delgados, de **una sola cromátida** | El ADN aún no se ha replicado |
| **S + M** | Cromatina **"pulverizada"** en fragmentos | Replicación en curso: se condensan trozos replicados y no replicados |
| **G2 + M** | Largos, con **dos cromátidas** | El ADN ya está duplicado |

📌 **Conclusión**: existe un **factor citoplasmático dominante que induce la mitosis (MPF)**, hoy identificado como **ciclina B–CDK1**.

➕ El MPF se describió en 1971 (Masui y Markert) como "factor promotor de la maduración" en oocitos de rana; en 1988 se demostró que era el complejo CDK1–ciclina B.

---

### 3.8 El motor: CDK y ciclinas *(Diap. 22–26)*

#### Las CDK *(Diap. 22–23)*

- 📌 **Qué son**: **cinasas dependientes de ciclina**. Transfieren fosfato del **ATP** a **serinas y treoninas** de proteínas diana, activándolas o inhibiéndolas.
- 📌 **Siempre presentes**: su concentración es **casi constante**; **lo que oscila es la ciclina** que las activa.
- **Conservadas**: el mismo sistema funciona desde levaduras hasta humanos; varía el número de genes y la complejidad de los puntos de control.
- **Se regulan por**: interacción proteína–proteína (ciclinas, CKI), fosforilación activadora e inhibidora, y proteólisis mediada por ubiquitina.

```
CDK inactiva  ──+ ciclina──►  ciclina–CDK parcialmente activa  ──+ fosfato activador (CAK)──►  complejo totalmente activo
                                                                                                │
                                         proteína diana fosforilada (Rb, láminas, condensinas) ◄┘ → el ciclo avanza
```

➕ **Premio Nobel de Fisiología o Medicina 2001**: Leland Hartwell (genes *CDC* y puntos de control en levadura), Paul Nurse (*cdc2* = CDK1) y Tim Hunt (descubrió las ciclinas en erizo de mar).

#### Las ciclinas aparecen y desaparecen en ondas *(Diap. 24)*

| Ciclina | Cuándo sube | Cuándo cae |
|---|---|---|
| **D** (CDK4/6) | Temprano en G1, **en respuesta a mitógenos** | Se mantiene mientras haya mitógenos |
| **E** (CDK2) | Pico en la **transición G1/S** | Al inicio de S |
| **A** (CDK2, CDK1) | Aumenta durante **S y G2** | Al inicio de la mitosis |
| **B** (CDK1) | Aumenta en **G2**, pico en **M** | **Caída abrupta en la transición metafase-anafase** |

- 📌 **Cada onda prepara la siguiente**: cada complejo activa la transcripción de la ciclina siguiente y ayuda a destruir la anterior. Así el ciclo **avanza en un solo sentido**, sin retroceder.
- 📌 **La ciclina D es distinta**: **no oscila con el ciclo**; su nivel depende de los **mitógenos**. Por eso **conecta el ambiente extracelular con el motor interno**.

#### Cada fase tiene su complejo ciclina–CDK *(Diap. 25–26)*

| Fase | Complejo | Clase de ciclina | Función |
|---|---|---|---|
| **G1** | **Ciclina D–CDK4/6** | Ciclina de G1 | Responde a mitógenos; **inicia la fosforilación de Rb** y la salida de G0/G1 temprana |
| **G1/S** | **Ciclina E–CDK2** | Ciclina de G1/S | **Completa la fosforilación de Rb**, cruza el punto R y **dispara el inicio de la replicación** |
| **S** | **Ciclina A–CDK2** | Ciclina de S | **Mantiene la replicación** y fosforila Cdc6/ORC para **impedir la re-replicación** |
| **G2/M** | **Ciclina A/B–CDK1** | Ciclina de M (**MPF**) | Ciclina A–CDK1 en G2 activa a ciclina B–CDK1, que **conduce la mitosis** |

- Peso molecular de las ciclinas: **36–87 kDa**.
- **Otras CDK** regulan la transcripción más que el avance del ciclo: **CDK7–ciclina H = CAK** (cinasa activadora de CDK; ➕ también forma parte de TFIIH, la misma proteína de la reparación por escisión de nucleótidos), **CDK8** y **CDK9**.

🧠 **"De Esto A Bailar"**: **D** → **E** → **A** → **B**. Y las CDK: **"4/6, 2, 2, 1"** (CDK4/6 con D; CDK2 con E y A; CDK1 con A y B).

---

### 3.9 Los seis niveles de regulación de las CDK *(Diap. 27–34)*

#### 1–4. Ciclina y fosforilación *(Diap. 27–28, 30)*

| # | Mecanismo | Quién | Efecto |
|---|---|---|---|
| 1 | **Unión de la ciclina** | Ciclina | Desplaza el **asa T** del sitio activo → **actividad parcial** |
| 2 | **Fosforilación activadora** | **CAK** (CDK7–ciclina H) | Fosforila la **Thr160/161** del asa T → **actividad completa** |
| 3 | **Fosforilación inhibidora** | **Wee1** (y Myt1) | Fosforila **Thr14/Tyr15** cerca del sitio de unión del ATP → **apaga** el complejo |
| 4 | **Desfosforilación activadora** | **Cdc25** (fosfatasa) | Retira el fosfato inhibidor → activa **súbitamente** a ciclina B–CDK1 |

📌 **El interruptor de entrada a mitosis** *(Diap. 27)*:

```
Ciclina B–CDK1 inactiva (P-Tyr15) ──Cdc25──► Ciclina B–CDK1 ACTIVA
        ▲  Wee1 la mantiene inactiva                    │
        └── bucle positivo: CDK1 activa ACTIVA a Cdc25 e INHIBE a Wee1
```

Por ese **bucle de retroalimentación positiva**, la activación es **abrupta, "todo o nada"**: un poco de CDK1 activa genera más CDK1 activa.

🧠 **Wee1 = "wee" (pequeño en escocés)**: sin Wee1, las levaduras entran a mitosis antes de tiempo y quedan pequeñas. **Wee1 frena, Cdc25 acelera.**

#### 4 (bis). Proteínas inhibidoras de CDK (CKI) *(Diap. 29, 31)*

| | **Familia INK4** | **Familia CIP/KIP** |
|---|---|---|
| Miembros | **p16** (INK4a), **p15** (INK4b), **p18** (INK4c), **p19** (INK4d) | **p21** (CIP1), **p27** (KIP1), **p57** (KIP2) |
| Blanco | **Solo CDK4 y CDK6**: impiden su unión a la ciclina D | Complejos de **CDK2 y CDK1** (y regulan a CDK4/6) |
| Efecto | Rb no se fosforila y la célula se queda en **G1** | **p27** se acumula **sin mitógenos** o por **contacto célula–célula** y lleva a **G0** |

- La diapositiva 31 muestra cómo **p27 envuelve al complejo ciclina–CDK activo** y lo inactiva, aunque tenga su fosfato activador.

⚠️📌 **Precisión conceptual** *(Diap. 29)*: **p53 no es una CKI**. Es un **factor de transcripción** que, ante daño del ADN, **induce la expresión de p21**. La nomenclatura "p + número" indica **proteína y su peso aproximado en kDa**. Los genes de las CKI, de *TP53* y de *RB1* son **genes supresores de tumores** porque frenan la proliferación.

🧠 **INK4 = "INhibe CDK4"**: solo frena a CDK4/6. **CIP/KIP** frenan "a todos los demás" (CDK2, CDK1).

#### 5–6. Degradación en el proteasoma *(Diap. 32–34)*

📌 Dos **ubiquitina-ligasas E3** marcan proteínas con **cadenas de poliubiquitina** para que el **proteasoma 26S** las destruya. La degradación es **irreversible**: impide que el ciclo retroceda.

| | **SCF** | **APC/C** |
|---|---|---|
| Momento | **Transición G1/S** | **Metafase → anafase y G1** |
| Actividad | **Activa durante todo el ciclo**; reconoce sustratos **fosforilados** mediante proteínas **F-box** (p. ej., **Skp2**) | Activadores: **Cdc20** (en mitosis) y **Cdh1** (al final de M y en G1) |
| Degrada | **CKI (p27, p21) y ciclina E** | **Securina, ciclinas A y B, geminina** |
| Resultado | **Libera a CDK2** y permite entrar en S | Separación de cromátidas, **salida de mitosis** y **CDK baja en G1** (permite el licenciamiento) |

🧠 **SCF = "Sustrato Con Fosfato"**: necesita que su blanco esté fosforilado. **APC/C = "Anafase"**: es la ligasa que dispara la anafase.

---

### 3.10 El ciclo como sistema de osciladores *(Diap. 35)*

Los reguladores deben encenderse y apagarse **a tiempo y en el orden correcto**. Cada oscilador (complejo ciclina–CDK) tiene cinco componentes (Poon, 2016):

| | Componente | Ejemplo |
|---|---|---|
| a | **Activación**: señal que lo enciende | Mitógenos → ciclina D |
| b | **Autoamplificación**: bucle positivo que lo vuelve un interruptor rápido | CDK1 ⇄ Cdc25 |
| c | **Autoapagado**: mecanismo que lo desactiva | CDK1 activa al APC/C, que degrada la ciclina B |
| d | **Bloqueo de reactivación**: impide que se repita en el mismo ciclo; se elimina en el siguiente | Geminina impide re-licenciar hasta la siguiente G1 |
| e | **Relevo**: estimula al oscilador siguiente | E2F → ciclina E → ciclina A |

🧠 Un oscilador **se Enciende, se Amplifica, se Apaga, se Bloquea y Releva** ("**EAABR**").

#### Qué detiene el ciclo en cada fase *(Diap. 36)*

La diapositiva 36 resume los inductores de arresto: en **G1**, daño del ADN (p53, p21), falta de factores de crecimiento, telómeros cortos (senescencia) y estrés oxidativo (p38 MAPK); en **S**, daño del ADN durante la replicación (ATM, ATR, CHK1); en **mitosis**, los defectos del huso (MAD2, BUBR1).

✅ En la imagen de la diapositiva 36 (generada automáticamente) el defecto del huso aparece en **G2** y el "Punto R" en el límite G2/G1. Lo correcto: el **punto de control del huso actúa en M** (paso de metafase a anafase) y el **punto R está al final de G1**. La tabla de la diapositiva 42 (sección 3.12) es la versión correcta.

---

### 3.11 Mitógenos y punto de restricción *(Diap. 38–39)*

#### Los mitógenos encienden el ciclo desde la membrana *(Diap. 38)*

```
Factores de crecimiento (EGF · PDGF · FGF · IGF)
                 │
        Receptor tirosina cinasa
          ┌──────┴──────┐
 RAS → RAF → MEK → ERK   PI3K → AKT → mTOR
          └──────┬──────┘
   c-MYC · genes tempranos · ↑ ciclina D  →  ciclina D–CDK4/6
```

| Componente | Función clave |
|---|---|
| **Receptor tirosina cinasa** | Recibe la señal externa |
| **RAS–RAF–MEK–ERK (MAPK)** | Proliferación y activación de genes |
| **PI3K–AKT–mTOR** | Crecimiento, metabolismo, supervivencia; **↓ p21/p27** |
| **c-MYC** | **↑ ciclina D2 y CDK4, ↑ Cdc25A**; reprime p21 y p27 |
| **Ciclinas/CDK** | Regulación directa del ciclo |
| **Rb y E2F** | **Puerta de entrada** a la síntesis de ADN |

**Frenos externos**:
- **TGF-β** induce **p15 y p21**.
- El **contacto célula–célula** (vía **Hippo**, **p27**) detiene en G1 (inhibición por contacto).
- Muchas células necesitan **adhesión a la matriz** (integrinas–FAK) para dividirse (dependencia de anclaje).

🩺 ➕ Las células tumorales pierden la inhibición por contacto y la dependencia de anclaje; *RAS* y *MYC* son oncogenes frecuentes.

#### Punto de restricción: el interruptor Rb–E2F *(Diap. 39)*

| Estado | Qué pasa |
|---|---|
| **Sin mitógenos** | **Rb hipofosforilado secuestra a E2F** y recluta represores: los genes de fase S están **apagados** |
| **Fosforilación secuencial** | **Ciclina D–CDK4/6** y luego **ciclina E–CDK2**: Rb pasa de **mono- a hiperfosforilado** y **libera a E2F** |
| **E2F libre** | Transcribe **ciclina E y CDK2**, **ciclina A**, **enzimas de replicación** (ADN polimerasa, timidina cinasa, DHFR) y **más E2F** |

📌 **Bucle de retroalimentación positiva**: E2F induce ciclina E, que fosforila más Rb y libera más E2F. **Por eso el paso por R es irreversible**: la célula completa el ciclo aunque se retiren los mitógenos. **p16 (INK4) y p27** se acumulan cuando faltan señales e impiden cruzar R.

🧠 **"Rb es el portero que agarra a E2F"**: mientras Rb está "desnudo" (sin fosfatos), sujeta a E2F. Las CDK lo "visten" de fosfatos y lo obligan a soltarlo.

➕ El concepto de punto de restricción fue propuesto por Arthur Pardee en 1974.

---

### 3.12 Puntos de control *(Diap. 40–42)*

#### La lógica *(Diap. 40)*

📌 Los puntos de control **detienen temporalmente el ciclo** para que cada etapa **termine correctamente antes de iniciar la siguiente**.

| Componente | Función | Ejemplo |
|---|---|---|
| **Sensor** | Detecta el defecto | ADN roto, cinetocoro sin unir |
| **Transductor** | Transmite y amplifica la señal | Cinasas **ATM/ATR**, **CHK1/2** |
| **Efector** | Detiene el motor (inhibe CDK o APC/C) o activa la reparación | p21, Cdc25 inactiva, MCC |

| Punto de control | Pregunta |
|---|---|
| **G1/S (restricción)** | ¿Ambiente favorable? ¿ADN intacto? |
| **Intra-S** | ¿Horquillas sin errores? |
| **G2/M** | ¿ADN replicado y sin daño? |
| **Huso (SAC)** | ¿Todos los cinetocoros unidos al huso? |

#### p53 y Rb en el punto de control G1 *(Diap. 41)*

- **p53**: si el ADN está dañado, **detiene la progresión a S** inhibiendo el complejo CDK–ciclina de G1 (a través de p21). Da tiempo para reparar; si el daño es excesivo, inicia la **apoptosis**. Tiene un papel similar en el punto de control G2.
- **Rb**: evita que las células entren en S **en ausencia de señales de factores de crecimiento**. Cuando hay señales, las CDK–ciclinas fosforilan a Rb e inhiben su función.
- Los genes de p53 y Rb son **supresores tumorales**. Las mutaciones que los desactivan pueden conducir a cáncer y son **recesivas** a nivel celular (hay que perder los dos alelos).
  - ➕ Matiz: algunas mutaciones puntuales de *TP53* producen una proteína que bloquea a la normal (efecto dominante negativo).

#### ¿Qué detiene el ciclo y dónde? *(Diap. 42)*

| Factor inductor | Proteínas clave | Punto bloqueado |
|---|---|---|
| **Daño en el ADN** | ATM/ATR, CHK1/CHK2, p53, p21 | **G1/S, intra-S o G2/M** |
| **Telómeros cortos** | p53, p16INK4a | **G1 (senescencia)** |
| **Falta de factores de crecimiento** | Ausencia de ciclina D; ↑ p27 | **G1 (punto R)** |
| **Estrés oxidativo** | p53, p21, p38 MAPK | **G1 o G2** |
| **Defecto del huso mitótico** | MAD2, BUBR1, BUB1 | **Metafase → anafase** |
| **Contacto célula–célula** | p27, vía Hippo | **G1** |
| **Señal antiproliferativa (TGF-β)** | SMAD → p15, p21 | **G1** |

---

### 3.13 Respuesta al daño del ADN y p53 *(Diap. 43–45)*

#### Dos vías paralelas *(Diap. 43)*

| | **Vía ATM** | **Vía ATR** |
|---|---|---|
| Lesión que la activa | **Roturas de doble cadena** | **ADN monocatenario / horquillas detenidas** (estrés replicativo) |
| Cinasa efectora | **CHK2** | **CHK1** |
| Efectos | **↑ p53 → p21** (inhibe CDK2) y **degradación de Cdc25A** | **Inactiva Cdc25C** y **↑ Wee1** → ciclina B–CDK1 inactiva |
| Arresto | **G1/S** | **Intra-S y G2/M** |

🧠 **ATR = R de Replicación** (horquilla detenida, ADN monocatenario); **ATM** es la otra: roturas de doble cadena. Las parejas se cruzan: **ATM–CHK2** y **ATR–CHK1**.

📌 **Tres desenlaces**: **reparar** y reanudar el ciclo; **senescencia** (arresto permanente); **apoptosis** si el daño es irreparable (p53 → PUMA, BAX).

#### p53: el "guardián del genoma" *(Diap. 44)*

| Situación | Qué pasa con p53 |
|---|---|
| **Célula sin daño** | **MDM2 ubiquitina a p53** → proteasoma. Vida media de **minutos**, nivel **bajo** |
| **Célula con ADN dañado** | **ATM/CHK2 fosforilan a p53** → se **separa de MDM2**, se **estabiliza y acumula** y actúa como **factor de transcripción** |

**Genes que activa p53**:

| Gen | Efecto |
|---|---|
| **p21** | Inhibe ciclina–CDK → **arresto en G1/S y G2/M** |
| **GADD45, 14-3-3σ** | Retienen a CDK1 y Cdc25C → **arresto en G2** |
| **Genes de reparación** | Dan tiempo y herramientas para corregir el daño |
| **PUMA, BAX, NOXA** | Si el daño es excesivo → **apoptosis** |

📌 **Rb y p53 se inactivan por pérdida de función de ambos alelos** (hipótesis de los **"dos golpes" de Knudson**).

🩺 ➕ *TP53* es el gen más mutado en el cáncer humano. La mutación germinal de *TP53* causa el **síndrome de Li-Fraumeni** (sarcomas, cáncer de mama temprano, tumores cerebrales, carcinoma suprarrenal).

#### Daño en la replicación: ATM y BRCA1/2 *(Diap. 45)*

1. Rotura de doble cadena durante la copia.
2. **ATM** se activa y detiene el ciclo.
3. Recluta proteínas de reparación (**BRCA1, BRCA2, RAD51**): **recombinación homóloga** usando la **cromátida hermana**.
4. Si la reparación falla: **p53 → p21** (arresto) o **BAX** (apoptosis).

📌 **¿Por qué la hermana?** Después de la fase S hay una **copia idéntica** de cada cromosoma. La recombinación homóloga la usa como molde y **repara sin errores**; por eso ocurre en **S y G2**.

🩺 **Correlación clínica**:
- ***ATM***: su mutación causa **ataxia-telangiectasia** (neurodegeneración, inmunodeficiencia, radiosensibilidad).
- ***BRCA1/2***: su pérdida impide la reparación por recombinación homóloga (cáncer de mama y ovario hereditario).

Detalle completo en el [capítulo 5, reparación del ADN](#57-roturas-de-doble-cadena-nhej-y-hr).

---

### 3.14 Punto de control del huso (SAC) *(Diap. 46)*

| | **Cinetocoro sin unir → SAC encendido** | **Todos unidos → SAC apagado** |
|---|---|---|
| Señal | **MAD2 · BUBR1 · BUB3** forman el **complejo MCC** | El MCC deja de formarse |
| APC/C–Cdc20 | **Inhibido** | **Activo**: ubiquitina **securina** y **ciclina B** |
| Securina | **Estable** → **separasa inactiva** | Degradada → **separasa activa** |
| Cohesina | Mantiene unidas a las cromátidas: **no hay anafase** | La separasa **corta la cohesina (Scc1)** → **anafase** |
| Salida de mitosis | — | La **caída de ciclina B** permite salir de mitosis |

- 📌 **Basta un solo cinetocoro libre** para mantener la señal y frenar toda la célula.
- Otros componentes del SAC: **BUB1, MPS1** y la cinesina **CENP-E** (une cinetocoros a microtúbulos).
- 📌 Su falla produce células hijas con **número desigual de cromosomas (aneuploidía)**.

🧠 **"La securina asegura la cohesina"**: mientras exista securina, la separasa no puede separar.

🩺💊 ➕ Los **taxanos** (paclitaxel, estabilizan microtúbulos) y los **alcaloides de la vinca** (vincristina, impiden su polimerización) mantienen el SAC encendido: la célula tumoral queda detenida en mitosis y muere. ➕ Mutaciones bialélicas en *BUB1B* (BUBR1) causan la **aneuploidía en mosaico variegado**, con microcefalia y riesgo de cáncer infantil.

---

### 3.15 Tres frenos sobre el mismo motor *(Diap. 47)*

| Freno | Nivel | Mecanismo | Arresto |
|---|---|---|---|
| **Eliminación de Cdc25** | Activación de la CDK | **CHK1/2 fosforilan a Cdc25**; la proteína **14-3-3** la retiene en el citoplasma o se degrada. CDK1 y CDK2 **conservan su fosfato inhibidor** | **G1/S o G2/M** |
| **Inducción de p21** | Inhibición directa de la CDK | **p53 induce p21**, que se une a ciclina E–CDK2 (y otros complejos) y la inactiva | **Principalmente G1/S** |
| **Rb hipofosforilado** | Represión transcripcional | Sin actividad CDK, **Rb sigue unido a E2F**: no se transcriben ciclina E, ciclina A, CDC2 (CDK1) ni genes de fase S | **G1** |

---

### 3.16 microARN *(Diap. 48, 51)*

📌 Los **miARN** son ARN de **~22 nucleótidos** que **silencian ARNm específicos**. **Afinan la cantidad** de reguladores del ciclo y su expresión es **específica de tejido**.

| miARN | Blanco | Efecto sobre el ciclo |
|---|---|---|
| **miR-195** | WEE1, E2F | Modula G2/M y G1/S |
| **miR-17-92 · miR-106b-25** | p21, E2F | **Favorecen el paso G1/S** |
| **miR-302 · miR-372** | p21 | **Ciclo rápido de células madre embrionarias** |
| **let-7** | RAS | **Reduce la señal mitogénica** |
| **miR-322** | CDC25A (músculo) | **Frena la proliferación al diferenciarse** |

**Específicos de tejido**:
- Epidérmicos: **miR-205, miR-203** (p63).
- Neurales: **miR-9, miR-124, miR-137**.
- Musculares: **miR-1, miR-206, miR-133**.

🧠 Si el miARN silencia un **freno** (p21), **acelera** el ciclo (miR-17-92, miR-302). Si silencia un **acelerador** (RAS, CDC25A), lo **frena** (let-7, miR-322).

---

### 3.17 Quiescencia frente a senescencia *(Diap. 49)*

| | **Quiescencia (G0)** | **Senescencia** |
|---|---|---|
| **Reversibilidad** | **Reversible**: vuelve a G1 con el estímulo adecuado | **Irreversible** en condiciones fisiológicas |
| **Inductores** | Falta de mitógenos, contacto celular, diferenciación | **Acortamiento de telómeros**, daño persistente del ADN, estrés oxidativo, **oncogenes** |
| **Reguladores** | **p27 alto**; HES1; metabolismo reducido | **p16INK4a → Rb hipofosforilado**; **p14ARF → p53 → p21** |
| **Marcadores** | **Ausencia de Ki-67** | **β-galactosidasa asociada a senescencia**, focos de heterocromatina, **fenotipo secretor (SASP)** |
| **Respuesta** | **Responde a mitógenos** | Viable y metabólicamente activa; **resistente a mitógenos y a la apoptosis** |

- **Senescencia replicativa**: los fibroblastos humanos en cultivo se dividen un número limitado de veces antes de detenerse (**límite de Hayflick**). ✅ La diapositiva da ≈ 25–50 divisiones; el dato clásico de Hayflick es **~40–60 duplicaciones** en fibroblastos fetales, y menos en células de donantes adultos.
- ➕ **p14ARF** inhibe a MDM2, de modo que p53 se acumula. **p16INK4a y p14ARF** salen del mismo locus (*CDKN2A*, 9p21) con marcos de lectura distintos; su deleción, frecuente en tumores, apaga a la vez las vías de Rb y de p53.
- ➕ El **SASP** (citocinas inflamatorias, proteasas) explica por qué acumular células senescentes contribuye al envejecimiento y a enfermedades crónicas.

🧠 **Quiescente = "quieto pero despierto"** (puede volver). **Senescente = "jubilado"** (no vuelve, pero sigue activo y opina: SASP).

---

### 3.18 Mapa integrador e ideas clave *(Diap. 50–52)*

#### Quién actúa en cada transición *(Diap. 50)*

| | **G1 → S** | **S** | **G2 → M** | **Metafase → anafase** |
|---|---|---|---|---|
| **Motor** | Ciclina D–CDK4/6; ciclina E–CDK2 | Ciclina A–CDK2 | Ciclina A/B–CDK1 | APC/C–Cdc20 |
| **Diana principal** | Rb → E2F | ORC, Cdc6, MCM | Láminas, condensinas | Securina, ciclina B |
| **Freno (CKI o vía)** | INK4, p21, p27; ATM–CHK2–p53 | ATR–CHK1 | Wee1; CHK1 → Cdc25C ✕ | SAC: MAD2, BUBR1 |
| **Pregunta** | ¿Señal y ADN íntegro? | ¿Copia sin errores, una sola vez? | ¿ADN completo y sin daño? | ¿Todos los cinetocoros unidos? |

#### Ideas clave *(Diap. 52)*

1. **El ciclo es unidireccional**: ondas de ciclinas y su degradación irreversible impiden retroceder.
2. **La replicación ocurre una sola vez**: licenciamiento con CDK baja en G1; disparo con CDK alta en S.
3. **Las CDK integran todo**: ciclinas, CAK, Wee1/Cdc25, CKI y proteólisis ajustan su actividad.
4. **El punto R conecta ambiente y núcleo**: mitógenos → ciclina D → Rb-P → E2F: compromiso irreversible.
5. **Los puntos de control protegen el genoma**: ATM/ATR–p53–p21 y el SAC detienen el ciclo ante errores.
6. **Salir del ciclo también se regula**: G0 es reversible; la senescencia, no.

---

### 3.19 ➕ Del ciclo celular a la clínica

No está en las diapositivas, pero conecta la clase con lo que verás en patología y farmacología.

| Tema | Relación con el ciclo |
|---|---|
| **Retinoblastoma** | Pérdida de los dos alelos de ***RB1*** (13q14). Forma hereditaria: primer golpe germinal, tumores bilaterales y tempranos (Knudson, 1971) |
| **Virus del papiloma humano (VPH)** | La oncoproteína **E6** degrada a **p53**; **E7** se une a **Rb** y libera E2F. 🩺 Por eso la sobreexpresión de **p16** se usa como marcador de lesiones por VPH |
| **Inhibidores de CDK4/6** 💊 | **Palbociclib, ribociclib, abemaciclib**: bloquean la fosforilación de Rb; se usan en cáncer de mama con receptores hormonales positivos y HER2 negativo. Requieren un Rb funcional |
| **Ki-67** | Proteína presente en G1, S, G2 y M, ausente en G0: el porcentaje de células Ki-67+ mide la proliferación de un tumor |
| **Quimioterapia específica de fase** 💊 | Fase S: antimetabolitos (metotrexato, 5-fluorouracilo, citarabina, hidroxiurea). G2: bleomicina, etopósido. M: taxanos y alcaloides de la vinca |
| **Li-Fraumeni** | *TP53* germinal (ver 3.13) |
| **Ataxia-telangiectasia** | *ATM* (ver 3.13 y la guía de reparación del ADN) |

---

### ✅ Verificación de datos de la clase (capítulo 3)

| Diapositiva | Dice | Verificación |
|---|---|---|
| 12 | "EPFF Efecsa gene de S" | Texto ilegible de una imagen generada automáticamente: debe leerse "E2F activa genes de fase S" |
| 18 | "En metafase actúa el punto de control del huso" | Correcto como simplificación. ➕ El SAC está activo desde la prometafase y controla el paso de metafase a anafase |
| 19 | Esquema con "CC" y flechas confusas | Imagen generada automáticamente; usar la diapositiva 16 |
| 29 | "p15, p16, p18, p19 (INK4a–d)" | Correspondencia exacta: **p16 = INK4a, p15 = INK4b**, p18 = INK4c, p19 = INK4d |
| 36 | Defecto del huso en G2; "Punto R" entre G2 y G1 | El SAC actúa en **M**; el punto R está al **final de G1** |
| 49 | Límite de Hayflick ≈ 25–50 divisiones | Dato clásico: ~40–60 duplicaciones en fibroblastos fetales; menos en adultos |
| 5 | 37,2 billones de células; 330.000 millones/día; 86 % sanguíneas | Correcto (Bianconi 2013; Sender y Milo 2021) |
| 8 | Duraciones (rana 30 min… hepatocito 1 año) | Correcto (Alberts, tabla de duraciones del ciclo) |

---

### Autoevaluación (capítulo 3)

<details><summary>1. ¿Qué fase explica casi todas las diferencias de duración del ciclo entre tipos celulares?</summary>

G1.
</details>

<details><summary>2. Tras la fase S, ¿cuántos cromosomas y cuántas cromátidas tiene una célula humana?</summary>

46 cromosomas, cada uno con 2 cromátidas hermanas (92 cromátidas); contenido de ADN 4C.
</details>

<details><summary>3. ¿Por qué un origen de replicación no puede disparar dos veces en el mismo ciclo?</summary>

Porque el licenciamiento (carga de MCM por ORC, Cdc6 y Cdt1) solo ocurre con CDK baja (G1). Desde S hasta M la CDK alta fosforila Cdc6 y ORC y la geminina secuestra a Cdt1; solo al final de la mitosis el APC/C baja la CDK y degrada la geminina.
</details>

<details><summary>4. En la fusión de una célula en S con una en M, ¿qué se observa y por qué?</summary>

Cromatina "pulverizada": el MPF fuerza la condensación de un ADN que está a medio replicar.
</details>

<details><summary>5. ¿Qué hace Wee1 y qué hace Cdc25 sobre CDK1?</summary>

Wee1 fosforila Thr14/Tyr15 e inhibe a CDK1. Cdc25 retira ese fosfato y la activa.
</details>

<details><summary>6. ¿Por qué la entrada en mitosis es "todo o nada"?</summary>

Por un bucle de retroalimentación positiva: CDK1 activa activa a Cdc25 e inhibe a Wee1, de modo que un poco de CDK1 activa genera rápidamente mucha más.
</details>

<details><summary>7. ¿Qué diferencia hay entre INK4 y CIP/KIP?</summary>

INK4 (p16, p15, p18, p19) inhibe solo a CDK4/6 impidiendo su unión a la ciclina D. CIP/KIP (p21, p27, p57) inhibe complejos de CDK2 y CDK1.
</details>

<details><summary>8. ¿p53 es una CKI? Explica.</summary>

No. Es un factor de transcripción que, ante daño del ADN, induce la expresión de la CKI p21.
</details>

<details><summary>9. ¿Por qué el punto R es irreversible?</summary>

Porque E2F libre induce ciclina E, que fosforila más Rb y libera más E2F (retroalimentación positiva). La célula deja de depender de los mitógenos.
</details>

<details><summary>10. Una célula tiene un cromosoma con un cinetocoro sin unir. ¿Qué proteína está inhibida y cuál queda estable?</summary>

APC/C–Cdc20 está inhibido por el MCC (MAD2, BUBR1, BUB3); la securina queda estable y la separasa inactiva, así que no hay anafase.
</details>

<details><summary>11. Diferencia una rotura de doble cadena de una horquilla detenida en cuanto a la vía que activan.</summary>

Rotura de doble cadena → ATM → CHK2 → p53/p21 (arresto G1/S). Horquilla detenida o ADN monocatenario → ATR → CHK1 → Cdc25 inactiva (arresto intra-S y G2/M).
</details>

<details><summary>12. Un hepatocito y una neurona dejan de dividirse. ¿En qué se diferencian?</summary>

El hepatocito es estable (quiescente): puede volver a G1 tras una lesión o hepatectomía. La neurona es permanente: salió del ciclo de forma definitiva.
</details>

<details><summary>13. Una célula senescente, ¿es Ki-67 positiva? ¿responde a mitógenos?</summary>

No y no. Es viable y metabólicamente activa, expresa β-galactosidasa asociada a senescencia y secreta el SASP, pero no vuelve a dividirse.
</details>

---

### Glosario (capítulo 3)

| Término | Definición |
|---|---|
| **APC/C** | Ubiquitina-ligasa E3 que dispara la anafase y la salida de mitosis (con Cdc20 o Cdh1) |
| **CAK** | Cinasa activadora de CDK: CDK7–ciclina H |
| **CDK** | Cinasa dependiente de ciclina |
| **CKI** | Proteína inhibidora de CDK (familias INK4 y CIP/KIP) |
| **Cohesina** | Complejo que une a las cromátidas hermanas hasta la anafase |
| **E2F** | Factor de transcripción de los genes de fase S, secuestrado por Rb |
| **G0** | Estado de quiescencia fuera del ciclo, reversible |
| **Geminina** | Proteína que secuestra a Cdt1 e impide re-licenciar orígenes |
| **Licenciamiento** | Carga de MCM2-7 en los orígenes durante G1 |
| **MPF** | Factor promotor de la mitosis: ciclina B–CDK1 |
| **Punto R** | Punto de restricción de G1 tras el cual la célula ya no depende de mitógenos |
| **SAC** | Punto de control del ensamblaje del huso |
| **SASP** | Fenotipo secretor asociado a senescencia |
| **SCF** | Ubiquitina-ligasa E3 que degrada sustratos fosforilados (p27, ciclina E) |
| **Securina** | Inhibidor de la separasa; su degradación permite la anafase |
| **Separasa** | Proteasa que corta la cohesina |

---

### Referencias (capítulo 3)

De la clase:

- Alberts B, et al. *Molecular Biology of the Cell.* 7.ª ed. W.W. Norton; 2022, cap. 17.
- Morgan DO. *The Cell Cycle: Principles of Control.* New Science Press; 2007.
- Song G, et al. Cell cycle checkpoint revolution. *Front Pharmacol.* 2024;15:1459057.
- Poon RYC. Cell cycle control: a system of interlinking oscillators. *Methods Mol Biol.* 2016;1342:3-19.
- Rao PN, Johnson RT. *Nature.* 1970;225:159-164.
- Hume S, Dianov GL, Ramadan K. A unified model for the G1/S transition. *Nucleic Acids Res.* 2020;48:12483-12501.
- Limas JC, Cook JG. Preparation for DNA replication. *FEBS Lett.* 2019;593:2853-2867.
- Musacchio A. Spindle assembly checkpoint signaling. *Curr Biol.* 2015;25:R1002-R1018.
- Bianconi E, et al. *Ann Hum Biol.* 2013;40:463-471; Sender R, Milo R. *Nat Med.* 2021;27:45-48.
- Smith HL, et al. DNA damage checkpoint kinases in cancer. *Expert Rev Mol Med.* 2020;22:e2.
- Escalona Mugica JR. *Ciclo celular.* Depto. de Embriología y Genética, Facultad de Medicina, UNAM.

Usadas en las ampliaciones:

- Hayflick L, Moorhead PS. The serial cultivation of human diploid cell strains. *Exp Cell Res.* 1961;25:585-621.
- Knudson AG. Mutation and cancer: statistical study of retinoblastoma. *PNAS.* 1971;68:820-823.
- Nobel de Fisiología o Medicina 2001: <https://www.nobelprize.org/prizes/medicine/2001/summary/>

[↑ Volver al índice general](#índice-general)

---

## 4. Errores innatos del metabolismo (EIM)

> Clase de la Prof. **Sandra Yaneth Ospina Lagos**, médica genetista, docente de la Universidad Nacional de Colombia (Asociación Colombiana de Genética Humana, ACGH).
> Las diapositivas no traen número impreso: *(Diap. N)* corresponde a la **página del PDF** (la portada es la página 2). Los símbolos 📌 ➕ ⚠️ ✅ 🩺 💊 🧠 se explican al [inicio de la guía](#cómo-usar-esta-guía).

---

### Índice (capítulo 4)

- [Lo esencial en un minuto](#lo-esencial-en-un-minuto-capítulo-4)
- [4.1 Historia](#41-historia-diap-4)
- [4.2 Definiciones y generalidades](#42-definiciones-y-generalidades-diap-57)
- [4.3 Epidemiología y tamizaje neonatal en Colombia](#43-epidemiología-y-tamizaje-neonatal-en-colombia-diap-89)
- [4.4 Principios para el diagnóstico clínico](#44-principios-para-el-diagnóstico-clínico-diap-10)
- [4.5 Clasificación](#45-clasificación-diap-1114)
- [4.6 Grupo 1: metabolismo intermediario (tipo intoxicación)](#46-grupo-1-metabolismo-intermediario-tipo-intoxicación-diap-1518)
- [4.7 Fenilcetonuria (PKU)](#47-fenilcetonuria-pku-diap-1926)
- [4.8 Caso clínico 1: acidemia propiónica](#48-caso-clínico-1-acidemia-propiónica-diap-2728)
- [4.9 Grupo 2: metabolismo energético](#49-grupo-2-metabolismo-energético-diap-2930)
- [4.10 Caso clínico 2: glucogenosis tipo VI](#410-caso-clínico-2-glucogenosis-tipo-vi-diap-3133)
- [4.11 Grupo 3: moléculas complejas](#411-grupo-3-moléculas-complejas-diap-3436)
- [4.12 Caso clínico 3 y mucopolisacaridosis](#412-caso-clínico-3-y-mucopolisacaridosis-diap-3762)
- [4.13 Reflexiones y conclusiones](#413-reflexiones-y-conclusiones-diap-6370)
- [4.14 ➕ Pistas de laboratorio para orientar un EIM](#414--pistas-de-laboratorio-para-orientar-un-eim)
- [✅ Verificación de datos de la clase](#-verificación-de-datos-de-la-clase-capítulo-4)
- [Autoevaluación](#autoevaluación-capítulo-4)
- [Glosario](#glosario-capítulo-4)
- [Referencias](#referencias-capítulo-4)

---

### Lo esencial en un minuto (capítulo 4)

1. Los **EIM** son enfermedades genéticas **raras individualmente** pero **frecuentes en conjunto** (incidencia acumulada **> 1 por 1.000** nacimientos), causadas por defectos de enzimas (o transportadores, cofactores) de una vía metabólica. Hay **acumulación** de sustrato o **deficiencia** de producto.
2. **Archibald Garrod (1908)**, con la **alcaptonuria**, propuso que son "fallas enzimáticas" heredadas.
3. La mayoría es **autosómica recesiva**: por eso los casos parecen **esporádicos**.
4. Pueden aparecer **a cualquier edad**. Hay que **pensar en ellos en paralelo** con las causas comunes y **buscar primero los tratables**.
5. Clasificación fisiopatológica en **tres grupos**: (1) **metabolismo intermediario de moléculas pequeñas** (tipo **intoxicación**), (2) **metabolismo energético**, (3) **moléculas complejas** (depósito, síntesis y tráfico).
6. **Tipo intoxicación**: no altera el desarrollo fetal, hay un **intervalo libre de síntomas**, las crisis se desencadenan por **ayuno, estrés catabólico o ingesta** y son **tratables** (retirar el tóxico).
7. **PKU**: déficit de **fenilalanina hidroxilasa** (*PAH*, cromosoma 12), cofactor **BH4**; ↑ Phe, ↓ Tyr; **olor a ratón**, eccema, hipopigmentación, convulsiones y **discapacidad intelectual** si no se trata. Se detecta con la **prueba del talón** y se trata con **dieta baja en Phe** y fórmula especial.
8. **Energéticos**: hipoglicemia, hiperlactatemia, acidosis, alteración de cetonas; afectan **hígado, músculo, corazón y cerebro**; pocos son tratables.
9. **Moléculas complejas**: síntomas **progresivos**, **sin crisis agudas**, gran morbimortalidad. Ejemplo: **mucopolisacaridosis (MPS)**, 7 tipos por 11 deficiencias enzimáticas.
10. En **Colombia** la **Ley 1980 de 2019** creó el programa de tamizaje neonatal; la **Resolución 117 de 2026** hizo obligatorias siete pruebas metabólicas (antes solo hipotiroidismo).
11. **Si sospechas un EIM, toma y congela muestras durante la crisis**; el diagnóstico puede depender de ellas.

---

### 4.1 Historia *(Diap. 4)*

| Época | Hito |
|---|---|
| **1908 – Archibald Garrod** | Estudia la **alcaptonuria** e introduce el concepto de **"errores innatos del metabolismo"**: propone que ciertas enfermedades metabólicas se deben a **fallas enzimáticas** |
| **1950–1980 – Avances en bioquímica** | Se identifican los **defectos enzimáticos** específicos de la **fenilcetonuria** y la **galactosemia** y se desarrollan **pruebas bioquímicas** para detectar metabolitos anómalos |
| **1960** | Stanbury y colaboradores publican *The Metabolic Basis of Inherited Disease* |
| **1990 – actualidad** | **Tamizaje neonatal con espectrometría de masas en tándem**, diagnóstico temprano, **terapias génicas** y tratamientos personalizados |
| **2001** | 8.ª edición del texto (Scriver): ~1.000 enfermedades metabólicas, la mayoría con compromiso neurológico, aunque casi no se enseñan en las facultades de medicina |
| **Impacto en salud pública** | Programas de **tamizaje neonatal**; mayor esperanza y calidad de vida por detección y tratamiento precoz |

➕ **Alcaptonuria**: déficit de homogentisato 1,2-dioxigenasa (vía de degradación de la tirosina). El ácido homogentísico se acumula y la **orina se oscurece al dejarla en reposo**; en adultos causa **ocronosis** (pigmentación del cartílago) y artritis. Garrod notó que era más frecuente entre hijos de primos (consanguinidad), lo que encajó con la herencia **recesiva** de Mendel.

✅ La diapositiva ubica el "descubrimiento" de la PKU y la galactosemia entre 1950 y 1980. La **PKU** la describió **Asbjørn Følling en 1934**, y la galactosemia se describió clínicamente a comienzos del siglo XX. En los años 50 se demostraron sus **defectos enzimáticos** y se inició la **dieta** para la PKU (Bickel, 1953); en **1963** Robert **Guthrie** creó la prueba en gota de sangre seca que dio origen al tamizaje neonatal.

---

### 4.2 Definiciones y generalidades *(Diap. 5–7)*

#### Definiciones *(Diap. 5)*

📌 **Errores innatos del metabolismo (EIM)**: grupo de **enfermedades genéticas raras** causadas por **defectos enzimáticos** que afectan **rutas metabólicas específicas**. Se caracterizan por la **acumulación o deficiencia de metabolitos esenciales**, lo que provoca alteraciones fisiológicas graves.

Segunda definición de la clase: trastornos hereditarios poco comunes en los que el cuerpo **no puede convertir los alimentos en energía** de manera apropiada, generalmente por defectos en **proteínas específicas (enzimas)** que descomponen partes del alimento.

- La figura de la diapositiva 5 resume el metabolismo: los **nutrientes** (glucosa, aminoácidos, ácidos grasos) se degradan (**catabolismo**) para dar **energía** y desechos (especies reactivas de oxígeno, CO₂, **amonio**), o se usan para construir **macromoléculas** (**anabolismo**): glucógeno, lípidos y proteínas de reserva; lípidos, proteínas y ácidos nucleicos para el crecimiento.
- La diapositiva 6 (mapas metabólicos de KEGG y de la IUBMB) muestra por qué hay tantos EIM: cada enzima de esa red puede fallar.

➕ La definición actual es más amplia: la **Clasificación Internacional de Trastornos Metabólicos Hereditarios (ICIMD, 2021)** los define como alteraciones primarias de una vía bioquímica con causa genética conocida o supuesta. Incluye defectos de **enzimas, transportadores, receptores y cofactores**, y suma **1.450 trastornos**.

#### Generalidades *(Diap. 7)*

1. Se han descrito **más de 1.015** EIM (✅ dato de 2018; la ICIMD de 2021 lista 1.450).
2. **Muchos se presentan de forma aguda** y pueden diagnosticarse con **pruebas metabólicas en plasma y orina** en laboratorios especializados de bioquímica genética.
3. **Algunos son tratables** y requieren **intervención temprana y urgente** para prevenir secuelas permanentes.
4. **La mayoría de los EIM tratables pueden identificarse con el tamizaje neonatal.**

---

### 4.3 Epidemiología y tamizaje neonatal en Colombia *(Diap. 8–9)*

#### Epidemiología *(Diap. 8)*

📌 Aunque cada EIM es raro, la **incidencia acumulada es superior a 1 por 1.000**.

| Lugar | Prevalencia | Referencia |
|---|---|---|
| Reino Unido (West Midlands) | **1/784** | Sanderson et al., 2006 |
| Columbia Británica, Canadá | 1/2.500 | Applegarth et al., 2000 |
| Italia | 1/2.555 | Dionisi-Vici et al., 2002 |

Los EIM están presentes **en todos los grupos étnicos y en todas las edades**.

➕ La cifra más alta del Reino Unido se explica en parte por la consanguinidad en algunas comunidades de esa región, que aumenta los trastornos recesivos.

#### Enfermedades del tamizaje básico en Colombia *(Diap. 9)*

📌 La **Ley 1980 de 2019** creó el **Programa de Tamizaje Neonatal**. Su **tamizaje básico** incluye siete condiciones:

| Condición | Frecuencia (según la clase) | Fuente |
|---|---|---|
| **Fenilcetonuria (PKU)** | 1:23.930 nacidos vivos en el mundo (de 1:4.500 en Italia a 1:125.000 en Japón) | Hillert et al., *Am J Hum Genet* 2020 |
| **Galactosemia** | Incidencia anual 1/40.000–1/60.000 | Orphanet |
| **Fibrosis quística** | Europa ~1/3.000; Irlanda 1/1.400; Finlandia 1/25.000 | Orphanet |
| **Déficit de biotinidasa** | 1/61.000 | Orphanet |
| **Hiperplasia suprarrenal congénita** | Prevalencia ~1/10.000; incidencia anual 1/5.000–1/15.000 | Orphanet |
| **Hemoglobinopatías** (defectos de la hemoglobina) | — | — |
| **Hipotiroidismo congénito** | ✅ 1:2.500–1:3.500 (la diapositiva dice "1:2500-3:500") | INS (Sivigila) |

- ⚠️ No todas son EIM en sentido estricto: el **hipotiroidismo congénito** es endocrino (casi siempre por disgenesia tiroidea), la **fibrosis quística** es un defecto de un canal de cloro (CFTR) y las **hemoglobinopatías** son defectos de la globina. Se tamizan porque son frecuentes o graves, tienen una fase sin síntomas, una prueba confiable y un tratamiento que cambia el pronóstico (➕ criterios de Wilson y Jungner).
- ✅ **Actualización 2026**: la **Resolución 117 de 2026** del Ministerio de Salud (30 de enero de 2026) hizo **obligatorias** las seis pruebas que se suman al hipotiroidismo congénito. El país pasa de **una a siete pruebas metabólicas**, con muestra del **talón entre las 48 y 72 horas** de vida y cuatro componentes de tamizaje (visual, auditivo, cardiopatías congénitas complejas y endocrino-metabólico). La implementación es progresiva: al terminar 2026, al menos el 79 % de los recién nacidos debe tener las seis nuevas pruebas ([MinSalud, 2026](https://www.minsalud.gov.co/Comunicaciones/noticias/2026/Paginas/minsalud-amplia-tamizaje-neonatal.aspx)). Antes, la Resolución 207 de 2024 había adoptado los lineamientos técnicos del programa.

🧠 **Las 7 del talón**: **"Tiroides, Fenil, Galacto, Fibro, Supra, Bio, Hemo"**.

---

### 4.4 Principios para el diagnóstico clínico *(Diap. 10)*

📌 Siete principios para **no pasar por alto un trastorno tratable** (en la tabla, "ECM" = enfermedad congénita del metabolismo, sinónimo de EIM):

1. En el contexto clínico apropiado, **considere un EIM en paralelo con las condiciones comunes** (no al final, cuando ya se descartó todo).
2. Si los **síntomas persisten y siguen inexplicados a pesar del tratamiento inicial** y de descartar lo común, considere un EIM.
3. **No confunda un síntoma o un síndrome con la etiología**: detrás de una "sepsis", una "encefalopatía" o un "reflujo" puede haber un EIM por establecer.
4. Un EIM **se puede presentar a cualquier edad**.
5. Por la **herencia autosómica recesiva**, la mayoría de los casos **parecen esporádicos** (padres sanos, sin antecedentes).
6. **Considere e intente diagnosticar primero los EIM susceptibles de tratamiento.**
7. En situaciones de emergencia, **se maneja primero al paciente** y luego a la familia (estudio y asesoría genética).

---

### 4.5 Clasificación *(Diap. 11–14)*

#### Clasificación simplificada de Saudubray (2019) *(Diap. 11–13)*

Saudubray, Mochel, Lamari y García-Cazorla propusieron una clasificación práctica basada en la fisiopatología, en **tres grandes categorías**:

| Categoría | Subtipos | Ejemplos | Tratabilidad |
|---|---|---|---|
| **Moléculas pequeñas** | **Acumulación** (intoxicación) | Catabolismo de aminoácidos, defectos del ciclo de la urea, acidurias orgánicas, galactosemia, metales | **Los más tratables** |
| | **Deficiencia** (síntesis y transporte defectuosos) | Defectos de síntesis de aminoácidos esenciales y no esenciales, de síntesis y elongación de ácidos grasos, deficiencias de metales | Pocos tratables |
| **Moléculas complejas** (glucógeno, esfingolípidos, fosfolípidos, colesterol, ácidos biliares, glucosaminoglucanos, oligosacáridos, glucoproteínas, ácidos nucleicos) | **Acumulación** (depósito) | Glucogenosis, esfingolipidosis, **mucopolisacaridosis**, glucoproteinosis | Terapias emergentes |
| | **Deficiencia** | Defectos peroxisomales, de colesterol y ácidos biliares, de síntesis de glucosaminoglucanos | En general no tratables |
| | **Procesamiento y tráfico celular** | Trastornos congénitos de la glicosilación (CDG), autofagia, ciclo de vesículas sinápticas | En general no tratables |
| **Defectos energéticos** | **Transportadores de membrana** | GLUT1, transportadores de monocarboxilatos | Tratables o parcialmente tratables |
| | **Citoplasmáticos** | Glucólisis, metabolismo del glucógeno, gluconeogénesis, hiperinsulinismo, creatina, vía de las pentosas | Tratables o parcialmente tratables |
| | **Mitocondriales** | Piruvato carboxilasa y deshidrogenasa, ciclo de Krebs, cadena respiratoria, oxidación de ácidos grasos, cuerpos cetónicos | Algunos tratables |

La diapositiva 13 conecta esta clasificación con la nosología completa: **9 grupos (A–I), 130 categorías y más de 1.200 trastornos**: (A) compuestos nitrogenados, (B) vitaminas, cofactores, metales y minerales, (C) carbohidratos, (D) mitocondriales, (E) lípidos, (F) tetrapirroles, (G) depósito, (H) peroxisoma y oxalato, (I) CDG.

#### Clasificación fisiopatológica (Saudubray y García-Cazorla, 2018) *(Diap. 14)*

| Tipo | Características | Ejemplo |
|---|---|---|
| Trastornos que afectan **un solo sistema funcional, órgano o sistema anatómico** | **Síntomas uniformes y consistentes** | ➕ La imagen (glóbulos rojos, habas, fármacos) alude al **déficit de G6PD**: anemia hemolítica al comer habas o tomar ciertos fármacos |
| Trastornos con compromiso bioquímico de una **vía común** a muchas células y órganos | **Síntomas diversos** | Tres grupos: **(1) metabolismo intermediario de moléculas pequeñas, (2) metabolismo energético, (3) moléculas complejas** |

🧠 **"Tóxico, Tanque vacío, Trastero lleno"**: (1) intoxicación por moléculas pequeñas; (2) falta energía; (3) se acumulan moléculas grandes que no se pueden desarmar.

---

### 4.6 Grupo 1: metabolismo intermediario (tipo intoxicación) *(Diap. 15–18)*

#### Qué incluye *(Diap. 15)*

1. **Aminoacidopatías** (por ejemplo, PKU, enfermedad de orina con olor a jarabe de arce).
2. **Acidemias orgánicas** (propiónica, metilmalónica, isovalérica).
3. **Defectos del ciclo de la urea**.

También: trastornos de **monosacáridos** (galactosemia), **porfirias**, trastornos de los **metales** (Wilson), de **neurotransmisores** y de **aminoácidos cerebrales**. Afectan el **anabolismo, el catabolismo o el reciclaje** de moléculas pequeñas. Mecanismo dominante: **intoxicación**.

#### Puntos en común de los EIM tipo intoxicación *(Diap. 16)*

📌 Seis rasgos (pregunta de examen casi segura):

1. **No alteran el desarrollo del embrión o del feto** (➕ la placenta "dializa" el tóxico durante el embarazo).
2. Hay un **intervalo libre de síntomas** (el recién nacido nace bien y se enferma días después, cuando empieza a alimentarse).
3. Los signos de intoxicación pueden ser:
   - **Agudos**: vómito, coma, insuficiencia hepática, trombosis.
   - **Crónicos**: retraso del desarrollo, ataxia, ectopia del cristalino (➕ homocistinuria), cirrosis, cardiomiopatía.
   - **Progresivos**: neurodegeneración.
4. Se presentan de forma **aguda por ayuno, estrés metabólico** (infección, fiebre, cirugía) **o aumento en la ingesta** de alimentos (proteínas).
5. **Diagnóstico disponible** con laboratorios convencionales; se confirma con **aminoácidos, ácidos orgánicos y perfil de acilcarnitinas**.
6. **Son tratables**: **remoción urgente de la toxina**, quelantes, vitaminas, fórmulas especiales.

➕ **Cómo se "retira la toxina"**: suspender temporalmente la fuente (proteínas o galactosa), aportar glucosa intravenosa para frenar el catabolismo, usar captadores de amonio (benzoato o fenilbutirato de sodio), hemodiálisis en casos graves, cofactores (biotina, vitamina B12, B6) y quelantes para los metales (Wilson).

#### Fisiopatología general *(Diap. 17–18)*

📌 Una mutación puede alterar la vía en cuatro puntos *(Diap. 17)*:

```
                       (2) gen de la ENZIMA mutado
                       (3) defecto del COFACTOR
                                 │
Sustrato ──(1) TRANSPORTADOR──► Sustrato ──── enzima + cofactor ────► Producto
             o receptor mutado      │
                                    └──(4)──► otra vía bioquímica
```

📌 Y las consecuencias son cuatro *(Diap. 18; Lanpher, Brunetti-Pierri y Lee, 2006)*:

| | Consecuencia | Ejemplo en la PKU |
|---|---|---|
| a | **Acumulación del sustrato** | ↑ Fenilalanina |
| b | **Deficiencia del producto** | ↓ Tirosina (y de sus derivados: melanina, catecolaminas) |
| c | **Activación de otras vías** | — |
| d | **Desviación hacia vías secundarias** (metabolitos tóxicos) | Ácido fenilpirúvico y fenilacetato |

---

### 4.7 Fenilcetonuria (PKU) *(Diap. 19–26)*

#### Vía y fisiopatología *(Diap. 19, 23)*

```
                 Tetrahidrobiopterina (BH4, cofactor)
                              │
Fenilalanina ───── fenilalanina hidroxilasa (PAH) ──✕──► Tirosina ──► melanina
      ↑↑↑                                                    ↓        ──► epinefrina (catecolaminas, dopamina)
      │                                                               ──► tiroxina
      └──► ácido fenilpirúvico (vía secundaria) ──► olor, eccema
```

| Mecanismo | Manifestación (frecuencia en la serie citada por la clase) |
|---|---|
| ↑ Phe → **ácido fenilpirúvico** y derivados | **Olor** característico (86 %), **eccema** (34 %) |
| ↓ Tirosina → ↓ **melanina** | **Pelo y ojos claros, piel blanca** |
| ↑ Phe en el cerebro, ↓ dopamina | **Convulsiones** (30 %), **problemas de conducta** (68 %), **discapacidad intelectual** |

- ➕ El **olor a ratón o a moho** se debe sobre todo al **fenilacetato**.
- ➕ **Por qué daña el cerebro** *(Diap. 23)*: la Phe elevada compite con otros aminoácidos neutros grandes (tirosina, triptófano) por el transportador de la barrera hematoencefálica. Baja la síntesis de **dopamina y serotonina** (alteraciones emocionales y del control motor) y se altera la **mielina** (cambios de sustancia blanca, procesamiento lento).
- 🧠 **Fenil-ceton-uria**: la fenilcetona (fenilpiruvato) **sale en la orina**.

#### Definición, causa y genética *(Diap. 21–22)*

- 📌 **Definición**: trastorno metabólico hereditario en el que el cuerpo **no puede metabolizar la fenilalanina** por **deficiencia de la fenilalanina hidroxilasa (PAH)**, que la convierte en tirosina.
- **Incidencia**: aproximadamente **1 por 10.000–15.000** nacimientos (en poblaciones europeas y norteamericanas; la cifra mundial es 1:23.930).
- **Causa**: mutaciones en el gen ***PAH***, **cromosoma 12** (➕ 12q23.2).
- **Herencia**: **autosómica recesiva**. Dos padres portadores: **25 %** de riesgo de hijo afectado, 50 % portador y 25 % sano no portador en cada embarazo.
- **Mutaciones**: la clase dice "más de 600" en *PAH*. ✅ Hoy se conocen **más de 950** (2016), y la base PAHvdb registra más de 3.000 variantes (2026).
- **Heterogeneidad genética**: no toda hiperfenilalaninemia se debe a *PAH*. Los **defectos del cofactor BH4** (por ejemplo, la **deficiencia de dihidropteridina reductasa**) también elevan la Phe y, además, bajan los neurotransmisores. 🩺 Por eso hay que **descartarlos siempre**: no responden solo a la dieta.
- Es posible la **detección de portadores** (estudio molecular).

#### Clasificación por niveles de fenilalanina *(Diap. 23)*

| Clasificación | Nivel de Phe en sangre |
|---|---|
| Individuo no afectado | ~1 mg/dL (60 µmol/L) |
| **Hiperfenilalaninemia** (HPA) | < 6 mg/dL (< 360 µmol/L) |
| **PKU moderada o leve** | 6–20 mg/dL (360–1.200 µmol/L) |
| **PKU clásica** | **> 20 mg/dL (> 1.200 µmol/L)** |

🧠 Para convertir: **1 mg/dL de Phe ≈ 60 µmol/L**. Cifras clave: **6 mg/dL = 360** (umbral de tratamiento) y **20 mg/dL = 1.200** (PKU clásica).

➕ Según Hillert et al. (2020), el 62 % de los pacientes en el mundo tiene PKU clásica, el 22 % PKU leve y el 16 % hiperfenilalaninemia leve.

#### Clínica *(Diap. 24)*

- **Neonatal**: **periodo libre de síntomas** (la madre metaboliza la Phe durante el embarazo).
- Sin tratamiento aparecen: **vómito**, **olor a ratón**, **convulsiones**, **alteraciones de la pigmentación** y **eccema**.
- **Compromiso cognitivo** progresivo y **trastornos del comportamiento**.
- Con **diagnóstico, manejo y control** tempranos, el desarrollo es casi normal.
- La clase menciona un CI ~10 puntos por debajo de la media. ➕ Matiz: sin tratamiento, la PKU clásica produce una **discapacidad intelectual grave**. La pérdida leve de CI (y las dificultades de función ejecutiva) se describe en pacientes **tratados** tarde o con mal control.

#### Diagnóstico *(Diap. 25)*

1. **Prueba del talón** en el recién nacido (gota de sangre seca en papel de filtro).
2. **Confirmación**: **nivel de fenilalanina en sangre** y **análisis genético** de *PAH*.
3. **Diagnóstico temprano**: crucial para prevenir el daño cerebral con tratamiento oportuno.

- Las fotos muestran las **pruebas históricas en orina**: **cloruro férrico** (color verde con fenilpiruvato) y **dinitrofenilhidrazina** (precipitado amarillo con cetoácidos). Hoy se usa la espectrometría de masas en tándem (Phe y relación Phe/Tyr).
- ✅ La diapositiva da "> 20 mg/dL" como criterio de confirmación: ese es el corte de **PKU clásica**. Las guías (ACMG 2014; guía europea 2017) **tratan desde > 360 µmol/L (6 mg/dL)**.
- ➕ Siempre se deben **descartar los defectos de BH4** (pterinas y actividad de dihidropteridina reductasa).

#### Tratamiento *(Diap. 26)*

| Pilar | Detalle |
|---|---|
| **Dieta estricta baja en fenilalanina** | Restringir alimentos ricos en Phe: **carne, lácteos, frutos secos** (➕ huevo, leguminosas). ➕ Evitar el **aspartamo** (libera Phe). |
| **Suplementos nutricionales** | **Fórmulas con proteínas sintéticas sin fenilalanina** (por ejemplo, Phenyl-Free), que aportan el resto de aminoácidos y la tirosina |
| **Monitorización constante** | Phe en sangre **1–2 veces por semana el primer mes** y **cada 15 días el primer año**, para ajustar la dieta. ➕ Meta habitual: 120–360 µmol/L (2–6 mg/dL), de por vida |
| **Terapia enzimática** 💊 | ➕ **Pegvaliasa** (fenilalanina amonio liasa pegilada, que degrada la Phe sin necesitar PAH ni BH4): adultos con Phe > 600 µmol/L |
| **Cofactor o activadores de PAH** 💊 | ➕ **Sapropterina** (BH4 sintética) en pacientes que responden; **sepiapterina** (aprobada en la Unión Europea en junio de 2025 y por la FDA en julio de 2025) |
| **Terapia génica** | En **investigación** (ensayos clínicos); todavía no hay una aprobada |

🩺 ➕ **PKU materna**: una mujer con PKU y Phe alta durante el embarazo daña al feto (microcefalia, discapacidad intelectual, cardiopatía congénita), aunque el feto no tenga PKU. Debe controlar la Phe **antes de concebir** y durante toda la gestación. Por eso la dieta es **de por vida**.

---

### 4.8 Caso clínico 1: acidemia propiónica *(Diap. 27–28)*

#### Evolución

| Edad | Hallazgo | Diagnóstico que se dio |
|---|---|---|
| Día 1 | Rechazo de la vía oral, irritabilidad | — |
| Día 4 | Dificultad respiratoria, pérdida anormal de peso; gases con **acidosis metabólica** | Manejo sintomático y salida |
| 0–2 meses | Consultas cada semana por **hiporexia, hipotonía, vómito y somnolencia** | **Reflujo gastroesofágico** |
| 2,5 meses | **Convulsiones**; **pancitopenia** | — |
| 3 meses | Remisión a tercer nivel por sospecha de **síndrome linfoproliferativo**; acidosis metabólica | — |

📌 **¿Puede tener un EIM?** Sí. Claves del caso:

- Cuadro **intermitente** con **periodos libres de síntomas**.
- **Síntomas persistentes** que **no mejoran con el manejo habitual** (principio 2).
- **Hallazgos bioquímicos persistentes** (acidosis).
- Clínica **tipo intoxicación** (empieza al iniciar la alimentación).
- ⚠️ Se confundió el síntoma con la etiología (principio 3): "reflujo" y "síndrome linfoproliferativo".

#### Laboratorios *(Diap. 28)*

| Examen | Resultado | Interpretación |
|---|---|---|
| Gases | pH 7,12; pO₂ 60; pCO₂ 30; HCO₃⁻ 10 | **Acidosis metabólica** grave |
| Electrolitos | Na 135; K 3,5; Cl 103 mEq/L | Para calcular el anión *gap* |
| Hemograma | Leucocitos 2.340 (neutrófilos 1.200, linfocitos 1.100); Hb 9,5; Hto 27,5; plaquetas 115.000 | **Pancitopenia** (leucopenia con neutropenia, anemia, trombocitopenia) |
| PCR | Negativa | No sugiere infección |
| Glicemia, creatinina, BUN | 88 mg/dL; 0,03 mg/dL (✅ probablemente 0,3); 12 mg/dL | Normales |
| Parcial de orina | Normal | — |
| **Amonio** | 0,8 µg/mL (= 80 µg/dL ≈ 47 µmol/L) | En el límite superior para un lactante |
| **Ácidos orgánicos en orina** | **Metilcitrato, 3-hidroxipropionato, propionilglicina** | Patrón diagnóstico de **acidemia propiónica** |

📌 **Anión *gap*** = (Na⁺ + K⁺) − (Cl⁻ + HCO₃⁻) = (135 + 3,5) − (103 + 10) = **25,5 mEq/L** (sin K⁺: 22 mEq/L). En los dos casos está **elevado** (la clase da como normal 12 ± 5; el valor de referencia cambia según se incluya el potasio y según el laboratorio). **Acidosis metabólica con anión *gap* alto** = hay un ácido no medido (aquí, ácidos orgánicos).

➕ **Compensación**: con la fórmula de Winter, la pCO₂ esperada es 1,5 × 10 + 8 ± 2 = **21–25 mmHg**. Una pCO₂ de 30 indica que la compensación respiratoria es insuficiente (el lactante somnoliento hipoventila).

✅ El hemograma de la diapositiva dice "VCM 30, HCM 80": los valores están **invertidos** (VCM ~80 fL y HCM ~30 pg son los fisiológicamente posibles).

#### ➕ La enfermedad

- **Defecto**: **propionil-CoA carboxilasa** (dependiente de **biotina**; genes *PCCA* y *PCCB*), autosómica recesiva.
- **De dónde sale el propionato**: de los aminoácidos **isoleucina, valina, metionina y treonina**, de los ácidos grasos de cadena impar y de las bacterias intestinales.
- **Por qué hay pancitopenia**: los metabolitos tóxicos suprimen la médula ósea.
- **Por qué sube el amonio**: el propionil-CoA inhibe la síntesis de N-acetilglutamato, activador del ciclo de la urea.
- **Diagnóstico**: ácidos orgánicos en orina (como en el caso) y **acilcarnitinas** (propionilcarnitina, C3, elevada).
- **Tratamiento**: en la crisis, suspender proteínas, glucosa intravenosa, L-carnitina y manejo del amonio (ácido carglúmico, diálisis). A largo plazo, dieta restringida en esos aminoácidos con fórmula especial, carnitina, metronidazol (reduce el propionato intestinal) y, en casos seleccionados, trasplante hepático.

🧠 Los precursores del propionato: **"VOMIT"** = **V**alina, ácidos grasos de cadena **O**dd (impar), **M**etionina, **I**soleucina, **T**reonina.

---

### 4.9 Grupo 2: metabolismo energético *(Diap. 29–30)*

#### Qué incluye *(Diap. 29)*

- **Sustratos**: glucosa, ácidos grasos, cuerpos cetónicos, ácidos monocarboxílicos.
- **Mitocondria**: oxidación aeróbica de la glucosa, **cadena respiratoria**, transportadores mitocondriales de moléculas energéticas, síntesis de coenzima A.
- 📌 **Deficiencia en la producción o en la utilización de la energía.**
- 📌 Órganos más afectados (los de mayor demanda energética): **hígado, músculo, corazón y cerebro**.

#### Síntomas comunes *(Diap. 30)*

- **Hipoglicemia, hiperlactatemia, acidosis, hiper- o hipocetonemia.**
- **Hepatomegalia**, **hipotonía generalizada grave**, **miopatía**, **cardiomiopatía**, retraso del desarrollo, **insuficiencia cardiaca**, **muerte súbita**, atrofia óptica o cerebral.
- **Crisis recurrentes desencadenadas por eventos intercurrentes** (infección, ayuno).
- **Dismorfismo, displasias y malformaciones** en algunos (alteraciones de la vía de las pentosas y algunos defectos mitocondriales). ⚠️ Esto los diferencia del tipo intoxicación, que no altera el desarrollo fetal.
- **Diagnóstico**: pruebas funcionales (glucosa, cetonas y lactato en ayuno y tras la alimentación), análisis enzimáticos en tejidos o pruebas moleculares.
- **Solo unos pocos son tratables.**

---

### 4.10 Caso clínico 2: glucogenosis tipo VI *(Diap. 31–33)*

*(Fuente: Rev Gastroenterol Perú 2020;40(1).)*

#### Historia

- Primera gestación controlada, padres sanos **no consanguíneos**; peso al nacer 3.000 g, talla 50 cm, **sin hipoglicemia** neonatal.
- **4 años**: hospitalizado por **hepatomegalia y retraso del crecimiento**; dado de alta como "hepatomegalia fisiológica".
- **15 años**: remitido a gastroenterología por **hepatomegalia e hipertransaminasemia** con dolor en hipocondrio derecho de un año de evolución.
- **Examen**: peso 41,5 kg y talla 147 cm (**< percentil 10**), abdomen globuloso, circulación colateral, hígado de ~12 cm.

#### Laboratorios *(Diap. 32–33)*

| Examen | Resultado | Referencia | Lectura |
|---|---|---|---|
| AST (TGO) | **382 U/L** | 0–34 | ↑↑ |
| ALT (TGP) | **189 U/L** | 10–49 | ↑ |
| Bilirrubina total / indirecta | 2,6 / 1,8 mg/dL | ≤ 1 / ≤ 0,8 | ↑ leve |
| Albúmina | 4,4 g/dL | 3,5–5 | Normal (síntesis hepática conservada) |
| Colesterol total | 174 mg/dL | 135–200 | Normal |
| Triglicéridos | **182 mg/dL** | 45–150 | ↑ |
| LDL / HDL | 123 / **14** mg/dL | < 130 / 35–55 | HDL bajo |
| Glicemia | 89 mg/dL | 70–110 | Normal |
| Insulina | 47,34 µUI/mL | ✅ la diapositiva pone "70–110" (rango de glicemia copiado por error) | Elevada para un valor basal habitual |
| IGF-1 | **45 ng/mL** | 116–200 | **Bajo** (retraso del crecimiento) |
| **CK** | **1.517 U/L** | 24–195 | **↑↑** |
| Lactato | 1,3 mmol/L | < 2 | **Normal** |
| Ácido úrico | 3,5 mg/dL | 3,5–7 | **Normal** |
| Cetonas en orina | Negativas | — | — |

- Se descartaron hepatitis B y C, toxoplasmosis, citomegalovirus y hepatitis autoinmune; hierro e inmunoglobulinas normales; cortisol y perfil tiroideo normales.
- **Ecografía Doppler**: hígado de 133 mm, **ecogenicidad aumentada**, parénquima homogéneo, sin lesiones focales; vena porta normal.
- **Biopsia hepática**: hepatocitos claros y aumentados de tamaño, cargados de glucógeno.
- 📌 **Diagnóstico: glucogenosis tipo VI (enfermedad de Hers).**

#### ➕ Para entender el caso

- **Glucogenosis tipo VI**: déficit de la **glucógeno fosforilasa hepática** (gen *PYGL*), autosómica recesiva. El hígado guarda glucógeno pero no puede liberarlo bien: **hepatomegalia**, **retraso del crecimiento**, hipoglicemia leve en ayuno con cetosis, transaminasas y lípidos elevados. Suele ser **leve y mejorar con la edad**. Se trata con comidas frecuentes, almidón de maíz crudo y dieta rica en proteínas.
- **Diferencia con la glucogenosis tipo I** (von Gierke): en la tipo I hay **lactato y ácido úrico altos**, triglicéridos muy elevados e hipoglicemia grave. Aquí lactato y ácido úrico son **normales**.
- ⚠️ **Detalle para pensar**: la **CK de 1.517** y una AST mayor que la ALT sugieren **compromiso muscular**, que no es típico de la tipo VI pura. Hace considerar la **tipo III** (déficit de enzima desramificante, hígado y músculo) o algunas formas de la **tipo IX** (fosforilasa cinasa). Clínicamente se superponen; el subtipo se confirma con **estudio molecular**.

---

### 4.11 Grupo 3: moléculas complejas *(Diap. 34–36)*

#### Características *(Diap. 34)*

📌 **Heterogéneas.**

- **Síntomas progresivos.**
- Compromiso de **un sistema** o **multisistémico**.
- **No hay episodios de agudización** (⚠️ diferencia clave con el tipo intoxicación).
- **Gran morbimortalidad.**

Afectan organelos: **lisosoma** (degradación de glucoesfingolípidos, mucopolisacáridos y otras macromoléculas), **peroxisoma** (sales biliares, oxidación de ácidos grasos de cadena muy larga y ácido fitánico), retículo endoplásmico, aparato de Golgi (cadenas de oligosacáridos de glucoproteínas) y mitocondria.

#### Defectos del catabolismo: enfermedades de depósito *(Diap. 35)*

| Compuesto | Defecto y localización | Trastornos y hallazgos principales |
|---|---|---|
| **Esfingolípidos** | Degradación (lisosoma, Golgi) | **Esfingolipidosis**: hepatoesplenomegalia, neurodeterioro, crisis óseas y neurológicas |
| **Lipopigmentos** | Degradación (lisosoma) | **Lipofuscinosis ceroides**: epilepsia, regresión mental, atrofia óptica, retinitis |
| **Glucosaminoglucanos (GAG)** | Degradación (lisosoma) | **Mucopolisacaridosis**: disostosis múltiple, hepatoesplenomegalia, compromiso neurológico y ocular |
| **Oligosacáridos, glucoproteínas, ácido siálico** | Degradación (lisosoma) | Oligosacaridosis, glucoproteinosis, mucolipidosis, sialidosis: disostosis múltiple, hepatoesplenomegalia, deterioro cognitivo, angioqueratomas |
| **Glucógeno** | Degradación (citosol, lisosoma) | **Glucogenosis**: hepatomegalia, hipoglicemia, miopatía, cardiomiopatía (**Pompe**); glucogenosis cerebral (enfermedad de Lafora) |
| **Lípidos neutros** | Degradación (citosol, lisosoma) | Enfermedades de depósito de lípidos neutros; esteatosis secundaria en muchos EIM |

#### Defectos de síntesis y reciclaje: sin material de depósito *(Diap. 36)*

| Compuesto | Trastornos y hallazgos principales |
|---|---|
| Glucógeno hepático y muscular (síntesis) | Glucogenosis 0a (hipoglicemia cetósica); 0b y glucogenina (miopatía, cardiomiopatía) |
| Ácidos grasos de cadena larga y muy larga, eicosanoides | Defectos de β/α-oxidación peroxisomal y de elongación: sistema nervioso, hueso, ojo, piel, hígado |
| Triglicéridos y lípidos neutros | Defectos de síntesis y lipólisis: hígado, músculo, piel |
| Esfingolípidos (ceramida, esfingomielina, glucoesfingolípidos) | Sistema nervioso central y periférico, piel (ictiosis), retina |
| Glucosaminoglucanos (síntesis) | Tejidos conectivos: hueso, cartílago, ligamentos, piel, escleras |
| Fosfolípidos (plasmalógenos, cardiolipina) | Sistema nervioso, músculo, piel, hueso, ojo, sistema inmune |
| Proteínas y lípidos glicosilados | **Trastornos congénitos de la glicosilación (CDG)**: más de 60 de tipo N, más de 10 de tipo O; sistema nervioso, músculo, piel, ojo, hígado, hueso |
| Isoprenoides (más de 30) | Colesterol: anomalías morfogenéticas congénitas (➕ Smith-Lemli-Opitz); ácidos biliares: colestasis y neurodegeneración; esteroides; dolicol (CDG); ubiquinona (defectos mitocondriales) |
| Dislipidemias (más de 20) | Aterosclerosis y enfermedad coronaria prematura |

---

### 4.12 Caso clínico 3 y mucopolisacaridosis *(Diap. 37–62)*

#### Caso: MPS tipo I, forma Scheie *(Diap. 37)*

- Sin antecedentes relevantes. **Desarrollo psicomotor normal**: sostén cefálico 4 meses, sedestación 7 meses, marcha 9 meses, lenguaje 12 meses, escolarizado desde los 4 años.
- **Síntomas tempranos**: **mano en garra**. Primer diagnóstico propuesto: **MPS IV**.
- Después: **talla baja patológica**.
- **Alfa-L-iduronidasa** muy baja en gota de sangre seca (0,0 y 0,08; referencia 1,5–8,5) y en leucocitos (0,6 y 0,67 nmol/mg de proteína/h).
- 📌 Cuadro **progresivo**, **sin episodios de agudización**, que compromete **un sistema (esquelético)** → **MPS tipo I, forma Scheie**.

➕ Para entender el caso:

- **MPS I**: déficit de **alfa-L-iduronidasa** (gen *IDUA*), autosómica recesiva; se acumulan **dermatán y heparán sulfato**. Es un espectro: **Hurler** (grave, discapacidad intelectual, sin tratamiento fallece en la infancia), **Hurler-Scheie** (intermedia) y **Scheie** (atenuada, **inteligencia normal**, rigidez articular, opacidad corneal, valvulopatía, túnel del carpo).
- ⚠️ **Por qué no era MPS IV**: la **MPS IV (Morquio)** se caracteriza por **hiperlaxitud** articular; la **mano en garra** (rigidez, contracturas) orienta a **MPS I, II o VI**. El desarrollo normal del paciente encaja con la forma atenuada (Scheie).
- 💊 Tratamiento: **terapia de reemplazo enzimático** (laronidasa); en la forma grave (Hurler), **trasplante de progenitores hematopoyéticos** antes de los 2–2,5 años.

#### ¿Cómo diagnosticar más temprano? *(Diap. 39–41)*

- La clase muestra tres fotos y pregunta cuál es "dismórfica". 📌 El mensaje: **no todos los pacientes con MPS tienen rasgos físicos gruesos o toscos**. Un fenotipo de apariencia normal **no descarta** una mucopolisacaridosis *(Diap. 49)*.
- La herramienta es la **historia clínica bien hecha**.

#### La historia clínica orientada a MPS *(Diap. 42–46)*

| Parte de la historia | Qué buscar |
|---|---|
| **Antecedentes familiares** (3 generaciones como mínimo) | **Apellidos en común**, **coterráneos**, **consanguinidad**, talla baja, infecciones respiratorias recurrentes, retraso del desarrollo, rasgos físicos particulares, problemas articulares |
| **Revisión por sistemas** | **Patrón del sueño**, **ronquido**, **respiración ruidosa**, actividad física, **limitación de la movilidad**, hábitos de alimentación e intestinales |
| **Antecedente prenatal** | **Hepatoesplenomegalia**, **acortamiento del fémur**, **hidrops fetal no inmune** (➕ sobre todo en MPS VII) |
| **Antecedentes patológicos** | **Obstrucción de la vía aérea**, **apnea del sueño**, **infecciones recurrentes** (otitis, sinusitis, rinitis), **deterioro auditivo**, **hepatomegalia**, **síndrome del túnel del carpo** (raro en niños: bandera roja), **displasia de cadera** |
| **Antecedentes quirúrgicos** | **Hernias recurrentes** (umbilicales, inguinales), **amigdalectomía**, **adenoidectomía**, **timpanostomías** |
| **Crecimiento** | Talla **normal hasta los 2 años** y **detención del crecimiento desde los 3 años** (< percentil 3) |

#### Examen físico *(Diap. 47–54)*

| Región | Hallazgos |
|---|---|
| **Cráneo y cara** | **Perímetro cefálico aumentado**, **rasgos faciales toscos**, **alteraciones dentales**, **macroglosia** |
| **Evolución facial** | Desde los **3–6 meses**, ligero engrosamiento de los rasgos; **frente prominente**; **puente nasal deprimido**, punta nasal ancha, **narinas antevertidas**; **mejillas llenas** |
| **Cavidad oral** (*Diap. 51*) | Defectos del esmalte, pérdida de estructura dental, mordida abierta anterior, macroglosia, **diastemas**, quistes dentígeros múltiples, **hiperplasia gingival**, malposición de dientes no erupcionados, reabsorción radicular, deterioro de las articulaciones temporomandibulares |
| **Piel** | **Manchas mongólicas extensas** (melanocitosis dérmica). La cebra es el símbolo de las enfermedades raras ("si oyes cascos, piensa en caballos… pero a veces es una cebra") |
| **Manos** | **Mano en garra** (rigidez) en la mayoría; **hiperlaxitud** en la MPS IV |
| **Articulaciones** | **Contracturas** de rodillas y codos, marcha en puntas |

✅ La diapositiva 53 asocia la hiperlaxitud a las MPS IV, III y VII. La asociación clásica y constante es con la **MPS IV (Morquio)**; en la MPS III los signos somáticos son leves y en la mayoría de las demás predominan la rigidez y las contracturas.

#### Historia natural *(Diap. 55–57)*

- Paciente con **MPS IVA** fotografiado de los 4 a los 30 años: talla baja progresiva y uso de silla de ruedas en la adultez (monografía de elosulfasa alfa, el reemplazo enzimático de la MPS IVA).
- Paciente con **MPS VII** que inició con hidrops neonatal y fue engrosando sus rasgos con los años (Montaño et al., 2016).
- Niña fotografiada de los 10 a los 39 meses: los rasgos se vuelven toscos poco a poco.

#### Tipos de MPS *(Diap. 58–61)*

📌 **Lo que diferencia una MPS de otra es la enzima que falta** para degradar un tipo de glucosaminoglucano. **Las 11 deficiencias enzimáticas conocidas provocan 7 tipos de MPS**: I, II, III, IV A (y B), VI, VII y IX.

📌 Es una **enfermedad multisistémica**: facies típica, cuello corto, **disostosis múltiple**, **displasia de cadera**, **infecciones respiratorias recurrentes**, **macroglosia y dentición anormal**, **laxitud ligamentaria**, **deficiencia auditiva**, **opacidad corneal**, **pectus carinatum**, **cifosis y escoliosis**, **valvulopatía cardiaca**, **hernias umbilicales e inguinales** y **talla baja**.

➕ **Tabla de las MPS** (útil para el examen)

| MPS | Epónimo | Enzima deficiente | GAG acumulado | Herencia | Rasgos distintivos | 💊 Reemplazo enzimático |
|---|---|---|---|---|---|---|
| **I** | Hurler / Hurler-Scheie / Scheie | Alfa-L-iduronidasa | Dermatán y heparán sulfato | AR | Opacidad corneal; espectro de grave a atenuada | Laronidasa |
| **II** | Hunter | Iduronato-2-sulfatasa | Dermatán y heparán sulfato | **Ligada al X** | **Sin opacidad corneal**; piel "en empedrado" | Idursulfasa |
| **III (A–D)** | Sanfilippo | Cuatro enzimas distintas | **Heparán sulfato** | AR | **Predomina el sistema nervioso** (conducta, regresión); rasgos somáticos leves | — |
| **IV (A, B)** | Morquio | A: N-acetilgalactosamina-6-sulfatasa; B: beta-galactosidasa | **Queratán sulfato** | AR | **Displasia esquelética grave, hiperlaxitud, inteligencia normal**; hipoplasia de la apófisis odontoides | Elosulfasa alfa (IVA) |
| **VI** | Maroteaux-Lamy | Arilsulfatasa B | Dermatán sulfato | AR | Inteligencia normal, rasgos somáticos marcados | Galsulfasa |
| **VII** | Sly | Beta-glucuronidasa | Varios | AR | **Hidrops fetal no inmune** | Vestronidasa alfa |
| **IX** | Natowicz | Hialuronidasa | Ácido hialurónico | AR | Masas periarticulares | — |

🧠 **Hunter es "el único que caza en el X"**: la MPS II es la única ligada al X (por eso afecta casi solo a varones) y tampoco "ve nublado" (no hay opacidad corneal). **Sanfilippo = "San Filipo se porta mal"**: predomina la conducta. **Morquio = "más laxo"**.

#### Diagnóstico *(Diap. 62)*

1. **Pruebas de tamizaje** (gota de sangre seca, GAG en orina).
2. **Estudios bioquímicos**: **electroforesis de GAG** (bandas de condroitín, queratán, dermatán y heparán sulfato según el tipo).
3. **Actividad de la enzima en leucocitos** (confirmación).
4. **Estudio molecular**.

La diapositiva menciona a **ACOPEL** (Asociación Colombiana de Pacientes con Enfermedades de Depósito Lisosomal).

---

### 4.13 Reflexiones y conclusiones *(Diap. 63–70)*

#### Cinco reflexiones *(Diap. 63–67)*

1. **"No se diagnostica lo que no se conoce o aquello en lo que no se piensa"** (M. A. Moreno). Se requiere **interés y voluntad**.
2. **Pensar más allá de lo evidente** (como Sherlock Holmes): buscar **claves** (un metabolito elevado o un síntoma persistente) y seguir una **ruta secuencial y lógica** de pruebas diagnósticas.
3. **Hacer seguimiento** a los pacientes; si no se conoce la causa del síntoma, **estudiar todos los diagnósticos diferenciales**; **mantenerse actualizado** (surgen nuevos métodos y medicamentos).
4. **Recolectar muestras en el periodo crítico** *(Diap. 66)*: si sospecha un EIM, tome y guarde muestras **durante la crisis**, antes de que el tratamiento normalice los metabolitos.
5. **No rendirse** *(Diap. 67)*: estudiar los síntomas, no descansar hasta confirmar o descartar la sospecha, apoyarse en expertos (laboratorio, nutricionistas, especialistas), comunicarse bien con los padres y no tener miedo de preguntar. La clase recomienda el libro *La criptología de la enfermedad*, del Dr. **Luis Alejandro Barrera Avellaneda**, pionero colombiano en EIM.

#### Protocolo de muestras en emergencias *(Diap. 66, Saudubray)*

| Muestra | Estudios inmediatos | Qué guardar |
|---|---|---|
| **Orina** | **Olor** y **color**; tira para **cetonas**, **sustancias reductoras**, pH y sulfitos; electrolitos, urea, creatinina, ácido úrico | Muestra fresca refrigerada; **congelar a −20 °C** muestras de antes y después del tratamiento (y una alícuota a las 24 h) para ácidos orgánicos, aminoácidos, ácido orótico y porfirinas |
| **Sangre** | Hemograma, **electrolitos (anión *gap*)**, glucosa, calcio, **gases**, ácido úrico, tiempo de protrombina, transaminasas, CK, **amonio**, **lactato**, **3-hidroxibutirato**, ácidos grasos libres | **Plasma heparinizado (5 mL) a −20 °C**; **2 gotas en papel de filtro**; **sangre total en EDTA (10 mL) congelada** para estudios moleculares; homocisteína total, aminoácidos, **acilcarnitinas** (tándem), ácidos orgánicos, porfirinas, neurotransmisores |
| **Otros** | Punción lumbar, radiografía de tórax, ecocardiograma y electrocardiograma, ecografía cerebral y electroencefalograma | **Biopsia de piel** (cultivo de fibroblastos); **1 mL de LCR congelado**; biopsias de hígado y músculo *post mortem* |

#### Conclusiones *(Diap. 69–70)*

1. Los EIM son **enfermedades raras**.
2. **Síntomas inespecíficos**; en el periodo neonatal, cuadro de **"intoxicación"**.
3. El diagnóstico es **por descarte**.
4. **No se diagnostican si no se buscan.**
5. En neonatos, el enfoque puede hacerse por **compromiso neurológico, hepático o cardiaco**.
6. Los **laboratorios iniciales son asequibles**.
7. **Congelar muestras durante las crisis** puede hacer la diferencia en el diagnóstico.
8. El **tamizaje metabólico no es costoso**.
9. **La sobrevida depende del diagnóstico.**
10. Requieren **manejo multidisciplinario**.
11. Son **hereditarios**: se debe hacer **asesoría genética a la familia**.

---

### 4.14 ➕ Pistas de laboratorio para orientar un EIM

No está en las diapositivas; organiza los laboratorios "asequibles" de las conclusiones.

| Hallazgo | Pensar en |
|---|---|
| **Acidosis metabólica con anión *gap* alto** y cetosis | **Acidemias orgánicas** (propiónica, metilmalónica, isovalérica), enfermedad de orina con olor a jarabe de arce |
| **Hiperamonemia** sin acidosis (a menudo con alcalosis respiratoria) | **Defectos del ciclo de la urea** |
| **Hipoglicemia hipocetósica** (sin cetonas) | Defectos de la **β-oxidación de ácidos grasos** (por ejemplo, MCAD) o **hiperinsulinismo** |
| Hipoglicemia con **lactato y ácido úrico altos** y hepatomegalia | **Glucogenosis tipo I** |
| **Lactato alto** persistente | Defectos **mitocondriales** o de la **piruvato deshidrogenasa** |
| **Sustancias reductoras en orina** (no glucosa), ictericia, cataratas, sepsis por *E. coli* | **Galactosemia** |
| **Olor** anormal | Ratón o moho: PKU · jarabe de arce: MSUD · pies sudados: acidemia isovalérica · repollo: tirosinemia tipo I |
| Pancitopenia con acidosis | Acidemias orgánicas (propiónica, metilmalónica) |

---

### ✅ Verificación de datos de la clase (capítulo 4)

| Diapositiva | Dice | Verificación |
|---|---|---|
| 4 | PKU y galactosemia "descubiertas" en 1950–1980 | PKU: Følling, **1934**. En los 50 se identificaron los defectos enzimáticos y la dieta (Bickel, 1953); tamizaje de Guthrie en 1963 |
| 7 | Más de 1.015 EIM | La ICIMD (2021) lista **1.450** ([Ferreira et al., *J Inherit Metab Dis* 2021](https://pubmed.ncbi.nlm.nih.gov/33340416/)) |
| 9 | Hipotiroidismo congénito "1:2500-3:500" | Error de digitación: 1:2.500–1:3.500 |
| 9 | Ley 1980 de 2019 | Correcta. Actualización: **Resolución 117 de 2026** hace obligatorias las siete pruebas ([MinSalud](https://www.minsalud.gov.co/Comunicaciones/noticias/2026/Paginas/minsalud-amplia-tamizaje-neonatal.aspx)) |
| 19 | "Melania", "Discapcacidas" | Melanina; discapacidad |
| 22 | Más de 600 mutaciones en *PAH* | Más de 950 (2016); más de 3.000 en PAHvdb (2026) |
| 24 | CI 10 puntos por debajo de la media | Corresponde a pacientes tratados; sin tratamiento la discapacidad es grave |
| 25 | Confirmación con Phe > 20 mg/dL | Es el corte de PKU clásica; el tratamiento empieza desde > 6 mg/dL (360 µmol/L) |
| 26 | Terapia enzimática y génica | Pegvaliasa y sapropterina aprobadas; **sepiapterina** aprobada en 2025 ([FDA](https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2025/219666Orig1s000ltr.pdf)); terapia génica aún en ensayos |
| 28 | VCM 30, HCM 80; creatinina 0,03 | Valores invertidos (VCM ~80, HCM ~30); creatinina probablemente 0,3 |
| 32 | Referencia de insulina 70–110 | Es el rango de glicemia, copiado por error |
| 33 | Glucogenosis VI con CK de 1.517 | La CK alta sugiere compromiso muscular (considerar tipos III o IX); confirmar con estudio molecular |
| 53 | Hiperlaxitud en MPS IV, III, VII | La asociación clásica es con la MPS IV (Morquio) |

---

### Autoevaluación (capítulo 4)

<details><summary>1. ¿Por qué los EIM tipo intoxicación no causan malformaciones y debutan días después del nacimiento?</summary>

Porque durante el embarazo la placenta y la madre eliminan el metabolito tóxico. El bebé nace sano y se intoxica cuando empieza a alimentarse (intervalo libre).
</details>

<details><summary>2. Cita los seis rasgos comunes de los EIM tipo intoxicación.</summary>

No alteran el desarrollo fetal; intervalo libre de síntomas; signos agudos, crónicos o progresivos; crisis por ayuno, estrés catabólico o ingesta; diagnóstico con aminoácidos, ácidos orgánicos y acilcarnitinas; tratables retirando la toxina.
</details>

<details><summary>3. ¿Cuál es la enzima, el cofactor, el gen y el cromosoma de la PKU?</summary>

Fenilalanina hidroxilasa; tetrahidrobiopterina (BH4); *PAH*; cromosoma 12.
</details>

<details><summary>4. ¿Por qué un niño con PKU no tratada tiene piel y pelo claros?</summary>

Porque baja la tirosina, precursora de la melanina (y la Phe alta inhibe la tirosinasa).
</details>

<details><summary>5. Un neonato tiene Phe alta en el tamizaje. Antes de iniciar solo dieta, ¿qué debes descartar y por qué?</summary>

Un defecto del cofactor BH4 (por ejemplo, deficiencia de dihidropteridina reductasa): también eleva la Phe, pero además falta la síntesis de neurotransmisores y requiere otro tratamiento.
</details>

<details><summary>6. Calcula el anión gap del caso 1 y di qué significa.</summary>

(135 + 3,5) − (103 + 10) = 25,5 mEq/L: elevado. Acidosis metabólica por un ácido no medido (ácidos orgánicos).
</details>

<details><summary>7. ¿Qué metabolitos urinarios dieron el diagnóstico de acidemia propiónica?</summary>

Metilcitrato, 3-hidroxipropionato y propionilglicina.
</details>

<details><summary>8. En una glucogenosis con hepatomegalia, ¿qué hallazgos te alejan de la tipo I?</summary>

Lactato y ácido úrico normales y ausencia de hipoglicemia grave.
</details>

<details><summary>9. ¿En qué se diferencian clínicamente los EIM de moléculas complejas de los tipo intoxicación?</summary>

Los de moléculas complejas son progresivos, sin crisis agudas, a menudo multisistémicos y en general no tratables; los de intoxicación tienen crisis agudas desencadenadas y son tratables.
</details>

<details><summary>10. Niño con mano en garra, talla baja y desarrollo normal. ¿Qué enzima mides primero y qué MPS sospechas?</summary>

Alfa-L-iduronidasa; MPS I forma atenuada (Scheie).
</details>

<details><summary>11. ¿Por qué un niño de 6 años con síndrome del túnel del carpo debe hacerte pensar en una MPS?</summary>

Porque el túnel del carpo es muy raro en niños, y el depósito de GAG en el retináculo flexor es una causa clásica.
</details>

<details><summary>12. ¿Cuál es la única MPS ligada al X?</summary>

La MPS II (Hunter).
</details>

<details><summary>13. ¿Qué muestras congelas en una crisis metabólica neonatal?</summary>

Plasma heparinizado a −20 °C, gotas en papel de filtro, sangre en EDTA para estudios moleculares, orina antes y después del tratamiento a −20 °C y, si se hace punción lumbar, 1 mL de LCR.
</details>

---

### Glosario (capítulo 4)

| Término | Definición |
|---|---|
| **Acilcarnitinas** | Ésteres de carnitina que reflejan qué acil-CoA se acumula; se miden por espectrometría de masas en tándem |
| **Anión *gap*** | (Na⁺ + K⁺) − (Cl⁻ + HCO₃⁻); elevado si hay un ácido no medido |
| **BH4** | Tetrahidrobiopterina, cofactor de la fenilalanina hidroxilasa |
| **Disostosis múltiple** | Conjunto de alteraciones esqueléticas radiológicas típicas de las MPS |
| **GAG** | Glucosaminoglucanos (mucopolisacáridos): dermatán, heparán, queratán y condroitín sulfato |
| **Hidrops fetal no inmune** | Acumulación de líquido en el feto sin aloinmunización; una causa son las enfermedades lisosomales |
| **Intervalo libre** | Periodo sin síntomas entre el nacimiento y la primera crisis |
| **Tamizaje neonatal** | Detección en todos los recién nacidos, por gota de sangre del talón, de enfermedades tratables antes de que den síntomas |
| **Terapia de reemplazo enzimático** | Administración intravenosa de la enzima recombinante que falta |

---

### Referencias (capítulo 4)

De la clase:

- Saudubray JM, García-Cazorla À. Inborn errors of metabolism overview. *Pediatr Clin N Am.* 2018;65:179-208.
- Saudubray JM, Mochel F, Lamari F, García-Cazorla A. Proposal for a simplified classification of IMD based on a pathophysiological approach. *J Inherit Metab Dis.* 2019;42:706-727.
- Lanpher B, Brunetti-Pierri N, Lee B. Inborn errors of metabolism: the flux from Mendelian to complex diseases. *Nat Rev Genet.* 2006;7:449-460.
- Hillert A, et al. The genetic landscape and epidemiology of phenylketonuria. *Am J Hum Genet.* 2020;107:234-250.
- Vockley J, et al. Phenylalanine hydroxylase deficiency: diagnosis and management guideline. *Genet Med.* 2014 (ACMG).
- Martín Sánchez MJ, et al. Errores innatos del metabolismo: aproximación diagnóstica en atención primaria. *Bol Pediatr.* 2007;47:111-115.
- Montaño AM, et al. Clinical course of Sly syndrome (MPS VII). *J Med Genet.* 2016;53:403-418.
- Ley 1980 de 2019, Programa de Tamizaje Neonatal en Colombia.

Usadas en la verificación:

- Ferreira CR, et al. An international classification of inherited metabolic disorders (ICIMD). *J Inherit Metab Dis.* 2021;44:164-177. <https://pubmed.ncbi.nlm.nih.gov/33340416/>
- Ministerio de Salud de Colombia. Resolución 117 de 2026 (nota de prensa del 30 de enero de 2026). <https://www.minsalud.gov.co/Comunicaciones/noticias/2026/Paginas/minsalud-amplia-tamizaje-neonatal.aspx>
- Ley 1980 de 2019, artículo 2 (definición de tamizaje neonatal básico): <https://leyes.co/se_crea_el_programa_de_tamizaje_neonatal_en_colombia/2o.htm>
- Blau N. Genetics of phenylketonuria: then and now. *Hum Mutat.* 2016;37:508-515. <https://pubmed.ncbi.nlm.nih.gov/26919687/>
- Analysis of PAH genetic variation and phenotypic diversity in the PAHvdb. *Int J Mol Sci.* 2026;27:6772. <https://pubmed.ncbi.nlm.nih.gov/42589429/>
- FDA. Carta de aprobación de Sephience (sepiapterina), 2025. <https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2025/219666Orig1s000ltr.pdf>

[↑ Volver al índice general](#índice-general)

---

## 5. Mecanismos de reparación del ADN: de la lesión molecular a la clínica

> Basada en la clase *"Mecanismos de reparación del ADN. De la lesión molecular a la clínica"* (Prof. Sandra Ospina Lagos, Genética y Ciencias Biomédicas) y ampliada con lo que necesitas para entenderla a fondo y para el examen.
>
> Sus tarjetas están en el submazo *05 Reparación del ADN* de [`Genetica_Biologia_Molecular.apkg`](Genetica_Biologia_Molecular.apkg). Los símbolos 📌 ➕ ⚠ 🩺 💊 🧠 se explican al [inicio de la guía](#cómo-usar-esta-guía).

---

**Ruta recomendada:** lee la sección 5.1 (prerrequisitos) si no tienes fresca la estructura del ADN; después estudia las vías en orden (5.2 → 5.9), porque cada una se apoya en la anterior; termina con la integración (5.10), los casos (5.11) y las preguntas (5.12). El submazo de Anki sigue exactamente este orden.

---

### Índice (capítulo 5)

- [5.1 Prerrequisitos: lo mínimo que necesitas saber](#51-prerrequisitos-lo-mínimo-que-necesitas-saber)
- [5.2 El problema: el ADN se daña todo el tiempo](#52-el-problema-el-adn-se-daña-todo-el-tiempo)
- [5.3 Reversión directa del daño (MGMT, fotoliasa, ALKBH)](#53-reversión-directa-del-daño)
- [5.4 Reparación por escisión de bases (BER)](#54-reparación-por-escisión-de-bases-ber)
- [5.5 Reparación por escisión de nucleótidos (NER)](#55-reparación-por-escisión-de-nucleótidos-ner)
- [5.6 Reparación de apareamientos erróneos (MMR)](#56-reparación-de-apareamientos-erróneos-mmr)
- [5.7 Roturas de doble cadena: NHEJ y HR](#57-roturas-de-doble-cadena-nhej-y-hr)
- [5.8 Anemia de Fanconi y enlaces cruzados intercatenarios](#58-anemia-de-fanconi-y-enlaces-cruzados-intercatenarios)
- [5.9 Tolerancia al daño: síntesis translesión (TLS)](#59-tolerancia-al-daño-síntesis-translesión-tls)
- [5.10 Integración: de la biología a la clínica](#510-integración-de-la-biología-a-la-clínica)
- [5.11 Casos clínicos resueltos](#511-casos-clínicos-resueltos)
- [5.12 Preguntas de repaso resueltas y autoevaluación](#512-preguntas-de-repaso-resueltas-y-autoevaluación)
- [5.13 Trampas de examen](#513-trampas-de-examen)
- [5.14 Mnemotecnias](#514-mnemotecnias)
- [5.15 Glosario](#515-glosario)
- [5.16 Plan de estudio y cómo usar el mazo de Anki](#516-plan-de-estudio-y-cómo-usar-el-mazo-de-anki)
- [5.17 Bibliografía](#517-bibliografía)

---

### Objetivos de aprendizaje (capítulo 5) *(Diap. 2)*

Al terminar deberías poder:

1. **Clasificar** las lesiones del ADN según su origen (endógeno o exógeno) y su tipo químico.
2. **Describir** los pasos y proteínas clave de la reversión directa, BER, NER, MMR, NHEJ, HR y la síntesis translesión.
3. **Relacionar** cada tipo de lesión con la vía que la repara.
4. **Correlacionar** defectos de reparación con enfermedades: xeroderma pigmentoso, Lynch, BRCA, ataxia-telangiectasia, Fanconi, SCID.
5. **Explicar** la base molecular de terapias: temozolomida, cisplatino, inhibidores de PARP e inmunoterapia.

---

### 5.1 Prerrequisitos: lo mínimo que necesitas saber

➕ Esta sección no está en la clase, pero sin ella muchas diapositivas se memorizan sin entenderse.

#### 5.1.1 La anatomía del ADN que importa para la reparación

```
        5′ ──P──[azúcar]──P──[azúcar]──P──[azúcar]── 3′   ← esqueleto (enlaces fosfodiéster)
                   │            │            │
                 base         base         base          ← unida al azúcar por el ENLACE N-GLICOSÍDICO
                   ┊            ┊            ┊            ← puentes de hidrógeno (A=T, G≡C)
                 base         base         base
                   │            │            │
        3′ ──P──[azúcar]──P──[azúcar]──P──[azúcar]── 5′
```

- **Nucleótido** = base + desoxirribosa + fosfato.
- **Enlace N-glicosídico**: une la base al azúcar. Es el que rompen las **glicosilasas** (BER) y el que se hidroliza en la **depurinación**. Si se rompe, queda un **sitio AP** (apurínico/apirimidínico = abásico): azúcar sin base.
- **Enlace fosfodiéster**: forma el esqueleto. Lo cortan las **endonucleasas** (APE1, XPF–ERCC1, XPG, PMS2, Artemis…). Una sola hebra cortada es una **mella** o rotura de cadena sencilla (SSB); las dos, una rotura de doble cadena (DSB).
- **Purinas** (dos anillos): **A** y **G**. **Pirimidinas** (un anillo): **C**, **T** (y **U** en el ARN). 🧠 *"PURA Agua y Gas"*: PURinas = A, G.
  - Por eso se habla de **de*purina*ción** (las purinas se pierden con más facilidad) y de **dímeros de *pirimidina*** (la UV une C y T vecinas).
- Las hebras son **antiparalelas** (5′→3′ frente a 3′→5′). Las polimerasas solo sintetizan 5′→3′ y necesitan un extremo **3′-OH** libre. Casi todas las vías terminan igual: una nucleasa deja un hueco con 3′-OH, una polimerasa lo rellena y una **ligasa** sella.

#### 5.1.2 Lesión no es lo mismo que mutación

📌 Es la idea que da sentido a todo el tema.

- **Lesión**: alteración química o física del ADN (una base oxidada, un dímero, una rotura). Todavía es reparable porque la otra hebra conserva la información.
- **Mutación**: cambio de secuencia **fijado en ambas hebras** tras la replicación. Ya no parece daño: la célula no la "ve".

```
Lesión          1.ª replicación          2.ª replicación
O⁶-meG : C  ──►  O⁶-meG : T   ──►   A : T   (mutación G:C→A:T fijada)
```

La ventana para reparar es **antes de replicar**. Por eso la respuesta al daño detiene el ciclo celular.

#### 5.1.3 Vocabulario de mutaciones

| Término | Definición | Ejemplo del tema |
|---|---|---|
| **Transición** | Purina↔purina o pirimidina↔pirimidina | O⁶-meG → G:C→A:T; UV → C→T; desaminación de 5-metilC → C→T |
| **Transversión** | Purina↔pirimidina | 8-oxoG → G:C→T:A; tabaco y aflatoxina → G→T |
| **Indel** | Inserción o deleción pequeña | Deslizamiento en microsatélites (MMR defectuoso) |
| **Cambio de marco** (*frameshift*) | Indel no múltiplo de 3 en región codificante | TGFBR2, BAX en tumores MSI |

🧠 **Transición** = te quedas en la misma "clase" de base (como transitar dentro del mismo barrio). **Transversión** = cambias de "versión" (de purina a pirimidina o al revés).

#### 5.1.4 El ciclo celular y sus puntos de control

```
G1 ──[G1/S]──► S ──[intra-S]──► G2 ──[G2/M]──► M ──► G1
     (puntos de control entre corchetes)
```

- **G1/S**: impide replicar un ADN dañado (eje ATM → CHK2 → p53 → p21).
- **Intra-S**: frena la replicación si hay estrés replicativo (eje ATR → CHK1).
- **G2/M**: impide entrar en mitosis con roturas (ATR/ATM → CHK1/CHK2 → inhibición de CDC25 → CDK1 inactiva).
- En **S y G2** existe la **cromátida hermana**, molde perfecto para la recombinación homóloga. En **G1** (y en células que no se dividen, como las neuronas) no existe.

#### 5.1.5 Genes "cuidadores" y la hipótesis de los dos golpes (Knudson)

- Los genes de reparación son **supresores de tumores de tipo "cuidador"** (*caretakers*): su pérdida no hace proliferar a la célula directamente, sino que **aumenta la tasa de mutación** (fenotipo mutador), y así se acumulan mutaciones en oncogenes y en supresores "porteros" (*gatekeepers*, como APC o RB1).
- **Dos golpes**: la célula necesita perder **los dos alelos** para perder la función.
  - En **Lynch** y **BRCA** se hereda un alelo mutado (primer golpe en todas las células). El tumor aparece cuando una célula pierde el segundo alelo (pérdida de heterocigosidad, mutación o metilación). Por eso la **predisposición se hereda de forma autosómica dominante**, aunque a nivel celular el defecto sea recesivo.
  - En **XP, Fanconi, A-T, MAP, SCID por Artemis o Bloom** el paciente hereda **dos** alelos mutados: todas sus células carecen de la función, y la herencia es **autosómica recesiva**.
- 🩺 Consecuencia práctica: las células normales de una portadora de BRCA1 tienen un alelo funcional y reparan bien. Solo el tumor es deficiente. Esa diferencia es la que explotan los inhibidores de PARP (sección 5.10.1).

#### 5.1.6 ¿De dónde vienen los nombres?

| Prefijo | Origen | Ejemplos |
|---|---|---|
| **XP-A…G, V** | Grupos de complementación del xeroderma pigmentoso: células de pacientes que, fusionadas, **no** corrigen mutuamente el defecto tienen el mismo gen alterado | XPA, XPC, XPD |
| **ERCC** | *Excision Repair Cross-Complementing*: genes humanos que corrigen la sensibilidad a UV de mutantes de hámster | ERCC1, ERCC2 = XPD, ERCC6 = CSB |
| **MSH / MLH / PMS** | Homólogos de las proteínas bacterianas MutS y MutL | MSH2, MLH1, PMS2 |
| **RAD** | Mutantes de levadura sensibles a radiación | RAD51, RAD18 |
| **FANC** | Grupos de complementación de la anemia de Fanconi | FANCA, FANCD2, FANCD1 = BRCA2 |

---

### 5.2 El problema: el ADN se daña todo el tiempo

#### 5.2.1 La magnitud *(Diap. 4)*

📌 Cada célula de mamífero sufre **10⁴–10⁵ lesiones por día**. Con ~3×10⁹ pb por genoma y ~3×10¹³ células, sin reparación el genoma acumularía mutaciones incompatibles con la vida. La mayoría de las lesiones se repara en minutos u horas.

| Lesión | Lesiones/célula/día (aprox.) | Vía principal |
|---|---|---|
| Roturas de cadena sencilla (SSB) | 10⁴–5×10⁴ (la más frecuente) | BER/SSBR (PARP1, XRCC1) |
| Depurinación (sitios AP) | 2.000–10.000 | BER |
| 7-metilguanina | ~4.000 | BER (MPG) |
| 8-oxoguanina | 400–1.500 | BER (OGG1, MUTYH) |
| Desaminación de citosina | 100–500 | BER (UNG) |
| Roturas de doble cadena (DSB) | 10–50 | NHEJ / HR |
| O⁶-metilguanina | 10–30 | Reversión directa (MGMT) |

*Valores aproximados en células de mamífero; varían según el método (Lindahl 1993; Tubbs y Nussenzweig 2017; Hoeijmakers 2009).*

⚠️ Frecuencia y peligrosidad no van juntas. Las DSB son pocas, pero son las más peligrosas: una sola DSB sin reparar puede causar la pérdida de un brazo cromosómico, una translocación o la muerte celular. La O⁶-metilguanina es rara, pero muy mutagénica.

#### 5.2.2 Fuentes de daño: endógenas y exógenas *(Diap. 5)*

##### Endógenas (metabolismo normal)

| Proceso | Qué ocurre químicamente | Lesión y consecuencia |
|---|---|---|
| **Hidrólisis: depurinación** | Se hidroliza el enlace N-glicosídico de A o G | **Sitio AP**. No es "instructivo": al replicar, la polimerasa no sabe qué base poner |
| **Hidrólisis: desaminación de C** | C pierde su grupo amino → **U** | U se aparea con A → transición **C:G→T:A** si no se repara (UNG) |
| **Desaminación de 5-metilC** | 5-meC → **T** (base normal) | Desapareamiento **T:G** → transición C→T. ➕ Las CpG metiladas son puntos calientes de mutación; solo TDG (y MBD4) lo detectan |
| **Especies reactivas de oxígeno (ROS)** | Oxidación de bases y del azúcar | **8-oxoguanina** (se aparea con A → transversión G:C→T:A) y roturas de cadena |
| **Alquilación espontánea** | La **S-adenosilmetionina (SAM)**, donador normal de metilos, metila el ADN por error | 7-meG (la más abundante, poco dañina), 3-meA (bloquea la replicación), algo de O⁶-meG (mutagénica) |
| **Errores de replicación** | La polimerasa incorpora la base equivocada o "resbala" | Apareamientos erróneos y bucles de inserción/deleción por **deslizamiento** en repeticiones (MMR) |
| **Aldehídos** (formaldehído, acetaldehído) | Reaccionan con bases de ambas hebras o con proteínas | **Enlaces cruzados** intercatenarios y ADN–proteína (vía de Fanconi) |

➕ **¿Por qué el ADN usa timina y no uracilo?** Porque la desaminación de C produce U. Si el ADN usara U normalmente, la célula no podría distinguir un U legítimo de uno nacido por daño. Al usar T, **todo U en el ADN es anómalo** y UNG lo retira sin ambigüedad. La excepción es la 5-metilC: al desaminarse da T, una base "legítima", y por eso las CpG mutan tanto.

##### Exógenas (ambiente y fármacos)

| Agente | Lesión | Detalle clínico |
|---|---|---|
| **Radiación UV-B** | **Dímeros de pirimidina ciclobutano (CPD)** y **fotoproductos 6-4** entre pirimidinas vecinas de la misma hebra | ➕ CPD ≈ 75 % de los fotoproductos (distorsionan poco); 6-4 ≈ 25 % (distorsionan más). Firma: C→T y CC→TT |
| **Radiación ionizante** | **Roturas de doble cadena** (y SSB, bases oxidadas), a menudo agrupadas | ➕ Actúa de forma directa y mediante radicales hidroxilo del agua. Del orden de ~1.000 SSB y ~20–40 DSB por célula y por Gy |
| **Tabaco: benzo[a]pireno** | Se activa a **diol-epóxido (BPDE)** → **aductos voluminosos en guanina** | ➕ Transversiones G→T (C>A) en TP53 en el cáncer de pulmón |
| **Aflatoxina B1** (*Aspergillus*; maní y maíz mal almacenados) | Activada por citocromo P450 → **aductos en N7 de guanina** | Mutación **TP53 R249S** (G→T en el codón 249) en el **carcinoma hepatocelular**. ➕ Sinergia con hepatitis B |
| **Quimioterapia** | Cisplatino (aductos intracatenarios y enlaces cruzados), alquilantes (bases metiladas), inhibidores de topoisomerasa (roturas) | Ver sección 5.10.3 |

#### 5.2.3 Catálogo visual de lesiones *(Diap. 6)*

| Grupo | Lesión | Ejemplo de causa | Vía |
|---|---|---|---|
| **Bases** | Sitio AP (sin base) | Depurinación, glicosilasas | BER |
| | 8-oxoG | ROS | BER (OGG1/MUTYH) |
| | Apareamiento erróneo | Error de la polimerasa | MMR |
| | Uracilo | Desaminación de C | BER (UNG) |
| | Dímero de pirimidina | UV | NER |
| | Aducto voluminoso | Benzo[a]pireno, cisplatino | NER |
| **Esqueleto y entre cadenas** | Rotura de cadena sencilla (SSB) | ROS, intermediarios de BER | PARP1 + BER/SSBR |
| | Enlace cruzado intercatenario (ICL) | Cisplatino, mitomicina C, aldehídos | Fanconi + NER + TLS + HR |
| | Rotura de doble cadena (DSB) | Radiación ionizante, horquillas colapsadas | NHEJ / HR |
| | Enlace cruzado ADN–proteína | Aldehídos, topoisomerasas atrapadas | Proteólisis + reparación |

📌 Un **ICL** une covalentemente las dos hebras: impide separarlas, y por tanto bloquea la replicación y la transcripción. Es una de las lesiones más tóxicas que existen.

#### 5.2.4 Destinos de una lesión

```
                      ┌─► Reparada correctamente ─────────► célula sana
                      │
LESIÓN ──► DDR ───────┼─► Tolerada (TLS) ─────────────────► sobrevive, a veces con mutación
                      │
                      ├─► Mal reparada / replicada ───────► MUTACIÓN (cáncer si afecta genes clave)
                      │
                      └─► Daño excesivo ──────────────────► apoptosis o senescencia
```

#### 5.2.5 La respuesta al daño del ADN (DDR) *(Diap. 7)*

La DDR es una **cascada de señales** con la lógica de cualquier vía de transducción:

```
DAÑO ──► SENSORES ──► TRANSDUCTORES (cinasas) ──► EFECTORES ──► RESULTADO
```

| Daño | Sensor | Transductor (cinasa) | Efectores principales |
|---|---|---|---|
| **DSB** | **MRN** (MRE11–RAD50–NBS1) | **ATM** | CHK2, p53, γH2AX, BRCA1, 53BP1 |
| **ADN monocatenario** (horquillas detenidas, resección) | **RPA–ATRIP** | **ATR** | CHK1 |
| **Extremos de DSB para NHEJ** | **Ku70/80** | **DNA-PKcs** | Reparación por NHEJ |
| **SSB** | **PARP1** | (PARilación, no es una cinasa PIKK) | XRCC1 y BER |

🧠 **ATR ↔ RPA**, las dos llevan R (y R de estrés **R**eplicativo). **ATM ↔ MRN**, las dos llevan M. Y para los efectores: la **M** tiene dos jorobas → **CHK2**; la **R** tiene un solo bucle → **CHK1**.

**Resultados de la DDR:**

1. **Arresto del ciclo celular** en los puntos de control G1/S, intra-S y G2/M, para dar tiempo a reparar.
2. **Reparación del ADN**: activación de la vía específica.
3. **Apoptosis**, si el daño es excesivo.
4. **Senescencia**: arresto permanente.

➕ **Detalles que conviene saber:**

- **ATM, ATR y DNA-PKcs** pertenecen a la familia **PIKK** (cinasas relacionadas con la PI3K) y fosforilan motivos Ser/Thr seguidos de Gln.
- **γH2AX** es la histona H2AX fosforilada en la Ser139 alrededor de una DSB. Se extiende a lo largo de megabases y sirve de plataforma (MDC1 → RNF8/RNF168 → 53BP1 y BRCA1). En el laboratorio, los "focos de γH2AX" se usan como marcador de DSB.
- **p53**, "guardián del genoma": en reposo, MDM2 la ubiquitina y se degrada. Tras el daño, ATM/ATR y CHK2/CHK1 la fosforilan, MDM2 ya no la une y p53 se acumula y activa genes como **p21 (CDKN1A)**, que inhibe CDK2–ciclina E y frena en G1/S, o **PUMA, NOXA y BAX**, que inducen apoptosis. TP53 es el gen más mutado en el cáncer humano.
- **ATR es esencial**: responde al estrés replicativo de cada fase S, y su pérdida total es letal. Las mutaciones hipomorfas causan el **síndrome de Seckel** (microcefalia y enanismo). ATM, en cambio, no es esencial (los pacientes con A-T viven).

🩺 **Correlaciones:**

- **TP53 germinal mutado → síndrome de Li-Fraumeni** (autosómico dominante). ➕ Sarcomas, cáncer de mama precoz, tumores cerebrales, carcinoma adrenocortical y leucemias. Se evita la radiación cuando es posible, porque favorece segundos tumores.
- **ATM mutado → ataxia-telangiectasia** (sección 5.7.8).

#### 5.2.6 Mapa general: cada lesión tiene su vía *(Diap. 8)*

📌 La tabla más importante de la clase:

| Lesión | Vía | Proteínas clave |
|---|---|---|
| O⁶-metilguanina, alquilaciones simples | **Reversión directa** | MGMT, ALKBH2/3 |
| Bases pequeñas dañadas, sitios AP, SSB | **BER** | Glicosilasas, APE1, Pol β, XRCC1, PARP1 |
| Lesiones voluminosas que distorsionan la hélice | **NER** | XPC, TFIIH (XPB/XPD), XPA, XPF–ERCC1, XPG |
| Apareamientos erróneos, pequeñas inserciones/deleciones | **MMR** | MSH2–MSH6, MSH2–MSH3, MLH1–PMS2 |
| Roturas de doble cadena | **NHEJ / HR** | Ku, DNA-PKcs, LIG4 / MRN, BRCA1/2, RAD51 |
| Enlaces cruzados intercatenarios | **Fanconi (FA)** | FANCD2–FANCI + NER + TLS + HR |
| Lesiones no reparadas al replicar | **Tolerancia (TLS)** | PCNA-Ub, Pol η, Pol ζ, REV1 |

🧠 Regla rápida *(Diap. 48)*: **pequeña → BER · voluminosa → NER · error de copia → MMR · rotura doble → NHEJ o HR**.

#### 5.2.7 Nobel de Química 2015 *(Diap. 9)*

Premio "por estudios mecanísticos de la reparación del ADN":

| Premiado | Vía | Aporte |
|---|---|---|
| **Tomas Lindahl** (Reino Unido/Suecia) | **BER** | Demostró que el ADN se degrada espontáneamente y descubrió las ADN-glicosilasas |
| **Aziz Sancar** (EE. UU./Turquía) | **NER** | Describió cómo se cortan y reemplazan segmentos dañados por UV; estudió la fotoliasa |
| **Paul Modrich** (EE. UU.) | **MMR** | Mostró cómo se corrigen los errores de apareamiento tras la replicación |

---

### 5.3 Reversión directa del daño

> Una enzima, un paso, sin cortar el esqueleto del ADN *(Diap. 10)*.

La reversión directa no retira bases ni sintetiza ADN: deshace químicamente la lesión en su sitio.

#### 5.3.1 MGMT: la enzima "suicida" *(Diap. 11)*

**MGMT** = O⁶-metilguanina-ADN metiltransferasa.

```
   G–CH₃ (O⁶-meG)                                   G  (guanina restaurada)
     :                MGMT-Cys145–SH                 :
     T   ← se aparea  ─────────────────►             C
         con T               │
                             ▼
                    MGMT-Cys145–S–CH₃  → inactivada → ubiquitinada → degradada
                    (1 molécula = 1 lesión)
```

- La **O⁶-metilguanina** se aparea con **T** en lugar de C → **transición G:C→A:T** tras dos rondas de replicación.
- MGMT transfiere el metilo a su **cisteína 145** del sitio activo. La enzima queda metilada de forma irreversible, se inactiva y se degrada.
- 📌 Es **estequiométrica, no catalítica**: **cada molécula repara una sola lesión**. La capacidad de reparación depende de cuánta proteína haya. Si se agota (dosis altas de alquilantes) o no se produce (promotor silenciado), la O⁶-meG persiste.

#### 5.3.2 Otras enzimas de reversión directa *(Diap. 11)*

| Enzima | Qué revierte | Cómo | Dato clave |
|---|---|---|---|
| **Fotoliasa** | Dímeros de pirimidina (CPD) | Usa **luz visible** (fotorreactivación; cofactor FAD) | Existe en bacterias, plantas y muchos animales; **ausente en los mamíferos placentarios** → los humanos dependemos de **NER** para los dímeros UV |
| **ALKBH2 / ALKBH3** | **1-metiladenina y 3-metilcitosina** | **Desmetilación oxidativa**; dioxigenasas dependientes de **Fe²⁺ y α-cetoglutarato** | Homólogas de AlkB bacteriana |

#### 5.3.3 ➕ ¿Por qué la O⁶-meG mata a la célula? El papel de MMR

Esta conexión entre vías explica la clínica de la temozolomida:

1. Al replicar, frente a la O⁶-meG se inserta **T**.
2. **MMR** reconoce el par O⁶-meG:T como un error y retira la T de la hebra nueva.
3. Pero la O⁶-meG sigue en el molde, así que se vuelve a insertar T… y MMR vuelve a cortar. Son **ciclos fútiles de reparación**.
4. Los huecos de ADN monocatenario persistentes se convierten en **DSB** en la siguiente fase S → **apoptosis**.

Consecuencias:

- Un tumor **sin MMR** es **tolerante (resistente) a la temozolomida**: deja la O⁶-meG:T sin tocar, sobrevive y acumula mutaciones C→T.
- 🩺 Los gliomas que recaen tras temozolomida pueden volverse **hipermutados** (firma SBS11), a menudo por mutaciones en **MSH6**.

#### 5.3.4 🩺💊 Ejemplo real: MGMT y la temozolomida en glioblastoma *(Diap. 12)*

- **El fármaco**: la **temozolomida (TMZ)** es un **alquilante oral** que genera O⁶-metilguanina (además de N7-meG y N3-meA, más abundantes pero menos importantes para su efecto). ➕ Es un profármaco que atraviesa la barrera hematoencefálica.
- **El biomarcador**: si el **promotor de MGMT está metilado** (silenciado epigenéticamente), el tumor no produce MGMT y no puede reparar la lesión.
- **La consecuencia**: los pacientes con MGMT silenciado obtienen el **mayor beneficio** de la TMZ.

**Supervivencia mediana (meses), Hegi et al., NEJM 2005:**

| Promotor de MGMT | Radioterapia sola | Radioterapia + TMZ | Beneficio |
|---|---|---|---|
| **Metilado** (silenciado) | 15,3 | **21,7** | +6,4 meses |
| **No metilado** | 11,8 | 12,7 | +0,9 meses |

⚠️ No confundas las dos "metilaciones":
- La **metilación del promotor de MGMT** (citosinas en islas CpG) es **epigenética** y apaga el gen. Es buena noticia para el paciente.
- La **metilación de la guanina** (O⁶-meG) es la **lesión** que causa la TMZ.

➕ MGMT también confiere resistencia a las **nitrosoureas** (carmustina, lomustina): retira el aducto O⁶-cloroetilguanina antes de que evolucione a un **enlace cruzado intercatenario** G–C.

---

### 5.4 Reparación por escisión de bases (BER)

> Para lesiones **pequeñas que no distorsionan la doble hélice** *(Diap. 13)*: bases oxidadas, desaminadas o alquiladas, sitios AP y roturas de cadena sencilla.

#### 5.4.1 Empieza con una ADN-glicosilasa específica *(Diap. 14)*

- La glicosilasa recorre el ADN, **"voltea" la base dañada fuera de la hélice** (*base flipping*) hacia su bolsillo catalítico y **rompe el enlace N-glicosídico**.
- **Monofuncionales**: solo retiran la base (p. ej., **UNG**). Dejan un sitio AP que corta APE1.
- **Bifuncionales**: retiran la base **y** cortan el esqueleto con su actividad **AP-liasa** (p. ej., **OGG1**, NTHL1, NEIL1–3).
- Hay **~11 glicosilasas humanas**. 📌 **La especificidad está en el primer paso**; el resto de la vía es común.

| Glicosilasa | Sustrato | Comentario |
|---|---|---|
| **UNG** | **Uracilo** en el ADN | Monofuncional; imprescindible para el cambio de isotipo |
| **OGG1** | **8-oxoG opuesta a C** | Bifuncional |
| **MUTYH** | **Adenina opuesta a 8-oxoG** | ⚠️ Retira una base **normal** (A) mal colocada, no la 8-oxoG |
| **MPG (AAG)** | **3-metiladenina, 7-metilG, hipoxantina** | Hipoxantina = desaminación de A |
| **TDG** | **T frente a G** (desaminación de 5-metilC) | También participa en la desmetilación activa del ADN |
| **NTHL1 / NEIL1–3** | **Pirimidinas oxidadas** | Bifuncionales |

#### 5.4.2 BER paso a paso: parche corto *(Diap. 15)*

```
1 RECONOCIMIENTO   2 SITIO AP        3 INCISIÓN         4 SÍNTESIS             5 LIGACIÓN
  Glicosilasa  ──►  azúcar sin  ──►   APE1 corta    ──►  Pol β inserta 1 nt ──► XRCC1–LIG3α
  retira la base    base             en 5′ del AP       y retira el dRP         sella la mella
```

1. **Glicosilasa**: retira la base dañada.
2. **Sitio AP**: queda el azúcar sin base.
3. **APE1** (AP-endonucleasa 1) corta el esqueleto **en 5′ del sitio AP**: deja un **3′-OH** utilizable y un residuo **5′-desoxirribosa-fosfato (dRP)**.
4. **Pol β** inserta **1 nucleótido** (actividad polimerasa) y **retira el dRP** (actividad **dRP-liasa**).
5. **XRCC1–LIG3α** sella la mella. XRCC1 es el andamio que coordina Pol β y LIG3.

🧠 **"Glicosilasa → APE → β → Ligasa"**: *"Gloria Aprende Bien a Leer"* (G-A-B-L).

#### 5.4.3 Parche corto frente a parche largo *(Diap. 16)*

| | **Parche corto (vía predominante)** | **Parche largo** |
|---|---|---|
| Nucleótidos reemplazados | **1** | **2–12** |
| Cuándo | El extremo 5′ puede procesarse (Pol β retira el dRP) | El extremo 5′ está **modificado** y Pol β no puede retirarlo |
| Polimerasa | **Pol β** | **Pol δ/ε** con **PCNA** (desplaza la hebra y forma un **colgajo**) |
| Nucleasa | — | **FEN1** corta el colgajo (*flap*) |
| Ligasa | **XRCC1–LIG3α** | **LIG1** |

#### 5.4.4 PARP1: la "alarma" de las roturas de cadena sencilla *(Diap. 16)*

- **PARP1** detecta la mella y, usando **NAD⁺** como sustrato, sintetiza cadenas de **poli(ADP-ribosa) (PAR)** sobre sí misma y sobre histonas.
- Las cadenas de PAR, cargadas negativamente, **reclutan a XRCC1** (y con él a Pol β y LIG3) para completar la reparación.
- ➕ La **autoPARilación** hace que PARP1 se **suelte** del ADN cuando termina su trabajo.
- 📌 Si PARP1 se inhibe y queda **"atrapada"** en el ADN, la SSB no se repara. Cuando llega la horquilla de replicación, la SSB se convierte en una **rotura de doble cadena**, que solo puede repararse con fidelidad por **recombinación homóloga**. Es la base de los inhibidores de PARP (sección 5.10.1).

#### 5.4.5 🩺 Ejemplo real: el "sistema GO" y la poliposis asociada a MUTYH *(Diap. 17)*

```
  8-oxoG : C   ──replicación──►   8-oxoG : A   ──replicación──►    T : A
  (lesión oxidativa)              (error al replicar)               (mutación fija G:C→T:A)
      ▲                                ▲                         ▲
     OGG1                            MUTYH                      MTH1 (NUDT1)
  retira 8-oxoG                  retira la A frente           limpia 8-oxo-dGTP del
  opuesta a C                    a 8-oxoG                     pool de nucleótidos
```

📌 **Tres guardianes** evitan que la oxidación de la guanina se convierta en una **transversión permanente G:C→T:A**:

- **OGG1**: retira la 8-oxoG cuando todavía está frente a C.
- **MUTYH**: si ya se replicó y quedó 8-oxoG:A, retira la **A** y le da a la célula otra oportunidad de poner C (y que luego actúe OGG1).
- **MTH1**: hidroliza el **8-oxo-dGTP** del pool de nucleótidos para que no se incorpore.

**Caso clínico (Al-Tassan et al., Nat Genet 2002):** una familia británica con **tres hermanos** con adenomas múltiples y cáncer colorrectal, **sin mutación germinal en APC**. Sus tumores mostraban un **exceso de transversiones G:C→T:A en APC**: la firma del sistema GO roto. Causa: **variantes bialélicas en MUTYH (Y179C y G396D)**.

**Poliposis asociada a MUTYH (MAP)**:
- Herencia **autosómica recesiva**: hermanos afectados, padres sanos (portadores).
- Decenas a cientos de adenomas y riesgo alto de cáncer colorrectal.
- ➕ Diagnóstico diferencial con la **poliposis adenomatosa familiar (FAP)**: gen *APC*, herencia **dominante** (suele haber un progenitor afectado).
- ➕ Otra poliposis por BER: variantes bialélicas de **NTHL1** (también recesiva).

#### 5.4.6 🩺 Ejemplo real: el sistema inmune usa BER (deficiencia de UNG) *(Diap. 18)*

**Cambio de isotipo (CSR) en el linfocito B:**

```
AID ──────────────► UNG ───────────► APE1 ───────────────► NHEJ
desamina C→U        retira el U      corta → roturas en     une las regiones de cambio
(programado) en     → sitio AP       las regiones de        → IgG, IgA, IgE
genes de Ig                          cambio (DSB)
```

📌 **Idea clave**: las vías de reparación no solo corrigen accidentes. El linfocito B **daña su propio ADN a propósito** (AID) y recluta BER y NHEJ para diversificar sus anticuerpos.

**Deficiencia de UNG (hiper-IgM tipo 5)** (Imai et al., Nat Immunol 2003):
- Autosómica recesiva.
- **IgM normal o alta; IgG, IgA e IgE muy bajas.**
- Infecciones bacterianas recurrentes y linfadenopatía.
- Falla el cambio de isotipo; la hipermutación somática queda sesgada.

➕ **Diagnóstico diferencial de los síndromes de hiper-IgM:**

| Tipo | Gen | Herencia | Pista |
|---|---|---|---|
| HIGM1 (el más frecuente) | **CD40LG** (CD40 ligando, linfocito T) | **Ligada al X** | Infecciones oportunistas (*Pneumocystis*, *Cryptosporidium*) por falla de la ayuda T |
| HIGM2 | **AICDA** (AID) | AR | Defecto intrínseco del linfocito B; linfadenopatía; sin oportunistas |
| HIGM3 | **CD40** | AR | Como HIGM1 |
| HIGM5 | **UNG** | AR | Como HIGM2 |

---

### 5.5 Reparación por escisión de nucleótidos (NER)

> Para lesiones **voluminosas que distorsionan la doble hélice** *(Diap. 19)*.

#### 5.5.1 ¿Qué repara NER? *(Diap. 20)*

| Lesión | Origen | Comentario |
|---|---|---|
| **Dímeros de pirimidina ciclobutano (CPD)** | UV-B | Enlace covalente entre pirimidinas adyacentes (típicamente T–T) que forma un **anillo de ciclobutano**; distorsionan poco |
| **Fotoproductos 6-4** | UV-B | Más distorsionantes que los CPD |
| **Aductos del tabaco** | Benzo[a]pireno diol-epóxido unido a guanina | |
| **Aductos de cisplatino** | Intracatenarios 1,2-d(GpG) | Ver 5.7 |
| **Aductos de aflatoxina B1** | En N7 de guanina | |

📌 **Firma mutacional de la UV**: **transiciones C→T y CC→TT en sitios de dipirimidina**, típicas del **melanoma** y de los **carcinomas cutáneos**.

#### 5.5.2 Dos formas de detectar la lesión: GG-NER y TC-NER *(Diap. 21)*

| | **NER global del genoma (GG-NER)** | **NER acoplada a la transcripción (TC-NER)** |
|---|---|---|
| Dónde actúa | En **todo el genoma**, ambas hebras, se transcriba o no | Solo en la **hebra molde de genes activos** |
| Quién detecta | **XPC–RAD23B** detecta la distorsión; **UV-DDB** (DDB1–DDB2; **DDB2 = XPE**) ayuda a encontrar los **CPD**, que distorsionan poco | La **ARN Pol II detenida** ante la lesión recluta **CSB (ERCC6)**, **CSA (ERCC8)** y **UVSSA** |
| Qué protege sobre todo | Frente a **mutaciones** (cáncer) | La **transcripción** y la supervivencia celular (neuronas, envejecimiento) |
| Enfermedad típica | **Xeroderma pigmentoso** | **Síndrome de Cockayne** |

Las dos subvías **convergen en TFIIH**, y a partir de ahí la vía es común.

#### 5.5.3 NER paso a paso *(Diap. 22)*

```
1 RECONOCIMIENTO      2 APERTURA            3 DOBLE INCISIÓN          4 ESCISIÓN           5 SÍNTESIS Y LIGACIÓN
XPC–RAD23B       ──►  TFIIH (XPB, XPD)  ──►  XPF–ERCC1 corta en 5′ ──► sale un oligo   ──►  Pol δ/ε/κ + PCNA rellenan;
(o Pol II + CSB)      abre ~30 nt;           XPG corta en 3′           de 24–32 nt          LIG1 o XRCC1–LIG3 sellan
                      XPA y RPA verifican                              con la lesión
```

1. **Reconocimiento**: XPC (GG-NER) o la Pol II detenida + CSB (TC-NER) detectan la distorsión.
2. **Apertura**: **TFIIH**, con sus helicasas **XPB (ERCC3)** y **XPD (ERCC2)**, abre una burbuja de **~30 nt**. **XPA** y **RPA** verifican la lesión y posicionan las nucleasas (RPA protege la hebra sana).
3. **Doble incisión**: **XPF–ERCC1** corta en **5′** y **XPG** corta en **3′** de la lesión.
4. **Escisión**: se libera un **oligonucleótido de 24–32 nt** que contiene la lesión.
5. **Síntesis y ligación**: **Pol δ/ε/κ** con **PCNA** rellenan el hueco usando la hebra sana como molde; **LIG1** o **XRCC1–LIG3** sellan.

🧠 **¿Quién corta dónde?** F va antes que G en el alfabeto, y 5′ va antes que 3′ en la hebra: **XPF corta en 5′, XPG corta en 3′**.

⚠️ **BER frente a NER**: BER retira **una base** (glicosilasa) y reemplaza 1 nt (o 2–12); NER retira **un fragmento** de 24–32 nt con dos cortes. BER reconoce la **química** de una base concreta; NER reconoce la **distorsión** de la hélice, así que repara lesiones muy diferentes.

➕ **TFIIH tiene doble función**: es un factor general de transcripción de la ARN Pol II (abre el promotor) y es la helicasa de NER. Por eso algunas mutaciones de XPD o XPB alteran además la transcripción (tricotiodistrofia).

#### 5.5.4 🩺 Ejemplo real: xeroderma pigmentoso (XP) *(Diap. 23)*

**Cifras (cohorte del NIH, 106 pacientes; Bradford et al. 2011):**

| Dato | Valor |
|---|---|
| Riesgo de cáncer de piel **no melanoma** antes de los 20 años | **~10.000 veces** mayor |
| Riesgo de **melanoma** antes de los 20 años | **~2.000 veces** mayor |
| Edad mediana del primer cáncer de piel no melanoma | **9 años** |
| Pacientes con **neurodegeneración progresiva** | **~24 %** |

**Clínica:**
- **Autosómico recesivo**; más frecuente con **consanguinidad**.
- **Quemadura solar grave o pecas precoces antes de los 2 años**, en zonas expuestas.
  - ➕ Alrededor de la mitad (sobre todo XPA, XPB, XPD, XPF, XPG) tiene quemaduras exageradas con exposición mínima. Los pacientes XPC, XPE y XPV suelen quemarse de forma normal, pero desarrollan pecas precoces y cáncer.
- **Lesiones oculares**: fotofobia, queratitis, cáncer conjuntival.
- **Manejo**: **fotoprotección estricta** y **vigilancia dermatológica, oftalmológica y neurológica**.
  - ➕ Extirpación precoz de lesiones, suplemento de vitamina D (por la evitación solar), retinoides orales como quimioprevención en pacientes con muchos tumores y consejo genético (cada hermano tiene un 25 % de riesgo).

**Grupos de complementación y genes:**

| Grupo | Gen | Función |
|---|---|---|
| **XPA** | XPA | Verificación de la lesión; organiza el complejo |
| **XPB** | ERCC3 | Helicasa/translocasa de TFIIH |
| **XPC** | XPC | Sensor de GG-NER |
| **XPD** | ERCC2 | Helicasa de TFIIH |
| **XPE** | DDB2 | UV-DDB: detecta CPD en GG-NER |
| **XPF** | ERCC4 | Nucleasa 5′ (con ERCC1) |
| **XPG** | ERCC5 | Nucleasa 3′ |
| **XPV** (variante) | **POLH** (Pol η) | **No es NER**: síntesis translesión (sección 5.9) |

➕ **Epidemiología**: XP es rara (del orden de 1 por millón en EE. UU. y Europa) y bastante más frecuente en Japón, donde predomina **XPA**. En EE. UU., Europa y el norte de África predomina **XPC**. La neurodegeneración aparece sobre todo en **XPA** y **XPD** (también en algunos XPB, XPF y XPG). XPC, XPE y XPV no suelen tenerla.

🧠 **ERCC y XP**: *"4-F, 5-G"* van seguidos, como en el alfabeto (ERCC4 = XPF, ERCC5 = XPG). *"2-D y 3-B"* van cruzados (ERCC2 = XPD, ERCC3 = XPB). *"6 y 8 son de Cockayne"* (ERCC6 = CSB, ERCC8 = CSA).

#### 5.5.5 Mismos genes, distintas enfermedades: XP, Cockayne y TTD *(Diap. 24)*

| Rasgo | **Xeroderma pigmentoso** | **Síndrome de Cockayne** | **Tricotiodistrofia (TTD)** |
|---|---|---|---|
| Fotosensibilidad | Sí | Sí | En ~la mitad |
| **Cáncer de piel** | **Muy aumentado** | **No aumentado** | **No aumentado** |
| Neurología | Pérdida neuronal (~24 %) | Desmielinización, microcefalia | Retraso del desarrollo |
| Crecimiento | Normal | Talla baja, aspecto envejecido | Talla baja |
| Cabello | Normal | Normal | **Quebradizo, pobre en azufre** |
| Defecto principal | GG-NER (± TC-NER) | **TC-NER** | **TFIIH**: NER + transcripción |
| Genes | XPA–XPG, POLH | **ERCC6 (CSB)**, **ERCC8 (CSA)** | **ERCC2 (XPD)**, ERCC3, GTF2H5 |

📌 **Lección**: el **cáncer** se asocia a la falla de la reparación **global**; la **neurodegeneración y el envejecimiento**, a la falla de la reparación **acoplada a la transcripción**.

**¿Por qué Cockayne no da cáncer?** En Cockayne, **GG-NER funciona**, así que la mayor parte del genoma se repara y no se acumulan mutaciones. Lo que falla es la recuperación de la transcripción: la Pol II queda bloqueada y la célula **muere** (apoptosis) en lugar de mutar. Las neuronas, que no se dividen y transcriben mucho, son las más afectadas.

➕ **Más rasgos útiles:**
- **Cockayne**: "enanismo caquéctico", ojos hundidos, cataratas, retinopatía pigmentaria, hipoacusia neurosensorial, calcificaciones intracraneales. Aproximadamente dos tercios de los casos se deben a **CSB (ERCC6)** y un tercio a **CSA (ERCC8)**.
- **TTD**: acrónimo **PIBIDS**: *Photosensitivity, Ichthyosis, Brittle hair, Intellectual impairment, Decreased fertility, Short stature*. El pelo muestra un patrón en "cola de tigre" con luz polarizada.
- **Un mismo gen, tres enfermedades**: según dónde caiga la mutación, **ERCC2 (XPD)** puede causar XP (falla la helicasa → cáncer), TTD (se desestabiliza TFIIH → transcripción) o un cuadro combinado XP/Cockayne.

#### 5.5.6 🩺💊 Ejemplo real: cisplatino, cuando la reparación es el enemigo *(Diap. 25)*

| Lesión del cisplatino | Frecuencia | Vía que la repara |
|---|---|---|
| **Intracatenaria 1,2** (sobre todo d(GpG)) | **~90 %** de los aductos | **NER** |
| **Intercatenaria (ICL)** | Rara, pero **muy tóxica** | **Fanconi + HR** |

➕ Dentro del ~90 % intracatenario, alrededor de dos tercios son 1,2-d(GpG) y el resto sobre todo 1,2-d(ApG). Los ICL son menos del 5 %.

- Las lesiones **bloquean replicación y transcripción → apoptosis**.
- 📌 **Cuanto mejor repare el tumor, más resistente será.**
- **Tumores de células germinales de testículo**: se curan en la gran mayoría de los casos con quimioterapia basada en cisplatino, incluso cuando hay metástasis. Parte de esta sensibilidad se ha atribuido a **niveles bajos de XPA** y menor capacidad de NER (Köberle et al. 1999).
- **ERCC1 en cáncer de pulmón**: los tumores con ERCC1 bajo parecían beneficiarse más del cisplatino adyuvante (Olaussen et al. 2006), pero la validación posterior fue inconsistente y **no se usa de rutina**.

➕ **Otros mecanismos de resistencia al cisplatino**: menor captación, más eflujo, inactivación por glutatión, síntesis translesión que "salta" el aducto, pérdida de MMR (tolerancia) y restauración de la HR (mutaciones de reversión de BRCA). Al revés, los tumores con **HR deficiente** (BRCA) son especialmente **sensibles al platino**.

---

### 5.6 Reparación de apareamientos erróneos (MMR)

> El corrector de pruebas posreplicativo *(Diap. 26)*.

#### 5.6.1 Tres filtros de fidelidad en la replicación *(Diap. 27)*

```
Selección de bases por la polimerasa ............ 1 error en 10⁴–10⁵
 + corrección exonucleasa 3′→5′ (proofreading) ... 1 error en 10⁶–10⁷
 + reparación de apareamientos (MMR) ............. 1 error en 10⁹–10¹⁰
```

📌 MMR aumenta la fidelidad unas **100–1.000 veces** (valores aproximados; Jiricny 2006).

**¿Qué reconoce MMR?**
- **Bases mal apareadas** (p. ej., G:T) que escaparon a la corrección de pruebas.
- **Bucles de inserción/deleción** por **deslizamiento** de la polimerasa en secuencias repetidas (**microsatélites**).

**¿Cómo sabe cuál de las dos bases es la errónea?** Debe distinguir la **hebra nueva** (que contiene el error) de la **parental**. En eucariotas usa las **mellas** de la hebra nueva (extremos de los fragmentos de Okazaki en la hebra rezagada) y la **orientación de PCNA**, que se carga con una polaridad definida.

➕ En *E. coli* la señal es distinta y es clásica de examen: la hebra parental está **metilada en las secuencias GATC** (metilasa Dam) y la nueva todavía no (ADN **hemimetilado**). MutH corta la hebra no metilada, es decir, la nueva.

#### 5.6.2 MMR paso a paso *(Diap. 28)*

```
1 RECONOCIMIENTO             2 CORTE EN HEBRA NUEVA        3 ESCISIÓN                 4 RESÍNTESIS
MutSα (MSH2–MSH6)       ──►  MutLα (MLH1–PMS2),       ──►  EXO1 degrada la hebra ──► Pol δ copia de nuevo
detecta el error;            activada por PCNA,             nueva hasta pasar el       y LIG1 sella
MutSβ (MSH2–MSH3)            corta la hebra nueva           error; RPA protege
bucles grandes
```

| Complejo | Composición | Función |
|---|---|---|
| **MutSα** | **MSH2–MSH6** | Reconoce desapareamientos de bases y bucles de 1–2 nt (la mayoría de los errores) |
| **MutSβ** | **MSH2–MSH3** | Reconoce **bucles de inserción/deleción más grandes** |
| **MutLα** | **MLH1–PMS2** | Activada por PCNA; **PMS2 tiene la actividad endonucleasa** que corta la hebra nueva |
| **EXO1** | — | Exonucleasa 5′→3′ que retira el tramo con el error |
| **RPA** | — | Protege el ADN monocatenario expuesto |
| **Pol δ + LIG1** | — | Resíntesis y sellado |

🧠 **MutS "Sensa"** (reconoce) y **MutL "Lanza el corte"** (PMS2 corta). **MSH2 es el socio común** de MSH6 y MSH3; **MLH1** va con PMS2.

#### 5.6.3 Inestabilidad de microsatélites (MSI): la huella de un MMR defectuoso *(Diap. 29)*

```
Microsatélite normal:   CA CA CA CA CA CA CA CA CA CA      (10 repeticiones)

Deslizamiento:          CA CA CA CA ┌CA┐ CA CA CA CA CA   ← bucle de 1 repetición no reparado
                                    └──┘
Sin MMR, la siguiente replicación fija un alelo con 9 u 11 repeticiones.
```

- Un **microsatélite** es una repetición en tándem de 1–6 pb, como (CA)n o (A)n. La polimerasa "resbala" con facilidad en ellos.
- Sin MMR, cada ronda de replicación cambia su longitud: el tumor muestra **alelos nuevos** (tumor **MSI-H**, inestabilidad alta).
- 📌 **Genes con repeticiones en su región codificante**: **TGFBR2 (A10)**, **ACVR2A** y **BAX (G8)**. Las inserciones o deleciones **cambian el marco de lectura** e inactivan supresores de tumores (o, en el caso de BAX, un gen proapoptótico).

**Diagnóstico de la deficiencia de MMR (dMMR):**

| Prueba | Qué mide | Resultado anormal |
|---|---|---|
| **PCR de microsatélites** (análisis de fragmentos) | Longitud de un panel de microsatélites, tumor frente a tejido normal | **MSI-H**. ➕ Paneles: Bethesda (BAT-25, BAT-26, D2S123, D5S346, D17S250) o pentaplex de mononucleótidos (BAT-25, BAT-26, NR-21, NR-24, MONO-27); MSI-H si hay ≥2 marcadores inestables. También se puede medir por NGS |
| **Inmunohistoquímica (IHQ)** para MLH1, MSH2, MSH6 y PMS2 | Presencia de cada proteína en los núcleos tumorales | **Pérdida de expresión = dMMR** |

#### 5.6.4 ➕ Cómo leer la inmunohistoquímica de MMR

Las proteínas MMR funcionan en **heterodímeros**, y cada pareja tiene un socio **"obligado"**: **MSH2** estabiliza a MSH6 y **MLH1** estabiliza a PMS2. Si falta el socio obligado, el otro se degrada. El socio "secundario" no es imprescindible para el obligado, porque MSH2 también se une a MSH3 y MLH1 a PMS1 o MLH3.

| Patrón de pérdida en IHQ | Gen sospechoso | Siguiente paso |
|---|---|---|
| **MLH1 + PMS2** | **MLH1** | Estudiar **BRAF V600E** e **hipermetilación del promotor de MLH1**. Si son positivos → tumor **esporádico** (no Lynch). Si son negativos → estudio germinal |
| **MSH2 + MSH6** | **MSH2** o **deleción de EPCAM** | Estudio germinal |
| **Solo MSH6** | **MSH6** | Estudio germinal |
| **Solo PMS2** | **PMS2** | Estudio germinal |

⚠️ **Pérdida de MLH1 no equivale a Lynch.** Alrededor del 15 % de los cánceres colorrectales son MSI-H, pero solo ~3 % son Lynch. La mayor parte del resto son **esporádicos**, por **hipermetilación del promotor de MLH1** (asociada a BRAF V600E, colon derecho y mujeres mayores).

➕ **EPCAM**: es el gen situado justo antes de MSH2. Las deleciones de su extremo 3′ eliminan la señal de terminación, la transcripción "se lee de corrido" hacia MSH2 y **metila (silencia) el promotor de MSH2** en los tejidos que expresan EPCAM (epitelios).

#### 5.6.5 🩺 Ejemplo real: síndrome de Lynch (CCR hereditario no polipósico) *(Diap. 30)*

**Genética:**
- **Autosómico dominante**.
- Genes: **MLH1, MSH2 (o deleción de EPCAM), MSH6, PMS2**.
- El tumor aparece cuando la célula pierde el segundo alelo y se vuelve dMMR/MSI-H.

**Cifras:**

| Dato | Valor en la clase | ➕ Matiz |
|---|---|---|
| Fracción de todos los CCR | **~3 %** | La forma hereditaria más frecuente de CCR |
| Riesgo de CCR de por vida | **Hasta ~80 %** (estimación clásica, MLH1/MSH2) | Las series prospectivas modernas dan cifras menores, que dependen del gen: a los 75 años, ~46 % (MLH1), ~43 % (MSH2), ~15 % (MSH6) y ~10 % (PMS2) (PLSD; Møller et al. 2018) |
| Riesgo de cáncer de endometrio en portadoras | **40–60 %** | Para MSH6 es alto (~46 %) aunque su riesgo colorrectal sea bajo |

**Espectro tumoral:** colon (sobre todo derecho) y endometrio, además de **ovario, estómago, intestino delgado, vías urinarias (urotelio alto) y páncreas**.

**Criterios de Ámsterdam II ("3-2-1"):**
- **≥3** familiares con cáncer asociado a Lynch (uno de ellos familiar de primer grado de los otros dos),
- en **≥2** generaciones sucesivas,
- **≥1** diagnosticado antes de los **50** años,
- ➕ excluida la FAP y con diagnóstico confirmado por patología.

⚠️ Ámsterdam II es **específico pero poco sensible**: deja escapar muchos casos. Por eso hoy se recomienda **tamizaje universal (IHQ o MSI) de todo CCR y de todo cáncer de endometrio**.

**Seguimiento y prevención de los portadores:**
- **Colonoscopia cada 1–2 años** (➕ desde los 20–25 años para MLH1/MSH2; más tarde para MSH6/PMS2).
- ➕ Considerar **histerectomía y salpingooforectomía** reductoras de riesgo al terminar la paridad.
- ➕ La **aspirina** reduce la incidencia de CCR en portadores (ensayo CAPP2).
- ➕ **Estudio en cascada** de los familiares: cada hijo de un portador tiene un 50 % de probabilidad de heredar la variante.

➕ **Variantes y formas relacionadas:**

| Entidad | Definición |
|---|---|
| **Síndrome de Muir-Torre** | Lynch + **neoplasias sebáceas** (adenomas o carcinomas sebáceos) y queratoacantomas; con frecuencia **MSH2** |
| **Síndrome de Turcot** | CCR + tumor cerebral: con Lynch suele ser **glioblastoma**; con FAP, **meduloblastoma** |
| **Deficiencia constitucional de MMR (CMMRD)** | Variantes **bialélicas** germinales en un gen MMR (con frecuencia PMS2): tumores cerebrales y hematológicos en la **infancia**, CCR muy precoz y **manchas café con leche** |
| **Síndrome tipo Lynch** (*Lynch-like*) | Tumor dMMR sin metilación de MLH1 y sin variante germinal; a menudo dos mutaciones somáticas |

#### 5.6.6 💊 Ejemplo real: MMR deficiente predice respuesta a inmunoterapia *(Diap. 31)*

**Mecanismo:**

```
1 dMMR → MSI → cientos o miles de mutaciones
2 Mutaciones de cambio de marco → péptidos nuevos (neoantígenos) muy "extraños"
3 Los linfocitos T reconocen el tumor; el bloqueo de PD-1 libera el freno
```

**Tasa de respuesta objetiva a pembrolizumab (anti-PD-1)** (Le et al., NEJM 2015; fase 2, cohortes pequeñas):

| Grupo | Respuesta objetiva |
|---|---|
| CCR con MMR deficiente | **40 %** |
| CCR con MMR conservado | **0 %** |
| Otros tumores con MMR deficiente | **71 %** |

**Impacto:**
- En **2017** la FDA aprobó **pembrolizumab para tumores sólidos MSI-H/dMMR independientemente del órgano**: la **primera aprobación "agnóstica"** basada en un biomarcador.
- En el **CCR metastásico MSI-H de primera línea** (KEYNOTE-177), pembrolizumab **duplicó la supervivencia libre de progresión** frente a la quimioterapia: **16,5 frente a 8,2 meses**.

➕ **Más allá de la clase:**
- En el **cáncer de recto localmente avanzado dMMR**, 6 meses de **dostarlimab** (anti-PD-1) produjeron respuesta clínica completa en los 12 primeros pacientes (Cercek et al., NEJM 2022), sin quimiorradioterapia ni cirugía. La actualización de 2025 (NEJM 2025;392:2297–2308) informó respuesta clínica completa en los **49 pacientes con cáncer de recto** y en el **65 %** de 54 pacientes con otros tumores dMMR en estadios iniciales, lo que permitió evitar la cirugía en la mayoría.
- La FDA aprobó también pembrolizumab para tumores con **carga mutacional alta** (TMB-H, ≥10 mutaciones/Mb) en 2020.

#### 5.6.7 ➕ MMR también "decide" la respuesta a algunos fármacos

MMR no solo corrige errores: también **señaliza** ciertas lesiones para que la célula muera.

| Fármaco | Papel de MMR | Consecuencia de dMMR |
|---|---|---|
| **Temozolomida** | Ciclos fútiles sobre O⁶-meG:T → DSB → apoptosis | **Resistencia** (tolerancia) e hipermutación |
| **6-tioguanina** (tiopurinas) | Reconoce la tioguanina metilada mal apareada | Resistencia |
| **Cisplatino** | Contribuye a señalizar el daño | Resistencia leve |
| **Anti-PD-1** | — | **Sensibilidad** (neoantígenos) |

➕ **Otra causa de hipermutación**: las mutaciones del dominio **exonucleasa de POLE** (o POLD1) anulan la corrección de pruebas de la polimerasa y producen tumores **ultramutados** (cáncer de endometrio y colorrectal). En la línea germinal causan la **poliposis asociada a la corrección de pruebas de la polimerasa** (PPAP), autosómica dominante.

---

### 5.7 Roturas de doble cadena: NHEJ y HR

> Unión de extremos no homólogos (NHEJ) y recombinación homóloga (HR) *(Diap. 32)*.

#### 5.7.1 Por qué las DSB son las lesiones más peligrosas

En las demás lesiones la hebra complementaria conserva la información. En una DSB **se rompen las dos hebras**: el cromosoma queda partido y no hay molde en la misma molécula. Si los extremos se unen mal aparecen **translocaciones, deleciones o pérdida de un brazo cromosómico**, y si no se reparan, la célula muere.

**Fuentes de DSB** *(Diap. 33)*:
- **Accidentales**: radiación ionizante, horquillas de replicación colapsadas, etopósido (inhibidor de topoisomerasa II).
- **Programadas**: recombinación **V(D)J**, **cambio de isotipo** y **meiosis**.

#### 5.7.2 ¿NHEJ o HR? La fase del ciclo celular decide *(Diap. 33)*

- **NHEJ** está disponible en **todo el ciclo** y **predomina en G1**.
- **HR** funciona en **S y G2**, cuando existe la **cromátida hermana** como molde.

📌 **El punto de decisión: ¿se resecan los extremos?**

| Promueve NHEJ | Promueve HR |
|---|---|
| **53BP1–RIF1–shieldina** protegen los extremos y **bloquean la resección** | **BRCA1–CtIP–MRN** promueven la **resección 5′→3′**, activadas por las **CDK** en S/G2 |

```
                DSB
                 │
     ┌───────────┴────────────┐
 53BP1–RIF1–shieldina     BRCA1–CtIP–MRN (+ actividad CDK alta en S/G2)
 (extremos protegidos)    (resección 5′→3′ → colas 3′ de ADN monocatenario)
     │                        │
   NHEJ                      HR
```

➕ BRCA1 y 53BP1 son **antagonistas**. Este antagonismo explica una forma de resistencia a los inhibidores de PARP: si un tumor sin BRCA1 pierde además 53BP1, vuelve a resecar y recupera parte de la HR (sección 5.10.1).

#### 5.7.3 NHEJ: rápida pero imprecisa *(Diap. 34)*

```
1 UNIÓN DE Ku          2 DNA-PKcs                3 PROCESAMIENTO             4 LIGACIÓN
Ku70/80 forma un  ──►  se une a Ku, mantiene ──► Artemis (nucleasa),   ──►  XRCC4–LIG4 con XLF
anillo que se          juntos los extremos       Pol μ/λ y PNKP hacen       (y PAXX) sellan
ensarta en cada        (sinapsis) y se           compatibles los extremos
extremo                autofosforila
```

1. **Ku70/80**: heterodímero en forma de **anillo** que se ensarta en cada extremo roto. ➕ Es muy abundante y llega en segundos.
2. **DNA-PKcs**: se une a Ku, mantiene juntos los dos extremos (**sinapsis**) y se **autofosforila**.
3. **Procesamiento**: **Artemis** (nucleasa), **Pol μ/λ** y **PNKP** hacen compatibles los extremos.
4. **Ligación**: **XRCC4–LIG4**, con **XLF** (y **PAXX**), sella la rotura.

📌 **Resultado**: NHEJ **no usa molde**, así que puede **ganar o perder algunos nucleótidos** en la unión (pequeñas indels). Aun así es la **vía principal en humanos** y la **única en las células que no se dividen**, como las neuronas.

➕ **Vías alternativas** (más mutagénicas):
- **Unión de extremos mediada por microhomología (MMEJ o alt-EJ)**: depende de la **Pol θ (POLQ)**; deja deleciones flanqueadas por microhomologías. Los tumores con HR deficiente dependen más de ella, y hay inhibidores de Pol θ en estudio.
- **Hibridación de hebra sencilla (SSA)**: depende de RAD52; une repeticiones y elimina la secuencia intermedia.

#### 5.7.4 HR: lenta pero fiel *(Diap. 35)*

```
1 RESECCIÓN         2 RPA               3 FILAMENTO RAD51        4 INVASIÓN               5 SÍNTESIS Y RESOLUCIÓN
MRN–CtIP inicia; ─► RPA recubre el ──► BRCA2 (con PALB2 y  ──► el filamento busca  ──► Pol δ copia el molde;
EXO1 y DNA2–BLM     ADN monocatenario   BRCA1) reemplaza a      la secuencia homóloga    se resuelve por SDSA o
extienden colas 3′  y activa ATR        RPA por RAD51           en la cromátida          uniones de Holliday
                                                                hermana: bucle D
```

1. **Resección**: **MRN–CtIP** inicia; **EXO1** y **DNA2–BLM** extienden **colas 3′ de ADN monocatenario**.
2. **Recubrimiento por RPA**: RPA protege el ADN monocatenario y **activa ATR**.
3. **Filamento de RAD51**: **BRCA2** (con **PALB2** y **BRCA1**) **reemplaza a RPA por RAD51**.
4. **Invasión**: el filamento busca la secuencia homóloga en la **cromátida hermana** e invade la doble hélice formando un **bucle D**.
5. **Síntesis y resolución**: **Pol δ** copia el molde. Se resuelve por **SDSA** (*synthesis-dependent strand annealing*) o mediante **uniones de Holliday**.

➕ **Resolución**: en células somáticas predomina la **SDSA**, que no produce entrecruzamiento. Las **dobles uniones de Holliday** pueden "disolverse" (complejo **BLM**–TOP3A–RMI, sin entrecruzamiento) o "resolverse" con nucleasas (MUS81, SLX4, GEN1), con o sin entrecruzamiento. En la **meiosis** la HR genera los **entrecruzamientos** (*crossing-over*) a partir de DSB programadas por SPO11.

🧠 **El eje de la HR**: **"BRCA1 abre, BRCA2 carga"**. BRCA1 promueve la resección y BRCA2 carga RAD51. **PALB2** (*Partner And Localizer of BRCA2*) es el **puente** entre ambas.

#### 5.7.5 NHEJ frente a HR *(Diap. 36)*

| | **NHEJ** | **HR** |
|---|---|---|
| Molde | **No requiere** | **Cromátida hermana** |
| Fase del ciclo | Todo el ciclo; **predomina en G1** | **S y G2** |
| Fidelidad | **Propensa a errores** (pequeñas indels) | **Alta fidelidad** |
| Velocidad | **Rápida** (minutos) | **Lenta** (horas) |
| Proteínas clave | Ku70/80, DNA-PKcs, Artemis, XRCC4–LIG4, XLF | MRN, CtIP, BRCA1, PALB2, BRCA2, RAD51 |
| Función fisiológica | **Recombinación V(D)J** y **cambio de isotipo** | **Meiosis** (entrecruzamiento), reinicio de horquillas |
| Enfermedad por defecto | **SCID radiosensible** (Artemis, LIG4) | **Cáncer hereditario de mama/ovario**; Fanconi (FANCD1 = BRCA2) |
| Relevancia terapéutica | Radiosensibilidad; inhibidores de DNA-PK (en estudio) | **Inhibidores de PARP** en tumores con HR deficiente |

#### 5.7.6 🩺 Ejemplo real: SCID por deficiencia de Artemis (NHEJ) *(Diap. 37)*

**La recombinación V(D)J necesita NHEJ:**

```
 V ──── D ──── J
        │  RAG1/2 cortan en las señales de recombinación (RSS)
        ▼
 D ⊃      ⊂ J          extremos codificantes en HORQUILLA cerrada
        │  Artemis–DNA-PKcs abre las horquillas
        ▼
 D ═ J                 NHEJ une → receptor funcional (BCR o TCR)
```

**SCID de los pueblos atabascanos:**
- Sin Artemis no se forman receptores de linfocitos B ni T: **SCID T−B−NK+** (las NK no necesitan V(D)J).
- Las células del paciente son **hipersensibles a la radiación ionizante** (**SCID radiosensible**), porque Artemis también repara DSB accidentales.
- Una **mutación fundadora en DCLRE1C** (el gen de Artemis) explica la alta frecuencia de SCID en **navajos y apaches** (➕ del orden de 1 por cada 2.000 nacidos vivos en la población navajo).
- **Tratamiento**: **trasplante de progenitores hematopoyéticos**, con **cautela con el acondicionamiento alquilante** (y con la radiación).

➕ **Para el diagnóstico diferencial:**
- Otras SCID radiosensibles T−B−NK+: **LIG4** (síndrome de ligasa IV, con microcefalia), **XLF/Cernunnos** y **DNA-PKcs**.
- La deficiencia de **RAG1/2** también produce SCID T−B−NK+, pero **no es radiosensible**: RAG solo actúa en la V(D)J y no repara DSB accidentales.
- El **tamizaje neonatal de SCID** mide los **TREC** (*T-cell receptor excision circles*), círculos de ADN que se escinden durante la recombinación V(D)J del TCR. Si no hay V(D)J, no hay TREC.

#### 5.7.7 🩺 Ejemplo real: BRCA1 y BRCA2, falla de la recombinación homóloga *(Diap. 38)*

| Proteína | Función en la HR |
|---|---|
| **BRCA1** | Con **BARD1**: promueve la **resección** y la **señalización** de las DSB |
| **BRCA2** | **Carga RAD51** sobre el ADN monocatenario (con **PALB2**) |

**Riesgo acumulado hasta los 80 años (%)** (Kuchenbaecker et al., JAMA 2017; población general según SEER):

| Cáncer | Población general | Portadoras de **BRCA1** | Portadoras de **BRCA2** |
|---|---|---|---|
| **Mama** | 12 | **72** | **69** |
| **Ovario** | 1,3 | **44** | **17** |

🧠 El riesgo de mama es parecido (~70 %) con los dos genes; el de ovario es **mucho mayor con BRCA1** (44 % frente a 17 %).

**Puntos clave:**
- Herencia **autosómica dominante**; el tumor **pierde el segundo alelo**.
- También aumentan el riesgo de cáncer de **próstata, páncreas y mama masculino** (sobre todo **BRCA2**).
- **Mutaciones fundadoras** en **judíos asquenazíes**: **185delAG** y **5382insC** (BRCA1) y **6174delT** (BRCA2).
- **Opciones**: vigilancia con **resonancia magnética**, **cirugía reductora de riesgo** e **inhibidores de PARP**.

➕ **Más detalles útiles:**
- Los tumores de mama de portadoras de **BRCA1** suelen ser **triple negativos** (basales); los de **BRCA2**, con más frecuencia **receptores hormonales positivos**.
- Otros genes de HR con riesgo de mama u ovario: **PALB2**, **RAD51C**, **RAD51D**, **BRIP1**; de riesgo moderado: **ATM** y **CHEK2**.
- **BRCA2 bialélico** (o PALB2 bialélico) causa **anemia de Fanconi** grave (FA-D1 y FA-N), con tumores sólidos y leucemias en la infancia.
- En los tumores con HR deficiente, el platino y los inhibidores de PARP funcionan mejor (sección 5.10.1).

#### 5.7.8 🩺 Ejemplo real: ataxia-telangiectasia (A-T), cuando falla la señal de alarma *(Diap. 39)*

**ATM** es una **cinasa** que, tras una DSB, **fosforila cientos de sustratos**: **CHK2, p53, γH2AX, BRCA1, KAP1, MRN**. Sin ATM, la célula no activa bien los puntos de control ni coordina la reparación.

| Manifestación | Detalle |
|---|---|
| **Ataxia cerebelosa progresiva** | Empieza entre **1 y 4 años**; silla de ruedas en la adolescencia |
| **Telangiectasias oculocutáneas** | Visibles en las **conjuntivas**, típicamente después de los **3–5 años** (por eso la ataxia suele preceder a las telangiectasias) |
| **Inmunodeficiencia** | Infecciones **sinopulmonares**; **IgA e IgG2 bajas** |
| **Radiosensibilidad extrema y cáncer** | **~25 % de riesgo de por vida**, sobre todo **linfomas y leucemias** |
| **Pista diagnóstica** | **Alfafetoproteína sérica elevada** |

🩺 **Implicaciones**:
- **Evitar la radiación ionizante** innecesaria (radiografías y TC). Si hace falta radioterapia, las dosis estándar pueden ser letales.
- Herencia **autosómica recesiva** (gen ATM, cromosoma 11q22-23).
- ➕ Las **portadoras heterocigotas** (madres, hermanas) tienen un riesgo de cáncer de mama aproximadamente **doble**.
- ➕ El cariotipo de los linfocitos muestra con frecuencia **translocaciones entre los cromosomas 7 y 14**, en los loci de TCR e inmunoglobulinas.
- ➕ La AFP es fisiológicamente alta en el lactante, así que se interpreta mejor después de los 2 años.

#### 5.7.9 ➕ Otros síndromes de inestabilidad cromosómica que conviene distinguir

| Síndrome | Gen (función) | Herencia | Claves clínicas |
|---|---|---|---|
| **Nijmegen breakage syndrome** | **NBN** (NBS1, parte de MRN) | AR | **Microcefalia**, cara "de pájaro", inmunodeficiencia, radiosensibilidad, linfomas. AFP **normal**. Mutación fundadora 657del5 en poblaciones eslavas |
| **Trastorno tipo A-T (ATLD)** | **MRE11** | AR | Parecido a A-T, más leve, sin telangiectasias |
| **Síndrome de Bloom** | **BLM** (helicasa RecQ; resolución de la HR) | AR | Talla baja proporcionada, **eritema facial fotosensible**, inmunodeficiencia, cánceres múltiples. **Aumento de los intercambios entre cromátidas hermanas**. Fundadora en asquenazíes |
| **Síndrome de Werner** | **WRN** (helicasa RecQ) | AR | **Progeria del adulto**: canas, cataratas, diabetes y aterosclerosis precoces, sarcomas |
| **Síndrome de Seckel** | **ATR** (hipomorfo) | AR | Microcefalia y enanismo |
| **Síndrome de ligasa IV** | **LIG4** (NHEJ) | AR | Microcefalia, SCID radiosensible |
| **Li-Fraumeni** | **TP53** | **AD** | Sarcomas, mama precoz, cerebro, corteza suprarrenal, leucemia |

---

### 5.8 Anemia de Fanconi y enlaces cruzados intercatenarios

#### 5.8.1 El problema del ICL

Un **enlace cruzado intercatenario (ICL)** une covalentemente las dos hebras. Ninguna helicasa puede separarlas, así que **bloquea la replicación y la transcripción**. Para repararlo hay que cortar en una hebra, "saltar" el aducto que queda colgando y reparar la rotura que se genera: por eso la vía de Fanconi **integra NER, TLS y HR**.

**Fuentes de ICL**: cisplatino, **mitomicina C**, mostazas nitrogenadas (ciclofosfamida, melfalán), nitrosoureas, psoralenos + UVA y ➕ **aldehídos endógenos** (formaldehído, acetaldehído).

#### 5.8.2 La vía de Fanconi paso a paso *(Diap. 40)*

```
1 ICL bloquea la horquilla de replicación
        ▼
2 Complejo central FA (FANCA, B, C, E, F, G, L, M…)   ← FANCL es la ubiquitina-ligasa (E3)
        ▼
3 MONOUBIQUITINACIÓN de FANCD2–FANCI                   ← paso central: el "interruptor" de la vía
        ▼
4 Nucleasas "desenganchan" el ICL (XPF–ERCC1, SLX4)   ← ingrediente de NER
        ▼
5 TLS rellena frente al aducto (REV1, Pol ζ)          ← ingrediente de TLS
        ▼
6 HR repara la DSB (BRCA2 = FANCD1, PALB2 = FANCN)    ← ingrediente de HR
```

📌 Hay **más de 20 genes FANC**. La vía integra **NER, TLS y HR**.

➕ **Equivalencias útiles** (muchos genes "FANC" ya los conoces con otro nombre):

| Gen FANC | Nombre clásico | Vía de origen |
|---|---|---|
| **FANCD1** | **BRCA2** | HR |
| **FANCN** | **PALB2** | HR |
| **FANCS** | **BRCA1** | HR |
| **FANCJ** | **BRIP1** | HR (helicasa) |
| **FANCO** | **RAD51C** | HR |
| **FANCR** | **RAD51** | HR |
| **FANCQ** | **XPF (ERCC4)** | NER (nucleasa) |
| **FANCP** | **SLX4** | Andamio de nucleasas |

#### 5.8.3 🩺 Clínica de la anemia de Fanconi *(Diap. 40)*

- **Insuficiencia medular progresiva** (pancitopenia). ➕ Suele aparecer en la primera década.
- **Malformaciones**: **radio/pulgar**, **talla baja**, **manchas café con leche** (➕ también renales, cardíacas y microcefalia; no todos los pacientes las tienen).
- Riesgo alto de **leucemia mieloide aguda** (y SMD) y de **carcinoma escamoso de cabeza y cuello** (➕ y anogenital).
- **BRCA2 bialélico (FANCD1)**: forma **grave** con tumores en la infancia (meduloblastoma, tumor de Wilms, leucemia).

**Diagnóstico: prueba de fragilidad cromosómica.** Los linfocitos expuestos a **diepoxibutano (DEB)** o **mitomicina C (MMC)** muestran **roturas cromosómicas y figuras radiales**.

➕ **Detalles de experto:**
- **Herencia**: casi siempre **autosómica recesiva**. Las excepciones son **FANCB**, **ligado al X**, y **FANCR (RAD51)**, **autosómico dominante** (de novo).
- **Mosaicismo**: algunos pacientes recuperan la función en parte de su médula por una reversión somática, y la prueba en sangre puede salir "normal". En ese caso se estudian fibroblastos de piel.
- **Tratamiento**: el **trasplante de progenitores hematopoyéticos** es el único tratamiento curativo de la falla medular. Se usa **acondicionamiento de intensidad reducida** (por ejemplo, basado en fludarabina), porque los pacientes toleran muy mal los alquilantes y la radiación. También se usan andrógenos para la falla medular y vigilancia de carcinomas escamosos.
- **Aldehídos y ALDH2**: en pacientes con Fanconi que además portan la variante **ALDH2\*2** (frecuente en Asia oriental), que elimina peor el acetaldehído, la falla medular es más precoz. Así se confirmó que los aldehídos endógenos son una fuente real de ICL.

---

### 5.9 Tolerancia al daño: síntesis translesión (TLS)

> Cuando no hay tiempo para reparar, la célula pasa por encima de la lesión *(Diap. 41)*.

⚠️ La TLS **no repara**: la lesión sigue en el ADN. Lo que hace es **permitir que la replicación continúe** para que la horquilla no colapse, y la lesión se repara después.

#### 5.9.1 El mecanismo *(Diap. 42)*

```
1. La polimerasa replicativa (Pol δ/ε) se detiene frente a la lesión
        ▼
2. RAD6–RAD18 MONOubiquitinan PCNA (lisina 164) → cambio de polimerasa
        ▼
3. Una polimerasa TLS (p. ej., Pol η) inserta nucleótidos frente a la lesión
        ▼
4. Vuelve la polimerasa replicativa
```

- **Pol η** (gen **POLH**) inserta **AA frente al dímero TT** de forma **correcta**: su sitio activo amplio acomoda las dos T unidas.
- Las otras polimerasas TLS (**Pol ι, κ, ζ, REV1**) tienen **baja fidelidad**: permiten sobrevivir a costa de mutaciones.
- La alternativa **sin error** es el **cambio de molde** (*template switching*), señalizado por la **PCNA poliubiquitinada**: la hebra nueva usa como molde la cromátida hermana recién sintetizada.

➕ **Detalles:**
- Modelo **"insertador–extensor"**: una polimerasa de la familia Y (η, ι, κ o REV1) inserta frente a la lesión y **Pol ζ** (REV3L–REV7) extiende a partir de ahí.
- **REV1** es una desoxicitidil-transferasa: inserta **C** frente a sitios abásicos o guaninas dañadas.
- La PCNA **monoubiquitinada** (RAD6–RAD18) activa la TLS; la **poliubiquitinada** (cadenas K63, por UBC13–MMS2 con HLTF/SHPRH) activa el cambio de molde.
- La TLS ayuda a los tumores a tolerar el cisplatino, otra forma de resistencia.

🧠 **"Mono = monta otra polimerasa (TLS, puede equivocarse); Poli = pide prestada la hermana (cambio de molde, sin error)."**

#### 5.9.2 🩺 Xeroderma pigmentoso variante (XPV) *(Diap. 42)*

- **NER normal**, pero mutación en **POLH (Pol η)**.
- Sin Pol η, otras polimerasas "adivinan" frente al dímero → **mutaciones C→T**.
- **Cáncer de piel frecuente**, con **inicio más tardío** y **generalmente sin neurodegeneración**.
- Representa una **fracción importante** de los pacientes con XP (Masutani et al., Nature 1999).

📌 Es la respuesta a la pregunta clásica: *"Un paciente con XP tiene NER normal en el laboratorio. ¿Qué gen sospechas?"* → **POLH**.

➕ En el laboratorio, la síntesis no programada de ADN tras UV (que mide NER) es normal. La pista es una sensibilidad a UV que aumenta con **cafeína**.

---

### 5.10 Integración: de la biología a la clínica

#### 5.10.1 💊 Letalidad sintética: inhibidores de PARP y tumores BRCA *(Diap. 44)*

**Letalidad sintética**: dos defectos que por separado se toleran, pero juntos matan a la célula.

| | **HR funcional** | **HR deficiente (BRCA1/2 mutado)** |
|---|---|---|
| **PARP activa** | Célula normal → **sobrevive** | Tumor BRCA → **sobrevive** (PARP compensa) |
| **PARP inhibida** | Célula normal + inhibidor → **sobrevive** (HR repara) | Tumor BRCA + inhibidor → **MUERE** |

**Mecanismo:**

```
1 El inhibidor bloquea PARP1 y la ATRAPA sobre las roturas de cadena sencilla
        ▼
2 Al replicar, la horquilla choca con la lesión → rotura de doble cadena
        ▼
3 Sin BRCA1/2 la HR falla → reparación propensa a error (NHEJ, MMEJ) → caos cromosómico → muerte
```

📌 **¿Por qué las células normales de una portadora de BRCA1 toleran el fármaco?** Porque son **heterocigotas**: conservan un alelo funcional y hacen HR. Solo las células tumorales perdieron el segundo alelo (sección 5.1.5).

**Evidencia clínica:**
- **OlympiAD** (Robson et al., NEJM 2017): olaparib en cáncer de mama metastásico HER2− con BRCA germinal; supervivencia libre de progresión de **7,0 frente a 4,2 meses** con la quimioterapia estándar.
- Aprobados también en **ovario, próstata y páncreas**.
- ➕ **SOLO-1** (ovario, mantenimiento tras platino, BRCA mutado): el riesgo de progresión o muerte bajó un ~70 % (HR 0,30). **OlympiA**: olaparib adyuvante en cáncer de mama precoz de alto riesgo con BRCA germinal mejoró la supervivencia libre de enfermedad invasiva y la global. **POLO** (páncreas metastásico con BRCA germinal, mantenimiento): supervivencia libre de progresión de 7,4 frente a 3,8 meses. **PROfound**: próstata resistente a castración con alteraciones de genes de HR.

➕ **Conceptos de experto:**
- **Atrapamiento frente a inhibición catalítica**: la toxicidad se debe sobre todo a que PARP queda **atrapada** en el ADN, un obstáculo peor que una SSB sin reparar. La potencia de atrapamiento varía: talazoparib > niraparib > olaparib ≈ rucaparib ≫ veliparib.
- **"BRCAness" y HRD**: tumores sin mutación de BRCA pero con HR deficiente por otras causas (PALB2, RAD51C/D, metilación del promotor de BRCA1…) también responden. Se detectan por la "cicatriz genómica" (pérdida de heterocigosidad, desequilibrio alélico telomérico, transiciones de estado a gran escala) o por la firma mutacional SBS3. Alrededor de la mitad de los carcinomas serosos de alto grado de ovario son HRD.
- **Resistencia a los inhibidores de PARP** (y al platino):
  1. **Mutaciones de reversión** en BRCA1/2 que restauran el marco de lectura.
  2. **Pérdida de 53BP1 o de la shieldina** en tumores sin BRCA1: vuelven a resecar y recuperan parte de la HR.
  3. Menor atrapamiento (pérdida o mutación de PARP1).
  4. Más eflujo del fármaco (bomba ABCB1/P-gp).
  5. Protección de las horquillas de replicación.
- **Otras dianas de letalidad sintética en estudio**: ATR, CHK1, WEE1 (fuerzan la entrada en mitosis con ADN dañado), Pol θ (en tumores HRD) y WRN (en tumores MSI).

#### 5.10.2 ➕ Firmas mutacionales: la lesión deja una huella *(Diap. 48, mensaje 4)*

📌 La **firma mutacional** del tumor puede revelar **qué vía falló o qué agente lo dañó**. Una firma combina el tipo de cambio de base y sus bases vecinas.

| Proceso | Firma (catálogo COSMIC) | Patrón característico |
|---|---|---|
| Desaminación espontánea de 5-metilC (envejecimiento) | **SBS1** | C>T en CpG; aumenta con la edad ("reloj") |
| **Luz UV** | **SBS7** (+ DBS1) | **C>T y CC>TT** en dipirimidinas |
| **Tabaco** (benzo[a]pireno) | **SBS4** | **C>A** (G→T) |
| **Aflatoxina** | **SBS24** | C>A (TP53 R249S) |
| **Defecto de MUTYH** | **SBS36** (y SBS18, ROS) | **C>A** (G:C→T:A) |
| **Defecto de NTHL1** | **SBS30** | C>T |
| **MMR deficiente** | **SBS6, 15, 20, 21, 26, 44** + indels en repeticiones | Cambios de 1 base e **indels en microsatélites** |
| **POLE** (corrección de pruebas) | **SBS10** | Ultramutación, C>A en TCT y C>T en TCG |
| **HR deficiente** (BRCA) | **SBS3** + deleciones con microhomología | Patrón "plano", reordenamientos |
| **Temozolomida** | **SBS11** | C>T (G→A) |
| **Platino** | **SBS31, SBS35** | C>T |
| **APOBEC** | **SBS2, SBS13** | C>T y C>G en TCW |

#### 5.10.3 💊 Los fármacos que dañan el ADN y la vía que decide la respuesta

| Fármaco | Lesión principal | Vía que la repara | Qué predice **sensibilidad** | Qué predice **resistencia** |
|---|---|---|---|---|
| **Temozolomida** (y dacarbazina, procarbazina) | O⁶-meG (también N7-meG, N3-meA) | **MGMT** (reversión directa); MMR media la toxicidad | **Promotor de MGMT metilado** | MGMT alta; **pérdida de MMR** |
| **Nitrosoureas** (carmustina, lomustina) | O⁶-cloroetilG → **ICL** | MGMT (lo previene); Fanconi/HR | MGMT silenciado | MGMT alta |
| **Cisplatino, carboplatino** | Aductos **intracatenarios** (~90 %) e **ICL** | **NER**; Fanconi + HR para los ICL | **HR deficiente** (BRCA); NER baja (XPA baja en testículo) | NER alta (ERCC1); reversión de BRCA; TLS |
| **Mostazas nitrogenadas, mitomicina C** | **ICL** | Fanconi + HR | HR o FA deficientes | — |
| **Inhibidores de topoisomerasa I** (irinotecán, topotecán) | TOP1 atrapada → SSB → **DSB** al replicar | HR (y TDP1) | HR deficiente | — |
| **Inhibidores de topoisomerasa II** (etopósido, doxorrubicina) | TOP2 atrapada → **DSB** | NHEJ y HR (y TDP2) | — | — |
| **Radioterapia** | **DSB** (y SSB, bases) | **NHEJ** y HR | Defectos de ATM, Artemis, LIG4 (toxicidad grave en pacientes) | Hipoxia; reparación eficiente |
| **Inhibidores de PARP** | PARP atrapada → **DSB** en fase S | **HR** | **BRCA1/2**, HRD | Reversión de BRCA; pérdida de 53BP1 |
| **Anti-PD-1** (pembrolizumab, dostarlimab) | — (no dañan el ADN) | — | **dMMR / MSI-H**, TMB alta | MMR conservado (CCR) |

#### 5.10.4 📌 Resumen maestro: vía, lesión, enfermedad y aplicación clínica *(Diap. 45, ampliada)*

| Vía | Lesión | Proteínas clave | Enfermedad por defecto | Herencia ➕ | Aplicación clínica |
|---|---|---|---|---|---|
| **Reversión directa** | O⁶-metilguanina | MGMT | — (silenciamiento en tumores) | — | Temozolomida en glioblastoma |
| **BER** | Bases oxidadas, U, sitios AP | Glicosilasas, APE1, Pol β, PARP1 | Poliposis MUTYH; hiper-IgM (UNG) | AR; AR | Inhibidores de PARP |
| **NER** | Dímeros UV, aductos voluminosos | XPA–XPG, TFIIH, CSA/CSB | XP, Cockayne, tricotiodistrofia | AR | Sensibilidad a cisplatino |
| **MMR** | Apareamientos erróneos, bucles | MSH2/6, MLH1, PMS2 | Síndrome de Lynch | AD (CMMRD: AR) | Anti-PD-1 en tumores dMMR |
| **NHEJ** | DSB (G1) | Ku, DNA-PKcs, Artemis, LIG4 | SCID radiosensible | AR | Radioterapia |
| **HR** | DSB en S/G2; horquillas rotas | BRCA1/2, PALB2, RAD51 | Cáncer de mama/ovario hereditario | AD (bialélico → Fanconi) | Inhibidores de PARP |
| **Señalización DDR** | DSB | ATM, MRN | Ataxia-telangiectasia | AR | Evitar radiación estándar |
| **FA / ICL** | Enlaces cruzados | FANC, FANCD2–I | Anemia de Fanconi | AR (FANCB ligado al X) | Prueba DEB/MMC |
| **TLS** | Lesiones al replicar | PCNA-Ub, Pol η | XP variante | AR | — |

#### 5.10.5 ➕ Tabla rápida de enfermedades para diagnóstico diferencial

| Enfermedad | Gen(es) | Vía | Herencia | Pista que la delata |
|---|---|---|---|---|
| Xeroderma pigmentoso | XPA–XPG | GG-NER | AR | Pecas o quemaduras antes de los 2 años; cáncer de piel en la infancia |
| XP variante | POLH | TLS | AR | XP con **NER normal**; inicio más tardío |
| Síndrome de Cockayne | ERCC6 (CSB), ERCC8 (CSA) | TC-NER | AR | Fotosensibilidad + talla baja, aspecto envejecido; **sin cáncer** |
| Tricotiodistrofia | ERCC2, ERCC3, GTF2H5 | TFIIH | AR | **Pelo quebradizo pobre en azufre**, ictiosis |
| Poliposis asociada a MUTYH | MUTYH | BER (sistema GO) | AR | Poliposis sin APC; **G:C→T:A**; hermanos afectados |
| Hiper-IgM tipo 5 | UNG | BER | AR | IgM normal/alta, IgG/IgA/IgE bajas, linfadenopatía |
| Síndrome de Lynch | MLH1, MSH2, EPCAM, MSH6, PMS2 | MMR | AD | CCR derecho y endometrio jóvenes; **MSI-H**; Ámsterdam 3-2-1 |
| CMMRD | MMR bialélico | MMR | AR | Tumores cerebrales y hematológicos infantiles + café con leche |
| SCID por Artemis | DCLRE1C | NHEJ | AR | **T−B−NK+**, radiosensible; navajos y apaches |
| Cáncer de mama/ovario hereditario | BRCA1, BRCA2 | HR | AD | Mama precoz o triple negativa, ovario, mama masculino, asquenazíes |
| Anemia de Fanconi | >20 FANC | ICL | AR (FANCB ligado al X) | Falla medular + **radio/pulgar** + café con leche; **DEB/MMC positivo** |
| Ataxia-telangiectasia | ATM | Señalización DDR | AR | Ataxia + telangiectasias conjuntivales + infecciones + **AFP alta** |
| Nijmegen | NBN | MRN | AR | **Microcefalia** + inmunodeficiencia + radiosensibilidad; AFP normal |
| Bloom | BLM | HR (helicasa) | AR | Talla baja + eritema facial + **↑ intercambio entre cromátidas hermanas** |
| Li-Fraumeni | TP53 | DDR (efector) | AD | Sarcomas, mama precoz, cerebro, suprarrenal |

#### 5.10.6 Mensajes para llevar *(Diap. 48)*

1. El ADN sufre **decenas de miles de lesiones por célula al día**; la reparación es **constante, no excepcional**.
2. **Cada tipo de lesión tiene su vía**: pequeña → BER; voluminosa → NER; error de copia → MMR; rotura doble → NHEJ o HR.
3. Los **defectos hereditarios de reparación** causan **cáncer, inmunodeficiencia, neurodegeneración o envejecimiento prematuro**.
4. La **firma mutacional** del tumor puede revelar qué vía falló (MUTYH, MMR, UV, tabaco).
5. La **reparación del tumor determina la respuesta al tratamiento**: temozolomida, cisplatino, PARP e inmunoterapia.

---

### 5.11 Casos clínicos resueltos

> *(Diap. 46)* Para cada caso: ¿qué vía está alterada? ¿qué gen sospechas? ¿qué implica para el tratamiento y para la familia? Intenta responder antes de abrir la solución.

#### Caso 1
**Niña de 8 años con pecas abundantes en zonas expuestas desde los 2 años, fotofobia y un carcinoma basocelular nasal. Padres primos hermanos.**

<details>
<summary>Ver solución</summary>

- **Diagnóstico**: **xeroderma pigmentoso**.
- **Por qué**: pecas precoces (antes de los 2 años) solo en zonas expuestas, fotofobia (afectación ocular) y un cáncer de piel a una edad en la que es excepcional (la mediana en XP es 9 años). La **consanguinidad** apunta a una herencia **autosómica recesiva**.
- **Vía**: **NER**, sobre todo GG-NER.
- **Gen**: un gen XP. Por frecuencia, **XPC** (EE. UU., Europa, norte de África) o **XPA** (Japón). Las pecas sin quemaduras exageradas encajan bien con XPC. Si el estudio de NER fuera normal, habría que pensar en **POLH (XPV)**.
- **Tratamiento**: **fotoprotección estricta** (ropa, filtros, vidrios con filtro UV), revisión dermatológica frecuente con extirpación precoz, evaluación **oftalmológica** y **neurológica** (vigilar neurodegeneración, sobre todo en XPA/XPD), suplemento de vitamina D y valorar quimioprevención con retinoides si aparecen muchos tumores.
- **Familia**: los padres son portadores obligados. Cada hermano tiene un **25 %** de riesgo de estar afectado y un 50 % de ser portador. Se ofrece asesoramiento genético y estudio de hermanos.
</details>

#### Caso 2
**Hombre de 42 años con adenocarcinoma de colon derecho. Su padre tuvo cáncer de colon a los 48 y una tía, de endometrio. La IHQ muestra pérdida de MSH2 y MSH6.**

<details>
<summary>Ver solución</summary>

- **Diagnóstico**: **síndrome de Lynch**. Cumple Ámsterdam II ("3-2-1"): 3 familiares con cánceres del espectro Lynch (colon, colon, endometrio), 2 generaciones y al menos uno antes de los 50.
- **Vía**: **MMR**.
- **Gen**: **MSH2** o una **deleción de EPCAM** que silencia MSH2. MSH6 se pierde porque **MSH2 es su socio obligado**: sin MSH2, MSH6 es inestable y se degrada. Se confirma con **estudio germinal**.
- **Tratamiento del paciente**: el tumor es dMMR/MSI-H. Si hay enfermedad metastásica, el **anti-PD-1 (pembrolizumab)** en primera línea es superior a la quimioterapia (KEYNOTE-177). Por el riesgo de cáncer metacrónico se puede valorar una colectomía más extensa. Después, colonoscopia cada 1–2 años, cribado de otros tumores del espectro y valorar aspirina.
- **Familia**: herencia **autosómica dominante**. Cada hijo y cada hermano tiene un **50 %** de riesgo. Se hace **estudio en cascada** de la variante. Los portadores inician colonoscopia cada 1–2 años desde los 20–25 años, y las mujeres portadoras valoran histerectomía y salpingooforectomía al terminar la paridad.
</details>

#### Caso 3
**Mujer de 35 años con cáncer de mama triple negativo. Su madre murió de cáncer de ovario a los 50 años.**

<details>
<summary>Ver solución</summary>

- **Diagnóstico**: sospecha de **síndrome de cáncer de mama y ovario hereditario**.
- **Vía**: **recombinación homóloga**.
- **Gen**: **BRCA1** es el más probable. El cáncer de mama **triple negativo** precoz es típico de BRCA1, y el riesgo de ovario es mucho mayor con BRCA1 (44 %) que con BRCA2 (17 %). Se hace un **panel germinal** (BRCA1, BRCA2, PALB2, RAD51C/D…).
- **Tratamiento**: el tumor HR deficiente es **sensible al platino** y a los **inhibidores de PARP** (olaparib en enfermedad metastásica; olaparib adyuvante en enfermedad precoz de alto riesgo). Hay que valorar **mastectomía bilateral reductora de riesgo** y **salpingooforectomía** reductora de riesgo (en BRCA1 hacia los 35–40 años, tras completar la paridad).
- **Familia**: herencia **autosómica dominante** (50 % para cada familiar de primer grado). Los varones portadores también tienen riesgo de cáncer de **próstata, páncreas y mama masculino** (sobre todo con BRCA2). Se ofrece estudio en cascada; las portadoras inician vigilancia con resonancia magnética mamaria.
</details>

#### Caso 4
**Niño de 4 años con marcha inestable progresiva, vasos dilatados en las conjuntivas, sinusitis y neumonías recurrentes. Alfafetoproteína elevada.**

<details>
<summary>Ver solución</summary>

- **Diagnóstico**: **ataxia-telangiectasia**. Reúne la tétrada: ataxia cerebelosa progresiva, telangiectasias conjuntivales, infecciones sinopulmonares por inmunodeficiencia y **AFP elevada**.
- **Vía**: **señalización de la respuesta al daño** de las DSB.
- **Gen**: **ATM** (autosómico recesivo).
- **Tratamiento**: **evitar la radiación ionizante** innecesaria (radiografías, TC) por la radiosensibilidad extrema. Si aparece un cáncer (riesgo ~25 %, sobre todo linfomas y leucemias), hay que **reducir la radioterapia y los fármacos radiomiméticos**. Manejo de la inmunodeficiencia (inmunoglobulinas si hay déficit de anticuerpos, vacunas, tratamiento precoz de infecciones), rehabilitación y vigilancia pulmonar y oncológica.
- **Familia**: los padres son portadores (25 % de recurrencia en cada embarazo). Las **mujeres portadoras heterocigotas** tienen un riesgo de cáncer de mama aproximadamente doble, por lo que merecen vigilancia.
</details>

#### ➕ Casos adicionales

**Caso 5.** Varón de 7 años con dos hermanos sanos y padres sanos, consulta por infecciones bacterianas sinopulmonares recurrentes y adenopatías. IgM alta; IgG, IgA e IgE muy bajas. No tiene infecciones oportunistas. La expresión de CD40L en linfocitos T es normal.

<details>
<summary>Ver solución</summary>

Síndrome de **hiper-IgM por defecto intrínseco del linfocito B**: **UNG (HIGM5)** o **AID (HIGM2)**, autosómicos recesivos. Falla el cambio de isotipo, porque AID desamina C→U y UNG retira el U para crear las roturas. La ausencia de infecciones oportunistas y el CD40L normal descartan la forma ligada al X (CD40L).
</details>

**Caso 6.** Lactante navajo de 4 meses con candidiasis oral persistente, diarrea crónica y neumonía. Linfocitos T y B ausentes, NK normales. Sus fibroblastos son muy sensibles a la radiación ionizante.

<details>
<summary>Ver solución</summary>

**SCID T−B−NK+ radiosensible por deficiencia de Artemis (DCLRE1C)**, por la mutación fundadora atabascana. Sin Artemis no se abren las horquillas de la V(D)J (y fallan también las DSB accidentales). Tratamiento: trasplante de progenitores hematopoyéticos con acondicionamiento cauteloso (evitar o reducir alquilantes y radiación). La radiosensibilidad lo distingue de la deficiencia de RAG.
</details>

**Caso 7.** Niña de 6 años con talla baja, pulgares hipoplásicos, manchas café con leche y pancitopenia progresiva. La prueba con diepoxibutano muestra muchas roturas cromosómicas y figuras radiales.

<details>
<summary>Ver solución</summary>

**Anemia de Fanconi**: defecto de la reparación de **enlaces cruzados intercatenarios**. La prueba DEB/MMC es diagnóstica. Riesgo de LMA y carcinoma escamoso de cabeza y cuello. El trasplante requiere acondicionamiento de intensidad reducida, porque la paciente es hipersensible a alquilantes y radiación.
</details>

**Caso 8.** Paciente con glioblastoma y promotor de MGMT metilado, que respondió a temozolomida. Al recaer, la secuenciación del tumor muestra cientos de mutaciones C→T y una mutación nueva en MSH6.

<details>
<summary>Ver solución</summary>

**Resistencia adquirida a temozolomida por pérdida de MMR**. La toxicidad de la O⁶-meG depende de los ciclos fútiles de MMR. Al perder MSH6, el tumor tolera las lesiones O⁶-meG:T y acumula transiciones C→T (firma SBS11): **hipermutación inducida por temozolomida**.
</details>

**Caso 9.** Niño de 5 años con talla muy baja, microcefalia, ojos hundidos, cataratas, hipoacusia y quemaduras solares con mínima exposición. No tiene lesiones cutáneas premalignas. La RM muestra desmielinización y calcificaciones.

<details>
<summary>Ver solución</summary>

**Síndrome de Cockayne**: defecto de **TC-NER** (**ERCC6/CSB** o **ERCC8/CSA**). Hay fotosensibilidad sin aumento de cáncer, porque GG-NER está conservada, y neurodegeneración y aspecto envejecido, porque la transcripción queda bloqueada y las células mueren.
</details>

**Caso 10.** Mujer con cáncer de ovario seroso de alto grado y BRCA1 germinal, tratada con olaparib durante dos años con buena respuesta. Ahora progresa. La biopsia muestra una deleción secundaria en BRCA1 que restaura el marco de lectura.

<details>
<summary>Ver solución</summary>

**Resistencia a inhibidores de PARP por mutación de reversión de BRCA1**: el tumor recupera una proteína BRCA1 funcional, vuelve a hacer HR y desaparece la letalidad sintética. Suele acompañarse de resistencia al platino. Otro mecanismo posible en tumores sin BRCA1 es la pérdida de 53BP1 o de la shieldina.
</details>

---

### 5.12 Preguntas de repaso resueltas y autoevaluación

#### 5.12.1 Las preguntas de la clase *(Diap. 47)*

**1. ¿Por qué una mutación en MSH2 se acompaña de pérdida de MSH6 en la inmunohistoquímica?**
<details><summary>Respuesta</summary>

Porque MSH6 solo es estable formando el heterodímero **MutSα (MSH2–MSH6)**: MSH2 es su **socio obligado**. Sin MSH2, MSH6 se degrada y no se tiñe. Al revés no ocurre: si falta MSH6, MSH2 se estabiliza uniéndose a MSH3, así que la pérdida aislada de MSH6 apunta a MSH6. Lo mismo pasa con MLH1 y PMS2.
</details>

**2. Un paciente con XP tiene NER normal en el laboratorio. ¿Qué gen sospechas?**
<details><summary>Respuesta</summary>

**POLH**, que codifica la **Pol η**: es el **XP variante (XPV)**. El defecto no está en NER, sino en la **síntesis translesión**: sin Pol η, otras polimerasas de baja fidelidad copian frente a los dímeros TT y generan mutaciones C→T.
</details>

**3. ¿Por qué los inhibidores de PARP son relativamente bien tolerados por las células normales de una portadora de BRCA1?**
<details><summary>Respuesta</summary>

Porque sus células normales son **heterocigotas**: conservan un alelo funcional de BRCA1 y hacen **recombinación homóloga**, así que reparan las DSB que aparecen al inhibir PARP. Solo las células tumorales, que perdieron el segundo alelo, carecen de HR y mueren (**letalidad sintética**).
</details>

**4. ¿Qué vía de reparación de DSB usa principalmente una neurona y por qué?**
<details><summary>Respuesta</summary>

**NHEJ**. La neurona es posmitótica (G0/G1): no replica su ADN, así que **no tiene cromátida hermana** que sirva de molde para la HR, y su actividad CDK baja no activa la resección. NHEJ es la única vía de DSB disponible en las células que no se dividen.
</details>

**5. ¿Por qué el silenciamiento de MGMT es una buena noticia en un paciente con glioblastoma?**
<details><summary>Respuesta</summary>

Porque predice **beneficio de la temozolomida**. Sin MGMT, el tumor no puede retirar la O⁶-metilguanina que genera el fármaco: la lesión persiste, MMR entra en ciclos fútiles, aparecen DSB y la célula muere. En el estudio de Hegi, la supervivencia mediana con RT + TMZ fue de 21,7 meses con promotor metilado frente a 12,7 meses sin metilar.
</details>

#### 5.12.2 ➕ Autoevaluación adicional

1. ¿Por qué el ADN contiene timina y no uracilo?
2. ¿Qué glicosilasa retira una base **no dañada**? ¿Cuál es esa base?
3. ¿Qué enzima corta el esqueleto en 5′ del sitio AP en BER?
4. ¿Qué dos actividades de Pol β se usan en BER de parche corto?
5. ¿Qué subvía de NER está alterada en el síndrome de Cockayne y por qué no hay más cáncer?
6. ¿Qué nucleasa corta en 5′ y cuál en 3′ en NER?
7. ¿Qué tamaño tiene el fragmento escindido en NER?
8. ¿Cómo distingue MMR la hebra nueva en eucariotas? ¿Y en *E. coli*?
9. ¿Qué proteína de MutLα tiene la actividad endonucleasa?
10. En un CCR con pérdida de MLH1 y PMS2, ¿qué dos estudios moleculares descartan un origen esporádico?
11. ¿Qué complejo protege los extremos de una DSB y favorece NHEJ?
12. ¿Qué proteína carga RAD51 sobre el ADN monocatenario?
13. ¿Por qué la deficiencia de RAG no es radiosensible y la de Artemis sí?
14. ¿Qué modificación de FANCD2–FANCI activa la vía de Fanconi?
15. ¿Qué modificación de PCNA activa la TLS y cuál activa el cambio de molde?
16. ¿Por qué un tumor MMR deficiente es resistente a la temozolomida?
17. ¿Qué mutación de TP53 deja la aflatoxina y en qué tumor?
18. ¿Qué indica una firma mutacional dominada por C>A en un CCR de un paciente con poliposis?

<details>
<summary>Respuestas</summary>

1. Porque la desaminación de C produce U: si el ADN no usa U, todo U es reconocible como daño (UNG lo retira sin ambigüedad).
2. **MUTYH**, que retira la **adenina** mal apareada frente a 8-oxoG.
3. **APE1**.
4. Polimerasa (inserta 1 nt) y **dRP-liasa** (retira el 5′-desoxirribosa-fosfato).
5. **TC-NER**. GG-NER funciona, así que el genoma se repara y no se acumulan mutaciones; las células con la transcripción bloqueada mueren (neurodegeneración y envejecimiento en lugar de cáncer).
6. **XPF–ERCC1 en 5′** y **XPG en 3′**.
7. **24–32 nucleótidos**.
8. Eucariotas: **mellas de la hebra nueva** (fragmentos de Okazaki) y **orientación de PCNA**. *E. coli*: **hemimetilación de GATC** (Dam); MutH corta la hebra no metilada.
9. **PMS2**.
10. **BRAF V600E** e **hipermetilación del promotor de MLH1**.
11. **53BP1–RIF1–shieldina** (con Ku).
12. **BRCA2** (con PALB2).
13. RAG solo corta en la V(D)J; Artemis además repara DSB accidentales por NHEJ.
14. La **monoubiquitinación** (por el complejo central; FANCL es la E3).
15. **Monoubiquitinación** (K164, RAD6–RAD18) → TLS. **Poliubiquitinación** (K63) → cambio de molde, sin error.
16. Porque la muerte por O⁶-meG requiere los **ciclos fútiles de MMR**. Sin MMR, la lesión se tolera.
17. **R249S** (G→T en el codón 249), en el **carcinoma hepatocelular**.
18. Un defecto del **sistema GO**: **poliposis asociada a MUTYH** (transversiones G:C→T:A, firma SBS36).
</details>

---

### 5.13 Trampas de examen

| ⚠️ Trampa | Lo correcto |
|---|---|
| "MUTYH retira la 8-oxoG" | MUTYH retira la **A** frente a 8-oxoG. Quien retira la 8-oxoG (frente a C) es **OGG1** |
| "La metilación de MGMT es mala para el paciente" | La metilación del **promotor** de MGMT silencia el gen y es **buena**: predice respuesta a temozolomida |
| "MGMT es una enzima catalítica" | Es **suicida/estequiométrica**: una molécula, una lesión |
| "Los humanos revierten los dímeros con fotoliasa" | Los mamíferos placentarios **no** tienen fotoliasa; usamos **NER** |
| "XPV es un defecto de NER" | XPV es un defecto de **TLS** (Pol η, POLH); NER es normal |
| "Cockayne predispone al cáncer de piel" | Cockayne y TTD **no** aumentan el cáncer de piel; XP sí |
| "Pérdida de MLH1 en IHQ = Lynch" | Lo más frecuente es la **hipermetilación esporádica de MLH1** (con BRAF V600E). Hay que descartarla |
| "Pérdida de MSH6 aislada = MSH2 mutado" | La pérdida aislada de MSH6 sugiere **MSH6**. La de MSH2 **arrastra** a MSH6, no al revés |
| "Lynch es recesivo porque el tumor necesita dos golpes" | La **predisposición** se hereda de forma **dominante**; el segundo golpe es somático |
| "La HR funciona en G1" | La HR necesita la **cromátida hermana**: S y G2. En G1 y en neuronas se usa **NHEJ** |
| "NHEJ es exacta" | NHEJ **no usa molde** y deja pequeñas indels |
| "Toda SCID T−B−NK+ es radiosensible" | La de **RAG** no; la de **Artemis, LIG4, XLF y DNA-PKcs** sí |
| "En A-T aparecen primero las telangiectasias" | Suele aparecer primero la **ataxia** (1–4 años); las telangiectasias, después de los 3–5 años |
| "La TLS repara la lesión" | La TLS **tolera** la lesión: la salta para seguir replicando |
| "Los inhibidores de PARP actúan solo por falta de reparación de SSB" | El efecto clave es el **atrapamiento de PARP** en el ADN, que se convierte en DSB al replicar |
| "Los tumores con MMR deficiente responden mejor a temozolomida" | Son **resistentes** a la temozolomida, pero **sensibles a anti-PD-1** |
| "El cisplatino daña sobre todo mediante enlaces intercatenarios" | ~90 % de sus aductos son **intracatenarios** (NER); los ICL son pocos, pero muy tóxicos |
| "La AFP alta descarta A-T en un lactante" | La AFP es fisiológicamente alta en el lactante; se interpreta mejor después de los 2 años |

---

### 5.14 Mnemotecnias

| Tema | Mnemotecnia |
|---|---|
| Purinas | **"PURA Agua y Gas"** → PURinas = A, G |
| Transición o transversión | Transición = te quedas en el mismo barrio (purina↔purina). Transversión = cambias de versión |
| Sensores y cinasas | **ATR ↔ RPA** (las dos con R; R de estrés Replicativo). **ATM ↔ MRN** (las dos con M) |
| Efectores | La **M** tiene **2 jorobas** → ATM–**CHK2**. La **R** tiene **1 bucle** → ATR–**CHK1** |
| Pasos de BER | **"Gloria Aprende Bien a Leer"**: Glicosilasa → APE1 → Pol β → Ligasa (XRCC1–LIG3) |
| Sistema GO | **"O-M-M"**: **O**GG1 quita la **O**xoG; **M**UTYH quita la A (**M**al puesta); **M**TH1 limpia el **M**ercado (pool) de nucleótidos |
| Incisiones en NER | **F antes que G** en el alfabeto = **5′ antes que 3′**: XPF corta en 5′, XPG en 3′ |
| ERCC y XP | **"4-F, 5-G"** seguidos; **"2-D, 3-B"** cruzados; **"6 y 8, Cockayne"** (CSB y CSA) |
| GG frente a TC | **G**lobal → **G**enoma entero → cáncer. **T**ranscripción → **T**ejido nervioso y envejecimiento |
| MMR | **MutS "Sensa"**, **MutL "Lanza el corte"** (PMS2). **MSH2 es el socio de todos** (6 y 3) |
| Ámsterdam II | **3-2-1**: 3 familiares, 2 generaciones, 1 antes de los 50 |
| HR | **"BRCA1 abre, BRCA2 carga"** (resección / RAD51). PALB2 es el puente |
| Elección de vía de DSB | **"53BP1 protege, BRCA1 resecciona"** |
| SCID por Artemis | **"Artemis, la arquera, abre las horquillas"** (hairpins de V(D)J) |
| A-T | **"ATAXIA"** = **A**taxia, **T**elangiectasias, **A**FP alta, **X** (rayos X: radiosensibilidad), **I**nmunodeficiencia (IgA), **A**umento de linfomas/leucemias |
| PCNA | **"Mono monta otra polimerasa; Poli pide la hermana"** (TLS frente a cambio de molde) |
| Riesgo de BRCA | Mama: los dos ~70 %. Ovario: **BRCA1 44 % ≫ BRCA2 17 %** |

---

### 5.15 Glosario

| Término | Definición |
|---|---|
| **Aducto** | Molécula unida covalentemente al ADN (p. ej., BPDE–guanina, cisplatino–guanina) |
| **AID** | Desaminasa inducida por activación: convierte C en U en los genes de inmunoglobulina del linfocito B |
| **APE1** | AP-endonucleasa 1: corta el esqueleto en 5′ del sitio AP en BER |
| **Base flipping** | Volteo de la base dañada fuera de la hélice para que la glicosilasa la procese |
| **Bucle D** (*D-loop*) | Estructura que se forma cuando la hebra resecada invade la doble hélice homóloga en la HR |
| **CPD** | Dímero de pirimidina ciclobutano, la principal lesión UV |
| **DDR** | Respuesta al daño del ADN: sensores, transductores y efectores |
| **dMMR / pMMR** | MMR deficiente o conservado (*proficient*) |
| **DSB / SSB** | Rotura de doble cadena / rotura de cadena sencilla |
| **Firma mutacional** | Patrón de mutaciones característico de un proceso de daño o de un defecto de reparación |
| **Glicosilasa** | Enzima que rompe el enlace N-glicosídico y retira una base dañada (inicia BER) |
| **γH2AX** | Histona H2AX fosforilada en Ser139 alrededor de una DSB |
| **HRD / BRCAness** | Deficiencia de recombinación homóloga, con o sin mutación de BRCA |
| **ICL** | Enlace cruzado intercatenario: une las dos hebras |
| **Letalidad sintética** | Dos defectos tolerables por separado que juntos son letales |
| **Mella** (*nick*) | Rotura de un enlace fosfodiéster en una sola hebra |
| **Microsatélite** | Repetición en tándem de 1–6 pb, propensa al deslizamiento de la polimerasa |
| **MSI-H** | Inestabilidad de microsatélites alta, la huella de dMMR |
| **Neoantígeno** | Péptido mutado que el sistema inmune reconoce como extraño |
| **PARilación** | Adición de cadenas de poli(ADP-ribosa) a partir de NAD⁺, catalizada por PARP |
| **PCNA** | Abrazadera deslizante de la replicación; su ubiquitinación decide entre TLS y cambio de molde |
| **PIKK** | Familia de cinasas relacionadas con PI3K: ATM, ATR, DNA-PKcs |
| **Resección** | Degradación 5′→3′ de los extremos de una DSB para generar colas 3′ monocatenarias (inicia la HR) |
| **Reversión** (mutación de) | Segunda mutación que restaura el marco de lectura de BRCA1/2 y causa resistencia |
| **SDSA** | *Synthesis-dependent strand annealing*: resolución de la HR sin entrecruzamiento |
| **Shieldina** | Complejo efector de 53BP1–RIF1 que protege los extremos de la resección |
| **Sitio AP** | Sitio apurínico/apirimidínico: azúcar sin base |
| **TFIIH** | Complejo con helicasas XPB y XPD; factor de transcripción y pieza central de NER |
| **TLS** | Síntesis translesión: polimerasas especializadas copian frente a la lesión sin repararla |
| **Transición / transversión** | Cambio purina↔purina o pirimidina↔pirimidina / cambio purina↔pirimidina |
| **TREC** | Círculos de escisión del receptor T; marcador de V(D)J usado en el tamizaje neonatal de SCID |
| **V(D)J** | Recombinación somática que genera la diversidad de receptores B y T; requiere RAG y NHEJ |

---

### 5.16 Plan de estudio y cómo usar el mazo de Anki

#### 5.16.1 Plan sugerido (5 sesiones)

| Sesión | Contenido | Tarjetas nuevas |
|---|---|---|
| 1 | Secciones 5.1–5.2 (prerrequisitos, daño, DDR, mapa) | Subdecks 00–01 |
| 2 | Secciones 5.3–5.4 (reversión directa y BER) | Subdecks 02–03 |
| 3 | Sección 5.5 (NER, XP, Cockayne, TTD, cisplatino) | Subdeck 04 |
| 4 | Secciones 5.6–5.7 (MMR, Lynch, inmunoterapia, DSB, BRCA, A-T) | Subdecks 05–06 |
| 5 | Secciones 5.8–5.10 y casos (Fanconi, TLS, integración) | Subdecks 07–10 |

Lee la sección **antes** de estudiar sus tarjetas nuevas: Anki sirve para **retener**, no para aprender por primera vez.

#### 5.16.2 El submazo *05 Reparación del ADN*

**Dónde está**: dentro de [`Genetica_Biologia_Molecular.apkg`](Genetica_Biologia_Molecular.apkg), el mazo único de la guía.

**Importar**: en Anki de escritorio, *Archivo → Importar* y elige el `.apkg` (o ábrelo con doble clic). En AnkiDroid y AnkiMobile, abre el archivo desde la app.

**Estructura**: el submazo **05 Reparación del ADN** del mazo *Genética y Biología Molecular (UNAL 2026)*, con subdecks numerados que siguen este capítulo:

```
Genética y Biología Molecular (UNAL 2026)::05 Reparación del ADN
├── 00 · Fundamentos
├── 01 · Daño del ADN y DDR
├── 02 · Reversión directa
├── 03 · BER
├── 04 · NER
├── 05 · MMR
├── 06 · Roturas de doble cadena (NHEJ · HR)
├── 07 · Fanconi y enlaces cruzados
├── 08 · Tolerancia al daño (TLS)
├── 09 · Integración clínica y terapias
└── 10 · Casos clínicos
```

**Tipos de tarjeta**:
- **Pregunta/Respuesta**: con un recuadro de *"Por qué"* para entender, no solo recordar, y mnemotecnias cuando existen.
- **Cloze** (completar): para datos atómicos y secuencias de pasos; cada hueco es una tarjeta distinta.
- **Caso clínico**: viñeta breve + pregunta + razonamiento + perla.
- Cada tarjeta indica su **fuente** (número de diapositiva o referencia). El color del encabezado identifica la vía, y las tarjetas de "mapa" y de casos usan un encabezado neutro para no revelar la respuesta.

**Etiquetas útiles** (filtra en el Explorador):

| Etiqueta | Para qué sirve |
|---|---|
| `ReparacionADN::fuente::clase` | Solo el contenido de las diapositivas |
| `ReparacionADN::fuente::ampliacion` | Lo añadido en esta guía; suspéndelo si solo quieres lo de la clase |
| `ReparacionADN::HY` | Alto rendimiento (lo más preguntado) |
| `ReparacionADN::tipo::dato_numerico` | Cifras; suspéndelas si tu examen no pide números |
| `ReparacionADN::tipo::clinica`, `::farmaco`, `::mecanismo`, `::caso` | Repaso por tipo de contenido |

**Ajustes recomendados** (*Opciones del mazo*):
- Activa **FSRS** con una retención deseada de **0,90**.
- **Nuevas por día: 20–30.** Este submazo tiene 366 tarjetas: a 25 por día terminas las nuevas en unos 15 días. Si tienes examen pronto, sube a 40–50.
- Activa **"Enterrar tarjetas hermanas"** (nuevas y de repaso), para no ver juntos los huecos de un mismo cloze.
- Orden de nuevas: **"Mazo"**, para respetar el orden pedagógico (fundamentos → vías → clínica).
- No borres tarjetas que te parezcan fáciles: déjalas, y Anki las espaciará solo.

---

### 5.17 Bibliografía

#### De la clase *(Diap. 49–50)*

**Textos y revisiones**
1. Alberts B, et al. *Molecular Biology of the Cell*. 7.ª ed. W. W. Norton; 2022. Cap. 5.
2. Lodish H, et al. *Molecular Cell Biology*. 9.ª ed. W. H. Freeman/Macmillan; 2021.
3. Nussbaum RL, McInnes RR, Willard HF. *Thompson & Thompson Genetics in Medicine*. 8.ª ed. Elsevier; 2016.
4. Lindahl T. Instability and decay of the primary structure of DNA. *Nature*. 1993;362:709–715.
5. Hoeijmakers JHJ. DNA damage, aging, and cancer. *N Engl J Med*. 2009;361:1475–1485.
6. Jackson SP, Bartek J. The DNA-damage response in human biology and disease. *Nature*. 2009;461:1071–1078.
7. Chatterjee N, Walker GC. Mechanisms of DNA damage, repair, and mutagenesis. *Environ Mol Mutagen*. 2017;58:235–263.
8. Tubbs A, Nussenzweig A. Endogenous DNA damage as a source of genomic instability in cancer. *Cell*. 2017;168:644–656.
9. Krokan HE, Bjørås M. Base excision repair. *Cold Spring Harb Perspect Biol*. 2013;5:a012583.
10. Marteijn JA, et al. Understanding nucleotide excision repair and its roles in cancer and ageing. *Nat Rev Mol Cell Biol*. 2014;15:465–481.
11. Jiricny J. The multifaceted mismatch-repair system. *Nat Rev Mol Cell Biol*. 2006;7:335–346.
12. Scully R, et al. DNA double-strand break repair-pathway choice in somatic mammalian cells. *Nat Rev Mol Cell Biol*. 2019;20:698–714.
13. Kottemann MC, Smogorzewska A. Fanconi anaemia and the repair of Watson and Crick DNA crosslinks. *Nature*. 2013;493:356–363.
14. Lord CJ, Ashworth A. PARP inhibitors: synthetic lethality in the clinic. *Science*. 2017;355:1152–1158.
15. The Nobel Prize in Chemistry 2015. NobelPrize.org.

**Estudios de los ejemplos clínicos**
16. Hegi ME, et al. MGMT gene silencing and benefit from temozolomide in glioblastoma. *N Engl J Med*. 2005;352:997–1003.
17. Al-Tassan N, et al. Inherited variants of MYH associated with somatic G:C→T:A mutations in colorectal tumors. *Nat Genet*. 2002;30:227–232.
18. Imai K, et al. Human uracil–DNA glycosylase deficiency associated with profoundly impaired immunoglobulin class-switch recombination. *Nat Immunol*. 2003;4:1023–1028.
19. DiGiovanna JJ, Kraemer KH. Shining a light on xeroderma pigmentosum. *J Invest Dermatol*. 2012;132:785–796.
20. Bradford PT, et al. Cancer and neurologic degeneration in xeroderma pigmentosum. *J Med Genet*. 2011;48:168–176.
21. Köberle B, et al. Defective repair of cisplatin-induced DNA damage caused by reduced XPA protein in testicular germ cell tumours. *Curr Biol*. 1999;9:273–276.
22. Olaussen KA, et al. DNA repair by ERCC1 in non-small-cell lung cancer and cisplatin-based adjuvant chemotherapy. *N Engl J Med*. 2006;355:983–991.
23. Lynch HT, de la Chapelle A. Hereditary colorectal cancer. *N Engl J Med*. 2003;348:919–932.
24. Le DT, et al. PD-1 blockade in tumors with mismatch-repair deficiency. *N Engl J Med*. 2015;372:2509–2520.
25. André T, et al. Pembrolizumab in microsatellite-instability-high advanced colorectal cancer. *N Engl J Med*. 2020;383:2207–2218.
26. Moshous D, et al. Artemis, a novel DNA double-strand break repair/V(D)J recombination protein, is mutated in human severe combined immune deficiency. *Cell*. 2001;105:177–186.
27. Li L, et al. A founder mutation in Artemis causes SCID in Athabascan-speaking Native Americans. *J Immunol*. 2002;168:6323–6329.
28. Kuchenbaecker KB, et al. Risks of breast, ovarian, and contralateral breast cancer for BRCA1 and BRCA2 mutation carriers. *JAMA*. 2017;317:2402–2416.
29. Rothblum-Oviatt C, et al. Ataxia telangiectasia: a review. *Orphanet J Rare Dis*. 2016;11:159.
30. Howlett NG, et al. Biallelic inactivation of BRCA2 in Fanconi anemia. *Science*. 2002;297:606–609.
31. Masutani C, et al. The XPV gene encodes human DNA polymerase η. *Nature*. 1999;399:700–704.
32. Farmer H, et al. Targeting the DNA repair defect in BRCA mutant cells as a therapeutic strategy. *Nature*. 2005;434:917–921.
33. Bryant HE, et al. Specific killing of BRCA2-deficient tumours with inhibitors of poly(ADP-ribose) polymerase. *Nature*. 2005;434:913–917.
34. Robson M, et al. Olaparib for metastatic breast cancer in patients with a germline BRCA mutation. *N Engl J Med*. 2017;377:523–533.

#### ➕ Referencias de las ampliaciones
35. Møller P, et al. Cancer risk and survival in path_MMR carriers by gene and gender up to 75 years of age: a report from the Prospective Lynch Syndrome Database. *Gut*. 2018;67:1306–1316.
36. Cercek A, et al. PD-1 blockade in mismatch repair–deficient, locally advanced rectal cancer. *N Engl J Med*. 2022;386:2363–2376.
37. Cercek A, et al. Nonoperative management of mismatch repair–deficient tumors. *N Engl J Med*. 2025;392:2297–2308. Resumen de resultados: [ACS Brief, julio 2025](https://www.facs.org/for-medical-professionals/news-publications/news-and-articles/acs-brief/july-15-2025-issue/is-neoadjuvant-checkpoint-blockade-sufficient-to-treat-mismatch-repair-deficient-rectal-cancer/).
38. Moore K, et al. Maintenance olaparib in patients with newly diagnosed advanced ovarian cancer (SOLO-1). *N Engl J Med*. 2018;379:2495–2505.
39. Tutt ANJ, et al. Adjuvant olaparib for patients with BRCA1- or BRCA2-mutated breast cancer (OlympiA). *N Engl J Med*. 2021;384:2394–2405.
40. Golan T, et al. Maintenance olaparib for germline BRCA-mutated metastatic pancreatic cancer (POLO). *N Engl J Med*. 2019;381:317–327.
41. Alexandrov LB, et al. The repertoire of mutational signatures in human cancer. *Nature*. 2020;578:94–101. Catálogo actualizado: [COSMIC Mutational Signatures](https://cancer.sanger.ac.uk/signatures/).
42. Bunting SF, et al. 53BP1 inhibits homologous recombination in Brca1-deficient cells by blocking resection of DNA breaks. *Cell*. 2010;141:243–254.
43. Hira A, et al. Variant ALDH2 is associated with accelerated progression of bone marrow failure in Japanese Fanconi anemia patients. *Blood*. 2013;122:3206–3209.

---

*Guía elaborada como material de estudio a partir de la clase indicada. Las cifras de riesgo y de los ensayos son aproximadas y pueden cambiar con nuevas series; para decisiones clínicas consulta siempre las guías vigentes.*

[↑ Volver al índice general](#índice-general)

---

## 6. Genética del cáncer: biología molecular, hallmarks y perspectivas terapéuticas

> Clase de la Prof. **Sandra Yaneth Ospina Lagos** (MD, MSc), Departamento de Genética Humana y Ciencias Biomédicas, Facultad de Medicina, Universidad Nacional de Colombia, 2026. La clase se basa en Hanahan y Weinberg (*Cell* 2000 y 2011) y en Hanahan (*Cancer Discovery* 2022).
> Las citas *(Diap. N)* siguen la numeración del PDF de la clase. Los símbolos 📌 ➕ ⚠️ ✅ 🩺 💊 🧠 se explican al [inicio de la guía](#cómo-usar-esta-guía).
> Se apoya en el [capítulo 3, ciclo celular](#3-ciclo-celular-fases-motor-molecular-y-puntos-de-control) (Rb, p53, CDK4/6, SAC) y en el [capítulo 5, reparación del ADN](#5-mecanismos-de-reparación-del-adn-de-la-lesión-molecular-a-la-clínica) (MMR, BRCA, PARP). Las técnicas que aparecen aquí (FISH, PCR, NGS) se explican en el [capítulo 7](#7-técnicas-de-biología-molecular).

---

### Índice (capítulo 6)

- [Objetivos de aprendizaje](#objetivos-de-aprendizaje-capítulo-6-diap-2)
- [Lo esencial en un minuto](#lo-esencial-en-un-minuto-capítulo-6)
- [6.1 Historia del cáncer](#61-historia-del-cáncer-diap-34)
- [6.2 ¿Qué es el cáncer?](#62-qué-es-el-cáncer-diap-56)
- [6.3 Los genes del cáncer](#63-los-genes-del-cáncer-diap-8-14)
- [6.4 Cómo se activa un oncogén](#64-cómo-se-activa-un-oncogén-diap-9)
- [6.5 Genes supresores y la hipótesis de los dos golpes](#65-genes-supresores-y-la-hipótesis-de-los-dos-golpes-diap-10)
- [6.6 El ciclo celular alterado en el cáncer](#66-el-ciclo-celular-alterado-en-el-cáncer-diap-12)
- [6.7 Mutaciones driver y passenger](#67-mutaciones-driver-y-passenger-diap-13)
- [6.8 Evolución clonal e inestabilidad genómica](#68-evolución-clonal-e-inestabilidad-genómica-diap-1516-26)
- [6.9 El modelo de los hallmarks: 2000, 2011 y 2022](#69-el-modelo-de-los-hallmarks-2000-2011-y-2022-diap-1718)
- [6.10 Señalización proliferativa sostenida](#610-señalización-proliferativa-sostenida-diap-19)
- [6.11 Evasión de los supresores de crecimiento](#611-evasión-de-los-supresores-de-crecimiento-diap-20)
- [6.12 Resistencia a la muerte celular](#612-resistencia-a-la-muerte-celular-diap-21)
- [6.13 Inmortalidad replicativa](#613-inmortalidad-replicativa-diap-22)
- [6.14 Inflamación promotora de tumores](#614-inflamación-promotora-de-tumores-diap-2223)
- [6.15 Inducción o acceso a la vasculatura](#615-inducción-o-acceso-a-la-vasculatura-diap-24)
- [6.16 Reprogramación metabólica](#616-reprogramación-metabólica-diap-24)
- [6.17 Evasión de la destrucción inmune](#617-evasión-de-la-destrucción-inmune-diap-25)
- [6.18 Invasión y metástasis](#618-invasión-y-metástasis-diap-26)
- [6.19 Las cuatro nuevas dimensiones de 2022](#619-las-cuatro-nuevas-dimensiones-de-2022-diap-2730)
- [6.20 Epidemiología mundial](#620-epidemiología-mundial-diap-3135)
- [6.21 Epidemiología en Colombia](#621-epidemiología-en-colombia-diap-3639)
- [6.22 De los hallmarks a los fármacos](#622-de-los-hallmarks-a-los-fármacos-diap-41)
- [6.23 Medicina personalizada](#623-medicina-personalizada-diap-42)
- [6.24 Síntesis: el modelo multietapa](#624-síntesis-el-modelo-multietapa-diap-4445)
- [6.25 Las preguntas de la clase, resueltas](#625-las-preguntas-de-la-clase-resueltas-diap-48)
- [6.26 ➕ Síndromes de cáncer hereditario](#626--síndromes-de-cáncer-hereditario)
- [✅ Verificación de datos de la clase](#-verificación-de-datos-de-la-clase-capítulo-6)
- [Autoevaluación](#autoevaluación-capítulo-6)
- [Glosario](#glosario-capítulo-6)
- [Referencias](#referencias-capítulo-6)

---

### Objetivos de aprendizaje (capítulo 6) *(Diap. 2)*

1. **Recorrer la historia** del cáncer y **definirlo** desde la clínica, la biología molecular y la genómica.
2. **Diferenciar** oncogenes, genes supresores de tumores, genes de reparación y microARN, y explicar **cómo se alteran**.
3. **Relacionar** el ciclo celular, las mutaciones *driver* y *passenger* y la evolución clonal.
4. **Describir los hallmarks** (Hanahan y Weinberg 2000 y 2011) y las **cuatro dimensiones nuevas** de 2022.
5. **Interpretar** la epidemiología mundial y colombiana.
6. **Conectar** cada hallmark con terapias aprobadas y con la medicina personalizada.

---

### Lo esencial en un minuto (capítulo 6)

1. **El cáncer es una enfermedad genética y epigenética de las células somáticas, de varias etapas**: se acumulan alteraciones en genes que controlan la proliferación, la muerte celular, la señalización y la reparación del ADN, a lo largo de años o décadas. No es una sola enfermedad, sino más de cien con rasgos comunes (los hallmarks).
2. **Oncogén = acelerador atascado**: ganancia de función; basta **un alelo** alterado. Se activa por **mutación puntual** (*KRAS* G12D), **amplificación** (*ERBB2*, *MYCN*), **translocación** (*BCR-ABL1*) o **captura de un *enhancer*** (*IGH*-*MYC*).
3. **Gen supresor = freno roto**: pérdida de función; hacen falta **dos golpes** (Knudson, 1971). **Gatekeepers** (*RB1*, *TP53*, *APC*) frenan el crecimiento; **caretakers** (*BRCA1/2*, genes MMR) cuidan el genoma.
4. **Retinoblastoma hereditario**: primer golpe germinal → tumores **bilaterales, múltiples y más tempranos**. **Esporádico**: dos golpes somáticos → **unilateral, único y más tardío** (aun así, en la infancia).
5. **Drivers** (2–8 por tumor) dan ventaja selectiva. **Passengers** (la gran mayoría) no la dan, pero dejan **firmas mutacionales**: SBS1 (edad), SBS4 (tabaco), SBS2/13 (APOBEC), SBS6 (MMR defectuoso).
6. **Inestabilidad genómica**: **CIN** (aneuploidía), **MSI** (MMR defectuoso; alta carga mutacional → respuesta a pembrolizumab), **POLE/POLD1** (ultramutador) y reordenamientos catastróficos (**cromotripsis, cromoplexia**).
7. **Hallmarks**: 6 en 2000 + 2 emergentes en 2011 = **8 capacidades**, más **2 características habilitantes** (inestabilidad genómica e inflamación). En 2022 se suman **plasticidad fenotípica, reprogramación epigenética no mutacional, microbiomas polimórficos y células senescentes**. La figura de 2022 tiene **14 elementos**.
8. **VHL–HIF–VEGF**: con oxígeno, la PHD hidroxila a HIF-1α y VHL lo envía al proteasoma. En hipoxia, o si falta VHL, HIF activa VEGF: **switch angiogénico**.
9. **Efecto Warburg**: glucólisis aeróbica aun con oxígeno. Produce poco ATP, pero aporta carbonos y NADPH para fabricar células nuevas. ***IDH1/2* mutada → 2-hidroxiglutarato**, un oncometabolito que hipermetila el genoma.
10. **Inmunoedición**: eliminación → equilibrio → escape. El tumor escapa con PD-L1, pérdida de MHC-I, Treg y MDSC, IDO1 y TGF-β.
11. **Epidemiología**: GLOBOCAN 2024 (julio de 2026) estima **20,6 millones de casos y 9,8 millones de muertes**; el pulmón es el más frecuente y el más letal. **Colombia (2024)**: ~**123.000 casos** y ~**56.000 muertes**; mama y próstata lideran la incidencia, y el estómago, la mortalidad.
12. **Cada hallmark tiene fármacos**: imatinib (BCR-ABL), osimertinib (EGFR), trastuzumab (HER2), sotorasib (KRAS G12C), palbociclib (CDK4/6), venetoclax (BCL-2), olaparib (PARP, letalidad sintética en *BRCA*), bevacizumab (VEGF), ivosidenib (IDH1), pembrolizumab (PD-1), ATRA (APL) y CAR-T (CD19, BCMA).

---

### 6.1 Historia del cáncer *(Diap. 3–4)*

| Época | Quién o qué | Aporte |
|---|---|---|
| **~1600 a. C.** | **Papiro de Edwin Smith** | Primera referencia científica y objetiva al cáncer. Lo conserva la Academia de Medicina de Nueva York. ➕ Describe masas abultadas de la mama y concluye que "no tienen tratamiento" |
| **460–370 a. C.** | **Hipócrates** | Acuñó ***karkinos*** y ***karkinoma*** (cangrejo); describió tumores avanzados no tratados. ➕ Celso tradujo el término al latín como *cancer*, y Galeno usó *onkos* (masa), de donde viene "oncología" |
| **1728–1793** | **John Hunter** | Propuso operar los tumores **"móviles"**, no adheridos a los tejidos vecinos |
| **1821–1902** | **Rudolf Virchow** | Fundador de la **patología celular**: las células cancerosas provienen de otras células (***omnis cellula e cellula***) |
| **Finales del siglo XIX** | Radioterapia | ➕ Röntgen describe los rayos X en 1895; al año siguiente ya se usaban contra tumores |
| **Segunda Guerra Mundial** | **Mostazas nitrogenadas** | Los expuestos al gas mostaza tenían leucopenia. **Goodman y Gilman** (Yale, 1942) probaron mostazas nitrogenadas en **linfomas**: nace la **quimioterapia** |
| **1970 a hoy** | Era molecular | Los **retrovirus de transformación aguda** llevan al descubrimiento de los **oncogenes**; **hipótesis de dos golpes** (Knudson, 1971); **hallmarks** (2000, 2011, 2022) |

- ✅ La diapositiva dice "años 50: terapias dirigidas iniciales". En los años 50 se desarrollaron antimetabolitos y la quimioterapia combinada. Las terapias dirigidas modernas llegaron después: tamoxifeno (receptor de estrógenos, aprobado en 1977), trastuzumab (1998) e imatinib (2001).
- ➕ En 1976 **Bishop y Varmus** demostraron que el oncogén *src* del virus del sarcoma de Rous tiene una versión normal en las células sanas (un **proto-oncogén**). Nobel de 1989.

🧠 **"El papiro describe, Hipócrates nombra, Hunter opera, Virchow explica, la guerra trae la quimio y la genética trae los oncogenes."**

---

### 6.2 ¿Qué es el cáncer? *(Diap. 5–6)*

#### Cuatro pasos visibles *(Diap. 5, NCI)*

1. **Células normales**: crecen y se dividen de forma controlada.
2. **Células anormales**: se multiplican sin control.
3. **Invasión local**: atraviesan la membrana basal e invaden tejidos vecinos.
4. **Diseminación**: entran a la sangre o la linfa y forman tumores en otros órganos (**metástasis**: pulmón, hígado, hueso).

#### Tres definiciones complementarias *(Diap. 6)*

| Perspectiva | Definición |
|---|---|
| **Clínica** (NCI) | Enfermedades en las que células anormales **se multiplican sin control** y pueden **invadir** tejidos cercanos o **diseminarse** |
| **Molecular** | Resultado de la **acumulación de mutaciones somáticas y cambios epigenéticos** en genes del ciclo celular, la apoptosis, la señalización y la reparación del ADN. Proceso de **varias etapas** que toma **años o décadas** |
| **Genómica** | **Evolución clonal darwiniana**: se seleccionan las células con ventaja proliferativa. La **heterogeneidad intratumoral** impulsa la progresión y la resistencia. La acumulación de mutaciones **precede** a los cambios morfológicos |

📌 El cáncer **no es una sola enfermedad**: son muchas enfermedades con mecanismos distintos y rasgos fenotípicos compartidos (los hallmarks).

✅ La diapositiva 6 dice "más de 200 enfermedades" y la 35, "más de 100 trastornos". Las dos cifras circulan; el NCI habla de **más de 100 tipos**. La diferencia depende de cuánto se subdividan los tipos histológicos.

---

### 6.3 Los genes del cáncer *(Diap. 8, 14)*

| | **Proto-oncogenes → oncogenes** | **Genes supresores de tumores (TSG)** | **microARN** |
|---|---|---|---|
| Función normal | **Estimulan** la división celular | **Inhiben** la división o **promueven** la muerte celular | Regulan genes después de la transcripción |
| Alteración en cáncer | **Ganancia de función** | **Pérdida de función** | OncomiR sobreexpresado o miARN supresor perdido |
| Alelos necesarios | **Uno** (dominante a nivel celular) | **Los dos** (recesivo a nivel celular, dos golpes) | Variable |
| Ejemplos | *RAS*, *MYC*, *ERBB2*/HER2, *BCR-ABL1*, *EGFR*, *ALK*, *BRAF*, *RET* | *TP53*, *RB1*, *BRCA1/2*, *PTEN*, *APC*, *CDKN2A*, *NF1*, *NF2*, *VHL* | OncomiR: **miR-21, miR-155**. Supresores: **miR-34, miR-200** |

🧠 *(Diap. 14)* **El auto**: el proto-oncogén es el **acelerador** y el gen supresor es el **freno** (paracaídas). Oncogén = **demasiado acelerador**. Supresor inactivado = **sin freno**. En ambos casos el auto choca contra el muro del cáncer.

#### Oncogenes por familia *(Diap. 8)*

| Familia | Ejemplos | Qué hacen |
|---|---|---|
| **Receptores tirosina cinasa** | **EGFR** (MAPK, PI3K/AKT), **HER2/ERBB2** (proliferación epitelial), **RET/ALK** (fusiones con señalización constante) | Señal de crecimiento sin ligando |
| **Vías intracelulares** | **RAS** (MAPK/ERK activo), **BRAF V600E** | Transmiten la señal hacia el núcleo |
| **Factores de transcripción** | **MYC** (amplificación) | Encienden programas de crecimiento |
| **Genes de fusión** | **BCR-ABL** | Tirosina cinasa constitutiva; proliferación hematológica |

- RAS, BRAF y EGFR → **eje MAPK**, muy relevante en tumores epiteliales.
- ALK, RET y BCR-ABL → **tirosina cinasas de fusión**, clave en terapias dirigidas.
- MYC → **amplificación y desregulación transcripcional** en tumores agresivos.
- HER2 → **amplificación** en cáncer de mama y gástrico, con terapias muy eficaces.

#### Genes supresores: frenos en cinco niveles *(Diap. 8)*

| Nivel | Genes |
|---|---|
| Ciclo celular | *TP53*, *RB1*, *CDKN2A* |
| Reparación del ADN | *BRCA1/2* |
| Señalización proliferativa | *PTEN*, *NF1*, *NF2* |
| Microambiente y angiogénesis | *VHL* |
| Arquitectura tisular | *APC* (epitelio intestinal) |

➕ *NF1* codifica la neurofibromina, una **RAS-GAP**: sin ella, RAS queda unida a GTP. *PTEN* es la fosfatasa que **apaga la vía PI3K–AKT**.

#### microARN en el cáncer *(Diap. 8)*

- **miR-21 y miR-155 (oncomiR)**: silencian genes supresores (➕ miR-21 silencia a *PTEN* y *PDCD4*), y promueven inflamación, proliferación y evasión inmune. miR-21 está elevado en cáncer de pulmón y colon.
- **miR-34 y miR-200 (supresores)**: **miR-34 es inducido por p53** y ejecuta su programa antiproliferativo; **miR-200 reprime a ZEB1/ZEB2** y bloquea la transición epitelio-mesénquima (EMT) y la metástasis.
- Su desregulación es un eje epigenético de la progresión tumoral y una diana terapéutica emergente.

✅ La diapositiva dice que los oncomiR "regulan a la baja protooncogenes" y los supresores "regulan a la baja genes supresores". Es al revés: **un oncomiR silencia genes supresores** y **un miARN supresor silencia oncogenes**. La misma diapositiva lo dice bien unas líneas después (miR-21 y miR-155 "silencian supresores").

➕ Kinzler y Vogelstein describieron una tercera clase de supresores, los ***landscapers***, que alteran el microambiente del epitelio más que la célula misma (por ejemplo, *SMAD4* y *BMPR1A* en la poliposis juvenil).

---

### 6.4 Cómo se activa un oncogén *(Diap. 9)*

| # | Mecanismo | Qué pasa | Ejemplo | Cómo se detecta |
|---|---|---|---|---|
| 1 | **Variante puntual** | En la región codificante: proteína **hiperactiva** o resistente a la degradación | ***KRAS* G12D** (Gly→Asp): RAS no hidroliza bien el GTP y queda **constitutivamente activa** | PCR y secuenciación |
| 2 | **Amplificación génica** | Decenas o cientos de copias → **sobreexpresión** | ***ERBB2*/HER2** en cáncer de mama y gástrico; ***MYCN*** en neuroblastoma | **FISH** (e IHQ para la proteína HER2) |
| 3 | **Translocación cromosómica** | El gen queda junto a un promotor activo o se **fusiona** con otro gen | ***BCR-ABL1*** en la leucemia mieloide crónica: **cromosoma Filadelfia, t(9;22)** | Cariotipo, FISH, RT-PCR |
| 4 | **Captura de *enhancer*** | Un reordenamiento pone un *enhancer* muy activo junto al proto-oncogén | ***IGH*-*MYC*** en el linfoma de Burkitt, **t(8;14)** | Cariotipo, FISH |
| 5 | **Inserción viral** *(figura de la diapositiva)* | Un virus inserta su promotor fuerte junto al proto-oncogén | ➕ El virus de la leucosis aviar activa a *MYC*; en un ensayo de terapia génica de 2003 un vector retroviral activó *LMO2* y causó leucemia | — |

- ✅ La diapositiva da "MYC en neuroblastoma": el gen amplificado en el neuroblastoma es ***MYCN*** (N-MYC), marcador de mal pronóstico. *MYC* (c-MYC) es el de Burkitt.
- ✅ La diapositiva menciona HER2 en "rabdomiosarcoma". El ejemplo clásico de amplificación de *ERBB2* es el cáncer de mama (también gástrico y esofágico); en el rabdomiosarcoma alveolar se amplifican sobre todo *MYCN* y *CDK4*.
- ✅ El texto lista cuatro mecanismos y la figura cambia el cuarto por "inserción viral". Son cinco mecanismos distintos; conviene saberlos todos.

🧠 **"MATE-V"**: **M**utación puntual, **A**mplificación, **T**ranslocación, ***E**nhancer*, **V**irus.

⚠️ La t(14;18) del linfoma folicular usa el mismo truco (el *enhancer* de *IGH* junto a *BCL2*), pero *BCL2* no acelera la proliferación: **impide la apoptosis** (sección 6.12).

---

### 6.5 Genes supresores y la hipótesis de los dos golpes *(Diap. 10)*

📌 **Hipótesis de Knudson (1971)**: un gen supresor pierde su función solo cuando se inactivan **sus dos alelos**.

| | **Forma hereditaria** | **Forma esporádica** |
|---|---|---|
| Primer golpe | **Germinal** (en todas las células) | Somático |
| Segundo golpe | Somático | Somático |
| Edad | **Temprana** | **Más tardía** |
| Tumores | **Múltiples y bilaterales** | **Únicos y unilaterales** |
| Retinoblastoma (*RB1*) | Bilateral, en lactantes | Unilateral, en niños algo mayores |

✅ La diapositiva dice "esporádico: retinoblastoma unilateral **adultos**". El retinoblastoma es un tumor de la **infancia** en ambas formas: el hereditario se diagnostica en promedio hacia el primer año de vida y el esporádico unilateral, hacia los dos años.

➕ Cerca del **40 %** de los retinoblastomas son hereditarios. Estos pacientes tienen además más riesgo de **osteosarcoma** y otros sarcomas. El segundo golpe suele ser una **pérdida de heterocigosidad (LOH)**: deleción, recombinación mitótica o pérdida del cromosoma con el alelo normal. También puede ser la **metilación del promotor**.

⚠️ **La predisposición se hereda como autosómica dominante, pero a nivel celular el gen es recesivo**: la persona hereda un alelo inactivo y el tumor aparece cuando se pierde el segundo.

#### Gatekeepers y caretakers *(Diap. 8, 10)*

| | **Gatekeepers ("porteros")** | **Caretakers ("cuidadores")** |
|---|---|---|
| Función | Inhiben directamente el crecimiento o inducen la muerte celular | Reparan el daño del ADN y mantienen la integridad del genoma |
| Ejemplos | **p53, RB** (➕ y *APC*) | ***BRCA1/2*, *MLH1*, *MSH2*** |
| Al perderse | La célula prolifera | **Inestabilidad genómica** → se acumulan mutaciones en los gatekeepers |

#### Cánceres familiares que revelaron genes supresores *(Diap. 10, tabla 19.5 de Strachan y Read)*

| Enfermedad | Gen | Locus |
|---|---|---|
| Poliposis adenomatosa familiar | *APC* | 5q21 |
| Síndrome de Lynch | *MSH2* / *MLH1* | 2p21 / 3p21.3 |
| Cáncer de mama y ovario | *BRCA1* | 17q21 |
| Cáncer de mama de inicio temprano | *BRCA2* | 13q13.1 |
| Síndrome de Li-Fraumeni | *TP53* | 17p13 |
| Síndrome de Gorlin (nevo basocelular) | *PTCH1* | 9q22.3 |
| Ataxia-telangiectasia | *ATM* | 11q22.3 |
| Retinoblastoma | *RB1* | 13q14 |
| Neurofibromatosis 1 (von Recklinghausen) | *NF1* | 17q11.2 |
| Neurofibromatosis 2 (schwannomas vestibulares) | *NF2* | 22q12.2 |
| Melanoma familiar | *CDKN2A* | 9p21 |
| Von Hippel-Lindau | *VHL* | 3p25.3 |

➕ Todos se heredan de forma autosómica dominante, salvo la ataxia-telangiectasia (autosómica recesiva). La sección [6.26](#626--síndromes-de-cáncer-hereditario) los resume con sus tumores.

---

### 6.6 El ciclo celular alterado en el cáncer *(Diap. 12)*

Repaso (detalle en el [capítulo 3](#38-el-motor-cdk-y-ciclinas-diap-2226)):

| Fase | Motor | Qué pasa |
|---|---|---|
| **G1** | **Ciclina D–CDK4/6** | Crecimiento; Rb fosforilado libera E2F |
| **S** | **Ciclina E/A–CDK2** | Síntesis de ADN, replicación controlada |
| **G2** | **Ciclina B–CDK1** (se prepara) | ATM/ATR vigilan; punto de control G2/M |
| **M** | **Ciclina B–CDK1** | Mitosis; el SAC verifica la alineación |

**Puntos de control**: G1/S (**p53 → p21 → inhibe CDK2**), G2/M (**ATM/ATR → CHK1/2 → CDC25C**) y huso (**BUBR1, MAD2**).

| Alteración | Consecuencia |
|---|---|
| ***TP53* mutado** (~50 % de los cánceres) | Falla el punto de control G1/S → se acumulan mutaciones |
| ***RB1* perdido** | E2F queda libre siempre → entrada forzada en S |
| ***CDKN2A* (p16) silenciado** por metilación o deleción | CDK4/6 sin freno → proliferación |
| ***CCND1* amplificado** | Exceso de ciclina D → CDK4/6 hiperfosforilan a Rb |

✅ La diapositiva dice "RB1 perdido: CDK4/6 activos constitutivamente". Si falta Rb, la actividad de CDK4/6 deja de importar: **E2F ya está libre sin necesidad de fosforilar nada**. 💊 Por eso los **inhibidores de CDK4/6 no funcionan en tumores sin Rb**: necesitan un Rb funcional al que impedir la fosforilación.

---

### 6.7 Mutaciones driver y passenger *(Diap. 13)*

| | **Driver** 🔴 | **Passenger** ⚪ |
|---|---|---|
| Ventaja selectiva | **Sí** | No directa |
| Número | **2–8 por tumor** (Vogelstein 2013) | La gran mayoría (más del 95 %) |
| Dónde | Genes de vías de señalización clave | En cualquier parte del genoma |
| Utilidad | **Dianas terapéuticas** | **Firmas mutacionales** y **carga mutacional (TMB)** |

#### Drivers clásicos (mutaciones "hotspot")

| Mutación | Dónde se ve | ➕ Relevancia |
|---|---|---|
| ***KRAS* G12D/V/C** | Páncreas, colon, pulmón | G12C: diana de sotorasib y adagrasib |
| ***TP53* R175H** | Muchos tumores | Hotspot del dominio de unión al ADN |
| ***BRAF* V600E** | Melanoma, tiroides papilar, colon | Vemurafenib, dabrafenib |
| ***EGFR* L858R** | Cáncer de pulmón no microcítico | Inhibidores de EGFR (osimertinib) |
| ***IDH1* R132H** | Glioma, leucemia mieloide aguda | Ivosidenib, vorasidenib |
| ***PIK3CA* H1047R** | Mama | Alpelisib |

#### Firmas mutacionales (COSMIC) *(Diap. 13)*

| Firma | Causa |
|---|---|
| **SBS1** | **Envejecimiento** (desaminación espontánea de 5-metilcitosina; "reloj") |
| **SBS4** | **Tabaco** |
| **SBS2/SBS13** | Enzimas **APOBEC** |
| **SBS6** | **MMR defectuoso** |
| ➕ **SBS88** | **Colibactina** de *E. coli pks+* (sección 6.19) |

📌 **TMB (carga mutacional tumoral)** alta = muchos neoantígenos → **predice respuesta a anti-PD-1**.

#### Tasas de mutación de la línea germinal *(Diap. 13)*

- **1,2 × 10⁻⁸** mutaciones por nucleótido por generación.
- Cada persona hereda **~60–70 mutaciones nuevas** (*de novo*).
- Por cada año adicional de edad del **padre**, el hijo hereda **~2 mutaciones más** (Kong et al., 2012).

⚠️ Estas cifras son de la **línea germinal** (lo que se hereda), no de las células tumorales. Explican por qué la edad paterna aumenta el riesgo de enfermedades *de novo* (por ejemplo, la acondroplasia).

➕ La figura de la diapositiva incluye **epi-drivers y epi-passengers**: cambios de metilación que, igual que las mutaciones, pueden dar ventaja (driver) o ser solo acompañantes.

---

### 6.8 Evolución clonal e inestabilidad genómica *(Diap. 15–16, 26)*

#### Evolución clonal *(Diap. 16)*

```
Célula normal → mutación inicial → expansión clonal → diversificación (subclones) → clon dominante
```

📌 La **inestabilidad genómica genera diversidad** y la **selección clonal** escoge las células con ventaja. El resultado: progresión, **resistencia terapéutica** y peor pronóstico.

#### Tipos de inestabilidad *(Diap. 15–16)*

| Tipo | Mecanismo | Consecuencia y relevancia |
|---|---|---|
| **CIN** (inestabilidad cromosómica) | Errores de segregación en la mitosis; ➕ falla del SAC (BUBR1, MAD2) | **Aneuploidía**, variantes estructurales, pérdida de heterocigosidad, amplificaciones y deleciones grandes. Es la forma más frecuente |
| **MSI** (inestabilidad de microsatélites) | Defecto de **MMR** (*MLH1*, *MSH2*, *MSH6*, *PMS2*) | Errores de replicación en repeticiones cortas. **MSI-H → TMB alta → responde a pembrolizumab** (aprobación agnóstica de tumor, FDA 2017) |
| **Ultramutador *POLE/POLD1*** | Mutación del dominio corrector (exonucleasa) de la polimerasa ε o δ | **TMB > 100 mutaciones/Mb**; respuesta muy buena a anti-PD-1. Frecuente en **endometrio** (tumores MSS ultramutados) |
| **Cromoplexia** | Varias roturas simultáneas que se reparan "encadenando" segmentos de **varios cromosomas** | Muchos reordenamientos en un solo evento. ➕ Descrita en cáncer de próstata (fusiones como *TMPRSS2-ERG*) |

✅ La diapositiva 15 anuncia "3 tipos" y enumera cuatro.

✅ La diapositiva atribuye a la cromoplexia los "ciclos de ruptura-fusión-puente". Son fenómenos distintos:
- **Ciclos de ruptura-fusión-puente (BFB)**: un cromosoma sin telómero se fusiona con su hermana, forma un puente en la anafase, se rompe y repite el ciclo. Producen amplificaciones en escalera. Aparecen en la **crisis telomérica** (sección 6.13).
- **Cromotripsis**: **un cromosoma (o pocos) se fragmenta** en un solo evento y se reensambla al azar (decenas a cientos de reordenamientos).
- **Cromoplexia**: reordenamientos **encadenados entre varios cromosomas**, generalmente balanceados.

📌 Con detalle de MMR, MSI y síndrome de Lynch en el [capítulo 5](#563-inestabilidad-de-microsatélites-msi-la-huella-de-un-mmr-defectuoso-diap-29).

#### Inestabilidad genómica como característica habilitante *(Diap. 26)*

- Ciertos genotipos mutantes dan a los subclones ventaja selectiva y les permiten diseminarse y dominar.
- Los clones minoritarios son difíciles de detectar: muchos tumores tardan años o décadas en manifestarse, y las células que escapan a la quimioterapia pueden no verse con métodos tradicionales.
- Genes implicados: *MLH1*, *MSH2*, *MSH6*, *BRCA1/2*, *ATM*, *CHEK1/2*, *POLE*, *POLD1*.

✅ La diapositiva dice que la secuenciación masiva con **cobertura 80x** detecta clones del 1 %. Con 80 lecturas, un clon del 1 % aporta en promedio menos de una lectura con la variante: no se detecta de forma fiable. Para ver clones del 1 % se necesita secuenciación **profunda** (del orden de cientos a miles de lecturas, como en los paneles dirigidos) o técnicas con códigos moleculares (biopsia líquida). Con 30–80x (genoma o exoma) se detectan subclones a partir de ~10–20 %.

---

### 6.9 El modelo de los hallmarks: 2000, 2011 y 2022 *(Diap. 17–18)*

📌 Los **hallmarks** son **capacidades funcionales** que las células adquieren al pasar de normales a malignas. Permiten ordenar la enorme variedad de mutaciones en unas pocas funciones compartidas.

| Año | Artículo | Qué se agrega |
|---|---|---|
| **2000** | Hanahan y Weinberg, *Cell* 100:57 | **6 hallmarks**: señalización proliferativa sostenida, evasión de supresores de crecimiento, resistencia a la muerte celular, inmortalidad replicativa, angiogénesis, invasión y metástasis |
| **2011** | Hanahan y Weinberg, *Cell* 144:646 | **2 hallmarks emergentes**: reprogramación del metabolismo energético y evasión de la destrucción inmune. **2 características habilitantes**: inestabilidad genómica y mutación, e inflamación promotora de tumores |
| **2022** | Hanahan, *Cancer Discov* 12:31 | **Plasticidad fenotípica** (nueva capacidad), **reprogramación epigenética no mutacional** y **microbiomas polimórficos** (nuevas características habilitantes), y **células senescentes** (nuevo tipo celular funcional del microambiente) |

| Nombre en inglés (figura) | En español |
|---|---|
| Sustaining proliferative signaling | Señalización proliferativa sostenida |
| Evading growth suppressors | Evasión de supresores de crecimiento |
| Resisting cell death | Resistencia a la muerte celular |
| Enabling replicative immortality | Inmortalidad replicativa |
| Inducing or accessing vasculature | Inducción o acceso a la vasculatura |
| Activating invasion & metastasis | Activación de invasión y metástasis |
| Deregulating cellular metabolism | Reprogramación metabólica |
| Avoiding immune destruction | Evasión de la destrucción inmune |
| *Genome instability & mutation* | *Inestabilidad genómica y mutación (habilitante)* |
| *Tumor-promoting inflammation* | *Inflamación promotora de tumores (habilitante)* |
| Unlocking phenotypic plasticity | Plasticidad fenotípica |
| *Nonmutational epigenetic reprogramming* | *Reprogramación epigenética no mutacional (habilitante)* |
| *Polymorphic microbiomes* | *Microbiomas polimórficos (habilitante)* |
| Senescent cells | Células senescentes |

✅ **Tres precisiones sobre las diapositivas 17–26**:
1. La diapositiva 18 se titula "figura original del artículo (2011)", pero la figura es la de **2022**, con 14 elementos.
2. La lista "Hallmarks 2022: 12 parámetros totales" omite las **dos características habilitantes de 2011** (inestabilidad genómica e inflamación). Sumándolas, el modelo de 2022 tiene **14 elementos**.
3. Las diapositivas 22–26 numeran distinto ("Hallmark 5: inflamación", "HM 9: invasión", "HM 10: inestabilidad genómica"). La inflamación y la inestabilidad genómica **no son hallmarks** sino **características habilitantes**: no son capacidades del tumor, sino condiciones que facilitan adquirirlas.

🧠 Los 8 hallmarks como un fugitivo: **acelera** (proliferación), **quita los frenos** (supresores), **no se deja matar** (muerte celular), **no envejece** (inmortalidad), **se consigue suministros** (vasos), **viaja** (metástasis), **cambia de dieta** (metabolismo) y **se esconde de la policía** (inmunidad).

---

### 6.10 Señalización proliferativa sostenida *(Diap. 19)*

#### En la célula normal

```
EGF, PDGF, HGF → receptor tirosina cinasa (RTK) → RAS-GTP → RAF → MEK → ERK → transcripción de ciclinas → proliferación
Freno: RAS-GAP (apaga RAS) y fosfatasas DUSP (apagan ERK)
```

➕ En paralelo, el RTK activa **PI3K → AKT → mTOR** (crecimiento y supervivencia); **PTEN** apaga esa vía.

#### En la célula tumoral: cuatro mecanismos

| # | Mecanismo | Ejemplo |
|---|---|---|
| 1 | **Producción autocrina** del factor de crecimiento | **TGF-α** en carcinomas |
| 2 | **Mutación activadora o amplificación del receptor** | ***EGFR* L858R**; ***ERBB2* amplificado** |
| 3 | **Mutación de un componente posterior** | ***KRAS* G12D/V**, ***BRAF* V600E** |
| 4 | **Pérdida de la retroalimentación negativa** | **Pérdida de *PTEN*** → PI3K/AKT siempre activa |

#### Frecuencias *(Diap. 19)*

| Gen | Dónde |
|---|---|
| ***KRAS*** | Páncreas **~90 %**, colon **~40 %**, pulmón **~30 %** |
| ***EGFR*** | Cáncer de pulmón no microcítico ~15 % (más en población asiática); glioblastoma > 50 % (sobre todo amplificación) |
| ***HER2/ERBB2*** | Mama **15–20 %**, gástrico |
| ***PIK3CA*** | Mama, endometrio, colon |

✅ La diapositiva dice "KRAS G12D/V (30 % de los cánceres)", citando a Prior et al. (2020). Ese mismo artículo estima que **~19 % de los pacientes con cáncer tienen una mutación en algún *RAS*** (y *KRAS* es ~75 % de ellas). El 30 % es una cifra antigua que el artículo corrige.

➕ La figura B de la diapositiva muestra el reordenamiento ***RET/PTC*** del **carcinoma papilar de tiroides**, que activa la misma cascada RAS → BRAF → MEK → ERK.

---

### 6.11 Evasión de los supresores de crecimiento *(Diap. 20)*

#### La vía de RB *(Diap. 20)*

- **RB hipofosforilado (activo)** se une a **E2F** y bloquea los genes de fase S.
- **Ciclina D–CDK4/6** fosforila a RB → E2F queda libre → proliferación.

| En cáncer | Tumores |
|---|---|
| ***RB1* mutado o deletado** | Retinoblastoma, **cáncer de pulmón de células pequeñas**, osteosarcoma |
| **CDK4/6 sobreactivadas** | *CCND1* amplificado (mama) |
| ***CDKN2A* (p16) silenciado** | Melanoma, páncreas |

💊 **Palbociclib, ribociclib y abemaciclib** (inhibidores de CDK4/6): cáncer de mama con receptores hormonales positivos y HER2 negativo.

➕ En melanoma y páncreas, *CDKN2A* se pierde sobre todo por **deleción o mutación**; la metilación es un mecanismo menos frecuente. En el melanoma familiar, la mutación es germinal.

#### p53, el guardián del genoma *(Diap. 20)*

```
Daño del ADN → ATM/ATR → fosforilan p53 (Ser15) → p53 se estabiliza → activa:
   p21 (pausa del ciclo) · BAX/PUMA (apoptosis) · GADD45 (reparación)
```

- Mutado en **~50 % de todos los cánceres** (➕ el gen más mutado; 42 % en el análisis pancáncer de Kandoth et al., 2013).
- Mutaciones *hotspot*: **R175H, R248W/Q** (➕ y R273H).
- **Li-Fraumeni**: mutación **germinal** de *TP53*.

⚠️ Dos efectos distintos de las mutaciones de *TP53*, que la diapositiva junta:
- **Dominante negativo**: p53 actúa como tetrámero; una subunidad mutante inactiva a las normales.
- **Ganancia de función (GOF)**: algunas proteínas mutantes adquieren funciones nuevas pro-tumorales (invasión, quimiorresistencia).

➕ Otras formas de apagar p53 sin mutarlo: **amplificación de *MDM2*** (liposarcoma) y la proteína **E6 del VPH**, que lo degrada (E7 secuestra a Rb).

---

### 6.12 Resistencia a la muerte celular *(Diap. 21)*

#### Apoptosis

| | **Vía intrínseca (mitocondrial)** | **Vía extrínseca (receptor de muerte)** |
|---|---|---|
| Estímulo | Daño del ADN, estrés oxidativo | **FAS-L, TRAIL** |
| Secuencia | Proteínas **BH3-only (BIM, PUMA)** → **BAX/BAK** → permeabilización de la membrana mitocondrial externa (**MOMP**) → **citocromo c** → **caspasa 9** → **caspasas 3/7** | **FAS, DR4/DR5** → complejo **DISC** → **caspasa 8** → caspasas 3/7 |
| Evasión en cáncer | **BCL-2/BCL-XL sobreexpresados** bloquean a BAX/BAK | **FAS mutado**, **c-FLIP sobreexpresado** |

**Morfología** *(figura)*: condensación de la cromatina → abombamiento ("globulación") de la membrana → colapso del núcleo → **cuerpos apoptóticos**. ➕ No hay inflamación: los macrófagos fagocitan los cuerpos apoptóticos.

#### La familia BCL-2 *(Diap. 21)*

| Gen | Contexto | Fármaco |
|---|---|---|
| ***BCL2*** | **t(14;18) del linfoma folicular** | **Venetoclax** (inhibidor de BCL-2) |
| ***BCL2L1*** (BCL-XL) | Mama, pulmón | Navitoclax (BCL-2/BCL-XL) |
| ***MCL1*** | Amplificado en muchos tumores | En investigación |
| ***BIRC5*** (survivina) | Sobreexpresado en más de 30 tipos | En investigación |

✅ **Venetoclax** está aprobado en **leucemia linfocítica crónica** y **leucemia mieloide aguda**, no en el linfoma folicular, aunque ese linfoma sea el ejemplo clásico de BCL-2 sobreexpresado. **Navitoclax no está aprobado** (en noviembre de 2026 sigue en ensayos, sobre todo en mielofibrosis); su toxicidad principal es la **trombocitopenia**, porque las plaquetas dependen de BCL-XL.

#### Otras formas de muerte celular *(Diap. 21)*

| Forma | Mecanismo |
|---|---|
| **Necroptosis** | "La apoptosis se encuentra con la necrosis": **RIPK3 → MLKL** perfora la membrana |
| **Piroptosis** | Células "en llamas": **inflamasoma** → caspasa 1 → **IL-1β e IL-18**; ➕ la **gasdermina D** forma los poros |
| **Ferroptosis** | Muerte por **peroxidación lipídica** dependiente de hierro cuando se inactiva **GPX4** |
| **Cuproptosis** | Muerte regulada por **cobre**; ➕ el cobre se une a enzimas lipoiladas del ciclo de Krebs y las agrega (Tsvetkov, 2022) |
| **Autofagia** | **Doble papel**: suprime tumores al inicio y ayuda a sobrevivir al tumor establecido |

---

### 6.13 Inmortalidad replicativa *(Diap. 22)*

📌 Secuencia:

```
Divisiones → telómeros cortos → p53/RB → senescencia (límite de Hayflick)
           → si p53/RB fallan → crisis → fusiones cromosómicas → casi todas mueren
           → la que reactiva un mantenimiento telomérico se vuelve inmortal
```

| Mecanismo de mantenimiento | Frecuencia | Detalle |
|---|---|---|
| **Telomerasa** (reactivación de *TERT*) | **85–90 %** de los cánceres | Mutaciones del promotor de *TERT* (**C228T, C250T**); ➕ también amplificación o reordenamientos de *TERT* |
| **ALT** (alargamiento alternativo de telómeros) | **10–15 %** | **Recombinación homóloga** entre telómeros; mutaciones de ***ATRX/DAXX*** (➕ sarcomas, gliomas, tumores neuroendocrinos pancreáticos) |

- ✅ El límite de Hayflick se resume como "~50 divisiones"; el dato clásico es **~40–60 duplicaciones** en fibroblastos fetales.
- ➕ Las mutaciones del promotor de *TERT* crean sitios de unión para factores de transcripción ETS. Son muy frecuentes en **melanoma, glioblastoma, vejiga y tiroides**, pero no explican todos los tumores con telomerasa activa.
- La **senescencia** también puede inducirse por estrés del microambiente (falta de nutrientes, daño del ADN).
- 💊 ➕ **Imetelstat**, el primer **inhibidor de telomerasa** aprobado (FDA, junio de 2024), se usa en síndromes mielodisplásicos de bajo riesgo con anemia dependiente de transfusiones.

---

### 6.14 Inflamación promotora de tumores *(Diap. 22–23)*

📌 Es una **característica habilitante**: la inflamación crónica **predispone** al cáncer y **promueve todas sus etapas**.

#### Ejemplos causales

| Agente o enfermedad | Inflamación | Cáncer |
|---|---|---|
| ***Helicobacter pylori*** | Gastritis crónica | **Adenocarcinoma gástrico** (➕ y linfoma MALT) |
| **VHB, VHC** | Hepatitis crónica | **Hepatocarcinoma** |
| **VPH** | Cervicitis | **Carcinoma de cuello uterino** |
| **Enfermedad inflamatoria intestinal** | Colitis | **Cáncer colorrectal** |

✅ En el VPH, el mecanismo principal no es la inflamación: las oncoproteínas virales **E6 (degrada p53) y E7 (inactiva Rb)** transforman directamente la célula. La inflamación es secundaria.

#### Mecanismos pro-tumorales *(Diap. 22–23)*

| Mecanismo | Mediadores |
|---|---|
| **Proliferación y supervivencia** | **TNF-α, IL-6, IL-8** → **NF-κB, STAT3**, MAPK, PI3K/AKT |
| **Daño del ADN** | **ROS/RNS** de los neutrófilos |
| **Remodelación de la matriz** | **MMP** de los macrófagos; activación de fibroblastos |
| **Angiogénesis** | VEGF |
| **Inmunosupresión** | **Macrófagos M2 (TAM)** → VEGF, **IL-10, TGF-β**; Treg y MDSC |
| **Resistencia terapéutica** | La inflamación protege a las células tumorales del daño por quimio y radioterapia |

#### Las seis etapas *(Diap. 23)*

1. **Inicio**: estímulo crónico (infecciones, irritantes, obesidad, daño tisular) activa la inmunidad innata.
2. **Inflamación crónica**: citocinas (TNF-α, IL-1β, IL-6, IL-17, IL-23), ROS, RNS, COX-2, PGE2, quimiocinas.
3. **Daño del ADN y estrés oxidativo**: mutaciones, inestabilidad genómica, cambios epigenéticos.
4. **Promoción tumoral**: proliferación, angiogénesis, remodelación de la matriz, inmunosupresión local.
5. **Progresión**: invasión, metástasis, evasión inmune y resistencia.
6. **Mantenimiento**: la inflamación se vuelve autónoma; el tumor y su estroma la retroalimentan.

**Estímulos crónicos comunes**: infecciones, **hígado graso y obesidad**, **tabaco y contaminantes**, enfermedades **autoinmunes**, irritación y daño tisular.

💊 Dianas: **COX-2**, **IL-6/JAK/STAT3**, **NF-κB**.

---

### 6.15 Inducción o acceso a la vasculatura *(Diap. 24)*

📌 **Switch angiogénico**: sin vasos nuevos, un tumor no crece más allá de **1–2 mm**, porque el oxígeno solo difunde unos 100–200 µm.

✅ La diapositiva dice "tumores **>**0,2–2 mm: avasculares". Es al revés: los tumores **de hasta ~1–2 mm** pueden ser avasculares; para crecer **más** necesitan inducir vasos.

#### El eje VHL–HIF–VEGF

| Condición | Qué pasa con HIF-1α |
|---|---|
| **Oxígeno normal** | La **PHD hidroxila a HIF-1α** → **VHL lo ubiquitina** → **proteasoma** |
| **Hipoxia** | La PHD no actúa → **HIF-1α escapa** → transcribe **VEGF-A, PDGF-BB, angiopoyetina 2** |
| ***VHL* mutado** (carcinoma renal de células claras, **~90 %** con *VHL* inactivado) | **HIF activo siempre** → máxima producción de VEGF (**seudohipoxia**) |

- Antiangiogénicos endógenos que el tumor pierde: **trombospondina 1 (TSP-1)** y **endostatina**.
- 💊 **Bevacizumab** (anti-VEGF-A), **ramucirumab** (anti-VEGFR2), **sunitinib** y **cabozantinib** (inhibidores multicinasa).
- ➕ 💊 **Belzutifan** (inhibidor de HIF-2α) está aprobado para tumores asociados a la enfermedad de von Hippel-Lindau (2021) y para el carcinoma renal avanzado (2023).
- ➕ El mecanismo de detección del oxígeno (PHD–VHL–HIF) recibió el **Nobel de Fisiología o Medicina 2019** (Kaelin, Ratcliffe y Semenza).

🧠 **"Con oxígeno, VHL Vacía HIF; sin oxígeno, HIF Hace vasos."**

---

### 6.16 Reprogramación metabólica *(Diap. 24)*

📌 **Efecto Warburg** (observado por Otto Warburg en 1924): las células tumorales prefieren la **glucólisis aeróbica**, que termina en **lactato**, **aun con oxígeno disponible**. La paradoja: **2 ATP** por glucosa frente a **~30–36** de la fosforilación oxidativa.

✅ La diapositiva da 36 ATP. Es el valor clásico de los libros; las estimaciones actuales son **~30–32 ATP** por glucosa.

#### Ventajas reales para el tumor

1. **ATP rápido**: la glucólisis produce ATP a gran velocidad.
2. **Vía de las pentosas**: **ribosa** para ADN y ARN, y **NADPH**.
3. **Carbonos para biosíntesis** de lípidos y proteínas.
4. El **lactato acidifica el microambiente** → inmunosupresión.
5. 🩺 Base de la **PET con FDG**: el tumor capta mucha glucosa marcada.

#### Oncometabolitos

| Gen mutado | Metabolito | Efecto |
|---|---|---|
| ***IDH1/2*** | **D-2-hidroxiglutarato (2-HG)** | Inhibe las **dioxigenasas dependientes de α-cetoglutarato** (TET, desmetilasas de histonas) → **hipermetilación** |
| ***SDH*** | **Succinato** | Inhibe la **PHD** → **HIF activo** (seudohipoxia) |

💊 Dianas: **HK2**, **LDHA** (inducida por MYC y HIF-1α), **IDH1** (**ivosidenib**) e **IDH2** (**enasidenib**) en leucemia mieloide aguda. ➕ **Vorasidenib** (inhibidor de IDH1/2) se aprobó en 2024 para el glioma de grado 2 con *IDH* mutado.

---

### 6.17 Evasión de la destrucción inmune *(Diap. 25)*

#### Las tres E de la inmunoedición (Schreiber, 2011)

| Fase | Qué pasa |
|---|---|
| **Eliminación** | Linfocitos T citotóxicos y células NK destruyen las células transformadas que presentan **neoantígenos**. La mayoría de las neoplasias incipientes se eliminan aquí |
| **Equilibrio** | Persisten subclones **menos inmunogénicos**. Fase de **latencia**; se seleccionan variantes de escape |
| **Escape** | Las variantes eluden la vigilancia → expansión clonal → **cáncer clínico** |

#### Mecanismos de escape

1. **PD-L1 → PD-1**: agota a los linfocitos que infiltran el tumor (TIL).
2. **Pérdida de MHC-I**: el tumor deja de presentar antígenos.
3. **Treg y MDSC**: células inmunosupresoras.
4. **IDO1**: degrada triptófano y genera quinurenina inmunosupresora.
5. **TGF-β** secretado.

🧠 **"El tumor se pone el escudo (PD-L1), se quita la placa (MHC-I), contrata guardaespaldas (Treg, MDSC), deja sin comida a la policía (IDO1) y la tranquiliza (TGF-β)."**

➕ La figura de la diapositiva muestra un **virus oncolítico**: se replica en la célula tumoral, la lisa y libera antígenos que activan la respuesta inmune. Ejemplo aprobado: **talimogén laherparepvec (T-VEC)**, un herpes modificado para melanoma (2015).

➕ El **Nobel de Fisiología o Medicina 2018** premió a Allison (CTLA-4) y Honjo (PD-1) por la inmunoterapia con inhibidores de puntos de control.

---

### 6.18 Invasión y metástasis *(Diap. 26)*

#### La cascada metastásica

| # | Paso | Qué pasa |
|---|---|---|
| 1 | **Transición epitelio-mesénquima (EMT)** | **Pérdida de E-cadherina** → motilidad; factores **ZEB1, SNAIL, TWIST** |
| 2 | **Invasión de la matriz** | **MMP** degradan colágeno y laminina |
| 3 | **Intravasación** | Entra a vasos sanguíneos o linfáticos |
| 4 | **Circulación** | Las **células tumorales circulantes (CTC)** sobreviven en el torrente |
| 5 | **Extravasación** | Adhesión y salida en el órgano diana |
| 6 | **Colonización** | **Micrometástasis → macrometástasis** |

**Genes clave**: ***CDH1*** (E-cadherina; ➕ su mutación germinal causa el **cáncer gástrico difuso hereditario**), **ZEB1, SNAIL**, **MMP2/9**, ***MET*** (gástrico, pulmón no microcítico), ***SMAD4***.

➕ La hipótesis de **"la semilla y el suelo"** (Paget, 1889) explica por qué cada tumor prefiere ciertos órganos: la célula tumoral (semilla) necesita un microambiente compatible (suelo).

---

### 6.19 Las cuatro nuevas dimensiones de 2022 *(Diap. 27–30)*

| Dimensión | Categoría según Hanahan | Idea central |
|---|---|---|
| **Plasticidad fenotípica** | Nueva **capacidad** (hallmark) | La célula tumoral escapa de la diferenciación terminal |
| **Reprogramación epigenética no mutacional** | Característica **habilitante** | Cambios de la expresión génica sin mutaciones |
| **Microbiomas polimórficos** | Característica **habilitante** | Las bacterias del intestino y del tumor modulan los hallmarks |
| **Células senescentes** | **Tipo celular** funcional del microambiente | El SASP de las células senescentes favorece al tumor |

#### 1. Plasticidad fenotípica *(Diap. 29)*

| Subtipo | Qué pasa | Ejemplos |
|---|---|---|
| **Desdiferenciación** | Células maduras vuelven a un estado progenitor | **Melanoma**: pérdida de **MITF** → reactivación de genes de la cresta neural. **Colon**: pérdida de **HOXA5** y **SMAD4** |
| **Diferenciación bloqueada** | Los progenitores no completan la diferenciación | **Leucemia promielocítica aguda (APL)**: ***PML-RARA*** detiene la maduración en el **promielocito**. 💊 **ATRA** (ácido transretinoico) fuerza la diferenciación a **granulocitos** |
| **Transdiferenciación** | Cambio a otro linaje | **Páncreas**: células **acinares → ductales** al perder **PTF1A/MIST1** y aumentar **SOX9**. **Próstata**: pérdida de ***RB1* + *TP53*** y **SOX2** alto → **carcinoma neuroendocrino** resistente a los antiandrógenos |

- La **vía WNT** es clave en la plasticidad. Genes de melanoma implicados: *MITF*, *BRAF*, *ATF2*.
- ➕ 🩺 La APL se debe a la **t(15;17)**. El tratamiento actual combina **ATRA y trióxido de arsénico**, que degrada la proteína de fusión; cura a más del 90 % de los pacientes de bajo riesgo.
- ➕ La transformación a **cáncer de pulmón de células pequeñas** es otro mecanismo de resistencia de tumores con *EGFR* mutado.

#### 2. Reprogramación epigenética no mutacional *(Diap. 29)*

- **ZEB1** (regulador maestro de la EMT) induce a **SETD1B**, una **metiltransferasa de histonas**. Se forma un circuito que **mantiene el estado mesenquimal sin mutaciones nuevas**.
- La **hipoxia inhibe a las desmetilasas TET** → **hipermetilación del ADN** → silenciamiento de genes supresores.
- La expresión depende de modificaciones de la cromatina: **H3K27me3** (puesta por **EZH2**), complejos de remodelación como ***ARID1A*** (SWI/SNF).
- Resultado: **heterogeneidad epigenómica intratumoral**.
- ➕ 💊 Fármacos epigenéticos aprobados: **azacitidina y decitabina** (hipometilantes), **vorinostat** (inhibidor de HDAC) y **tazemetostat** (inhibidor de EZH2).

#### 3. Microbiomas polimórficos *(Diap. 28, 30)*

| Mecanismo | Ejemplo |
|---|---|
| **Mutagénesis directa** | ***E. coli pks+*** produce **colibactina**, que daña el ADN y deja la **firma SBS88** en el cáncer colorrectal |
| **Señalización pro-proliferativa** | ***Fusobacterium nucleatum*** activa **Wnt/β-catenina** (➕ su adhesina FadA se une a la E-cadherina) |
| **Inmunomodulación sistémica** | Señales como **NOD2** e **inosina** bacteriana modulan la respuesta inmune |
| **Respuesta a la inmunoterapia** | El **trasplante fecal de pacientes respondedores** restaura la eficacia del anti-PD-1 en **melanoma refractario** (Baruch y Davar, *Science* 2021) |
| **Eje intestino-hígado** | La disbiosis lleva bacterias por la porta → **TLR4 → CXCL1** → reclutamiento de **MDSC** → inhibición de las NK → **colangiocarcinoma** |
| **Microbioma intratumoral** | En **1.526 tumores de 7 tipos**, cada tipo tuvo un microbioma **intracelular** propio (Nejman, 2020) |

➕ El ejemplo microbiano más antiguo y sólido es ***H. pylori*** (carcinógeno del grupo 1 de la IARC).

#### 4. Células senescentes *(Diap. 28, 30)*

- Las células senescentes (tumorales y del estroma) secretan el **SASP**: **IL-6, IL-8, MMP3, VEGF, CXCL1**.
- **Baker et al. (*Nature* 2016)**: eliminar las células **p16<sup>INK4a</sup>+** en ratones envejecidos redujo la tumorigénesis espontánea.
- **Paradoja**: el SASP puede ser pro- o antitumoral según el contexto. Los **fibroblastos asociados al cáncer (CAF) senescentes** dan soporte paracrino.
- **Senescencia transitoria**: la célula tumoral entra en dormancia, **escapa a la quimioterapia** y luego **reanuda** la proliferación.
- 💊 **Senolíticos**: **navitoclax**, **dasatinib + quercetina**. ✅ Son **experimentales**: ninguno está aprobado como senolítico.

Conecta con [senescencia frente a quiescencia en el capítulo 3](#317-quiescencia-frente-a-senescencia-diap-49).

---

### 6.20 Epidemiología mundial *(Diap. 31–35)*

✅ La clase usa **GLOBOCAN 2022** (Bray et al., 2024). En **julio de 2026** la IARC publicó **GLOBOCAN 2024** (Sung et al., *CA Cancer J Clin* 2026). Aprende las dos: la de la clase para el examen y la nueva para la práctica.

| Indicador | GLOBOCAN 2022 *(Diap. 32)* | ➕ GLOBOCAN 2024 |
|---|---|---|
| Casos nuevos | **~20 millones** | **20,6 millones** |
| Muertes | **9,7 millones** | **9,8 millones** |
| Riesgo de desarrollar cáncer en la vida | **1 de cada 5** | 1 de cada 5 |
| Riesgo de morir por cáncer | 1 de cada 9 hombres y 1 de cada 12 mujeres | 1 de cada 9 hombres y 1 de cada 13 mujeres |
| Proyección a 2050 | **35 millones** de casos | 34,4 millones (+67 %) |

#### Cánceres más frecuentes (ambos sexos)

| # | GLOBOCAN 2022 *(Diap. 32)* | ➕ GLOBOCAN 2024 |
|---|---|---|
| 1 | **Pulmón 12,4 %** | Pulmón 12,8 % |
| 2 | **Mama 11,6 %** | Mama 11,8 % |
| 3 | **Colorrectal 9,6 %** | Colorrectal 9,9 % |
| 4 | **Próstata 7,3 %** | Próstata 7,5 % |
| 5 | **Estómago 4,9 %** | Estómago 4,8 % |

➕ **Mortalidad (2024)**: pulmón 19,1 % (1,9 millones), colorrectal 9,4 %, hígado 7,5 %, mama 7,1 %, estómago 6,6 %.

#### Otros datos de la clase *(Diap. 32–35)*

- **Mama**: el más común en mujeres, con **más de 2,3 millones** de casos al año (➕ 2,4 millones en 2024).
- **Pulmón**: lidera la mortalidad, con **más de 1,8 millones** de muertes al año.
- **Niños**: ~**400.000 casos** al año; leucemias, tumores cerebrales y linfomas; mucho mejor supervivencia en países de ingresos altos. ✅ La OMS da esa cifra para **0 a 19 años**, no para menores de 15.
- **Leucemia linfoblástica aguda**: la diapositiva le asigna el 30 % de los casos pediátricos. ✅ Las **leucemias en conjunto** son ~30 % de los cánceres infantiles; la **LLA sola**, ~25 % (es ~3 de cada 4 leucemias infantiles).
- **Adultos**: ~50 % de las muertes son atribuibles a factores modificables (**tabaco, dieta, alcohol**).
- El cáncer es la **segunda causa de muerte** en el mundo, después de las enfermedades cardiovasculares. Causa **~1 de cada 6 muertes**. ✅ La diapositiva dice "1 de cada 6 personas muere a causa del cáncer"; la cifra de la OMS se refiere a **muertes**, no a personas.
- **~70 % de las muertes por cáncer** ocurren en países de **ingresos bajos y medios**. ✅ La diapositiva lo presenta como "tasa de mortalidad (70 %)"; no es una tasa, es la **proporción** de muertes.
- El **tabaco** causa **~22 % de las muertes por cáncer** (dato de la OMS).
- La carga crece en los países de ingresos medios, donde cuesta implementar la detección temprana.

#### Estados Unidos *(Diap. 33, ACS 2025)*

| | Hombres | Mujeres |
|---|---|---|
| 1.ª causa de muerte por cáncer | **Pulmón y bronquios** (20 %) | **Pulmón y bronquios** (21 %) |
| 2.ª | Próstata (11 %) | Mama (14 %) |
| 3.ª | Colon y recto (9 %) | Páncreas (8 %) |
| 4.ª | Páncreas (8 %) | Colon y recto (8 %) |
| Total de muertes estimadas | 323.900 | 294.220 |

➕ La edición 2026 de la ACS proyecta **2.114.850 casos nuevos y 626.140 muertes** en Estados Unidos.

---

### 6.21 Epidemiología en Colombia *(Diap. 36–39)*

| Indicador | Diapositiva 37 | GLOBOCAN 2022 | ➕ GLOBOCAN 2024 |
|---|---|---|---|
| Casos nuevos | **117.620** | 117.620 ✔ | **123.053** |
| Tasa de incidencia ajustada por edad (× 100.000) | **177,6** | 177,6 ✔ | 180,8 |
| Muertes | **40.333** ("INC 2023") | **56.719** | **55.981** |
| Tasa de mortalidad ajustada (× 100.000) | — | 81,4 | 78,9 |
| Proyección | **~150.000 en 2030** | — | — |

✅ No fue posible verificar las **40.333 muertes**: GLOBOCAN estima **~56.000** y la plataforma de información de cáncer del INC reportó ~51.000 muertes en su indicador de 2025. La proyección de 150.000 casos para 2030 tampoco aparece en las fuentes citadas.

#### Cánceres más frecuentes

| | Diapositiva 37 ("INC 2023") | ➕ GLOBOCAN 2024 (estimación nacional) |
|---|---|---|
| **Hombres** | 1. Piel no melanoma · 2. Próstata · 3. Estómago · 4. Colon y recto · 5. Vías urinarias | 1. **Próstata** (29 %) · 2. Estómago · 3. Colorrectal · 4. Pulmón · 5. Linfoma no Hodgkin |
| **Mujeres** | 1. Mama · 2. Cuello uterino · 3. Colon y recto · 4. Tiroides · 5. Pulmón | 1. **Mama** (27 %) · 2. Tiroides · 3. Colorrectal · 4. Cuello uterino · 5. Estómago |
| **Ambos sexos** | — | Mama, próstata, colorrectal, estómago, tiroides |
| **Mortalidad** | — | 1. **Estómago** · 2. Pulmón · 3. Colorrectal · 4. Mama · 5. Próstata |

⚠️ La lista de la clase viene de los **pacientes atendidos en el INC** (un solo hospital), no de toda la población. GLOBOCAN es una estimación nacional. Por eso los órdenes no coinciden.

⚠️ El **cáncer de piel no melanoma** es el más frecuente en números absolutos, pero casi siempre se **excluye de los rankings**: rara vez es mortal y se registra mal.

#### El INC en cifras, 2023 *(Diap. 38)*

| Dato | Valor |
|---|---|
| Casos nuevos atendidos | **6.640** |
| Mujeres / hombres | **57,2 %** / 42,8 % |
| Grupo de edad más frecuente | **≥ 65 años (41,3 %)**; 0–14 años: 2,1 % |
| Régimen de afiliación | **Subsidiado 49,4 %**, contributivo 35,0 %, particular 11,4 % |
| Procedencia | **Bogotá 56,1 %**; el 90 % vive en Bogotá o en su área de influencia (Cundinamarca, Boyacá, Tolima, Casanare, Meta, Huila) |

*(Diap. 39)* El gráfico de burbujas por departamento no indica qué variable mide. Los valores más altos son Bogotá (411), Antioquia (208), Valle (146) y Santander (71); seis departamentos de la Amazonía y la Orinoquía aparecen sin dato.

#### Políticas *(Diap. 37)*

- **Risaralda** tuvo la **mayor mortalidad ajustada por cáncer** en 2015–2017 (Cuenta de Alto Costo: 54,8 a 61,1 por 100.000).
- **Plan de Choque contra el Cáncer 2023–2026**: tamizaje, diagnóstico temprano, acceso a tratamiento y fortalecimiento de la red oncológica. ✅ Se formalizó con la **Circular Conjunta Externa 010 de 2024**, firmada por el **Ministerio de Salud, el INC y la Superintendencia Nacional de Salud** (la diapositiva menciona a la OPS).
- ➕ En **julio de 2026** el Ministerio adoptó el **Plan Decenal para el Control del Cáncer 2026–2035**, con enfoque territorial y evaluaciones en 2028, 2030 y 2035.

---

### 6.22 De los hallmarks a los fármacos *(Diap. 41)*

| Hallmark | Diana | Fármacos | Indicación |
|---|---|---|---|
| **Señalización proliferativa** | BCR-ABL, EGFR, HER2, KRAS G12C | **Imatinib, osimertinib, trastuzumab, sotorasib** | LMC, pulmón no microcítico, mama, pulmón no microcítico |
| **Evasión de supresores** | CDK4/6–ciclina D | **Palbociclib, ribociclib, abemaciclib** | Mama RH+ HER2− |
| **Resistencia a la apoptosis** | BCL-2 | **Venetoclax** | LLC, LMA |
| **Inmortalidad replicativa** | ➕ Telomerasa | ➕ **Imetelstat** | Síndrome mielodisplásico de bajo riesgo |
| **Angiogénesis** | VEGF/VEGFR, multicinasa | **Bevacizumab, ramucirumab, sunitinib** | Colorrectal, gástrico, pulmón, renal |
| **Invasión y metástasis** | MET (➕ y ALK, ROS1) | **Capmatinib** (➕ crizotinib, entrectinib) | Pulmón con salto del exón 14 de *MET*; pulmón ALK+ o ROS1+ |
| **Metabolismo** | IDH1/2 mutada | **Ivosidenib, enasidenib** | LMA con *IDH1* / *IDH2* mutado |
| **Evasión inmune** | PD-1/PD-L1, CTLA-4, LAG-3 | **Pembrolizumab, ipilimumab, relatlimab** | Melanoma, pulmón, muchos tumores |
| **Plasticidad fenotípica** | RARα, HDAC | **ATRA (tretinoína), vorinostat** | APL, linfoma cutáneo de células T |
| **Inmunoterapia celular** | CD19, BCMA | **Tisagenlecleucel, idecabtagén vicleucel** | LLA-B, mieloma múltiple |
| ➕ **Inestabilidad genómica** (habilitante) | PARP | **Olaparib, niraparib, rucaparib** | Ovario, mama, próstata y páncreas con *BRCA* mutado |

✅ Correcciones a la tabla de la diapositiva:
- **PARP** aparece como diana de "resistencia a la apoptosis" y de "inmortalidad replicativa". Los inhibidores de PARP aprovechan un **defecto de reparación** (letalidad sintética en tumores sin recombinación homóloga): corresponden a la **inestabilidad genómica**.
- En "inmortalidad replicativa" la diapositiva pone olaparib y palbociclib, que no actúan sobre la telomerasa. El ejemplo correcto es **imetelstat** (FDA 2024).
- **ALK y ROS1** son receptores de fusión que dan **señalización proliferativa**; en el esquema de Hanahan, la diana asociada a invasión es **HGF/MET**.

---

### 6.23 Medicina personalizada *(Diap. 42)*

| Herramienta | Qué es | Ejemplos |
|---|---|---|
| **NGS / perfil genómico** | Paneles que detectan SNV, CNV, fusiones, **MSI**, **TMB** y **HRD** (deficiencia de recombinación homóloga) | **FoundationOne CDx**, **MSK-IMPACT** (aprobados por la FDA en 2017 para tumores sólidos avanzados) |
| **Terapias dirigidas** | Inhibidores de una alteración concreta | **Imatinib** (BCR-ABL), **osimertinib** (EGFR), **sotorasib** (2021) y **adagrasib** (2022) para KRAS G12C, **alpelisib** (PI3Kα), inhibidores de CDK4/6 |
| **Inhibidores de puntos de control (ICI)** | Liberan el freno de los linfocitos T | **Pembrolizumab** agnóstico de tumor: **MSI-H (2017)** y **TMB alta (2020)**; **ipilimumab** (anti-CTLA-4); **relatlimab** (anti-LAG-3, melanoma, 2022) |
| **Vacunas de ARNm personalizadas** | ARNm que codifica **neoantígenos del propio tumor** | **mRNA-4157/V940** (intismeran autogén; Moderna y MSD) + pembrolizumab |
| **CAR-T y terapias celulares** | Linfocitos del paciente modificados o expandidos | **Tisagenlecleucel** (CD19, LLA-B), **idecabtagén** (BCMA, mieloma), **lifileucel** (TIL, melanoma, FDA 2024); CAR-T alogénicos editados con CRISPR en desarrollo |
| **Inhibidores de PARP y senolíticos** | Letalidad sintética; eliminación de células senescentes | **Olaparib, niraparib, rucaparib** en tumores con *BRCA1/2* deficiente; senolíticos experimentales |

#### La vacuna de ARNm contra el melanoma

| Ensayo | Diseño | Resultado |
|---|---|---|
| **KEYNOTE-942** (fase IIb) *(Diap. 42)* | Melanoma resecado de alto riesgo; vacuna + pembrolizumab frente a pembrolizumab solo | **44 % menos recurrencia o muerte (HR 0,56)** |
| ➕ **INTerpath-001** (fase III, ESMO 2026) | Melanoma resecado estadios IIB–IV; 1.137 pacientes | Supervivencia libre de recurrencia **HR 0,58**; a 24 meses, **82,2 % frente a 70,0 %**. Metástasis a distancia: HR 0,62. La supervivencia global aún es inmadura |

✅ La diapositiva cita KEYNOTE-942 como *NEJM Evidence* 2023; la publicación principal del ensayo es **Weber et al., *Lancet* 2024**. La diapositiva dice "fase III activa": ya se presentaron sus resultados (positivos) en octubre de 2026.

#### ➕ Letalidad sintética

Dos genes son **sintéticamente letales** cuando perder uno solo es tolerable, pero perder los dos mata a la célula. Las células con ***BRCA1/2*** deficiente no reparan por recombinación homóloga; si además se **inhibe PARP**, las roturas de cadena sencilla se convierten en roturas de doble cadena que no pueden reparar y mueren. Las células normales del paciente conservan un alelo de *BRCA* y sobreviven. Detalle en el [capítulo 5](#5101--letalidad-sintética-inhibidores-de-parp-y-tumores-brca-diap-44).

#### ➕ Aprobaciones agnósticas de tumor

Se aprueba el fármaco por la **alteración molecular**, sin importar el órgano de origen.

| Año | Fármaco | Biomarcador |
|---|---|---|
| 2017 | Pembrolizumab | MSI-H o dMMR |
| 2018 | Larotrectinib | Fusiones de *NTRK* |
| 2020 | Pembrolizumab | TMB ≥ 10 mutaciones/Mb |
| 2021 | Dostarlimab | dMMR |
| 2022 | Dabrafenib + trametinib | *BRAF* V600E |
| 2022 | Selpercatinib | Fusiones de *RET* |
| 2024 | Trastuzumab deruxtecán | HER2 3+ por IHQ |

---

### 6.24 Síntesis: el modelo multietapa *(Diap. 44–45)*

```
Célula normal → Iniciación → Clonalidad → Progresión → Metástasis → Resistencia → Escape / recaída
                1.ª driver    2.ª–3.ª      MYC, SMAD4    plasticidad   heterogeneidad   subclon
                (APC, KRAS)   (CDKN2A,      EMT activa    angiogénesis  subclon          dominante
                              TP53)                                    resistente
```

1. **Modelo multietapa**: hacen falta **varias alteraciones driver** para un carcinoma invasivo; cada una da ventaja selectiva.
2. **Evolución darwiniana**: se seleccionan los clones con mayor *fitness*. La **heterogeneidad intratumoral** genera resistencia.
3. **Tronco y ramas**: las mutaciones del **tronco** (fundadoras) están en todos los clones; las de las **ramas**, solo en algunos subclones. Por eso una sola biopsia puede no mostrar todo el tumor.
4. La acumulación de mutaciones somáticas **precede** a los cambios morfológicos; muchos tumores tardan **décadas**. De ahí la importancia de la detección temprana.
5. **Plasticidad fenotípica**: las células cambian de fenotipo **sin mutaciones nuevas**, lo que complica la terapia.
6. **ADN tumoral circulante (ctDNA) / biopsia líquida**: detecta clones minoritarios, resistencia emergente y **enfermedad mínima residual**.

✅ La diapositiva cita "Vogelstein 1990, *Science*"; el modelo es de **Fearon y Vogelstein, *Cell* 1990;61:759**. La diapositiva 44 habla de "4–8 alteraciones driver" y la 13 de "2–8": la cifra de Vogelstein (2013) es **2–8 drivers por tumor**.

#### ➕ La secuencia clásica adenoma-carcinoma colorrectal (Fearon y Vogelstein)

```
Epitelio normal → (APC) → adenoma temprano → (KRAS) → adenoma intermedio → (pérdida de 18q: SMAD4) → adenoma tardío → (TP53) → carcinoma → metástasis
```

🧠 **"A-K-S-T"**: ***A**PC* abre la puerta, ***K**RAS* acelera, ***S**MAD4* se pierde, ***T**P53* cae y aparece el carcinoma.

#### Conclusiones de la clase *(Diap. 45)*

1. El cáncer es una enfermedad **genética y epigenética multietapa**: oncogenes con ganancia de función (*KRAS*, *EGFR*, *MYC*), supresores con pérdida (*TP53*, *RB1*, *BRCA1/2*), cambios epigenéticos y del microambiente.
2. Los **8 hallmarks** dan un marco unificador; Hanahan (2022) añade **plasticidad, epigenética no mutacional, microbiomas y células senescentes**.
3. La **medicina personalizada** conecta los hallmarks con decisiones clínicas: NGS, inhibidores dirigidos, inmunoterapia, CAR-T y vacunas de ARNm.
4. **Colombia**: 117.620 casos al año (GLOBOCAN 2022); el Plan de Choque fue la hoja de ruta 2023–2026 (➕ y el Plan Decenal 2026–2035 la de la próxima década).
5. El médico moderno necesita genética molecular para interpretar NGS, entender biomarcadores y participar en la oncología de precisión.

---

### 6.25 Las preguntas de la clase, resueltas *(Diap. 48)*

<details><summary>1. ¿Diferencia entre proto-oncogén y gen supresor? Explique con KRAS y TP53.</summary>

Un **proto-oncogén** estimula la proliferación; su mutación de **ganancia de función en un solo alelo** basta. *KRAS* G12D no hidroliza el GTP, queda activo y mantiene encendida la vía MAPK sin señal externa. Un **gen supresor** frena la proliferación o induce apoptosis; hay que **perder los dos alelos**. Sin p53 funcional, la célula con ADN dañado no se detiene (no induce p21) ni muere (no induce BAX/PUMA), y acumula mutaciones.
</details>

<details><summary>2. Hipótesis de Knudson. ¿Por qué el retinoblastoma hereditario aparece antes? Aplique a BRCA1/2.</summary>

En la forma hereditaria **todas las células ya tienen el primer golpe** (germinal), así que basta un evento somático: es más probable y más temprano, y suele afectar ambos ojos. En la esporádica hacen falta dos eventos somáticos en la misma célula. Con *BRCA1/2* pasa lo mismo: la portadora heterocigota desarrolla cáncer de mama u ovario **más joven** y con más frecuencia **bilateral**, porque solo necesita perder el alelo normal en una célula.
</details>

<details><summary>3. Paciente con cáncer de pulmón no microcítico y EGFR L858R. ¿Qué inhibidor? Seis meses después aparece T790M. ¿Mecanismo y siguiente paso?</summary>

L858R (exón 21) sensibiliza al tumor a los inhibidores de tirosina cinasa de EGFR. **Esquema clásico**: inhibidor de primera o segunda generación (**gefitinib, erlotinib, afatinib**). **T790M** es la mutación del "guardián" (*gatekeeper*) del exón 20: aumenta la afinidad del receptor por el ATP y desplaza al fármaco. Es la causa de ~50–60 % de las resistencias a esos fármacos. El siguiente paso es **osimertinib** (tercera generación, se une de forma covalente a C797 y funciona con T790M). T790M puede detectarse en **biopsia líquida** (ctDNA). ➕ Hoy **osimertinib es primera línea** (estudio FLAURA); la resistencia a osimertinib incluye **C797S**, **amplificación de *MET*** y **transformación a carcinoma de células pequeñas** (plasticidad).
</details>

<details><summary>4. Diferenciación bloqueada en APL. ¿Por qué funciona ATRA?</summary>

La **t(15;17)** crea la fusión **PML-RARα**, que reprime los genes de diferenciación mieloide: las células se quedan como **promielocitos** que proliferan. El **ATRA en dosis farmacológicas** se une a RARα, libera a los correpresores, induce la degradación de la fusión y obliga a los promielocitos a madurar a **granulocitos**. Es el ejemplo clínico de que **revertir la plasticidad fenotípica** (diferenciación bloqueada) trata el cáncer.
</details>

<details><summary>5. Un tumor colorrectal es MSI-H. ¿Qué significa y por qué predice respuesta a pembrolizumab?</summary>

**MSI-H** indica un **sistema MMR deficiente** (pérdida de MLH1, MSH2, MSH6 o PMS2): se acumulan inserciones y deleciones en microsatélites, muchas con **cambio del marco de lectura**. Eso genera una **carga mutacional alta** y muchos **neoantígenos**; el tumor atrae linfocitos T, pero se protege con PD-L1. Al bloquear PD-1, los linfocitos atacan. La causa está en la biología (MMR), no en el órgano: por eso la aprobación es **agnóstica de tumor** (2017). Puede ser **síndrome de Lynch** (germinal) o esporádico por **hipermetilación de *MLH1*** (a menudo con *BRAF* V600E). Ver el [capítulo 5](#566--ejemplo-real-mmr-deficiente-predice-respuesta-a-inmunoterapia-diap-31).
</details>

<details><summary>6. Tres mecanismos por los que el microbioma intestinal contribuye a la oncogénesis. ¿Cuál es la evidencia clínica más sólida?</summary>

1. **Genotoxicidad directa**: la colibactina de *E. coli pks+* daña el ADN (firma SBS88).
2. **Señalización proliferativa e inflamación**: *Fusobacterium nucleatum* activa Wnt/β-catenina.
3. **Inmunomodulación**: el eje intestino-hígado recluta MDSC e inhibe a las NK (colangiocarcinoma); el microbioma también modula la respuesta a la inmunoterapia.

**Evidencia clínica más sólida (según Hanahan 2022)**: el **trasplante fecal de pacientes respondedores** devolvió la respuesta al anti-PD-1 en parte de los pacientes con **melanoma refractario** (Baruch y Davar, *Science* 2021; ensayos pequeños de fase I). ➕ Fuera del intestino, la evidencia más antigua es *H. pylori*: su erradicación reduce el cáncer gástrico.
</details>

---

### 6.26 ➕ Síndromes de cáncer hereditario

| Síndrome | Gen | Tumores principales | Herencia |
|---|---|---|---|
| **Li-Fraumeni** | *TP53* | Sarcomas, mama temprana, cerebro, corteza suprarrenal, leucemias | AD |
| **Retinoblastoma hereditario** | *RB1* | Retinoblastoma bilateral, osteosarcoma | AD |
| **Mama y ovario hereditario** | *BRCA1*, *BRCA2* | Mama, ovario, próstata, páncreas | AD |
| **Lynch** | *MLH1*, *MSH2*, *MSH6*, *PMS2*, *EPCAM* | Colorrectal, endometrio, ovario, estómago, vías urinarias | AD |
| **Poliposis adenomatosa familiar** | *APC* | Cientos a miles de pólipos; colorrectal casi seguro sin colectomía | AD |
| **Von Hippel-Lindau** | *VHL* | Carcinoma renal de células claras, hemangioblastomas, feocromocitoma | AD |
| **Neurofibromatosis 1** | *NF1* | Neurofibromas, gliomas ópticos, tumor maligno de vaina nerviosa | AD |
| **Neurofibromatosis 2** | *NF2* | Schwannomas vestibulares bilaterales, meningiomas | AD |
| **Gorlin** | *PTCH1* | Carcinomas basocelulares múltiples, meduloblastoma | AD |
| **Melanoma familiar** | *CDKN2A* | Melanoma, páncreas | AD |
| **Cáncer gástrico difuso hereditario** | *CDH1* | Gástrico difuso, mama lobulillar | AD |
| **Neoplasia endocrina múltiple 2** | *RET* | Carcinoma medular de tiroides, feocromocitoma | AD |
| **Ataxia-telangiectasia** | *ATM* | Linfomas, leucemias (y mama en portadoras) | AR |

⚠️ Casi todos los síndromes hereditarios se deben a **genes supresores**. La excepción clásica es ***RET*** en la **MEN2**: un **oncogén** con mutación germinal de ganancia de función (igual que *MET* en el carcinoma renal papilar hereditario). Por eso en la MEN2 se hace **tiroidectomía profiláctica** según la mutación.

🩺 **Señales de alarma de cáncer hereditario**: diagnóstico a edad temprana, tumores bilaterales o múltiples, varios familiares afectados en la misma rama, tumores raros (sarcoma infantil, cáncer de mama en hombres, carcinoma suprarrenal) y combinaciones típicas (colon + endometrio; mama + ovario).

---

### ✅ Verificación de datos de la clase (capítulo 6)

| Diapositiva | Dice | Verificación |
|---|---|---|
| 4 | Papiro de Edwin Smith ~1600 a. C.; Hipócrates; Hunter; Virchow; Goodman y Gilman | Correcto |
| 4 | "Años 50: terapias dirigidas iniciales" | Impreciso: las terapias dirigidas modernas empiezan con tamoxifeno (1977), trastuzumab (1998) e imatinib (2001) |
| 6 y 35 | "Más de 200 enfermedades" / "más de 100 trastornos" | Ambas cifras circulan; el NCI habla de más de 100 tipos |
| 8 | OncomiR "regulan a la baja protooncogenes" | Invertido: los oncomiR silencian supresores; los miARN supresores silencian oncogenes |
| 9 | "MYC en neuroblastoma"; HER2 en "rabdomiosarcoma" | En neuroblastoma se amplifica *MYCN*; el ejemplo clásico de *ERBB2* amplificado es mama (y gástrico) |
| 9 | Cuatro mecanismos; la figura pone "inserción viral" en lugar de captura de *enhancer* | Son cinco mecanismos distintos |
| 10 | "Esporádico: retinoblastoma unilateral adultos" | El retinoblastoma esporádico también es de la infancia (hacia los 2 años) |
| 12 | "RB1 perdido: CDK4/6 activos constitutivamente" | Sin Rb, E2F está libre sin necesidad de CDK4/6; por eso los inhibidores de CDK4/6 no sirven en tumores sin Rb |
| 13 | 2–8 drivers; 1,2 × 10⁻⁸; ~70 mutaciones *de novo*; +2 por año de edad paterna | Correcto (Vogelstein 2013; Kong 2012). Son tasas germinales, no tumorales |
| 15 | "3 tipos" de inestabilidad | Enumera cuatro |
| 15 | Cromoplexia = "ciclos ruptura-fusión-puente" | Son fenómenos distintos (BFB, cromotripsis, cromoplexia) |
| 15 | Pembrolizumab agnóstico para MSI-H en 2017 | Correcto |
| 18 | "Figura original del artículo (2011)"; "12 parámetros totales" | La figura es la de 2022, con 14 elementos (faltan las 2 características habilitantes de 2011) |
| 19 | "KRAS G12D/V (30 % cánceres)" (cita a Prior 2020) | Prior 2020: ~19 % de los pacientes tienen mutación en algún *RAS* |
| 20 | *TP53* mutado en > 50 %; R175H, R248W/Q | Aproximado (~50 %; 42 % en TCGA pancáncer). R175H y R248 son *hotspots* |
| 21 | "BCL-2 → venetoclax" en linfoma folicular; "BCL-XL → navitoclax" | Venetoclax está aprobado en LLC y LMA, no en linfoma folicular; navitoclax no está aprobado |
| 22 | Hayflick ~50 divisiones; TERT 85–90 %; ALT 10–15 % | Correcto como aproximación (Hayflick: 40–60) |
| 22 | VPH → cervicitis → carcinoma, como ejemplo de inflamación | El VPH transforma sobre todo por E6 y E7; la inflamación es secundaria |
| 24 | "Tumores > 0,2–2 mm: avasculares" | Al revés: hasta ~1–2 mm pueden ser avasculares |
| 24 | VHL mutado en ~90 % de carcinomas renales de células claras | Correcto como inactivación de *VHL* (mutación, metilación o pérdida) |
| 24 | 2 ATP frente a 36 ATP | 36 es el valor clásico; hoy se estima ~30–32 |
| 26 | "Cobertura 80x detecta clones del 1 %" | Se necesitan cientos a miles de lecturas para clones del 1 % |
| 22–26 | Inflamación como "Hallmark 5", inestabilidad genómica como "HM 10" | Son características habilitantes, no hallmarks |
| 30 | Senolíticos: navitoclax, dasatinib + quercetina | Experimentales, no aprobados |
| 32 | 20 M casos, 9,7 M muertes, 1 de 5, 35 M en 2050; top 5 | Correcto para GLOBOCAN 2022. GLOBOCAN 2024 (julio de 2026): 20,6 M y 9,8 M |
| 32 | Niños < 15 años: 400.000 casos | La OMS da ~400.000 casos para 0–19 años |
| 34 | LLA = 30 % de los casos pediátricos | Las leucemias suman ~30 %; la LLA sola ~25 % |
| 35 | "1 de cada 6 personas muere a causa del cáncer"; "tasa de mortalidad (70 %)" | 1 de cada 6 **muertes**; el 70 % es la proporción de muertes en países de ingresos bajos y medios |
| 37 | 117.620 casos; tasa 177,6 | Correcto (GLOBOCAN 2022) |
| 37 | 40.333 muertes ("INC 2023"); ~150.000 casos en 2030 | No verificable; GLOBOCAN 2022 estima 56.719 muertes |
| 37 | Risaralda con la mayor mortalidad ajustada (2015–2017) | Correcto (Cuenta de Alto Costo) |
| 37 | Plan de Choque "Minsalud + INC + OPS" | Circular Conjunta Externa 010 de 2024: Minsalud, INC y Supersalud |
| 41 | PARP en "resistencia a apoptosis" e "inmortalidad replicativa" | PARP corresponde a inestabilidad genómica (letalidad sintética); para inmortalidad, el ejemplo es imetelstat |
| 42 | mRNA-4157 "fase III activa"; cita *NEJM Evid* 2023 | La fase III (INTerpath-001) fue positiva en 2026; la fase IIb se publicó en *Lancet* 2024 |
| 44 | "Vogelstein 1990, *Science*"; "4–8 alteraciones driver" | Fearon y Vogelstein, *Cell* 1990; 2–8 drivers (Vogelstein 2013) |

---

### Autoevaluación (capítulo 6)

<details><summary>1. ¿Por qué una mutación en un oncogén basta, y en un gen supresor hacen falta dos?</summary>

El oncogén mutado produce una proteína hiperactiva que actúa aunque el otro alelo sea normal (ganancia de función, dominante a nivel celular). El supresor pierde su función, y el alelo normal restante sigue frenando: solo cuando se pierden los dos desaparece el freno (recesivo a nivel celular).
</details>

<details><summary>2. Nombra cinco formas de activar un oncogén con un ejemplo de cada una.</summary>

Mutación puntual (*KRAS* G12D), amplificación (*ERBB2* en mama, *MYCN* en neuroblastoma), translocación con fusión (*BCR-ABL1*, t(9;22)), captura de *enhancer* (*IGH*-*MYC*, t(8;14) en Burkitt) e inserción viral (promotor viral junto a *MYC*).
</details>

<details><summary>3. ¿Qué diferencia a un gatekeeper de un caretaker?</summary>

El gatekeeper (RB, p53, APC) controla directamente la proliferación o la muerte celular. El caretaker (BRCA1/2, MLH1, MSH2) mantiene la integridad del genoma; su pérdida no hace proliferar a la célula, pero acelera la acumulación de mutaciones en los gatekeepers.
</details>

<details><summary>4. Un tumor sin Rb, ¿responde a palbociclib? ¿Por qué?</summary>

No. Palbociclib impide que CDK4/6 fosforile a Rb. Si no hay Rb, E2F ya está libre y el fármaco no tiene nada que bloquear.
</details>

<details><summary>5. ¿Qué indica la firma SBS4 y qué la SBS6?</summary>

SBS4: exposición al tabaco. SBS6: deficiencia de reparación de apareamientos erróneos (MMR).
</details>

<details><summary>6. ¿Por qué los tumores con mutación de POLE responden muy bien a anti-PD-1?</summary>

La polimerasa pierde su actividad correctora y el tumor acumula más de 100 mutaciones por megabase. Muchas generan neoantígenos que los linfocitos T reconocen cuando se bloquea PD-1.
</details>

<details><summary>7. ¿Cuántos elementos tiene la figura de hallmarks de 2022 y cómo se reparten?</summary>

Catorce: 8 hallmarks (6 de 2000 + 2 de 2011), 2 características habilitantes de 2011 (inestabilidad genómica, inflamación) y 4 dimensiones de 2022 (plasticidad fenotípica, epigenética no mutacional, microbiomas polimórficos, células senescentes).
</details>

<details><summary>8. Explica por qué la pérdida de VHL produce un tumor muy vascularizado.</summary>

VHL es la ubiquitina-ligasa que marca a HIF-1α (hidroxilado por la PHD) para su degradación. Sin VHL, HIF se acumula aunque haya oxígeno y transcribe VEGF de forma continua: el tumor se comporta como si estuviera siempre en hipoxia.
</details>

<details><summary>9. ¿Por qué el efecto Warburg conviene al tumor si produce menos ATP?</summary>

Porque la glucólisis rápida genera ATP a gran velocidad y, sobre todo, deriva carbonos a la vía de las pentosas (ribosa y NADPH) y a la síntesis de lípidos y aminoácidos. El lactato además acidifica el microambiente y frena a los linfocitos.
</details>

<details><summary>10. ¿Qué es el 2-hidroxiglutarato y cómo causa cáncer?</summary>

Es un oncometabolito producido por IDH1/2 mutada. Inhibe las dioxigenasas que dependen de α-cetoglutarato (TET, desmetilasas de histonas), lo que hipermetila el ADN y las histonas y bloquea la diferenciación.
</details>

<details><summary>11. Ordena las fases de la inmunoedición y di en cuál se hace clínico el tumor.</summary>

Eliminación → equilibrio → escape. El cáncer se manifiesta en la fase de escape.
</details>

<details><summary>12. Clasifica las cuatro dimensiones de 2022.</summary>

Plasticidad fenotípica: nueva capacidad (hallmark). Reprogramación epigenética no mutacional y microbiomas polimórficos: características habilitantes. Células senescentes: tipo celular funcional del microambiente tumoral.
</details>

<details><summary>13. ¿Cuál es el cáncer más frecuente y cuál el más letal en el mundo? ¿Y en Colombia?</summary>

Mundo: pulmón en ambos casos. Colombia (GLOBOCAN 2024): mama es el más frecuente (seguido de próstata) y estómago el que más muertes causa.
</details>

<details><summary>14. ¿Por qué un inhibidor de PARP mata a la célula tumoral BRCA deficiente y no a las células normales del portador?</summary>

Por letalidad sintética. Las células normales del portador conservan un alelo funcional de *BRCA* y reparan por recombinación homóloga las roturas que deja la inhibición de PARP. La célula tumoral perdió el segundo alelo, no tiene esa vía y muere.
</details>

<details><summary>15. Un paciente de 30 años tiene cáncer colorrectal y su madre tuvo cáncer de endometrio a los 45. ¿Qué síndrome sospechas y qué estudio pedirías al tumor?</summary>

Síndrome de Lynch. Inmunohistoquímica de las proteínas MMR (MLH1, MSH2, MSH6, PMS2) o análisis de MSI en el tumor y, si hay deficiencia, estudio germinal.
</details>

<details><summary>16. ¿Qué excepción a la regla "los síndromes hereditarios se deben a supresores" debes recordar?</summary>

*RET* en la neoplasia endocrina múltiple 2: es un oncogén con mutación germinal de ganancia de función.
</details>

---

### Glosario (capítulo 6)

| Término | Definición |
|---|---|
| **ALT** | Alargamiento alternativo de telómeros por recombinación homóloga |
| **Característica habilitante** | Condición que facilita adquirir hallmarks (inestabilidad genómica, inflamación, epigenética no mutacional, microbiomas) |
| **Caretaker** | Gen supresor que mantiene la integridad del genoma (*BRCA1/2*, MMR) |
| **CIN** | Inestabilidad cromosómica: aneuploidía y reordenamientos |
| **Cromotripsis** | Fragmentación de uno o pocos cromosomas en un solo evento, con reensamblaje al azar |
| **Cromoplexia** | Reordenamientos encadenados entre varios cromosomas |
| **ctDNA** | ADN tumoral circulante en plasma; base de la biopsia líquida |
| **Driver** | Mutación que da ventaja selectiva a la célula tumoral |
| **EMT** | Transición epitelio-mesénquima |
| **Gatekeeper** | Gen supresor que controla directamente la proliferación (*RB1*, *TP53*, *APC*) |
| **Hallmark** | Capacidad funcional adquirida necesaria para el crecimiento maligno |
| **HIF** | Factor inducible por hipoxia; activa VEGF |
| **Letalidad sintética** | Perder uno de dos genes es tolerable; perder ambos es letal |
| **LOH** | Pérdida de heterocigosidad: el mecanismo más común del segundo golpe |
| **MSI** | Inestabilidad de microsatélites por MMR defectuoso |
| **Neoantígeno** | Péptido nuevo creado por una mutación tumoral y reconocible por los linfocitos T |
| **OncomiR** | microARN que promueve el cáncer silenciando supresores |
| **Passenger** | Mutación acompañante sin ventaja selectiva |
| **SASP** | Fenotipo secretor asociado a senescencia |
| **TMB** | Carga mutacional tumoral, en mutaciones por megabase |
| **Agnóstico de tumor** | Aprobación de un fármaco por biomarcador, sin importar el órgano |
| **Warburg (efecto)** | Glucólisis aeróbica en presencia de oxígeno |

---

### Referencias (capítulo 6)

De la clase:

- Hanahan D, Weinberg RA. The hallmarks of cancer. *Cell.* 2000;100:57-70.
- Hanahan D, Weinberg RA. Hallmarks of cancer: the next generation. *Cell.* 2011;144:646-674.
- Hanahan D. Hallmarks of cancer: new dimensions. *Cancer Discov.* 2022;12:31-46.
- Strachan T, Read A. *Human Molecular Genetics.* 5.ª ed. CRC Press; 2019.
- Vogelstein B, et al. Cancer genome landscapes. *Science.* 2013;339:1546-1558.
- Alexandrov LB, et al. The repertoire of mutational signatures in human cancer. *Nature.* 2020;578:94-101.
- Knudson AG. Mutation and cancer: statistical study of retinoblastoma. *PNAS.* 1971;68:820-823.
- Schreiber RD, et al. Cancer immunoediting. *Science.* 2011;331:1565-1570.
- Fearon ER, Vogelstein B. A genetic model for colorectal tumorigenesis. *Cell.* 1990;61:759-767.
- Greaves M, Maley CC. Clonal evolution in cancer. *Nature.* 2012;481:306-313.
- Prior IA, et al. The frequency of Ras mutations in cancer. *Cancer Res.* 2020;80:2969-2974.
- Baruch EN, et al. *Science.* 2021;371:602-609; Davar D, et al. *Science.* 2021;371:595-602.
- Baker DJ, et al. *Nature.* 2016;530:184-189.
- Bray F, et al. Global cancer statistics 2022. *CA Cancer J Clin.* 2024;74:229-263.
- Instituto Nacional de Cancerología. Cáncer en cifras 2023.

Usadas en la verificación y las ampliaciones:

- Sung H, et al. Global cancer statistics 2024: GLOBOCAN estimates for 34 cancers in 186 countries. *CA Cancer J Clin.* Publicado el 8 de julio de 2026. doi:10.3322/caac.70090. Resumen de la IARC: <https://www.iarc.who.int/news-events/global-cancer-statistics-2024-globocan-estimates-of-incidence-and-mortality-worldwide-for-34-cancers-in-186-countries>
- Global Cancer Observatory, ficha de Colombia (GLOBOCAN 2024, septiembre de 2026): <https://gco.iarc.who.int/media/globocan/factsheets/populations/170-colombia-fact-sheet.pdf>
- Datos de Colombia en GLOBOCAN 2022 (117.620 casos, 56.719 muertes): Consultorsalud, Circular 010 de 2024 <https://consultorsalud.com/imple-plan-de-choque-contra-cancer-circular-010/>
- Plan Decenal para el Control del Cáncer 2026–2035: Ministerio de Salud, julio de 2026 <https://www.minsalud.gov.co/Comunicaciones/noticias/2026/Paginas/Colombia-adopta-el-nuevo-Plan-Decenal-para-el-Control-del-Cancer-y-fortalece-la-respuesta-del-pais-frente-a-esta-enfermedad.aspx>
- Mortalidad por cáncer en Risaralda (Cuenta de Alto Costo): <https://caracol.com.co/emisora/2020/11/23/pereira/1606132690_101332.html>
- Siegel RL, et al. Cancer statistics, 2026. *CA Cancer J Clin.* 2026. <https://pubmed.ncbi.nlm.nih.gov/41528114/>
- Weber JS, et al. KEYNOTE-942. *Lancet.* 2024;403:632-644. INTerpath-001 (ESMO 2026): <https://www.onclive.com/view/adjuvant-intismeran-autogene-plus-pembrolizumab-improves-rfs-and-dmfs-in-melanoma>
- FDA. Aprobación de imetelstat (6 de junio de 2024): <https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-imetelstat-low-intermediate-1-risk-myelodysplastic-syndromes-transfusion-dependent>
- Estado de navitoclax (ensayos en mielofibrosis): <https://ctv.veeva.com/study/study-of-oral-navitoclax-tablet-in-combination-with-oral-ruxolitinib-tablet-versus-best-available-therapy-to-assess-change-in-sple>
- OMS. Cáncer infantil (nota descriptiva): <https://www.who.int/news-room/fact-sheets/detail/cancer-in-children>
- Kandoth C, et al. Mutational landscape and significance across 12 major cancer types. *Nature.* 2013;502:333-339.
- Kong A, et al. Rate of de novo mutations and the importance of father's age to disease risk. *Nature.* 2012;488:471-475.
- Baca SC, et al. Punctuated evolution of prostate cancer genomes (cromoplexia). *Cell.* 2013;153:666-677.

[↑ Volver al índice general](#índice-general)

---

## 7. Técnicas de biología molecular

> Clase del Prof. **Mauricio Rey Buitrago** (Dr. en Ciencias Farmacéuticas), curso de genética, Facultad de Medicina, Universidad Nacional de Colombia, 4 de agosto de 2026.
> Las citas *(Diap. N)* siguen la numeración del PDF de la clase (51 diapositivas; la tabla de contenidos de la diapositiva 2 usa otra numeración, por temas). Los símbolos 📌 ➕ ⚠️ ✅ 🩺 💊 🧠 se explican al [inicio de la guía](#cómo-usar-esta-guía).
> Es un capítulo transversal: las técnicas que aparecen aquí son las que se usan en la [genética del cáncer](#6-genética-del-cáncer-biología-molecular-hallmarks-y-perspectivas-terapéuticas) (FISH, NGS, biopsia líquida), la [bioinformática](#1-introducción-a-la-bioinformática-y-medicina-genómica) (exoma, bases de datos) y la [reparación del ADN](#5-mecanismos-de-reparación-del-adn-de-la-lesión-molecular-a-la-clínica) (MSI, BRCA).

---

### Índice (capítulo 7)

- [Lo esencial en un minuto](#lo-esencial-en-un-minuto-capítulo-7)
- [7.1 Fundamentos y objetivos del diagnóstico molecular](#71-fundamentos-y-objetivos-del-diagnóstico-molecular-diap-34)
- [7.2 Muestras biológicas para ADN](#72-muestras-biológicas-para-adn-diap-5)
- [7.3 Extracción de ADN](#73-extracción-de-adn-diap-69)
- [7.4 Electroforesis](#74-electroforesis-diap-1012)
- [7.5 Enzimas de restricción](#75-enzimas-de-restricción-diap-1316)
- [7.6 Ejercicio de digestión, resuelto](#76-ejercicio-de-digestión-resuelto-diap-17)
- [7.7 RFLP y diagnóstico de la hemoglobina S](#77-rflp-y-diagnóstico-de-la-hemoglobina-s-diap-1823)
- [7.8 Clonación: tipos y vectores](#78-clonación-tipos-y-vectores-diap-2426)
- [7.9 El plásmido y el flujo de la clonación](#79-el-plásmido-y-el-flujo-de-la-clonación-diap-2729)
- [7.10 Vectores lanzadera, transfección y genes reporteros](#710-vectores-lanzadera-transfección-y-genes-reporteros-diap-3033)
- [7.11 Bibliotecas de ADN e hibridación de colonias](#711-bibliotecas-de-adn-e-hibridación-de-colonias-diap-3435)
- [7.12 Blotting: Southern, Northern y Western](#712-blotting-southern-northern-y-western-diap-3637)
- [7.13 FISH](#713-fish-diap-38)
- [7.14 Microarreglos](#714-microarreglos-diap-3940)
- [7.15 PCR](#715-pcr-diap-4144)
- [7.16 Secuenciación: de Sanger a NGS](#716-secuenciación-de-sanger-a-ngs-diap-45)
- [7.17 Aplicaciones clínicas, terapia génica y OGM](#717-aplicaciones-clínicas-terapia-génica-y-ogm-diap-4648)
- [7.18 Identificación humana y genética forense](#718-identificación-humana-y-genética-forense-diap-49)
- [7.19 Flujo integrado y perspectivas](#719-flujo-integrado-y-perspectivas-diap-5051)
- [7.20 ➕ ¿Qué técnica uso para cada pregunta?](#720--qué-técnica-uso-para-cada-pregunta)
- [✅ Verificación de datos de la clase](#-verificación-de-datos-de-la-clase-capítulo-7)
- [Autoevaluación](#autoevaluación-capítulo-7)
- [Glosario](#glosario-capítulo-7)
- [Referencias](#referencias-capítulo-7)

---

### Lo esencial en un minuto (capítulo 7)

1. **Dos estrategias diagnósticas**: **indirecta** (productos génicos, cambios fisicoquímicos, hibridación) y **directa** (secuenciar el ADN).
2. **Extracción**: lisis → purificación → precipitación con alcohol y sal → lavado → almacenamiento. Pureza por **A260/A280 ≈ 1,8** (ADN). Una célula diploide tiene **~6 pg** de ADN; un espermatozoide, **~3 pg**.
3. **Métodos de extracción**: **orgánico** (fenol-cloroformo), **no orgánico** (*salting out* con proteinasa K y sales), **sílice** y **papel FTA**.
4. **Electroforesis**: el ADN es **negativo** (fosfatos) y migra al **ánodo (+)**; los fragmentos pequeños van más lejos. **Agarosa**: 200–50.000 pb, horizontal. **Poliacrilamida**: ≤ 500 pb, vertical, resuelve **1 base**.
5. **Enzimas de restricción**: cortan ADN de doble cadena en **secuencias palindrómicas**. **EcoRI** (G^AATTC) y **HindIII** (A^AGCTT) dejan **extremos cohesivos 5'**; **HaeIII** (GG^CC) deja **extremos romos**. Nombre: género (1 letra) + especie (2) + cepa + orden.
6. **RFLP de la Hb S**: la mutación **GAG→GTG** (Glu6Val) **destruye un sitio de MstII**. Normal: **1,2 kb**; portador: **1,2 + 1,4 kb**; enfermo: **1,4 kb**.
7. **Vectores por capacidad**: plásmido < 15 kb · fago λ < 20 · cósmido < 50 · BAC 150–300 · YAC 100–2.000 · MAC > 1.000.
8. **Plásmido**: **ori** + **marcador de selección** + **sitio de clonación múltiple** + **gen reportero (lacZ)**. **Colonia blanca = recombinante** (el inserto interrumpe lacZ).
9. **Blotting**: **Southern = ADN, Northern = ARN, Western = proteína** (🧠 SNOW DROP).
10. **FISH**: sondas fluorescentes sobre cromosomas en metafase o núcleos en interfase; detecta aneuploidías, deleciones, translocaciones y amplificaciones.
11. **Microarreglos**: dos fluoróforos (**Cy3 verde, Cy5 rojo**); el **log₂ (Cy5/Cy3)** mide la expresión relativa.
12. **PCR**: **95 °C** (desnaturalizar) → **50–65 °C** (alinear cebadores) → **72 °C** (extender con Taq); **2ⁿ copias**, ~30 ciclos.
13. **Sanger**: los **ddNTP** (sin 3'-OH) terminan la cadena; hoy con electroforesis capilar. **NGS**: millones de lecturas en paralelo.
14. **Forense**: **STR** amplificados por **PCR multiplex**; el núcleo **CODIS** pasó de 13 a **20 loci** en 2017.

---

### 7.1 Fundamentos y objetivos del diagnóstico molecular *(Diap. 3–4)*

📌 La biología molecular estudia la relación entre **ADN, ARN y proteínas**: cómo se almacena la información genética y cómo se ejecuta para determinar la función celular.

**Meta del diagnóstico molecular**: obtener información genética detallada y **detectar alteraciones** en el ADN, el ARN o las proteínas.

| Estrategia | Qué analiza | ➕ Ejemplos |
|---|---|---|
| **Indirecta** | Productos génicos, cambios fisicoquímicos o hibridación, para **inferir** la anomalía | Electroforesis de hemoglobina, RFLP, Southern, FISH, microarreglos |
| **Directa** | **Secuencia** del ADN: identifica la variante de forma explícita | Sanger, NGS |

---

### 7.2 Muestras biológicas para ADN *(Diap. 5)*

| Tipo | Ejemplos |
|---|---|
| **Biológicas** | Sangre, saliva, pelo con raíz, uñas, dientes, hueso, semen |
| **Rastros** | Chicle, colillas de cigarrillo, sobres y sellos postales (saliva) |
| **No invasivas** | Saliva, pelo, uñas: mínimo impacto para la persona |
| **Invasivas o forenses** | Sangre, hueso, dientes: exigen alto rigor técnico |
| **De interés forense** | **Sangre, semen y restos óseos** |

➕ Puntos útiles:
- El ADN de la sangre viene de los **leucocitos**: los eritrocitos maduros no tienen núcleo.
- El **pelo necesita raíz** (bulbo) para tener ADN nuclear; el tallo solo aporta **ADN mitocondrial**.
- **Hueso y dientes** conservan ADN durante años: se usan para identificar restos.
- La diapositiva muestra trigo, una placa de bacterias, *Drosophila* y una jirafa: **cualquier ser vivo** sirve como fuente de ADN.

---

### 7.3 Extracción de ADN *(Diap. 6–9)*

#### Tres principios *(Diap. 6)*

| Principio | Qué busca |
|---|---|
| **Recuperación máxima** | Obtener la mayor cantidad posible de material genético |
| **Eliminación de inhibidores** | Proteger el ADN de las **nucleasas** y retirar contaminantes que inhiben la PCR |
| **Calidad e integridad** | ADN de **doble cadena** íntegro, apto para PCR y secuenciación |

➕ Inhibidores típicos de la PCR: **hemo** (sangre), **heparina**, **melanina**, **ácidos húmicos** (suelo), **índigo** (tela de jean), restos de fenol o etanol. El **EDTA** del tampón protege el ADN porque **quela el Mg²⁺** que necesitan las ADNasas.

#### Pureza y concentración *(Diap. 6)*

| Medida | Valor esperado | Si está baja |
|---|---|---|
| **A260/A280** | **~1,8** para ADN; ~2,0 para ARN | **Proteínas** o fenol |
| ➕ **A260/A230** | ~2,0–2,2 | Sales caotrópicas (guanidina), carbohidratos, fenol |
| ➕ **Concentración** | **1 unidad de A260 = 50 µg/mL de ADN de doble cadena** (40 µg/mL de ARN) | — |

🧠 El ADN absorbe a **260 nm** (bases); las proteínas, a **280 nm** (triptófano y tirosina).

#### Cantidades teóricas *(Diap. 7)*

| Fuente | ADN |
|---|---|
| **Célula diploide** | **~6 pg** (➕ ~6,6 pg) |
| **Espermatozoide** (haploide) | **~3 pg** |
| **1 µL de sangre** | **30–60 ng** (➕ viene de los 4.000–11.000 leucocitos por µL) |
| **PCR de identificación** | **≈ 1 ng ≈ 350 espermatozoides** (unos 300 genomas haploides o 150 células diploides) |

✅ La diapositiva llama "PCR estándar" a 1 ng. Ese es el ADN óptimo de los **kits forenses de STR** (0,5–1 ng). En una PCR de rutina suelen usarse 10–100 ng de ADN genómico.

**Cálculo**: 1 ng ÷ 3 pg = 1.000 pg ÷ 3 pg ≈ **333 genomas haploides**.

#### Métodos de extracción *(Diap. 8–9)*

| Método | Principio | Ventaja | Desventaja |
|---|---|---|---|
| **Orgánico: fenol-cloroformo** | Las proteínas pasan a la fase orgánica o a la interfase; el ADN queda en la **fase acuosa** | Muy eficiente en muestras complejas | **Solventes tóxicos** |
| **No orgánico: *salting out*** | **Proteinasa K** digiere proteínas; **sales concentradas** las precipitan; el ADN se precipita con alcohol | Ideal para **sangre y tejidos**, sin solventes tóxicos | Pureza algo menor |
| **Sílice** (columnas, perlas magnéticas) | En sales caotrópicas el ADN se **une a la sílice**; se lava y se eluye con baja sal | **Alta pureza, automatizable** | Costo |
| **Papel FTA** | Papel tratado que **lisa las células y protege el ADN** | **Fácil transporte** y almacenamiento a temperatura ambiente | Poca cantidad |
| ➕ **Chelex** *(figura de la Diap. 9)* | Hervir la muestra con una resina quelante | Rápido (forense) | ADN de cadena sencilla, solo sirve para PCR |

➕ El **pH del fenol** decide qué se extrae: a **pH ~8** el ADN queda en la fase acuosa; el **fenol ácido** (pH 4–5) retiene el ADN en la interfase y deja el **ARN** arriba (base del TRIzol).

#### Protocolo universal de purificación *(Diap. 9)*

| # | Paso | Qué se hace |
|---|---|---|
| 1 | **Ruptura de membranas (lisis)** | Detergente, proteinasa K o calor liberan el material genético |
| 2 | **Aislamiento / purificación** | Se separa el ADN de proteínas y lípidos |
| 3 | **Precipitación** | **Alcohol (etanol o isopropanol) + sal**: el ADN se vuelve insoluble y se concentra |
| 4 | **Lavado** | Etanol al 70 % retira sales e impurezas |
| 5 | **Almacenamiento** | Resuspensión en **tampón** (➕ TE: Tris-EDTA) para estabilidad a largo plazo |

**En sangre** *(figura)*: lisis de eritrocitos → lisis celular → precipitación de proteínas → precipitación del ADN → lavado → hidratación.

**En tejido en parafina** *(Diap. 6, figura)*: desparafinar con **xileno** (dos veces) → tampón de lisis + **proteinasa K** → precipitación de proteínas → precipitar y lavar el ADN. ➕ La formalina **fragmenta** el ADN, por eso el de los bloques de parafina es de menor calidad.

🧠 **"Rompe, Separa, Precipita, Lava, Guarda."**

---

### 7.4 Electroforesis *(Diap. 10–12)*

📌 **Principio**: los **grupos fosfato** dan al ADN y al ARN **carga negativa proporcional a su longitud**. En un campo eléctrico **migran hacia el ánodo (+)** a través de una matriz porosa que actúa como tamiz: los fragmentos **pequeños avanzan más**.

🧠 **"Run to red"**: el ADN corre hacia el electrodo rojo (positivo).

| | **Agarosa** | **Poliacrilamida (PAGE)** |
|---|---|---|
| Formato | **Horizontal** | **Vertical** |
| Rango | **200–50.000 pb** | **≤ 500 pb** |
| Resolución | Baja (separación general) | **Alta: diferencia de 1 base** |
| Seguridad | **No tóxica**, manejo simple | **Monómeros tóxicos** (acrilamida, neurotóxica) |

➕ Detalles:
- A **mayor porcentaje** de agarosa, mejor separa fragmentos pequeños (en la figura, el gel al 2 % resuelve 60–500 pb mejor que el de 1 %).
- Siempre se corre un **marcador de peso molecular** (*ladder*) para estimar tamaños.
- Para fragmentos mayores de ~50 kb se usa **electroforesis en campo pulsado (PFGE)**.
- Variantes de PAGE en la figura: **SDS-PAGE** separa proteínas (el SDS les da carga negativa uniforme) y **urea-PAGE** separa ARN desnaturalizado.
- La **electroforesis capilar** (Sanger, STR) resuelve 1 pb de forma automatizada.

#### Métodos de detección *(Diap. 12)*

| Agente | Tipo | Características |
|---|---|---|
| **Bromuro de etidio (EtBr)** | **Intercalante** fluorescente con **luz UV** | Clásico y sensible para ADN y ARN; **mutágeno** |
| **SYBR Safe** | Fluorescente | **Menos tóxico**, sensibilidad similar al EtBr; ➕ se puede ver con luz azul (figura) |
| **Azul de Coomassie** | Colorimétrico | **Tiñe proteínas** (SDS-PAGE) |
| **Tinción de plata** | Colorimétrico | **Sensibilidad extrema**: detecta trazas de proteínas o ácidos nucleicos en PAGE (geles marrones de la figura) |

✅ La diapositiva dice que el Coomassie tiene "menor sensibilidad para la detección de ácidos nucleicos". El Coomassie **no se usa para ácidos nucleicos**: es un colorante de **proteínas**.

---

### 7.5 Enzimas de restricción *(Diap. 13–16)*

#### Definición *(Diap. 13)*

📌 **Endonucleasas** que reconocen **secuencias palindrómicas específicas** en el **ADN de doble cadena** y lo cortan **hidrolizando enlaces fosfodiéster**.

**Palíndromo**: la secuencia se lee igual en las dos cadenas en sentido 5'→3'. Ejemplo: EcoRI, 5'-GAATTC-3' / 3'-CTTAAG-5'.

➕ **Función natural**: son el "sistema inmune" de las bacterias contra los fagos (**sistema de restricción-modificación**). La bacteria **metila su propio ADN** en esos sitios para no cortarlo. Arber, Nathans y Smith recibieron el **Nobel de 1978**.

#### Tipos de extremos *(Diap. 13, 15)*

| Enzima | Sitio (^ = corte) | Extremo |
|---|---|---|
| **EcoRI** | G^AATTC | **Cohesivo**, saliente **5' AATT** |
| **HindIII** | A^AGCTT | **Cohesivo**, saliente **5' AGCT** |
| **PstI** *(figura)* | CTGCA^G | **Cohesivo**, saliente **3' TGCA** |
| **HaeIII** | GG^CC | **Romo** |
| **PvuII** *(figura)* | CAG^CTG | **Romo** |
| ➕ **BamHI** | G^GATCC | Cohesivo, 5' GATC |
| ➕ **BglII** | A^GATCT | Cohesivo, 5' GATC (compatible con BamHI) |
| ➕ **MstII** | CC^TNAGG | Cohesivo (usado en la Hb S) |

- **Cohesivos (*sticky ends*)**: colas de cadena sencilla que se aparean con cualquier extremo cortado por la misma enzima: **ligación eficiente y específica**.
- **Romos (*blunt ends*)**: ambas cadenas terminan al mismo nivel; se unen con cualquier otro extremo romo (**clonación inespecífica**), pero la ligación es menos eficiente.

✅ La diapositiva 15 dice que HindIII produce "extremos **asimétricos**". Sus extremos son tan simétricos como los de EcoRI: el sitio es palindrómico y ambas cadenas dejan el mismo saliente 5' AGCT.

➕ **Frecuencia esperada de un sitio** en ADN al azar: **4ⁿ**, con n = número de bases del sitio. Un sitio de 4 pb (HaeIII) aparece cada **256 pb**; uno de 6 pb (EcoRI), cada **4.096 pb**; uno de 8 pb, cada **65.536 pb**.

#### Nomenclatura *(Diap. 14)*

| Parte | Ejemplo en **EcoRI** |
|---|---|
| **Género** (1.ª letra, mayúscula) | **E** de *Escherichia* |
| **Especie** (2 primeras letras) | **co** de *coli* |
| **Cepa** | **R** de la cepa RY13 |
| **Orden de aislamiento** (número romano) | **I**: primera enzima aislada de esa cepa |

| Microorganismo | Enzima |
|---|---|
| *Escherichia coli* | EcoRI |
| *Bacillus amyloliquefaciens* | BamHI |
| *Bacillus globigii* | BglII |
| *Haemophilus aegyptius* | HaeII, HaeIII |
| *Haemophilus influenzae* | HindII (➕ y HindIII; la "d" es de la cepa Rd) |
| *Brevibacterium albidum* | BalI |

#### Aplicaciones *(Diap. 16)*

| Área | Uso |
|---|---|
| **Diagnóstico y caracterización** | **RFLP** y **mapas de restricción** |
| **Ingeniería genética** | **Clonación** y **bibliotecas genómicas** |
| **Hibridación** | Preparar el ADN para **Southern blot** |

✅ La diapositiva incluye el **Northern** entre las aplicaciones. Las enzimas de restricción cortan **ADN de doble cadena**: en un Northern el ARN **no se digiere**. Como mucho, se usan para preparar o linealizar el molde de la sonda.

➕ La **ADN ligasa** sella el enlace fosfodiéster entre el vector y el inserto (la de T4 usa ATP). Tras la ligación se forma el **ADN recombinante** (figuras de la diapositiva 16).

---

### 7.6 Ejercicio de digestión, resuelto *(Diap. 17)*

La diapositiva da una secuencia de **350 pb** (molécula lineal) y tres enzimas: **HaeIII (GG^CC)**, **EcoRI (G^AATTC)** y **HindIII (A^AGCTT)**. La secuencia completa, numerada:

```
   1 TTTTTTTTATATACCATCAGCACTTGCTATGAGGGCCAGCGTAGATCGGTCCAAGTCCACCTAGGGTATA
  71 CCGCGCCCCGGGACGAAGATATATATATATAGTACCACTCACTTGGAATTCCTGCGCGCGCGCGCCTACC
 141 TATATATAGTACAAAGCTTGATATAATGCCACTCCAGTCACTTGCTATGACTAGGAATTAGCGAAAGGGG
 211 GTTAATCGGTCCCCACTCCTTGCTCATGATTGTGCGTAGGAATTCATCGGTCCCCGCTATAATATTCCCA
 281 CTCAGCTTGCTATGATTGTAGCGTAATCGGTCCATTTTTTTTCCCGGGCCATCAGCACTTGCTATGATTG
```

#### Solución

| Enzima | Sitios (posición del primer nucleótido) | Corte después del nucleótido | Fragmentos |
|---|---|---|---|
| **HaeIII** | 34 (…GAGG**GGCC**AG…) y 327 (…CCCG**GGCC**AT…) | 35 y 328 | **35 + 293 + 22 pb** |
| **EcoRI** | 116 (…TTG**GAATTC**CT…) y 250 (…AGG**GAATTC**AT…) | 116 y 250 | **116 + 134 + 100 pb** |
| **HindIII** | 154 (…ACA**AAGCTT**GA…) | 154 | **154 + 196 pb** |
| **Las tres juntas** | 5 cortes | 35, 116, 154, 250, 328 | **35 + 81 + 38 + 96 + 78 + 22 pb** (6 fragmentos) |

⚠️ **Trampa del ejercicio**: en la posición 195 aparece **GGAATTAG**. Se parece al sitio de EcoRI, pero **GAATTA ≠ GAATTC**: la enzima no corta ahí. Las enzimas de restricción exigen la secuencia exacta.

📌 **Reglas para contar fragmentos**:
- **ADN lineal**: n cortes → **n + 1 fragmentos**.
- **ADN circular** (plásmido): n cortes → **n fragmentos**.
- La suma de los fragmentos debe dar el tamaño total (35 + 293 + 22 = 350).

#### Cómo se construye un mapa de restricción *(figura de la Diap. 17)*

1. Se digiere por separado con cada enzima y luego con las dos juntas (**digestión doble**).
2. Se miden los fragmentos en un gel.
3. Se buscan los órdenes compatibles: cada fragmento de la digestión simple debe ser la suma de fragmentos de la doble.
4. Ejemplo de la figura, una molécula lineal de 5.000 pb:
   - *Bam* sola: 3.000 + 1.500 + 500 (dos sitios).
   - *Eco* sola: 4.000 + 1.000 (un sitio).
   - Las dos juntas: 2.000 + 1.500 + 1.000 + 500.
   - Lectura: el fragmento *Bam* de 3.000 desaparece y aparecen 2.000 + 1.000, así que **el sitio *Eco* está dentro de él**. Los fragmentos *Bam* de 1.500 y 500 no cambian.
   - Quedan dos mapas posibles: 1.000 · 2.000 · 1.500 · 500 o 1.000 · 2.000 · 500 · 1.500. Para decidir hace falta otra enzima o una sonda. Un mapa leído al revés es el mismo mapa.

---

### 7.7 RFLP y diagnóstico de la hemoglobina S *(Diap. 18–23)*

#### Polimorfismo de longitud de fragmentos de restricción (RFLP) *(Diap. 18)*

📌 Una variante puede **crear o destruir un sitio de restricción**. Entonces la enzima produce **fragmentos de distinto tamaño** en las personas con y sin la variante.

| Paso | Qué se hace |
|---|---|
| 1 | **Extracción** del ADN (y, en la versión moderna, **PCR** de la región, a veces con cebadores marcados) |
| 2 | **Digestión enzimática** |
| 3 | **Electroforesis** |
| 4 | **Análisis de las bandas**: clásicamente, **Southern blot** con una **sonda** de la región; hoy, detección láser de los productos marcados |

#### La anemia falciforme *(Diap. 19–21)*

| Nivel | Qué pasa |
|---|---|
| **ADN** | Una base errónea en el gen de la **β-globina** (*HBB*): **GAG → GTG** |
| **Proteína** | **Valina en lugar de ácido glutámico en la posición 6** de la cadena β (**HbS**) |
| **Molécula** | La HbS desoxigenada **polimeriza**: forma **fibras tubulares insolubles** |
| **Célula** | El eritrocito se deforma en **hoz** (falciforme), se vuelve rígido y frágil |

➕ En la nomenclatura HGVS, que cuenta desde la metionina inicial, la variante es **c.20A>T, p.Glu7Val** (rs334). "Glu6Val" es la numeración clásica de la proteína madura.

**Consecuencias** *(Diap. 21)*:

| Mecanismo | Manifestaciones |
|---|---|
| **Destrucción rápida de los eritrocitos** → **anemia** | Cansancio, dilatación cardíaca y falla cardíaca, **hiperactividad de la médula ósea** (cráneo en torre, "turricefalia"), desnutrición (marasmo), lesión renal |
| **Oclusión de vasos** por eritrocitos falciformes | Daño muscular y articular ("reumatismo"), dolor abdominal, **daño cerebral** (parálisis), **daño pulmonar** (neumonía), lesión cardíaca y renal |
| **Secuestro en el bazo** | Esplenomegalia → **fibrosis del bazo** |

#### El RFLP con MstII *(Diap. 22–23)*

📌 La enzima **MstII** reconoce **CCTNAGG**. La secuencia normal de los codones 5–7 es **CCT GAG G**AG: contiene el sitio. La mutación (**CCT GTG G**AG) lo **destruye**.

| Alelo | Sitios de MstII en la región | Fragmento que detecta la sonda |
|---|---|---|
| **βA (normal)** | Tres sitios | **1,2 kb** (➕ más un fragmento de 0,2 kb que la sonda no ve) |
| **βS (falciforme)** | Se pierde el sitio central | **1,4 kb** (1,2 + 0,2) |

| Genotipo | Bandas |
|---|---|
| **Normal (AA)** | **1,2 kb** |
| **Portador (AS)** | **1,2 kb + 1,4 kb** |
| **Enfermo (SS)** | **1,4 kb** |

🧠 **"La S Suprime el Sitio y la banda Sube de tamaño."**

➕ La misma mutación destruye un sitio de **DdeI** (C^TNAG), la enzima más usada hoy en la **PCR-RFLP** de la Hb S. En el tamizaje neonatal se usa sobre todo **HPLC o electroforesis de hemoglobina**.

💊 ➕ Tratamientos que conectan con este capítulo: **hidroxiurea** (aumenta la hemoglobina fetal), y desde diciembre de 2023 dos terapias génicas aprobadas por la FDA: **exagamglogén autotemcel** (Casgevy; edición con **CRISPR-Cas9** del *enhancer* eritroide de *BCL11A* para reactivar la hemoglobina fetal) y **lovotibeglogén autotemcel** (Lyfgenia; **vector lentiviral** con una β-globina antifalciforme).

---

### 7.8 Clonación: tipos y vectores *(Diap. 24–26)*

#### Tres significados de "clonación" *(Diap. 24)*

| Tipo | Objetivo | Producto |
|---|---|---|
| **Genética (molecular)** | Copias idénticas de un gen o fragmento de ADN | Fragmentos para investigación y **proteínas recombinantes** |
| **Reproductiva** | Un organismo genéticamente idéntico | Un organismo viable (➕ la oveja Dolly, 1996) |
| **Terapéutica** | Células madre para tratamientos | **Células pluripotentes** para generar tejidos |

**Clonación terapéutica** *(figura)*: se transfiere el núcleo de una célula adulta del paciente a un **óvulo enucleado** (➕ transferencia nuclear somática), un pulso eléctrico inicia el desarrollo embrionario, se extraen las células madre y se diferencian en el tejido necesario (corazón, riñón, médula espinal, células productoras de insulina). El trasplante **no se rechaza** porque el ADN es del propio paciente.

➕ Las **iPSC** (Yamanaka, 2006) obtienen células pluripotentes reprogramando células adultas, sin óvulos ni embriones. Ver el [capítulo 2](#23-principios-de-las-familias-de-genes-del-desarrollo-diap-1218).

#### Vectores de clonación *(Diap. 25–26)*

📌 Un **vector** es una molécula de ADN que transporta el fragmento de interés a una célula huésped y se replica en ella. Se elige según el **tamaño del inserto**.

| Vector | Capacidad máxima | Huésped | Elementos clave |
|---|---|---|---|
| **Plásmido** | **< 15 kb** | Bacteria | ori, resistencia a antibiótico (Amp<sup>R</sup>), lacZ, sitio de clonación múltiple |
| **Fago lambda (λ)** | **< 20 kb** | Bacteria | Brazos izquierdo y derecho, **sitios cos**; el inserto reemplaza la región central |
| **Cósmido** | **< 50 kb** | Bacteria | Plásmido con **sitios cos**: se empaqueta en cabezas de fago λ |
| **BAC** (cromosoma artificial bacteriano) | **150–300 kb** | Bacteria | Basado en el **plásmido F** (una copia por célula, estable); resistencia a cloranfenicol |
| **YAC** (cromosoma artificial de levadura) | **100–2.000 kb** | Levadura | **ARS** (origen), **CEN** (centrómero), **TEL** (telómeros), marcadores de selección |
| **MAC** (cromosoma artificial de mamífero) | **> 1.000 kb** | Células de mamífero | Centrómero, telómeros, orígenes de mamífero |

🧠 **"Pocos Fagos Cosen Bien Ya Mucho"**: **P**lásmido < **F**ago < **C**ósmido < **B**AC < **Y**AC < **M**AC.

- YAC: desarrollado por **Burke, Carle y Olson (1987)**; se replica dentro de la levadura.
- BAC: se replica dentro de la bacteria. ✅ La figura lo atribuye a "Melsimon et al. 1992": lo desarrollaron **Shizuya et al. (1992) en el laboratorio de Mel Simon**. ➕ Los BAC fueron la base del Proyecto Genoma Humano porque son más estables que los YAC (que tienden a reordenarse y formar quimeras).
- ✅ La diapositiva 25 escribe "kba"; la unidad es **kb** (kilobases).

➕ **Vector de clonación frente a vector de expresión**: el de expresión agrega un **promotor** adecuado al huésped, un sitio de unión al ribosoma (o secuencia de Kozak en eucariotas) y un terminador, para **producir la proteína**.

---

### 7.9 El plásmido y el flujo de la clonación *(Diap. 27–29)*

#### Anatomía del plásmido *(Diap. 27)*

| Elemento | Función |
|---|---|
| **Origen de replicación (ori)** | Replicación **autónoma** dentro de la bacteria |
| **Marcador de selección** (Amp<sup>R</sup>, Tet<sup>R</sup>) | Solo sobreviven en el antibiótico las bacterias que tienen el plásmido |
| **Sitio de clonación múltiple (MCS)** | Muchos sitios de restricción únicos donde insertar el ADN |
| **Gen reportero (lacZ)** | Cribado visual: indica si el inserto entró |

#### Selección azul-blanca *(Diap. 28)*

| Colonia | Qué tiene | Por qué |
|---|---|---|
| **Azul** | Plásmido **sin inserto** | *lacZ* intacto → β-galactosidasa funcional → corta **X-gal** → color azul |
| **Blanca** | Plásmido **recombinante** | El inserto **interrumpe *lacZ*** → no hay β-galactosidasa → colonia blanca |

⚠️ Son dos filtros distintos: el **antibiótico** selecciona las bacterias que tienen **plásmido**; el **color** distingue cuáles tienen **inserto**.

➕ El medio lleva también **IPTG**, que induce la expresión de *lacZ*.

#### Flujo de clonación *(Diap. 28–29)*

```
1. Cortar vector e inserto con las mismas enzimas (p. ej., EcoRI y PvuII)
2. Purificar los fragmentos por electroforesis en agarosa
3. Ligar con ADN ligasa (+ ATP) → plásmido recombinante
4. Transformar bacterias "competentes" (CaCl₂ + choque térmico)
5. Sembrar en agar con antibiótico (ampicilina o tetraciclina)
6. Las células sin plásmido mueren; cada colonia sobreviviente es un clon con copias del mismo plásmido recombinante
```

➕ Usar **dos enzimas distintas** (como EcoRI y PvuII en la figura) permite **clonación direccional**: el inserto solo entra en una orientación y el vector no puede volver a cerrarse sobre sí mismo. Con una sola enzima, se trata el vector con **fosfatasa alcalina** para evitar que se religue vacío.

---

### 7.10 Vectores lanzadera, transfección y genes reporteros *(Diap. 30–33)*

#### Vectores lanzadera *(Diap. 30)*

📌 Se replican en **dos sistemas distintos**, normalmente *E. coli* (procariota) y levadura o células de mamífero (eucariota). Se manipulan rápido en la bacteria y luego se expresan en el sistema complejo.

Elementos de un vector lanzadera de levadura *(figura)*: origen y resistencia a antibiótico **para la bacteria**, origen de replicación **de levadura**, gen de selección en levadura (síntesis de **leucina**), **centrómero de levadura** y sitio de clonación múltiple.

Uso: expresión de **proteínas recombinantes** y transferencia de genes con vectores virales modificados (terapia génica).

#### Métodos de transferencia de genes *(Diap. 31–32)*

➕ Vocabulario:
- **Transformación**: introducir ADN en **bacterias** (o levaduras).
- **Transfección**: introducir ácidos nucleicos en **células eucariotas** por métodos no virales.
- **Transducción**: introducirlos **con un virus**.

| Tipo | Método | Cómo funciona |
|---|---|---|
| **Químico** | **Lipofección** | Lípidos catiónicos forman complejos con el ADN (liposomas); entran por **endocitosis** y se liberan del endosoma |
| | **Coprecipitado de fosfato de calcio** | El ADN precipita con calcio y la célula lo capta |
| | Polímeros catiónicos (➕ PEI, DEAE-dextrano) | Complejos con el ADN |
| **Físico** | **Electroporación** | Pulsos eléctricos abren **poros transitorios** en la membrana |
| | **Microinyección** | Inyección directa en el núcleo |
| | **Biolística** ("pistola de genes") | **Microproyectiles** de oro o tungsteno recubiertos de ADN (➕ muy usada en plantas) |
| **Biológico** | **Transducción viral** | Lentivirus, retrovirus, adenovirus, ➕ virus adenoasociados (AAV) |

✅ La diapositiva dice que la transducción viral da una entrega "altamente eficiente y **estable**". La estabilidad depende del virus: **lentivirus y retrovirus se integran** en el genoma (expresión estable); **adenovirus y AAV quedan como episomas** en su mayoría (expresión transitoria o más corta en células que se dividen).

#### Genes reporteros *(Diap. 33)*

📌 Indicadores que se fusionan a la secuencia que se quiere estudiar (por ejemplo, un **promotor**) para medir la **actividad transcripcional**, la eficiencia de traducción o la **localización** de la proteína.

| Reportero | Proteína | Cómo se detecta |
|---|---|---|
| **LacZ** | β-galactosidasa | **X-gal → color azul** |
| **CAT** | Cloranfenicol acetiltransferasa | Cloranfenicol marcado + **cromatografía en capa fina (TLC)** con extracción orgánica |
| **LUC** | **Luciferasa** | **Luciferina + ATP + O₂ → luz** (luminómetro); muy sensible |
| **GFP** | Proteína verde fluorescente | **Fluorescencia sin sustrato**; sirve en células vivas y para ver la localización |
| **SEAP** | Fosfatasa alcalina **secretada** | Se mide en el **medio de cultivo** por luminiscencia, sin lisar las células |

➕ La GFP viene de la medusa *Aequorea victoria*; Shimomura, Chalfie y Tsien recibieron el **Nobel de Química 2008**.

✅ Las cifras "100 % de sensibilidad" y "tiempo real" de la diapositiva son frases de diseño: ningún reportero tiene 100 % de sensibilidad. GFP y luciferasa sí permiten seguir la expresión en células vivas.

---

### 7.11 Bibliotecas de ADN e hibridación de colonias *(Diap. 34–35)*

#### Construcción de una biblioteca *(Diap. 34)*

📌 Una **biblioteca** es una colección de clones que, en conjunto, contiene el genoma (biblioteca **genómica**) o los ARNm expresados (biblioteca **de ADNc**) de un organismo o tejido.

| # | Paso | Qué se hace |
|---|---|---|
| 1 | **Digestión** | Cortar vector e inserto con enzimas de restricción para crear extremos complementarios |
| 2 | **Ligadura** | La **ADN ligasa** une covalentemente inserto y vector: moléculas recombinantes |
| 3 | **Transformación** | Introducir el ADN en células **competentes** |
| 4 | **Siembra selectiva** | Medio que solo deja crecer las células con el vector |
| 5 | **Análisis de clones** | **PCR o hibridación** para encontrar el inserto buscado |

El éxito depende de la **eficiencia de la ligadura** y de la **competencia** de las bacterias.

➕ **Genómica frente a ADNc**:

| | **Biblioteca genómica** | **Biblioteca de ADNc** |
|---|---|---|
| Origen | ADN genómico fragmentado | **ARNm → transcriptasa inversa → ADNc** |
| Contiene | Todo: exones, **intrones**, regiones reguladoras | Solo genes **expresados** en ese tejido, **sin intrones** |
| Sirve para | Estudiar la estructura del gen | **Expresar la proteína en bacterias** |

🩺 ➕ Por eso la **insulina humana recombinante** (la figura de la diapositiva; aprobada en 1982, el primer fármaco recombinante) se produce a partir de ADNc: las bacterias **no hacen *splicing*** y no podrían procesar un gen humano con intrones.

#### Hibridación de colonias *(Diap. 35)*

📌 Localiza la colonia que contiene la secuencia buscada en una biblioteca. ➕ Descrita por Grunstein y Hogness (1975).

| # | Paso |
|---|---|
| 1 | Crecer las colonias en una placa (placa maestra) |
| 2 | Apoyar un filtro de **nitrocelulosa o nailon** (réplica) |
| 3 | Retirar el filtro |
| 4 | **Lisar las bacterias y desnaturalizar el ADN** en el filtro |
| 5 | Agregar la **sonda marcada** (isótopos o fluorocromos) |
| 6 | Detectar por **autorradiografía** y volver a la placa maestra a buscar la colonia positiva |

**Principio**: la **hibridación** selectiva de una sonda marcada con su secuencia complementaria inmovilizada. La sonda puede ser de **ADN o ARN**.

➕ La figura inferior muestra sondas fluorescentes modernas: la **baliza molecular** (*molecular beacon*), una horquilla con fluoróforo y apagador que solo brilla al hibridar, y las sondas **FRET**. Se usan en la PCR en tiempo real.

---

### 7.12 Blotting: Southern, Northern y Western *(Diap. 36–37)*

📌 Se separan las moléculas (casi siempre por electroforesis), se **transfieren a una membrana** y se detecta la molécula diana con una sonda o un anticuerpo.

| Técnica | Detecta | Separación | Sonda | ➕ Usos clínicos o de investigación |
|---|---|---|---|---|
| **Southern** (Edwin Southern, 1975) | **ADN** | Digestión + agarosa + desnaturalización alcalina | ADN o ARN marcado | RFLP; **expansiones grandes** que la PCR no amplifica (X frágil con más de 200 CGG); reordenamientos y clonalidad |
| **Northern** (1977) | **ARN** | Gel **desnaturalizante** (formaldehído) | ADN o ARN marcado | **Tamaño y abundancia** de un ARNm, splicing alternativo |
| **Western** (1979) | **Proteínas** | **SDS-PAGE** | **Anticuerpos** (primario y secundario marcado) | Confirmar expresión de una proteína y su tamaño |
| **Dot/slot blot** | ADN, ARN o proteína | **Sin electroforesis**: la muestra se aplica directo | Sonda o anticuerpo | Tamizaje rápido de muchas muestras |

🧠 **SNOW DROP**: **S**outhern–**D**NA, **N**orthern–**R**NA, **O**–**O**, **W**estern–**P**rotein.

⚠️ "Southern" es un **apellido**; Northern y Western son **juegos de palabras** con los puntos cardinales.

#### Flujo del Northern blot *(Diap. 37)*

1. **Extracción del ARN** (sin ARNasas).
2. **Electroforesis** desnaturalizante.
3. **Transferencia** a la membrana.
4. **Generación de la sonda**: la clase usa el sistema **pGEM-T** y nucleótidos marcados. ➕ pGEM-T es un vector de clonación T/A con promotores **T7 y SP6** que permite sintetizar **sondas de ARN** por transcripción *in vitro*.
5. **Hibridación**.
6. **Visualización**.

✅ La diapositiva califica al Northern de "cuantitativo". Es **semicuantitativo**: compara la abundancia relativa entre muestras. Hoy la cuantificación de ARN se hace sobre todo con **RT-qPCR** y **RNA-seq**.

---

### 7.13 FISH *(Diap. 38)*

📌 **Hibridación *in situ* fluorescente**: sondas marcadas con **fluorocromos** se unen a secuencias complementarias en **cromosomas metafásicos** o **núcleos en interfase**, y se ven al microscopio de fluorescencia.

| Sobre qué | Ventaja | ➕ Ejemplos |
|---|---|---|
| **Núcleos en interfase** | No requiere cultivo; rápido; sirve en tejido | **Amplificación de *HER2*** en cáncer de mama; aneuploidías prenatales rápidas (13, 18, 21, X, Y) |
| **Cromosomas en metafase** | Muestra **dónde** está la secuencia | Localizar un gen; confirmar una translocación |

**Detecta**: anomalías **numéricas** (trisomías) y **estructurales** (deleciones, duplicaciones, translocaciones, amplificaciones).

➕ Tipos de sondas: **centroméricas** (contar cromosomas), **de locus específico** (microdeleciones, amplificaciones), de **fusión** (BCR-ABL) o de **separación** (*break-apart*, para reordenamientos de *ALK* o *ROS1*), y de **pintado cromosómico** completo.

✅ La diapositiva da a la FISH una "resolución > 5 Mb". Esa es la resolución del **cariotipo con bandas G** (~5–10 Mb). La FISH es mucho más fina: **~1–3 Mb** para ordenar sondas en metafase y **~50 kb–1 Mb** en interfase. Por eso detecta **microdeleciones invisibles en el cariotipo**, como la de **22q11.2** (~3 Mb) o la del síndrome de **Williams** (7q11.23, ~1,5 Mb).

⚠️ La FISH solo responde la pregunta que se le hace: hay que **sospechar la región** y elegir la sonda. Para buscar en todo el genoma se usa un **microarreglo**.

---

### 7.14 Microarreglos *(Diap. 39–40)*

#### Principio *(Diap. 39)*

| Elemento | Qué es |
|---|---|
| **Sustrato sólido** | Miles de **sondas de ADN** inmovilizadas que hibridan **a la vez** con la muestra |
| **Marcaje diferencial** | Dos fluoróforos: **Cy3 (verde)** y **Cy5 (rojo)**, para comparar dos estados biológicos |
| **Aplicaciones** | **Expresión génica**, detección de **SNP**, plataformas de oligonucleótidos |

#### Análisis de los datos *(Diap. 40)*

1. Se extrae el ARN de las dos muestras, se hace **transcripción inversa** y se marca cada ADNc con un fluoróforo.
2. Se mezclan cantidades iguales y se hibridan en el chip.
3. Se escanea con láser: **Cy3 a 532 nm** y **Cy5 a 633 nm**.
4. Se calcula la razón **Cy5/Cy3** y su **log₂**.
5. Se **agrupan** (*clustering*) los genes con patrones parecidos.

| Cy3 | Cy5 | Cy5/Cy3 | log₂ | Color | Interpretación |
|---|---|---|---|---|---|
| 200 | 10.000 | 50 | **+5,64** | **Rojo** | Mucho más expresado en la muestra Cy5 |
| 4.800 | 4.800 | 1 | **0** | Amarillo en la imagen (negro en el mapa de calor) | Igual en ambas |
| 9.000 | 300 | 0,03 | **−4,91** | **Verde** | Mucho más expresado en la muestra Cy3 |

📌 El **log₂** hace simétricos los cambios: el doble = **+1**; la mitad = **−1**.

🧠 **"Rojo = sube en la muestra roja (Cy5); verde = sube en la verde (Cy3)."**

➕ 🩺 **Microarreglo cromosómico** (CGH array o de SNP): se compara el ADN del paciente con uno de referencia para detectar **variaciones del número de copias** (deleciones y duplicaciones de decenas a cientos de kb) en todo el genoma. Es la prueba de **primera línea** en discapacidad intelectual, autismo y anomalías congénitas múltiples. ⚠️ **No detecta translocaciones balanceadas** (no cambia el número de copias). Para expresión génica, la **RNA-seq** ha reemplazado en gran parte a los microarreglos.

---

### 7.15 PCR *(Diap. 41–44)*

📌 La **reacción en cadena de la polimerasa** amplifica *in vitro* un segmento de ADN definido por dos **cebadores**. A partir de muy poco ADN genera millones de copias.

#### Componentes ➕

ADN molde · **dos cebadores** (directo y reverso) · **dNTP** · **Mg²⁺** · tampón · **ADN polimerasa termoestable** (Taq).

#### El ciclo

| Paso | Temperatura | Qué pasa |
|---|---|---|
| **1. Desnaturalización** | **94–96 °C** | Se separan las dos cadenas |
| **2. Alineamiento (*annealing*)** | **50–65 °C** | Los cebadores se unen a sus secuencias complementarias (➕ ~5 °C por debajo de su Tm) |
| **3. Extensión** | **72 °C** | La **Taq polimerasa** sintetiza la cadena nueva desde el extremo 3' del cebador (➕ ~1 kb por minuto) |

- Se repite **20–40 veces** (~30 ciclos).
- Crecimiento **exponencial: 2ⁿ**. Tras 30 ciclos, en teoría, **2³⁰ ≈ 10⁹ copias** por molécula molde. ➕ En la práctica la reacción llega a una **meseta** porque se agotan los reactivos.

#### Qué pasa en los primeros ciclos *(Diap. 42–44)*

| Ciclo | Productos |
|---|---|
| **1** | Cadenas "largas": empiezan en el cebador pero no tienen final definido |
| **2** | Aparecen las primeras **cadenas sencillas de longitud exacta** (entre los dos cebadores) |
| **3** | Aparecen las primeras **2 moléculas de doble cadena de longitud exacta** |
| **n** | Moléculas de longitud exacta: **2ⁿ − 2n**; dominan por completo a partir de unos pocos ciclos |

➕ Kary **Mullis** inventó la PCR en 1983 (**Nobel de Química 1993**). La **Taq** viene de *Thermus aquaticus*, una bacteria de aguas termales de Yellowstone; al resistir 95 °C, ya no hay que añadir enzima en cada ciclo.

#### Variantes ➕

| Variante | Qué hace | Ejemplo |
|---|---|---|
| **RT-PCR** | ARN → ADNc (transcriptasa inversa) → PCR | Transcritos de *BCR-ABL1*; virus ARN |
| **PCR en tiempo real (qPCR)** | Mide la fluorescencia en cada ciclo; el **Ct** (ciclo umbral) es menor cuanto más molde hay | **Carga viral**, enfermedad mínima residual, SARS-CoV-2 |
| **Multiplex** | Varios pares de cebadores a la vez | **STR forenses** |
| **Anidada** | Segunda PCR con cebadores internos | Más sensibilidad y especificidad |
| **Digital** | Divide la muestra en miles de microrreacciones | **Cuantificación absoluta**; ADN tumoral circulante |
| **Alelo-específica** | Un cebador solo funciona con una variante | Genotipar mutaciones puntuales |

⚠️ La PCR es tan sensible que un **amplicón contaminante** produce falsos positivos: áreas separadas, puntas con filtro y **controles negativos** en cada corrida.

---

### 7.16 Secuenciación: de Sanger a NGS *(Diap. 45)*

| Etapa | Idea clave |
|---|---|
| **Método de Sanger** (1977) | Determina la secuencia por **terminación controlada de la cadena** |
| **ddNTP** | Didesoxinucleótidos **sin grupo hidroxilo en 3'**: cuando la polimerasa los incorpora, **no puede añadir el siguiente nucleótido** y la cadena se detiene |
| **Automatización capilar** | ddNTP marcados con **cuatro fluoróforos** y **electroforesis capilar**: lectura rápida en un solo tubo |
| **NGS** | Secuenciación **masiva en paralelo**: millones de fragmentos a la vez |

📌 En Sanger, la mezcla tiene **muchos dNTP y pocos ddNTP**. Cada molécula se detiene en una posición distinta; al ordenar los fragmentos por tamaño, el color del último nucleótido da la secuencia.

➕ Sanger recibió por este método su **segundo Nobel de Química (1980)**.

| | **Sanger** | **NGS (segunda generación, p. ej., Illumina)** | ➕ **Lecturas largas (PacBio, Oxford Nanopore)** |
|---|---|---|---|
| Lectura | **700–1.000 pb** | 100–300 pb | Más de 10 kb |
| Fragmentos por corrida | Uno | **Millones a miles de millones** | Miles a millones |
| Uso típico | **Confirmar una variante**; un gen | Paneles, **exoma**, genoma, RNA-seq, ADN tumoral circulante | Variantes estructurales, repeticiones, ensamblaje |

➕ **Profundidad (cobertura)**: cuántas lecturas cubren cada base. Un genoma clínico suele hacerse a ~30x; los paneles oncológicos, a cientos o miles de lecturas para detectar variantes en pocas células. Ver el [capítulo 1](#18-aplicaciones-en-la-clínica-diap-4959) (exoma) y el [capítulo 6](#623-medicina-personalizada-diap-42) (NGS en oncología).

---

### 7.17 Aplicaciones clínicas, terapia génica y OGM *(Diap. 46–48)*

#### PCR y secuenciación en la clínica *(Diap. 46)*

| Aplicación | ➕ Ejemplos |
|---|---|
| **Identificación de mutaciones** (enfermedades genéticas, oncología de precisión) | *CFTR* en fibrosis quística, *EGFR* y *KRAS* en tumores, *BRCA1/2* |
| **Detección de patógenos** (epidemiología, infecciones críticas) | RT-qPCR para SARS-CoV-2; carga viral de VIH y VHC; GeneXpert para tuberculosis y resistencia a rifampicina |
| **Farmacogenética** (tratamiento según el genotipo) | *CYP2C19* y clopidogrel; **HLA-B\*57:01** y abacavir; **HLA-B\*15:02** y carbamazepina; *TPMT*/*NUDT15* y tiopurinas; *DPYD* y fluoropirimidinas |

La diapositiva resalta su **alta sensibilidad analítica**. ✅ "Especificidad clínica total" es una exageración: ninguna prueba tiene 100 % de especificidad (hay contaminación, variantes en el sitio del cebador y errores preanalíticos).

#### Terapia génica *(Diap. 47)*

| Concepto | Idea |
|---|---|
| **Base** | **Corregir** un defecto genético introduciendo material funcional en las células |
| **Vectores virales** | **Eficiencia**: virus modificados que transfieren genes con facilidad |
| **Vectores no virales** | **Seguridad**: nanopartículas lipídicas y lípidos, menos inmunogénicos y más versátiles |
| **Potencial** | Tratar la enfermedad en su **raíz genética** |

➕ Ejemplos aprobados:

| Terapia | Vector o herramienta | Enfermedad |
|---|---|---|
| Voretigén neparvovec (2017) | **AAV2** con *RPE65* | Distrofia retiniana hereditaria |
| Onasemnogén abeparvovec (2019) | **AAV9** con *SMN1* | Atrofia muscular espinal |
| Tisagenlecleucel (2017) | **Lentivirus** con un receptor quimérico (CAR) | Leucemia linfoblástica B ([capítulo 6](#623-medicina-personalizada-diap-42)) |
| Exagamglogén autotemcel (2023) | **CRISPR-Cas9** *ex vivo* | Anemia falciforme y β-talasemia |

⚠️ ➕ **Riesgos** que dieron forma a la disciplina: un vector retroviral se insertó junto al oncogén *LMO2* y causó **leucemia** en niños tratados por inmunodeficiencia ligada al X (2003): es la **activación de un oncogén por inserción viral** del [capítulo 6](#64-cómo-se-activa-un-oncogén-diap-9). Y en 1999 una **respuesta inmune masiva a un adenovirus** causó la muerte de Jesse Gelsinger.

#### Organismos genéticamente modificados *(Diap. 48)*

📌 Plantas, animales o microorganismos cuyo material genético se **alteró por ingeniería genética** para introducir "genes de interés". Sirven para estudiar la función de genes y vías biológicas.

**Propósitos**: resistencia de cultivos a plagas (➕ maíz y algodón *Bt*), mayor rendimiento agrícola, **producción de proteínas terapéuticas** (biofármacos como la insulina), **biorremediación** y nuevas estrategias de terapia génica.

➕ En investigación, los **ratones transgénicos** (ganan un gen) y ***knock-out*** (pierden uno) permiten ver qué hace un gen en un organismo completo.

---

### 7.18 Identificación humana y genética forense *(Diap. 49)*

📌 El perfil genético se basa en **STR** (*short tandem repeats*, repeticiones cortas en tándem): unidades de **2–6 pb** repetidas en tándem; el **número de repeticiones** varía mucho entre personas (**hipervariables**). Se amplifican por **PCR multiplex** con cebadores fluorescentes y se separan por electroforesis capilar.

| Concepto | Detalle |
|---|---|
| **Perfil** | Dos alelos (uno materno y otro paterno) en cada locus |
| **CODIS** | Base de datos del **FBI** (*Combined DNA Index System*). Núcleo de **13 loci** hasta 2016; **20 loci** desde el **1 de enero de 2017** |
| **Amelogenina (AMEL)** | Marcador de **sexo** que se amplifica junto con los STR (➕ X: 106 pb; Y: 112 pb en los kits clásicos) |
| ➕ **Paternidad** | En cada locus, el hijo comparte **un alelo** con cada progenitor |
| ➕ **Linajes** | **Y-STR** (línea paterna); **ADN mitocondrial** (línea materna; útil en tallos de pelo y huesos antiguos) |

✅ Precisiones:
- Las figuras pequeñas muestran los **13 loci originales**; la figura grande ya tiene los 20 actuales (incluye D1S1656, D2S441, D2S1338, D10S1248, D12S391, D19S433 y D22S1045).
- La diapositiva llama al CODIS "estándar mundial". Es el sistema de Estados Unidos, adoptado por muchos países; Europa usa el **conjunto estándar europeo (ESS)**, que comparte la mayoría de los loci.
- El perfil es "único para cada individuo" **excepto en gemelos monocigóticos**, que comparten el mismo perfil de STR.

---

### 7.19 Flujo integrado y perspectivas *(Diap. 50–51)*

#### De la muestra al diagnóstico *(Diap. 50)*

```
Muestra (sangre, saliva, tejido) → extracción y purificación del ADN → amplificación por PCR
      → secuenciación (Sanger o NGS) o electroforesis → interpretación
```

**Flujo de clonación** *(figura)*: digestión de restricción → ligadura → transformación bacteriana → inoculación de una colonia → purificación del plásmido → **secuenciación de Sanger** para confirmar el inserto.

📌 **Calidad del material**: el aislamiento es crítico para evitar la **contaminación externa**.

#### Perspectivas *(Diap. 51)*

| Eje | Contenido |
|---|---|
| **Implicaciones éticas** | Privacidad genética y equidad en el acceso a la intervención del genoma humano |
| **Progreso técnico** | Integración de datos **multiómicos** y herramientas de **edición génica** (➕ CRISPR-Cas9; Nobel de Química 2020 para Charpentier y Doudna) |
| **Síntesis** | Colaboración interdisciplinaria y reflexión bioética para que el potencial genético beneficie a la humanidad |

---

### 7.20 ➕ ¿Qué técnica uso para cada pregunta?

| Pregunta clínica o de laboratorio | Técnica |
|---|---|
| ¿Tiene una mutación puntual conocida? | PCR + Sanger; PCR-RFLP; PCR alelo-específica o qPCR |
| ¿Cuál de muchos genes tiene la variante? | **NGS** (panel, exoma o genoma) |
| ¿Tiene una trisomía? | Cariotipo; **FISH en interfase** si se necesita rápido; microarreglo |
| ¿Tiene una microdeleción (22q11.2)? | **FISH** o **microarreglo cromosómico** (el cariotipo no la ve) |
| ¿Hay una translocación *BCR-ABL1*? | Cariotipo, **FISH**, **RT-PCR**; **qPCR** para el seguimiento |
| ¿Está amplificado *HER2*? | Inmunohistoquímica y **FISH** (o ISH) |
| ¿Cuánto ARNm de un gen hay? | **RT-qPCR**; Northern; RNA-seq |
| ¿Está la proteína y de qué tamaño es? | **Western blot** |
| ¿Hay una expansión grande de CGG (X frágil)? | **Southern blot** (con PCR complementaria) |
| ¿De quién es esta muestra? ¿Es el padre? | **STR** por PCR multiplex + electroforesis capilar |
| ¿Cuánta carga viral tiene? | **RT-qPCR** |
| ¿Hay ADN tumoral en la sangre? | NGS profunda o **PCR digital** |
| ¿Dónde está este gen en el cromosoma? | **FISH en metafase** |
| ¿Qué genes cambian su expresión con un tratamiento? | Microarreglo de expresión o **RNA-seq** |

---

### ✅ Verificación de datos de la clase (capítulo 7)

| Diapositiva | Dice | Verificación |
|---|---|---|
| 2 | Tabla de contenidos con 39 temas | No coincide con la numeración del PDF (51 diapositivas); esta guía cita el PDF |
| 6 | Pureza 260/280 | Correcto; el valor esperado para ADN puro es ~1,8 |
| 7 | 6 pg por célula diploide; 3 pg por espermatozoide; 30–60 ng por µL de sangre | Correcto |
| 7 | "≈ 1 ng: PCR estándar" | Es la cantidad óptima de los kits forenses de STR; una PCR de rutina suele usar 10–100 ng |
| 10–11 | Agarosa 200–50.000 pb; PAGE ≤ 500 pb con resolución de 1 base | Correcto como rangos de trabajo |
| 12 | Coomassie: "menor sensibilidad para ácidos nucleicos" | El Coomassie tiñe proteínas; no se usa para ácidos nucleicos |
| 13–15 | EcoRI G^AATTC, HindIII A^AGCTT, HaeIII GG^CC | Correcto |
| 15 | HindIII produce "extremos asimétricos" | Sus extremos cohesivos son simétricos, igual que los de EcoRI |
| 14 | Nomenclatura y tabla de enzimas | Correcto |
| 16 | Restricción para "Southern y Northern" | Solo el Southern digiere el ADN; en el Northern el ARN no se corta |
| 17 | Secuencia con cortes marcados | Los cinco cortes marcados coinciden con los sitios reales (verificado con la secuencia completa) |
| 18 | "MstI restriction sites" en la figura | La enzima es MstII (CCTNAGG) |
| 18–23 | Hb S elimina un sitio de MstII; 1,2 frente a 1,4 kb | Correcto |
| 25 | Capacidades en "kba" | La unidad es kb |
| 26 | Plásmido < 15, λ < 20, cósmido < 50, BAC 150–300, YAC 100–2.000, MAC > 1.000 kb | Correcto como rangos típicos |
| 26 | BAC "developed Melsimon et al 1992" | Shizuya et al. 1992, laboratorio de Mel Simon |
| 31 | Transducción viral "estable" | Solo lentivirus y retrovirus se integran; adenovirus y AAV son mayormente episomales |
| 33 | "100 % sensibilidad" | No es un dato técnico |
| 37 | Northern "cuantitativo" | Semicuantitativo |
| 38 | FISH: "resolución > 5 Mb" | Esa es la resolución del cariotipo; la FISH llega a ~1–3 Mb en metafase y ~50 kb–1 Mb en interfase |
| 40 | Cy3 532 nm / Cy5 633 nm; log₂ 5,64 y −4,91 | Correcto (log₂ 50 = 5,64; log₂ 0,033 = −4,91) |
| 41–42 | 94–96 °C, 50–65 °C, 72 °C; 2ⁿ; ~30 ciclos | Correcto |
| 45 | ddNTP sin 3'-OH | Correcto |
| 46 | "Especificidad clínica total" | Exagerado: ninguna prueba es 100 % específica |
| 49 | 13 loci CODIS (figuras pequeñas); "estándar mundial"; STR "únicos para cada individuo" | Desde 2017 son 20 loci; CODIS es el sistema de EE. UU.; los gemelos monocigóticos comparten perfil |

---

### Autoevaluación (capítulo 7)

<details><summary>1. Una muestra de ADN tiene A260/A280 = 1,5. ¿Qué significa?</summary>

Contaminación con proteínas (o fenol): el ADN puro da ~1,8.
</details>

<details><summary>2. ¿Cuántos espermatozoides hay en 1 ng de ADN, y por qué?</summary>

Unos 330–350: cada espermatozoide tiene ~3 pg y 1 ng = 1.000 pg.
</details>

<details><summary>3. ¿Hacia qué electrodo migra el ADN y por qué los fragmentos pequeños llegan más lejos?</summary>

Hacia el ánodo (+), porque los fosfatos le dan carga negativa. La carga es proporcional a la longitud, así que la separación depende del tamaño: los fragmentos pequeños atraviesan con más facilidad los poros del gel.
</details>

<details><summary>4. Necesitas separar dos fragmentos de 150 y 151 pb. ¿Qué gel usas?</summary>

Poliacrilamida: resuelve diferencias de una base en fragmentos de hasta ~500 pb.
</details>

<details><summary>5. ¿Qué extremos dejan EcoRI, PstI y HaeIII?</summary>

EcoRI: cohesivos con saliente 5' (AATT). PstI: cohesivos con saliente 3' (TGCA). HaeIII: romos.
</details>

<details><summary>6. ¿Cada cuántas pares de bases se espera, en promedio, un sitio de EcoRI?</summary>

Cada 4⁶ = 4.096 pb, suponiendo bases al azar en igual proporción.
</details>

<details><summary>7. Un plásmido circular tiene tres sitios de EcoRI. ¿Cuántos fragmentos produce?</summary>

Tres. En una molécula circular, n cortes producen n fragmentos (en una lineal, n + 1).
</details>

<details><summary>8. Un Southern con MstII y sonda de β-globina muestra bandas de 1,2 y 1,4 kb. ¿Genotipo?</summary>

Portador (AS): un alelo normal (1,2 kb) y uno falciforme que perdió el sitio (1,4 kb).
</details>

<details><summary>9. Necesitas clonar un fragmento de 200 kb. ¿Qué vector eliges?</summary>

Un BAC (150–300 kb). Un YAC también lo acepta, pero los BAC son más estables.
</details>

<details><summary>10. Después de transformar y sembrar en ampicilina con X-gal, ves colonias azules y blancas. ¿Cuáles eliges y por qué?</summary>

Las blancas: el inserto interrumpió *lacZ*. Las azules tienen el plásmido (por eso crecen en ampicilina) pero sin inserto.
</details>

<details><summary>11. ¿Por qué se produce la insulina humana desde una biblioteca de ADNc y no desde el gen genómico?</summary>

Porque las bacterias no hacen *splicing*: el ADNc ya no tiene intrones.
</details>

<details><summary>12. Quieres saber si un tejido expresa el ARNm de un gen y de qué tamaño es. ¿Qué blot usas?</summary>

Northern blot (o, hoy, RT-qPCR o RNA-seq para cuantificar).
</details>

<details><summary>13. Un recién nacido tiene sospecha de deleción 22q11.2 y cariotipo normal. ¿Descarta el diagnóstico?</summary>

No. La deleción mide ~3 Mb, por debajo de la resolución del cariotipo (~5–10 Mb). Se confirma con FISH o microarreglo cromosómico.
</details>

<details><summary>14. En un microarreglo, un gen tiene Cy3 = 1.000 y Cy5 = 4.000. ¿log₂ y color?</summary>

Cy5/Cy3 = 4; log₂ 4 = +2. Rojo: el gen está 4 veces más expresado en la muestra marcada con Cy5.
</details>

<details><summary>15. ¿Cuántas copias teóricas hay tras 20 ciclos de PCR partiendo de una molécula? ¿Cuándo aparecen las primeras moléculas de doble cadena de longitud exacta?</summary>

2²⁰ ≈ 1 millón (1.048.576). Las primeras dos moléculas de doble cadena de longitud exacta aparecen en el ciclo 3.
</details>

<details><summary>16. ¿Por qué un ddNTP detiene la síntesis en el método de Sanger?</summary>

Porque le falta el grupo 3'-OH, necesario para formar el enlace fosfodiéster con el siguiente nucleótido.
</details>

<details><summary>17. Dos muestras de un crimen tienen perfiles STR idénticos en los 20 loci CODIS. ¿Son necesariamente de la misma persona?</summary>

Casi con certeza, salvo que se trate de gemelos monocigóticos, que comparten el perfil.
</details>

<details><summary>18. ¿Qué diferencia hay entre transformación, transfección y transducción?</summary>

Transformación: introducir ADN en bacterias (o levaduras). Transfección: en células eucariotas por métodos no virales. Transducción: con un virus.
</details>

---

### Glosario (capítulo 7)

| Término | Definición |
|---|---|
| **A260/A280** | Razón de absorbancias que estima la pureza del ADN (~1,8) |
| **BAC / YAC / MAC** | Cromosomas artificiales bacteriano, de levadura y de mamífero |
| **ADNc** | ADN complementario sintetizado a partir de ARNm por la transcriptasa inversa |
| **Cebador** | Oligonucleótido corto que marca el inicio de la síntesis en la PCR |
| **CODIS** | Sistema de índice combinado de ADN del FBI; 20 loci STR desde 2017 |
| **Cósmido** | Plásmido con sitios *cos* que se empaqueta en cabezas de fago λ |
| **Ct** | Ciclo umbral de la qPCR; menor cuanto más molde hay |
| **ddNTP** | Didesoxinucleótido sin 3'-OH: termina la cadena en Sanger |
| **Extremo cohesivo** | Cola de cadena sencilla que deja una enzima de restricción |
| **Extremo romo** | Corte sin colas de cadena sencilla |
| **FISH** | Hibridación *in situ* fluorescente |
| **Gen reportero** | Gen cuyo producto se mide fácilmente (LacZ, luciferasa, GFP) |
| **Hibridación** | Apareamiento de una sonda con su secuencia complementaria |
| **Palíndromo** | Secuencia que se lee igual en ambas cadenas en sentido 5'→3' |
| **PCR** | Reacción en cadena de la polimerasa |
| **RFLP** | Polimorfismo de longitud de fragmentos de restricción |
| **Sitio de clonación múltiple** | Región del vector con muchos sitios de restricción únicos |
| **Sonda** | Fragmento de ácido nucleico marcado que detecta una secuencia |
| **STR** | Repeticiones cortas en tándem, base de la identificación humana |
| **Taq polimerasa** | ADN polimerasa termoestable de *Thermus aquaticus* |
| **Transfección** | Introducción de ácidos nucleicos en células eucariotas sin virus |
| **Vector lanzadera** | Vector que se replica en dos huéspedes distintos |

---

### Referencias (capítulo 7)

De la clase:

- Rey Buitrago M. *Técnicas de biología molecular* [presentación]. Curso de genética, Facultad de Medicina, Universidad Nacional de Colombia; 2026.
- King MW. *The Medical Biochemistry Page*: RFLP de la β-globina con MstII (figura de la Diap. 22), 1996.

Usadas en la verificación y las ampliaciones:

- Alberts B, et al. *Molecular Biology of the Cell.* 7.ª ed. W.W. Norton; 2022, cap. 8.
- Strachan T, Read A. *Human Molecular Genetics.* 5.ª ed. CRC Press; 2019, caps. 6–7.
- Chang JC, Kan YW. A sensitive new prenatal test for sickle-cell anemia. *N Engl J Med.* 1982;307:30-32.
- Southern EM. Detection of specific sequences among DNA fragments separated by gel electrophoresis. *J Mol Biol.* 1975;98:503-517.
- Sanger F, Nicklen S, Coulson AR. DNA sequencing with chain-terminating inhibitors. *PNAS.* 1977;74:5463-5467.
- Saiki RK, et al. Primer-directed enzymatic amplification of DNA with a thermostable DNA polymerase. *Science.* 1988;239:487-491.
- Burke DT, Carle GF, Olson MV. *Science.* 1987;236:806-812 (YAC); Shizuya H, et al. *PNAS.* 1992;89:8794-8797 (BAC).
- Resolución de la FISH: *Studies of metaphase and interphase chromosomes using fluorescence in situ hybridization* <https://pubmed.ncbi.nlm.nih.gov/7956093/>; *Fiber FISH as a DNA mapping tool* <https://pubmed.ncbi.nlm.nih.gov/9245344/>
- Miller DT, et al. Consensus statement: chromosomal microarray is a first-tier clinical diagnostic test. *Am J Hum Genet.* 2010;86:749-764.
- Office of Justice Programs. Switching to 20 core CODIS loci (1 de enero de 2017): <https://uat.ojp.gov/library/publications/switching-20-core-codis-loci-and-impact-saki-testing>
- Hacein-Bey-Abina S, et al. LMO2-associated clonal T cell proliferation in two patients after gene therapy for SCID-X1. *Science.* 2003;302:415-419.

[↑ Volver al índice general](#índice-general)

---

## Anexo A. Conexiones entre clases

| Concepto | Dónde aparece | La conexión |
|---|---|---|
| **ATM, ATR, CHK1/2, p53, p21** | Ciclo celular (3.13); [reparación del ADN (5.2.5)](#525-la-respuesta-al-daño-del-adn-ddr-diap-7) | Son el mismo sistema: los sensores del daño del ADN son los que frenan el ciclo |
| **BRCA1/2, RAD51 y recombinación homóloga** | Ciclo celular (3.13); [reparación del ADN (5.7)](#57-roturas-de-doble-cadena-nhej-y-hr) | La recombinación homóloga solo ocurre en S y G2 porque necesita la cromátida hermana |
| **CDK7–ciclina H (CAK)** | Ciclo celular (3.8); [reparación del ADN (5.5, NER)](#55-reparación-por-escisión-de-nucleótidos-ner) | La cinasa que activa a las CDK es parte de TFIIH, el complejo que abre el ADN en la reparación por escisión de nucleótidos |
| **c-MYC** | Ciclo celular (3.11); desarrollo (2.3) | Es un mitógeno interno que acelera el ciclo y uno de los cuatro factores de Yamanaka |
| **Ciclos sin G1 ni G2** | Ciclo celular (3.2); desarrollo (2.1) | Los embriones tempranos solo replican y dividen; el control de G1 aparece después |
| **miR-302 y células madre** | Ciclo celular (3.16); desarrollo (2.3) | Silencian p21: por eso las células pluripotentes ciclan rápido |
| **Metilación del ADN** | Desarrollo (2.2); ciclo (3.17); reparación del ADN (5.3, MGMT) | La epigenética borra y reescribe marcas en el embrión; silenciar *MGMT* por metilación predice respuesta a temozolomida |
| **Apoptosis** | Desarrollo (2.3); ciclo (3.13) | Separa los dedos en el embrión y elimina células con ADN irreparable (p53 → PUMA, BAX) |
| **Malformaciones y EIM** | Desarrollo (2.9); EIM (4.6, 4.9, 4.11) | Los EIM tipo intoxicación **no** causan malformaciones (la placenta elimina el tóxico); algunos energéticos y de moléculas complejas (colesterol) **sí** |
| **Fenotipo dismórfico** | Desarrollo (2.9); EIM (4.12) | Las MPS producen rasgos "toscos", pero un fenotipo normal no las descarta |
| **Hidrops fetal no inmune** | EIM (4.12) | Hallazgo prenatal que obliga a pensar en enfermedades lisosomales (MPS VII) |
| **Exoma y bases de datos** | Bioinformática (1.7–1.8); desarrollo; EIM | El exoma confirma síndromes y EIM; OMIM, dbSNP y Ensembl permiten interpretar las variantes |
| **Herencia autosómica recesiva y consanguinidad** | Bioinformática (*HERC1*); EIM (PKU, MPS, acidemia propiónica) | Padres portadores sanos: los casos parecen esporádicos |
| **Tamizaje neonatal** | Bioinformática (medicina genómica); EIM (4.3) | Ejemplo de medicina genómica en salud pública: Ley 1980 de 2019 y Resolución 117 de 2026 en Colombia |
| **Rb, E2F y CDK4/6** | Ciclo celular (3.11); [cáncer (6.6, 6.11)](#611-evasión-de-los-supresores-de-crecimiento-diap-20) | El freno del punto R es el hallmark "evasión de supresores"; los inhibidores de CDK4/6 solo funcionan si el tumor conserva Rb |
| **p53, p21 y los dos golpes** | Ciclo celular (3.13); reparación (5.1.5); [cáncer (6.5, 6.11)](#65-genes-supresores-y-la-hipótesis-de-los-dos-golpes-diap-10) | El guardián del genoma es el gen más mutado en cáncer; Li-Fraumeni es su forma germinal |
| **MMR, MSI y síndrome de Lynch** | Reparación (5.6); [cáncer (6.8, 6.25)](#68-evolución-clonal-e-inestabilidad-genómica-diap-1516-26) | La falla del MMR genera inestabilidad de microsatélites, alta carga mutacional y respuesta a pembrolizumab |
| **BRCA1/2 y PARP** | Reparación (5.7.7, 5.10.1); [cáncer (6.22, 6.23)](#623-medicina-personalizada-diap-42) | La letalidad sintética convierte un defecto de reparación en diana terapéutica |
| **Senescencia y telómeros** | Ciclo celular (3.17); [cáncer (6.13, 6.19)](#613-inmortalidad-replicativa-diap-22) | La senescencia frena al tumor, pero su SASP lo ayuda; el tumor escapa reactivando la telomerasa |
| **miARN** | Ciclo celular (3.16); cáncer (6.3) | miR-17-92 y miR-21 aceleran (oncomiR); let-7, miR-34 y miR-200 frenan |
| **FISH, PCR y NGS** | [Técnicas (7.13, 7.15, 7.16)](#713-fish-diap-38); cáncer (6.4, 6.23); bioinformática (1.8) | HER2 y BCR-ABL se detectan por FISH; las mutaciones driver, por PCR o NGS; el exoma es NGS |
| **Inserción viral** | Cáncer (6.4); [técnicas (7.17)](#717-aplicaciones-clínicas-terapia-génica-y-ogm-diap-4648) | El mismo mecanismo que activa oncogenes causó leucemia en un ensayo de terapia génica (2003) |
| **Hemoglobina S** | Técnicas (7.7) | Ejemplo clásico de RFLP (MstII) y hoy de terapia génica con CRISPR |

---

## Anexo B. Tabla transversal de enfermedades

| Enfermedad | Gen o alteración | Herencia | Mecanismo | Capítulo |
|---|---|---|---|---|
| Acondroplasia | *FGFR3* | AD | Receptor de FGF (ganancia de función) | 1, 2 |
| Fibrosis quística | *CFTR* (F508del = rs113993960) | AR | Canal de cloro | 1, 4 |
| Sobrecrecimiento con discapacidad intelectual | *HERC1* | AR (heterocigosis compuesta) | Ubiquitina-ligasa | 1 |
| COVID-19 grave (factor de riesgo) | *LZTFL1* rs11385942 (3p21.31) | Riesgo poligénico, no mendeliano | — | 1 |
| Malformación mano-pie hendida 1 | *DLX5/DLX6* (7q21.3) | AD | Factor de transcripción homeobox | 2 |
| Síndrome EEC | *TP63* | AD | Factor de transcripción | 2 |
| Osteogénesis imperfecta XIII | *BMP1* | AR | Proteinasa C del procolágeno | 2 |
| Síndrome mano-pie-genital | *HOXA13* | AD | HOX | 2 |
| Aniridia | *PAX6* | AD (haploinsuficiencia) | PAX | 2 |
| Waardenburg tipos 1 y 3 | *PAX3* | AD | PAX | 2 |
| Holt-Oram | *TBX5* | AD | T-box | 2 |
| Síndrome de Down | Trisomía 21 | Cromosómica (casi siempre esporádica) | — | 2 |
| Síndrome de Marfan | *FBN1* | AD | Fibrilina | 2 |
| Retinoblastoma | *RB1* | AD (predisposición; dos golpes) | Freno del punto R | 3, 6 |
| Li-Fraumeni | *TP53* | AD (predisposición) | Guardián del genoma | 3, 6 |
| Ataxia-telangiectasia | *ATM* | AR | Señal de daño del ADN | 3, 5, 6 |
| Cáncer de mama y ovario hereditario | *BRCA1*, *BRCA2* | AD (predisposición) | Recombinación homóloga | 3, 5, 6 |
| Aneuploidía en mosaico variegado | *BUB1B* | AR | Punto de control del huso | 3 |
| Alcaptonuria | *HGD* | AR | Degradación de tirosina | 4 |
| Fenilcetonuria | *PAH* | AR | Fenilalanina hidroxilasa | 4 |
| Deficiencia de BH4 (p. ej., DHPR) | *QDPR* y otros | AR | Cofactor de PAH | 4 |
| Acidemia propiónica | *PCCA*, *PCCB* | AR | Propionil-CoA carboxilasa | 4 |
| Glucogenosis VI (Hers) | *PYGL* | AR | Glucógeno fosforilasa hepática | 4 |
| Déficit de G6PD | *G6PD* | Ligada al X | Vía de las pentosas | 4 |
| MPS I (Hurler, Scheie) | *IDUA* | AR | Alfa-L-iduronidasa | 4 |
| MPS II (Hunter) | *IDS* | Ligada al X | Iduronato-2-sulfatasa | 4 |
| MPS IVA (Morquio A) | *GALNS* | AR | N-acetilgalactosamina-6-sulfatasa | 4 |
| MPS VII (Sly) | *GUSB* | AR | Beta-glucuronidasa | 4 |
| Síndrome de Lynch | *MLH1*, *MSH2*, *MSH6*, *PMS2* | AD (predisposición) | Reparación de apareamientos erróneos (MSI) | 5, 6 |
| Poliposis adenomatosa familiar | *APC* | AD | Supresor gatekeeper (vía Wnt) | 6 |
| Von Hippel-Lindau | *VHL* | AD | Degradación de HIF | 6 |
| Neurofibromatosis 1 y 2 | *NF1*, *NF2* | AD | RAS-GAP (NF1); merlina (NF2) | 6 |
| Síndrome de Gorlin | *PTCH1* | AD | Vía Hedgehog | 6 |
| Melanoma familiar | *CDKN2A* | AD | p16 (inhibidor de CDK4/6) | 6 |
| Cáncer gástrico difuso hereditario | *CDH1* | AD | E-cadherina | 6 |
| Neoplasia endocrina múltiple 2 | *RET* | AD | Oncogén germinal (ganancia de función) | 6 |
| Leucemia mieloide crónica | *BCR-ABL1*, t(9;22) | Somática | Tirosina cinasa de fusión | 6, 7 |
| Linfoma de Burkitt | *IGH*-*MYC*, t(8;14) | Somática | Captura de *enhancer* | 6 |
| Leucemia promielocítica aguda | *PML-RARA*, t(15;17) | Somática | Diferenciación bloqueada | 6 |
| Anemia falciforme | *HBB* (Glu6Val) | AR | Polimerización de la HbS | 7 |

El capítulo 5 tiene además su propia [tabla rápida de enfermedades de la reparación del ADN](#5105--tabla-rápida-de-enfermedades-para-diagnóstico-diferencial) (xeroderma pigmentoso, Cockayne, Fanconi, SCID por Artemis y otras).

---

## Anexo C. Fe de erratas consolidada

Errores o datos desactualizados de las diapositivas. El detalle y las fuentes están en la sección "✅ Verificación" de cada capítulo.

**Bioinformática** ([detalle](#-verificación-de-datos-de-la-clase-capítulo-1))
- 20.000–25.000 genes → hoy ~19.000–20.000 codificantes.
- Code School ya no existe; un enlace de recursos está caído.
- El PDB suele clasificarse como base primaria, no secundaria.
- Frontier ya no es el n.º 1 del TOP500 (es el n.º 3 en noviembre de 2026).

**Genética del desarrollo** ([detalle](#-verificación-de-datos-de-la-clase-capítulo-2))
- Cita de Darwin: 1859, no 1942.
- Células del adulto: ~3,7 × 10¹³, no 10.000 billones.
- La tríada ectrodactilia + displasia ectodérmica + fisura es el síndrome EEC (*TP63*), no SHFM1 aislada.
- *BMP1* no pertenece a la superfamilia TGF-β (es una metaloproteasa).
- Dominio *paired*: 128 aa; artrogriposis y glosoptosis estaban mal escritas.

**Ciclo celular** ([detalle](#-verificación-de-datos-de-la-clase-capítulo-3))
- p16 = INK4a y p15 = INK4b (la diapositiva los invierte).
- Las imágenes de las diapositivas 12, 19 y 36 tienen texto ilegible o el punto de control del huso en G2; el SAC actúa en M y el punto R al final de G1.
- Límite de Hayflick: ~40–60 duplicaciones.

**Errores innatos del metabolismo** ([detalle](#-verificación-de-datos-de-la-clase-capítulo-4))
- La PKU se describió en 1934 (Følling).
- La ICIMD (2021) lista 1.450 EIM.
- Colombia: la Resolución 117 de 2026 hizo obligatorias las 7 pruebas del tamizaje básico.
- *PAH*: más de 950 variantes (más de 3.000 en PAHvdb), no 600.
- El tratamiento de la PKU empieza desde 6 mg/dL (360 µmol/L); 20 mg/dL define la forma clásica.
- Nuevas terapias: sepiapterina (2025).
- En los casos clínicos: VCM y HCM invertidos; referencia de insulina errada; la CK alta en la glucogenosis VI sugiere compromiso muscular.

**Genética del cáncer** ([detalle](#-verificación-de-datos-de-la-clase-capítulo-6))
- Los oncomiR silencian supresores (la diapositiva lo invierte en una frase).
- En neuroblastoma se amplifica *MYCN*, no *MYC*.
- El retinoblastoma esporádico también es de la infancia, no de adultos.
- Sin Rb, CDK4/6 deja de importar: los inhibidores de CDK4/6 no sirven en tumores sin Rb.
- La cromoplexia no es lo mismo que los ciclos de ruptura-fusión-puente.
- La figura de hallmarks de 2022 tiene 14 elementos; inflamación e inestabilidad genómica son características habilitantes, no hallmarks.
- RAS mutado: ~19 % de los pacientes (Prior 2020), no 30 %.
- Los tumores avasculares miden hasta ~1–2 mm (la diapositiva lo invierte).
- Venetoclax no está aprobado en linfoma folicular; navitoclax y los senolíticos no están aprobados.
- Con 80x no se detectan clones del 1 %.
- PARP corresponde a inestabilidad genómica; el inhibidor de telomerasa aprobado es imetelstat (2024).
- GLOBOCAN 2024 (julio de 2026) actualiza las cifras: 20,6 millones de casos y 9,8 millones de muertes; Colombia, 123.053 casos y 55.981 muertes. Las 40.333 muertes de la diapositiva no son verificables.
- El Plan de Choque se formalizó con la Circular 010 de 2024 (Minsalud, INC, Supersalud); desde julio de 2026 rige el Plan Decenal 2026–2035.
- mRNA-4157: la fase III (INTerpath-001) fue positiva en 2026.

**Técnicas de biología molecular** ([detalle](#-verificación-de-datos-de-la-clase-capítulo-7))
- El Coomassie tiñe proteínas, no ácidos nucleicos.
- Los extremos de HindIII no son "asimétricos".
- En el Northern blot el ARN no se digiere con enzimas de restricción; además es semicuantitativo.
- La FISH tiene resolución de ~50 kb a 3 Mb; ">5 Mb" es la del cariotipo.
- Solo lentivirus y retrovirus dan expresión estable; adenovirus y AAV son mayormente episomales.
- El BAC lo desarrollaron Shizuya et al. (1992), no "Melsimon".
- El núcleo CODIS tiene 20 loci desde 2017; los gemelos monocigóticos comparten perfil.

---

## Anexo D. Cómo estudiar con el mazo de Anki

- **Un solo archivo**: [`Genetica_Biologia_Molecular.apkg`](Genetica_Biologia_Molecular.apkg). Crea el mazo *Genética y Biología Molecular (UNAL 2026)* con un submazo por capítulo (01 a 07). Instrucciones de importación en el [README](README.md).
- **Tipos de tarjeta**:
  - Capítulos 1–4, 6 y 7: **Basic**. Pregunta en el anverso; respuesta corta en negrita y, debajo, una línea gris con la explicación y la diapositiva.
  - Capítulo 5 (reparación del ADN): conserva sus tres tipos propios, **cloze**, **pregunta-respuesta** y **caso clínico**, repartidos en 11 subdecks. Detalle en la [sección 5.16](#516-plan-de-estudio-y-cómo-usar-el-mazo-de-anki).
- **Etiquetas útiles** para filtrar (Explorar → buscar `tag:nombre`):
  - `verificado`: tarjetas que corrigen o actualizan la diapositiva (repásalas antes del examen).
  - `ampliacion`: contenido que no está en las diapositivas. Si solo quieres lo de la clase, suspéndelas con `tag:ampliacion` (en el capítulo 5, `tag:ReparacionADN::fuente::ampliacion`).
  - `caso`, `clinica`, `numeros`, `lista`, `trampa`, `historia`.
  - Por capítulo: `bioinformatica`, `desarrollo`, `ciclo_celular`, `eim`, `reparacion`, `cancer`, `tecnicas`; subtemas como `pku`, `mps`, `p53`, `sac`, `hallmarks`, `colombia`, `pcr`, `fish`, `hbs`; y las etiquetas jerárquicas `ReparacionADN::…` del capítulo 5.
- **Ajustes recomendados** (*Opciones del mazo*): FSRS con retención deseada de 0,90; **20–30 tarjetas nuevas al día** (con 1.047 tarjetas, el mazo completo entra en unas 6 semanas); orden de nuevas por **mazo**, para respetar el orden de la guía; **enterrar tarjetas hermanas**, para no ver juntos los huecos de un mismo cloze. Si tienes examen pronto, empieza por el submazo de la clase que viene.
- Lee primero el capítulo y después haz sus tarjetas: el orden de las tarjetas sigue el de la guía.

---

## Anexo E. Cómo crecerá esta guía

Cuando lleguen nuevas diapositivas:

1. Se verifica el contenido y se agrega un capítulo nuevo a esta guía, antes de los anexos, con la misma estructura.
2. Se crea `anki/cards_NN_tema.txt` y se añade su submazo en `anki/build_deck.py`.
3. Se actualizan el índice general, los anexos y el README.
4. Las tarjetas existentes conservan su id: al reimportar el `.apkg`, Anki agrega las nuevas y actualiza las editadas **sin perder tu progreso**.
