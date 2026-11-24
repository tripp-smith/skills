# Ecosystems

Each directory here is one installable ecosystem. Clients discover skills one level deep, at `skills/<skill-name>/SKILL.md`, so related skills are grouped by plugin instead of by a nested folder.

| Plugin | Captures | Skills |
| --- | --- | --- |
| `writing` | Long-form writing, manuscripts, and reader-facing prose | `reader-first-communication` (cold-read titles, headings, and prose) |
| `product` | Specifications, planning, and product communication | — |
| `engineering` | Implementation, delivery, and verification workflows | — |
| `media` | Image, video, voice, and film workflows | — |

Add another ecosystem with `python3 scripts/new-plugin.py`. Add a skill inside an existing ecosystem with the `add-skill` skill.
