# Finding Elements, Guardrails, and Canonical Handoff Contract

## 1. Immutable Evidentiary Status Labels

Preserve the exact upstream evidentiary status from `evidence-triage` across every draft and revision. Never upgrade an inferior label into `Verified fact`:

| Label | Meaning | Drafting Constraint |
| --- | --- | --- |
| `Verified fact` | Directly supported by reconciled system extract, re-performance, or signed primary artifact | May support Condition and realized Consequence |
| `Management representation` | Uncorroborated statement, tracker, or explanation from management | Cite explicitly as management's statement; cannot prove operating effectiveness or closure |
| `Auditor inference` | Analytical link inferred from facts (e.g., probable cause or unmeasured impact) | Label as inference; keep `cause_status: provisional` until corroborated/approved |
| `Unverified allegation` | Whistleblower tip, rumor, or uncorroborated fraud/misconduct claim | Halt routine finding attribution; route via Investigation Firewall |
| `Scope limitation` | Missing population, log outage, or restricted access | State limitation explicitly; never record `0` exceptions |
| `Investigation or protocol referral` | Matter routed to fraud, forensic, legal, or ethics protocol | Keep investigative specifics out of routine finding and governance outputs |

## 2. Routine Cause Taxonomy vs. Investigation Firewall

### Routine Cause Families (4 allowed categories)
Classify routine control/process causes at the deepest actionable level management can fix ("stop rule": stop before unactionable macro-causes like "budget" or "culture", and never stop at "human error"):

1. `design_gap` — Control was never built to cover the risk/scenario or lacks enforcement logic.
2. `ownership_gap` — Task, queue, or review lacks an assigned accountable role or backup coverage.
3. `knowledge_gap` — Standard exists, but executing roles were not trained or criteria were never communicated.
4. `incentive_or_workload_conflict` — Targets, close calendars, or volume assignments conflict with control execution.

### Investigation Firewall (Outside Routine Taxonomy)
Suspected deliberate misconduct, fraud, collusion, override for personal benefit, or any `Unverified allegation` is **never** a routine cause category:
1. **Stop** inferring intent or blaming individuals from transaction patterns alone.
2. **Preserve neutral factual wording** in any cleared control observation (e.g., *"transactions combined to exceed threshold"*, not *"split to circumvent policy"*).
3. **Set** `investigation_referral: required` and route to the bank's fraud/forensic/legal investigation lead.
4. **Exclude** investigative leads, suspect names, and unverified allegations from routine finding text passed to `audit-report-writer`.

## 3. Legal Currency Gate

Keep live legal verification outside the writing agent when authoritative legal repositories are unavailable:
- Before citing any law, decree, central-bank circular, or supervisory regulation as binding criteria, verify: (a) current in-force status, (b) amendments or replacements, (c) effective date covering the audit period, (d) institutional applicability to the audited bank/entity, and (e) exact article and clause.
- If any item is unverified in the provided record or live authoritative source, emit:
  `[UNVERIFIED LEGAL CURRENCY — EXCLUDE AS BINDING CRITERIA UNTIL VERIFIED]`
- Set `legal_currency_status: unverified_hold` and add the unverified citation to `upstream_holds`. Rely on verified internal bank policy or engagement-agreed criteria until legal currency is confirmed.

## 4. Sampling & Extrapolation Rule

- **Statistical sampling (valid projection):** Extrapolate to the population **only** when statistical sampling design, selection method, and complete sampling frame are documented in the source record. State confidence/precision bounds alongside the point estimate.
- **Judgmental / non-statistical / unverified frame (no projection):** Never extrapolate exception rates to total population exposure. Always report all five elements explicitly:
  1. `tested population` (e.g., total universe N and period, or `not_measured` if unknown)
  2. `sample size` (`n`)
  3. `exception count` (`k`)
  4. `observed rate` (`k / n` — scoped strictly to the sample)
  5. `extrapolation limitation` (e.g., *"Judgmental sample; rate applies only to the 25 items tested and cannot be projected to the annual population."*)

## 5. Canonical Handoff Contract (19 Required Fields)

Every finalized finding passed to `audit-report-writer` must emit this exact schema so figures, roles, dates, statuses, and holds do not drift across layers:

```yaml
finding_id: "F-01"
title: "Consequence-led title under 12 words (no editorial adjectives)"
evidence_status: "Verified fact | Management representation | Auditor inference | Unverified allegation | Scope limitation | Investigation or protocol referral"
condition: "Neutral, quantified facts with population/sample bounds, period, worst instance, and workpaper locus"
criteria: "Verified binding source (policy §/version, verified law/article, or engagement-agreed criteria)"
cause: "Actionable root cause (design_gap | ownership_gap | knowledge_gap | incentive_or_workload_conflict) or 'Held pending verification'"
cause_status: "approved | provisional | disputed"
consequence_realized: "Confirmed loss/impact observed in testing, or 'None identified in tested items'"
consequence_potential: "Mechanism and bounded risk exposure supported by facts/criteria"
sampling_basis: "full_population | statistical_extrapolated | non_statistical_no_extrapolation (must list tested population, sample size, exception count, observed rate, extrapolation limitation)"
rating: "Rating per Tier 1/2/3 precedence, or 'HOLD — methodology missing'"
rating_methodology: "Named bank-approved methodology | engagement-approved criteria | [FALLBACK DRAFTING AID — NOT AN AUTHORITATIVE BANK RATING]"
accountable_role: "Accountable role title (personal name only if formally assigned in source record)"
target_date: "YYYY-MM-DD (or 'HOLD — missing commitment date')"
interim_control: "Active compensating control with role & cadence, 'N/A (Low/Medium)', or 'Infeasible — [reason]; escalated to CAE/Supervisory Board'"
closure_evidence: "Objective artifact or re-test condition required to validate closure"
investigation_referral: "none | required (neutral routing note only; zero investigative details)"
legal_currency_status: "verified | internal_policy_only | unverified_hold"
upstream_holds:
  - "Explicit list of unresolved holds (disputed cause, unverified legal citation, missing methodology, infeasible interim control, systemic repeat flag, unauthorized risk acceptance)"
```
