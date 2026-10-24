document.documentElement.classList.remove('sans-js');

// Menu mobile
const menuBtn = document.querySelector('.menu-btn');
const menu = document.getElementById('menu');
if (menuBtn && menu) {
  menuBtn.addEventListener('click', () => {
    const ouvert = menu.classList.toggle('ouvert');
    menuBtn.setAttribute('aria-expanded', ouvert);
  });
}

// Sous-menu Produits
document.querySelectorAll('.deroulant').forEach(d => {
  const b = d.querySelector('button');
  const fermer = () => { d.classList.remove('ouvert'); b.setAttribute('aria-expanded', false); };
  b.addEventListener('click', e => {
    e.stopPropagation();
    const ouvert = d.classList.toggle('ouvert');
    b.setAttribute('aria-expanded', ouvert);
  });
  document.addEventListener('click', e => { if (!d.contains(e.target)) fermer(); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') { fermer(); b.focus(); } });
});

// Filtres du catalogue
const boutons = document.querySelectorAll('.filtres button');
boutons.forEach(b => b.addEventListener('click', () => {
  boutons.forEach(x => x.setAttribute('aria-pressed', x === b));
  const f = b.dataset.filtre;
  document.querySelectorAll('.grille .produit').forEach(p => { p.hidden = f !== 'tous' && p.dataset.pole !== f; });
}));

// Apparition au défilement
const elements = document.querySelectorAll('.apparait');
if ('IntersectionObserver' in window) {
  const obs = new IntersectionObserver(entrees => {
    entrees.forEach(e => { if (e.isIntersecting) { e.target.classList.add('vu'); obs.unobserve(e.target); } });
  }, { threshold: .12 });
  elements.forEach(el => obs.observe(el));
} else {
  elements.forEach(el => el.classList.add('vu'));
}

// Formulaire de contact : prépare le message et l'envoie par le canal configuré
const form = document.getElementById('form-contact');
if (form) {
  const params = new URLSearchParams(location.search);
  const sujet = params.get('sujet');
  if (sujet) {
    const select = form.querySelector('[name=objet]');
    const option = [...select.options].find(o => o.value === sujet);
    if (option) select.value = sujet;
  }
  const produit = params.get('produit');
  if (produit) {
    const choix = form.querySelector('[name=produit_concerne]');
    if ([...choix.options].some(o => o.value === produit)) choix.value = produit;
    form.querySelector('[name=message]').value = `Bonjour, je souhaite en savoir plus sur ${produit}.\n\n`;
  }

  form.addEventListener('submit', async e => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    const d = Object.fromEntries(new FormData(form));
    const texte = `${d.produit_concerne ? 'Produit : ' + d.produit_concerne + '\n\n' : ''}${d.message}\n\n${d.nom}${d.organisation ? ', ' + d.organisation : ''}\n${d.coordonnees}`;
    const retour = form.querySelector('.retour');
    const email = form.dataset.email;
    if (email) {
      location.href = `mailto:${email}?subject=${encodeURIComponent('[' + d.objet + '] ' + d.nom)}&body=${encodeURIComponent(texte)}`;
      retour.textContent = 'Votre messagerie va s\'ouvrir avec le message prêt à envoyer.';
      return;
    }
    try { await navigator.clipboard.writeText(`[${d.objet}]\n${texte}`); } catch (_) {}
    retour.textContent = 'Message copié. Collez-le dans la conversation LinkedIn qui vient de s\'ouvrir.';
    window.open(form.dataset.linkedin, '_blank', 'noopener');
  });
}
