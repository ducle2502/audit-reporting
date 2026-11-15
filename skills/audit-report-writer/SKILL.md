---
name: audit-report-writer
description: >-
  Assemble internal audit reports, executive summaries, supervisory board memos,
  owner decision briefs, project remediation packs, risk-acceptance escalations,
  and closing decks aligned with GIAS Standard 15.1. Use when aggregating vetted
  findings into engagement deliverables, routing audit outputs by governance
  altitude, forming a holistic audit opinion, or verifying cross-layer
  consistency.
---

# IA Audit Report Writer

Synthesize vetted finding records (conforming to the `audit-finding-writer` Canonical Handoff Contract) and engagement scope records into audience-calibrated reports, briefs, and remediation packs aligned with IIA GIAS Standard 15.1.

Follow the user's language (English, Vietnamese, or bilingual). Keep structural rules language-neutral; consult [references/vn-banking-terminology.md](references/vn-banking-terminology.md) only when writing or translating Vietnamese banking governance terms.

## Core Guardrails (Non-Negotiable)

- **Upstream boundary & root-cause mutability:** Never silently rewrite upstream `Verified fact` figures, finding ratings, `accountable_role`s, `target_date`s, or `approved` causes. Keep any `disputed` or `provisional` cause explicitly marked provisional rather than treating it as locked. Flag defective or incomplete upstream inputs with `[UPSTREAM FINDING HOLD]` for `audit-finding-writer` / CAE resolution.
- **Evidentiary status is immutable:** Preserve all six evidentiary labels (`Verified fact`, `Management representation`, `Auditor inference`, `Unverified allegation`, `Scope limitation`, `Investigation or protocol referral`). Never present `Management representation` or `Auditor inference` as `Verified fact`.
- **Non-mechanical holistic conclusion:** Finding ratings inform the engagement opinion but never determine it mechanically unless an explicit bank-approved formula governs. Formulate the overall conclusion holistically across **scope coverage, control pervasiveness, compensating controls, repeat/systemic patterns (including clustered `Medium` findings), management response quality, and evidence/scope limitations**.
- **Insufficient-evidence gate:** When `Scope limitation` or missing evidence prevents concluding on an engagement objective, refuse an unqualified opinion and issue a scope-limited, qualified, or disclaimed conclusion per bank methodology.
- **Investigation firewall:** Strip investigative details, suspect names, and `Unverified allegation` narratives from all routine governance and project deliverables. Include at most a neutral one-sentence referral notice only where bank protocol authorizes it.
- **No forced extrapolation:** Extrapolate sample exceptions only when the upstream record confirms statistical sampling design and frame completeness; otherwise report `tested population`, `sample size`, `exception count`, `observed rate`, and `extrapolation limitation`.
- **Legal currency gate:** Never assume any statute or central-bank circular is currently in force; exclude `[UNVERIFIED LEGAL CURRENCY — EXCLUDE AS BINDING CRITERIA UNTIL VERIFIED]` items as binding criteria until externally verified.
- **Canonical-value consistency:** Maintain canonical consistency of counts, currencies, denominators, ratings, `accountable_role`s, and `target_date`s across every report layer. Presentation rounding is permitted in executive/board layers only when the unrounded source value remains traceable and rounding does not alter meaning.

## Reference Map

Load only the reference file needed for the current step:

| File | Read when |
| --- | --- |
| [references/governance-routing-profiles.md](references/governance-routing-profiles.md) | Step 2: verifying bank charter distribution rules and routing outputs across the configurable default 4-tier bank chain (Owner, Supervisory Board, Head of IA, Project Board). |
| [references/gias-aligned-report-structures.md](references/gias-aligned-report-structures.md) | Step 3: selecting the GIAS 15.1-aligned bank assurance structure, forming a holistic non-mechanical opinion, handling recurring Mediums, or issuing scope-limited conclusions. |
| [references/altitude-numbers-and-consistency.md](references/altitude-numbers-and-consistency.md) | Step 4–5: applying `C/M/G` altitude rules, sample non-extrapolation phrasing, GIAS 11.5 risk-acceptance escalation, closing decks, and cross-layer canonical checks. |
| [references/vn-banking-terminology.md](references/vn-banking-terminology.md) | Any step: drafting or translating Vietnamese banking governance or audit-status terminology. |

## Workflow

Work through Steps 1–5 in order.

### Step 1: Lock upstream finding records and enforce firewalls

Verify every incoming finding against the 19-field Canonical Handoff Contract before aggregating:

1. **Check upstream holds:** Identify any `upstream_holds`, `unverified_hold` legal citations, provisional/disputed causes, or `[FALLBACK DRAFTING AID]` rating labels. Carry them forward transparently; never mask or drop them.
2. **Apply Investigation Firewall:** Segregate any `investigation_referral: required` or `Investigation or protocol referral` material out of governance and project drafts.
3. **Preserve evidentiary status:** Confirm `Management representation` items (such as unverified verbal remediation claims) remain labeled as representations, not `Verified fact`.

**Done when:** Every finding's evidentiary status, holds, cause status, and investigation boundary are verified and segregated.

### Step 2: Resolve governance audience and charter routing

Read [references/governance-routing-profiles.md](references/governance-routing-profiles.md) and configure the output set:

1. **Apply bank charter / statutory override first:** Check whether local banking law or bank charter restricts direct shareholder/owner distribution or designates an Audit Committee / Board Risk Committee as the supervisory recipient.
2. **Apply the configurable default 4-tier profile** when no override is specified:
   - **Owner of the Bank (Principal Decision Tier):** 1-page capital, regulatory license, and enterprise-exposure brief ending with an **explicit decision request**.
   - **Head of the Supervisory Board:** Cruising-altitude oversight memo / Executive Summary highlighting holistic conclusion, systemic/repeat themes, scope limitations, escalated risk acceptances, and an explicit `note / discuss / decide` ask.
   - **Head of Internal Audit (CAE):** Full **Bank assurance report structure aligned with GIAS Standard 15.1** (scope, exclusions, limitations, conformance, holistic opinion rationale, complete finding blocks, prior-issue status, and detailed appendix).
   - **Project Board:** Action-focused remediation pack with Summary of Findings table, `accountable_role`, `target_date`, `interim_control` (or infeasibility notice), dependencies, and **verifiable closure evidence criteria**.

**Done when:** Deliverable format(s), charter authorization, and required audience elements are selected.

### Step 3: Formulate the holistic engagement conclusion

Read [references/gias-aligned-report-structures.md](references/gias-aligned-report-structures.md) and synthesize the overall conclusion:

1. **Assess all six holistic dimensions** (never derive the rating solely by counting findings unless a bank-approved formula explicitly governs): scope coverage, control pervasiveness, compensating controls, repeat/recurring issues (evaluating whether clustered `Medium` findings indicate a systemic control weakness), management response and interim control adequacy, and evidence/scope limitations.
2. **Apply the Insufficient-Evidence Gate:** Where `Scope limitation` blocks testing of material controls or periods, issue a scope-limited, qualified, or disclaimed conclusion per bank methodology and state the unexamined exposure explicitly.
3. **Apply the Risk-Acceptance Gate (GIAS 11.5):** Where management proposes accepting risk above delegated authority or on regulatory-prohibited items, refuse closure and route an explicit risk-acceptance escalation to the Supervisory Board / authorized Owner tier.

**Done when:** The overall opinion is justified across all six holistic dimensions (or explicitly scope-limited/disclaimed) and cites the governing bank methodology.

### Step 4: Draft deliverables by altitude and sample honesty

Read [references/altitude-numbers-and-consistency.md](references/altitude-numbers-and-consistency.md) and write the target outputs:

1. **Write the Executive Summary / Brief last and place it first** using Pyramid Principle (verdict first, consequence themes, verified strengths, finding/prior-issue summary, committed executive action + interim controls, base rates, explicit governance ask).
2. **Enforce altitude (`C/M/G`):** Keep Owner and Supervisory Board openings at cruising altitude (`C`) with plain, de-jargoned business consequences and calibrated confidence statements. Keep Project Board and Head of IA layers grounded with exact mechanisms, sample disclosures, and closure criteria.
3. **Format numbers honestly:** Show non-statistical samples using all five required elements (`tested population`, `sample size`, `exception count`, `observed rate`, `extrapolation limitation`). Keep unrounded source numbers traceable in detailed tables whenever executive layers apply presentation rounding.

**Done when:** Every requested audience deliverable is drafted at the right altitude with zero unsupported extrapolations, unverified legal citations, or personal-name defaults.

### Step 5: Run canonical-value consistency and AI-QC sweep

Audit every layer (Cover, Owner Brief, Supervisory Board Memo, Executive Summary, Summary of Findings Table, Finding Blocks, Appendices, Project Board Pack):

1. Confirm canonical consistency of all counts, currencies, denominators, ratings, `accountable_role`s, `target_date`s, `cause_status` tags, and `closure_evidence` criteria.
2. Confirm every mandatory audience element is present (explicit decision request for Owner; `note/discuss/decide` ask for Supervisory Board; closure evidence criteria for Project Board; GIAS 15.1 baseline elements for Head of IA).
3. Confirm zero investigative leaks, zero upgraded evidentiary labels, and zero invented facts.

**Done when:** All cross-layer canonical checks and audience-completeness gates pass.

## Authority Boundary

This skill synthesizes vetted findings, enforces governance routing, and verifies cross-layer consistency. The Head of Internal Audit (CAE) and authorized governance bodies own the final engagement opinion, external regulatory notifications, investigation governance, and risk-acceptance approvals.

## Provenance

Aligned with public IIA Global Internal Audit Standards (GIAS 2024), COSO Internal Control framework, and PCAOB audit documentation principles. All examples are synthetic.
