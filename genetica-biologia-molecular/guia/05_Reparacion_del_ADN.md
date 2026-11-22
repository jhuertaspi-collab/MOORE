# Mecanismos de reparación del ADN
## Guía de estudio completa: de la lesión molecular a la clínica

> Basada en la clase *"Mecanismos de reparación del ADN. De la lesión molecular a la clínica"* (Prof. Sandra Ospina Lagos, Genética y Ciencias Biomédicas) y ampliada con lo que necesitas para entenderla a fondo y para el examen.
>
> Capítulo 5 de la [guía de Genética y Biología Molecular](../Guia_de_estudio.md). Su mazo es [`Reparacion_ADN.apkg`](../Reparacion_ADN.apkg).

---

## Cómo usar esta guía

| Símbolo | Significado |
|---|---|
| 📌 | Idea clave de la clase. Si solo repasas algo, que sea esto. |
| ➕ | **Ampliación**: no está en las diapositivas, pero la necesitas para entender el tema o es típica de examen. |
| ⚠️ | Trampa frecuente o confusión típica. |
| 🩺 | Correlación clínica. |
| 💊 | Terapia o farmacología. |
| 🧠 | Mnemotecnia. |
| *(Diap. N)* | Diapositiva de la clase donde está el contenido. |

**Ruta recomendada:** lee la sección 1 (prerrequisitos) si no tienes fresca la estructura del ADN; después estudia las vías en orden (2 → 9), porque cada una se apoya en la anterior; termina con la integración (10), los casos (11) y las preguntas (12). El mazo de Anki sigue exactamente este orden.

---

## Índice

1. [Prerrequisitos: lo mínimo que necesitas saber](#1-prerrequisitos-lo-mínimo-que-necesitas-saber)
2. [El problema: el ADN se daña todo el tiempo](#2-el-problema-el-adn-se-daña-todo-el-tiempo)
3. [Reversión directa del daño (MGMT, fotoliasa, ALKBH)](#3-reversión-directa-del-daño)
4. [Reparación por escisión de bases (BER)](#4-reparación-por-escisión-de-bases-ber)
5. [Reparación por escisión de nucleótidos (NER)](#5-reparación-por-escisión-de-nucleótidos-ner)
6. [Reparación de apareamientos erróneos (MMR)](#6-reparación-de-apareamientos-erróneos-mmr)
7. [Roturas de doble cadena: NHEJ y HR](#7-roturas-de-doble-cadena-nhej-y-hr)
8. [Anemia de Fanconi y enlaces cruzados intercatenarios](#8-anemia-de-fanconi-y-enlaces-cruzados-intercatenarios)
9. [Tolerancia al daño: síntesis translesión (TLS)](#9-tolerancia-al-daño-síntesis-translesión-tls)
10. [Integración: de la biología a la clínica](#10-integración-de-la-biología-a-la-clínica)
11. [Casos clínicos resueltos](#11-casos-clínicos-resueltos)
12. [Preguntas de repaso resueltas y autoevaluación](#12-preguntas-de-repaso-resueltas-y-autoevaluación)
13. [Trampas de examen](#13-trampas-de-examen)
14. [Mnemotecnias](#14-mnemotecnias)
15. [Glosario](#15-glosario)
16. [Plan de estudio y cómo usar el mazo de Anki](#16-plan-de-estudio-y-cómo-usar-el-mazo-de-anki)
17. [Bibliografía](#17-bibliografía)

---

## Objetivos de aprendizaje *(Diap. 2)*

Al terminar deberías poder:

1. **Clasificar** las lesiones del ADN según su origen (endógeno o exógeno) y su tipo químico.
2. **Describir** los pasos y proteínas clave de la reversión directa, BER, NER, MMR, NHEJ, HR y la síntesis translesión.
3. **Relacionar** cada tipo de lesión con la vía que la repara.
4. **Correlacionar** defectos de reparación con enfermedades: xeroderma pigmentoso, Lynch, BRCA, ataxia-telangiectasia, Fanconi, SCID.
5. **Explicar** la base molecular de terapias: temozolomida, cisplatino, inhibidores de PARP e inmunoterapia.

---

## 1. Prerrequisitos: lo mínimo que necesitas saber

➕ Esta sección no está en la clase, pero sin ella muchas diapositivas se memorizan sin entenderse.

### 1.1 La anatomía del ADN que importa para la reparación

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

### 1.2 Lesión no es lo mismo que mutación

📌 Es la idea que da sentido a todo el tema.

- **Lesión**: alteración química o física del ADN (una base oxidada, un dímero, una rotura). Todavía es reparable porque la otra hebra conserva la información.
- **Mutación**: cambio de secuencia **fijado en ambas hebras** tras la replicación. Ya no parece daño: la célula no la "ve".

```
Lesión          1.ª replicación          2.ª replicación
O⁶-meG : C  ──►  O⁶-meG : T   ──►   A : T   (mutación G:C→A:T fijada)
```

La ventana para reparar es **antes de replicar**. Por eso la respuesta al daño detiene el ciclo celular.

### 1.3 Vocabulario de mutaciones

| Término | Definición | Ejemplo del tema |
|---|---|---|
| **Transición** | Purina↔purina o pirimidina↔pirimidina | O⁶-meG → G:C→A:T; UV → C→T; desaminación de 5-metilC → C→T |
| **Transversión** | Purina↔pirimidina | 8-oxoG → G:C→T:A; tabaco y aflatoxina → G→T |
| **Indel** | Inserción o deleción pequeña | Deslizamiento en microsatélites (MMR defectuoso) |
| **Cambio de marco** (*frameshift*) | Indel no múltiplo de 3 en región codificante | TGFBR2, BAX en tumores MSI |

🧠 **Transición** = te quedas en la misma "clase" de base (como transitar dentro del mismo barrio). **Transversión** = cambias de "versión" (de purina a pirimidina o al revés).

### 1.4 El ciclo celular y sus puntos de control

```
G1 ──[G1/S]──► S ──[intra-S]──► G2 ──[G2/M]──► M ──► G1
     (puntos de control entre corchetes)
```

- **G1/S**: impide replicar un ADN dañado (eje ATM → CHK2 → p53 → p21).
- **Intra-S**: frena la replicación si hay estrés replicativo (eje ATR → CHK1).
- **G2/M**: impide entrar en mitosis con roturas (ATR/ATM → CHK1/CHK2 → inhibición de CDC25 → CDK1 inactiva).
- En **S y G2** existe la **cromátida hermana**, molde perfecto para la recombinación homóloga. En **G1** (y en células que no se dividen, como las neuronas) no existe.

### 1.5 Genes "cuidadores" y la hipótesis de los dos golpes (Knudson)

- Los genes de reparación son **supresores de tumores de tipo "cuidador"** (*caretakers*): su pérdida no hace proliferar a la célula directamente, sino que **aumenta la tasa de mutación** (fenotipo mutador), y así se acumulan mutaciones en oncogenes y en supresores "porteros" (*gatekeepers*, como APC o RB1).
- **Dos golpes**: la célula necesita perder **los dos alelos** para perder la función.
  - En **Lynch** y **BRCA** se hereda un alelo mutado (primer golpe en todas las células). El tumor aparece cuando una célula pierde el segundo alelo (pérdida de heterocigosidad, mutación o metilación). Por eso la **predisposición se hereda de forma autosómica dominante**, aunque a nivel celular el defecto sea recesivo.
  - En **XP, Fanconi, A-T, MAP, SCID por Artemis o Bloom** el paciente hereda **dos** alelos mutados: todas sus células carecen de la función, y la herencia es **autosómica recesiva**.
- 🩺 Consecuencia práctica: las células normales de una portadora de BRCA1 tienen un alelo funcional y reparan bien. Solo el tumor es deficiente. Esa diferencia es la que explotan los inhibidores de PARP (sección 10.1).

### 1.6 ¿De dónde vienen los nombres?

| Prefijo | Origen | Ejemplos |
|---|---|---|
| **XP-A…G, V** | Grupos de complementación del xeroderma pigmentoso: células de pacientes que, fusionadas, **no** corrigen mutuamente el defecto tienen el mismo gen alterado | XPA, XPC, XPD |
| **ERCC** | *Excision Repair Cross-Complementing*: genes humanos que corrigen la sensibilidad a UV de mutantes de hámster | ERCC1, ERCC2 = XPD, ERCC6 = CSB |
| **MSH / MLH / PMS** | Homólogos de las proteínas bacterianas MutS y MutL | MSH2, MLH1, PMS2 |
| **RAD** | Mutantes de levadura sensibles a radiación | RAD51, RAD18 |
| **FANC** | Grupos de complementación de la anemia de Fanconi | FANCA, FANCD2, FANCD1 = BRCA2 |

---

## 2. El problema: el ADN se daña todo el tiempo

### 2.1 La magnitud *(Diap. 4)*

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

### 2.2 Fuentes de daño: endógenas y exógenas *(Diap. 5)*

#### Endógenas (metabolismo normal)

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

#### Exógenas (ambiente y fármacos)

| Agente | Lesión | Detalle clínico |
|---|---|---|
| **Radiación UV-B** | **Dímeros de pirimidina ciclobutano (CPD)** y **fotoproductos 6-4** entre pirimidinas vecinas de la misma hebra | ➕ CPD ≈ 75 % de los fotoproductos (distorsionan poco); 6-4 ≈ 25 % (distorsionan más). Firma: C→T y CC→TT |
| **Radiación ionizante** | **Roturas de doble cadena** (y SSB, bases oxidadas), a menudo agrupadas | ➕ Actúa de forma directa y mediante radicales hidroxilo del agua. Del orden de ~1.000 SSB y ~20–40 DSB por célula y por Gy |
| **Tabaco: benzo[a]pireno** | Se activa a **diol-epóxido (BPDE)** → **aductos voluminosos en guanina** | ➕ Transversiones G→T (C>A) en TP53 en el cáncer de pulmón |
| **Aflatoxina B1** (*Aspergillus*; maní y maíz mal almacenados) | Activada por citocromo P450 → **aductos en N7 de guanina** | Mutación **TP53 R249S** (G→T en el codón 249) en el **carcinoma hepatocelular**. ➕ Sinergia con hepatitis B |
| **Quimioterapia** | Cisplatino (aductos intracatenarios y enlaces cruzados), alquilantes (bases metiladas), inhibidores de topoisomerasa (roturas) | Ver sección 10.3 |

### 2.3 Catálogo visual de lesiones *(Diap. 6)*

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

### 2.4 Destinos de una lesión

```
                      ┌─► Reparada correctamente ─────────► célula sana
                      │
LESIÓN ──► DDR ───────┼─► Tolerada (TLS) ─────────────────► sobrevive, a veces con mutación
                      │
                      ├─► Mal reparada / replicada ───────► MUTACIÓN (cáncer si afecta genes clave)
                      │
                      └─► Daño excesivo ──────────────────► apoptosis o senescencia
```

### 2.5 La respuesta al daño del ADN (DDR) *(Diap. 7)*

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
- **ATM mutado → ataxia-telangiectasia** (sección 7.8).

### 2.6 Mapa general: cada lesión tiene su vía *(Diap. 8)*

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

### 2.7 Nobel de Química 2015 *(Diap. 9)*

Premio "por estudios mecanísticos de la reparación del ADN":

| Premiado | Vía | Aporte |
|---|---|---|
| **Tomas Lindahl** (Reino Unido/Suecia) | **BER** | Demostró que el ADN se degrada espontáneamente y descubrió las ADN-glicosilasas |
| **Aziz Sancar** (EE. UU./Turquía) | **NER** | Describió cómo se cortan y reemplazan segmentos dañados por UV; estudió la fotoliasa |
| **Paul Modrich** (EE. UU.) | **MMR** | Mostró cómo se corrigen los errores de apareamiento tras la replicación |

---

## 3. Reversión directa del daño

> Una enzima, un paso, sin cortar el esqueleto del ADN *(Diap. 10)*.

La reversión directa no retira bases ni sintetiza ADN: deshace químicamente la lesión en su sitio.

### 3.1 MGMT: la enzima "suicida" *(Diap. 11)*

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

### 3.2 Otras enzimas de reversión directa *(Diap. 11)*

| Enzima | Qué revierte | Cómo | Dato clave |
|---|---|---|---|
| **Fotoliasa** | Dímeros de pirimidina (CPD) | Usa **luz visible** (fotorreactivación; cofactor FAD) | Existe en bacterias, plantas y muchos animales; **ausente en los mamíferos placentarios** → los humanos dependemos de **NER** para los dímeros UV |
| **ALKBH2 / ALKBH3** | **1-metiladenina y 3-metilcitosina** | **Desmetilación oxidativa**; dioxigenasas dependientes de **Fe²⁺ y α-cetoglutarato** | Homólogas de AlkB bacteriana |

### 3.3 ➕ ¿Por qué la O⁶-meG mata a la célula? El papel de MMR

Esta conexión entre vías explica la clínica de la temozolomida:

1. Al replicar, frente a la O⁶-meG se inserta **T**.
2. **MMR** reconoce el par O⁶-meG:T como un error y retira la T de la hebra nueva.
3. Pero la O⁶-meG sigue en el molde, así que se vuelve a insertar T… y MMR vuelve a cortar. Son **ciclos fútiles de reparación**.
4. Los huecos de ADN monocatenario persistentes se convierten en **DSB** en la siguiente fase S → **apoptosis**.

Consecuencias:

- Un tumor **sin MMR** es **tolerante (resistente) a la temozolomida**: deja la O⁶-meG:T sin tocar, sobrevive y acumula mutaciones C→T.
- 🩺 Los gliomas que recaen tras temozolomida pueden volverse **hipermutados** (firma SBS11), a menudo por mutaciones en **MSH6**.

### 3.4 🩺💊 Ejemplo real: MGMT y la temozolomida en glioblastoma *(Diap. 12)*

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

## 4. Reparación por escisión de bases (BER)

> Para lesiones **pequeñas que no distorsionan la doble hélice** *(Diap. 13)*: bases oxidadas, desaminadas o alquiladas, sitios AP y roturas de cadena sencilla.

### 4.1 Empieza con una ADN-glicosilasa específica *(Diap. 14)*

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

### 4.2 BER paso a paso: parche corto *(Diap. 15)*

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

### 4.3 Parche corto frente a parche largo *(Diap. 16)*

| | **Parche corto (vía predominante)** | **Parche largo** |
|---|---|---|
| Nucleótidos reemplazados | **1** | **2–12** |
| Cuándo | El extremo 5′ puede procesarse (Pol β retira el dRP) | El extremo 5′ está **modificado** y Pol β no puede retirarlo |
| Polimerasa | **Pol β** | **Pol δ/ε** con **PCNA** (desplaza la hebra y forma un **colgajo**) |
| Nucleasa | — | **FEN1** corta el colgajo (*flap*) |
| Ligasa | **XRCC1–LIG3α** | **LIG1** |

### 4.4 PARP1: la "alarma" de las roturas de cadena sencilla *(Diap. 16)*

- **PARP1** detecta la mella y, usando **NAD⁺** como sustrato, sintetiza cadenas de **poli(ADP-ribosa) (PAR)** sobre sí misma y sobre histonas.
- Las cadenas de PAR, cargadas negativamente, **reclutan a XRCC1** (y con él a Pol β y LIG3) para completar la reparación.
- ➕ La **autoPARilación** hace que PARP1 se **suelte** del ADN cuando termina su trabajo.
- 📌 Si PARP1 se inhibe y queda **"atrapada"** en el ADN, la SSB no se repara. Cuando llega la horquilla de replicación, la SSB se convierte en una **rotura de doble cadena**, que solo puede repararse con fidelidad por **recombinación homóloga**. Es la base de los inhibidores de PARP (sección 10.1).

### 4.5 🩺 Ejemplo real: el "sistema GO" y la poliposis asociada a MUTYH *(Diap. 17)*

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

### 4.6 🩺 Ejemplo real: el sistema inmune usa BER (deficiencia de UNG) *(Diap. 18)*

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

## 5. Reparación por escisión de nucleótidos (NER)

> Para lesiones **voluminosas que distorsionan la doble hélice** *(Diap. 19)*.

### 5.1 ¿Qué repara NER? *(Diap. 20)*

| Lesión | Origen | Comentario |
|---|---|---|
| **Dímeros de pirimidina ciclobutano (CPD)** | UV-B | Enlace covalente entre pirimidinas adyacentes (típicamente T–T) que forma un **anillo de ciclobutano**; distorsionan poco |
| **Fotoproductos 6-4** | UV-B | Más distorsionantes que los CPD |
| **Aductos del tabaco** | Benzo[a]pireno diol-epóxido unido a guanina | |
| **Aductos de cisplatino** | Intracatenarios 1,2-d(GpG) | Ver 5.7 |
| **Aductos de aflatoxina B1** | En N7 de guanina | |

📌 **Firma mutacional de la UV**: **transiciones C→T y CC→TT en sitios de dipirimidina**, típicas del **melanoma** y de los **carcinomas cutáneos**.

### 5.2 Dos formas de detectar la lesión: GG-NER y TC-NER *(Diap. 21)*

| | **NER global del genoma (GG-NER)** | **NER acoplada a la transcripción (TC-NER)** |
|---|---|---|
| Dónde actúa | En **todo el genoma**, ambas hebras, se transcriba o no | Solo en la **hebra molde de genes activos** |
| Quién detecta | **XPC–RAD23B** detecta la distorsión; **UV-DDB** (DDB1–DDB2; **DDB2 = XPE**) ayuda a encontrar los **CPD**, que distorsionan poco | La **ARN Pol II detenida** ante la lesión recluta **CSB (ERCC6)**, **CSA (ERCC8)** y **UVSSA** |
| Qué protege sobre todo | Frente a **mutaciones** (cáncer) | La **transcripción** y la supervivencia celular (neuronas, envejecimiento) |
| Enfermedad típica | **Xeroderma pigmentoso** | **Síndrome de Cockayne** |

Las dos subvías **convergen en TFIIH**, y a partir de ahí la vía es común.

### 5.3 NER paso a paso *(Diap. 22)*

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

### 5.4 🩺 Ejemplo real: xeroderma pigmentoso (XP) *(Diap. 23)*

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
| **XPV** (variante) | **POLH** (Pol η) | **No es NER**: síntesis translesión (sección 9) |

➕ **Epidemiología**: XP es rara (del orden de 1 por millón en EE. UU. y Europa) y bastante más frecuente en Japón, donde predomina **XPA**. En EE. UU., Europa y el norte de África predomina **XPC**. La neurodegeneración aparece sobre todo en **XPA** y **XPD** (también en algunos XPB, XPF y XPG). XPC, XPE y XPV no suelen tenerla.

🧠 **ERCC y XP**: *"4-F, 5-G"* van seguidos, como en el alfabeto (ERCC4 = XPF, ERCC5 = XPG). *"2-D y 3-B"* van cruzados (ERCC2 = XPD, ERCC3 = XPB). *"6 y 8 son de Cockayne"* (ERCC6 = CSB, ERCC8 = CSA).

### 5.5 Mismos genes, distintas enfermedades: XP, Cockayne y TTD *(Diap. 24)*

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

### 5.6 🩺💊 Ejemplo real: cisplatino, cuando la reparación es el enemigo *(Diap. 25)*

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

## 6. Reparación de apareamientos erróneos (MMR)

> El corrector de pruebas posreplicativo *(Diap. 26)*.

### 6.1 Tres filtros de fidelidad en la replicación *(Diap. 27)*

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

### 6.2 MMR paso a paso *(Diap. 28)*

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

### 6.3 Inestabilidad de microsatélites (MSI): la huella de un MMR defectuoso *(Diap. 29)*

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

### 6.4 ➕ Cómo leer la inmunohistoquímica de MMR

Las proteínas MMR funcionan en **heterodímeros**, y cada pareja tiene un socio **"obligado"**: **MSH2** estabiliza a MSH6 y **MLH1** estabiliza a PMS2. Si falta el socio obligado, el otro se degrada. El socio "secundario" no es imprescindible para el obligado, porque MSH2 también se une a MSH3 y MLH1 a PMS1 o MLH3.

| Patrón de pérdida en IHQ | Gen sospechoso | Siguiente paso |
|---|---|---|
| **MLH1 + PMS2** | **MLH1** | Estudiar **BRAF V600E** e **hipermetilación del promotor de MLH1**. Si son positivos → tumor **esporádico** (no Lynch). Si son negativos → estudio germinal |
| **MSH2 + MSH6** | **MSH2** o **deleción de EPCAM** | Estudio germinal |
| **Solo MSH6** | **MSH6** | Estudio germinal |
| **Solo PMS2** | **PMS2** | Estudio germinal |

⚠️ **Pérdida de MLH1 no equivale a Lynch.** Alrededor del 15 % de los cánceres colorrectales son MSI-H, pero solo ~3 % son Lynch. La mayor parte del resto son **esporádicos**, por **hipermetilación del promotor de MLH1** (asociada a BRAF V600E, colon derecho y mujeres mayores).

➕ **EPCAM**: es el gen situado justo antes de MSH2. Las deleciones de su extremo 3′ eliminan la señal de terminación, la transcripción "se lee de corrido" hacia MSH2 y **metila (silencia) el promotor de MSH2** en los tejidos que expresan EPCAM (epitelios).

### 6.5 🩺 Ejemplo real: síndrome de Lynch (CCR hereditario no polipósico) *(Diap. 30)*

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

### 6.6 💊 Ejemplo real: MMR deficiente predice respuesta a inmunoterapia *(Diap. 31)*

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

### 6.7 ➕ MMR también "decide" la respuesta a algunos fármacos

MMR no solo corrige errores: también **señaliza** ciertas lesiones para que la célula muera.

| Fármaco | Papel de MMR | Consecuencia de dMMR |
|---|---|---|
| **Temozolomida** | Ciclos fútiles sobre O⁶-meG:T → DSB → apoptosis | **Resistencia** (tolerancia) e hipermutación |
| **6-tioguanina** (tiopurinas) | Reconoce la tioguanina metilada mal apareada | Resistencia |
| **Cisplatino** | Contribuye a señalizar el daño | Resistencia leve |
| **Anti-PD-1** | — | **Sensibilidad** (neoantígenos) |

➕ **Otra causa de hipermutación**: las mutaciones del dominio **exonucleasa de POLE** (o POLD1) anulan la corrección de pruebas de la polimerasa y producen tumores **ultramutados** (cáncer de endometrio y colorrectal). En la línea germinal causan la **poliposis asociada a la corrección de pruebas de la polimerasa** (PPAP), autosómica dominante.

---

## 7. Roturas de doble cadena: NHEJ y HR

> Unión de extremos no homólogos (NHEJ) y recombinación homóloga (HR) *(Diap. 32)*.

### 7.1 Por qué las DSB son las lesiones más peligrosas

En las demás lesiones la hebra complementaria conserva la información. En una DSB **se rompen las dos hebras**: el cromosoma queda partido y no hay molde en la misma molécula. Si los extremos se unen mal aparecen **translocaciones, deleciones o pérdida de un brazo cromosómico**, y si no se reparan, la célula muere.

**Fuentes de DSB** *(Diap. 33)*:
- **Accidentales**: radiación ionizante, horquillas de replicación colapsadas, etopósido (inhibidor de topoisomerasa II).
- **Programadas**: recombinación **V(D)J**, **cambio de isotipo** y **meiosis**.

### 7.2 ¿NHEJ o HR? La fase del ciclo celular decide *(Diap. 33)*

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

➕ BRCA1 y 53BP1 son **antagonistas**. Este antagonismo explica una forma de resistencia a los inhibidores de PARP: si un tumor sin BRCA1 pierde además 53BP1, vuelve a resecar y recupera parte de la HR (sección 10.1).

### 7.3 NHEJ: rápida pero imprecisa *(Diap. 34)*

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

### 7.4 HR: lenta pero fiel *(Diap. 35)*

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

### 7.5 NHEJ frente a HR *(Diap. 36)*

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

### 7.6 🩺 Ejemplo real: SCID por deficiencia de Artemis (NHEJ) *(Diap. 37)*

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

### 7.7 🩺 Ejemplo real: BRCA1 y BRCA2, falla de la recombinación homóloga *(Diap. 38)*

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
- En los tumores con HR deficiente, el platino y los inhibidores de PARP funcionan mejor (sección 10.1).

### 7.8 🩺 Ejemplo real: ataxia-telangiectasia (A-T), cuando falla la señal de alarma *(Diap. 39)*

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

### 7.9 ➕ Otros síndromes de inestabilidad cromosómica que conviene distinguir

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

## 8. Anemia de Fanconi y enlaces cruzados intercatenarios

### 8.1 El problema del ICL

Un **enlace cruzado intercatenario (ICL)** une covalentemente las dos hebras. Ninguna helicasa puede separarlas, así que **bloquea la replicación y la transcripción**. Para repararlo hay que cortar en una hebra, "saltar" el aducto que queda colgando y reparar la rotura que se genera: por eso la vía de Fanconi **integra NER, TLS y HR**.

**Fuentes de ICL**: cisplatino, **mitomicina C**, mostazas nitrogenadas (ciclofosfamida, melfalán), nitrosoureas, psoralenos + UVA y ➕ **aldehídos endógenos** (formaldehído, acetaldehído).

### 8.2 La vía de Fanconi paso a paso *(Diap. 40)*

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

### 8.3 🩺 Clínica de la anemia de Fanconi *(Diap. 40)*

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

## 9. Tolerancia al daño: síntesis translesión (TLS)

> Cuando no hay tiempo para reparar, la célula pasa por encima de la lesión *(Diap. 41)*.

⚠️ La TLS **no repara**: la lesión sigue en el ADN. Lo que hace es **permitir que la replicación continúe** para que la horquilla no colapse, y la lesión se repara después.

### 9.1 El mecanismo *(Diap. 42)*

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

### 9.2 🩺 Xeroderma pigmentoso variante (XPV) *(Diap. 42)*

- **NER normal**, pero mutación en **POLH (Pol η)**.
- Sin Pol η, otras polimerasas "adivinan" frente al dímero → **mutaciones C→T**.
- **Cáncer de piel frecuente**, con **inicio más tardío** y **generalmente sin neurodegeneración**.
- Representa una **fracción importante** de los pacientes con XP (Masutani et al., Nature 1999).

📌 Es la respuesta a la pregunta clásica: *"Un paciente con XP tiene NER normal en el laboratorio. ¿Qué gen sospechas?"* → **POLH**.

➕ En el laboratorio, la síntesis no programada de ADN tras UV (que mide NER) es normal. La pista es una sensibilidad a UV que aumenta con **cafeína**.

---

## 10. Integración: de la biología a la clínica

### 10.1 💊 Letalidad sintética: inhibidores de PARP y tumores BRCA *(Diap. 44)*

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

📌 **¿Por qué las células normales de una portadora de BRCA1 toleran el fármaco?** Porque son **heterocigotas**: conservan un alelo funcional y hacen HR. Solo las células tumorales perdieron el segundo alelo (sección 1.5).

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

### 10.2 ➕ Firmas mutacionales: la lesión deja una huella *(Diap. 48, mensaje 4)*

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

### 10.3 💊 Los fármacos que dañan el ADN y la vía que decide la respuesta

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

### 10.4 📌 Resumen maestro: vía, lesión, enfermedad y aplicación clínica *(Diap. 45, ampliada)*

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

### 10.5 ➕ Tabla rápida de enfermedades para diagnóstico diferencial

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

### 10.6 Mensajes para llevar *(Diap. 48)*

1. El ADN sufre **decenas de miles de lesiones por célula al día**; la reparación es **constante, no excepcional**.
2. **Cada tipo de lesión tiene su vía**: pequeña → BER; voluminosa → NER; error de copia → MMR; rotura doble → NHEJ o HR.
3. Los **defectos hereditarios de reparación** causan **cáncer, inmunodeficiencia, neurodegeneración o envejecimiento prematuro**.
4. La **firma mutacional** del tumor puede revelar qué vía falló (MUTYH, MMR, UV, tabaco).
5. La **reparación del tumor determina la respuesta al tratamiento**: temozolomida, cisplatino, PARP e inmunoterapia.

---

## 11. Casos clínicos resueltos

> *(Diap. 46)* Para cada caso: ¿qué vía está alterada? ¿qué gen sospechas? ¿qué implica para el tratamiento y para la familia? Intenta responder antes de abrir la solución.

### Caso 1
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

### Caso 2
**Hombre de 42 años con adenocarcinoma de colon derecho. Su padre tuvo cáncer de colon a los 48 y una tía, de endometrio. La IHQ muestra pérdida de MSH2 y MSH6.**

<details>
<summary>Ver solución</summary>

- **Diagnóstico**: **síndrome de Lynch**. Cumple Ámsterdam II ("3-2-1"): 3 familiares con cánceres del espectro Lynch (colon, colon, endometrio), 2 generaciones y al menos uno antes de los 50.
- **Vía**: **MMR**.
- **Gen**: **MSH2** o una **deleción de EPCAM** que silencia MSH2. MSH6 se pierde porque **MSH2 es su socio obligado**: sin MSH2, MSH6 es inestable y se degrada. Se confirma con **estudio germinal**.
- **Tratamiento del paciente**: el tumor es dMMR/MSI-H. Si hay enfermedad metastásica, el **anti-PD-1 (pembrolizumab)** en primera línea es superior a la quimioterapia (KEYNOTE-177). Por el riesgo de cáncer metacrónico se puede valorar una colectomía más extensa. Después, colonoscopia cada 1–2 años, cribado de otros tumores del espectro y valorar aspirina.
- **Familia**: herencia **autosómica dominante**. Cada hijo y cada hermano tiene un **50 %** de riesgo. Se hace **estudio en cascada** de la variante. Los portadores inician colonoscopia cada 1–2 años desde los 20–25 años, y las mujeres portadoras valoran histerectomía y salpingooforectomía al terminar la paridad.
</details>

### Caso 3
**Mujer de 35 años con cáncer de mama triple negativo. Su madre murió de cáncer de ovario a los 50 años.**

<details>
<summary>Ver solución</summary>

- **Diagnóstico**: sospecha de **síndrome de cáncer de mama y ovario hereditario**.
- **Vía**: **recombinación homóloga**.
- **Gen**: **BRCA1** es el más probable. El cáncer de mama **triple negativo** precoz es típico de BRCA1, y el riesgo de ovario es mucho mayor con BRCA1 (44 %) que con BRCA2 (17 %). Se hace un **panel germinal** (BRCA1, BRCA2, PALB2, RAD51C/D…).
- **Tratamiento**: el tumor HR deficiente es **sensible al platino** y a los **inhibidores de PARP** (olaparib en enfermedad metastásica; olaparib adyuvante en enfermedad precoz de alto riesgo). Hay que valorar **mastectomía bilateral reductora de riesgo** y **salpingooforectomía** reductora de riesgo (en BRCA1 hacia los 35–40 años, tras completar la paridad).
- **Familia**: herencia **autosómica dominante** (50 % para cada familiar de primer grado). Los varones portadores también tienen riesgo de cáncer de **próstata, páncreas y mama masculino** (sobre todo con BRCA2). Se ofrece estudio en cascada; las portadoras inician vigilancia con resonancia magnética mamaria.
</details>

### Caso 4
**Niño de 4 años con marcha inestable progresiva, vasos dilatados en las conjuntivas, sinusitis y neumonías recurrentes. Alfafetoproteína elevada.**

<details>
<summary>Ver solución</summary>

- **Diagnóstico**: **ataxia-telangiectasia**. Reúne la tétrada: ataxia cerebelosa progresiva, telangiectasias conjuntivales, infecciones sinopulmonares por inmunodeficiencia y **AFP elevada**.
- **Vía**: **señalización de la respuesta al daño** de las DSB.
- **Gen**: **ATM** (autosómico recesivo).
- **Tratamiento**: **evitar la radiación ionizante** innecesaria (radiografías, TC) por la radiosensibilidad extrema. Si aparece un cáncer (riesgo ~25 %, sobre todo linfomas y leucemias), hay que **reducir la radioterapia y los fármacos radiomiméticos**. Manejo de la inmunodeficiencia (inmunoglobulinas si hay déficit de anticuerpos, vacunas, tratamiento precoz de infecciones), rehabilitación y vigilancia pulmonar y oncológica.
- **Familia**: los padres son portadores (25 % de recurrencia en cada embarazo). Las **mujeres portadoras heterocigotas** tienen un riesgo de cáncer de mama aproximadamente doble, por lo que merecen vigilancia.
</details>

### ➕ Casos adicionales

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

## 12. Preguntas de repaso resueltas y autoevaluación

### 12.1 Las preguntas de la clase *(Diap. 47)*

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

### 12.2 ➕ Autoevaluación adicional

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

## 13. Trampas de examen

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

## 14. Mnemotecnias

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

## 15. Glosario

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

## 16. Plan de estudio y cómo usar el mazo de Anki

### 16.1 Plan sugerido (5 sesiones)

| Sesión | Contenido | Tarjetas nuevas |
|---|---|---|
| 1 | Secciones 1–2 (prerrequisitos, daño, DDR, mapa) | Subdecks 00–01 |
| 2 | Secciones 3–4 (reversión directa y BER) | Subdecks 02–03 |
| 3 | Sección 5 (NER, XP, Cockayne, TTD, cisplatino) | Subdeck 04 |
| 4 | Secciones 6–7 (MMR, Lynch, inmunoterapia, DSB, BRCA, A-T) | Subdecks 05–06 |
| 5 | Secciones 8–10 y casos (Fanconi, TLS, integración) | Subdecks 07–10 |

Lee la sección **antes** de estudiar sus tarjetas nuevas: Anki sirve para **retener**, no para aprender por primera vez.

### 16.2 El mazo `Reparacion_ADN.apkg`

**Dónde está**: en la carpeta principal, [`genetica-biologia-molecular/Reparacion_ADN.apkg`](../Reparacion_ADN.apkg).

**Importar**: en Anki de escritorio, *Archivo → Importar* y elige el `.apkg` (o ábrelo con doble clic). En AnkiDroid y AnkiMobile, abre el archivo desde la app.

**Estructura**: un mazo principal, **"Reparación del ADN (Medicina)"**, con subdecks numerados que siguen esta guía:

```
Reparación del ADN (Medicina)
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
- **Nuevas por día: 20–30.** El mazo tiene 366 tarjetas: a 25 por día terminas las nuevas en unos 15 días. Si tienes examen pronto, sube a 40–50.
- Activa **"Enterrar tarjetas hermanas"** (nuevas y de repaso), para no ver juntos los huecos de un mismo cloze.
- Orden de nuevas: **"Mazo"**, para respetar el orden pedagógico (fundamentos → vías → clínica).
- No borres tarjetas que te parezcan fáciles: déjalas, y Anki las espaciará solo.

---

## 17. Bibliografía

### De la clase *(Diap. 49–50)*

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

### ➕ Referencias de las ampliaciones
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
