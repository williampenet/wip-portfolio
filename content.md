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
- Mise en forme : **gras**, [texte du lien](https://adresse), [lien vers une page](page:career).
- `{icon}` place la petite icône violette dans une phrase d'intro (voir `icon:`).
- `{logo:python|Python}` place le logo d'un outil, dans sa couleur, collé à son nom (fichiers dans assets/tools/, issus de Simple Icons).
- Un texte qui commence par [ ... ] s'affiche en gris italique : c'est un emplacement à remplir.
- Les espaces insécables du français (avant : ; ? ! et dans « ») sont ajoutées automatiquement.
- Logos d'entreprise : `logo: nom-du-fichier | Initiales` → assets/companies/nom-du-fichier.png
  (ou .jpg/.webp/.svg). Tant que le fichier n'existe pas, les initiales s'affichent.
- Captures : `image: screens/fichier.jpg | https://lien-au-clic` → assets/screens/fichier.jpg
- `compact: yes` = carte courte (pas de détail).
- `small:` (petit texte gris) peut être répété : chaque `small.en` / `small.fr` fait une ligne à part.
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
// Un | dans le titre marque un retour à la ligne (facultatif).
headline.en: Freelancing Senior Product Builder
headline.fr: Product Builder Senior freelance


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
text.en: WiP is my initials. It also stands for Work in Progress. Chasing perfection is the surest way to stop trying: I’d rather ship something honest, see what breaks, and keep going. A mistake is information — it’s the whole idea behind [MEWI](https://mewi.studio/), my side project on the words children get wrong.
text.fr: WiP, ce sont mes initiales. C’est aussi Work in Progress. Courir après la perfection, c’est la meilleure façon d’arrêter d’essayer : je préfère livrer quelque chose d’honnête, voir ce qui casse, et continuer. Une erreur, c’est de l’information : c’est toute l’idée de [MEWI](https://mewi.studio/), mon projet sur les mots que les enfants déforment.
text.en: Let’s talk.
text.fr: On en parle ?


# Page: stuff-i-built
title: Stuff I built
icon: hammer
intro.en: Tools I built on my own time {icon}, because I wanted them to exist.
intro.fr: Des outils construits sur mon temps libre {icon}, parce que je voulais qu’ils existent.

## Card
tags.en: Live | Solo build | AI
tags.fr: En ligne | Projet solo | IA
title: Nightcrawler
text.en: I never took the time to go through every venue’s listings in Lyon and around, and I kept missing artists I really wanted to see live.
text.fr: Je ne prenais pas le temps de parcourir la programmation de toutes les salles de Lyon et des environs, et j’ai raté plusieurs fois des artistes que je voulais absolument voir en concert.
text.en: So I built a personal concert recommender fed by my own taste: the artists from my Spotify account, plus a like / not-for-me button on every concert. A Mistral model scores each concert and sorts it into Must Not Miss, For You or Discovery, with a one-line reason.
text.fr: J’ai donc construit une app perso de recommandation de concerts, nourrie par mes goûts : les artistes de mon compte Spotify et un bouton « j’aime / pas pour moi » sur chaque concert. Un modèle Mistral note chaque concert et le range dans Must Not Miss, For You ou Discovery, avec une raison en une phrase.
small.en: Stack: {logo:python|Python} pipeline run daily on {logo:githubactions|GitHub Actions}, reading venue websites, {logo:openstreetmap|OpenStreetMap} and Ticketmaster · {logo:mistralai|Mistral Small 3.2} for taste and Gemma 4 for agenda pages, both on {logo:scaleway|Scaleway} in Paris · serverless {logo:postgresql|PostgreSQL} on Scaleway for likes and verdicts · static web app on {logo:github|GitHub Pages}
small.en: [Live](https://williampenet.github.io/nightcrawler/) · [GitHub](https://github.com/williampenet/nightcrawler)
small.fr: Outils : pipeline {logo:python|Python} lancé chaque jour par {logo:githubactions|GitHub Actions}, qui lit les sites des salles, {logo:openstreetmap|OpenStreetMap} et Ticketmaster · {logo:mistralai|Mistral Small 3.2} pour le goût et Gemma 4 pour les pages d’agenda, tous deux chez {logo:scaleway|Scaleway} à Paris · {logo:postgresql|PostgreSQL} serverless chez Scaleway pour les avis et les verdicts · app web statique sur {logo:github|GitHub Pages}
small.fr: [En ligne](https://williampenet.github.io/nightcrawler/) · [GitHub](https://github.com/williampenet/nightcrawler)
image: screens/nightcrawler.jpg | https://williampenet.github.io/nightcrawler/

## Card
tags.en: Live | Solo build
tags.fr: En ligne | Projet solo
title: SpotiBoard
text.en: I wanted a project to practise API calls and see what Streamlit can do. I was also curious about what 15 years of Spotify listening would say about me.
text.fr: Je cherchais un projet pour m’exercer aux appels d’API et tester ce que Streamlit permet de faire. J’étais aussi curieux de voir ce que 15 ans d’écoute Spotify diraient de moi.
text.en: So I built this dashboard, before Spotify started showing similar all-time stats in its own app.
text.fr: J’ai donc construit ce tableau de bord, avant que Spotify ne propose des statistiques similaires dans sa propre app.
small.en: Stack: full {logo:spotify|Spotify} data export loaded into {logo:supabase|Supabase} ({logo:postgresql|PostgreSQL}), recent plays synced from the Spotify API with {logo:n8n|n8n} · {logo:streamlit|Streamlit} dashboard with {logo:pandas|pandas} and {logo:plotly|Plotly}, hosted on Streamlit Community Cloud
small.en: [Live](https://spotiboard.streamlit.app) · [GitHub](https://github.com/williampenet/spotiboard)
small.fr: Outils : export complet des données {logo:spotify|Spotify} chargé dans {logo:supabase|Supabase} ({logo:postgresql|PostgreSQL}), écoutes récentes synchronisées depuis l’API Spotify avec {logo:n8n|n8n} · tableau de bord {logo:streamlit|Streamlit} avec {logo:pandas|pandas} et {logo:plotly|Plotly}, hébergé sur Streamlit Community Cloud
small.fr: [En ligne](https://spotiboard.streamlit.app) · [GitHub](https://github.com/williampenet/spotiboard)
image: screens/spotiboard.jpg | https://spotiboard.streamlit.app

## Card
tags.en: Toolkit | Product | Design
tags.fr: Boîte à outils | Produit | Design
title: Toolkit
text.en: {logo:github|**[Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills)**} by Dean Peters: to separate what a client asks for from what they actually need, prepare discovery interviews and pick the cheapest probe before building anything.
text.fr: {logo:github|**[Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills)**} de Dean Peters : pour distinguer ce qu’un client demande de ce dont il a vraiment besoin, préparer les entretiens de discovery et choisir le test le moins coûteux avant de construire quoi que ce soit.
text.en: {logo:github|**[PM Skills](https://github.com/phuryn/pm-skills)**} by Paweł Huryn: to red-team an idea that looks too good, rank the assumptions it rests on and map what we learn into an opportunity solution tree.
text.fr: {logo:github|**[PM Skills](https://github.com/phuryn/pm-skills)**} de Paweł Huryn : pour attaquer une idée trop séduisante, classer les hypothèses sur lesquelles elle repose et ranger ce qu’on apprend dans un opportunity solution tree.
text.en: {logo:tastecode|**[TasteCode](https://tastecode.dev/)**}: the desktop home for my coding agents, with a Design Mode that takes a page from brief to a reviewed live preview at every screen size.
text.fr: {logo:tastecode|**[TasteCode](https://tastecode.dev/)**} : l’espace de travail de mes agents de code, avec un Design Mode qui mène une page du brief à un aperçu en ligne relu, à toutes les tailles d’écran.
text.en: {logo:impeccable|**[Impeccable](https://github.com/pbakaus/impeccable)**}: a shared design vocabulary for my agents (critique, audit, polish) that catches the usual tells of AI-made interfaces before they ship. This site was shaped with both.
text.fr: {logo:impeccable|**[Impeccable](https://github.com/pbakaus/impeccable)**} : un vocabulaire de design commun avec mes agents (critique, audit, polish), qui repère les tics des interfaces faites par IA avant la mise en ligne. Ce site a été travaillé avec les deux.


# Page: career
title: Career
icon: briefcase
intro.en: Over ten years in product {icon}, now focused on data and CRM integration: making customer data flow between systems, both ways and in real time. Most recent first.
intro.fr: Plus de dix ans de produit {icon}, aujourd’hui centrés sur la data et l’intégration CRM : faire circuler les données clients entre les systèmes, dans les deux sens et en temps réel. Du plus récent au plus ancien.

## Card
compact: yes
logo: bedrock | B
tags.en: 2025 – now | Video streaming
tags.fr: 2025 – aujourd’hui | Streaming vidéo
title: Bedrock Streaming
text: Freelance Senior Product Manager
text.en: I lead the two-way integration between our broadcaster clients’ CRMs and the streaming platform, from defining the use cases to setting up real-time data feeds.
text.fr: Je pilote l’intégration bidirectionnelle entre les CRM de nos clients diffuseurs et la plateforme de streaming, de la définition des cas d’usage à la mise en place des flux de données en temps réel.
small.en: Product stack: {logo:claude|Claude}, {logo:apachesuperset|Superset}, {logo:atlassian|Atlassian}, Airship, Braze, Salesforce Marketing Cloud
small.fr: Outils produit : {logo:claude|Claude}, {logo:apachesuperset|Superset}, {logo:atlassian|Atlassian}, Airship, Braze, Salesforce Marketing Cloud

## Card
logo: interflora | I
tags.en: 2024 – 2025 | Retail
tags.fr: 2024 – 2025 | eCommerce
title: Interflora
text: Data Product Manager
text.en: I automated sentiment analysis of 40k+ monthly customer comments with Google Gemini 2.5 Flash.
text.fr: J’ai automatisé l’analyse de sentiment de plus de 40 000 commentaires clients par mois avec Google Gemini 2.5 Flash.
text.en: Feedback came in through NPS, {logo:trustpilot|Trustpilot}, {logo:hotjar|Hotjar}, {logo:zendesk|Zendesk} and social, in several languages. The CX team tagged it by hand, so insights landed late and read differently from one business unit to the next.
text.fr: Les retours arrivaient par le NPS, {logo:trustpilot|Trustpilot}, {logo:hotjar|Hotjar}, {logo:zendesk|Zendesk} et les réseaux, en plusieurs langues. L’équipe CX les classait à la main : les enseignements arrivaient tard et se lisaient différemment d’une BU à l’autre.
text.en: Every comment is classified twice; disagreements go to a human. **I chose to build in-house** so we could change the prompt daily on our own data instead of waiting for a vendor’s roadmap.
text.fr: Chaque commentaire est classé deux fois ; les désaccords remontent à un humain. **J’ai choisi de construire en interne** pour pouvoir modifier le prompt chaque jour sur nos propres données, sans attendre la feuille de route d’un éditeur.
facts.en: 3 analyst-days a month → a few minutes | 95% accuracy on blind evaluation | 40× cheaper than the vendor quote
facts.fr: 3 jours d’analyste par mois → quelques minutes | 95 % de précision en évaluation à l’aveugle | 40× moins cher que le devis de l’éditeur
small.en: Stack: {logo:googlegemini|Gemini 2.5 Flash}, {logo:python|Python}, {logo:googlebigquery|BigQuery}, {logo:googlecloud|GCP}, Power BI · Internal product, no public link.
small.fr: Outils : {logo:googlegemini|Gemini 2.5 Flash}, {logo:python|Python}, {logo:googlebigquery|BigQuery}, {logo:googlecloud|GCP}, Power BI · Produit interne, pas de lien public.

## Card
compact: yes
logo: systhen | S
tags.en: 2021 – 2024 | B2B SaaS
tags.fr: 2021 – 2024 | SaaS B2B
title: Systhen
text: Digital Marketing Manager
text.en: I joined to gain marketing experience, and designed and ran the whole digital marketing engine that took this SME from zero to 500+ qualified leads a year.
text.fr: Je suis venu y chercher une expérience en marketing, et j’ai conçu et animé toute la machine de marketing digital qui a fait passer cette PME de zéro à plus de 500 leads qualifiés par an.
small.en: Stack: {logo:hubspot|HubSpot}, Odoo CRM, LinkedIn Sales Navigator, Lemlist
small.fr: Outils : {logo:hubspot|HubSpot}, Odoo CRM, LinkedIn Sales Navigator, Lemlist

## Card
logo: mister-auto | MA
tags.en: 2019 – 2021 | eCommerce
tags.fr: 2019 – 2021 | eCommerce
title: Mister Auto × Stellantis
text: Product Manager & CRO Lead
text.en: I rolled out Algolia search across 21 countries and 12 partner sites.
text.fr: J’ai déployé la recherche Algolia sur 21 pays et 12 sites partenaires.
text.en: Searches kept returning nothing. Not for lack of stock: a pro types a part number, a semi-pro types a brand, a consumer types “front brake pads for my 2008 Clio”. The search bar treated all three the same way.
text.fr: Les recherches ne renvoyaient rien. Pas faute de stock : un pro tape une référence, un semi-pro une marque, un particulier « plaquettes de frein avant pour ma Clio de 2008 ». La barre de recherche traitait les trois de la même façon.
text.en: Multi-attribute indexing, synonyms built from real search logs, continuous A/B testing. **I kept humans in the loop on vocabulary**: technical part names don’t survive machine-made synonyms without someone who knows the trade.
text.fr: Indexation multi-attributs, synonymes construits à partir des vraies recherches, tests A/B en continu. **J’ai gardé des humains dans la boucle sur le vocabulaire** : un nom de pièce technique ne survit pas à un synonyme généré sans quelqu’un qui connaît le métier.
facts.en: +12% conversion | +2–6% CTR depending on country | “No results” pages cut by 65–80%
facts.fr: +12 % de conversion | +2 à 6 % de CTR selon les pays | Pages « aucun résultat » réduites de 65 à 80 %
small.en: Stack: {logo:algolia|Algolia}, AB Tasty, {logo:googleanalytics|GA}, {logo:javascript|JS}
small.fr: Outils : {logo:algolia|Algolia}, AB Tasty, {logo:googleanalytics|GA}, {logo:javascript|JS}

## Card
compact: yes
logo: rocket-labs | RL
tags.en: 2018 – 2019 | Consulting
tags.fr: 2018 – 2019 | Conseil
title: Rocket Labs
text.en: Product Owner consultant
text.fr: Consultant Product Owner
text.en: Complex B2B projects for Airbus Helicopters, Crédit Agricole and RATP.
text.fr: Des projets B2B complexes pour Airbus Helicopters, le Crédit Agricole et la RATP.

## Card
compact: yes
logo: 1d-lab | 1D
tags.en: 2015 – 2018 | Startup | Music streaming
tags.fr: 2015 – 2018 | Startup | Streaming musical
title: 1D Lab
text.en: First Product Manager
text.fr: Premier Product Manager
text.en: A startup set on overturning how independent musicians get paid, with a dedicated streaming platform and a fairer business model.
text.fr: Une startup qui entendait bouleverser la rémunération des artistes indépendants, avec une plateforme de streaming dédiée et un modèle économique plus équitable.


# Page: b-sides
title: B-Sides
icon: moon
intro.en: WiP applies to my own time too {icon}! Here’s a glimpse of the B-Sides projects I’m working on, or have worked on.
intro.fr: WiP s’applique aussi à mon temps libre {icon} ! Voici un aperçu des projets B-Sides sur lesquels je travaille, ou j’ai travaillé.

## Card
compact: yes
logo: mewi | MW
tags.en: 2024 – now | Stories, games, objects
tags.fr: 2024 – aujourd’hui | Récits, jeux, objets
title: MEWI
text.en: When children learn to speak, their mistakes are often better than the right words. MEWI collects them and turns them into stories, games and objects. The idea behind it: a mistake, taken the right way, gives more than it costs. **Founder.**
text.fr: Quand les enfants apprennent à parler, leurs erreurs sont souvent plus belles que les vrais mots. MEWI les recueille et en fait des récits, des jeux et des objets. L’idée de fond : une erreur, prise par le bon bout, rapporte plus qu’elle ne coûte. **Fondateur.**
small: [mewi.studio](https://mewi.studio/)

## Card
logo: data-for-good | DG
tags.en: 2024 – now | Volunteer
tags.fr: 2024 – aujourd’hui | Bénévole
title: Data for Good
text.en: Volunteer product manager for two years. In 2026 I’m working on an electoral mapping project that helps associations and movements bring persistent non-voters back to the polls.
text.fr: Product manager bénévole depuis deux ans. En 2026, je travaille sur un projet de cartographie électorale qui aide les associations et les mouvements à faire revenir aux urnes les populations abstentionnistes.

## Card
logo: time-for-the-planet | TP
tags.en: 2023 – now | Volunteer
tags.fr: 2023 – aujourd’hui | Bénévole
title: Time for the Planet
text.en: An international initiative that finds and invests in companies whose work should cut CO₂ emissions. I’m one of the reviewers of the hundreds of applications it receives every year.
text.fr: Une initiative internationale qui repère des entreprises dont l’activité doit réduire les émissions de CO₂ et investit dans elles. Je fais partie des évaluateurs des centaines de candidatures reçues chaque année.

## Card
logo: die-pod-die | DP
tags.en: 2014 – 2016 | Lyon · Paris · Montréal
tags.fr: 2014 – 2016 | Lyon · Paris · Montréal
title: DIE POD DIE
text.en: In the shuffle-and-skip years of the iPod, I asked people to do the opposite: sit down and do nothing but listen, for two 40-minute stretches. Each session played a well-known classic and a lesser-known contemporary album in full on vinyl, on good equipment, for 40 people at most. Vinyl listening bars have made this common since; back then it was an odd idea.
text.fr: À l’époque du zapping et de l’iPod Shuffle, je demandais aux gens l’inverse : s’asseoir et ne rien faire d’autre qu’écouter, deux fois quarante minutes. Chaque session faisait entendre en entier, sur vinyle et sur du bon matériel, un classique connu et un album contemporain moins connu, devant 40 personnes au plus. Les bars d’écoute ont depuis rendu la pratique courante ; à l’époque, l’idée était insolite.
text.en: Guests included Brigitte Fontaine and Areski Belkacem, Arthur H, Lee Ranaldo and Étienne Jaumet.
text.fr: Parmi les invités : Brigitte Fontaine et Areski Belkacem, Arthur H, Lee Ranaldo et Étienne Jaumet.
text.en: Started in Lyon in 2014 (Le Périscope, Le Marché Gare), then Paris (Le 104) and Montréal (Centre Phi), for three years. **Founder and host.**
text.fr: Lancé à Lyon en 2014 (Le Périscope, Le Marché Gare), puis Paris (Le 104) et Montréal (Centre Phi), pendant trois ans. **Fondateur et animateur.**
small: [bazaar-bonzo.ovh/diepoddie](https://bazaar-bonzo.ovh/diepoddie/)
