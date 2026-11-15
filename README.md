# audit-reporting

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Synthetic data only](https://img.shields.io/badge/data-synthetic%20only-15803D)

Public internal audit finding and report writing skills for AI agents, designed to sit downstream of [evidence-triage](https://github.com/ducle2502/evidence-triage) and enforce evidentiary immutability, methodology-first severity ratings, investigation firewalls, sampling honesty, and configurable governance routing.

> [!IMPORTANT]
> This repository is public. Do not commit employer, client, customer, or personal data, internal bank policies, or real investigation output. Every example is synthetic.

## Skills

| Skill | Scope | Path |
| --- | --- | --- |
| `audit-finding-writer` | Finding-level reasoning: 5-Cs causal chain, immutable evidentiary labels, Legal Currency Gate, sampling non-extrapolation, methodology-first ratings, response QA, and 19-field Canonical Handoff Contract | [skills/audit-finding-writer/SKILL.md](skills/audit-finding-writer/SKILL.md) |
| `audit-report-writer` | Multi-finding synthesis: holistic non-mechanical engagement conclusions (aligned with IIA GIAS Standard 15.1), configurable governance routing, GIAS 11.5 risk-acceptance escalations, investigation firewalls, and cross-layer canonical consistency | [skills/audit-report-writer/SKILL.md](skills/audit-report-writer/SKILL.md) |

## End-to-End Pipeline

```text
evidence-triage (Evidence QC & Claim QC)
  └─> audit-finding-writer (19-field Canonical Handoff Contract)
        └─> audit-report-writer (Configurable Audience Routing & GIAS 15.1 Report)
```

## Verification

Run the included test suite:

```bash
python -m unittest discover -s tests -v
```

## License

MIT — see [LICENSE](LICENSE).
