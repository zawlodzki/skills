#!/usr/bin/env python3
"""Skaner typowych nawyków prozy generowanej przez LLM (PL i EN).

Wyłapuje frazy z katalogu (references/patterns-*.md) oraz proste metryki rytmu
i interpunkcji. Wynik to lista miejsc do obejrzenia, nie werdykt "AI / nie AI".

Użycie:
    python3 scan_tells.py plik.md [--lang pl|en|auto] [--json]
    cat plik.md | python3 scan_tells.py -
"""

import argparse
import json
import re
import statistics
import sys

# (kategoria, regex, podpowiedź). Regexy są kompilowane z IGNORECASE.
PATTERNS_PL = [
    ("otwarcie", r"w dzisiejszym\s+\w+\s+świecie|w dzisiejszych czasach|w obecnej rzeczywistości|w erze\s+\w+", "Zacznij od konkretu, nie od tła epoki."),
    ("otwarcie", r"w tym (artykule|wpisie|tekście|poradniku)\s+(przyjrzymy|omówimy|dowiesz|pokażę|przedstawi)", "Usuń zapowiedź treści."),
    ("otwarcie", r"\brewolucjonizuj\w*|zmienia zasady gry", "Napisz, co konkretnie się zmienia."),
    ("otwarcie", r"firmy coraz częściej", "Które firmy? Skąd wiesz?"),
    ("wypełniacz", r"warto (podkreślić|zaznaczyć|pamiętać|zauważyć|wspomnieć|dodać)", "Wytnij ramkę, zostaw informację."),
    ("wypełniacz", r"należy (podkreślić|zaznaczyć|pamiętać|zauważyć)", "Wytnij ramkę, zostaw informację."),
    ("wypełniacz", r"kluczowe jest|nie można zapomnieć|jest to szczególnie istotne|szczególnie istotne w kontekście", "Pokaż ważność treścią."),
    ("wypełniacz", r"stawka (nigdy nie była|jest) (wyższa|wysoka)|dzieje się coś (ważnego|wielkiego)", "Pseudo-głębia: co się dzieje?"),
    ("kontrast", r"nie tylko\b[^.!?\n]{1,80}\b(ale|lecz)( także| również| też)?", "Pusty kontrast? Spróbuj od razu powiedzieć drugą część."),
    ("kontrast", r"\bto nie\s+\w+[^.!?\n]{0,40}[,.–—-]\s*to\s+\w+|nie chodzi o\b[^.!?\n]{1,60}chodzi o", "„To nie X, to Y” — czy X jest potrzebne?"),
    ("klucz do", r"(to|jest) klucz(em)? do|odgrywa\w* (kluczową|istotną|ważną|znaczącą) rolę", "Opisz mechanizm zamiast „klucza”."),
    ("pseudo-dane", r"na podstawie dostępnych danych|badania (pokazują|wskazują|dowodzą)|eksperci (uważają|twierdzą|podkreślają|zgodnie)", "Podaj źródło albo zrób z tego opinię autora."),
    ("łącznik", r"(^|[.!?]\s+)(ponadto|dodatkowo|co więcej|jednocześnie|niemniej jednak)\b", "Łącznik-wata na początku zdania."),
    ("asekuracja", r"w pewnym sensie|w wielu przypadkach|do pewnego stopnia|można argumentować", "Asekuracja — potrzebna?"),
    ("podsumowanie", r"koniec końców|w gruncie rzeczy|na koniec dnia|(^|[.!?]\s+)podsumowując\b", "Zwykle do skreślenia."),
    ("przymiotnik", r"\b(kompleksow|holistyczn|innowacyjn|przełomow|dynamiczn|wszechstronn|unikaln|kluczow)\w*", "Pusty przymiotnik? Pokaż cechę."),
    ("kalka", r"\bdedykowan\w*", "„Dedykowany” = przeznaczony dla."),
    ("kalka", r"\badresow\w*\s+(problem|wyzwani|potrzeb|kwesti)\w*", "Rozwiązywać / zajmować się."),
    ("kalka", r"dostarcz\w*\s+(wartoś\w*|wartość)", "Napisz, co konkretnie daje."),
    ("kalka", r"\bnawigow\w*|odblokow\w*\s+(potencjał|możliwoś)\w*|robi\w* różnicę|lewarow\w*", "Kalka z angielskiego."),
    ("mgła", r"\b(ekosystem|krajobraz|synergi|transformacj)\w*", "Rzeczownik-mgła — co konkretnie?"),
    ("mgła", r"\bpodróż\w*\s+(klienta|użytkownika|transformacj|cyfrow)\w*", "„Podróż” — co konkretnie?"),
    ("pozorny ruch", r"\b(napędza|kształtuj|wzmacnia|usprawnia|redefiniuj)\w*|na wyższy poziom", "Czasownik pozornego ruchu."),
    ("latarnia", r"jest świadectwem|stanowi dowód|przypomina nam|stanowi fundament|nieodłączn\w* element", "Powiedz wprost."),
    ("wzmacniacz", r"(bardzo|niezwykle|szczególnie) (ważn|istotn)\w*|znacząc\w* wpływ|ogromne znaczenie|istotn\w* rol\w*", "Wzmacniacz bez danych."),
    ("balans", r"z jednej strony", "Brak stanowiska?"),
    ("drogowskaz", r"przyjrzyjmy się|rozłóżmy (to|go|je)|\bpo pierwsze\b|istnieją trzy|oto (trzy|pięć|kilka)\b", "Drogowskaz / zapowiedź sekcji."),
    ("zakończenie", r"mam nadzieję, że (ten|ta|to|powyższ)|zostaw komentarz|niezależnie od tego, czy|(^|[.!?]\s+)pamiętaj, że", "Szablonowe zakończenie."),
    ("zastrzeżenie", r"bez twierdzenia,? że|to nie jest twierdzenie|nie twierdzę,? że|nie oznacza(,)? to,? że|to nie oznacza,? że|(^|[.!?]\s+)nie oznacza,? że|nie mam (badania|badań|podstaw|danych),? (które|żeby|by)|bez obietnicy|nie jest (to )?(obietnicą|gwarancją|cennikiem|harmonogramem)|nie (pisał|traktował|używał|nazywał|szukał)(bym|abym)\b|różnica nie polega|nie będę udawać|to (tylko )?(ilustracja|opis możliwości|proponowany pilot)|nie należy (tego )?(traktować|rozumieć) jako|nie chodzi (mi )?o to,? że", "Zastrzeżenie przed zarzutem, którego nikt nie postawił? Podaj ograniczenie raz, twierdząco, albo usuń."),
    ("ciepło", r"świetne pytanie|doskonałe pytanie|doskonale rozumiem", "Ciepło z poczekalni."),
    ("resztki czatu", r"czy chcesz, (żebym|abym)|mogę (też|również) przygotować|oto (propozycja|przykładow|gotow)\w*|jasne! poniżej|jako model językowy", "Resztka odpowiedzi chatbota."),
]

PATTERNS_EN = [
    ("opening", r"in today'?s\s+([\w-]+\s+){0,2}(world|landscape|age|era)|in the ever[- ]evolving", "Open with something concrete."),
    ("opening", r"we'?re (excited|thrilled|delighted) to (announce|share)|inflection point|next chapter of our", "Corporate filler."),
    ("profundity", r"something (real|big|important) is happening|stakes (couldn'?t|could not) be higher|implications are (significant|profound)|this matters for", "Faux profundity: say what is happening."),
    ("contrast", r"\bnot (just|only|merely)\b[^.!?\n]{1,80}\b(but|it'?s)\b|\bisn'?t (just )?about\b[^.!?\n]{1,60}it'?s about", "Empty contrast? Lead with Y."),
    ("hedge", r"\bin many ways\b|\bat some level\b|\barguably\b|\bto some extent\b|\bin a sense\b", "Hedge — needed?"),
    ("summation", r"at the end of the day|when the dust settles|\bultimately,|\bin conclusion\b|\bin summary\b", "Usually deletable."),
    ("warmth", r"great question|i completely understand|happy to help", "Generic warmth."),
    ("recyclable", r"a useful way to think about|the key (idea|takeaway|insight) (is|here)|this can be understood as|it'?s worth noting|it is important to note", "Recyclable frame."),
    ("vocabulary", r"\b(delve\w*|tapestry|testament|underscor\w+|realm|pivotal|multifaceted|seamless\w*|robust|nuanced|load-bearing|scaffolding|lean(s|ing)? into|double down)\b", "Low-friction vocabulary."),
    ("dynamism", r"\b(navigat\w+|leverag\w+|unlock\w*|foster\w*|empower\w*|elevat\w+|streamlin\w+|supercharg\w+|harness\w*)\b", "Insipid dynamism: name the actual action."),
    ("beacon", r"a testament to|beacon of|serves as a (reminder|testament)|stands as a", "Say it directly."),
    ("vague noun", r"\b(landscape|ecosystem|journey|synergy|paradigm)\b", "Gestures vaguely — what exactly?"),
    ("intensifier", r"very important|significant (impact|role)|major role|crucial role|vital role", "Intensifier without evidence."),
    ("signpost", r"let'?s (unpack|dive|break)|here'?s (a|the) breakdown|there are (three|five|several) key|to understand why this matters", "Signposting / section preview."),
    ("ending", r"the future (is|looks)|what we can learn|only time will tell", "Moral-of-the-story ending?"),
    ("disclaimer", r"this (isn'?t|is not) to say|that'?s not to say|without claiming|i'?m not (saying|claiming|suggesting)|this does(n'?t| not) mean (that )?|none of this means|to be clear,|this is (just |only )?an illustration|i have no (data|evidence) (that|to)|this is not a (claim|promise|guarantee)", "Pre-emptive disclaimer? State a real limit once, affirmatively, or cut."),
    ("chat leftover", r"i hope this helps|let me know if|would you like me to|sure! here|certainly! here|as an ai (language )?model|as of my (knowledge|last)", "Chatbot leftover."),
]

COMMON_PATTERNS = [
    ("technical", r"utm_source=chatgpt\.com|utm_source=openai|utm_source=perplexity", "Remove tracking parameter."),
]


def detect_lang(text):
    pl_chars = len(re.findall(r"[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]", text))
    pl_words = len(re.findall(r"\b(się|jest|nie|że|oraz|który|która|które|dla|jak)\b", text, re.I))
    return "pl" if pl_chars + pl_words > len(text) / 400 else "en"


def strip_code(text):
    return re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)


def line_of(text, idx):
    return text.count("\n", 0, idx) + 1


def phrase_hits(text, patterns):
    hits = []
    for cat, rx, hint in patterns:
        for m in re.finditer(rx, text, re.I | re.M):
            hits.append({"line": line_of(text, m.start()), "category": cat,
                         "match": m.group(0).strip(), "hint": hint})
    hits.sort(key=lambda h: h["line"])
    return hits


def prose_lines(text):
    """Linie będące prozą (bez nagłówków, list, cytatów, tabel)."""
    out = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s.startswith(("#", "-", "*", "+", ">", "|")) or re.match(r"\d+[.)]\s", s):
            continue
        out.append(s)
    return out


def sentences(text):
    prose = " ".join(prose_lines(text))
    parts = re.split(r"(?<=[.!?…])\s+(?=[A-ZĄĆĘŁŃÓŚŹŻ„\"“])", prose)
    return [p for p in parts if len(p.split()) >= 2]


def metrics(text, lang):
    words = re.findall(r"\b\w+\b", text)
    n_words = max(len(words), 1)
    sents = sentences(text)
    lens = [len(s.split()) for s in sents]
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip() and not p.strip().startswith(("#", "-", "*", "|", ">"))]
    para_lens = [len(p.split()) for p in paras]
    lines = text.splitlines()
    bullets = [l for l in lines if re.match(r"\s*([-*+]|\d+[.)])\s+", l)]
    bold_lead = [l for l in bullets if re.match(r"\s*([-*+]|\d+[.)])\s+\*\*[^*]+\*\*\s*[:.–—-]?", l)]
    headings = [l for l in lines if re.match(r"\s*#{2,6}\s", l)]
    title_case = []
    if lang == "pl":
        for h in headings:
            ws = [w for w in re.sub(r"^\s*#+\s*", "", h).split() if len(w) > 3]
            if len(ws) >= 3 and all(w[0].isupper() for w in ws):
                title_case.append(h.strip())
    summary_heading = [h.strip() for h in headings if re.search(r"podsumowanie|wnioski|conclusion|summary|key takeaways", h, re.I)]
    dashes = len(re.findall(r"—|(?<=\S)[ \t]+[–-][ \t]+", text))
    colons_intro = len(re.findall(r":\s*$", text, re.M))
    def cv(xs):
        return round(statistics.pstdev(xs) / statistics.mean(xs), 2) if len(xs) >= 3 and statistics.mean(xs) else None
    m = {
        "words": n_words,
        "sentences": len(lens),
        "sentence_len_mean": round(statistics.mean(lens), 1) if lens else None,
        "sentence_len_cv": cv(lens),
        "long_sentences_35plus": sum(1 for x in lens if x >= 35),
        "paragraph_len_cv": cv(para_lens),
        "dashes_per_100_words": round(dashes * 100 / n_words, 2),
        "lines_ending_with_colon": colons_intro,
        "bullet_lines": len(bullets),
        "bullet_share_of_lines": round(len(bullets) / max(len([l for l in lines if l.strip()]), 1), 2),
        "bullets_with_bold_lead": len(bold_lead),
        "headings": len(headings),
        "words_per_heading": round(n_words / len(headings)) if headings else None,
        "title_case_headings_pl": title_case,
        "summary_headings": summary_heading,
    }
    return m


def flags(m, hits=()):
    f = []
    disc = sum(1 for h in hits if h["category"] in ("zastrzeżenie", "disclaimer"))
    per_k = disc * 1000 / max(m["words"], 1)
    if disc >= 3 and per_k > 3:
        f.append(f"Defensywny ton: {disc} zastrzeżeń przed zarzutami, których nikt nie postawił ({per_k:.1f} na 1000 słów).")
    if m["sentence_len_cv"] is not None and m["sentences"] >= 6 and m["sentence_len_cv"] < 0.35:
        f.append(f"Monotonny rytm: zdania podobnej długości (CV={m['sentence_len_cv']}). Przeplataj krótkie z długimi.")
    if m["long_sentences_35plus"]:
        f.append(f"{m['long_sentences_35plus']} zdań ma 35+ słów. Sprawdź, czy da się je podzielić.")
    if m["paragraph_len_cv"] is not None and m["paragraph_len_cv"] < 0.25:
        f.append(f"Akapity bardzo równej długości (CV={m['paragraph_len_cv']}).")
    if m["dashes_per_100_words"] > 1.0:
        f.append(f"Dużo myślników: {m['dashes_per_100_words']} na 100 słów.")
    if m["lines_ending_with_colon"] >= 3:
        f.append(f"{m['lines_ending_with_colon']} linii kończy się dwukropkiem (zapowiedź listy).")
    if m["bullet_share_of_lines"] > 0.4 and m["bullet_lines"] >= 6:
        f.append(f"{int(m['bullet_share_of_lines']*100)}% linii to punkty listy. Czy część to narracja?")
    if m["bullets_with_bold_lead"] >= 3:
        f.append(f"{m['bullets_with_bold_lead']} punktów zaczyna się pogrubieniem („**X:** …”).")
    if m["words_per_heading"] is not None and m["words_per_heading"] < 120 and m["headings"] >= 3:
        f.append(f"Nagłówek co ~{m['words_per_heading']} słów. Czy format tego wymaga?")
    if m["title_case_headings_pl"]:
        f.append(f"Nagłówki Wielkimi Literami: {len(m['title_case_headings_pl'])}.")
    if m["summary_headings"]:
        f.append("Osobna sekcja podsumowania/wniosków: " + "; ".join(m["summary_headings"]))
    return f


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="plik z tekstem lub '-' dla stdin")
    ap.add_argument("--lang", choices=["pl", "en", "auto"], default="auto")
    ap.add_argument("--json", action="store_true", help="wynik jako JSON")
    a = ap.parse_args()

    raw = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    text = strip_code(raw)
    lang = detect_lang(text) if a.lang == "auto" else a.lang
    pats = (PATTERNS_PL if lang == "pl" else PATTERNS_EN) + COMMON_PATTERNS
    hits = phrase_hits(text, pats)
    m = metrics(text, lang)
    fl = flags(m, hits)

    if a.json:
        print(json.dumps({"lang": lang, "phrase_hits": hits, "metrics": m, "flags": fl}, ensure_ascii=False, indent=2))
        return

    print(f"Język: {lang} | słów: {m['words']} | zdań: {m['sentences']} | trafień fraz: {len(hits)}")
    print("Wynik to lista miejsc do obejrzenia, nie werdykt. Oceń każde w kontekście.\n")
    if fl:
        print("== Rytm i struktura ==")
        for x in fl:
            print(f"- {x}")
        print()
    if hits:
        print("== Frazy ==")
        by_cat = {}
        for h in hits:
            by_cat.setdefault(h["category"], []).append(h)
        for cat, hs in sorted(by_cat.items(), key=lambda kv: -len(kv[1])):
            print(f"[{cat}] ({len(hs)}) — {hs[0]['hint']}")
            for h in hs:
                print(f"   l.{h['line']}: {h['match']}")
        print()
    if not fl and not hits:
        print("Nic nie wyskoczyło. Zrób jeszcze testy parafrazy, przeszczepu i na głos — skaner ich nie zastąpi.")


if __name__ == "__main__":
    main()
