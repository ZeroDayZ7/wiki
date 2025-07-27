### 🟢 **GitLab CI/CD – pełne wprowadzenie (od A do Z)**

GitLab CI/CD (Continuous Integration / Continuous Deployment) to **wbudowany w GitLab system automatyzacji**, który pozwala na:

* automatyczne **budowanie**,
* **testowanie**,
* **wdrażanie** (deployment) Twojego kodu,
  za każdym razem, gdy coś zmienisz w repozytorium.

---

## 1️⃣ **Co to właściwie jest?**

* **CI (Continuous Integration)** – ciągła integracja – oznacza, że przy każdym pushu kodu do repozytorium:

  * uruchamiane są testy,
  * sprawdzane są błędy,
  * kod jest budowany.
    Dzięki temu błędy są wychwytywane **wcześnie**, a nie dopiero w produkcji.

* **CD (Continuous Delivery/Deployment)** – ciągłe dostarczanie lub wdrażanie – oznacza, że po pomyślnym zbudowaniu aplikacji można:

  * **automatycznie** wysłać ją na serwer testowy (staging) lub produkcyjny,
  * skrócić czas od developmentu do wdrożenia.

💡 **Czyli GitLab CI/CD to Twój „robot DevOps”, który wykonuje za Ciebie żmudne rzeczy.**

---

## 2️⃣ **Jak to działa?**

### 🔹 Kluczowy element: `.gitlab-ci.yml`

* To plik konfiguracyjny, który umieszczasz w root repozytorium.
* W nim definiujesz **pipeline** – czyli zestaw kroków, jakie mają się wykonać.
* Każdy pipeline składa się z **jobs** (zadań) i **stages** (etapów).

**Przykład prostego pliku:**

```yaml
stages:
  - build
  - test
  - deploy

build-job:
  stage: build
  script:
    - echo "Buduję aplikację..."
    - npm install && npm run build

test-job:
  stage: test
  script:
    - echo "Uruchamiam testy..."
    - npm run test

deploy-job:
  stage: deploy
  script:
    - echo "Wdrażam na serwer..."
    - ./deploy.sh
  only:
    - main
```

---

## 3️⃣ **Główne elementy CI/CD w GitLab**

* **Runner** – agent, który wykonuje Twoje zadania (może być w chmurze GitLaba lub na Twoim serwerze).
* **Pipeline** – zestaw kroków, które mają się wykonać po pushu kodu.
* **Stages** – etapy (np. build → test → deploy).
* **Jobs** – konkretne zadania w danym etapie.
* **Artifacts** – pliki wynikowe (np. paczki aplikacji), które przechodzą między etapami.
* **Variables** – zmienne środowiskowe, np. klucze API, hasła do serwerów.

---

## 4️⃣ **Po co używać GitLab CI/CD?**

✅ **Automatyzacja** – zamiast ręcznie wdrażać aplikację, robisz `git push` i system zajmuje się resztą.
✅ **Większa pewność** – testy uruchamiają się za każdym razem, więc produkcja jest stabilniejsza.
✅ **Szybsze wdrożenia** – brak ręcznej pracy, wdrażasz nawet kilka razy dziennie.
✅ **Standaryzacja** – wszyscy w zespole mają te same procesy.
✅ **Łatwe rollbacki** – w razie problemów szybko możesz przywrócić poprzednią wersję.

---

## 5️⃣ **Kiedy tego używać?**

* Zawsze, gdy masz **zespół programistów** – CI/CD minimalizuje konflikty w kodzie.
* Gdy **wdrażasz aplikację często** – np. SaaS, API, aplikacje webowe.
* Przy projektach z testami automatycznymi – testy uruchamiają się automatycznie.
* Nawet w małych projektach – oszczędza czas przy deployach.

---

## 6️⃣ **Jak zacząć? (Krok po kroku)**

1. **Stwórz projekt na GitLabie** (lub użyj istniejącego).
2. **Dodaj plik `.gitlab-ci.yml`** do repozytorium.
3. **Skonfiguruj GitLab Runnera** – możesz użyć:

   * **shared runners** (darmowe, udostępnione przez GitLab, ale mają limity),
   * **self-hosted runner** (Twój serwer/VPS – pełna kontrola).
4. **Zdefiniuj pipeline** w YAML-u (build → test → deploy).
5. **Zrób `git push`** – GitLab sam wykona pipeline.
6. **Monitoruj pipeline** w zakładce *CI/CD* w projekcie.

---

## 7️⃣ **Przykład: Next.js + Express + Docker + GitLab CI/CD**

Jeżeli masz aplikację Next.js + Express i chcesz, aby pipeline:

* zbudował aplikację,
* spakował ją w Dockera,
* wdrożył na VPS,

Twój `.gitlab-ci.yml` może wyglądać np. tak:

```yaml
stages:
  - build
  - deploy

build:
  stage: build
  image: node:22
  script:
    - npm install
    - npm run build
  artifacts:
    paths:
      - .next

docker-build:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -t myapp:latest .
    - docker save myapp:latest > myapp.tar
  artifacts:
    paths:
      - myapp.tar

deploy:
  stage: deploy
  script:
    - scp myapp.tar user@server:/home/user/
    - ssh user@server "docker load -i myapp.tar && docker-compose up -d"
  only:
    - main
```

---

## 8️⃣ **Gdzie GitLab CI/CD jest używany w praktyce?**

* 🌍 **W dużych firmach** – Netflix, Airbus, CERN korzystają z CI/CD do wdrożeń.
* 🚀 **W projektach open-source** – automatyczne testy PR-ów.
* 👨‍💻 **W startupach** – szybkie wdrażanie MVP i aktualizacji.
* 🏛 **W administracji publicznej** – automatyczne aktualizacje systemów.

---

## 9️⃣ **Najczęstsze pułapki i dobre praktyki**

❌ Nie wrzucaj haseł do repozytorium – używaj **CI/CD Variables**.
❌ Nie testuj tylko lokalnie – pipeline powinien robić to za Ciebie.
✅ Dodaj **linting i testy jednostkowe** – szybciej łapiesz błędy.
✅ Rozdziel środowiska (dev, staging, production).
✅ Monitoruj pipeline – jeśli coś się psuje, pipeline powie Ci gdzie.

---

## 🔟 **Podsumowanie**

GitLab CI/CD to **potężne narzędzie**, które pozwala:

* automatyzować proces developmentu,
* szybciej dostarczać aplikacje,
* zmniejszać ryzyko błędów.

Dzięki prostemu plikowi `.gitlab-ci.yml` możesz w kilka godzin zbudować profesjonalny proces DevOps – bez dodatkowych serwerów CI jak Jenkins.