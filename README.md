*Adatok analizációja és adatbányászat*  

*Python nyelven* 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.001.png)

*Szabó Ákos Dániel* 

GEIAL526-ML Adatelemzési és adatbányászati módszerek tárgyból 

Beadandó  II.  

Szabó Ákos Dániel DLKN1D  Mérnök informatikus MSc levelező  2023/2024/1 

Tartalomjegyzék 

[Feladat specifikáció ....................................................................................................................................... 3 ](#_page2_x69.00_y72.00)[Használt technológiák, adatkészletek bemutatása....................................................................................... 4 ](#_page3_x69.00_y72.00)[Adatkészlet................................................................................................................................................ 4 ](#_page3_x69.00_y116.00)[Python ....................................................................................................................................................... 5 ](#_page4_x69.00_y72.00)[Könyvtárak és csomagok:...................................................................................................................... 5 ](#_page4_x69.00_y206.00)[Adatkészlet beolvasás és tisztítás ................................................................................................................. 6 ](#_page5_x69.00_y72.00)[Tisztítás ..................................................................................................................................................... 6 ](#_page5_x69.00_y165.00)[Adatok elemzése ........................................................................................................................................... 7 ](#_page6_x69.00_y72.00)[Hisztogrammok ......................................................................................................................................... 9 ](#_page8_x69.00_y72.00)[Korrelációs Mátrix ....................................................................................................................................... 13 ](#_page12_x69.00_y72.00)[Döntési Fa ................................................................................................................................................... 15 ](#_page14_x69.00_y72.00)[Adatok felosztása .................................................................................................................................... 15 ](#_page14_x69.00_y94.00)[Tanítás ..................................................................................................................................................... 16 ](#_page15_x69.00_y95.00)[Megjelenítés ........................................................................................................................................... 17 ](#_page16_x69.00_y72.00)[Gyökér (Root) node ............................................................................................................................. 17 ](#_page16_x69.00_y476.00)[Elágazás a bal ágon (feature_4 <= 14.91) ........................................................................................... 17 ](#_page16_x69.00_y571.00)[Elágazás a jobb ágon (feature_4 > 14.91) ........................................................................................... 17 ](#_page16_x69.00_y658.00)[További elágazások ............................................................................................................................. 18 ](#_page17_x69.00_y95.00)[Confusion Matrix......................................................................................................................................... 19 ](#_page18_x69.00_y72.00)

<a name="_page2_x69.00_y72.00"></a>Feladat specifikáció 

**Adatelemzés és adatbányászati módszerek** 

**2. féléves feladat** 

Válasszon ki egy adathalmazt (kaggle.com, seaborn adatcsomag, saját adatok) (kivéve iris.csv) és 

végezze el az adatok elemzését Python-ban az alábbi módszertant alkalmazva. 

1. Töltse be az adatokat és végezze el a szükséges adattisztítási lépéseket. 
1. Elemezze az adathalmazt leíró statisztikai mutatókkal, grafikonokkal. Szűrje ki a kiugró értékeket. 
1. Keresse meg a változók között fennálló korrelációs viszonyokat. 
1. Klaszterezze az adatokat egy kiválasztott algoritmussal, vagy készítsen osztályozó modellt az adathalmazhoz egy kiválasztott módszerrel és mutassa meg a modell pontosságát. 

Az elemzésről készítsen pdf dokumentumot, amely tartalmazza: az adathalmaz forrását és leírását, 

az alkalmazott eljárások rövid ismertetését, a futási eredményeket és az eredmények kiértékelését. A 

feladathoz csatolni kell a Python kódot is magyarázattal ellátva (kommentezve). **Leadási határidő: 2023. december 8.** 

A feladat leadása az aláírás megszerzésének a feltétele. 

Feladat leadás módja: MS Teams feladatkiíráshoz feltölteni

<a name="_page3_x69.00_y72.00"></a>Használt technológiák, adatkészletek bemutatása 

<a name="_page3_x69.00_y116.00"></a>Adatkészlet 

Kaggle oldalon választottam a feladat specifikációban ismertetett forrásból ezt az adatkészletet: [Drug Classification (kaggle.com) ](https://www.kaggle.com/datasets/prathamtripathi/drug-classification/data)

Ezeket  az  adatokat  egy  gyógyszergyártó  cégtől  gyűjtötték,  amely  címkézte  a  gyógyszerek adatkészletét és az azt befolyásoló paramétereket. Ezért a betegség és a beteg típusa alapján meglehet határozni milyen gyógyszer ajánlott. 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.002.jpeg)

1. *Figure Adathalmaz* 

<a name="_page4_x69.00_y72.00"></a>Python 

Python egy magasszintű, interpretált programozási nyelv. Széles körben használják adatelemzés, mesterséges intelligencia, webfejlesztés és hardverprogramozás területén. Az egyszerűsége és könnyen érthetősége miatt ideális választás kezdők számára. Számos külső könyvtár érhető el, ami további funkcionalitást biztosít. 

<a name="_page4_x69.00_y206.00"></a>Könyvtárak és csomagok: 

*pandas:* 

Felhasználása: Adatok importálására, tisztítására, feldolgozására és statisztikai műveletek végrehajtására szolgál. 

Példa alkalmazás: A beadandó feladatban az adatkészlet beolvasására és tisztítására használtam. 

*seaborn:* 

Felhasználása: Statisztikai grafikonok készítésére alkalmas. 

Példa alkalmazás: A beadandó feladatban ezzel a csomaggal készítettem grafikonokat az adatkészletből. 

*scikit-learn:* 

Felhasználása: Gépi tanulási algoritmusok implementálására használható, például regresszió, csoportosítás stb. 

Példa alkalmazás: A beadandó feladatban ezt a csomagot alkalmaztam korrelációs elemzésre és kiugró értékek azonosítására az adatkészletben. 

<a name="_page5_x69.00_y72.00"></a>Adatkészlet beolvasás és tisztítás 

A használt könyvtárcsomagok bemutatásánál ismertettem a pandas csomagot, amivel beolvastam az általam használt adatkészletet.  Mivel konstans az adatkészlet, és egy szinten van a python forráskóddal, így beégetve megadtam a .CSV fájl nevét és elmentettem egy *data* változóba.  

<a name="_page5_x69.00_y165.00"></a>Tisztítás 

Az eredeti dokumentum nem tartalmazott hibákat ezért az adattisztítás bemutatása érdekében én generáltam bele plusz hibákat a fájlba. 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.003.png)

2. *Figure DirtyData* 

A korral és Koleszterollal lehet kezdeni valamit ha hiányzik vagy kiugró az adat  akkor a mediánnal pótlom. Viszont a többi adat kritkus és éppen ha valamelyik ezek közül hiányzik akkor az adatsort eltávolítom. 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.004.png)

3. *Figure Kód részlet adattisztítás* 

<a name="_page6_x69.00_y72.00"></a>Adatok elemzése 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.005.jpeg)

4. *Figure Doboz diagramm* 

A kód egy dobozdiagramot, más néven boxplotot, hoz létre két numerikus változó, azaz 'Age' és 'Na\_to\_K' oszlopok alapján. A dobozdiagramot gyakran használják a statisztikai adatok szemléltetésére, különösen az adatok eloszlásának és kiugró értékek azonosítására. 

A dobozdiagramnak két fő része van: a dobozok és az esetleges kiugró értékek. A dobozok a változók interkvartilis tartományát (Q1 és Q3 közötti területet) mutatják, míg a középső vonal a mediánt reprezentálja. Az esetleges kiugró értékek (outlierek) azok az értékek, amelyek messzebb vannak a dobozoktól, és lehetnek fontosak az adathalmaz eloszlásának megértése szempontjából. Az ábra színekkel és egyéb vizuális elemekkel segíti a könnyebb értelmezést. 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.006.jpeg)

5. *Figure Kor gyakoriság* 

A kód egy hisztogramot is készít az 'Age' (kor) oszlop alapján, és aztán megjeleníti azt. A hisztogram egy olyan diagram, amely bemutatja az értékek gyakoriságát különböző intervallumokban. 

Ez a hisztogram segít megérteni az 'Age' oszlop eloszlását, vagyis hogy az életkorok hogyan vannak elosztva az adathalmazban. Az x tengelyen az életkor intervallumok vannak, míg az y tengelyen a gyakoriság (az adott intervallumban található értékek száma). A hisztogram segíthet az életkorok eloszlásának és eloszlásának vizuális értelmezésében. 

<a name="_page8_x69.00_y72.00"></a>Hisztogrammok 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.007.jpeg)

6. *Figure Kor Hisztogram* 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.008.jpeg)

7. *Figure Nem Hisztogram* 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.009.jpeg)

8. *Figure Vérnyomás Hisztogram* 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.010.jpeg)

9. *Figure Koleszterol Hisztogram* 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.011.jpeg)

10. *Figure Na to K Hisztogram* 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.012.jpeg)

11. *Figure Gyógyszer Hisztogram* 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.013.jpeg)

12. *Figure Gyakoriság* 

A hisztogramok hasznosak lehetnek az adathalmaz jellemzéséhez és annak megértéséhez, hogy az attribútumok milyen értéktartományban és eloszlásban vannak. Ezen információk segíthetnek a modellalkotás során az attribútumok kezelésében és az esetleges további adatfeldolgozási lépések kiválasztásában. 

<a name="_page12_x69.00_y72.00"></a>Korrelációs Mátrix 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.014.jpeg)

13. *Figure Correlation Matrix* 

A korreláció egy statisztikai mutató, amely azt méri, hogy két változó milyen mértékben mozog együtt. A korrelációs mátrix egy táblázat, amely megmutatja a változók közötti lineáris kapcsolatokat, vagyis hogy milyen erős és irányú az egyik változó változása a másikkal összefüggésben. 

A korrelációs mátrixban található értékek közül a leggyakrabban használt a Pearson-korreláció, amely -1 és 1 közötti értékeket vehet fel: 

- Ha egy érték 1-hez közelít, az azt jelenti, hogy két változó között erős pozitív lineáris kapcsolat van: amikor az egyik változó nő, a másik is nő. 
- Ha egy érték -1-hez közelít, akkor erős negatív lineáris kapcsolat áll fenn: amikor az egyik változó nő, a másik csökken. 
- Ha az érték közel van 0-hoz, az azt jelenti, hogy nincs vagy csak gyenge lineáris kapcsolat a változók között. 

A fenti példában a következőket láthatod a mátrixban: 

- 'Age' és 'Sex' közötti korreláció 0.142803, ami egy gyenge pozitív kapcsolatot jelent. 
- 'Na\_to\_K' és 'Drug' közötti korreláció -0.695237, ami egy erős negatív kapcsolatot jelent. Ez azt mondja nekünk, hogy minél magasabb a nátrium-kálium arány, annál kisebb az esélye annak, hogy egy adott gyógyszert felírjanak. 
- Ez azt mutatja, hogy van valamiféle összefüggés a vérnyomás ('Blood Pressure') és a gyógyszerválasztás ('Drug') között. A pozitív korreláció azt sugallja, hogy általában magasabb vérnyomás esetén bizonyos típusú gyógyszerek gyakrabban előfordulhatnak, vagy fordítva 

Ez a mátrix segít abban, hogy lássuk, milyen irányban és milyen erősségben követik egymást a változók, ami hasznos lehet az adatok megértése és a további elemzések tervezése szempontjából. 

<a name="_page14_x69.00_y72.00"></a>Döntési Fa 

<a name="_page14_x69.00_y94.00"></a>Adatok felosztása 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.015.png)

14. *Figure Adatok felosztása* 

Ez a kód a dataset-et (adathalmazt) két részre osztja: tanító (training) és tesztelő (testing) részekre. A `train\_test\_split` függvényt a Scikit-Learn könyvtár `model\_selection` moduljából importáljuk. Ez a módszer hasznos azért, hogy a gépi tanulási modellek teljesítményét értékeljük. 

A paraméterek rövid magyarázata: 

- `X`: A független változókat tartalmazó mátrix (input features). 
- `y`: A célváltozót tartalmazó vektor (target variable). 
- `test\_size`: A tesztelő halmaz mérete a teljes adathalmazhoz viszonyítva. Ebben az esetben a 0.3 azt jelenti, hogy a tesztelő halmaz 30% -át teszi ki az összes adatnak, és a tanító halmaz 70% -át. 
- `random\_state`: A véletlenszám-generátor kezdőértéke. Ezt azért használjuk, hogy a program minden futtatáskor ugyanazokat az adatokat válassza ki a tesztelő és tanító halmazokból. Ez segít reprodukálható eredmények elérésében. 

A függvény visszatérési értékei négy részlet: 

- `X\_train`: A tanító halmaz független változói. 
- `X\_test`: A tesztelő halmaz független változói. 
- `y\_train`: A tanító halmaz célváltozói. 
- `y\_test`: A tesztelő halmaz célváltozói. 

Ezután a `DecisionTreeClassifier` vagy más gépi tanulási algoritmusok segítségével megtanítjuk a modellet (`mod\_dt`), majd teszteljük a modellt a tesztelő halmazon, és kiértékeljük a teljesítményét. A tesztelés során a modeltől függően a kimeneteket (például a predikciókat) összehasonlítjuk a valóságos célváltozókkal (tesztelő halmaz).  

<a name="_page15_x69.00_y95.00"></a>Tanítás 

A döntési fa tanítása során a cél az, hogy a modell megtanulja az adathalmaz mintáit és azokat a címkékhez rendelje. Az alábbiakban részletezem a döntési fa tanításának lépéseit a kódban: 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.016.png)

15. *Figure Tanítás* 

**Modell létrehozása:** A DecisionTreeClassifier osztályból létrehozok egy döntési fa modellt. Ez az osztály az alapvető döntési fa algoritmust implementálja. 

**Modell tanítása:** A fit metódust használom a modell tanítására. A fit függvény két fő bemenettel rendelkezik: 

- X\_train: A tanító adathalmaz, amely az attribútumokat tartalmazza. 
- y\_train: A tanító adathalmaz címkéit tartalmazó vektor. 

Ezután a modell tanulni fogja az adathalmaz mintáit és azok címkéit. A döntési fa a be- és kimeneti változók közötti összefüggéseket fogja megtanulni, és egy fastruktúrát fog kialakítani, amely az attribútumok alapján vezet az osztálycímkékhez. 

A tanítás után a modell készen áll az előrejelzésekre, és a tesztadathalmazon történő alkalmazáshoz a predict metódust használhatod. 

Ez a kód az előrejelzéseket hozza létre a tesztadathalmazon, és azokat a prediction változóban tárolja. 

A tanítás utáni fázisban érdemes kiértékelni a modell teljesítményét, például a pontosságát, ami a következőképpen történik: 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.017.png)

16. *Figure Accury calculation* 

Az én esetemben a pontosság:  

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.018.png)

17. *Figure Accuracy* 

<a name="_page16_x69.00_y72.00"></a>Megjelenítés 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.019.jpeg)

18. *Figure Tree* 

A döntési fa egy fátérkép struktúrájú modellezési technika, ahol a gyökér (root) node-nál kezdve minden node egy jellemző értékét vizsgálja, majd a vizsgálat eredményének függvényében az ágakon továbbhalad. A levélcsomópontok tartalmazzák az osztályokat vagy a predikciókat. A fák célja a bemeneti adatok szegmentálása olyan részekre, ahol könnyen kezelhetőek, és kategorikus kimenetek (osztályok) biztosíthatók. 

A megadott döntési fa szekvenciálisan vizsgálja a jellemzőket, és döntéseket hoz az egyes lépésekben. Az alábbiakban részletezem a kódban szereplő fátérképet: 

<a name="_page16_x69.00_y476.00"></a>Gyökér (Root) node 

- A gyökér node az `feature\_4`-et vizsgálja, kisebb-e vagy egyenlő 14.91-gyel. 
- Ha igen, az adott példányt az `0` osztályhoz rendeli, és a fa jobb ágára lép. 
- Ha nem, a bal ágra lép, ahol további döntéseket hoz. 

<a name="_page16_x69.00_y571.00"></a>Elágazás a bal ágon (feature\_4 <= 14.91) 

- Az elágazások között a `feature\_2`, majd az `feature\_0` és `feature\_4` következnek. 
- Ha a feltételek teljesülnek, a példányt az `1` osztályhoz rendeli. 
- Ellenkező esetben az `2` osztályba kerül. 

<a name="_page16_x69.00_y658.00"></a>Elágazás a jobb ágon (feature\_4 > 14.91) 

- Itt a példányt az `0` osztályhoz rendeli. 

<a name="_page17_x69.00_y95.00"></a>További elágazások 

- Az feature\_2 értéke szerint további elágazások következnek. 
- Például, ha feature\_2 kisebb vagy egyenlő 0.50-gyel, akkor az feature\_3 értékét vizsgálja. 
- A különböző feltételek és a levélcsomópontok tartalmazzák az osztályokat. 

Ez a fa tükrözi a gépi tanulási modell gondolkodását. A fa egyes ágai és levélcsomópontjai alapján a modell döntéseket hoz az adatpontok osztályozása során. Ezáltal könnyen értelmezhető, és a fa struktúrájának elemzésével jobban megérthető, hogyan hoz döntéseket a modell az adott jellemzők alapján. 

<a name="_page18_x69.00_y72.00"></a>Confusion Matrix 

![](Aspose.Words.ca7f979b-7cdd-4c24-882a-a192e4c5d22a.020.jpeg)

19. *Figure Confusion Matrix* 

A kapott confusion matrix (zavarási mátrix) egy olyan táblázat, amely bemutatja a gépi tanulási modell teljesítményét az osztályozási feladatban. A mátrix fő átlós elemei azok az értékek, amelyek a modell által helyesen vagy helytelenül osztályozott példányok számát mutatják meg az egyes osztályokban. Az oszlopok általában a modell által tett előrejelzéseket, míg a sorok a valóságban lévő osztályokat jelentik. 

Ahol a sorok a valós osztályokat, az oszlopok pedig a modell által tett előrejelzéseket jelképezik. Néhány kulcsfontosságú információ a mátrixból: 

A [0, 0] elem (34): 34 példányt helyesen osztályozott a modell az első osztályba ('drugX'). 

A [1, 1] elem (5): 5 példányt helyesen osztályozott a modell a második osztályba ('DrugY'). A [2, 2] elem (3): 3 példányt helyesen osztályozott a modell a harmadik osztályba ('drugC'). A [3, 3] elem (5): 5 példányt helyesen osztályozott a modell a negyedik osztályba ('drugA'). A [4, 4] elem (14): 14 példányt helyesen osztályozott a modell az ötödik osztályba ('drugB'). 

Az átló felett és alatt található értékek (0) azt mutatják, hogy a modell nem tett helytelen előrejelzéseket azokban az osztályokban, ahol valóban nem voltak példányok. 

A modell teljes pontosságát a diagonális elemek (az átló) összege adja meg az összes példányból. Az esetek egyesítése azonban további fontos információkat nyújthat a modell teljesítményéről, különösen akkor, ha az osztályok egyenetlenül vannak elosztva. 

A confusion matrix harmadik sorának második eleme (2. oszlopban) a [2, 1] cella tartalma mutatja, hogy a modell egy példányt helytelenül osztályozott. Tehát a harmadik osztályban ('drugC') lévő példányok közül egyet rosszul prediktált, azt hiszi, hogy a második osztályba ('DrugY') tartozik. 
20 

