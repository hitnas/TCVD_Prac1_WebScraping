# TCVD_Prac1_WebScraping

Projecte de web scraping de la pàgina de [Bolsa de Madrid](http://www.bolsamadrid.es/esp/aspx/Portada/Portada.aspx) per descarregar dades diàries de l'Índex de referència dels valors més cotitzats (IBEX-35) com a Pràctica 1 de l'assignatura Tipologia i cicle de vida de les dades del Màster en Ciència de Dades de la UOC (semestre març-abril 2018). 

En aquest espai es pot trobar: 
- README.md --> Arxiu que esteu llegint.  
- /csv  --> Carpeta amb els datasets. Atès que és un arxiu que es genera per un dia, s'hi troben diversos arxius dels dies en què s'ha executat el codi. 
- /pdf --> Carpeta on es troba l'arxiu explicatiu amb les caracterstiques del *dataset*.
- /src --> Codi amb *Python* utilitzat per a la descàrrega i la generació dels arxius de dades. 

Com a introducció i avançament, el codi està pensat per executar-lo una vegada al dia, iniciant-lo de manera manual abans del començament de la sessió al mercat continu. Un cop iniciat el programa consulta la pàgina amb la informació dels valors al mercat continu cada minut. Abans de l'inici de la sessió es desa una vegada el registre del tancament del mercat el dia anterior. Un cop iniciat el mercat, es va desant cada minut la informació del valor de referència (IBEX 35) i de cadascun dels 35 valors que formen part d'aquest índex. Quan es tanca el mercat, es desa una vegada la informació amb els valors en el moment del tancament i la segona vegada que s'accedeix després del tancament s'atura l'execució. 

En cada accés es creen els registres als Datasets amb el *nom* de l'empresa (o de l'IBEX 35), el *valor* en euros, el *% de diferència* respecte l'inici d'aquella sessió, els valors *màxim* i *mínim* que les accions d'aquella empresa han tingut aquell dia fins aquell moment, el *volum* d'accions que s'han transferit i l'import *efectiu en milers d'euros* d'aquelles transaccions i la *data* i *hora* de les dades (hora de les dades del mercat continu, no de la recollida en el dataset).  

----
**Autor**: Santiago Herrero Blanco 
[sherrerobl@uoc.edu](mailto:sherrerobl@uoc.edu)
