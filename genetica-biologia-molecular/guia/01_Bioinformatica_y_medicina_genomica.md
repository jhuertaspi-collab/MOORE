# 1. Introducción a la bioinformática y medicina genómica

> Clase del Prof. **Oscar Ortega-Recalde** (MD, MSc, PhD), Universidad Nacional de Colombia, 2026.
> Las citas *(Diap. N)* siguen la numeración de las diapositivas de la clase. Los símbolos 📌 ➕ ⚠️ ✅ 🩺 🧠 se explican en la [guía principal](../Guia_de_estudio.md#cómo-usar-esta-guía).

---

## Índice

- [Lo esencial en un minuto](#lo-esencial-en-un-minuto)
- [1.1 Definiciones](#11-definiciones-diap-36)
- [1.2 ¿Por qué importan la bioinformática y la medicina genómica?](#12-por-qué-importan-la-bioinformática-y-la-medicina-genómica-diap-710)
- [1.3 Alfabetización en programación](#13-alfabetización-en-programación-diap-11)
- [1.4 Lenguajes de programación y algoritmos](#14-lenguajes-de-programación-y-algoritmos-diap-1317)
- [1.5 Recursos para aprender](#15-recursos-para-aprender-diap-1819)
- [1.6 Definiciones comunes en bioinformática](#16-definiciones-comunes-en-bioinformática-diap-2128)
- [1.7 Bases de datos en ciencias biomédicas](#17-bases-de-datos-en-ciencias-biomédicas-diap-3148)
- [1.8 Aplicaciones en la clínica](#18-aplicaciones-en-la-clínica-diap-4959)
- [✅ Verificación de datos de la clase](#-verificación-de-datos-de-la-clase)
- [Autoevaluación](#autoevaluación)
- [Glosario](#glosario)
- [Referencias](#referencias)

---

## Lo esencial en un minuto

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

## 1.1 Definiciones *(Diap. 3–6)*

### Contenido de la clase *(Diap. 3)*

1. Definición y utilidad en ciencias biomédicas.
2. Lenguajes de programación y algoritmos.
3. Definiciones comunes en bioinformática.
4. Bases de datos en ciencias biomédicas.
5. Aplicaciones en la clínica.

La frase de apertura *(Diap. 2)*, de C. William Pollard, resume la idea de la clase: la información solo es útil si está **organizada, procesada y disponible** para quien debe tomar decisiones; si no, es una carga.

### ¿Qué es la bioinformática? *(Diap. 5)*

📌 **Ciencia interdisciplinaria encargada de la investigación, desarrollo y aplicación de métodos computacionales en ciencias biológicas.**

```
   Ingenierías                                     Medicina
   Matemáticas    ( Ciencias de la  ∩  Biología )   Genética
   Estadística    (  computación    BIOINFORMÁTICA)  Microbiología
```

- Del lado computacional aportan: **ingenierías, matemáticas y estadística**.
- Del lado biológico aportan: **medicina, genética y microbiología**.

### ¿Qué es la medicina genómica? *(Diap. 6)*

📌 Disciplina que utiliza **información genética a gran escala** para mejorar el cuidado de la salud y la atención clínica de **pacientes y grupos poblacionales**.

➕ **Genética frente a genómica**

| | Genética | Genómica |
|---|---|---|
| Objeto | Genes individuales y su herencia | El genoma completo y la interacción entre genes y con el ambiente |
| Escala | Uno o pocos genes | Miles de genes a la vez (datos a gran escala) |
| Ejemplo | Estudiar *CFTR* en un paciente con sospecha de fibrosis quística | Secuenciar el exoma o el genoma de un niño sin diagnóstico |

---

## 1.2 ¿Por qué importan la bioinformática y la medicina genómica? *(Diap. 7–10)*

### La cadena del dato *(Diap. 7)*

```
Tecnologías high-throughput → Gran cantidad de datos → Análisis de datos biológicos complejos → Nuevas hipótesis biomédicas
```

*High-throughput* (alto rendimiento) se refiere a técnicas que procesan miles o millones de muestras o moléculas a la vez: secuenciadores de nueva generación, microarreglos, espectrometría de masas.

### El flujo de información genética y las ómicas *(Diap. 8)*

```
ADN  →  ARN  →  Proteína  →  Metabolitos
Genómica  Transcriptómica  Proteómica  Metabolómica
```

- La diapositiva atribuye al genoma humano **20.000–25.000 genes**. ✅ Esa es la estimación de 2004; las anotaciones actuales (GENCODE, Ensembl) cuentan **~19.000–20.000 genes codificantes de proteínas**. Cada nivel "aguas abajo" es más numeroso: hay muchos más transcritos (empalme alternativo) y proteínas (modificaciones postraduccionales) que genes.
- **Genotipo → fenotipo**: el fenotipo resulta de la integración de las capas moleculares (genoma, epigenoma, transcriptoma, proteoma, metaboloma) **y de la exposición ambiental**. Por eso un mismo genotipo puede dar fenotipos distintos (salud o enfermedad).

### Margaret Oakley Dayhoff y el crecimiento de GenBank *(Diap. 9)*

- **Margaret Oakley Dayhoff (1925–1983)** publicó en **1965** el ***Atlas of Protein Sequence and Structure***, la primera recopilación sistemática de secuencias de proteínas: en la práctica, la primera base de datos biológica. Se la considera pionera de la bioinformática.
  - ➕ También creó el **código de una letra** de los aminoácidos y las **matrices PAM** de sustitución de aminoácidos, que todavía se usan para alinear secuencias.
- La gráfica muestra el **número de secuencias reportadas en GenBank**, que crece de forma exponencial: el cuello de botella dejó de ser producir datos y pasó a ser analizarlos.

### ¿Por qué importa la medicina genómica? *(Diap. 10)*

La clase parte de la **enfermedad mendeliana** (una variante en un gen, en una persona entre muchas) y la ubica en un ciclo de aplicaciones de la genómica a lo largo de la vida, tanto en la línea germinal como en tejidos somáticos:

- Diagnóstico de **enfermedades mendelianas**.
- Diagnóstico rápido en la **UCI neonatal**.
- **Tamizaje prenatal no invasivo** (ADN fetal libre en sangre materna).
- **Farmacogenómica** (elegir fármaco y dosis según el genotipo).
- **Cáncer** (variantes somáticas del tumor y predisposición germinal).
- **Puntajes de riesgo poligénico** (enfermedades comunes).

---

## 1.3 Alfabetización en programación *(Diap. 11)*

Aprender a programar es:

- Una **habilidad útil en múltiples escenarios**.
- De **curva de aprendizaje gradual**: no se requiere ser experto.
- Una fuente de **nuevas perspectivas para resolver problemas**.

---

## 1.4 Lenguajes de programación y algoritmos *(Diap. 13–17)*

### ¿Qué es un lenguaje de programación? *(Diap. 13–14)*

📌 Dos definiciones de la clase, complementarias:

- **Conjunto de reglas que permiten a un computador comunicar qué operaciones realizar** *(Diap. 13)*. Notas manuscritas de la clase: es la *forma de dar instrucciones a un equipo* (una lavadora o un horno microondas también reciben instrucciones); *para una tarea más compleja se requieren instrucciones más específicas*.
- **Conjunto de reglas para comunicar un algoritmo a una máquina** *(Diap. 14)*.

### ¿Qué es un algoritmo? *(Diap. 14)*

📌 **Serie de pasos específicos y precisos para resolver un problema de interés.**

Ejemplo de la clase, "preparar huevos revueltos":

1. Revolver los huevos.
2. Calentar una sartén.
3. Agregar aceite.
4. Agregar los huevos y revolver.
5. Servir los huevos revueltos.

El "algoritmo del éxito" de la diapositiva lo traduce a código: `while (noSuccess) { tryAgain(); if (Dead) break; }`. Muestra tres ideas básicas de programación: un **ciclo** (`while`), una **acción** que se repite y una **condición** (`if`) que detiene el ciclo.

### Lenguaje natural frente a lenguaje de programación *(Diap. 15)*

| Elemento | Lenguaje natural (humano) | Lenguaje de programación |
|---|---|---|
| Palabras | "Casa", "Oso", "Jugar" | `X`, `Y`, `Z` (variables, funciones) |
| Símbolos | `,` | `>=` |
| Reglas gramaticales | Sujeto + verbo | `.` `()` `:` (sintaxis) |

Ambos tienen vocabulario, símbolos y gramática. La diferencia es que la máquina no tolera ambigüedad: una coma fuera de lugar detiene el programa.

### ¿Qué lenguaje aprender? *(Diap. 16–17)*

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

## 1.5 Recursos para aprender *(Diap. 18–19)*

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

## 1.6 Definiciones comunes en bioinformática *(Diap. 21–28)*

### Texto plano frente a texto enriquecido *(Diap. 21)*

| | Texto plano | Texto enriquecido (con formato) |
|---|---|---|
| Qué contiene | Solo caracteres. Nota de la clase: *"no hay datos adicionales al texto"* (sin colores, imágenes ni formato) | Texto más información de formato (fuentes, colores, imágenes, tablas) |
| Ejemplos | `.txt`, `.csv`, `.tsv`, archivos FASTA | `.docx`, `.pdf`, un afiche |
| Uso en bioinformática | Es el formato que leen los programas | Útil para humanos, difícil de procesar por máquinas |

### Matriz de datos frente a hoja de cálculo *(Diap. 22)*

- **Matriz de datos**: tabla en **formato de texto plano** (nota manuscrita de la clase), con filas y columnas separadas por un delimitador (coma, tabulación).
- **Hoja de cálculo** (Excel, por ejemplo): tabla con formato, colores, fórmulas y celdas combinadas. Cómoda para ver, pero se presta a errores al analizar.
- ➕ Error clásico: Excel convierte nombres de genes en fechas (*SEPT2* → "2-sep", *MARCH1* → "1-mar"). Fue tan frecuente que en 2020 el comité de nomenclatura renombró esos genes (*SEPTIN2*, *MARCHF1*).

### Higiene de datos *(Diap. 23)*

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

### Sistema operativo y línea de comandos *(Diap. 24)*

- **Sistema operativo**: programa base que administra el computador. En bioinformática predominan los de la familia **UNIX**: **Linux** y **macOS**.
- **Línea de comandos** (terminal, *shell*, Bash): interfaz de texto para dar órdenes al sistema operativo. Casi todas las herramientas bioinformáticas se ejecutan así.

### Supercomputador, clúster y nube *(Diap. 25–26)*

| Concepto | Qué es | Ejemplo de la clase |
|---|---|---|
| **Supercomputador** | Máquina con capacidad de cálculo enorme | **Frontier** (Oak Ridge National Laboratory, Departamento de Energía de EE. UU.) |
| **Clúster de computadores** | Varios computadores conectados por una red (Ethernet) que trabajan como uno solo: un **nodo maestro** reparte el trabajo entre **nodos esclavos** (trabajadores) | Clúster universitario |
| **Computación en la nube** | Uso de servidores remotos por internet, pagando por uso | Amazon Web Services, Google Cloud, Microsoft Azure |

✅ Frontier fue el **primer supercomputador exaescala** (2022) y lideró el TOP500 hasta noviembre de 2024. En la lista de noviembre de 2026 ocupa el **3.er lugar**, detrás de LineShine (China) y El Capitan (EE. UU.).

### Pseudocódigo, script y *pipeline* *(Diap. 27–28)*

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

## 1.7 Bases de datos en ciencias biomédicas *(Diap. 31–48)*

### Definición *(Diap. 31)*

📌 **Base de datos biomédica**: colección **organizada (estructurada)** de información relacionada con las ciencias biomédicas.

- Datos pertenecientes a un **mismo contexto**.
- **Almacenamiento sistemático** para su posterior uso.
- Pueden ser **físicas** (una biblioteca, un archivo de historias clínicas) o **electrónicas**.

### Características de una base de datos *(Diap. 32)*

📌 **Estructurada · Indexable · Actualizada periódicamente · Con referencias cruzadas.**

🧠 *"E-I-A-R"*: **E**structurada, **I**ndexable, **A**ctualizada, **R**eferencias cruzadas.

### Bases de datos relacionales *(Diap. 33)*

- Organizan la información en **tablas relacionadas** entre sí (modelo relacional). Ejemplo de la clase: una tabla de usuarios (`id`, `username`…), una de publicaciones (`tweets`) y una de seguidores (`following`) que conecta usuarios entre sí.
- ➕ Cada tabla tiene una **clave primaria** (identificador único de cada fila) y las tablas se enlazan mediante **claves foráneas** (la columna `from_user` apunta al `id` de la tabla de usuarios). Por eso la higiene de datos exige identificadores únicos.
- El **NCBI** funciona con este modelo: PubMed, revistas de texto completo, secuencias de nucleótidos, estructuras 3D, taxonomía, mapas y genomas, secuencias de proteínas y OMIM están enlazados entre sí.

### Primarias frente a secundarias *(Diap. 34–35)*

| | Bases de datos **primarias** | Bases de datos **secundarias** |
|---|---|---|
| Qué son | Repositorios primarios de información | Repositorios **curados** |
| Redundancia | **Redundantes** (la misma secuencia puede estar muchas veces) | **No redundantes** |
| Control editorial | Lo tiene **quien somete** los archivos | Información complementaria **validada por un experto o comité** |
| Vocabulario | **No** controlado; anotación variable de los hallazgos | **Controlado** |
| Acceso | — | Generalmente de dominio público |
| Ejemplos | GenBank, ENA, DDBJ (secuencias de nucleótidos) | UniProtKB/Swiss-Prot, RefSeq, OMIM |

⚠️✅ La diapositiva 35 muestra el **PDB** como ejemplo de base secundaria. Muchas fuentes lo clasifican como **primaria**, porque archiva las estructuras tal como las depositan los investigadores (aunque el wwPDB las valida). Para el examen usa la clasificación de la clase, pero conoce el matiz.

### Bases de datos de referencia *(Diap. 36)*

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

### NCBI *(Diap. 37–41)*

- **NCBI** (*National Center for Biotechnology Information*): recurso **administrado por el gobierno de EE. UU.** enfocado en información biotecnológica. ➕ Fundado en 1988, forma parte de la Biblioteca Nacional de Medicina (NLM) de los NIH.
- Recursos que muestra la clase:
  - **PubMed** *(Diap. 38)*: buscador de literatura biomédica.
  - **MeSH** (*Medical Subject Headings*) *(Diap. 39)*: **vocabulario controlado** de la NLM con el que se indexan los artículos de PubMed. Buscar con términos MeSH recupera artículos aunque usen sinónimos.
  - **Nucleotide** y **Protein** *(Diap. 40)*: secuencias de ácidos nucleicos y de proteínas.
  - **dbSNP** *(Diap. 41)*: variantes cortas (SNV, pequeñas inserciones y deleciones), cada una con un identificador **rs**. El ejemplo de la clase, **rs113993960**, es la deleción de 3 nt (delCTT) en *CFTR* (cromosoma 7) conocida como **F508del**, la variante más frecuente en fibrosis quística.

### Ensembl *(Diap. 42–45)*

- Proyecto científico del **EBI** (*European Bioinformatics Institute*, parte de EMBL) que provee un **recurso centralizado** para genetistas, biólogos moleculares y otros investigadores que estudian el **genoma de vertebrados y otros organismos modelo**. ➕ Se lanzó en 1999 como proyecto conjunto del EBI y el Wellcome Sanger Institute.
- La clase muestra la página del gen ***BRCA2***: ubicación, **transcritos** alternativos (codificantes y no codificantes), estructura de exones e intrones y la **secuencia** del gen.

### OMIM *(Diap. 46–48)*

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

## 1.8 Aplicaciones en la clínica *(Diap. 49–59)*

### Análisis de exoma *(Diap. 50–52)*

- 📌 Nota de la clase: en el **análisis de exoma solo se secuencia el exoma**, que es **~1 % (1–2 %) del genoma humano**.
- El **exoma** es el conjunto de **exones** (las partes de los genes que quedan en el ARNm maduro). La diapositiva usa la analogía de una manzana: el exoma es apenas una tajada (~1 %) del total, pero concentra gran parte de las variantes patogénicas conocidas de las enfermedades mendelianas.
- La imagen de la derecha *(Diap. 52)* es un visor de lecturas alineadas (tipo IGV): cada barra gris es una lectura del secuenciador; una variante aparece como un cambio de color en la misma posición en muchas lecturas.

### Caso de investigación: *HERC1* *(Diap. 51, 53–55)*

- **Ortega-Recalde et al., 2015** (*Clinical Genetics*): **mutaciones bialélicas en *HERC1*** en una **forma sindrómica de sobrecrecimiento y discapacidad intelectual**.
- Encontrar la variante causal es **buscar una aguja en un pajar** *(Diap. 53)*: el exoma de una persona tiene decenas de miles de variantes, y se filtran paso a paso hasta quedar unas pocas candidatas.
  - ➕ Filtros típicos: calidad de la lectura → frecuencia en población (descartar las comunes) → efecto en la proteína (cambio de aminoácido, codón de parada, empalme) → predicción de patogenicidad → modelo de herencia → segregación en la familia → plausibilidad del gen.
- Árbol genealógico *(Diap. 54)*: los padres son portadores sanos, cada uno de una variante distinta; los **dos hijos afectados heredaron ambas** y el hermano sano solo una:
  - *HERC1* c.13559G>A (p.Gly4520Glu): cambio de aminoácido (*missense*).
  - *HERC1* c.2625G>A (p.Trp875Ter): codón de parada prematuro (*nonsense*).
  - 📌 Esto es **heterocigosis compuesta**: dos alelos mutados **distintos** del mismo gen (herencia autosómica recesiva). Se confirmó con secuenciación de Sanger (los electroferogramas muestran los dos picos superpuestos en cada posición).
- *(Diap. 55)* Trabajos posteriores: una variante de sitio de empalme en ***HERC2*** asociada a discapacidad intelectual sindrómica con macrocefalia y dismorfismo facial, y una revisión sobre cómo las ubiquitina-ligasas HERC grandes regulan la vía de las MAPK.

### Inteligencia artificial y *big data* *(Diap. 56)*

- La implementación de **herramientas de inteligencia artificial** en el análisis de información médica es **cada vez mayor** (Zhavoronkov et al., *Nature Aging*, 2021).
- Fuentes de *big data* en salud: genoma, transcriptoma, proteoma, metaboloma, imágenes, fotos y videos, actividad física, exámenes de sangre y comportamiento. Redes neuronales profundas integran estos datos en el tiempo para estimar el estado de salud o enfermedad.

### Predictor de severidad de COVID-19 en Colombia *(Diap. 57–59)*

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

## ✅ Verificación de datos de la clase

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

## Autoevaluación

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

## Glosario

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

## Referencias

De la clase:

- Ortega-Recalde O, et al. Biallelic HERC1 mutations in a syndromic form of overgrowth and intellectual disability. *Clin Genet.* 2015;88(4):e1-3.
- Zhavoronkov A, et al. *Nature Aging.* 2021.
- Angulo-Aguado M, et al. Association between the LZTFL1 rs11385942 polymorphism and COVID-19 severity in Colombian population. *Front Med.* 2022.
- Dayhoff MO. *Atlas of Protein Sequence and Structure.* 1965.

Usadas en la verificación:

- TOP500, lista de noviembre de 2026: <https://top500.org/news/top500-leadership-holds-steady-new-system-turnover-falls-historic-low/>
- OMIM, guía de símbolos y estadísticas: <https://www.omim.org>
- Wickham H. Tidy data. *J Stat Softw.* 2014;59(10).
