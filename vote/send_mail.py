import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Charger les identifiants depuis creds.txt
with open("creds.txt", "r", encoding="utf-8") as f:
    creds = json.load(f)  # Ex: {"email1@example.com": "motdepasse1", "email2@example.com": "motdepasse2"}

# Configuration SMTP Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "boris.bda.tmsp@gmail.com"
GMAIL_APP_PASSWORD = "yjzf gukj otmj ggzf"

# Connexion au serveur SMTP
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(GMAIL_USER, GMAIL_APP_PASSWORD)

# Envoyer un email à chaque personne
for email, code in creds.items():
    msg = MIMEMultipart()
    msg["From"] = GMAIL_USER
    msg["To"] = email
    msg["Subject"] = "Votre code de vote pour l'élection"

    body = f"""
    Bonjour,

    Pour les éléctions BDA, vous aurez besoin d'un code de vote.
    Voici votre code de vote pour l'élection :
    
    🔑 **Code de vote :** {code}

    📩 Pour voter, suivez ce lien : [Lien vers l'élection](https://vote.belenios.org/v3/election#XRDEJBRYx4RsFx)

    Cordialement,
    L'équipe BDA 

    Pour toute question, je reste joignable : 
    Par mail à boris.bda.tmsp@gmail.com
    Sur discord : @ilaguitare
    Sur Facebook : Ithar Artefact KAazem
    Sur place : en amphi 10 pendant toute la durée des votes
    """
    
    msg.attach(MIMEText(body, "html"))

    # Envoyer l'email
    server.sendmail(GMAIL_USER, email, msg.as_string())

# Fermer la connexion SMTP
server.quit()
print("Emails envoyés avec succès ! ✅")

