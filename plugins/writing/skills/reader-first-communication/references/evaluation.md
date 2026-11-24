# Evaluation and red-team review

Use for an explicit audit, title rewrite, or large deliverable. Do not show this machinery in the final artifact unless the user requests scoring or a review report.

## Review procedure

1. Inventory all reader-facing entry points: artifact title; executive summary or lead; slide titles; chart/table titles; section headings; important callouts; email subjects.
2. For each, hide subordinate text and score only what is available at that entry point. Do not use conversational context to rescue an ambiguous title.
3. Extract the verified claim from the underlying evidence separately. Compare it with the claim implied by the title.
4. Check whether the method, sample, visual shape, poetic metaphor, or writer action has displaced the result.
5. Rewrite failures, then rerun the checks. Review title sequences and exported excerpts independently.

## Pass/fail rubric

| Dimension | Pass | Failure |
|---|---|---|
| Cold-read meaning | Subject and message understandable at the intended reader's level | Requires seeing chart, prior slides, or conversation |
| Claim specificity | Clear relevant relationship, action, decision, or topic | Indeterminate `shift`, `floor`, `lens`, `story`, `moment` |
| Salient fact allocation | Key supported figure or comparison given prominence when it defines takeaway | Numbers buried in subtitle for purely stylistic reasons |
| Accuracy | Supported claim with appropriate scope and uncertainty | Invented value, overstated significance, false causal framing |
| Audience independence | Terms and references available at point of encounter | Unexplained nickname, internal method reference, author-process diary |
| Information order | Main message before supporting mechanics | Interpretation only possible after reading fine print |

Treat accuracy, reader comprehensibility, and materially misleading omission as hard failures. The other criteria guide rewrites, not forced stylistic uniformity.

## Adversarial tests

- **Hide the figure:** What factual proposition does the title alone communicate?
- **Remove the chat:** Are all references still meaningful?
- **Swap the title:** Could it move to several materially different charts and still sound right?
- **Say what changed:** Can the intended reader identify who/what, direction, and central comparison where the subject permits it?
- **Audit confidence:** Did a weak observation become an absolute claim?
- **Check headline/subtitle:** Does the larger type carry the stronger information?
- **Read headings only:** Does the resulting outline summarize the argument rather than the writer's activities?
- **Quote one paragraph:** Is the opening independently interpretable without repeating the full document?

## Optional scoring for batch review

Use a 0–2 scale across five categories: isolation, specificity, evidence fidelity, context independence, and hierarchy. Each category is 0 (fail), 1 (partial), 2 (pass). A total of 9 or 10 is a strong candidate, but a score never overrides an accuracy or materially misleading omission failure. Prefer explaining the failure and the rewrite to reporting a single numeric score.
