---
name: natural-writing
description: Pisze i redaguje teksty (PL i EN) tak, żeby nie miały typowych nawyków prozy generowanej przez LLM: pustych fraz „brzmiących mądrze", kalk („dedykowany", „adresować problem"), przesadnej struktury, trójek, nadmiaru myślników i dwukropków, ogólników bez konkretu, wyważania „z jednej strony… z drugiej" i resztek odpowiedzi chatbota. Używaj ZAWSZE, gdy piszesz dla użytkownika tekst przeznaczony do publikacji lub wysłania (artykuł, wpis blogowy, post na LinkedIn, newsletter, opis usługi lub produktu, stronę www, mail do klienta, ofertę, bio), a także gdy użytkownik prosi o redakcję, korektę, „uczłowieczenie", humanizację, proofreading tekstu AI albo pyta, czy tekst „brzmi jak AI / jak ChatGPT". Trigger też: „napisz naturalnie", „bez AI-owego stylu", „żeby nie było widać, że to AI", „popraw, bo brzmi sztucznie", „sounds like AI", „make it sound human", „remove AI tells", „de-slop".
---

# Natural writing

Ten skill służy do pisania i redagowania tekstów, które robią swoją robotę: mówią coś konkretnego, mają autora i czyta się je bez zgrzytu. Wzorce, po których ludzie rozpoznają tekst z LLM, to w większości stare problemy pisarskie (korpomowa, wata, przeorganizowanie), które modele produkują hurtowo. Usuwamy je dlatego, że osłabiają tekst. To, że zdradzają AI, jest sprawą drugorzędną.

Z tego wynikają dwie zasady:

1. **Celem jest dobry tekst, a nie oszukanie detektora.** Nie dokładaj sztucznych literówek ani „niedoskonałości". Detektory (zwłaszcza dla polskiego) są zawodne, a tekst pisany pod detektor czyta się źle.
2. **Wzorzec to sygnał do sprawdzenia, a nie zakaz.** Lista trzech rzeczy jest w porządku, jeśli rzeczy naprawdę są trzy. Nagłówki są w porządku w dokumentacji i FAQ. Myślnik bywa najlepszym znakiem. Pytanie zawsze brzmi: czy ten zabieg czemuś tu służy?

## Proces

### 1. Zanim zaczniesz pisać

Ustal (z rozmowy albo krótko dopytaj, jeśli brakuje czegoś kluczowego):

- **Kto czyta i jakie ma pytanie.** Tekst ma odpowiadać na konkretne pytanie konkretnej osoby. Początkujący przedsiębiorca i doświadczony konsultant potrzebują innego tekstu.
- **Format i jego zadanie.** Artykuł z tezą potrzebuje napięcia i argumentu, ogłoszenie produktu musi być szybkie, poradnik ma budować wiedzę krok po kroku, dokumentacja ma dać się skanować. Struktura wynika z zadania.
- **Głos autora.** Jeśli użytkownik ma próbki swoich tekstów (lub w repo są teksty pisane ręcznie), przeczytaj 2–3 i zanotuj: długość zdań, rytm, ulubione zwroty, poziom formalności, jak zaczyna i kończy, jak używa interpunkcji. Pisz pod ten wzorzec, a nie pod ogólny „profesjonalny ton".
- **Materiał, którego model nie wymyśli.** Własne obserwacje, liczby, nazwy klientów i projektów, przykłady z praktyki, stanowisko autora. To one sprawiają, że tekst jest czyjś (i dają mu wartość informacyjną). Jeśli ich nie masz, nie zmyślaj (patrz punkt 3).

### 2. Pisanie

Pisz od razu z tymi nawykami:

- **Konkret zamiast kategorii.** Zamiast „ekosystem Ethereum się rozwija" napisz „deweloperzy budują wokół Ethereum coraz więcej portfeli, giełd i rynków pożyczkowych". Zamiast „eksperci uważają" podaj, kto dokładnie, albo stanowisko autora z uzasadnieniem.
- **Autor ma zdanie.** Wybierz stanowisko i je uzasadnij, zamiast balansować dwie strony. Strona czynna, podmiot, który coś robi („przeprowadziłam badanie", nie „zostało przeprowadzone badanie").
- **Uczciwość bez defensywności.** Ograniczenie, które czytelnik musi znać (mała próba, brak testu, cena bez licencji), podaj raz, twierdząco, tam, gdzie ma znaczenie. Nie dopisuj zaprzeczeń twierdzeń, których tekst nie postawił („To nie jest twierdzenie, że…", „Nie pisałbym zatem, że…"). Seria takich zdań brzmi jak odpowiedź na recenzję.
- **Zróżnicowany rytm.** Krótkie zdanie, dłuższe rozwinięcie, krótka puenta. Akapity różnej długości, bo różne myśli mają różną wagę.
- **Proste słowa.** Domyślna proza AI używa wąskiego słownika „bezpiecznych" słów. Wybieraj słowo, które najdokładniej nazywa rzecz, i proste słowa do trudnych tematów.
- **Interpunkcja domyślnie: kropka i przecinek.** Myślnik, dwukropek, średnik i nawias tylko tam, gdzie są gramatycznie potrzebne albo naprawdę robią robotę. Maksymalnie jeden–dwa myślniki w zdaniu, nigdy kilka zdań z rzędu przerwanych wtrąceniem.
- **Wejście od rzeczy.** Pierwsze zdanie to sytuacja, problem, fakt albo teza. Bez rozbiegu o „dzisiejszym dynamicznym świecie" i zapowiedzi „w tym artykule przyjrzymy się".
- **Zakończenie, które coś dodaje.** Wniosek, konsekwencja, następny krok, otwarte pytanie. Bez streszczenia całości i bez morału o przyszłości. Bez sekcji „Podsumowanie" w tekście, który tego nie wymaga.
- **Struktura tylko taka, jakiej treść potrzebuje.** Narrację pisz akapitami. Listę rób wtedy, gdy elementy są naprawdę osobne i równorzędne. Nie pogrubiaj początku każdego punktu. Nie dziel tekstu na nagłówki co trzy akapity.

### 3. Gdy brakuje konkretów, nie zmyślaj

Pokusa przy „uczłowieczaniu" to dopisanie fikcyjnej anegdoty, klienta albo liczby. Nie rób tego: zmyślone doświadczenie jest gorsze od ogólnika, bo autor podpisze się pod nieprawdą. Zamiast tego wstaw widoczny znacznik w miejscu, gdzie tekst potrzebuje materiału od autora:

`[DO UZUPEŁNIENIA: przykład klienta, u którego wdrożenie CRM trwało dłużej niż planowano: ile i dlaczego]`

Po angielsku: `[TO ADD: ...]`. Lepszy tekst z trzema znacznikami niż gładki tekst bez treści.

Tak samo z faktami: jeśli podajesz liczbę, datę, nazwisko, nazwę instytucji, przepis albo „badania pokazują", musisz mieć źródło. Jeśli go nie masz, przepisz zdanie jako opinię autora albo oznacz `[DO WERYFIKACJI: ...]`.

### 4. Przegląd własnego tekstu

Po napisaniu przejdź przez tekst testami poniżej. To najważniejszy etap. Pierwsza wersja zawsze ma trochę „języka pierwszego szkicu" i to normalne. Problem jest dopiero wtedy, gdy na nim kończymy.

**Testy na zdania:**

- **Test parafrazy.** Przy zdaniu, które „brzmi dobrze, ale coś nie gra", spróbuj powiedzieć to samo prościej. Jeśli wychodzi lepiej, zostaw prostszą wersję. Jeśli sprowadza się do „rzeczy istnieją" albo „wszystko się zmienia", usuń zdanie i sprawdź, czy tekst bez niego działa (zwykle działa).
- **Test przeszczepu.** Czy to zdanie dałoby się wyjąć i wkleić bez zmian do innego tekstu, nawet na inny temat? Jeśli tak, jest wymienne. Przepisz je konkretnie albo usuń.
- **Test na głos.** Przeczytaj tekst w myślach jak na głos, traktując interpunkcję jak didaskalia. Miejsca, gdzie autor „tak nie mówi", przepisz.
- **Test „czyj to tekst?".** Czy po pierwszym akapicie wiadomo, kto pisze i co myśli? Czy jest tu coś, czego model nie mógł wygenerować sam?

**Skan wzorców:** sprawdź tekst z katalogiem dla swojego języka:

- polski: [references/patterns-pl.md](references/patterns-pl.md)
- angielski: [references/patterns-en.md](references/patterns-en.md)

Możesz też uruchomić skaner, który wyłapie frazy i metryki rytmu (to szybkie sito, nie wyrocznia):

```bash
python3 scripts/scan_tells.py tekst.md            # język wykrywany automatycznie
python3 scripts/scan_tells.py tekst.md --lang en
cat tekst.md | python3 scripts/scan_tells.py -
```

Każde trafienie oceń w kontekście: popraw, jeśli osłabia tekst; zostaw, jeśli robi robotę.

**Nie przenoś wzorca w inne miejsce.** Typowy błąd redakcji: usunąć wszystkie myślniki i wstawić dwukropki, zostawiając tę samą budowę zdań. Albo zamienić „kluczowy" na „istotny". Popraw zdanie, a nie tylko słowo.

### 5. Co oddajesz

- Sam tekst, gotowy do wklejenia. Bez wstępu w stylu „Oto tekst…" i bez pytania na końcu w stylu „Czy chcesz, żebym przygotował też wersję…?" (to dokładnie ten rodzaj resztek, który zdradza AI, gdy ktoś wklei odpowiedź w całości).
- Pod tekstem, oddzielone wyraźnie (np. linią `---`), krótka notka tylko jeśli jest potrzebna: lista znaczników `[DO UZUPEŁNIENIA]` / `[DO WERYFIKACJI]` i ewentualnie 1–3 zdania o decyzjach, które autor powinien znać.
- Przy redakcji cudzego tekstu: poprawiona wersja, a pod nią krótka lista najważniejszych zmian (kategoriami, nie zdanie po zdaniu), chyba że użytkownik chce inaczej.

## Kiedy NIE wygładzać na siłę

Neutralny, przewidywalny ton jest zaletą tam, gdzie tekst czyta milion obcych osób w milionie kontekstów: dokumentacja, komunikaty błędów, regulaminy, instrukcje bezpieczeństwa, FAQ, odpowiedzi supportu. Tam osobowość przeszkadza. Struktura z nagłówkami i listami jest też właściwa w poradnikach, listicle'ach, materiałach do skanowania i treściach optymalizowanych pod wyszukiwarki i LLM. W branżach regulowanych (finanse, zdrowie, prawo) część zastrzeżeń jest wymagana i musi zostać.

## Redakcja istniejącego tekstu AI (proofreading)

Gdy użytkownik daje gotowy tekst do poprawy, kolejność ma znaczenie. Najpierw treść, potem styl.

1. **Fakty i źródła.** Daty, liczby, nazwiska, instytucje, przepisy, cytaty, linki. Model konfabuluje z pełnym przekonaniem. Czego nie da się potwierdzić, oznacz albo usuń. W tematach zdrowia, prawa, finansów i bezpieczeństwa sprawdź też aktualność.
2. **Ogólniki → konkrety.** „Eksperci", „badania", „firmy coraz częściej" zamień na konkretne źródło albo stanowisko autora.
3. **Doświadczenie.** Wskaż miejsca, gdzie przykład z praktyki autora zrobiłby największą różnicę (znaczniki).
4. **Wzorce AI.** Skan z katalogiem i testami z punktu 4.
5. **Głos.** Czy brzmi jak autor, a nie jak neutralny asystent.
6. **Śmieci techniczne.** Parametry `utm_source=chatgpt.com` (i podobne) w linkach, resztki odpowiedzi chatbota, formatowanie Markdown wklejone tam, gdzie nie działa.

Jeśli tekst ma być publikowany w kontekście, gdzie użycie AI może wymagać ujawnienia (konkurs, przetarg, praca dyplomowa, teksty o sprawach publicznych w świetle art. 50 AI Act), wspomnij o tym autorowi w notce. Decyzja należy do niego.

## Źródła

Katalog wzorców opiera się na:

- a16z crypto, *The habits of AI writing, and what to do about them* (2026): https://x.com/a16zcrypto/status/2091934263302402318
- Katarzyna Baranowska, *Humanizacja tekstu AI*: https://katarzynabaranowska.com/humanizacja-tekstu-ai/
- Katarzyna Baranowska, *Jak zrobić proofreading treści AI*: https://katarzynabaranowska.com/jak-zrobic-proofreading-tresci-ai/
