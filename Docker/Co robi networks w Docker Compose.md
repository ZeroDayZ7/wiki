## Co robi `networks` w Docker Compose?

* Docker Compose pozwala tworzyć własne sieci (networks), na których działają kontenery.
* Sieć pozwala kontenerom się **komunikować** (np. frontend z backendem).
* Domyślnie, jeśli nie zdefiniujesz sieci, Docker Compose tworzy sieć domyślną dla projektu.
* Definiując własną sieć, możesz mieć lepszą kontrolę np. nad izolacją usług.

---

## Przykład z Twojego pliku:

```yaml
networks:
  internal:
    driver: bridge
```

* Tworzysz sieć o nazwie `internal` z typem `bridge`.
* Typ `bridge` to najczęściej używany rodzaj sieci w Dockerze — to wirtualny most, który łączy kontenery na tym samym hoście.
* Kontenery podłączone do `internal` mogą się ze sobą komunikować po nazwach usług (np. kontener `gateway` może pingować `redis`).

---

## Czy można mieć kilka sieci?

Tak, oczywiście! Możesz mieć wiele sieci i podłączać do nich kontenery według potrzeb.

Przykład:

```yaml
networks:
  internal:
    driver: bridge
  public:
    driver: bridge
```

I usługi:

```yaml
services:
  frontend:
    networks:
      - public
  backend:
    networks:
      - internal
      - public
  db:
    networks:
      - internal
```

Tutaj:

* `frontend` jest tylko w sieci `public`.
* `backend` jest w `internal` i `public` — może się komunikować z frontendem i z bazą danych.
* `db` jest tylko w `internal` — izolowana od frontendu.

---

## Kiedy warto mieć kilka sieci?

* Chcesz izolować ruch między usługami (np. front nie ma dostępu do bazy danych bezpośrednio).
* Chcesz mieć osobną sieć dla publicznych i prywatnych usług.
* Masz różne grupy usług, które nie powinny się widzieć.

---

## Podsumowanie:

* `networks` definiują, jak kontenery się komunikują.
* Możesz mieć jedną lub wiele sieci.
* Każdy kontener może być podłączony do kilku sieci.
* Domyślnie jest jedna sieć tworzona przez Compose, ale definiowanie własnych daje więcej kontroli.