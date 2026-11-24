---
name: reader-first-communication
description: Create and revise reader-facing documents, slides, presentations, chart and plot titles, dashboards, report headings, executive summaries, headlines, email subjects, and explanatory prose. Use whenever writing must make sense to an external audience without the author's conversational or analytical context. Prevents retrospective labeling, context-dependent metaphors, vague headings, buried findings, and wording that is grammatical but unnatural for the domain, including figurative verbs and metaphors a conventional literal expression would convey as well or better. Prefer assertion-first information hierarchy and cold-read review. Do not impose on explicitly creative, literary, or intentionally cryptic writing.
---

# Reader-first communication

## Purpose

Write for the reader's **first encounter**, not the author's **last step**. The reader has not participated in the conversation, performed the analysis, or seen the supporting material. A title or opening line must give them the context needed to interpret the detail that follows.

Prevent **writer-centric context leakage**: when a writer uses vocabulary, shortcuts, metaphors, process notes, or assumptions that make sense only after seeing the underlying work. In visual artifacts this often appears as **retrospective labeling**: naming a panel after a method, chart shape, or local analytical decision rather than communicating its finding. The resulting **information hierarchy inversion** puts abstraction in the headline and the actual finding in small text.

A figurative word can be grammatical and still fail when it is not the conventional expression for the domain and does not add understanding a literal wording would miss. Reject terms that are local to this analysis or that require prior conversation. Keep standard domain vocabulary an intended expert reader would expect, such as `confidence band`, `time window`, or `price floor` in pricing contexts where that is the precise term.

This is a production and review skill, not merely a style preference. Apply it during planning, drafting, and final editing. Do not announce these checks in the finished artifact unless asked.

## Trigger and boundaries

Use for:
- Slides and presentations, including slide titles, section transitions, and speaker-facing summaries.
- Charts, graphs, tables, dashboards, infographics, and exhibit captions.
- Reports, research notes, memos, executive summaries, briefing documents, web pages, and knowledge-base articles.
- Headlines, subheadings, decks/subtitles, callouts, email subjects, and explanatory prose.
- Rewriting existing artifacts with vague, clever, method-centric, or context-dependent labels.

Do not turn creative fiction, literary titles, brand slogans, deliberate suspense, or an explicitly requested internal shorthand into assertion-based reporting. For exploratory material without a supported conclusion, provide a precise descriptive title rather than manufacturing a finding. Follow the user's explicit audience, voice, length, and format requirements.

## Governing rule

**Generate titles and openings from the reader's information state, not from the author's analytical state.**

The author travels from evidence to understanding to title. The reader travels from title to expectation to evidence to understanding. Write for the second sequence. Every level of the artifact must stand on information available at that point in the reading journey.

If the user has explicitly requested internal shorthand, creative framing, or suspense, follow that instruction. Do not force assertion-first wording onto internal notes or deliberately evocative work when the request asks for something else.

## Workflow

### 1. Establish the audience contract

Before drafting, infer or record:
- **Reader:** Who encounters the artifact? If unspecified, assume an intelligent external reader unfamiliar with the underlying work.
- **Prior knowledge:** What can be safely assumed? Do not count the current chat, scratchpad, preceding tool calls, draft history, or undisclosed analysis as reader knowledge.
- **Encounter:** Will the reader skim the title alone, receive an isolated screenshot, navigate headings, or read continuously?
- **Purpose:** Inform, explain, compare, recommend, persuade with evidence, instruct, or narrate. Select the right kind of opening for that purpose.

If the intended audience is expert, retain technical precision but still introduce the subject and central result. Expertise does not imply familiarity with this particular dataset, conversation, decision, or methodology.

Separate (a) domain vocabulary the stated reader can be assumed to know from (b) instance-specific facts, methods, windows, samples, or intermediate analytical decisions that must be re-introduced. Before locking a title, list the presuppositions it activates and verify each is licensed for that reader.

### 2. Extract the message before drafting its label

For each significant unit (document, section, slide, chart, table, paragraph), identify silently:

| Field | Question |
|---|---|
| Subject | Which entity, population, metric, decision, or concept is this about? |
| Claim | What is the most important supported finding or proposition? |
| Direction | What changed, differs, predicts, relates, or remains unchanged? |
| Magnitude | Which value, estimate, difference, or rank is central to the claim? |
| Context | Compared with what, over which period, or under what condition? |
| Qualification | What uncertainty or limitation would materially change the interpretation? |
| Reader value | What question does this unit answer, or why does it matter here? |

Treat missing fields as missing; never invent values to fill a formula. Distinguish measured facts, forecasts, correlations, hypotheses, and interpretations. Do not convert correlation into causation, probability into certainty, or a local sample into a universal claim.

Choose **one principal message** per unit. If a unit makes multiple independent claims, split it or state an honest higher-level synthesis.

### 3. Build an assertion-first information hierarchy

Allocate information by the order in which a reader encounters it:

1. **Title / headline / lead:** The primary supported assertion, decision, or explicit question. Identify the subject and what happened. Include a salient number when it carries the message. A conclusion-bearing title is the default for explanatory or analytical work.
2. **Subtitle / deck / standfirst:** Scope, comparison, timeframe, method, and concise qualification. When a limitation would make the title misleading, state that limitation in the title itself.
3. **Exhibit / body:** Data, reasoning, examples, derivation, supporting detail, and mechanism.
4. **Notes / footnotes / appendix:** Provenance, full methods, definitions, secondary caveats, and reproducibility details. Do not bury decisive qualifications here.

Under a tight character limit, prefer a precise topic label with an immediately visible assertion subtitle over an underspecified assertion title that drops material context. Do not compress away the subject, comparison, or qualification the claim depends on.

Intentional repetition is allowed and often useful. The same central value can appear in the headline, a chart annotation, and the discussion. These placements serve different reading modes. Do not replace the factual headline with a metaphor merely to avoid repeating a number or noun.

### 4. Draft for cold comprehension

Write a **self-contained statement** rather than a label for already-seen content.

For result-oriented titles, prefer:

`[Specific subject] + [observed relationship or action] + [salient value / comparator / period, when needed]`

Examples (illustrative, not verified findings):
- Poor: `At the floor`  ->  Better: `Price forecast falls 1% to $3.99`.
- Poor: `The dense window`  ->  Better: `Sales and hiring correlate strongly in the 2024 sample (r = 0.76)`.
- Poor: `Holt's view`  ->  Better: `Holt forecast projects a 1% price decline`.
- Poor: `A widening band`  ->  Better: `Forecast uncertainty rises from month 3 onward`.
- Poor: `What we learned`  ->  Better: `Three approval delays account for most of the launch slippage`.
- Poor: `A 10-year TIPS auction lands at 1:00 PM ET.`  ->  Better: `A 10-year TIPS auction is scheduled for 1:00 PM ET.` (`lands` is grammatical and still the wrong verb for a scheduled auction.)

Do **not** make these forms rigid templates. A title about a policy, definition, choice, or unresolved question may have no numeric magnitude or change direction. A document title can identify the subject and intended decision, with the executive summary carrying the full answer. A title may be a question when the content genuinely investigates that question without assuming the result.

Choose plain, concrete language. Keep the actual subject in the highest-prominence text. A method, window, sample, visual shape, analyst's action, or clever analogy must not become the main noun unless that *is* the subject of the finding. Prefer the conventional, literal expression for the intended domain. Use metaphor only when it conveys information or understanding that the literal expression cannot convey as effectively. Distinguish idiosyncratic author labels from conventional technical terms: reject `the dense window` as a private nickname for a sample period; keep `confidence band` when that is the domain's precise term.

### 5. Apply the rule at each scale

**Document / report**
- Title identifies the topic, scope, or decision; if the report makes a single supported headline finding, the title may state it.
- Executive summary opens with the answer or central finding, not a description of the research process.
- Section headings form a meaningful outline when read alone. Prefer takeaways to generic headings such as `Observations`, `Discussion`, or `Interesting patterns` when findings are available.
- Each heading should make clear how it continues from the previous one, or explicitly signal a topic shift, so the outline reads as cumulative rather than a set of disconnected assertions.
- First sentences supply referents before analysis. Each paragraph should answer a recognizable question or advance one claim.

**Slides**
- Each slide's headline asserts its main point; its visual is evidence, not a puzzle the audience must solve to decode the headline.
- A reader should grasp the key message by scanning slide titles in sequence.
- Do not force titles to match in rhythm at the cost of informativeness. No parallel poetic headings that hide different findings.
- Allow neutral section dividers and agenda slides, where assertion headlines are not appropriate.

**Charts / tables / dashboards**
- State subject, relationship or direction, and salient magnitude where supported. Give comparator and timeframe where omission would distort the takeaway.
- Make axes, units, and labels explicit. The title should still convey the takeaway when the plot is hidden.
- A chart with inconclusive results says `No clear association between X and Y in the sampled period`, not `A hidden signal`.
- Dashboard tiles may use metric labels when the value is immediately paired with the label (e.g., `Quarterly churn | 2.1%`). Do not manufacture complete sentences in a compact KPI grid.
- Preserve neutral titles for exploratory charts with no established result.

**Headlines / email subjects / calls to action**
- Convey the news, decision, request, or next action, not generic atmosphere.
- Provide an explicit referent and expected response when action is requested.
- Avoid clickbait, unsupported urgency, and rhetorical mystery unless intentionally requested.

**General explanatory writing**
- Open with the proposition the paragraph will establish. Name actors and mechanisms before using pronouns, shorthand, or analogies.
- Explain new terms on first use at the relevant reading level. Do not assume the reader saw a prior chat turn.
- Place limitations near the claims they constrain; use examples only after the underlying assertion is comprehensible.
- Remove process narration that reports what the writer did instead of what the reader needs to know, except when methodology is itself the topic.

### 6. Cold-read quality gate (mandatory)

Review the finished artifact from an external reader's vantage point. Test every prominent title and opening against all five gates:

1. **Isolation:** With the body, figure, and prior conversation hidden, can the intended reader tell what the statement is about and what it communicates? A question or topic label is acceptable only where genuinely appropriate.
2. **Specificity:** Is the central subject explicit? Is the direction, comparison, decision, or most informative quantity present when the finding relies on it?
3. **Evidence fidelity:** Is the claim supported at the stated level of certainty? Are comparisons, units, timeframes, and meaningful uncertainty accurate? Is any caveat necessary to prevent misinterpretation visible early enough?
4. **Context independence:** Does it avoid unexplained local vocabulary, pronouns without referents, idiosyncratic metaphors, references to the drafting process, and labels such as `the floor`, `the window`, `the shift`, `our approach` that rely on hidden context? A figurative word that a reader can decode still fails when the conventional literal expression for the domain would communicate the fact as effectively. Standard domain terms licensed for the stated reader pass; private nicknames for this analysis fail.
5. **Information hierarchy:** Does the top line carry the highest-value information rather than a mood, method, or decorative gloss? Could the title be pasted onto several unrelated exhibits without becoming obviously wrong? If so, improve its specificity. If space is tight, is a precise topic title plus an immediately visible assertion subtitle better than a compressed assertion that loses material context?

**Fail any applicable gate -> rewrite and retest.** A catchy or balanced title does not compensate for a failed gate. Evidence fidelity is a hard constraint: never fabricate a claim to satisfy a title formula.

For long documents, run two further checks:
- **Outline-only test:** Read only the title, section headings, and paragraph openings. Do they tell a coherent, accurate story? Does each heading continue the prior topic or clearly mark a shift, rather than jumping without signal?
- **Detached-excerpt test:** Imagine a slide exported as a screenshot, a chart forwarded alone, or a paragraph quoted outside the document. Does enough context travel with it?

### 7. Final output behavior

Deliver the requested artifact, not a discussion of your writing process. Apply the quality gate internally. Preserve the user's requested tone and medium. If evidence is unavailable, use clear bounded claims or descriptive headings and make the limitation explicit; never fake precision.

## Additional resources

- For a large batch of headings, domain-specific rewrites, or edge cases, read [references/title-patterns.md](references/title-patterns.md).
- For an explicit audit or QA pass on an existing artifact, read [references/evaluation.md](references/evaluation.md).
- For acceptance examples demonstrating pass and fail cases, read [tests/acceptance-cases.md](tests/acceptance-cases.md).
