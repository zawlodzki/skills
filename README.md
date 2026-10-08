# zawlodzki-skills

Skille do [Claude Code](https://claude.com/claude-code), które przygotowuję przy pracy nad CRM, automatyzacją i AI w sprzedaży B2B. Więcej o tym, czym się zajmuję: [zawlodzki.pl](https://www.zawlodzki.pl).

## Instalacja

```bash
claude plugin marketplace add zawlodzki/skills
claude plugin install zawlodzki-skills@zawlodzki
```

## Skille

### natural-writing

Pisanie i redakcja tekstów po polsku i angielsku bez nawyków typowych dla prozy z LLM. Chodzi o frazy, które brzmią mądrze, ale nic nie mówią, kalki w rodzaju „dedykowany” i „adresować problem”, nadmiar nagłówków, list i myślników oraz wyważanie „z jednej strony… z drugiej”. Skill nie dopisuje zmyślonych przykładów. Tam, gdzie tekst potrzebuje materiału od autora, zostawia znacznik `[DO UZUPEŁNIENIA]`.

W zestawie są katalogi wzorców dla obu języków i skaner, który pokazuje miejsca do sprawdzenia:

```bash
python3 skills/natural-writing/scripts/scan_tells.py tekst.md
```

Katalogi opierają się na tekście a16z crypto [The habits of AI writing, and what to do about them](https://x.com/a16zcrypto/status/2091934263302402318) oraz artykułach Katarzyny Baranowskiej o [humanizacji tekstu AI](https://katarzynabaranowska.com/humanizacja-tekstu-ai/) i [proofreadingu treści AI](https://katarzynabaranowska.com/jak-zrobic-proofreading-tresci-ai/).

## Licencja

[MIT](LICENSE)
