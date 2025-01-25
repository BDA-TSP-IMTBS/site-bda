# Présentation 
Ceci est le git du site du BDA de Télécom sudParis et IMTBS développé par le mandat Artefact 2024-2025. 
Ce site est accessible sur [bda-imtbs-tsp.fr](bda-imtbs-tsp.fr).



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

# Ajouter les balises de Google Analytics 
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

# Template à copier 
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

# Crédit
Développé par : Ithar Kazem

Illustrations : Ithar Kazem, sur Procreate

Photos : Déclic Club photo 
