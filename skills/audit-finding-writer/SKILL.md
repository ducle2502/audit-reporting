---
name: audit-finding-writer
description: >-
  Draft, critique, or rewrite internal audit findings from workpapers while
  preserving evidentiary status, sampling limits, legal currency, and
  methodology-first severity ratings. Use when turning exceptions into 5-Cs
  findings, evaluating root causes, rating finding severity, testing
  management action plans, handling disputed causes or missing interim controls,
  or running pre-issue finding QA.
---

# IA Audit Finding Writer

Turn verified audit exceptions and workpapers into defensible, QA-ready 5-Cs finding records that preserve evidentiary boundaries and hand off cleanly to `audit-report-writer` via the canonical finding handoff contract.

Follow the user's language (English, Vietnamese, or bilingual). Keep structural rules language-neutral; consult [references/vn-banking-terminology.md](references/vn-banking-terminology.md) only when writing or translating Vietnamese banking governance terms.

## Core Guardrails (Non-Negotiable)

- **Evidentiary status is immutable:** Preserve and display the exact label from `evidence-triage` (`Verified fact`, `Management representation`, `Auditor inference`, `Unverified allegation`, `Scope limitation`, `Investigation or protocol referral`). Never upgrade `Management representation`, `Auditor inference`, or `Unverified allegation` into `Verified fact`.
- **Investigation Firewall:** Routine findings cover only four control/process cause families (`design_gap`, `ownership_gap`, `knowledge_gap`, `incentive_or_workload_conflict`). Whenever facts indicate suspected deliberate override, fraud, collusion, misconduct, or rely on an `Unverified allegation`, **stop** causal and intent attribution, preserve neutral factual wording, populate `investigation_referral`, and route for investigation assessment.
- **No forced extrapolation or invented denominators:** Never invent a denominator or convert `Scope limitation` / `not_measured` into zero exceptions. Extrapolate sample results only when statistical sampling design and frame completeness support it; otherwise state `tested population`, `sample size`, `exception count`, `observed rate`, and `extrapolation limitation`.
- **Legal Currency Gate:** Keep live legal verification outside the writing agent when authoritative legal sources are unavailable. Before citing any statute, decree, or central-bank circular as binding criteria, verify in-force status, amendments/replacements, effective date covering the audit period, institutional applicability, and exact article. If unverified, emit `[UNVERIFIED LEGAL CURRENCY — EXCLUDE AS BINDING CRITERIA UNTIL VERIFIED]` and set `legal_currency_status: unverified_hold`.
- **Methodology-first ratings:** Apply rating criteria in strict precedence: **(1) Bank-approved methodology → (2) Engagement-approved criteria → (3) Configurable fallback scale** (explicitly tagged `[FALLBACK DRAFTING AID — NOT AN AUTHORITATIVE BANK RATING]`). Never emit a rating without naming `rating_methodology`.
- **Accountable role owners:** Assign remediation to an `accountable_role` (with `target_date`, `interim_control`, and `closure_evidence`). Name an individual only when formally assigned in the input record.

## Reference Map

Load only the reference file needed for the current step:

| File | Read when |
| --- | --- |
| [references/finding-elements-and-guardrails.md](references/finding-elements-and-guardrails.md) | Step 1–2: classifying evidence labels, triggering the Investigation Firewall, checking legal currency, enforcing sampling rules, drafting the 5-Cs, or building the canonical handoff record. |
| [references/rating-and-response-evaluation.md](references/rating-and-response-evaluation.md) | Step 3–5: applying the 3-tier rating precedence, evaluating management action plans, handling disputed causes or infeasible interim controls, escalating unauthorized risk acceptance, or running pre-issue QA. |
| [references/vn-banking-terminology.md](references/vn-banking-terminology.md) | Any step: drafting or translating Vietnamese banking governance, role, or audit-status terminology. |

## Workflow

Work through Steps 1–5 in order.

### Step 1: Lock evidentiary provenance and check gates

Read [references/finding-elements-and-guardrails.md](references/finding-elements-and-guardrails.md) and classify the incoming record before drafting prose:

1. **Tag every input assertion** with one of the six immutable evidentiary labels. Separate confirmed test facts from management statements and auditor inferences.
2. **Run the Investigation Firewall:** Check for suspected fraud, intentional override, collusion, personal benefit, or `Unverified allegation`. If triggered, halt intent/causal attribution immediately, keep wording strictly observable, set `investigation_referral: required`, and restrict any routine finding to cleared control gaps.
3. **Run the Legal Currency Gate:** Check every statutory or supervisory citation for verified in-force status, amendments, effective date, applicability, and exact article. Flag unverified citations with `[UNVERIFIED LEGAL CURRENCY — EXCLUDE AS BINDING CRITERIA UNTIL VERIFIED]` and record `upstream_holds`.
4. **Verify sampling basis:** Record whether the test used full-population analytics, statistical sampling (with documented design/frame), or judgmental/non-statistical sampling. Record `Scope limitation` where data is incomplete.

**Done when:** Every input claim carries an evidentiary label, `investigation_referral` and `legal_currency_status` are resolved or placed on hold, and `sampling_basis` is documented with no invented denominators.

### Step 2: Draft the 5-Cs causal chain

Draft the finding elements so each answers its challenge without editorializing:

1. **Title:** Consequence-led, under 12 words, containing no evaluative adjectives (`serious`, `egregious`, `poor`).
2. **Condition (`Verified fact`):** Quantified numerator, denominator (or explicit sample/limitation disclosure), period, population boundary, and worst instance in neutral language.
3. **Criteria:** Strongest verified authoritative source (verified law/regulation → adopted framework → internal policy with section/version → engagement-agreed criteria). Exclude unverified legal citations as binding criteria.
4. **Cause (`cause_status`):** Deepest actionable control or process root cause across the four routine families (`design_gap`, `ownership_gap`, `knowledge_gap`, `incentive_or_workload_conflict`), capped at the deepest link supported by direct evidence. Set `cause_status` to `approved`, `provisional`, or `disputed`. Never treat a disputed or inference-only cause as locked.
5. **Consequence:** Separate `consequence_realized` from `consequence_potential` in stakeholder currency. State explicitly what was *not* found when tested (e.g., *"no unauthorized disbursement identified in tested items"*).

**Done when:** All 5-Cs elements trace to input evidence, `cause_status` accurately reflects agreement/evidence depth, and zero intent or unsupported extrapolation appears.

### Step 3: Score severity under methodology precedence

Read [references/rating-and-response-evaluation.md](references/rating-and-response-evaluation.md) and assign `rating` strictly by precedence:

1. **Tier 1 — Bank-approved methodology:** Apply the bank's approved risk/finding matrix and definitions unconditionally; ignore conflicting fallback anchors.
2. **Tier 2 — Engagement-approved criteria:** Apply criteria documented in the engagement scoping/planning record when bank-wide thresholds do not cover the test.
3. **Tier 3 — Configurable fallback drafting aid:** Only when neither Tier 1 nor Tier 2 is provided, apply the configurable drafting aid and label `rating_methodology` and the output `[FALLBACK DRAFTING AID — NOT AN AUTHORITATIVE BANK RATING]`.
4. **Repeat / systemic flag:** If this finding repeats a prior audit issue or clusters with recurring `Medium` findings across periods/controls, flag `systemic_escalation` in `upstream_holds` for `audit-report-writer`.

**Done when:** `rating` and `rating_methodology` are explicitly populated (or held under `upstream_holds` if criteria are missing) with zero unanchored severity adjectives.

### Step 4: Evaluate corrective action, interim control, and response

Test the proposed recommendation or management action plan against the five action-plan tests:

1. **Cause closure:** Confirm the action closes the verified cause rather than merely cleaning up the exception symptom.
2. **Role & date:** Record `accountable_role` (never invent or default to a personal name unless formally assigned in the input) and an exact calendar `target_date`.
3. **Interim control & infeasibility rule:** For `High` or `Critical` findings, require an `interim_control` (compensating safeguard with owner role and cadence). If architecture or operations make an interim control genuinely infeasible, **do not invent one**—record `interim_control: infeasible — [reason]`, state the unmitigated interim exposure, and add CAE / Supervisory Board escalation to `upstream_holds`.
4. **Closure testability:** Write `closure_evidence` as an objective artifact/re-test condition an independent validator can verify later.
5. **Disputes & unauthorized risk acceptance:** If management accepts the condition but disputes the cause, preserve the `Verified fact` condition, label the conflicting positions (`Auditor inference` vs. `Management representation`), keep `cause_status: disputed` (provisional), and draft an *Auditor's Comment* if management's plan misses the verified control gap. If management proposes accepting risk above delegated authority, refuse closure and flag a GIAS Standard 11.5 escalation hold.

**Done when:** `accountable_role`, `target_date`, `interim_control`, and `closure_evidence` are complete (or explicit disagreement/escalation holds are recorded).

### Step 5: Emit the canonical handoff record and run pre-issue QA

Assemble the finding using the **Canonical Handoff Contract** defined in [references/finding-elements-and-guardrails.md](references/finding-elements-and-guardrails.md) (all 19 required fields) and run the 15-question QA check in [references/rating-and-response-evaluation.md](references/rating-and-response-evaluation.md).

**Done when:** Every canonical handoff field is populated, all holds/provisional statuses are explicit, and every pre-issue QA check passes.

## Authority Boundary

This skill drafts and quality-checks finding-level reasoning and produces structured handoff records. The Head of Internal Audit (CAE) and authorized governance bodies retain final judgment on root-cause resolution, severity ratings, investigation referrals, and risk acceptance.

## Provenance

Aligned with public IIA Global Internal Audit Standards (GIAS 2024), COSO Internal Control framework, and PCAOB audit documentation principles. All examples are synthetic.
