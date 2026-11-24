# Acceptance cases

Use these as behavioral probes when testing an agent that claims to follow this skill. They are synthetic. Expected results describe properties, not exact strings.

## Case 1: buried numerical takeaway

Input: A chart showing forecast price decreasing from $4.03 to $3.99, roughly 1%. Candidate title: `At the floor`. Subtitle contains `$3.99 (-1%)`.

Expected: Reject candidate. Title includes price/forecast and the decline to $3.99 or 1%. It may repeat subtitle numbers. Avoid implying an actual observed floor.

## Case 2: writer-action leakage

Input: Analyst decided to exclude incompatible time series, then made a slide about two estimates that cannot be directly compared. Candidate title: `No splice`.

Expected: Reject. Title tells the reader *what cannot be compared and why*, without requiring awareness of analyst's action. Do not invent the series names if absent.

## Case 3: chart geometry substitute

Input: The 95% forecast interval expands from +/-2 units at 1 month to +/-10 at 12 months. Candidate title: `The band opens`.

Expected: Rewrite to name uncertainty, horizon, and magnitude. Keep `95%` if necessary to interpret the interval. Do not confuse interval width with expected point forecast.

## Case 4: unsupported causality

Input: A plot has r = 0.76 correlation between vacancy and prices; no causal analysis. Candidate: `Vacancies drive prices`.

Expected: Reject. Use association terminology. Include sample/period where known; do not fabricate.

## Case 5: inconclusive analysis

Input: A noisy scatter plot shows no clear, statistically defensible relationship.

Expected: A neutral descriptive title or a properly bounded no-clear-association title. Do not manufacture trend, magnitude, confidence, or significance to satisfy an assertion-first rule.

## Case 6: section-heading outline

Input: Headings `The problem`, `Our approach`, `The results`, `Looking forward`; text says reconciliation takes 3 days, automation reduces it to 1 day, rollout begins in November.

Expected: Rewrite appropriate headings as self-contained claims or reader questions. The outline alone should convey delay, improvement, and next step. Preserve any meaningful uncertainty and dates.

## Case 7: dashboard KPI

Input: A 4-column KPI strip shows `Churn` with `2.1%`, and its period `Q3` in the same tile.

Expected: Accept compact `Churn` label when paired visibly with value and period. Do not insist on a full-sentence assertion where tile structure supplies the missing elements.

## Case 8: valid method-centered result

Input: A benchmark shows Holt forecast mean absolute error 12% below a baseline; candidate title: `Holt model reduces forecast error 12% vs. baseline`.

Expected: Accept if result and calculation are supported. The method is the subject of this finding.

## Case 9: critical caveat

Input: Revenue rose 8% after acquisition, but organic revenue fell 3%. Candidate title: `Revenue rises 8%`.

Expected: Reject as materially misleading if presented as organic growth or business-wide performance without qualification. Surface acquisition and organic decline at headline level or split claims.

## Case 10: intentional creative title

Input: User requests an evocative chapter title for a fictional novella.

Expected: Do not enforce literal subject-direction-quantity framing. Follow the creative brief.

## Case 11: external excerpt

Input: A slide title `The window changes everything` refers to a correlation reversal in 2018–2020 versus 2022–2024.

Expected: Rewrite so an exported slide can communicate the correlation reversal and the relevant windows without the chat.

## Case 12: length constraint

Input: A chart title is restricted to 45 characters and result is too complex for one line.

Expected: Preserve subject plus strongest supported distinction in title; place remaining context in immediately visible subtitle. Never choose a metaphor simply to fit length. Avoid incorrect compression.
