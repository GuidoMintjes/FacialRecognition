# FacialRecognition
Een simpel facial recognition programma gemaakt met python en de facial_recognition library.

<h1>Instructies Voor Gebruik</b>

<h2>Benodigdheden vooraf:</h2>
	<ul>
		<li>Python 3, te krijgen op https://www.python.org/downloads/</li>
		<li>Pip, de python package manager, zit vaak al bij de python installatie in, dit is te checken door `pip` te doen in command prompt, als er niks verschijnt, dan kan je pip halen op https://pip.pypa.io/en/stable/installing/ </li>
		<li>Een lege folder om de bestanden in kwijt te kunnen, noem hem 'FacialRec' of iets dergelijks</li>
		<li>Een programma om git repositories mee te clonen, dit kan de CLI tool zijn: https://github.com/cli/cli/releases/tag/v1.3.0 , of de desktop applicatie: https://desktop.github.com/ </li>
	<li>Een github-account, afhangend van de download-methode</li>
	<li>Een laptop met camera, hierop doe je alle stappen (liefst op windows)</li>
	</ul>
	
<h2>Voorbereiding vooraf:</h2>
<p>Zorg dat je een aantal foto's maakt waatbij je gezicht duidelijk te zien is, hiermee wordt bedoeld, foto's waarbij het gezicht duidelijk te zien is en ook het enige is dat eigenlijk te zien is<p>
<p>Een aantal van minimaal <b>5 foto's</b> is meestal ideaal, maak er een recht naar voren kijkend, een een klein beetje naar links, een beetje naar rechts, een beetje naar boven en een een beetje naar onder<p>
<p><b><u>Zorg dat je deze foto's ergens terug kunt vinden!</u></b></p>

<h2>Repository clonen:</h2>
<p>Om succesvol de bestanden te bemachtigen, kan je een aantal dingen doen:</p>

* Op github.com/GuidoMintjes/FacialRecognition (overigens waar je nu bent) kan je klikken op het groene knopje met code: ![Code Knop](https://i.imgur.com/WdN4pUI.png)

* Dan kan je het of als zip bestand downloaden, als je dit doet zorg dan dat je het volledige zip bestand uitpakt in de werkmap die je hebt aangemaakt
* Of je opent hem in GitHub Desktop, zorg dan dat je deze goed hebt ingesteld en dat je eerst bent ingelogd! Als je er niet uitkomt, zijn er [hier](https://docs.github.com/en/free-pro-team@latest/desktop/contributing-and-collaborating-using-github-desktop/cloning-a-repository-from-github-to-github-desktop) instructies te vinden
* En anders gebruik je de CLI, ook te vinden in het code menu, instructies zijn [hier](https://cli.github.com/manual/gh_repo_clone) te vinden

<h2>Het gebruik</h2>
<p>Als het goed is heb je nu alle bestanden in je werkmap, open je werkmap nu in de bestandenverkenner</p>
1. <b>Belangrijke stap!</b> Maak in je werkmap nu een map aan met de naam 'KNOWN_FACES', deze map mag niet anders heten!!!  
2. Ga naar deze zojuist gemaakte map toe, en maak daarin een nieuwe map met de naam van de persoon waarvan je de foto's hebt gemaakt, bijvoorbeeld 'Jantje', het maakt niet uit hoe deze map heet, je kan dus ook meerdere mappen van meerdere personen maken!  
3. Plak in elke map die je hebt van een persoon zijn/haar foto's  
4. Ga met de bestandenverkenner nu weer een map omhoog, naar de 'FacialRecognition' map  
5. Open command prompt en navigeer naar deze werkmap, of open de command prompt door in de zoekbalk in de verkenner 'cmd' in te typen, en op enter te drukken  
6. <b>Erg belangrijk!</b> Hiermee installeer je de benodigde packages met de pip module: `pip install -r requirements.txt`  
7. Om de AI te trainen op de foto's, voer je de volgende code in in deze command prompt: `python savefaces.py`  
8. Wanneer dit klaar is, voer dan `python frec.py` in, en laat het herkennen maar beginnen!  
9. Nadat je klaar bent met herkennen, klik je met je muis op het camera-venster en klikt op de volgende toets combinatie: `left-shift+q`  
10. Er is automatisch een video bestand gemaakt genaamd `video_capture.avi`, in dit bestand wordt automatisch doorgespoeld wanneer er niet herkend wordt, deze wordt elke keer herschreven, dus als je hem op wilt slaan, geef hem dan een andere naam of sla hem ergens op  

<h2>Eind</h2>
Ik hoop dat dit programma goed werkt!

<b>Dit programma mag niet hergebruikt worden zonder schriftelijke toestemming van de oorspronkelijke auteur, de rechten voor de gebruikte packages zijn voorbehouden aan hun rechtmatige eigenaren!</b>
