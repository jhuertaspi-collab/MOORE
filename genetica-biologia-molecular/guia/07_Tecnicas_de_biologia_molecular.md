# 7. Técnicas de biología molecular

> Clase del Prof. **Mauricio Rey Buitrago** (Dr. en Ciencias Farmacéuticas), curso de genética, Facultad de Medicina, Universidad Nacional de Colombia, 4 de agosto de 2026.
> Las citas *(Diap. N)* siguen la numeración del PDF de la clase (51 diapositivas; la tabla de contenidos de la diapositiva 2 usa otra numeración, por temas). Los símbolos 📌 ➕ ⚠️ ✅ 🩺 💊 🧠 se explican en la [guía principal](../Guia_de_estudio.md#cómo-usar-esta-guía).
> Es un capítulo transversal: las técnicas que aparecen aquí son las que se usan en la [genética del cáncer](06_Genetica_del_cancer.md) (FISH, NGS, biopsia líquida), la [bioinformática](01_Bioinformatica_y_medicina_genomica.md) (exoma, bases de datos) y la [reparación del ADN](05_Reparacion_del_ADN.md) (MSI, BRCA).

---

## Índice

- [Lo esencial en un minuto](#lo-esencial-en-un-minuto)
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
- [✅ Verificación de datos de la clase](#-verificación-de-datos-de-la-clase)
- [Autoevaluación](#autoevaluación)
- [Glosario](#glosario)
- [Referencias](#referencias)

---

## Lo esencial en un minuto

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

## 7.1 Fundamentos y objetivos del diagnóstico molecular *(Diap. 3–4)*

📌 La biología molecular estudia la relación entre **ADN, ARN y proteínas**: cómo se almacena la información genética y cómo se ejecuta para determinar la función celular.

**Meta del diagnóstico molecular**: obtener información genética detallada y **detectar alteraciones** en el ADN, el ARN o las proteínas.

| Estrategia | Qué analiza | ➕ Ejemplos |
|---|---|---|
| **Indirecta** | Productos génicos, cambios fisicoquímicos o hibridación, para **inferir** la anomalía | Electroforesis de hemoglobina, RFLP, Southern, FISH, microarreglos |
| **Directa** | **Secuencia** del ADN: identifica la variante de forma explícita | Sanger, NGS |

---

## 7.2 Muestras biológicas para ADN *(Diap. 5)*

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

## 7.3 Extracción de ADN *(Diap. 6–9)*

### Tres principios *(Diap. 6)*

| Principio | Qué busca |
|---|---|
| **Recuperación máxima** | Obtener la mayor cantidad posible de material genético |
| **Eliminación de inhibidores** | Proteger el ADN de las **nucleasas** y retirar contaminantes que inhiben la PCR |
| **Calidad e integridad** | ADN de **doble cadena** íntegro, apto para PCR y secuenciación |

➕ Inhibidores típicos de la PCR: **hemo** (sangre), **heparina**, **melanina**, **ácidos húmicos** (suelo), **índigo** (tela de jean), restos de fenol o etanol. El **EDTA** del tampón protege el ADN porque **quela el Mg²⁺** que necesitan las ADNasas.

### Pureza y concentración *(Diap. 6)*

| Medida | Valor esperado | Si está baja |
|---|---|---|
| **A260/A280** | **~1,8** para ADN; ~2,0 para ARN | **Proteínas** o fenol |
| ➕ **A260/A230** | ~2,0–2,2 | Sales caotrópicas (guanidina), carbohidratos, fenol |
| ➕ **Concentración** | **1 unidad de A260 = 50 µg/mL de ADN de doble cadena** (40 µg/mL de ARN) | — |

🧠 El ADN absorbe a **260 nm** (bases); las proteínas, a **280 nm** (triptófano y tirosina).

### Cantidades teóricas *(Diap. 7)*

| Fuente | ADN |
|---|---|
| **Célula diploide** | **~6 pg** (➕ ~6,6 pg) |
| **Espermatozoide** (haploide) | **~3 pg** |
| **1 µL de sangre** | **30–60 ng** (➕ viene de los 4.000–11.000 leucocitos por µL) |
| **PCR de identificación** | **≈ 1 ng ≈ 350 espermatozoides** (unos 300 genomas haploides o 150 células diploides) |

✅ La diapositiva llama "PCR estándar" a 1 ng. Ese es el ADN óptimo de los **kits forenses de STR** (0,5–1 ng). En una PCR de rutina suelen usarse 10–100 ng de ADN genómico.

**Cálculo**: 1 ng ÷ 3 pg = 1.000 pg ÷ 3 pg ≈ **333 genomas haploides**.

### Métodos de extracción *(Diap. 8–9)*

| Método | Principio | Ventaja | Desventaja |
|---|---|---|---|
| **Orgánico: fenol-cloroformo** | Las proteínas pasan a la fase orgánica o a la interfase; el ADN queda en la **fase acuosa** | Muy eficiente en muestras complejas | **Solventes tóxicos** |
| **No orgánico: *salting out*** | **Proteinasa K** digiere proteínas; **sales concentradas** las precipitan; el ADN se precipita con alcohol | Ideal para **sangre y tejidos**, sin solventes tóxicos | Pureza algo menor |
| **Sílice** (columnas, perlas magnéticas) | En sales caotrópicas el ADN se **une a la sílice**; se lava y se eluye con baja sal | **Alta pureza, automatizable** | Costo |
| **Papel FTA** | Papel tratado que **lisa las células y protege el ADN** | **Fácil transporte** y almacenamiento a temperatura ambiente | Poca cantidad |
| ➕ **Chelex** *(figura de la Diap. 9)* | Hervir la muestra con una resina quelante | Rápido (forense) | ADN de cadena sencilla, solo sirve para PCR |

➕ El **pH del fenol** decide qué se extrae: a **pH ~8** el ADN queda en la fase acuosa; el **fenol ácido** (pH 4–5) retiene el ADN en la interfase y deja el **ARN** arriba (base del TRIzol).

### Protocolo universal de purificación *(Diap. 9)*

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

## 7.4 Electroforesis *(Diap. 10–12)*

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

### Métodos de detección *(Diap. 12)*

| Agente | Tipo | Características |
|---|---|---|
| **Bromuro de etidio (EtBr)** | **Intercalante** fluorescente con **luz UV** | Clásico y sensible para ADN y ARN; **mutágeno** |
| **SYBR Safe** | Fluorescente | **Menos tóxico**, sensibilidad similar al EtBr; ➕ se puede ver con luz azul (figura) |
| **Azul de Coomassie** | Colorimétrico | **Tiñe proteínas** (SDS-PAGE) |
| **Tinción de plata** | Colorimétrico | **Sensibilidad extrema**: detecta trazas de proteínas o ácidos nucleicos en PAGE (geles marrones de la figura) |

✅ La diapositiva dice que el Coomassie tiene "menor sensibilidad para la detección de ácidos nucleicos". El Coomassie **no se usa para ácidos nucleicos**: es un colorante de **proteínas**.

---

## 7.5 Enzimas de restricción *(Diap. 13–16)*

### Definición *(Diap. 13)*

📌 **Endonucleasas** que reconocen **secuencias palindrómicas específicas** en el **ADN de doble cadena** y lo cortan **hidrolizando enlaces fosfodiéster**.

**Palíndromo**: la secuencia se lee igual en las dos cadenas en sentido 5'→3'. Ejemplo: EcoRI, 5'-GAATTC-3' / 3'-CTTAAG-5'.

➕ **Función natural**: son el "sistema inmune" de las bacterias contra los fagos (**sistema de restricción-modificación**). La bacteria **metila su propio ADN** en esos sitios para no cortarlo. Arber, Nathans y Smith recibieron el **Nobel de 1978**.

### Tipos de extremos *(Diap. 13, 15)*

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

### Nomenclatura *(Diap. 14)*

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

### Aplicaciones *(Diap. 16)*

| Área | Uso |
|---|---|
| **Diagnóstico y caracterización** | **RFLP** y **mapas de restricción** |
| **Ingeniería genética** | **Clonación** y **bibliotecas genómicas** |
| **Hibridación** | Preparar el ADN para **Southern blot** |

✅ La diapositiva incluye el **Northern** entre las aplicaciones. Las enzimas de restricción cortan **ADN de doble cadena**: en un Northern el ARN **no se digiere**. Como mucho, se usan para preparar o linealizar el molde de la sonda.

➕ La **ADN ligasa** sella el enlace fosfodiéster entre el vector y el inserto (la de T4 usa ATP). Tras la ligación se forma el **ADN recombinante** (figuras de la diapositiva 16).

---

## 7.6 Ejercicio de digestión, resuelto *(Diap. 17)*

La diapositiva da una secuencia de **350 pb** (molécula lineal) y tres enzimas: **HaeIII (GG^CC)**, **EcoRI (G^AATTC)** y **HindIII (A^AGCTT)**. La secuencia completa, numerada:

```
   1 TTTTTTTTATATACCATCAGCACTTGCTATGAGGGCCAGCGTAGATCGGTCCAAGTCCACCTAGGGTATA
  71 CCGCGCCCCGGGACGAAGATATATATATATAGTACCACTCACTTGGAATTCCTGCGCGCGCGCGCCTACC
 141 TATATATAGTACAAAGCTTGATATAATGCCACTCCAGTCACTTGCTATGACTAGGAATTAGCGAAAGGGG
 211 GTTAATCGGTCCCCACTCCTTGCTCATGATTGTGCGTAGGAATTCATCGGTCCCCGCTATAATATTCCCA
 281 CTCAGCTTGCTATGATTGTAGCGTAATCGGTCCATTTTTTTTCCCGGGCCATCAGCACTTGCTATGATTG
```

### Solución

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

### Cómo se construye un mapa de restricción *(figura de la Diap. 17)*

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

## 7.7 RFLP y diagnóstico de la hemoglobina S *(Diap. 18–23)*

### Polimorfismo de longitud de fragmentos de restricción (RFLP) *(Diap. 18)*

📌 Una variante puede **crear o destruir un sitio de restricción**. Entonces la enzima produce **fragmentos de distinto tamaño** en las personas con y sin la variante.

| Paso | Qué se hace |
|---|---|
| 1 | **Extracción** del ADN (y, en la versión moderna, **PCR** de la región, a veces con cebadores marcados) |
| 2 | **Digestión enzimática** |
| 3 | **Electroforesis** |
| 4 | **Análisis de las bandas**: clásicamente, **Southern blot** con una **sonda** de la región; hoy, detección láser de los productos marcados |

### La anemia falciforme *(Diap. 19–21)*

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

### El RFLP con MstII *(Diap. 22–23)*

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

## 7.8 Clonación: tipos y vectores *(Diap. 24–26)*

### Tres significados de "clonación" *(Diap. 24)*

| Tipo | Objetivo | Producto |
|---|---|---|
| **Genética (molecular)** | Copias idénticas de un gen o fragmento de ADN | Fragmentos para investigación y **proteínas recombinantes** |
| **Reproductiva** | Un organismo genéticamente idéntico | Un organismo viable (➕ la oveja Dolly, 1996) |
| **Terapéutica** | Células madre para tratamientos | **Células pluripotentes** para generar tejidos |

**Clonación terapéutica** *(figura)*: se transfiere el núcleo de una célula adulta del paciente a un **óvulo enucleado** (➕ transferencia nuclear somática), un pulso eléctrico inicia el desarrollo embrionario, se extraen las células madre y se diferencian en el tejido necesario (corazón, riñón, médula espinal, células productoras de insulina). El trasplante **no se rechaza** porque el ADN es del propio paciente.

➕ Las **iPSC** (Yamanaka, 2006) obtienen células pluripotentes reprogramando células adultas, sin óvulos ni embriones. Ver el [capítulo 2](02_Genetica_del_desarrollo.md#23-principios-de-las-familias-de-genes-del-desarrollo-diap-1218).

### Vectores de clonación *(Diap. 25–26)*

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

## 7.9 El plásmido y el flujo de la clonación *(Diap. 27–29)*

### Anatomía del plásmido *(Diap. 27)*

| Elemento | Función |
|---|---|
| **Origen de replicación (ori)** | Replicación **autónoma** dentro de la bacteria |
| **Marcador de selección** (Amp<sup>R</sup>, Tet<sup>R</sup>) | Solo sobreviven en el antibiótico las bacterias que tienen el plásmido |
| **Sitio de clonación múltiple (MCS)** | Muchos sitios de restricción únicos donde insertar el ADN |
| **Gen reportero (lacZ)** | Cribado visual: indica si el inserto entró |

### Selección azul-blanca *(Diap. 28)*

| Colonia | Qué tiene | Por qué |
|---|---|---|
| **Azul** | Plásmido **sin inserto** | *lacZ* intacto → β-galactosidasa funcional → corta **X-gal** → color azul |
| **Blanca** | Plásmido **recombinante** | El inserto **interrumpe *lacZ*** → no hay β-galactosidasa → colonia blanca |

⚠️ Son dos filtros distintos: el **antibiótico** selecciona las bacterias que tienen **plásmido**; el **color** distingue cuáles tienen **inserto**.

➕ El medio lleva también **IPTG**, que induce la expresión de *lacZ*.

### Flujo de clonación *(Diap. 28–29)*

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

## 7.10 Vectores lanzadera, transfección y genes reporteros *(Diap. 30–33)*

### Vectores lanzadera *(Diap. 30)*

📌 Se replican en **dos sistemas distintos**, normalmente *E. coli* (procariota) y levadura o células de mamífero (eucariota). Se manipulan rápido en la bacteria y luego se expresan en el sistema complejo.

Elementos de un vector lanzadera de levadura *(figura)*: origen y resistencia a antibiótico **para la bacteria**, origen de replicación **de levadura**, gen de selección en levadura (síntesis de **leucina**), **centrómero de levadura** y sitio de clonación múltiple.

Uso: expresión de **proteínas recombinantes** y transferencia de genes con vectores virales modificados (terapia génica).

### Métodos de transferencia de genes *(Diap. 31–32)*

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

### Genes reporteros *(Diap. 33)*

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

## 7.11 Bibliotecas de ADN e hibridación de colonias *(Diap. 34–35)*

### Construcción de una biblioteca *(Diap. 34)*

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

### Hibridación de colonias *(Diap. 35)*

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

## 7.12 Blotting: Southern, Northern y Western *(Diap. 36–37)*

📌 Se separan las moléculas (casi siempre por electroforesis), se **transfieren a una membrana** y se detecta la molécula diana con una sonda o un anticuerpo.

| Técnica | Detecta | Separación | Sonda | ➕ Usos clínicos o de investigación |
|---|---|---|---|---|
| **Southern** (Edwin Southern, 1975) | **ADN** | Digestión + agarosa + desnaturalización alcalina | ADN o ARN marcado | RFLP; **expansiones grandes** que la PCR no amplifica (X frágil con más de 200 CGG); reordenamientos y clonalidad |
| **Northern** (1977) | **ARN** | Gel **desnaturalizante** (formaldehído) | ADN o ARN marcado | **Tamaño y abundancia** de un ARNm, splicing alternativo |
| **Western** (1979) | **Proteínas** | **SDS-PAGE** | **Anticuerpos** (primario y secundario marcado) | Confirmar expresión de una proteína y su tamaño |
| **Dot/slot blot** | ADN, ARN o proteína | **Sin electroforesis**: la muestra se aplica directo | Sonda o anticuerpo | Tamizaje rápido de muchas muestras |

🧠 **SNOW DROP**: **S**outhern–**D**NA, **N**orthern–**R**NA, **O**–**O**, **W**estern–**P**rotein.

⚠️ "Southern" es un **apellido**; Northern y Western son **juegos de palabras** con los puntos cardinales.

### Flujo del Northern blot *(Diap. 37)*

1. **Extracción del ARN** (sin ARNasas).
2. **Electroforesis** desnaturalizante.
3. **Transferencia** a la membrana.
4. **Generación de la sonda**: la clase usa el sistema **pGEM-T** y nucleótidos marcados. ➕ pGEM-T es un vector de clonación T/A con promotores **T7 y SP6** que permite sintetizar **sondas de ARN** por transcripción *in vitro*.
5. **Hibridación**.
6. **Visualización**.

✅ La diapositiva califica al Northern de "cuantitativo". Es **semicuantitativo**: compara la abundancia relativa entre muestras. Hoy la cuantificación de ARN se hace sobre todo con **RT-qPCR** y **RNA-seq**.

---

## 7.13 FISH *(Diap. 38)*

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

## 7.14 Microarreglos *(Diap. 39–40)*

### Principio *(Diap. 39)*

| Elemento | Qué es |
|---|---|
| **Sustrato sólido** | Miles de **sondas de ADN** inmovilizadas que hibridan **a la vez** con la muestra |
| **Marcaje diferencial** | Dos fluoróforos: **Cy3 (verde)** y **Cy5 (rojo)**, para comparar dos estados biológicos |
| **Aplicaciones** | **Expresión génica**, detección de **SNP**, plataformas de oligonucleótidos |

### Análisis de los datos *(Diap. 40)*

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

## 7.15 PCR *(Diap. 41–44)*

📌 La **reacción en cadena de la polimerasa** amplifica *in vitro* un segmento de ADN definido por dos **cebadores**. A partir de muy poco ADN genera millones de copias.

### Componentes ➕

ADN molde · **dos cebadores** (directo y reverso) · **dNTP** · **Mg²⁺** · tampón · **ADN polimerasa termoestable** (Taq).

### El ciclo

| Paso | Temperatura | Qué pasa |
|---|---|---|
| **1. Desnaturalización** | **94–96 °C** | Se separan las dos cadenas |
| **2. Alineamiento (*annealing*)** | **50–65 °C** | Los cebadores se unen a sus secuencias complementarias (➕ ~5 °C por debajo de su Tm) |
| **3. Extensión** | **72 °C** | La **Taq polimerasa** sintetiza la cadena nueva desde el extremo 3' del cebador (➕ ~1 kb por minuto) |

- Se repite **20–40 veces** (~30 ciclos).
- Crecimiento **exponencial: 2ⁿ**. Tras 30 ciclos, en teoría, **2³⁰ ≈ 10⁹ copias** por molécula molde. ➕ En la práctica la reacción llega a una **meseta** porque se agotan los reactivos.

### Qué pasa en los primeros ciclos *(Diap. 42–44)*

| Ciclo | Productos |
|---|---|
| **1** | Cadenas "largas": empiezan en el cebador pero no tienen final definido |
| **2** | Aparecen las primeras **cadenas sencillas de longitud exacta** (entre los dos cebadores) |
| **3** | Aparecen las primeras **2 moléculas de doble cadena de longitud exacta** |
| **n** | Moléculas de longitud exacta: **2ⁿ − 2n**; dominan por completo a partir de unos pocos ciclos |

➕ Kary **Mullis** inventó la PCR en 1983 (**Nobel de Química 1993**). La **Taq** viene de *Thermus aquaticus*, una bacteria de aguas termales de Yellowstone; al resistir 95 °C, ya no hay que añadir enzima en cada ciclo.

### Variantes ➕

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

## 7.16 Secuenciación: de Sanger a NGS *(Diap. 45)*

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

➕ **Profundidad (cobertura)**: cuántas lecturas cubren cada base. Un genoma clínico suele hacerse a ~30x; los paneles oncológicos, a cientos o miles de lecturas para detectar variantes en pocas células. Ver el [capítulo 1](01_Bioinformatica_y_medicina_genomica.md#18-aplicaciones-en-la-clínica-diap-4959) (exoma) y el [capítulo 6](06_Genetica_del_cancer.md#623-medicina-personalizada-diap-42) (NGS en oncología).

---

## 7.17 Aplicaciones clínicas, terapia génica y OGM *(Diap. 46–48)*

### PCR y secuenciación en la clínica *(Diap. 46)*

| Aplicación | ➕ Ejemplos |
|---|---|
| **Identificación de mutaciones** (enfermedades genéticas, oncología de precisión) | *CFTR* en fibrosis quística, *EGFR* y *KRAS* en tumores, *BRCA1/2* |
| **Detección de patógenos** (epidemiología, infecciones críticas) | RT-qPCR para SARS-CoV-2; carga viral de VIH y VHC; GeneXpert para tuberculosis y resistencia a rifampicina |
| **Farmacogenética** (tratamiento según el genotipo) | *CYP2C19* y clopidogrel; **HLA-B\*57:01** y abacavir; **HLA-B\*15:02** y carbamazepina; *TPMT*/*NUDT15* y tiopurinas; *DPYD* y fluoropirimidinas |

La diapositiva resalta su **alta sensibilidad analítica**. ✅ "Especificidad clínica total" es una exageración: ninguna prueba tiene 100 % de especificidad (hay contaminación, variantes en el sitio del cebador y errores preanalíticos).

### Terapia génica *(Diap. 47)*

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
| Tisagenlecleucel (2017) | **Lentivirus** con un receptor quimérico (CAR) | Leucemia linfoblástica B ([capítulo 6](06_Genetica_del_cancer.md#623-medicina-personalizada-diap-42)) |
| Exagamglogén autotemcel (2023) | **CRISPR-Cas9** *ex vivo* | Anemia falciforme y β-talasemia |

⚠️ ➕ **Riesgos** que dieron forma a la disciplina: un vector retroviral se insertó junto al oncogén *LMO2* y causó **leucemia** en niños tratados por inmunodeficiencia ligada al X (2003): es la **activación de un oncogén por inserción viral** del [capítulo 6](06_Genetica_del_cancer.md#64-cómo-se-activa-un-oncogén-diap-9). Y en 1999 una **respuesta inmune masiva a un adenovirus** causó la muerte de Jesse Gelsinger.

### Organismos genéticamente modificados *(Diap. 48)*

📌 Plantas, animales o microorganismos cuyo material genético se **alteró por ingeniería genética** para introducir "genes de interés". Sirven para estudiar la función de genes y vías biológicas.

**Propósitos**: resistencia de cultivos a plagas (➕ maíz y algodón *Bt*), mayor rendimiento agrícola, **producción de proteínas terapéuticas** (biofármacos como la insulina), **biorremediación** y nuevas estrategias de terapia génica.

➕ En investigación, los **ratones transgénicos** (ganan un gen) y ***knock-out*** (pierden uno) permiten ver qué hace un gen en un organismo completo.

---

## 7.18 Identificación humana y genética forense *(Diap. 49)*

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

## 7.19 Flujo integrado y perspectivas *(Diap. 50–51)*

### De la muestra al diagnóstico *(Diap. 50)*

```
Muestra (sangre, saliva, tejido) → extracción y purificación del ADN → amplificación por PCR
      → secuenciación (Sanger o NGS) o electroforesis → interpretación
```

**Flujo de clonación** *(figura)*: digestión de restricción → ligadura → transformación bacteriana → inoculación de una colonia → purificación del plásmido → **secuenciación de Sanger** para confirmar el inserto.

📌 **Calidad del material**: el aislamiento es crítico para evitar la **contaminación externa**.

### Perspectivas *(Diap. 51)*

| Eje | Contenido |
|---|---|
| **Implicaciones éticas** | Privacidad genética y equidad en el acceso a la intervención del genoma humano |
| **Progreso técnico** | Integración de datos **multiómicos** y herramientas de **edición génica** (➕ CRISPR-Cas9; Nobel de Química 2020 para Charpentier y Doudna) |
| **Síntesis** | Colaboración interdisciplinaria y reflexión bioética para que el potencial genético beneficie a la humanidad |

---

## 7.20 ➕ ¿Qué técnica uso para cada pregunta?

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

## ✅ Verificación de datos de la clase

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

## Autoevaluación

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

## Glosario

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

## Referencias

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
