# Guía de estudio: Genética y Biología Molecular

> Medicina, Universidad Nacional de Colombia, 2026. Basada en las diapositivas de clase de los profesores **Oscar Ortega-Recalde**, **Sandra Yaneth Ospina Lagos** y **Mauricio Rey Buitrago**, verificada contra fuentes primarias y ampliada con lo necesario para entender cada tema.
> Última actualización: 22 de noviembre de 2026. La guía crece a medida que llegan nuevas clases.

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

Cada capítulo tiene la misma estructura: **lo esencial en un minuto** → desarrollo por diapositivas → **verificación de datos** → **autoevaluación** con respuestas desplegables → glosario → referencias.

---

## Capítulos

| # | Clase | Docente | Guía | Submazo Anki (Basic) |
|---|---|---|---|---|
| 1 | Introducción a la bioinformática y medicina genómica | O. Ortega-Recalde | [01_Bioinformatica_y_medicina_genomica.md](guia/01_Bioinformatica_y_medicina_genomica.md) | 66 tarjetas |
| 2 | Genética del desarrollo | O. Ortega-Recalde | [02_Genetica_del_desarrollo.md](guia/02_Genetica_del_desarrollo.md) | 84 tarjetas |
| 3 | Ciclo celular: fases, motor molecular y puntos de control | S. Y. Ospina Lagos | [03_Ciclo_celular.md](guia/03_Ciclo_celular.md) | 125 tarjetas |
| 4 | Errores innatos del metabolismo | S. Y. Ospina Lagos | [04_Errores_innatos_del_metabolismo.md](guia/04_Errores_innatos_del_metabolismo.md) | 108 tarjetas |
| 5 | Mecanismos de reparación del ADN | S. Ospina Lagos | [05_Reparacion_del_ADN.md](guia/05_Reparacion_del_ADN.md) | Mazo aparte: [`Reparacion_ADN.apkg`](Reparacion_ADN.apkg) (366 tarjetas) |
| 6 | Genética del cáncer: biología molecular, hallmarks y perspectivas terapéuticas | S. Y. Ospina Lagos | [06_Genetica_del_cancer.md](guia/06_Genetica_del_cancer.md) | 156 tarjetas |
| 7 | Técnicas de biología molecular | M. Rey Buitrago | [07_Tecnicas_de_biologia_molecular.md](guia/07_Tecnicas_de_biologia_molecular.md) | 142 tarjetas |

El capítulo 5 y su mazo se hicieron antes que el resto, por eso el mazo de reparación del ADN va en un archivo aparte y usa tarjetas cloze y de pregunta-respuesta en lugar de Basic.

**Ruta sugerida**: ciclo celular → reparación del ADN (continúa directamente desde los puntos de control) → genética del cáncer (integra las dos anteriores) → genética del desarrollo → errores innatos del metabolismo. La bioinformática y las técnicas de biología molecular son transversales: estudia las técnicas temprano, porque las demás clases las usan (FISH, PCR, NGS), y usa la bioinformática para buscar en OMIM, dbSNP o Ensembl cada enfermedad.

---

## Conexiones entre clases

| Concepto | Dónde aparece | La conexión |
|---|---|---|
| **ATM, ATR, CHK1/2, p53, p21** | Ciclo celular (3.13); [reparación del ADN (sección 2.5)](guia/05_Reparacion_del_ADN.md#25-la-respuesta-al-daño-del-adn-ddr-diap-7) | Son el mismo sistema: los sensores del daño del ADN son los que frenan el ciclo |
| **BRCA1/2, RAD51 y recombinación homóloga** | Ciclo celular (3.13); [reparación del ADN (sección 7)](guia/05_Reparacion_del_ADN.md#7-roturas-de-doble-cadena-nhej-y-hr) | La recombinación homóloga solo ocurre en S y G2 porque necesita la cromátida hermana |
| **CDK7–ciclina H (CAK)** | Ciclo celular (3.8); [reparación del ADN (NER)](guia/05_Reparacion_del_ADN.md#5-reparación-por-escisión-de-nucleótidos-ner) | La cinasa que activa a las CDK es parte de TFIIH, el complejo que abre el ADN en la reparación por escisión de nucleótidos |
| **c-MYC** | Ciclo celular (3.11); desarrollo (2.3) | Es un mitógeno interno que acelera el ciclo y uno de los cuatro factores de Yamanaka |
| **Ciclos sin G1 ni G2** | Ciclo celular (3.2); desarrollo (2.1) | Los embriones tempranos solo replican y dividen; el control de G1 aparece después |
| **miR-302 y células madre** | Ciclo celular (3.16); desarrollo (2.3) | Silencian p21: por eso las células pluripotentes ciclan rápido |
| **Metilación del ADN** | Desarrollo (2.2); ciclo (3.17); reparación del ADN (MGMT) | La epigenética borra y reescribe marcas en el embrión; silenciar *MGMT* por metilación predice respuesta a temozolomida |
| **Apoptosis** | Desarrollo (2.3); ciclo (3.13) | Separa los dedos en el embrión y elimina células con ADN irreparable (p53 → PUMA, BAX) |
| **Malformaciones y EIM** | Desarrollo (2.9); EIM (4.6, 4.9, 4.11) | Los EIM tipo intoxicación **no** causan malformaciones (la placenta elimina el tóxico); algunos energéticos y de moléculas complejas (colesterol) **sí** |
| **Fenotipo dismórfico** | Desarrollo (2.9); EIM (4.12) | Las MPS producen rasgos "toscos", pero un fenotipo normal no las descarta |
| **Hidrops fetal no inmune** | EIM (4.12) | Hallazgo prenatal que obliga a pensar en enfermedades lisosomales (MPS VII) |
| **Exoma y bases de datos** | Bioinformática (1.7–1.8); desarrollo; EIM | El exoma confirma síndromes y EIM; OMIM, dbSNP y Ensembl permiten interpretar las variantes |
| **Herencia autosómica recesiva y consanguinidad** | Bioinformática (*HERC1*); EIM (PKU, MPS, acidemia propiónica) | Padres portadores sanos: los casos parecen esporádicos |
| **Tamizaje neonatal** | Bioinformática (medicina genómica); EIM (4.3) | Ejemplo de medicina genómica en salud pública: Ley 1980 de 2019 y Resolución 117 de 2026 en Colombia |
| **Rb, E2F y CDK4/6** | Ciclo celular (3.11); [cáncer (6.6, 6.11)](guia/06_Genetica_del_cancer.md#611-evasión-de-los-supresores-de-crecimiento-diap-20) | El freno del punto R es el hallmark "evasión de supresores"; los inhibidores de CDK4/6 solo funcionan si el tumor conserva Rb |
| **p53, p21 y los dos golpes** | Ciclo celular (3.13); reparación (1.5); [cáncer (6.5, 6.11)](guia/06_Genetica_del_cancer.md#65-genes-supresores-y-la-hipótesis-de-los-dos-golpes-diap-10) | El guardián del genoma es el gen más mutado en cáncer; Li-Fraumeni es su forma germinal |
| **MMR, MSI y síndrome de Lynch** | Reparación (sección 6); [cáncer (6.8, 6.25)](guia/06_Genetica_del_cancer.md#68-evolución-clonal-e-inestabilidad-genómica-diap-1516-26) | La falla del MMR genera inestabilidad de microsatélites, alta carga mutacional y respuesta a pembrolizumab |
| **BRCA1/2 y PARP** | Reparación (7.7, 10.1); [cáncer (6.22, 6.23)](guia/06_Genetica_del_cancer.md#623-medicina-personalizada-diap-42) | La letalidad sintética convierte un defecto de reparación en diana terapéutica |
| **Senescencia y telómeros** | Ciclo celular (3.17); [cáncer (6.13, 6.19)](guia/06_Genetica_del_cancer.md#613-inmortalidad-replicativa-diap-22) | La senescencia frena al tumor, pero su SASP lo ayuda; el tumor escapa reactivando la telomerasa |
| **miARN** | Ciclo celular (3.16); cáncer (6.3) | miR-17-92 y miR-21 aceleran (oncomiR); let-7, miR-34 y miR-200 frenan |
| **FISH, PCR y NGS** | [Técnicas (7.13, 7.15, 7.16)](guia/07_Tecnicas_de_biologia_molecular.md#713-fish-diap-38); cáncer (6.4, 6.23); bioinformática (1.8) | HER2 y BCR-ABL se detectan por FISH; las mutaciones driver, por PCR o NGS; el exoma es NGS |
| **Inserción viral** | Cáncer (6.4); [técnicas (7.17)](guia/07_Tecnicas_de_biologia_molecular.md#717-aplicaciones-clínicas-terapia-génica-y-ogm-diap-4648) | El mismo mecanismo que activa oncogenes causó leucemia en un ensayo de terapia génica (2003) |
| **Hemoglobina S** | Técnicas (7.7) | Ejemplo clásico de RFLP (MstII) y hoy de terapia génica con CRISPR |

---

## Tabla transversal de enfermedades

| Enfermedad | Gen o alteración | Herencia | Mecanismo | Clase |
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

---

## Fe de erratas consolidada

Errores o datos desactualizados de las diapositivas. El detalle y las fuentes están en la sección "✅ Verificación" de cada capítulo.

**Bioinformática** ([detalle](guia/01_Bioinformatica_y_medicina_genomica.md#-verificación-de-datos-de-la-clase))
- 20.000–25.000 genes → hoy ~19.000–20.000 codificantes.
- Code School ya no existe; un enlace de recursos está caído.
- El PDB suele clasificarse como base primaria, no secundaria.
- Frontier ya no es el n.º 1 del TOP500 (es el n.º 3 en noviembre de 2026).

**Genética del desarrollo** ([detalle](guia/02_Genetica_del_desarrollo.md#-verificación-de-datos-de-la-clase))
- Cita de Darwin: 1859, no 1942.
- Células del adulto: ~3,7 × 10¹³, no 10.000 billones.
- La tríada ectrodactilia + displasia ectodérmica + fisura es el síndrome EEC (*TP63*), no SHFM1 aislada.
- *BMP1* no pertenece a la superfamilia TGF-β (es una metaloproteasa).
- Dominio *paired*: 128 aa; artrogriposis y glosoptosis estaban mal escritas.

**Ciclo celular** ([detalle](guia/03_Ciclo_celular.md#-verificación-de-datos-de-la-clase))
- p16 = INK4a y p15 = INK4b (la diapositiva los invierte).
- Las imágenes de las diapositivas 12, 19 y 36 tienen texto ilegible o el punto de control del huso en G2; el SAC actúa en M y el punto R al final de G1.
- Límite de Hayflick: ~40–60 duplicaciones.

**Errores innatos del metabolismo** ([detalle](guia/04_Errores_innatos_del_metabolismo.md#-verificación-de-datos-de-la-clase))
- La PKU se describió en 1934 (Følling).
- La ICIMD (2021) lista 1.450 EIM.
- Colombia: la Resolución 117 de 2026 hizo obligatorias las 7 pruebas del tamizaje básico.
- *PAH*: más de 950 variantes (más de 3.000 en PAHvdb), no 600.
- El tratamiento de la PKU empieza desde 6 mg/dL (360 µmol/L); 20 mg/dL define la forma clásica.
- Nuevas terapias: sepiapterina (2025).
- En los casos clínicos: VCM y HCM invertidos; referencia de insulina errada; la CK alta en la glucogenosis VI sugiere compromiso muscular.

**Genética del cáncer** ([detalle](guia/06_Genetica_del_cancer.md#-verificación-de-datos-de-la-clase))
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

**Técnicas de biología molecular** ([detalle](guia/07_Tecnicas_de_biologia_molecular.md#-verificación-de-datos-de-la-clase))
- El Coomassie tiñe proteínas, no ácidos nucleicos.
- Los extremos de HindIII no son "asimétricos".
- En el Northern blot el ARN no se digiere con enzimas de restricción; además es semicuantitativo.
- La FISH tiene resolución de ~50 kb a 3 Mb; ">5 Mb" es la del cariotipo.
- Solo lentivirus y retrovirus dan expresión estable; adenovirus y AAV son mayormente episomales.
- El BAC lo desarrollaron Shizuya et al. (1992), no "Melsimon".
- El núcleo CODIS tiene 20 loci desde 2017; los gemelos monocigóticos comparten perfil.

---

## Cómo estudiar con el mazo de Anki

- Archivo: [`Genetica_Biologia_Molecular.apkg`](Genetica_Biologia_Molecular.apkg). Instrucciones de importación en el [README](README.md).
- Todas las tarjetas son **Basic**: pregunta en el anverso; respuesta corta en negrita y, debajo, una línea gris con la explicación y la diapositiva.
- **Etiquetas útiles** para filtrar (Explorar → buscar `tag:nombre`):
  - `verificado`: tarjetas que corrigen o actualizan la diapositiva (repásalas antes del examen).
  - `ampliacion`: contenido que no está en las diapositivas. Si solo quieres lo de la clase, suspéndelas con `tag:ampliacion`.
  - `caso`, `clinica`, `numeros`, `lista`, `trampa`, `historia`.
  - Por tema: `bioinformatica`, `desarrollo`, `ciclo_celular`, `eim`, `cancer`, `tecnicas`, y subtemas como `pku`, `mps`, `p53`, `sac`, `hallmarks`, `colombia`, `pcr`, `fish`, `hbs`.
- Ritmo sugerido: 20–30 tarjetas nuevas al día; con 681 tarjetas, el mazo completo entra en 4–5 semanas. Si tienes examen pronto, empieza por el submazo de la clase que viene.
- Lee primero el capítulo de la guía y después haz sus tarjetas: el orden de las tarjetas sigue el de la guía.
- **Reparación del ADN** tiene su propio archivo, [`Reparacion_ADN.apkg`](Reparacion_ADN.apkg), que crea el mazo *Reparación del ADN (Medicina)*. Sus etiquetas y ajustes recomendados están en la [sección 16 del capítulo 5](guia/05_Reparacion_del_ADN.md#16-plan-de-estudio-y-cómo-usar-el-mazo-de-anki).

---

## Cómo crecerá esta guía

Cuando lleguen nuevas diapositivas:

1. Se verifica el contenido y se escribe un capítulo nuevo en `guia/` con la misma estructura.
2. Se crea `anki/cards_NN_tema.txt` y se añade su submazo en `anki/build_deck.py`.
3. Se actualizan esta página (capítulos, conexiones, tabla de enfermedades, fe de erratas) y el README.
4. Las tarjetas existentes conservan su id: al reimportar el `.apkg`, Anki agrega las nuevas y actualiza las editadas **sin perder tu progreso**.
