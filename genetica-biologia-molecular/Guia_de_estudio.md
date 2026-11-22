# Guía de estudio: Genética y Biología Molecular

> Medicina, Universidad Nacional de Colombia, 2026. Basada en las diapositivas de clase de los profesores **Oscar Ortega-Recalde** y **Sandra Yaneth Ospina Lagos**, verificada contra fuentes primarias y ampliada con lo necesario para entender cada tema.
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

El capítulo 5 y su mazo se hicieron antes que el resto, por eso el mazo de reparación del ADN va en un archivo aparte y usa tarjetas cloze y de pregunta-respuesta en lugar de Basic.

**Ruta sugerida**: ciclo celular → reparación del ADN (continúa directamente desde los puntos de control) → genética del desarrollo → errores innatos del metabolismo. La bioinformática es transversal: úsala para buscar en OMIM, dbSNP o Ensembl cada enfermedad de las otras clases.

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
| Retinoblastoma | *RB1* | AD (predisposición; dos golpes) | Freno del punto R | 3 |
| Li-Fraumeni | *TP53* | AD (predisposición) | Guardián del genoma | 3 |
| Ataxia-telangiectasia | *ATM* | AR | Señal de daño del ADN | 3, 5 |
| Cáncer de mama y ovario hereditario | *BRCA1*, *BRCA2* | AD (predisposición) | Recombinación homóloga | 3, 5 |
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

---

## Cómo estudiar con el mazo de Anki

- Archivo: [`Genetica_Biologia_Molecular.apkg`](Genetica_Biologia_Molecular.apkg). Instrucciones de importación en el [README](README.md).
- Todas las tarjetas son **Basic**: pregunta en el anverso; respuesta corta en negrita y, debajo, una línea gris con la explicación y la diapositiva.
- **Etiquetas útiles** para filtrar (Explorar → buscar `tag:nombre`):
  - `verificado`: tarjetas que corrigen o actualizan la diapositiva (repásalas antes del examen).
  - `ampliacion`: contenido que no está en las diapositivas. Si solo quieres lo de la clase, suspéndelas con `tag:ampliacion`.
  - `caso`, `clinica`, `numeros`, `lista`, `trampa`, `historia`.
  - Por tema: `bioinformatica`, `desarrollo`, `ciclo_celular`, `eim`, y subtemas como `pku`, `mps`, `p53`, `sac`.
- Ritmo sugerido: 20–30 tarjetas nuevas al día; con 383 tarjetas, el mazo completo entra en 2–3 semanas.
- Lee primero el capítulo de la guía y después haz sus tarjetas: el orden de las tarjetas sigue el de la guía.
- **Reparación del ADN** tiene su propio archivo, [`Reparacion_ADN.apkg`](Reparacion_ADN.apkg), que crea el mazo *Reparación del ADN (Medicina)*. Sus etiquetas y ajustes recomendados están en la [sección 16 del capítulo 5](guia/05_Reparacion_del_ADN.md#16-plan-de-estudio-y-cómo-usar-el-mazo-de-anki).

---

## Cómo crecerá esta guía

Cuando lleguen nuevas diapositivas:

1. Se verifica el contenido y se escribe un capítulo nuevo en `guia/` con la misma estructura.
2. Se crea `anki/cards_NN_tema.txt` y se añade su submazo en `anki/build_deck.py`.
3. Se actualizan esta página (capítulos, conexiones, tabla de enfermedades, fe de erratas) y el README.
4. Las tarjetas existentes conservan su id: al reimportar el `.apkg`, Anki agrega las nuevas y actualiza las editadas **sin perder tu progreso**.
