# Video Script Director

Orchestrates a complete direct response video script from a one-line description of what you sell. Runs a four-phase pipeline and delegates each phase to a specialist, producing a word-for-word script with visual direction for every line.

**This is the agent you call.** The other six in the suite are its specialists, each also usable standalone.

## The Suite

```
video-script-director          ← start here
├── avatar-offer-researcher    Phase 1 — Research
├── hook-architect             Phase 2 — Attention Getter
├── gap-and-bridge-architect   Phase 2 — Gap, Bridge, CTA
├── claim-validator            Phase 3 — Proof and believability
├── script-dimensionalizer     Phase 3 — Weight and differentiation
└── script-finalizer           Phase 4 — Selection, writing, variants
```

| Phase | What happens | Specialist |
|-------|--------------|------------|
| 1. Research | Immersion exercise on the buyer's psychographics and the offer's real value | [Avatar & Offer Researcher](../avatar-offer-researcher/) |
| 2. Brainstorm | Storyboard filled with raw volume across all four components | [Hook Architect](../hook-architect/), [Gap & Bridge Architect](../gap-and-bridge-architect/) |
| 3. Dimensionalize | Proof attached, differentiation techniques applied | [Claim Validator](../claim-validator/), [Script Dimensionalizer](../script-dimensionalizer/) |
| 4. Finalize | 80/20 cut, word-for-word write, read-aloud pass, variants | [Script Finalizer](../script-finalizer/) |

## When to Use

- Writing a video ad, commercial, VSL, or sales video from scratch
- Rebuilding an underperforming script from the buyer's psychology up
- Producing many script variants from one offer for testing
- Scripting for a client whose industry you do not know well

## When NOT to Use

- Long-form content that is not selling something — a documentary, a brand film, a tutorial
- Written copy with no video component — landing pages, emails, ads without a script
- You only need one piece (just hooks, just a value stack) — call that specialist directly
- Editing an existing finished script for tone or length — that is a copyedit, not this process

## How It Works

You provide: what you sell, roughly who it is for, the price, the next step you want viewers to take, and where it will run.

The director drafts plausible answers to the fifteen immersion questions from what it can infer about your industry, then walks you through confirming or correcting each one. Nothing about your buyer is invented and presented as fact — drafts are labeled as drafts.

From there it runs the phases in order, gating between each one so you can redirect before work compounds on a bad assumption.

## Running It Inside a Codebase

Optional, and worth doing when the repository belongs to the business being advertised. The director mines marketing copy, pricing config, plan tiers, feature definitions, and docs before intake, then opens by showing you what it found instead of a blank form. Downstream, `avatar-offer-researcher` uses it for the offer-side questions and the language bank, and `claim-validator` verifies capability claims against the actual implementation.

Nothing requires it. With no repository present the pipeline is identical — the agents ask instead of read, and never request access to one. Code answers what the product *is*; it never answers who the buyer is or why they buy.

One practical note: `.scripts/` is written to the current working directory — wherever the session was started, not a fixed or global location. Start a session inside a subproject and the script files live in that subproject. The director does not walk up to a workspace root or consolidate runs into one shared folder. In a source repo it says where it is writing before it writes and offers to keep it untracked.

## Installing the Suite Elsewhere

The prompts depend on nothing in this repository. To run the suite in another project, convert each `prompt.md` to your tool's agent format — for Claude Code, a file in `~/.claude/agents/` or `<project>/.claude/agents/` with `name` and `description` frontmatter.

The director refers to its specialists by slug (`avatar-offer-researcher`, `hook-architect`, `gap-and-bridge-architect`, `claim-validator`, `script-dimensionalizer`, `script-finalizer`). Install them under those names and it invokes them as subagents. Install only the director and it runs all four phases itself, with the same phase order, deliverable counts, and gates.

## Output Location

```
.scripts/<offer-slug>/
├── 01-avatar-offer.md      Avatar and offer profile
├── 02-storyboard-v1.md     Raw brainstorm — never overwritten
├── 03-storyboard-v2.md     Dimensionalized and concentrated
└── 04-script-final.md      Word-for-word script + shot list
```

Version 1 of the storyboard is deliberately preserved. The ideas cut from one script are the raw material for the next several, which is most of the value of doing the work once.

## Model Recommendations

| Model       | Suitability | Notes                                                                             |
|-------------|-------------|-----------------------------------------------------------------------------------|
| Claude Code | Excellent   | Can write and version the storyboard files, and invoke the specialists as subagents |
| Cursor      | Good        | Full pipeline works; specialist delegation is manual                              |
| Claude API  | Good        | Works well as a single long conversation; keep the storyboard inline               |

## Context Requirements

Works best with:

- A clear description of the offer and its price
- The specific next step you want a viewer to take
- Any real proof you have: reviews, testimonials, client results, press, guarantees
- Competitor names, if the market is competitive
- Anything you know from actually talking to customers — their words beat inferred ones every time

## Limitations

- Only as good as the avatar profile it is built on. Rushing Phase 1 degrades everything downstream.
- Cannot supply proof you do not have. It will tell you exactly which claims are unsupported and what to go get.
- Does not know your competitors' actual pricing or features. It structures the comparison; you verify the facts.
- Produces the script, not the video. Shooting, editing, and media buying are out of scope.
- Regulated industries (finance, healthcare, legal) constrain which validation techniques are legal. Raise this at intake — the [Claim Validator](../claim-validator/) handles it, but only if it knows.

## Customization

Fork and modify for:

- A fixed house style or brand voice applied at the finalize stage
- Different default runtimes (a 6-second bumper suite versus a 20-minute VSL)
- Platform-specific constraints — vertical framing, sound-off captioning, YouTube pre-roll's 5-second skip point
- An in-house proof library the Claim Validator draws on automatically
- Non-video formats that share the same structure, like webinar or sales call frameworks
