Pour se conecter en ssh à la vm Minet : 
1- Vérifier si vous avez déjà une clé publique, vérifier s'il existe un fichier du type id_rsa.pub (comme id_ed24419.pub) dans ~/.ssh: 
  a) si tel est le cas, copier la clé public : ```cat ~/.ssh/eed_rsa.pub``` en remplaçant rsa par l'id de votre clé publique (dans l'exemple c'est ed24419)
  b) si ce n'est pas le cas, générer votre clé public ```ssh-keygen -t rsa -b 4096 -C "votre_email@example.com"``` en remplaçant votre_email@example.com par votre adresse mail. Passez ensuite à l'éape a)
