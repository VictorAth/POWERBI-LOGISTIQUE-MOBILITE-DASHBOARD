#  Dashboard Logistique & Mobilité – Performance des Courses & Chauffeurs

##  Contexte du Projet
Ce projet s'inscrit dans le cadre de mon portfolio de **Data Analyst**, avec pour objectif de concevoir de bout en bout un pipeline de données orienté vers le secteur de la **logistique urbaine et du transport**. 

L'application simule le suivi opérationnel de courses de chauffeurs/chasseurs urbains, permettant d'analyser le chiffre d'affaires, le volume d'activité, le taux d'annulation et la répartition géographique des courses.

---

##  Architecture & Pipeline de Données
Le projet repose sur une architecture moderne, gratuite et sans installation lourde locale :
1. **Stockage & Base de Données :** PostgreSQL hébergé gratuitement sur **Render**.
2. **Ingestion & Scripting :** Python (via `psycopg2` dans VS Code) pour la création automatisée des tables et l'insertion des données de test.
3. **Modélisation & Business Intelligence :** Connexion directe et modélisation relationnelle dans **Power BI**.

---

##  Modélisation des Données
La base de données (`logistics_fyxa`) s'articule autour de deux tables principales liées par une relation de type **Plusieurs à un (\* : 1)** via la clé étrangère `driver_id` :
* **`drivers` (Chauffeurs) :** Informations sur les chauffeurs (ID, nom, type de véhicule, zone d'intervention).
* **`rides` (Courses) :** Données transactionnelles de chaque course (ID, date, client, lieux de départ/arrivée, distance en km, montant, statut de la course).

---

##  Mesures DAX Clés
Les indicateurs de performance (KPIs) suivants ont été développés sous Power BI pour piloter l'activité :
* **Chiffre d'Affaires Total** = `SUM('public.rides'[fare_amount])`
* **Total Courses** = `COUNT('public.rides'[ride_id])`
* **Courses Réussies** = `CALCULATE([Total Courses], 'public.rides'[ride_status] = "Completed")`
* **Taux d'Annulation (%)** = `DIVIDE(CALCULATE([Total Courses], 'public.rides'[ride_status] = "Cancelled"), [Total Courses], 0)`
* **Distance Totale (km)** = `SUM('public.rides'[distance_km])`
* **Tarif Moyen** = `AVERAGE('public.rides'[fare_amount])`

---

##  Aperçu du Tableau de Bord (Dashboard)
Le rapport Power BI adopte un design professionnel en **thème sombre** et s'articule autour de deux grands blocs :
1. **4 Cartes KPI supérieures :** Chiffre d'affaires total, courses réussies, taux d'annulation et tarif moyen.
2. **4 Graphiques d'analyse :**
   * Répartition du chiffre d'affaires par **Zone géographique** (Barres horizontales).
   * Part des courses par **Type de véhicule** (Moto, Tricycle, Voiture - Graphique en secteurs).
   * **Évolution chronologique** du chiffre d'affaires par date (Graphique linéaire).
   * Filtre interactif par **Nom de chauffeur** pour un suivi individuel.

---

##  Comment lancer le projet ?
1. Cloner le dépôt et ouvrir le dossier dans **VS Code**.
2. Installer le connecteur Python pour PostgreSQL :
   ```bash
   python -m pip install psycopg2-binary

3. Exécuter le script de configuration pour créer et alimenter les tables sur la base distante: 
 ```bash
 python setup_db.py 
```
4. Ouvir POWERBI desktop, se connecter à la base PostgreSQL Render et actualiser les données

Auteur 
Victor ATTOH-AHOIN 
