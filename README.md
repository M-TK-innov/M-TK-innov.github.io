# M-TK innov, site web

Site vitrine de M-TK innov (pôles MedTech Innovation et SIKA Education), statique, publié par GitHub Pages.

## Pages

- `index.html` : accueil
- `produits.html` : catalogue filtrable, puis une page par produit (`parledocteur.html`, `bloodlink-229.html`, `paluwatch-ai.html`, `dagbeninon.html`, `baya.html`, `carte-sika.html`, `carte-sika-jeu.html`, `linguabox.html`)
- `services.html`, `mission.html`, `equipe.html`, `investir.html`, `contact.html`, `404.html`

## Modifier le site

Les pages HTML sont générées : ne pas les modifier à la main. Tout le contenu (produits, coordonnées, textes) se trouve dans `outils/build.py`.

```bash
python outils/build.py
```

- Ajouter une adresse e-mail : renseigner `CONTACT["email"]` dans `outils/build.py`. Le formulaire de contact ouvrira alors la messagerie ; sans adresse, il copie le message et ouvre LinkedIn.
- Styles : `css/style.css`. Comportements (menu, filtres, formulaire) : `js/site.js`.
- `sitemap.xml` et `robots.txt` sont régénérés avec les pages (adresse du site : `URL_SITE`).
