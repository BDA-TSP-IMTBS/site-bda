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

Une fois copiée, aller sur [hosting.minet.net](hosting.minet.net), connectez-vous au compte du BDA, sélectionner la vm, cliquez sur "changer mes identifiants" et coller votre clé punlique. Pour le nom d'utilisateur et le mdp, c'est ceux du BDA. 

# Ajouter le navbar et le footer 
Ajoutez ceci :
  ````
    <script src="/include-navbar.js"></script> <!-- Inclusion du fichier JavaScript -->
    <script src="/include-footer.js"></script> <!-- Inclusion du fichier JavaScript -->
    <script src="/script-navbar-footer.js"></script>
  ````
Les fichiers include-navbar.js et include-footer.js permettent d'inclure le nacbar et fopter sans avoir à copier 


