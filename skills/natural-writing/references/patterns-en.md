# AI writing patterns: English catalogue

Use this when reviewing English text. Each entry says what the pattern looks like, why it weakens the writing, and what to do instead. A hit is a reason to look at the sentence, not an automatic verdict. Many items are long-standing writing problems (corporate speak, filler, over-structure) that models simply produce in bulk.

## Contents

1. Rhetoric: insight-shaped writing
2. Voice: the "Alexa voice"
3. Structure: all form, no function
4. Punctuation
5. Chat leftovers and technical debris
6. When to keep a pattern

---

## 1. Rhetoric: insight-shaped writing

Sentences that sound like insight but don't survive paraphrase. Rule of thumb: edit almost always.

- **Faux profundity.** "Something real is happening." "The stakes couldn't be higher." "The implications are significant." "This matters for crucial reasons." Sounds important, is filler. Say what is happening and what follows from it.
- **Corporate filler.** "We're excited to announce…", "We're at an inflection point", "This is the next chapter of our journey." Weighty-sounding, not specific enough to survive paraphrase.
- **Empty contrasts.** "It's not just about X — it's about Y", "This isn't X. It's Y.", especially when Y is fuzzier than X. Try deleting the "not X" half and get to the point.
- **Hedges.** "In many ways", "At some level", "Arguably", "To some extent". They make a sentence impossible to be wrong about, which also makes it empty. Keep hedges that are legally or factually required (finance, health).
- **Pre-emptive disclaimers.** Sentences that deny a claim nobody made: "This isn't to say that…", "without claiming that…", "That doesn't mean…", "To be clear, …", "I'm not suggesting…", "This is an illustration, not a description of a real deployment." One is honest; a run of them makes the piece sound like it is answering a reviewer instead of talking to the reader. Models produce more of these when told "don't overclaim". State a real limit once, affirmatively, where it matters ("I haven't run this test yet"); delete denials of claims the text never made; keep disclaimers that carry an actionable warning or are legally required. More than ~3 per 1,000 words reads as defensive.
- **In-summation phrases.** "At the end of the day", "When the dust settles", "Ultimately". Usually deletable with no loss.
- **Over-parallelism.** Bullets and sentences mirroring each other too tidily, every item the same grammatical shape and length.

Tests: ask for the "boring" version of the sentence. If the paraphrase is better, keep it. If the sentence boils down to "stuff exists" or "things are changing", delete it and check whether the piece still works.

## 2. Voice: the "Alexa voice"

Default model prose draws on a small, safe vocabulary. The test is **fungibility**: could this sentence be lifted word-for-word into someone else's piece, on a different topic, without anyone noticing? If a stranger could claim it, rework it.

- **Generic warmth.** "Great question!", "I completely understand your concern." Friendly in a hold-music way.
- **Recyclable framing.** "A useful way to think about it is…", "The key idea is…", "This can be understood as…". Delete the frame, keep the content.
- **Low-friction vocabulary.** Every word acceptable in an uncanny way. Known offenders over time: *delve, tapestry, testament, underscore, realm, pivotal, nuanced, multifaceted, robust, seamless, crucial, vital*; more recently *load-bearing, scaffolding, broader, surface (v.), lean into, double down*.
- **Abstract nouns.** *efficiency, complexity, society, communication, innovation, alignment, synergy*. Saying nothing in three syllables.
- **Insipid dynamism.** *navigate, leverage, unlock, foster, power / empower, shape, elevate, streamline, supercharge, transform, drive*. Verbs that signal motion but fall flat. Use the verb that names the actual action.
- **"A beacon of something."** "A testament to…", "Stands as a beacon of…", "Serves as a reminder that…".
- **Gestures vaguely.** *landscape, space, journey, ecosystem, tapestry, realm, world of*. They point near a thing instead of naming it. Example: "The Ethereum ecosystem is expanding" → "Developers are building more wallets, exchanges, and lending markets around Ethereum."
- **Vague intensifiers.** "very important", "significant impact", "major role" with nothing concrete behind them.

Ask of every vague word: is there a more specific one? Match diction to mood: short plain words to explain something opaque; "scheme" rather than "plan" when the reader should smell trouble.

## 3. Structure: all form, no function

Structure is a set of decisions: which container, what matters most, what goes together, what to call it. Those depend on the job. A narrative essay needs discovery and tension, a product announcement needs brutal efficiency, an explainer needs concepts in learning order.

Tells:

- **Over-organization.** Many subheads, bullets, numbered sections, mini-frameworks; paragraph breaks every sentence or two.
- **Everything in threes.** Fine when an idea really has three parts; a tell when a third item is obviously forced.
- **Familiar essay shape.** Broad intro → explanation → examples → caveat → conclusion, regardless of genre.
- **Formulaic openings.** "In today's rapidly changing world…", "In the ever-evolving landscape of…".
- **Too much signposting.** "First," "Next," "Finally," "In conclusion," "Here's a breakdown," "Let's unpack this," "Let's dive in."
- **Hard-pivot transitions.** "To understand why this matters, we first need to look at…"
- **Section previews.** "There are three key reasons…"
- **Bold lead-ins on bullets.** "**Flexibility:** …" — a signature model move. Fine for scannable reference material, odd elsewhere.
- **Punchy fragments.** "Short. Punchy. Often in threes." The LinkedIn cadence.
- **Ending on a restatement.** The conclusion paraphrases the piece instead of extending it.
- **Moral-of-the-story endings.** A vague last line about progress, the future, or "what we can learn."

Edit when: subheads don't fit the format (op-eds, personal narratives, anything argued through voice and momentum); sections aren't really distinct; structure changes the meaning (a numbered list of reasons a startup pivoted reads differently from the story of the pivot); signposts announce a self-evident structure.

## 4. Punctuation

The issue is sameness and density, not any single mark. Default to periods and commas; use "special" punctuation when grammar calls for it or it clearly earns its place.

- **Em dash clustering.** Several dash asides in neighbouring sentences, dashes in lists. No more than two per sentence. Em dashes remain legitimate for longer parentheticals and abrupt shifts in thought.
- **Colon-heavy phrasing.** "The issue is:", "The result is:", "The key point is:" — especially colons followed by grocery lists, sentence after sentence.
- **Unserious parentheticals** (like this one). The self-aware, joking register.
- **Performative semicolons.** Legitimate uses exist; they don't come up that often.
- **Don't just swap marks.** Telling a model to "remove all em dashes" tends to produce colons with the same sentence structure. Rebuild the sentence instead.

Test: read it aloud, treating punctuation as stage directions. Anything that sounds unnatural will stand out to readers too.

## 5. Chat leftovers and technical debris

- Assistant preambles: "Sure! Here's a draft…", "Certainly, here is…".
- Follow-up offers pasted into the text: "Let me know if you'd like a shorter version", "Would you like me to…", "I hope this helps!".
- `utm_source=chatgpt.com` and similar tracking parameters in links.
- Unrendered Markdown (`**`, `##`) in places that don't support it.
- Self-references: "As an AI language model…", "As of my knowledge cutoff…".
- Title Case On Every Heading when the house style is sentence case.

## 6. When to keep a pattern

- **Neutral "Alexa voice"** is a mercy in support docs, error messages, terms of service, safety instructions, FAQs — anything read by a million strangers in a million contexts.
- **Heavy structure** belongs in listicles, explainers, how-tos, documentation, reference material people scan and return to, and content written for skimmers or for search engines and LLMs.
- **Threes** when the idea actually has three parts.
- **Hedges** when they are legally or factually load-bearing.
- **Any punctuation** that is correct, supports the meaning, and stays mostly invisible.
