# Zaawansowana wiedza o PostgreSQL 🧠

## 1. Projektowanie wydajnych baz danych

### 📐 Normalizacja i denormalizacja danych
- Co to jest normalizacja? Kiedy warto ją stosować?
- Zalety i wady denormalizacji.

### 🔑 Klucze główne, obce, unikalne, indeksy — kiedy, jak i dlaczego
- Rola kluczy w integralności danych.
- Typy indeksów w PostgreSQL (B-tree, Hash, GIN, GiST).
- Kiedy używać indeksów, a kiedy nie?

### 🧮 Typy danych PostgreSQL: JSONB, ARRAY, ENUM, UUID, TSVECTOR
- Kiedy korzystać z JSONB zamiast tradycyjnych tabel?
- Zastosowanie typów ENUM i UUID.
- Praktyczne użycie TSVECTOR do pełnotekstowego wyszukiwania.

---

## 2. Pisanie zapytań SQL na wysokim poziomie

### ⚙️ Złożone JOIN-y (INNER, LEFT, FULL, CROSS)
- Różnice między typami JOIN-ów.
- Przykłady zastosowań i optymalizacja.

### 📊 Agregacje (GROUP BY, HAVING, WINDOW FUNCTIONS)
- Zaawansowane agregacje i funkcje okna.
- Przykłady użycia ROW_NUMBER(), RANK(), LEAD(), LAG().

### 🔁 CTE (WITH), rekursywne zapytania
- Budowa i zastosowania CTE.
- Tworzenie rekursywnych zapytań — przykłady.

### 🚀 Optymalizacja zapytań — analiza EXPLAIN ANALYZE
- Jak czytać wynik EXPLAIN ANALYZE?
- Typowe problemy i ich rozwiązania.

---

## 3. Programowanie wewnątrz PostgreSQL

### 📄 Pisanie funkcji i procedur (PL/pgSQL)
- Podstawy PL/pgSQL.
- Tworzenie funkcji z parametrami i zwracanych typów.

### 🔔 Trigger’y — automatyzacja reakcji na zmiany w danych
- Rodzaje triggerów (BEFORE, AFTER, INSTEAD OF).
- Przykłady użycia.

### 💬 Użycie NOTIFY/LISTEN do komunikacji między procesami
- Mechanizm Publish/Subscribe w PostgreSQL.
- Praktyczne zastosowania.

---

## 4. Bezpieczeństwo i dostęp

### 🔒 Role i uprawnienia (GRANT, REVOKE)
- Tworzenie ról i przydzielanie uprawnień.
- Najlepsze praktyki bezpieczeństwa.

### 🛡️ Hasła, SSL, kontrola dostępu do danych
- Konfiguracja SSL dla połączeń.
- Zarządzanie hasłami i uwierzytelnianiem.

---

## 5. Backupy, migracje, monitorowanie

### 💾 pg_dump, pg_restore, pg_basebackup — różnice i zastosowanie
- Kiedy używać każdego narzędzia.
- Przykłady backupów i przywracania.

### 🛠️ Narzędzia jak Flyway, Liquibase do zarządzania migracjami
- Zalety automatycznych migracji.
- Przykładowy workflow migracji.

### 📈 Monitorowanie: pg_stat_statements, pg_activity, Prometheus + Grafana
- Jak monitorować wydajność zapytań.
- Integracja z narzędziami do wizualizacji.

---

## 6. Integracje z innymi systemami

### 🌍 API i frameworki: jak PostgreSQL współgra z np. Django, Spring, Node.js
- Dostępne biblioteki i ORM-y.
- Typowe problemy i rozwiązania.

### 🗂️ Obsługa danych geograficznych z PostGIS (jeśli interesuje Cię GIS)
- Podstawy PostGIS.
- Przykłady zapytań przestrzennych.

---

# Zadania i pytania do samodzielnej nauki

1. Zaprojektuj bazę danych do systemu zarządzania zamówieniami, uwzględniając normalizację.
2. Napisz złożone zapytanie SQL z kilkoma JOIN-ami i funkcjami okna.
3. Stwórz funkcję PL/pgSQL, która automatycznie aktualizuje pole w tabeli po wstawieniu nowego rekordu.
4. Skonfiguruj prosty trigger, który loguje zmiany w tabeli.
5. Zrób backup bazy PostgreSQL i przywróć ją na innym serwerze.
6. Przeanalizuj wynik EXPLAIN ANALYZE dla wybranego zapytania i zoptymalizuj je.
7. Zaimplementuj prostą komunikację między procesami w PostgreSQL za pomocą NOTIFY/LISTEN.
8. Zintegruj prostą aplikację Node.js z bazą PostgreSQL i wykonaj podstawowe operacje CRUD.

---

# Materiały dodatkowe

- [Oficjalna dokumentacja PostgreSQL](https://www.postgresql.org/docs/)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
- [PostGIS Documentation](https://postgis.net/documentation/)
- [Flyway](https://flywaydb.org/)
- [Liquibase](https://www.liquibase.org/)

---

*Ten przewodnik może służyć jako baza do samodzielnej nauki i rozwijania umiejętności PostgreSQL na poziomie zaawansowanym.*


⚙️ Architektura i wydajność systemów
Sharding i partycjonowanie danych (table partitioning, declarative partitioning)

Replikacja (asynchronous/synchronous replication, logical vs physical)

High Availability (HA): Patroni, pgpool-II, streaming replication + failover

Connection pooling: PgBouncer, Odyssey — jak zredukować zużycie zasobów

🧠 PostgreSQL jako silnik analityczny
Materialized views vs zwykłe widoki

Window Functions w praktyce (np. analizy trendów, rankingi)

CUBE, ROLLUP, GROUPING SETS — zaawansowane agregacje

Foreign Data Wrappers (FDW) — dostęp do danych z zewnętrznych źródeł

🧑‍💻 PostgreSQL w systemach rozproszonych
Integracja z narzędziami typu Kafka, RabbitMQ

Obsługa danych temporalnych i czasowych (interwały, strefy czasowe, tsrange)

Replikacja między regionami w chmurze (AWS Aurora PostgreSQL, Azure PG)

📦 PostGIS & GIS (Systemy Geolokalizacji)
Obsługa danych przestrzennych (geometryczne typy danych, geolokalizacja, mapy)

Zastosowania w aplikacjach: mapy interaktywne, analizy tras, geofencing

🧪 Testowanie i debugowanie bazy
Pisanie testów jednostkowych dla funkcji PL/pgSQL

Narzędzia: pg_stat_statements, auto_explain, pgBadger — audyt zapytań

Symulacje awarii, transakcji, deadlocków i ich rozwiązywanie

📈 Monitoring i metryki
Integracje z Prometheus, Grafana

Alarmy na podstawie zapytań/statystyk (np. wolne zapytania, użycie CPU)

Tworzenie dashboardów w czasie rzeczywistym

🤖 Połączenie PostgreSQL z AI/Data Science
Przechowywanie danych ML-ready: NumPy/Pandas → PostgreSQL (COPY, INSERT)

Integracja z Apache Spark, Airflow

Tworzenie pipeline’ów ETL: ekstrakcja → transformacja → ładowanie danych

📌 Złota rada: jeśli chcesz być niezastąpiony — pokaż, że potrafisz nie tylko pisać zapytania SQL, ale zbudować skalowalny, bezpieczny i szybki system danych z PostgreSQL jako fundamentem.