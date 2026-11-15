# Rating Precedence, Response Evaluation, and Pre-Issue QA

## 1. Three-Tier Rating Precedence (No Universal Matrix)

Never override bank methodology with generic severity thresholds. Resolve `rating` strictly in this order:

1. **Priority 1 — Bank-approved methodology:** Use the bank's approved risk/control deficiency matrix, materiality thresholds, and rating labels. When bank rules conflict with any generic rule, **bank methodology governs unconditionally**.
2. **Priority 2 — Engagement-approved criteria:** Where bank-wide methodology is silent on a specialized domain/project, apply rating criteria documented and approved in the engagement planning/scoping memo.
3. **Priority 3 — Configurable fallback scale (Drafting Aid Only):** Use only when neither Priority 1 nor Priority 2 exists in the record. Stamp both `rating_methodology` and the output block:
   `[FALLBACK DRAFTING AID — NOT AN AUTHORITATIVE BANK RATING]`
   - *Configurable drafting anchors (replace with bank scale before issue):* `Critical / High` (key control missing/failed on material exposure or regulatory compliance without effective mitigation), `Medium` (control operates inconsistently or moderate exposure bounded by compensating controls), `Low` (isolated administrative or minor efficiency gap).

### Repeat & Systemic Flagging
Even when a single finding is `Medium` under bank rules, check prior audit history and sibling findings. If the same control or root-cause family recurs across periods or processes, preserve its individual `Medium` rating and add `systemic_repeat_flag: evaluate holistic impact` to `upstream_holds` for `audit-report-writer`.

## 2. Five Tests of a Management Action Plan

Evaluate proposed management responses before closing Step 4:

| Test | Pass Condition | Common Failure to Reject |
| --- | --- | --- |
| 1. Closes the cause | Directly eliminates the verified `design_gap`, `ownership_gap`, `knowledge_gap`, or `incentive_or_workload_conflict` | "Remind staff", "retrain without fixing system", or fixing only the sampled items |
| 2. Accountable role | Names an `accountable_role` (personal name only if formally assigned in source) | "Management", "IT team", or an unallocated department |
| 3. Hard target date | Exact calendar date (`YYYY-MM-DD`) proportionate to exposure | "Q3", "ongoing", "ASAP", or open-ended milestones |
| 4. Interim control (`High`/`Critical`) | Active compensating safeguard with owner role and cadence until permanent fix | Missing interim protection on high exposure, or **fabricated** manual control when infeasible |
| 5. Closure testability | States `closure_evidence` an independent validator can re-test without asking the author | Vague "ensure compliance" with no observable artifact or operating window |

## 3. Handling Rule Conflicts & Pushback

### Conflict A: Management Accepts Condition, Disputes Cause
- **Do not** lock or alter the verified `Condition` figures to compromise on cause.
- Keep `cause_status: disputed` (explicitly **provisional**, never locked).
- Document both sides transparently: `Verified fact` (condition) + `Auditor inference` (diagnosed cause) + `Management representation` (disputed alternative explanation).
- If management's proposed action plan fails to address the `Auditor inference` cause, keep the action-plan gap in `upstream_holds` and draft a neutral **Auditor's Comment** focused on the control gap, never on personalities.

### Conflict B: `High`/`Critical` Finding with No Feasible Interim Control
- **Never** invent a performative manual check (e.g., "daily spreadsheet review of 50,000 batch records") if the record shows technical or operational infeasibility.
- Set `interim_control: Infeasible — [technical/operational reason]`.
- Document the unmitigated residual exposure window until the permanent fix date.
- Add `infeasible_interim_control — CAE and Supervisory Board notification required` to `upstream_holds`.

### Conflict C: Management Risk Acceptance Outside Delegated Authority (GIAS Standard 11.5)
- Management cannot unilaterally "accept" a regulatory breach, charter-prohibited exposure, or risk exceeding its approved risk-acceptance threshold.
- Refuse to mark the finding closed or resolved.
- Record `risk_acceptance_out_of_authority` in `upstream_holds` for escalation by the CAE to the Supervisory Board (and Owner tier if authorized by charter).

## 4. 15-Question Pre-Issue QA Gate

Verify every finding before handoff to `audit-report-writer`:

1. **Condition:** Numerator, denominator (or sample/limitation disclosure), period, and workpaper locus stated?
2. **Condition:** Worst instance shown rather than hidden inside an average?
3. **Condition:** Hostile-reader test — could a skeptical auditee agree every word is a `Verified fact` with zero editorial adjectives?
4. **Criteria:** Exact source, section, and version effective during the audit period cited?
5. **Criteria:** Legal Currency Gate passed, or unverified laws excluded as binding criteria via hold tag?
6. **Criteria:** Unwritten operational criteria agreed prior to testing (or flagged as a hold)?
7. **Cause:** Classified in one of the 4 routine families (and zero unverified intent/fraud inside routine causes)?
8. **Cause:** `cause_status` accurately set (`approved`, `provisional`, or `disputed`)?
9. **Consequence:** Realized and potential consequences separated, with negative assurance stated where tested?
10. **Sampling:** Zero unsupported extrapolation (all 5 non-statistical elements shown when applicable)?
11. **Rating:** Named `rating_methodology` follows Tier 1 → Tier 2 → Tier 3 precedence?
12. **Action:** Closes the root cause rather than just the sampled exceptions?
13. **Action:** Specifies `accountable_role`, exact `target_date`, and verifiable `closure_evidence`?
14. **Interim:** Active `interim_control` specified for `High`/`Critical`, or infeasibility + escalation documented?
15. **Handoff:** All 19 fields of the Canonical Handoff Contract complete and consistent?
