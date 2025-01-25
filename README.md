# Sommaire

1. [Présentation](#présentation)  
2. [À faire](#à-faire)  
3. [Se connecter à la VM MiNET en SSH](#se-connecter-à-la-vm-minet-en-ssh)  
4. [Hébergement du site sur la VM](#hébergement-du-site-sur-la-vm)  
5. [Ajouter le navbar et le footer](#ajouter-le-navbar-et-le-footer)  
6. [Ajouter les balises Google Analytics](#ajouter-les-balises-google-analytics)  
7. [Template pour une nouvelle page](#template-pour-une-nouvelle-page)
8. [Structure du site](#structure-du-site)
9. [Crédit](#crédit)

# Présentation 
Ceci est le dépôt Git du **site du BDA de Télécom SudParis et IMT-BS**, développé par le mandat **Artefact 2024-2025**.

Le site est accessible à l'adresse : [bda-imtbs-tsp.fr](http://bda-imtbs-tsp.fr).

Ce site a été développé en **HTML, CSS et JavaScript**, sans framework particulier. Il inclut :  
- Une **page principale** avec une section actualités, qui contient les actualités du BDA et de ses clubs.  
- Une **page présentation du BDA** qui offre une description générale de l'association.  
- Une **page équipe** qui présente le mandat actuel.  
- Une **page clubs**, qui donne un aperçu de tous les clubs du BDA, avec une sous-page par club contenant :
  - Une description,  
  - Un organigramme,  
  - Des photos d'événements,  
  - Une phrase du président du club,  
  - Les contacts et réseaux sociaux.  
- Une **page événements** présentant les événements organisés par le BDA, avec une sous-page par événement (en cours de réalisation).  
- Une **page cotiser**, avec les informations nécessaires pour adhérer, les prix et un lien vers HelloAsso pour effectuer le paiement.  
- Une **page jouer !** incluant un jeu développé par le CELL (merci à Valentin Lantigny) pour l'intronisation.  
- Une **page partenariats**, expliquant comment devenir partenaire et affichant les logos des partenaires actuels.  
- Une **page nous contacter**, contenant un formulaire de contact en PHP.  
  ⚠️ **Attention** : le formulaire de contact ne fonctionne pas pour l’instant. Il devra être corrigé ultérieurement.

### À faire
- Réparer le formulaire de contact sur la page "Nous contacter".  
- Ajouter un calendrier hebdomadaire des activités des clubs.  
- Intégrer une API Google Sheets pour automatiser les mises à jour des actualités sans avoir à modifier le site manuellement chaque semaine.  
- Compléter les pages dédiées aux événements.  
- Ajouter une page "Dons" pour permettre aux utilisateurs de contribuer financièrement au BDA.  
- Créer un jeu "Quel Artefact es-tu ?", prévu pendant la campagne.

# Se Connecter à la vm MiNET en SSH 
### 1. Vérifier si vous avez déjà une clé publique: 

vérifier s'il existe un fichier du type ```id_rsa.pub``` (comme id_ed24419.pub) dans ```~/.ssh```: 

  a) si tel est le cas, copier la clé public :
  ````
  cat ~/.ssh/id_rsa.pub
  ````
 en remplaçant rsa par l'id de votre clé publique (dans l'exemple c'est ed24419)
 
  b) si ce n'est pas le cas, générer votre clé public
  ````
  ssh-keygen -t rsa -b 4096 -C "votre_email@example.com"
  ````
 en remplaçant votre_email@example.com par votre adresse mail. Passez ensuite à l'étape a)
 

### 2. Ajouter votre clé publique sur le site hosting

Une fois copiée, aller sur [hosting.minet.net](hosting.minet.net), connectez-vous au compte du BDA, sélectionner la vm, cliquez sur "changer mes identifiants" et coller votre clé publique. Pour le nom d'utilisateur et le mdp, c'est ceux du BDA. 

# Hébergement du site sur la vm 

J'utilse nginx pour faie l'hébéregement. Normalement tout est déjà fait sur la vm donc vous n'aurez rien à modifier 

# Ajouter le navbar et le footer 
Ajoutez ceci :
  ````
    <script src="/include-navbar.js"></script> <!-- Inclusion du fichier JavaScript -->
    <script src="/include-footer.js"></script> <!-- Inclusion du fichier JavaScript -->
    <script src="/script-navbar-footer.js"></script>
    <link rel="stylesheet" href="/styles-navbar-footer.css" />
  ````
Les fichiers include-navbar.js et include-footer.js permettent d'inclure le navbar et footer sans avoir à copier 
Les fichiers script-navbar-footer.js et styles-navbar-footer.css sont les fichiers js et css des navbar et footer.

Ensuite, pour mettre le footer on met un div avec un id particulier qu'on a mis dans le fichier include-footer.js, on ajoute donc cette ligne à la toute fin (juste avant </body>:
````
<div id="footer-container"></div>
````
Idem pour le navbar, on ajoute ça dans au début de body: 
````
<div id="navbar-container"></div>
````

# Ajouter les balises Google Analytics 
Google Analytics permet d'observer le nombre de personnes ayant visité le site, quelles pages ils ont visités, où ont-ils cliqué, etc. C'est assez complet, bref c'est que pour les stats. Pour pouvoir récupérer les stats d'une page, on ajoute ça dans le <head> : 
````
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-BS8M7EH78B"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-BS8M7EH78B');
    </script>
````

# Template pour une nouvelle page
Pou faire simple, voici un template à copier coller à la création de toute nouvelle page : 
````
<!DOCTYPE html>
<html lang="en">
<head>
    
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-BS8M7EH78B"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-BS8M7EH78B');
    </script>

    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <link rel="stylesheet" href="/styles-navbar-footer.css" />
    <link rel="icon" href="images/Tache_BDA.png" type="image/x-icon">
    <title>BDA</title>
</head>
<body>
    <div id="navbar-container"></div> <!-- L'élément pour inclure la navbar -->

    <-- inserer le code principal ici -->

    <div id="footer-container"></div>
    <script src="/include-navbar.js"></script> <!-- Inclusion du navbar -->
    <script src="/animations.js"></script> <!-- Inclusion du fichier JavaScript -->
    <script src="/include-footer.js"></script> <!-- Inclusion du footer -->
    <script src="/script-navbar-footer.js"></script>
</body>
</html>
````

# Structure du site 
Le site est configuré pour que les .html et les index.html ne se voient pas dans le lien. Sinon, pour chaque page, il existe normalement un dossier au nom de la page à l'intérieur duquel il y a un fichier index.html et styles.css
pou voir et comprendre la structure du code, je vous conseille de lancer cette commande : 

````
tree --prune -I 'api'
````

Pour les erreurs, j'ai juste codé la page erreur 404, vous pourrez en faire d'autre :)

# &copy; Crédit
Développement : Ithar Kazem

Jeu : Valentin Lantigny

Illustrations : Ithar Kazem (réalisées sur Procreate)

Photos : Déclic Club Photo
