# AGENT OPERATING CONTRACT

> هذا الملف جزء من كل أمر تنفيذي في هذه المكتبة. كل أمر يبدأ بقراءته والالتزام به.
> النص التنفيذي بالإنجليزية لأنه موجَّه إلى عميل برمجي.
>
> This file is referenced by every executable prompt in `EXECUTION_BLUEPRINT/PHASES/`.
> It exists so that each prompt stays standalone in a fresh session without
> repeating these rules, while still never depending on hidden conversation context.
> It is a specified project file, not conversation memory.

## 0. Status of the source material

The requirements behind this blueprint come from exactly one source artifact:
`Sketch_Design_Model_Gateway_Observability_v11.md`, a 77-sheet Markdown export
of the Sketch Design workbook. Every requirement reference in
`EXECUTION_BLUEPRINT/_registry/requirements.tsv` points into it as
`<sheet number>:<row>`.

That export states about itself that it carries every populated worksheet cell
including formula expressions, but that Excel-specific interactive features and
visual styling cannot be represented. So cell comments, dropdown validation,
conditional formatting, charts, images and defined names are outside this
blueprint's coverage, and their absence rests on the export's own statement
rather than on an independent inspection of the binary workbook. If you are
told a requirement exists that you cannot find in the export, do not reconstruct
it from memory — ask for it.

The source describes an **architecture and operating baseline**. It states about
itself, in its own words, that it is "not proof that the platform is built or
tested" (sheet 00 row 14) and that "the runtime environment was not accessed"
(sheet 68 row 9). Therefore:

- Treat every row of the source as a **requirement statement**, never as
  evidence that something already works.
- Never convert a source status word (`DEFINED`, `DESIGNED`, `SPEC`,
  `PROPOSED`, `UNVERIFIED`, `NOT TESTED`, `PLANNED`, `DESIGN ONLY`) into
  `READY`, `DONE`, `VERIFIED` or `PASSING`.
- `EXECUTION_BLUEPRINT/_registry/requirements.tsv` is the requirement registry.
  Its `class` column tells you whether a statement is `CONFIRMED` (stated by the
  source), `DERIVED` (a logically necessary consequence), `PROPOSED` (an
  engineering recommendation that is **not** in the source) or `UNKNOWN`.
  Never silently promote `PROPOSED` or `UNKNOWN` to an approved requirement.

## 1. Inspect before you change

Before editing anything, establish the actual state of the project:

1. List the repository and read the build, test and dependency manifests.
2. Run the project's existing test and lint commands and record the real output.
3. Read the modules you are about to touch, in full.
4. If the repository is empty or the component does not exist yet, say so
   explicitly in your report rather than assuming a layout.

If what you find contradicts this prompt, stop and report the contradiction.
Do not implement around it.

## 2. Root cause, then the smallest correct change

- Diagnose the actual cause of a failure before changing code.
- Implement the smallest change that correctly and durably solves the stated
  problem at production quality.
- Do not refactor, re-platform, rename or restructure anything the prompt did
  not ask you to touch.
- Do not introduce a framework, provider, language or architectural pattern that
  is neither supported by the source nor recorded as an accepted ADR in
  `docs/adr/`. If you believe one is needed, write the ADR and ask.

## 3. Preserve what works

- Never delete or rewrite working functionality to make a new feature fit.
- Never drop, truncate or destructively migrate a table that holds data.
  Write forward migrations; keep them reversible or explicitly document why
  they are not.
- Never rotate, overwrite, print, log or commit a secret. If you need a
  credential that is absent, stop and request it by name.
- Never run a command against a production environment. Staging, sandbox and
  local only, unless the prompt names production and the owner authorized it in
  writing.

## 4. Authorization boundary

Make routine technical decisions yourself (naming, file placement consistent
with the repository, test structure, library-level choices already present in
the manifest).

**Stop and request explicit authorization** before anything destructive, costly,
irreversible or scope-changing. That includes: deleting data or infrastructure,
provisioning paid resources, calling a paid model provider outside an agreed
budget, sending anything to a third party, publishing or deploying, changing a
payment or billing path, altering a recorded reviewer decision or a released
delivery, and widening the scope beyond the prompt.

## 5. Evidence or it did not happen

A task is complete only when you can show it works. In your completion report:

- Paste the **actual** command invocations and their **actual** output.
- Name the files you created or changed, with line counts.
- State which acceptance criteria passed, which failed, and which you could
  not execute — and why.
- If you could not verify something, write `NOT VERIFIED` and explain the
  blocker. Do not pad the report to look complete.

**Never fabricate** a test result, a log line, a trace id, a passing build, a
benchmark number, an integration that is not wired up, or a provider response.
A plausible-looking invented result is the single most damaging thing you can
produce in this project, because the whole governance model of this platform is
evidence-based readiness (source sheet 02 row 9, ADR-008).

## 6. Continue or stop

Continue to the next step without asking when: the work is inside the prompt's
stated scope, you have the inputs you need, and nothing in section 4 applies.

Stop and report when: a prerequisite is missing, a credential or contract is
absent, the source is contradictory on the point you need, a test fails for a
reason outside the prompt's scope, or finishing would require an action from
section 4.

## 7. Resuming after context loss

Every prompt is written to be executable in a fresh session. If you are resuming:

1. Read this file.
2. Read `EXECUTION_BLUEPRINT/00-START-HERE.md` and
   `EXECUTION_BLUEPRINT/02-EXECUTION-ROADMAP.md`.
3. Read `EXECUTION_BLUEPRINT/_registry/requirements.tsv` for the requirement IDs
   your prompt names.
4. Read `docs/EXECUTION-LOG.md` if it exists — that is the running record of what
   previous prompts actually accomplished and verified.
5. Re-establish actual project state per section 1 before trusting any earlier
   claim, including your own.

## 8. The execution log

Every prompt appends one entry to `docs/EXECUTION-LOG.md` (create it if absent):

```
## <PROMPT-ID> — <date UTC> — <RESULT: COMPLETE | PARTIAL | BLOCKED>
Requirements: <req ids>
Changed: <files>
Commands run: <command> -> <exit code>
Evidence: <paths to test output, traces, screenshots>
Acceptance: <criterion> -> PASS | FAIL | NOT EXECUTED
Blockers: <what stopped you, or "none">
Next: <next prompt id>
```

This log is the continuity mechanism for the whole library. Writing it is not
optional, and it records what actually happened, not what was planned.

## 9. Language

Code, identifiers, commit messages, API fields, configuration keys and tests are
in English. User-facing product copy is Arabic-first with RTL layout, per the
source (sheet 54 row 12: RTL, mobile camera, accessibility). Do not translate
identifiers.

## 10. What this blueprint does not authorize

This blueprint is an execution plan. It does not authorize you to:

- present the platform as production-ready, certified or compliant;
- claim a Saudi authority integration works before a provider agreement,
  credentials and a successful sandbox call exist (sheet 68 row 6);
- issue, imply or generate a licensed engineering approval without a qualified
  human reviewer inside their recorded eligibility scope (ADR-010, sheet 35
  row 6);
- treat a LiDAR or photogrammetry measurement as a certified survey
  (sheet 57 row 6);
- quote a commercial price from the source rate card, because every rate in it
  is zero except VAT (sheet 19 row 54).
