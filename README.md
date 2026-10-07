# human-eval-audit-skill

An agent skill for auditing human-rating studies (rubrics, instructions, response scales, assignment and integration config, analysis plans), plus the benchmark used to develop and test it.

- **`skill/`**: the installable skill (`audit-human-eval-study`), its changelog, an archive of the first version, and maintainer test cases.
- **`benchmark/`**: 165 synthetic study cases with planted defects, matched controls and incomplete-evidence variants; generators; a harness that runs coding agents and judges them; and the result reports.

The skill is built around one rule: **audit and suggest by default; change a study only when the owner says so.** A poor rubric is usually ill-defined, not wrong, and settling that is the owner's decision.

## What the skill does

| You say | The agent does |
|---|---|
| "Review / audit / check this" (no edit permission) | Reports findings, separates **determined fixes** (the owner's own materials settle the answer) from **open ambiguities**. For each ambiguity: a source quote, how raters' answers would differ by reading, 2-3 options with draft wording, a recommended default, and one question for the owner. Does not rewrite the rubric. |
| "Revise it" / "apply the fixes" | Applies determined fixes only. Unanswered owner questions stay outside the rater-facing text. |
| "Use your judgment on open choices" | Revises and settles open choices itself, listing every judgment call so the owner can review it. |

Findings are labelled `confirmed_defect` (a quoted source establishes it), `plausible_risk`, `cannot_verify` or `needs_human_judgment`. Missing media, UI or implementation is reported as not verified, never described from imagination.

## Install

Copy `skill/audit-human-eval-study/` (the directory, with its `references/`) into a skill location your agent loads.

| Agent | Project-scoped location | Personal location |
|---|---|---|
| Claude Code | `.claude/skills/audit-human-eval-study/` | `~/.claude/skills/audit-human-eval-study/` |
| Codex | `.agents/skills/audit-human-eval-study/` | host's user skill folder |
| Antigravity | `.agents/skills/audit-human-eval-study/` | host's user skill folder |
| Other agents | Put `SKILL.md` and `references/` somewhere in the repo and tell the agent to read `SKILL.md` first. | |

The skill uses only standard `SKILL.md` frontmatter and relative references, with no scripts, services or named browser. Keep one copy of the source; do not fork per agent.

Evidence status: in the benchmark the agent was **explicitly told to read `SKILL.md`**. Whether it triggers automatically from its description alone was not measured. When it matters, name the skill in the prompt.

## Using it at different steps of building a study

Each example is a prompt you can paste after installing.

**1. Drafting the rubric and instructions (before any code)**
> Use the audit-human-eval-study skill to review `rubric.md` and `instructions.md`. Don't change anything; give me the findings and the questions I need to answer.

Catches undefined terms ("plausible", "better"), unbalanced or mixed-polarity scales, leading wording, double-barreled items, missing escape options, and instructions that contradict their own examples.

**2. Writing the collection config or annotation UI**
> Audit `task_config.json`, `scale.json` and `assignment.csv` against `study.md`. Check scale direction and option codes, display-to-storage mapping, and whether position or order is confounded with system.

Uses `references/integration-checks.md`. Good for ordinal codes, stable item IDs after session resume, and assignment schedules.

**3. Reviewing a pull request that touches study materials**
> Use the audit-human-eval-study skill on the files changed in this PR. Report only supported findings; mark anything you can't verify.

Headless example (Claude Code print mode; adapt the flags to your agent and review the output before trusting it):
```bash
claude -p "Use the audit-human-eval-study skill on the changed files in this branch. Return JSON with audit, owner_questions, proposed_patches and coverage." --allowedTools "Read,Grep,Glob"
```
Untested as a CI gate; treat the result as a review aid, not a pass/fail check.

**4. Pre-launch check of a preview, screenshot or recording**
> Review this screenshot and the study instructions. Separate what is visible from what you cannot verify.

A screenshot gives visible-state feedback only; a runnable preview can support interaction checks. The skill never submits live ratings or changes production configuration.

**5. Checking a pilot export or test responses**
> Check `responses.csv` against `scale.json`: are answer codes mapped to the displayed options, and is each response tied to the right item?

**6. Reviewing the analysis plan or report**
> Audit `analysis_plan.md` and `report_draft.md`. Look for pseudoreplication, majority-vote ground truth, ranking on trivial differences, multiple comparisons, and conclusions beyond the design.

The textbook-mistake families in the benchmark target exactly these.

**7. Working through open questions with the owner (interactive)**
In a session where the owner is present, the skill tells the agent to ask the owner its questions (using the host's question tool, if any) before drafting a revision. In headless runs the questions come back in `owner_questions` and the agent stops short of settling them.

**8. Applying the owner's decisions**
> Revise the rubric. Apply only the determined fixes, and use these answers for the open questions: ...

or, to hand over judgment:

> Revise the rubric and use your own judgment on open choices; list every judgment call.

## Output shape

When a harness asks for JSON (as the benchmark does), the contract is:

```json
{
  "audit": [{"finding": "", "classification": "confirmed_defect | plausible_risk | cannot_verify", "evidence": [""], "suggestion": ""}],
  "owner_questions": [{"ambiguity": "", "why_it_matters": "", "options": [""], "recommended_default": "", "question": ""}],
  "proposed_patches": [{"path": "", "change": "", "rationale": ""}],
  "coverage": {"inspected": [""], "not_verified": [""]}
}
```
Interactive use has no imposed format.

## Benchmark in one page

- **Cases**: 165 synthetic cases from 55 families (control = sound for the target mechanism, defect = one planted mistake, partial = the decisive file withheld). 20 families cover interface and integration mistakes (position confounds, resume mapping, stale exports), 6 more come from a separate coverage pass (shipped as cases only, no generator), and 29 cover classic methods mistakes (leading questions, optional stopping, pseudoreplication, majority-vote truth, consent that misstates the task, and more). See [`benchmark/taxonomy/`](benchmark/taxonomy/TEXTBOOK_MISTAKES_TAXONOMY.md).
- **Scoring**: an audit-only judge scores six axes separately (key-issue handling, label calibration, evidence accuracy, ambiguity coverage, ambiguity quality, scope and abstention). There is deliberately **no total score**. The judge never sees the revised rubric and the arm is hidden.
- **Arms**: bare agent, skill v1, skill v2, skill v2.1 (not adopted).

Headline results (reports in [`benchmark/results/`](benchmark/results/)):

| Test | What it showed |
|---|---|
| Fresh cases (12 cases the skill was not tuned on; 3 models) | v2 raised ambiguity quality (1.10 to 1.67) and coverage (0.75 to 0.88), cut ambiguities settled by decree (13% to 2%) and cut unrequested rubric rewrites (44% to 3%). v1 did not replicate its earlier coverage gain. |
| Textbook cases (87 cases; Sonnet) | Detection is at ceiling for both arms. v2 differs on restraint: fewer overclaims on controls (0.83 vs 1.33), and no unrequested rewrites (0% vs 97% on defect cases). |
| Image reading (108 trials) | v2 reduced wrong major or critical claims (1.08 to 0.68 per run). v2.1's extra reading rule did not help and was dropped. |

Read these as a pilot: one trial per cell in most tests, a single judge family, synthetic cases, author-written keys and unvalidated reference lists. Judge test-retest agreement was 80-97% exact per axis.

## Run the benchmark

Prerequisites: Docker, [Harbor](https://pypi.org/project/harbor/), Python 3.11+, and API keys in your environment (`ANTHROPIC_API_KEY` for the agent trials, `OPENAI_API_KEY` for the judge; `JUDGE_MODEL` overrides the judge model). Trials and judging cost real money; start with a small experiment.

```bash
pip install -r benchmark/harness/requirements.txt
docker build -f benchmark/harness/docker/Dockerfile.runtime -t study-audit-runtime:20261006 benchmark/harness/docker
docker build -f benchmark/harness/docker/Dockerfile.claude  -t study-audit-runtime-claude:20261006 benchmark/harness/docker
cd benchmark/harness
python experiments.py tb build        # tasks for 87 textbook cases, bare vs v2
python experiments.py tb ref          # frozen per-case references (judge model)
python run_trials.py tb               # run the agent trials in Docker via Harbor
python experiments.py tb prep         # blind packets for the judge
python experiments.py tb judge 1 && python experiments.py tb judge 2
python summarize_tb.py
```
Experiments: `tb` (textbook cases), `img` (image reading), `rev` (revision with explicit permission). Outputs go to `workdir/` (override with `BENCH_WORKDIR`). Keep concurrency modest: too many parallel trials exhausted Docker's network address pool in our runs. The generators rebuild 49 of the 55 families; do it with `python benchmark/generators/build_dataset.py --help`.

## Known limits

- Reference lists and issue keys were written or generated by the authors and the judge model; no independent human adjudication yet.
- Revision-with-permission results are not reported here (runs exist; not yet judged).
- Image reading is only partly helped by the skill; Haiku in particular misreads images.
- Only synthetic cases are included. Externally sourced, public-instrument-derived and account-fixture cases from the development set were left out.
- No license file yet; choose one and confirm rights before making the repo public.
