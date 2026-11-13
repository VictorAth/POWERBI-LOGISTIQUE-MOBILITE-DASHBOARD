import psycopg2

# Connexion à ta base PostgreSQL sur Render
conn = psycopg2.connect(
    dbname="logistics_fyxa",
    user="logistics_fyxa_user",
    password="GWhnRHz3oA9nPwGeos2yoQ4TvHX5B7ed",
    host="dpg-dbqe02l6e07s73eu96vg-a.oregon-postgres.render.com",
    port="5432"
)
cur = conn.cursor()

# Création des tables et insertion des données
cur.execute("""
CREATE TABLE IF NOT EXISTS drivers (
    driver_id INT PRIMARY KEY,
    driver_name VARCHAR(100),
    vehicle_type VARCHAR(50), 
    zone VARCHAR(50)          
);

CREATE TABLE IF NOT EXISTS rides (
    ride_id INT PRIMARY KEY,
    driver_id INT,
    customer_name VARCHAR(100),
    ride_date DATE,
    pickup_location VARCHAR(50),
    dropoff_location VARCHAR(50),
    distance_km DECIMAL(5,2),
    fare_amount DECIMAL(10,2),
    ride_status VARCHAR(20),    
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id)
);

INSERT INTO drivers VALUES 
(1, 'Kossi Mensah', 'Moto', 'Agoè'),
(2, 'Afiwa Dovi', 'Moto', 'Bè'),
(3, 'Kodjo Assiongbon', 'Voiture', 'Hedzranawoé'),
(4, 'Yaovi Agbégnon', 'Tricycle', 'Adidogomé')
ON CONFLICT DO NOTHING;

INSERT INTO rides VALUES 
(101, 1, 'Marc Kouassi', '2026-11-01', 'Agoè', 'Tokoin', 5.2, 1500.00, 'Completed'),
(102, 2, 'Sarah Kpessou', '2026-11-02', 'Bè', 'Port', 3.1, 1000.00, 'Completed'),
(103, 3, 'Jean Dupont', '2026-11-02', 'Hedzranawoé', 'Aéroport', 8.5, 3500.00, 'Completed'),
(104, 1, 'Aminatou Diallo', '2026-11-03', 'Agoè', 'Kpota', 12.0, 4500.00, 'Cancelled'),
(105, 4, 'Kokou Lawson', '2026-11-03', 'Adidogomé', 'Deckon', 6.4, 2000.00, 'Completed'),
(106, 2, 'Nathalie Vlavonou', '2026-11-04', 'Bè', 'Tokoin', 4.0, 1200.00, 'Completed')
ON CONFLICT DO NOTHING;
""")

conn.commit()
cur.close()
conn.close()
print("Succès : Tables créées et alimentées sur Render !")