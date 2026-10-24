"""Génère toutes les pages du site M-TK innov à partir des données ci-dessous.

Usage : python outils/build.py   (depuis la racine du site)
Les pages HTML sont écrites à la racine ; css/ et js/ sont partagés.
"""
from pathlib import Path
from urllib.parse import quote

RACINE = Path(__file__).resolve().parent.parent
URL_SITE = "https://m-tk-innov.github.io"

CONTACT = {
    # Laisser vide tant qu'aucune adresse d'entreprise n'existe : le formulaire passe alors par LinkedIn.
    "email": "",
    "linkedin": "https://linkedin.com/in/turibio-keke",
    "github": "https://github.com/M-TK-innov",
    "ville": "Bénin",
}

POLES = {
    "sante": {"nom": "MedTech Innovation", "court": "Santé numérique"},
    "educ": {"nom": "SIKA Education", "court": "Éducation technologique"},
}

ICONES = {
    "parledocteur": '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
    "bloodlink-229": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/><path d="M9.5 14.5A2.5 2.5 0 0 0 12 17"/>',
    "paluwatch-ai": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.5"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>',
    "dagbeninon": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
    "baya": '<path d="M20.8 8.6a5 5 0 0 0-8.8-3.2 5 5 0 0 0-8.8 3.2c0 5.4 8.8 10.9 8.8 10.9s8.8-5.5 8.8-10.9z"/><path d="M7 12h3l1.5-3 2 5 1.5-2H17"/>',
    "carte-sika": '<rect x="3" y="6" width="12" height="15" rx="2"/><path d="M8 3h11a2 2 0 0 1 2 2v13"/><path d="M7 11h4M7 15h2"/>',
    "carte-sika-jeu": '<rect x="2" y="7" width="20" height="11" rx="5"/><path d="M7 11v3M5.5 12.5h3M15.5 11.5h.01M18 14h.01"/>',
    "linguabox": '<path d="M3 5h12v8H8l-4 3z"/><path d="M15 9h6v8l-3-2h-6v-2"/>',
}

PRODUITS = [
    {
        "slug": "parledocteur", "nom": "ParleDocteur", "pole": "sante", "accent": "#34d399",
        "statut": "En développement", "classe": "",
        "court": "Scribe médical IA : il écoute la consultation, structure les données cliniques et prépare une ordonnance que le médecin valide.",
        "titre": "Le médecin parle au patient. ParleDocteur s'occupe du dossier.",
        "chapeau": "Un scribe médical assisté par IA. Il écoute la consultation, en extrait les données cliniques codées, rédige le compte rendu, enrichit le dossier du patient et prépare l'ordonnance.",
        "probleme": ("La saisie mange le temps de consultation.",
                     ["Une grande partie de la consultation se passe à écrire : antécédents, constantes, diagnostic, traitement. Le patient attend, le dossier reste incomplet, et les données utiles au système de santé ne sont jamais remontées.",
                      "ParleDocteur rend ce temps au médecin et produit, dans le même geste, des données exploitables par l'établissement et par les programmes nationaux."]),
        "points": [("Écoute et transcription", "La conversation est captée pendant la consultation, y compris quand le réseau coupe : elle repart vers le serveur au rétablissement."),
                   ("Données cliniques codées", "Motif, constantes, diagnostic et traitement sont extraits et structurés pour enrichir le dossier médical du patient."),
                   ("Ordonnance validée", "L'ordonnance numérique est préparée automatiquement, mais elle n'existe qu'une fois relue et validée par le médecin."),
                   ("Interopérable", "Tout ce qui sort de l'application respecte HL7 FHIR R4, HL7 v2.5.1 et DHIS2.")],
        "engagement": ("Le médecin garde la main.",
                       "Aucune ordonnance n'est émise sans validation humaine. Hors ligne, aucune page de dossier n'est conservée en cache : un dossier périmé affiché comme actuel serait un risque clinique. Ces règles sont vérifiées par des tests automatiques."),
        "pour_qui": ["Médecins", "Cabinets et cliniques", "Hôpitaux de zone", "Centres de santé", "Programmes de santé publique"],
        "fiche": [("Supports", "Web, mobile, tablette, Windows"), ("Normes", "FHIR R4, HL7 v2.5.1, DHIS2"), ("Hors ligne", "Version poste de travail sans réseau")],
    },
    {
        "slug": "bloodlink-229", "nom": "BloodLink 229", "pole": "sante", "accent": "#f87171",
        "statut": "Prototype", "classe": "",
        "court": "Réseau intelligent de gestion du sang au Bénin, qui relie donneurs, banques de sang et hôpitaux face aux besoins urgents.",
        "titre": "La bonne poche de sang, au bon endroit, à temps.",
        "chapeau": "Une plateforme nationale qui relie les banques de sang, les hôpitaux et les donneurs volontaires, avec une prévision des besoins par intelligence artificielle.",
        "probleme": ("Une poche disponible à vingt kilomètres ne sert à rien si personne ne le sait.",
                     ["Les stocks sont suivis séparément, les demandes passent par téléphone, et les donneurs sont prévenus trop tard ou pas du tout. Devant une hémorragie à la maternité, chaque appel perdu compte.",
                      "BloodLink 229 donne à chacun la même vue des stocks et déclenche les bonnes alertes au bon moment."]),
        "points": [("Un espace par acteur", "Donneur, hôpital, banque de sang : chacun dispose d'un espace dédié, avec connexion par téléphone, NPI ou e-mail."),
                   ("Carte des stocks", "Les poches disponibles sont géolocalisées et triées par compatibilité transfusionnelle et par disponibilité."),
                   ("Alertes ciblées", "Les donneurs du bon groupe, dans la bonne zone et éligibles au don, reçoivent une alerte quand leur sang est recherché."),
                   ("Prévisions à quatre semaines", "La demande est projetée (accidents, accouchements, urgences) avec un intervalle de confiance et des recommandations.")],
        "engagement": ("La compatibilité d'abord, la proximité ensuite.",
                       "Une poche proche mais incompatible n'aide personne. La recherche classe d'abord par compatibilité, puis par distance et disponibilité, et respecte le délai entre deux dons pour protéger les donneurs."),
        "pour_qui": ["Banques de sang", "Hôpitaux et maternités", "Donneurs volontaires", "Autorités sanitaires", "Associations de donneurs"],
        "fiche": [("Format", "Application web installable (PWA)"), ("Acteurs", "Donneurs, hôpitaux, banques"), ("Stade", "Prototype de démonstration")],
    },
    {
        "slug": "paluwatch-ai", "nom": "PaluWatch AI", "pole": "sante", "accent": "#fbbf24",
        "statut": "Prototype", "classe": "",
        "court": "Prédiction, surveillance et alerte précoce contre le paludisme : carte des risques par département, prévisions, signalements communautaires.",
        "titre": "Voir venir le paludisme avant qu'il ne remplisse les hôpitaux.",
        "chapeau": "Un système intelligent de prédiction, de surveillance et de réponse précoce, qui réunit cas observés, prévisions, capteurs et signalements communautaires.",
        "probleme": ("On compte les cas quand ils sont déjà là.",
                     ["Les pics de paludisme suivent les saisons, mais la réponse arrive souvent après eux : stocks de tests et d'antipaludiques mal répartis, équipes mobilisées trop tard.",
                      "PaluWatch AI anticipe les zones à risque pour que les moyens soient en place avant le pic."]),
        "points": [("Tableau de bord national", "Cas observés, prévisions, capteurs et signalements réunis sur un même écran."),
                   ("Carte des risques", "Les douze départements du Bénin, colorés du risque faible au risque critique."),
                   ("Alertes précoces", "Messages aux relais communautaires et notifications aux autorités sanitaires quand un seuil est franchi."),
                   ("Assistant IA", "Des questions en langage naturel sur la situation épidémiologique, avec des réponses tirées des données.")],
        "engagement": ("Une prévision n'a de valeur que si elle déclenche une action.",
                       "Chaque niveau de risque est associé à une alerte, à un destinataire et à une action attendue. Le prototype actuel fonctionne sur des données fictives, en attendant un partenariat avec les acteurs de la lutte contre le paludisme."),
        "pour_qui": ["Programme national de lutte contre le paludisme", "Directions départementales de santé", "Agents de santé communautaires", "Chercheurs", "Partenaires techniques et financiers"],
        "fiche": [("Couverture", "12 départements du Bénin"), ("Sources", "Cas, climat, capteurs, signalements"), ("Stade", "Prototype, données fictives")],
    },
    {
        "slug": "dagbeninon", "nom": "Dagbeninon", "pole": "sante", "accent": "#60a5fa",
        "statut": "En incubation", "classe": "",
        "court": "Les résultats d'analyses biomédicales transcrits dans les langues nationales, pour que chaque patient comprenne son bilan.",
        "titre": "Comprendre ses résultats d'analyses, dans sa propre langue.",
        "chapeau": "Une solution e-santé qui transcrit les résultats d'analyses biomédicales dans les langues nationales du Bénin. Dagbeninon est sélectionnée à l'Academy 5 de Sèmè City.",
        "probleme": ("Un bilan qu'on ne comprend pas est un bilan qu'on ne suit pas.",
                     ["Les résultats d'analyses sont rédigés en français technique, avec des valeurs de référence que peu de patients savent lire. Beaucoup repartent du laboratoire sans savoir si leur résultat est normal ni quoi faire ensuite.",
                      "Dagbeninon rend ce document lisible et compréhensible pour le patient et sa famille."]),
        "points": [("Lecture du bilan", "Les valeurs du compte rendu de laboratoire sont repérées et situées par rapport aux valeurs de référence."),
                   ("Langues nationales", "Le contenu est restitué dans la langue du patient, et pas seulement en français."),
                   ("Mots simples", "Chaque résultat est expliqué sans jargon, pour être compris par le patient et ses proches."),
                   ("Retour vers le soignant", "Le patient sait quand reconsulter et quelles questions poser à son médecin.")],
        "engagement": ("Expliquer, sans jamais diagnostiquer.",
                       "Dagbeninon aide à comprendre un résultat. Il ne remplace ni l'interprétation du biologiste ni l'avis du médecin, et oriente toujours vers eux."),
        "pour_qui": ["Patients et familles", "Laboratoires d'analyses", "Médecins", "Centres de santé", "Mutuelles de santé"],
        "fiche": [("Langues", "Langues nationales du Bénin"), ("Stade", "Incubation"), ("Accompagnement", "Academy 5, Sèmè City")],
    },
    {
        "slug": "baya", "nom": "BAYA", "pole": "sante", "accent": "#c084fc",
        "statut": "Primé", "classe": "prime",
        "court": "Suivi des grossesses et santé maternelle. 1re place au Hackathon e-Santé 2026, avec l'équipe G-one.",
        "titre": "Suivre chaque grossesse, parce que chaque battement compte.",
        "chapeau": "Une plateforme de santé numérique pour le suivi des grossesses et la santé maternelle, qui relie les femmes enceintes, les sages-femmes, les gynécologues et les agents communautaires.",
        "probleme": ("Les signes d'alerte passent entre deux consultations.",
                     ["Entre deux visites prénatales, une femme enceinte reste souvent seule face à ses symptômes, loin du centre de santé. Les complications sont repérées tard, parfois trop tard.",
                      "BAYA maintient le lien entre la future mère et ceux qui la suivent, tout au long de la grossesse."]),
        "points": [("Un espace par rôle", "Femme enceinte, sage-femme, gynécologue, agent communautaire : chacun voit ce qui le concerne."),
                   ("Alertes graduées", "Normal, à surveiller, consultation recommandée, urgence : un code couleur simple et partagé par tous."),
                   ("Suivi continu", "Rendez-vous, symptômes et évolution de la grossesse suivis entre les consultations."),
                   ("Relais communautaire", "Les agents de santé communautaires prolongent le suivi jusqu'aux zones éloignées.")],
        "engagement": ("Prévenir plutôt que constater.",
                       "BAYA est conçu pour faire remonter un signe d'alerte le plus tôt possible vers la personne qui peut agir, et non pour remplacer le suivi médical."),
        "pour_qui": ["Femmes enceintes", "Sages-femmes", "Gynécologues", "Agents de santé communautaires", "Maternités"],
        "fiche": [("Distinction", "1re place, Hackathon e-Santé 2026"), ("Équipe", "G-one"), ("Domaine", "Santé maternelle")],
    },
    {
        "slug": "carte-sika", "nom": "Carte SIKA", "pole": "educ", "accent": "#f2c66d",
        "statut": "Disponible", "classe": "ok",
        "court": "Jeux de cartes Code Cauris pour apprendre la programmation, l'IA et l'électronique sans écran, en classe ou en famille.",
        "titre": "Apprendre à programmer avec des cartes, sans écran ni électricité.",
        "chapeau": "Les jeux de cartes Code Cauris enseignent la programmation en six langages (Scratch, algorithmique, Python, Arduino, C et C++), ainsi que l'intelligence artificielle et l'électronique.",
        "probleme": ("Pas d'ordinateur ne devrait pas vouloir dire pas de code.",
                     ["Dans beaucoup d'écoles, il n'y a ni salle informatique ni courant stable. L'enseignement du numérique reste alors théorique, ou n'existe pas du tout.",
                      "Carte SIKA transforme les notions de programmation en cartes que l'on manipule, que l'on assemble et que l'on teste sur un plateau."]),
        "points": [("Six langages", "Scratch, algorithmique, Python, Arduino, C et C++, avec un paquet de cartes par langage."),
                   ("Des défis vérifiés", "Défis sur plateau et sur ardoise, dont les solutions sont toutes contrôlées par un simulateur."),
                   ("Ancré dans le quotidien", "Le zem, le marché Dantokpa, Ganvié, la tontine, les coupures de courant : des exemples que les élèves reconnaissent."),
                   ("Prêt à imprimer", "Cartes, plateau, pions et livret au format A4. Le noir et blanc suffit : chaque famille de cartes a son symbole.")],
        "engagement": ("Chaque solution est vérifiée.",
                       "Un défi dont la solution est fausse décourage un élève pour longtemps. Toutes les solutions des défis sur plateau sont donc rejouées par un simulateur avant chaque édition du jeu."),
        "pour_qui": ["Écoles primaires et collèges", "Enseignants", "Clubs de code et de robotique", "Parents", "ONG éducatives"],
        "fiche": [("Langages", "Scratch, algo, Python, Arduino, C, C++"), ("Contenu", "Cartes, plateau, défis, livret"), ("Matériel", "Impression A4, noir et blanc")],
        "lie": "carte-sika-jeu",
    },
    {
        "slug": "carte-sika-jeu", "nom": "Carte SIKA Jeu", "pole": "educ", "accent": "#fb923c",
        "statut": "Disponible", "classe": "ok",
        "court": "Le jeu sur écran, hors ligne : programmer le zem jusqu'au marché, relever des défis et obtenir un certificat par niveau.",
        "titre": "Le jeu Carte SIKA sur tous les écrans, même sans internet.",
        "chapeau": "La version numérique de Carte SIKA : programmer le zem jusqu'au marché, relever des défis Arduino, IA et électronique, et obtenir un certificat à chaque niveau. Sur le web, Android, iPhone, iPad et Windows.",
        "probleme": ("Apprendre seul, c'est souvent rester bloqué.",
                     ["Sans enseignant à côté, une erreur de logique peut arrêter un élève pendant des heures. Et donner la réponse directement ne lui apprend rien.",
                      "Carte SIKA Jeu contrôle chaque réponse et guide l'élève jusqu'à ce qu'il trouve par lui-même."]),
        "points": [("Plateau du zem", "Le joueur programme le zem avec les cartes Code Cauris (avancer, tourner, répéter, si...) jusqu'au marché."),
                   ("Défis variés", "Questions sur ardoise, Arduino, Cauris IA et Cauris Électronique, tirées des cartes défi."),
                   ("Astuces graduées", "Chaque réponse est comparée aux éléments attendus : le joueur voit ce qui est juste, ce qui manque, et reçoit des indices progressifs."),
                   ("Certificats et tuteur", "Un certificat PDF par niveau, au nom du joueur, et un tuteur SIKA qui répond aux questions sans internet.")],
        "engagement": ("Aider sans donner la réponse.",
                       "Les indices arrivent un par un, du plus général au plus précis. L'objectif est que l'élève comprenne son erreur, pas qu'il recopie une solution."),
        "pour_qui": ["Élèves", "Enseignants", "Écoles", "Autodidactes", "Parents"],
        "fiche": [("Plateformes", "Web, Android, iOS, Windows"), ("Licence", "5 000 FCFA, activée une fois"), ("Paiement", "FedaPay ou code école")],
        "lie": "carte-sika",
    },
    {
        "slug": "linguabox", "nom": "LinguaBox", "pole": "educ", "accent": "#38bdf8",
        "statut": "En développement", "classe": "",
        "court": "Apprendre l'anglais hors ligne, du niveau A1 au C2, avec un tuteur vocal et une conversation quotidienne de 15 minutes.",
        "titre": "Parler anglais quinze minutes par jour, sans connexion.",
        "chapeau": "Une application pour apprendre l'anglais du niveau A1 au niveau C2, conçue pour les francophones. Son cœur : une conversation quotidienne de quinze minutes avec un tuteur vocal.",
        "probleme": ("On étudie l'anglais pendant des années sans jamais le parler.",
                     ["À l'école comme dans la plupart des applications, on apprend des règles et des listes de mots. L'oral, lui, reste la compétence la moins travaillée, alors que c'est celle dont on a besoin.",
                      "LinguaBox fait de la conversation l'activité principale, et met tout le reste à son service."]),
        "points": [("Conversation de 15 minutes", "Treize sujets gradués ou un sujet libre : le tuteur relance, fait parler et corrige avec discrétion."),
                   ("Niveau par compétence", "Un test adaptatif évalue séparément lecture, écoute, écrit et oral, et le planning en tient compte."),
                   ("Correcteur pour francophones", "Trente-neuf règles ciblent les fautes typiques : « I have 25 years », « I am agree », faux amis..."),
                   ("Révision espacée", "Tout ce qui est travaillé revient au bon moment, avec une progression ludique pour garder le rythme.")],
        "engagement": ("Rien ne quitte l'appareil.",
                       "Pas de compte, pas de serveur, pas de connexion nécessaire. Les progrès et les enregistrements restent sur le téléphone ou l'ordinateur de l'apprenant."),
        "pour_qui": ["Élèves et étudiants", "Professionnels", "Candidats aux examens", "Voyageurs", "Enseignants d'anglais"],
        "fiche": [("Niveaux", "A1 à C2"), ("Plateformes", "Web, ordinateur, mobile"), ("Connexion", "Aucune requise")],
    },
]
PAR_SLUG = {p["slug"]: p for p in PRODUITS}


def icone(slug, taille=24):
    return (f'<svg width="{taille}" height="{taille}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONES[slug]}</svg>')


FLECHE = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
LOGO = '<svg width="34" height="34" viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="14" fill="#13241f"/><path d="M14 46V18l12 16 12-16v28" fill="none" stroke="#34d399" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="48" cy="20" r="5" fill="#f2c66d"/></svg>'
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230b1512'/%3E%3Cpath d='M14 46V18l12 16 12-16v28' fill='none' stroke='%2334d399' stroke-width='5' stroke-linecap='round' stroke-linejoin='round'/%3E%3Ccircle cx='48' cy='20' r='5' fill='%23f2c66d'/%3E%3C/svg%3E"


def lien_contact(sujet, produit=None):
    url = f"contact.html?sujet={quote(sujet)}"
    if produit:
        url += f"&produit={quote(produit)}"
    return url


def cur(actif, nom):
    return ' aria-current="page"' if actif == nom else ""


def entete(actif):
    sante = "".join(f'<a href="{p["slug"]}.html"{cur(actif, p["slug"])}>{p["nom"]}<small>{p["statut"]}</small></a>'
                    for p in PRODUITS if p["pole"] == "sante")
    educ = "".join(f'<a href="{p["slug"]}.html"{cur(actif, p["slug"])}>{p["nom"]}<small>{p["statut"]}</small></a>'
                   for p in PRODUITS if p["pole"] == "educ")
    produits_actif = " actif" if actif == "produits" or actif in PAR_SLUG else ""
    return f'''<a class="lien-evitement" href="#contenu">Aller au contenu</a>
<header>
  <div class="conteneur barre">
    <a class="logo" href="index.html" aria-label="M-TK innov, accueil">{LOGO}<span>M-TK <b>innov</b></span></a>
    <nav class="nav-principale" aria-label="Navigation principale">
      <ul id="menu">
        <li class="deroulant{produits_actif}">
          <button type="button" aria-expanded="false" aria-controls="sous-menu-produits">Produits
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
          </button>
          <div class="sous-menu" id="sous-menu-produits">
            <div><div class="groupe">{POLES["sante"]["nom"]}</div>{sante}</div>
            <div><div class="groupe">{POLES["educ"]["nom"]}</div>{educ}</div>
            <a class="tout" href="produits.html"{cur(actif, "produits")}>Voir tous les produits</a>
          </div>
        </li>
        <li><a href="services.html"{cur(actif, "services")}>Services</a></li>
        <li><a href="mission.html"{cur(actif, "mission")}>Mission</a></li>
        <li><a href="equipe.html"{cur(actif, "equipe")}>Équipe</a></li>
        <li><a href="investir.html"{cur(actif, "investir")}>Investir</a></li>
        <li><a href="contact.html"{cur(actif, "contact")}>Contact</a></li>
      </ul>
    </nav>
    <a class="btn btn-plein" href="{lien_contact("Projet")}">Travailler avec nous</a>
    <button class="menu-btn" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="menu">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
  </div>
</header>'''


def pied():
    sante = "".join(f'<li><a href="{p["slug"]}.html">{p["nom"]}</a></li>' for p in PRODUITS if p["pole"] == "sante")
    educ = "".join(f'<li><a href="{p["slug"]}.html">{p["nom"]}</a></li>' for p in PRODUITS if p["pole"] == "educ")
    email = f'<li><a href="mailto:{CONTACT["email"]}">{CONTACT["email"]}</a></li>' if CONTACT["email"] else ""
    return f'''<footer>
  <div class="conteneur">
    <div class="pied-grille">
      <div>
        <a class="logo" href="index.html">{LOGO}<span>M-TK <b>innov</b></span></a>
        <p>Des technologies qui soignent et qui forment, conçues au Bénin depuis 2024.</p>
      </div>
      <div><h4>{POLES["sante"]["nom"]}</h4><ul>{sante}</ul></div>
      <div><h4>{POLES["educ"]["nom"]}</h4><ul>{educ}</ul></div>
      <div><h4>M-TK innov</h4><ul>
        <li><a href="services.html">Services</a></li>
        <li><a href="mission.html">Mission</a></li>
        <li><a href="equipe.html">Équipe</a></li>
        <li><a href="investir.html">Investir</a></li>
        <li><a href="contact.html">Contact</a></li>
        {email}
      </ul></div>
    </div>
    <div class="pied-bas">
      <span>© <span class="annee">2026</span> M-TK innov, {CONTACT["ville"]}</span>
      <span><a href="{CONTACT["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a> · <a href="{CONTACT["github"]}" target="_blank" rel="noopener">GitHub</a></span>
    </div>
  </div>
</footer>'''


def page(fichier, titre, description, contenu, actif="", accent=None):
    style_accent = f' style="--accent:{accent}"' if accent else ""
    titre_complet = "M-TK innov | Santé numérique et éducation technologique au Bénin" if fichier == "index.html" else f"{titre} | M-TK innov"
    url = f"{URL_SITE}/" if fichier == "index.html" else f"{URL_SITE}/{fichier}"
    html = f'''<!DOCTYPE html>
<html lang="fr" class="sans-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre_complet}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="M-TK innov">
<meta property="og:title" content="{titre}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta name="theme-color" content="#0b1512">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body{style_accent}>
{entete(actif)}
<main id="contenu">
{contenu}
</main>
{pied()}
<script src="js/site.js"></script>
<script>document.querySelectorAll('.annee').forEach(e => e.textContent = new Date().getFullYear());</script>
</body>
</html>
'''
    (RACINE / fichier).write_text(html, encoding="utf-8")
    return fichier


# ---------- Blocs réutilisables ----------

def carte_produit(p):
    return f'''<article class="produit" data-pole="{p["pole"]}" style="--accent:{p["accent"]}">
  <div class="haut"><span class="pastille">{icone(p["slug"])}</span><span class="statut {p["classe"]}">{p["statut"]}</span></div>
  <h3><a class="couvre" href="{p["slug"]}.html">{p["nom"]}</a></h3>
  <p>{p["court"]}</p>
  <div class="pied"><span>{POLES[p["pole"]]["nom"]}</span><b>Découvrir {FLECHE}</b></div>
</article>'''


def bloc_contact(titre="Un projet en santé ou en éducation ?",
                 texte="Hôpital, école, ONG, institution ou entreprise : parlons de votre besoin et de la manière d'y répondre ensemble.",
                 sujet="Projet", bouton="Nous écrire"):
    return f'''<div class="contact">
  <div class="conteneur">
    <div class="contact-carte apparait">
      <div><h2>{titre}</h2><p>{texte}</p></div>
      <div class="actions">
        <a class="btn btn-plein" href="{lien_contact(sujet)}">{bouton}</a>
        <a class="btn btn-contour" href="produits.html">Voir nos produits</a>
      </div>
    </div>
  </div>
</div>'''


DISTINCTIONS = '''<div class="distinctions">
  <div class="conteneur">
    <div class="distinction"><strong>1re place, Hackathon e-Santé 2026</strong><span>avec le projet BAYA</span></div>
    <div class="distinction"><strong>Incubation à Sèmè City</strong><span>Dagbeninon, sélectionnée à l'Academy 5</span></div>
    <div class="distinction"><strong>2e place nationale FLL</strong><span>équipe du LMJFGMK, formée et accompagnée par M-TK</span></div>
  </div>
</div>'''


def defile(mots):
    suite = "".join(f"<span>{m}</span>" for m in mots)
    return f'<div class="defile" aria-hidden="true"><div class="defile-piste">{suite}{suite}</div></div>'


# ---------- Pages ----------

def accueil():
    vedettes = "".join(carte_produit(PAR_SLUG[s]) for s in ["parledocteur", "carte-sika-jeu", "bloodlink-229", "linguabox", "baya", "carte-sika"])
    sante = "".join(f'<li><a href="{p["slug"]}.html">{p["nom"]}</a></li>' for p in PRODUITS if p["pole"] == "sante")
    educ = "".join(f'<li><a href="{p["slug"]}.html">{p["nom"]}</a></li>' for p in PRODUITS if p["pole"] == "educ")
    contenu = f'''<div class="hero">
  <div class="conteneur">
    <div class="cauris" aria-hidden="true"><span></span><span></span><span></span></div>
    <h1>Des technologies qui <em>soignent</em> et qui <em>forment</em>, conçues au Bénin.</h1>
    <div class="hero-bas">
      <p class="chapeau">Intelligence artificielle médicale, outils de santé publique, jeux pour apprendre le code sans écran. Nous transformons les besoins du terrain en produits utilisables dès aujourd'hui.</p>
      <div class="actions">
        <a class="btn btn-plein" href="produits.html">Découvrir nos produits</a>
        <a class="btn btn-contour" href="{lien_contact("Projet")}">Travailler avec nous</a>
      </div>
    </div>
  </div>
</div>
{DISTINCTIONS}
{defile(["Hôpitaux", "Centres de santé", "Banques de sang", "Laboratoires", "Écoles", "Enseignants", "Clubs de robotique", "ONG", "Institutions publiques", "Familles"])}

<div class="citation"><div class="conteneur apparait">
  <p>Partir d'un problème local, le résoudre avec <span>rigueur</span>, et le rendre accessible à tous.</p>
</div></div>

<section id="poles" class="serre">
  <div class="conteneur">
    <div class="apparait">
      <div class="surtitre">Nos pôles</div>
      <h2>Deux pôles, une même exigence.</h2>
      <p class="intro">Depuis avril 2024, M-TK innov développe ses produits autour de deux axes complémentaires : la santé numérique et l'éducation technologique.</p>
    </div>
    <div class="poles">
      <article class="pole sante apparait">
        <svg width="52" height="52" viewBox="0 0 52 52" fill="none" stroke="#34d399" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="4" width="44" height="44" rx="12"/><path d="M26 15v22M15 26h22"/></svg>
        <span class="etiquette">MedTech Innovation</span>
        <h3>L'IA au service des soignants</h3>
        <p>Scribe médical, gestion du sang, prédiction des épidémies, suivi de grossesse, analyses expliquées dans les langues nationales. Des outils pensés pour les hôpitaux, les centres de santé et les autorités sanitaires.</p>
        <ul>{sante}</ul>
      </article>
      <article class="pole educ apparait">
        <svg width="52" height="52" viewBox="0 0 52 52" fill="none" stroke="#f2c66d" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><ellipse cx="26" cy="26" rx="14" ry="20"/><path d="M26 10v32M20 18h2M20 24h2M20 30h2M30 18h2M30 24h2M30 30h2"/></svg>
        <span class="etiquette">SIKA Education</span>
        <h3>Apprendre le numérique, même sans écran</h3>
        <p>Jeux de cartes, applications hors ligne et formations pour initier enfants, élèves et enseignants au code, à l'intelligence artificielle, à l'électronique et à l'anglais.</p>
        <ul>{educ}</ul>
      </article>
    </div>
  </div>
</section>

<section class="serre">
  <div class="conteneur">
    <div class="entete-section apparait">
      <div><div class="surtitre">Nos produits</div><h2>Nés du terrain, testés sur le terrain.</h2></div>
      <a class="btn-lien" href="produits.html">Tous les produits {FLECHE}</a>
    </div>
    <div class="grille">{vedettes}</div>
  </div>
</section>

<section class="fond-2">
  <div class="conteneur deux-col">
    <div class="apparait">
      <div class="surtitre">Services</div>
      <h2>L'équipe qui construit nos produits peut construire le vôtre.</h2>
      <p class="intro">Solutions e-santé, intelligence artificielle, applications web et mobiles, formations en IA et en robotique : nous mettons au service de nos partenaires les méthodes éprouvées sur nos propres produits.</p>
      <p style="margin-top:28px"><a class="btn btn-contour" href="services.html">Découvrir nos services</a></p>
    </div>
    <div class="chiffres apparait">
      <div class="chiffre"><strong>2024</strong><span>année de création, au Bénin</span></div>
      <div class="chiffre"><strong>2</strong><span>pôles : santé et éducation</span></div>
      <div class="chiffre"><strong>8</strong><span>produits conçus</span></div>
      <div class="chiffre"><strong>4</strong><span>plateformes : web, Android, iOS, ordinateur</span></div>
    </div>
  </div>
</section>

<div class="citation"><div class="conteneur apparait">
  <p>Beaucoup de solutions conçues ailleurs ne fonctionnent pas ici. Nous partons de nos <span>contraintes</span> pour construire ce qui marche.</p>
  <p style="margin-top:28px;font-size:1rem;font-family:var(--corps)"><a class="btn-lien" href="mission.html">Notre mission {FLECHE}</a></p>
</div></div>
{bloc_contact()}'''
    return page("index.html", "M-TK innov",
                "M-TK innov conçoit au Bénin des solutions d'intelligence artificielle pour la santé (MedTech Innovation) et des outils pour apprendre le code, l'IA et l'électronique (SIKA Education).",
                contenu, "accueil")


def catalogue():
    cartes = "".join(carte_produit(p) for p in PRODUITS)
    contenu = f'''<div class="page-hero">
  <div class="conteneur">
    <div class="surtitre">Nos produits</div>
    <h1>Huit produits, deux pôles, un même terrain.</h1>
    <p class="intro">Chaque produit part d'un problème observé dans un hôpital, une école ou une famille, et vise une solution qui fonctionne avec les moyens disponibles : connexion intermittente, téléphone d'entrée de gamme, langues nationales.</p>
  </div>
</div>
<section class="serre">
  <div class="conteneur">
    <div class="filtres" role="group" aria-label="Filtrer les produits">
      <button type="button" data-filtre="tous" aria-pressed="true">Tous</button>
      <button type="button" data-filtre="sante" aria-pressed="false">{POLES["sante"]["nom"]}</button>
      <button type="button" data-filtre="educ" aria-pressed="false">{POLES["educ"]["nom"]}</button>
    </div>
    <div class="grille">{cartes}</div>
  </div>
</section>
{bloc_contact("Un produit vous intéresse ?", "Démonstration, projet pilote dans votre établissement, déploiement à plus grande échelle : dites-nous ce que vous cherchez.", "Démo", "Demander une démonstration")}'''
    return page("produits.html", "Nos produits",
                "ParleDocteur, BloodLink 229, PaluWatch AI, Dagbeninon, BAYA, Carte SIKA, Carte SIKA Jeu et LinguaBox : les produits de M-TK innov.",
                contenu, "produits")


def page_produit(i, p):
    pole = POLES[p["pole"]]
    titre_pb, paras = p["probleme"]
    points = "".join(f'<div class="point apparait"><span class="num">{n:02d}</span><h3>{t}</h3><p>{d}</p></div>'
                     for n, (t, d) in enumerate(p["points"], 1))
    fiche = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in p["fiche"])
    pour_qui = "".join(f"<span>{x}</span>" for x in p["pour_qui"])
    prec, suiv = PRODUITS[i - 1], PRODUITS[(i + 1) % len(PRODUITS)]
    lie = ""
    if p.get("lie"):
        q = PAR_SLUG[p["lie"]]
        lie = f'<a class="btn btn-contour" href="{q["slug"]}.html">Voir {q["nom"]}</a>'
    contenu = f'''<div class="page-hero">
  <div class="conteneur">
    <nav class="fil" aria-label="Fil d'Ariane"><a href="produits.html">Produits</a><span aria-hidden="true">/</span><span>{pole["nom"]}</span><span aria-hidden="true">/</span><span>{p["nom"]}</span></nav>
    <div class="produit-entete"><span class="pastille">{icone(p["slug"], 26)}</span><div><strong>{p["nom"]}</strong><small>{pole["nom"]}</small></div><span class="statut {p["classe"]}" style="margin-left:auto">{p["statut"]}</span></div>
    <h1>{p["titre"]}</h1>
    <div class="hero-bas">
      <p class="chapeau">{p["chapeau"]}</p>
      <div class="actions">
        <a class="btn btn-plein" href="{lien_contact("Démo", p["nom"])}">Demander une démonstration</a>
        {lie}
      </div>
    </div>
    <dl class="fiche">{fiche}</dl>
  </div>
</div>

<section class="fond-2">
  <div class="etroit texte apparait">
    <div class="surtitre">Le problème</div>
    <h2>{titre_pb}</h2>
    {"".join(f"<p>{x}</p>" for x in paras)}
  </div>
</section>

<section>
  <div class="conteneur">
    <div class="apparait"><div class="surtitre">Ce que fait {p["nom"]}</div><h2>Quatre fonctions, un seul objectif.</h2></div>
    <div class="points">{points}</div>
  </div>
</section>

<section class="serre">
  <div class="conteneur">
    <div class="engagement apparait">
      <div class="surtitre">Notre engagement</div>
      <h2>{p["engagement"][0]}</h2>
      <p>{p["engagement"][1]}</p>
    </div>
  </div>
</section>

<section class="serre">
  <div class="conteneur apparait">
    <div class="surtitre">Pour qui</div>
    <h2>Conçu avec et pour</h2>
    <div class="pilules">{pour_qui}</div>
  </div>
</section>

<section class="serre">
  <div class="conteneur suivant">
    <a href="{prec["slug"]}.html"><small>Produit précédent</small><strong>{prec["nom"]}</strong></a>
    <a href="{suiv["slug"]}.html"><small>Produit suivant</small><strong>{suiv["nom"]}</strong></a>
  </div>
</section>
{bloc_contact(f"Essayer {p['nom']} dans votre structure ?", "Nous organisons des démonstrations et des projets pilotes avec les établissements et les partenaires intéressés.", "Démo", "Demander une démonstration")}'''
    return page(f'{p["slug"]}.html', p["nom"], p["court"], contenu, p["slug"], p["accent"])


def services():
    reals = "".join(f'''<a class="realisation apparait" href="{p["slug"]}.html" style="--accent:{p["accent"]}">
  <strong>{p["nom"]}<small>{POLES[p["pole"]]["nom"]}</small></strong><p>{p["court"]}</p><span class="fleche">{FLECHE}</span></a>'''
                    for p in PRODUITS if p["slug"] in ("parledocteur", "bloodlink-229", "carte-sika-jeu", "linguabox"))
    contenu = f'''<div class="page-hero">
  <div class="conteneur">
    <div class="surtitre">Services</div>
    <h1>Ce que nous construisons pour nous, nous le construisons pour vous.</h1>
    <div class="hero-bas">
      <p class="chapeau">L'équipe qui a conçu ParleDocteur, BloodLink 229 et Carte SIKA met ses méthodes au service des hôpitaux, des écoles, des ONG et des entreprises.</p>
      <div class="actions"><a class="btn btn-plein" href="{lien_contact("Projet")}">Démarrer un projet</a></div>
    </div>
  </div>
</div>

<div class="citation" style="padding-top:20px"><div class="conteneur apparait">
  <p>Nous ne vendons pas des recommandations : nous proposons des choix que nous avons <span>déjà testés</span> sur nos propres produits.</p>
</div></div>

<section class="fond-2">
  <div class="conteneur">
    <div class="apparait"><div class="surtitre">Nos domaines</div><h2>Quatre métiers sous un même toit.</h2></div>
    <div class="services-grille">
      <div class="service"><span class="num">01</span><h3>Solutions e-santé</h3><p>Des outils numériques pour les soignants et les gestionnaires de santé.</p>
        <ul><li>Dossier patient et consultation</li><li>Tableaux de bord épidémiologiques</li><li>Interopérabilité FHIR, HL7, DHIS2</li></ul></div>
      <div class="service"><span class="num">02</span><h3>Intelligence artificielle</h3><p>Des modèles adaptés aux langues, aux données et aux usages locaux.</p>
        <ul><li>Reconnaissance et synthèse vocale</li><li>Modèles de prédiction</li><li>Assistants conversationnels</li></ul></div>
      <div class="service"><span class="num">03</span><h3>Applications web et mobiles</h3><p>Pensées pour le mobile d'abord et pour une connexion intermittente.</p>
        <ul><li>Applications installables (PWA)</li><li>Android, iOS et ordinateur</li><li>Fonctionnement hors ligne</li></ul></div>
      <div class="service"><span class="num">04</span><h3>Formation IA et robotique</h3><p>Des formations concrètes, sur le terrain, avec ou sans ordinateur.</p>
        <ul><li>Ateliers élèves et enseignants</li><li>Initiation à Arduino et à l'IA</li><li>Coaching d'équipes de compétition</li></ul></div>
    </div>
  </div>
</section>

<section>
  <div class="conteneur">
    <div class="apparait"><div class="surtitre">Notre méthode</div><h2>Du terrain au produit, en quatre temps.</h2></div>
    <div class="etapes">
      <div class="etape apparait"><span class="num">01 · COMPRENDRE</span><h3>Partir du terrain</h3><p>Nous observons le problème là où il se pose : au service, en classe, auprès des usagers. Objectif clair, contraintes réelles, budget connu.</p></div>
      <div class="etape apparait"><span class="num">02 · CONCEVOIR</span><h3>Avec les usagers</h3><p>Parcours, interfaces et contenus conçus avec ceux qui vont s'en servir, et testés tôt sur de vrais appareils.</p></div>
      <div class="etape apparait"><span class="num">03 · CONSTRUIRE</span><h3>Par étapes</h3><p>Livraison par jalons. Vous voyez le produit avancer et vous pouvez l'essayer à chaque étape.</p></div>
      <div class="etape apparait"><span class="num">04 · ACCOMPAGNER</span><h3>Former et suivre</h3><p>Formation des équipes, documentation, suivi après le lancement et corrections à partir de l'usage réel.</p></div>
    </div>
  </div>
</section>

<section class="serre">
  <div class="conteneur">
    <div class="entete-section apparait">
      <div><div class="surtitre">Réalisations</div><h2>Ce que notre équipe a déjà construit.</h2></div>
      <a class="btn-lien" href="produits.html">Tous les produits {FLECHE}</a>
    </div>
    <div class="realisations">{reals}</div>
  </div>
</section>

<section class="serre">
  <div class="conteneur apparait">
    <div class="surtitre">Nous travaillons bien avec</div>
    <h2>Les structures qui veulent un outil qui sert vraiment.</h2>
    <div class="pilules"><span>Hôpitaux et cliniques</span><span>Programmes de santé publique</span><span>Écoles et universités</span><span>ONG et associations</span><span>Collectivités locales</span><span>Entreprises</span><span>Porteurs de projets</span></div>
  </div>
</section>
{bloc_contact("Parlons de votre projet.", "Décrivez votre besoin en quelques lignes : nous revenons vers vous avec une première proposition.", "Projet", "Démarrer un projet")}'''
    return page("services.html", "Services",
                "Solutions e-santé, intelligence artificielle, applications web et mobiles, formation IA et robotique : les services de M-TK innov.",
                contenu, "services")


def mission():
    contenu = f'''<div class="page-hero">
  <div class="conteneur">
    <div class="surtitre">Mission</div>
    <h1>Soigner mieux et apprendre plus ne devrait pas dépendre de l'endroit où l'on vit.</h1>
  </div>
</div>

<section class="fond-2">
  <div class="conteneur deux-col haut">
    <div class="texte apparait">
      <div class="surtitre">Le constat</div>
      <h2>Beaucoup de solutions conçues ailleurs ne fonctionnent pas ici.</h2>
    </div>
    <div class="texte apparait">
      <p>Connexion instable, coupures de courant, téléphones d'entrée de gamme, rareté des spécialistes, langues nationales absentes des logiciels : la plupart des outils numériques supposent des conditions que nos hôpitaux et nos écoles n'ont pas.</p>
      <p>Résultat : des médecins qui remplissent encore des registres à la main, des stocks de sang suivis par téléphone, des élèves qui finissent leur scolarité sans avoir jamais écrit une ligne de code.</p>
    </div>
  </div>
</section>

<section>
  <div class="conteneur deux-col haut">
    <div class="texte apparait">
      <div class="surtitre">Notre conviction</div>
      <h2>Les contraintes du terrain sont un cahier des charges.</h2>
    </div>
    <div class="texte apparait">
      <p>Un outil qui fonctionne hors ligne, sur un petit téléphone et dans la langue de l'usager fonctionnera partout. Nous partons donc de ces contraintes au lieu de les contourner.</p>
      <p>Et nous ne remplaçons personne : <strong>le médecin valide, l'enseignant guide, le patient décide.</strong> La technologie leur fait gagner du temps et de la portée.</p>
    </div>
  </div>
</section>

<section class="serre">
  <div class="conteneur">
    <div class="engagement apparait">
      <div class="surtitre">Notre mission</div>
      <div class="triade"><span>Soigner.</span><span>Former.</span><span>Rendre accessible.</span></div>
      <p>Concevoir au Bénin des solutions d'intelligence artificielle et des outils numériques qui améliorent la prise en charge des patients et l'apprentissage des technologies, et les rendre utilisables par tous, y compris loin des grandes villes.</p>
    </div>
  </div>
</section>

<section class="serre">
  <div class="conteneur deux-col haut">
    <div class="texte apparait">
      <div class="surtitre">Notre vision</div>
      <h2>Un soignant mieux équipé, un élève mieux préparé, dans chaque commune.</h2>
    </div>
    <div class="texte apparait">
      <p>Nous voulons que chaque centre de santé dispose d'outils fiables pour suivre ses patients et partager ses données, et que chaque élève puisse découvrir le code, l'électronique et l'intelligence artificielle, avec ou sans ordinateur.</p>
    </div>
  </div>
</section>

<section class="fond-2">
  <div class="conteneur">
    <div class="apparait"><div class="surtitre">Deux pôles, deux leviers</div><h2>La santé et l'éducation, parce que tout le reste en dépend.</h2></div>
    <div class="services-grille deux">
      <div class="service"><span class="num">MedTech Innovation</span><h3>Pour les soignants et les patients</h3><p>Des outils qui font gagner du temps aux soignants, sécurisent les décisions et rendent l'information médicale compréhensible.</p>
        <ul>{"".join(f'<li><a href="{p["slug"]}.html">{p["nom"]}</a></li>' for p in PRODUITS if p["pole"] == "sante")}</ul></div>
      <div class="service"><span class="num" style="color:var(--or)">SIKA Education</span><h3>Pour les élèves et les enseignants</h3><p>Des jeux, des applications et des formations pour apprendre les technologies en partant du quotidien des élèves.</p>
        <ul>{"".join(f'<li><a href="{p["slug"]}.html">{p["nom"]}</a></li>' for p in PRODUITS if p["pole"] == "educ")}</ul></div>
    </div>
  </div>
</section>

<section>
  <div class="conteneur apparait">
    <div class="surtitre">Pour qui nous construisons</div>
    <h2>Ceux qui soignent, ceux qui apprennent, ceux qui décident.</h2>
    <div class="pilules"><span>Médecins et sages-femmes</span><span>Agents de santé communautaires</span><span>Patients et familles</span><span>Élèves et étudiants</span><span>Enseignants</span><span>Autorités sanitaires et éducatives</span><span>Partenaires de développement</span></div>
    <div class="actions" style="margin-top:40px"><a class="btn btn-plein" href="produits.html">Découvrir nos produits</a><a class="btn btn-contour" href="{lien_contact("Projet")}">Travailler avec nous</a></div>
  </div>
</section>'''
    return page("mission.html", "Mission",
                "Soigner, former, rendre accessible : la mission de M-TK innov, startup béninoise de santé numérique et d'éducation technologique.",
                contenu, "mission")


def equipe():
    contenu = f'''<div class="page-hero">
  <div class="conteneur">
    <div class="surtitre">Équipe</div>
    <h1>Des métiers qui travaillent rarement ensemble.</h1>
    <p class="intro">Ingénierie IA, développement, santé numérique, pédagogie, électronique : M-TK innov réunit des profils qui se croisent peu. C'est ce qui nous permet de concevoir des produits complets, de l'observation du terrain jusqu'à la mise en service.</p>
  </div>
</div>

<section class="serre">
  <div class="conteneur">
    <div class="fondateur apparait">
      <img src="img/fondateur.jpg" alt="Portrait de Mahuvivi Turibio KEKE" width="280" height="280" loading="lazy">
      <div>
        <div class="surtitre">Fondateur</div>
        <h3>Mahuvivi Turibio KEKE</h3>
        <div class="role">Fondateur et directeur de M-TK innov</div>
        <p>Ingénieur, formateur et entrepreneur, Mahuvivi Turibio KEKE a créé M-TK innov en avril 2024 pour réunir sous un même toit l'innovation en santé et l'éducation technologique.</p>
        <ul>
          <li>Consultant formateur en IA et robotique à Sèmè City</li>
          <li>Enseignant à l'IFRI depuis 2025</li>
          <li>Mentor IT chez Tekbot Robotics</li>
          <li>Diplôme interuniversitaire e-Santé (Digi-Santé-Mali, 2026)</li>
          <li>Participant au Deep Learning Indaba 2024, 2025 et 2026</li>
        </ul>
        <div class="actions" style="margin-top:22px"><a class="btn btn-contour" href="{CONTACT["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a></div>
      </div>
    </div>
  </div>
</section>

<section class="fond-2">
  <div class="conteneur">
    <div class="apparait"><div class="surtitre">Nos départements</div><h2>Cinq compétences pour un même produit.</h2></div>
    <div class="services-grille trois">
      <div class="service"><span class="num">01</span><h3>Intelligence artificielle</h3><p>Reconnaissance vocale, extraction de données cliniques, modèles de prédiction, tuteurs conversationnels. Le département qui fait parler nos produits, et qui les empêche d'inventer.</p></div>
      <div class="service"><span class="num">02</span><h3>Développement</h3><p>Applications web, mobiles et de bureau, conçues pour fonctionner hors ligne et sur des appareils modestes.</p></div>
      <div class="service"><span class="num">03</span><h3>Santé numérique</h3><p>Normes d'interopérabilité, sécurité des données, parcours de soins. Le lien entre nos outils et la réalité des établissements de santé.</p></div>
      <div class="service"><span class="num">04</span><h3>Pédagogie et contenus</h3><p>Cartes, défis, livrets, programmes de langue : des contenus vérifiés et adaptés au quotidien des élèves.</p></div>
      <div class="service"><span class="num">05</span><h3>Électronique et robotique</h3><p>Arduino, capteurs, robotique éducative et accompagnement d'équipes de compétition.</p></div>
      <div class="service"><span class="num">06</span><h3>Vous ?</h3><p>Développeurs, soignants, enseignants, designers : nous cherchons des personnes qui veulent construire des outils utiles.</p>
        <p style="margin-top:14px"><a class="btn-lien" href="{lien_contact("Rejoindre")}">Nous rejoindre {FLECHE}</a></p></div>
    </div>
  </div>
</section>

<section>
  <div class="conteneur apparait">
    <div class="surtitre">Écosystème</div>
    <h2>Ils accompagnent notre parcours.</h2>
    <div class="pilules"><span>Sèmè City, Academy 5</span><span>Tekbot Robotics</span><span>IFRI</span><span>Cotonou AI Academy</span><span>Deep Learning Indaba</span><span>Digi-Santé-Mali</span></div>
  </div>
</section>
{bloc_contact("Envie de construire avec nous ?", "Candidature spontanée, stage, collaboration de recherche : écrivez-nous en présentant ce que vous aimeriez apporter.", "Rejoindre", "Nous rejoindre")}'''
    return page("equipe.html", "Équipe",
                "L'équipe de M-TK innov : intelligence artificielle, développement, santé numérique, pédagogie, électronique et robotique.",
                contenu, "equipe")


def investir():
    contenu = f'''<div class="page-hero">
  <div class="conteneur">
    <div class="surtitre">Investisseurs et partenaires</div>
    <h1>Investir dans les outils qui manquent à la santé et à l'école.</h1>
    <div class="hero-bas">
      <p class="chapeau">M-TK innov construit des produits pour deux secteurs où chaque gain de temps et chaque compétence acquise se mesure en vies et en avenir.</p>
      <div class="actions"><a class="btn btn-plein" href="{lien_contact("Investir")}">Demander le dossier</a></div>
    </div>
  </div>
</div>

<section class="serre">
  <div class="conteneur apparait">
    <div class="surtitre">Où nous en sommes</div>
    <h2>Des produits, pas des intentions.</h2>
    <dl class="etat">
      <div><dt>Produits</dt><dd>Huit conçus, deux disponibles</dd></div>
      <div><dt>Distinction</dt><dd>1re place, Hackathon e-Santé 2026</dd></div>
      <div><dt>Incubation</dt><dd>Academy 5, Sèmè City</dd></div>
      <div><dt>Création</dt><dd>Avril 2024, Bénin</dd></div>
    </dl>
  </div>
</section>

<section>
  <div class="conteneur deux-col haut">
    <div class="apparait"><div class="surtitre">Pourquoi maintenant</div><h2>Les conditions sont enfin réunies.</h2></div>
    <ol class="raisons apparait">
      <li><b>01</b><span>Le téléphone est devenu le premier écran, y compris pour les soignants et les enseignants.</span></li>
      <li><b>02</b><span>La reconnaissance vocale et l'IA conversationnelle atteignent une qualité qui les rend utiles en consultation comme en classe.</span></li>
      <li><b>03</b><span>Les systèmes de santé se numérisent et demandent des données interopérables (DHIS2, FHIR).</span></li>
      <li><b>04</b><span>L'enseignement du numérique et de l'IA devient une priorité, alors que la plupart des écoles n'ont pas d'ordinateurs.</span></li>
    </ol>
  </div>
</section>

<section class="fond-2">
  <div class="conteneur deux-col haut">
    <div class="texte apparait">
      <div class="surtitre">Pourquoi nous</div>
      <h2>La santé et l'éducation, sous un même toit.</h2>
    </div>
    <div class="texte apparait">
      <p>Nous réunissons des compétences rarement associées : ingénierie IA, développement hors ligne, normes de santé, pédagogie et électronique. Elles nous permettent d'aller de l'observation du terrain jusqu'au produit en service.</p>
      <p>Nos produits sont conçus pour les contraintes locales dès le départ : <strong>hors ligne, sur mobile, dans les langues des usagers</strong>. C'est ce qui les rend difficiles à copier et faciles à étendre à d'autres pays de la sous-région.</p>
    </div>
  </div>
</section>

<section>
  <div class="conteneur apparait">
    <div class="surtitre">Ce que nous cherchons</div>
    <h2>Des partenaires pour passer du prototype au déploiement.</h2>
    <div class="services-grille trois fond-normal">
      <div class="service"><span class="num">01</span><h3>Sites pilotes</h3><p>Hôpitaux, centres de santé, banques de sang et écoles prêts à tester nos produits en conditions réelles.</p></div>
      <div class="service"><span class="num">02</span><h3>Financement</h3><p>Investisseurs d'impact, subventions et programmes d'appui pour accélérer le développement et la mise à l'échelle.</p></div>
      <div class="service"><span class="num">03</span><h3>Partenaires institutionnels</h3><p>Ministères, programmes nationaux et partenaires techniques pour intégrer nos outils aux systèmes existants.</p></div>
    </div>
    <div class="actions" style="margin-top:40px"><a class="btn btn-plein" href="{lien_contact("Investir")}">Demander le dossier</a><a class="btn btn-contour" href="produits.html">Voir nos produits</a></div>
  </div>
</section>'''
    return page("investir.html", "Investir",
                "Investisseurs et partenaires : où en est M-TK innov, pourquoi maintenant et ce que nous cherchons.",
                contenu, "investir")


def contact():
    options = [("Projet", "Un projet à réaliser"), ("Démo", "Une démonstration de produit"), ("Partenariat", "Un partenariat ou un projet pilote"),
               ("Formation", "Une formation IA ou robotique"), ("Investir", "Investir ou recevoir le dossier"), ("Rejoindre", "Rejoindre l'équipe"), ("Autre", "Autre demande")]
    opts = "".join(f'<option value="{v}">{t}</option>' for v, t in options)
    produits = "".join(f'<option>{p["nom"]}</option>' for p in PRODUITS)
    if CONTACT["email"]:
        aide = "Votre messagerie s'ouvrira avec le message prêt à envoyer."
        canal_email = f'''<a class="canal" href="mailto:{CONTACT["email"]}"><span class="pastille"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></span><div><strong>E-mail</strong><small>{CONTACT["email"]}</small></div></a>'''
    else:
        aide = "Le message sera copié, puis LinkedIn s'ouvrira pour que vous puissiez nous l'envoyer."
        canal_email = ""
    contenu = f'''<div class="page-hero">
  <div class="conteneur">
    <div class="surtitre">Contact</div>
    <h1>Parlons de votre besoin.</h1>
    <p class="intro">Projet, démonstration, partenariat, formation ou investissement : quelques lignes suffisent pour commencer.</p>
  </div>
</div>
<section class="serre">
  <div class="conteneur deux-col haut">
    <form class="formulaire apparait" id="form-contact" data-email="{CONTACT["email"]}" data-linkedin="{CONTACT["linkedin"]}" novalidate>
      <div class="ligne2">
        <label>Nom et prénoms<input name="nom" required autocomplete="name"></label>
        <label>Organisation<input name="organisation" autocomplete="organization" placeholder="Facultatif"></label>
      </div>
      <div class="ligne2">
        <label>Objet<select name="objet" required>{opts}</select></label>
        <label>Produit concerné<select name="produit_concerne"><option value="">Aucun en particulier</option>{produits}</select></label>
      </div>
      <label>Téléphone ou e-mail<input name="coordonnees" required placeholder="Pour vous répondre"></label>
      <label>Message<textarea name="message" required placeholder="Décrivez votre besoin en quelques lignes"></textarea></label>
      <p class="aide">{aide}</p>
      <div><button class="btn btn-plein" type="submit">Préparer le message</button></div>
      <p class="retour" role="status" aria-live="polite"></p>
    </form>
    <div class="canaux apparait">
      {canal_email}
      <a class="canal" href="{CONTACT["linkedin"]}" target="_blank" rel="noopener"><span class="pastille"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4V21H3zM9.5 9.75h3.8v1.6h.06c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.77 2.65 4.77 6.1V21h-4v-4.96c0-1.18-.02-2.7-1.65-2.7-1.65 0-1.9 1.29-1.9 2.62V21h-4z"/></svg></span><div><strong>LinkedIn</strong><small>Message direct au fondateur</small></div></a>
      <a class="canal" href="{CONTACT["github"]}" target="_blank" rel="noopener"><span class="pastille"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.7c-2.78.6-3.37-1.34-3.37-1.34-.45-1.16-1.11-1.47-1.11-1.47-.9-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.9 1.52 2.34 1.08 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.94 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.65 0 0 .84-.27 2.75 1.02a9.56 9.56 0 0 1 5 0c1.91-1.29 2.75-1.02 2.75-1.02.55 1.38.2 2.4.1 2.65.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.68-4.57 4.93.36.31.68.92.68 1.85v2.74c0 .27.18.58.69.48A10 10 0 0 0 12 2z"/></svg></span><div><strong>GitHub</strong><small>Nos dépôts publics</small></div></a>
      <div class="canal"><span class="pastille"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg></span><div><strong>{CONTACT["ville"]}</strong><small>Nous intervenons dans tout le pays et dans la sous-région</small></div></div>
    </div>
  </div>
</section>'''
    return page("contact.html", "Contact",
                "Contacter M-TK innov pour un projet, une démonstration, un partenariat, une formation ou un investissement.",
                contenu, "contact")


def erreur():
    contenu = '''<div class="erreur"><div class="conteneur">
  <strong>404</strong>
  <h2 style="margin-inline:auto">Cette page n'existe pas.</h2>
  <p>Le lien est peut-être ancien ou mal recopié. Les pages principales restent accessibles depuis le menu.</p>
  <div class="actions" style="justify-content:center"><a class="btn btn-plein" href="index.html">Retour à l'accueil</a><a class="btn btn-contour" href="produits.html">Voir nos produits</a></div>
</div></div>'''
    return page("404.html", "Page introuvable", "Cette page n'existe pas.", contenu)


def plan_du_site(fichiers):
    urls = "".join(f"<url><loc>{URL_SITE}/{'' if f == 'index.html' else f}</loc></url>" for f in fichiers if f != "404.html")
    (RACINE / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n', encoding="utf-8")
    (RACINE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {URL_SITE}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    fichiers = [accueil(), catalogue(), services(), mission(), equipe(), investir(), contact(), erreur()]
    fichiers += [page_produit(i, p) for i, p in enumerate(PRODUITS)]
    plan_du_site(fichiers)
    print(f"{len(fichiers)} pages générées : " + ", ".join(fichiers))
