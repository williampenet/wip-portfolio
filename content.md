<!--
WiP — contenu du site
=====================

Ce fichier contient TOUS les textes du site. Modifie-le, puis lance :

    python3 build.py

Règles d'écriture
-----------------
- Une ligne = un champ :   clé: valeur
- `.en` / `.fr` = version anglaise / française. Sans suffixe = identique dans les deux langues.
- Un paragraphe tient sur UNE ligne (aussi long que nécessaire). Pour plusieurs paragraphes,
  répète `text.en:` / `text.fr:` dans l'ordre.
- `|` sépare les éléments d'une liste (tags, facts) ou le retour à la ligne du titre d'accueil.
- Mise en forme : **gras**, [texte du lien](https://adresse), [lien vers une page](page:freelance).
- `{icon}` place la petite icône violette dans une phrase d'intro (voir `icon:`).
- Un texte qui commence par [ ... ] s'affiche en gris italique : c'est un emplacement à remplir.
- Les espaces insécables du français (avant : ; ? ! et dans « ») sont ajoutées automatiquement.
- Logos d'entreprise : `logo: nom-du-fichier | Initiales` → assets/companies/nom-du-fichier.png
  (ou .jpg/.webp/.svg). Tant que le fichier n'existe pas, les initiales s'affichent.
- Captures : `image: screens/fichier.jpg | https://lien-au-clic` → assets/screens/fichier.jpg
- `compact: yes` = carte courte (pas de détail).
- Pour ajouter une mission ou un projet : copie un bloc `## Card` complet et modifie-le.
- Les lignes qui commencent par // sont des commentaires (ignorées).

Icônes disponibles pour `icon:` : scan-text, briefcase, moon, heart-handshake, sprout, hammer
-->

# Home
title.en: William Pénet — Senior Product Builder
title.fr: William Pénet — Senior Product Builder freelance
description.en: William Pénet, Senior Product Builder in freelance. Ten years of product, AI shipped in production, side projects live.
description.fr: William Pénet, Senior Product Builder en freelance. Dix ans de produit, l’IA livrée en production, des projets personnels en ligne.
name: William Pénet
// Le | marque le retour à la ligne ; l'icône marteau se place juste avant.
headline.en: Senior Product Builder | freelance, who builds with AI.
headline.fr: Senior Product Builder | freelance, qui construit avec l’IA.


# About
title.en: About
title.fr: À propos
text.en: Hi.
text.fr: Bonjour.
text.en: I’m a Senior Product Builder. Ten years of product, one mission at a time: a startup (1D Lab), a digital consultancy (Rocket Labs), e-commerce at Stellantis scale ([Mister Auto](https://www.mister-auto.com)), B2B SaaS (Systhen), a data platform ([Interflora](https://www.interflora.fr)) and now streaming ([Bedrock](https://www.bedrockstreaming.com)).
text.fr: Je suis Senior Product Builder. Dix ans de produit, menés mission après mission : une startup (1D Lab), un cabinet digital (Rocket Labs), le e-commerce à l’échelle de Stellantis ([Mister Auto](https://www.mister-auto.com)), le SaaS B2B (Systhen), une plateforme data ([Interflora](https://www.interflora.fr)) et aujourd’hui le streaming ([Bedrock](https://www.bedrockstreaming.com)).
text.en: I came to product by rebounding from one job to the next, picking up marketing, CRM and data on the way. It reads messy on paper and makes sense in a scoping meeting.
text.fr: Je suis arrivé au produit par rebonds, en ramassant marketing, CRM et data en chemin. Sur le papier, le parcours paraît désordonné ; en réunion de cadrage, il prend tout son sens.
text.en: I’m drawn to problems where the hard part is deciding, not building — all the more now that AI has made building cheaper than ever. I work in small steps, let data settle arguments, and stay close enough to the tech to argue about it rather than defer to it.
text.fr: Ce qui m’intéresse, ce sont les problèmes où le plus dur est de décider, pas de construire — d’autant plus maintenant que l’IA a rendu la construction moins chère que jamais. J’avance par petits pas, je laisse les données trancher les débats, et je reste assez près de la technique pour en discuter plutôt que de m’en remettre à elle.
text.en: In my own time, I build the tools I need: [Nightcrawler](https://williampenet.github.io/nightcrawler/) and [SpotiBoard](https://spotiboard.streamlit.app).
text.fr: Sur mon temps libre, je construis les outils dont j’ai besoin : [Nightcrawler](https://williampenet.github.io/nightcrawler/) et [SpotiBoard](https://spotiboard.streamlit.app).
text.en: WiP is my initials. It also stands for Work in Progress. Chasing perfection is the surest way to stop trying: I’d rather ship something honest, see what breaks, and keep going.
text.fr: WiP, ce sont mes initiales. C’est aussi Work in Progress. Courir après la perfection, c’est la meilleure façon d’arrêter d’essayer : je préfère livrer quelque chose d’honnête, voir ce qui casse, et continuer.
text.en: Let’s talk.
text.fr: On en parle ?


# Page: stuff-i-built
title: Stuff I built
icon: hammer
intro.en: Tools I built on my own time {icon}, because I wanted them to exist. Live ones first, work in progress after.
intro.fr: Des outils construits sur mon temps libre {icon}, parce que je voulais qu’ils existent. Ceux en ligne d’abord, les chantiers ensuite.

## Card
tags.en: Live | Solo build
tags.fr: En ligne | Projet solo
title: Nightcrawler
text.en: Concert discovery that reads your taste against venue listings.
text.fr: La découverte de concerts qui lit un goût musical face aux programmations des salles.
text.en: Type in the artists you care about, or connect Spotify and let MusicBrainz fill in the styles. A Mistral model scores each concert and sorts it into Must Not Miss, For You or Discovery. State lives in the browser.
text.fr: On saisit ses artistes, ou on connecte Spotify et MusicBrainz complète les styles. Un modèle Mistral note chaque concert et le range dans Must Not Miss, For You ou Discovery. L’état vit dans le navigateur.
text.en: **Cut on purpose:** ticketing, social features and accounts. It had to be useful on the first visit, with nothing to sign up for.
text.fr: **Coupé volontairement :** billetterie, fonctions sociales et comptes. L’outil devait servir dès la première visite, sans inscription.
small.en: Stack: Mistral, Spotify, MusicBrainz · [williampenet.github.io/nightcrawler](https://williampenet.github.io/nightcrawler/)
small.fr: Outils : Mistral, Spotify, MusicBrainz · [williampenet.github.io/nightcrawler](https://williampenet.github.io/nightcrawler/)
image: screens/nightcrawler.jpg | https://williampenet.github.io/nightcrawler/

## Card
tags.en: Live | Solo build
tags.fr: En ligne | Projet solo
title: SpotiBoard
text.en: 15 years of Spotify history, finally in a dashboard that answers questions.
text.fr: 15 ans d’historique Spotify, enfin dans un tableau de bord qui répond aux questions.
text.en: Spotify Wrapped is a 60-second showreel of one calendar year. I loaded the full export into Supabase, with a Streamlit interface and Plotly charts.
text.fr: Spotify Wrapped, c’est une bande-annonce de 60 secondes sur une année civile. J’ai chargé l’export complet dans Supabase, avec une interface Streamlit et des graphiques Plotly.
text.en: **Cut on purpose:** ranking charts switch themselves off when a filter is active. A Top 10 that silently excludes most of the data is misinformation dressed as a number.
text.fr: **Coupé volontairement :** les classements se désactivent dès qu’un filtre est actif. Un Top 10 qui exclut en silence l’essentiel des données, c’est de la désinformation déguisée en chiffre.
small.en: Stack: Supabase, Streamlit, Plotly, Python · [spotiboard.streamlit.app](https://spotiboard.streamlit.app)
small.fr: Outils : Supabase, Streamlit, Plotly, Python · [spotiboard.streamlit.app](https://spotiboard.streamlit.app)
image: screens/spotiboard.jpg | https://spotiboard.streamlit.app

## Card
compact: yes
tags.en: In progress | Open-source LLM
tags.fr: En cours | LLM open source
title: [Project name — to come]
text.en: [Customizing an open-source LLM: the need, the model chosen, how it is evaluated. To come.]
text.fr: [Personnalisation d’un LLM open source : le besoin, le modèle choisi, son évaluation. À venir.]

## Card
compact: yes
tags.en: Toolkit | Product management
tags.fr: Boîte à outils | Product management
title: PM toolkit
text.en: [The product skills I use, and the ones I wrote. To come.]
text.fr: [Les skills produit que j’utilise, et ceux que j’ai écrits. À venir.]


# Page: freelance
title: Freelance
icon: briefcase
intro.en: Ten years of product {icon}, one mission at a time: startup, e-commerce, B2B SaaS, data, streaming. Most recent first.
intro.fr: Dix ans de produit {icon} menés mission après mission : startup, e-commerce, SaaS B2B, data, streaming. La plus récente d’abord.

## Card
compact: yes
logo: bedrock | B
tags.en: 2025 – now | Streaming
tags.fr: 2025 – aujourd’hui | Streaming
title: Bedrock Streaming
text: Product Manager.

## Card
logo: interflora | I
tags: 2024 – 2025 | Data
title: Interflora
text.en: Data Product Manager. I automated sentiment analysis of 40k+ monthly customer comments with Google Gemini 2.5 Flash.
text.fr: Data Product Manager. J’ai automatisé l’analyse de sentiment de plus de 40 000 commentaires clients par mois avec Google Gemini 2.5 Flash.
text.en: Feedback came in through NPS, Trustpilot, Hotjar, Zendesk and social, in several languages. The CX team tagged it by hand, so insights landed late and read differently from one business unit to the next.
text.fr: Les retours arrivaient par le NPS, Trustpilot, Hotjar, Zendesk et les réseaux, en plusieurs langues. L’équipe CX les classait à la main : les enseignements arrivaient tard et se lisaient différemment d’une BU à l’autre.
text.en: Every comment is classified twice; disagreements go to a human. **I chose to build in-house** so we could change the prompt daily on our own data instead of waiting for a vendor’s roadmap.
text.fr: Chaque commentaire est classé deux fois ; les désaccords remontent à un humain. **J’ai choisi de construire en interne** pour pouvoir modifier le prompt chaque jour sur nos propres données, sans attendre la feuille de route d’un éditeur.
facts.en: 3 analyst-days a month → a few minutes | 95% accuracy on blind evaluation | 40× cheaper than the vendor quote
facts.fr: 3 jours d’analyste par mois → quelques minutes | 95 % de précision en évaluation à l’aveugle | 40× moins cher que le devis de l’éditeur
small.en: Stack: Gemini 2.5 Flash, Python, BigQuery, GCP, Power BI · Internal product, no public link.
small.fr: Outils : Gemini 2.5 Flash, Python, BigQuery, GCP, Power BI · Produit interne, pas de lien public.

## Card
compact: yes
logo: systhen | S
tags.en: 2021 – 2024 | B2B SaaS
tags.fr: 2021 – 2024 | SaaS B2B
title: Systhen
text.en: Group CMO & Product Marketing Manager: digital acquisition, HubSpot, Odoo CRM, 500+ qualified leads a year.
text.fr: Group CMO & Product Marketing Manager : acquisition digitale, HubSpot, Odoo CRM, plus de 500 leads qualifiés par an.

## Card
logo: mister-auto | MA
tags.en: 2019 – 2021 | E-commerce | 21 countries
tags.fr: 2019 – 2021 | E-commerce | 21 pays
title: Mister Auto × Stellantis
text.en: Product Manager & CRO Lead. I rolled out Algolia search across 21 countries and 12 partner sites.
text.fr: Product Manager & CRO Lead. J’ai déployé la recherche Algolia sur 21 pays et 12 sites partenaires.
text.en: Searches kept returning nothing. Not for lack of stock: a pro types a part number, a semi-pro types a brand, a consumer types “front brake pads for my 2008 Clio”. The search bar treated all three the same way.
text.fr: Les recherches ne renvoyaient rien. Pas faute de stock : un pro tape une référence, un semi-pro une marque, un particulier « plaquettes de frein avant pour ma Clio de 2008 ». La barre de recherche traitait les trois de la même façon.
text.en: Multi-attribute indexing, synonyms built from real search logs, continuous A/B testing. **I kept humans in the loop on vocabulary**: technical part names don’t survive machine-made synonyms without someone who knows the trade.
text.fr: Indexation multi-attributs, synonymes construits à partir des vraies recherches, tests A/B en continu. **J’ai gardé des humains dans la boucle sur le vocabulaire** : un nom de pièce technique ne survit pas à un synonyme généré sans quelqu’un qui connaît le métier.
facts.en: +12% conversion | +2–6% CTR depending on country | “No results” pages cut by 65–80%
facts.fr: +12 % de conversion | +2 à 6 % de CTR selon les pays | Pages « aucun résultat » réduites de 65 à 80 %
small.en: Stack: Algolia, AB Tasty, GA, JS
small.fr: Outils : Algolia, AB Tasty, GA, JS

## Card
compact: yes
logo: rocket-labs | RL
tags.en: 2018 – 2019 | Consulting
tags.fr: 2018 – 2019 | Conseil
title: Rocket Labs
text.en: Product Owner consultant on complex B2B projects.
text.fr: Consultant PO sur des projets B2B complexes.

## Card
compact: yes
logo: 1d-lab | 1D
tags: 2015 – 2018 | Startup
title: 1D Lab
text.en: Product Manager: startup foundations, music streaming.
text.fr: Product Manager : les fondations d’une startup, le streaming musical.


# Page: b-sides
title: B-Sides
icon: moon
intro.en: Same brain, own time {icon}. Illustration, music nights and volunteer work. [One sentence on why — to come.]
intro.fr: Même cerveau, temps libre {icon}. Illustration, soirées musicales et bénévolat. [Une phrase sur le sens de ces projets — à venir.]

## Card
compact: yes
logo: mewi | MW
tags.en: [years] | Illustration & publishing
tags.fr: [années] | Illustration et édition
title: MEWI
text.en: An illustration and publishing project I started on the side. [What it makes, my role. To come.]
text.fr: Un projet d’illustration et d’édition lancé à côté. [Ce qu’il produit, mon rôle. À venir.]
small: [mewi.studio](https://mewi.studio/)

## Card
logo: die-pod-die | DP
tags.en: 2014 – 2016 | Lyon · Paris · Montréal
tags.fr: 2014 – 2016 | Lyon · Paris · Montréal
title: DIE POD DIE
text.en: Listening sessions where a full vinyl album is played start to finish on good equipment, for 40 people at most. Each session paired a well-known classic with a lesser-known contemporary record.
text.fr: Des sessions d’écoute où un vinyle est joué en entier sur du bon matériel, devant 40 personnes au plus. Chaque session associait un classique connu à un album contemporain moins connu.
text.en: Started in Lyon in 2014 (Le Périscope, Le Marché Gare), then Paris (Le 104) and Montréal (Centre Phi), for three years. [My role. To come.]
text.fr: Lancé à Lyon en 2014 (Le Périscope, Le Marché Gare), puis Paris (Le 104) et Montréal (Centre Phi), pendant trois ans. [Mon rôle. À venir.]
small: [bazaar-bonzo.ovh/diepoddie](https://bazaar-bonzo.ovh/diepoddie/)

## Card
compact: yes
logo: brrrr-sessions | BS
tags.en: 2011 | Paris | Playlists
tags.fr: 2011 | Paris | Playlists
title: Brrrr Sessions
text.en: A free weekly playlist of about 40 minutes: a side A of standard-length tracks, a side B of long ones, some over 15 minutes. Open to guest selectors.
text.fr: Une playlist hebdomadaire gratuite d’environ 40 minutes : une face A de morceaux au format classique, une face B de titres longs, parfois plus de 15 minutes. Ouverte aux sélections invitées.
small: [bazaar-bonzo.ovh/brrrrsessions](https://bazaar-bonzo.ovh/brrrrsessions/)

## Card
compact: yes
logo: radio-bonzo | RB
tags.en: 2009 – 2010 | New York | Radio
tags.fr: 2009 – 2010 | New York | Radio
title: Radio Bonzo
text.en: A French radio show from New York. [The format, my role. To come.]
text.fr: Une radio française depuis New York. [Le format, mon rôle. À venir.]
small: [bazaar-bonzo.ovh/radiobonzo](https://bazaar-bonzo.ovh/radiobonzo/)

## Card
logo: data-for-good | DG
tags.en: [years] | Volunteer
tags.fr: [années] | Bénévole
title: Data for Good
text.en: [The project, my role, what changed. To come.]
text.fr: [Le projet, mon rôle, ce qui a changé. À venir.]

## Card
logo: time-for-the-planet | TP
tags.en: [years] | Volunteer
tags.fr: [années] | Bénévole
title: Time for the Planet
text.en: [The project, my role, what changed. To come.]
text.fr: [Le projet, mon rôle, ce qui a changé. À venir.]
