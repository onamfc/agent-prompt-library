# Gap & Bridge Architect

Builds the middle and the close of a video script: the problem, the solution, and the ask. Components 2, 3, and 4 of the storyboard.

Phase 2 of the [Video Script Director](../video-script-director/) pipeline, working alongside the [Hook Architect](../hook-architect/), which handles component 1.

## When to Use

- Building the body of a video script after the hook work is done
- An ad gets watched but does not convert — the problem is usually the gap or the CTA, not the hook
- The offer section reads like a feature list instead of a solution
- The CTA is vague, asks for too much, or asks for several things at once

## When NOT to Use

- No avatar profile exists yet — the pain points would be invented rather than grounded
- You only need the hook — use the [Hook Architect](../hook-architect/)
- You need proof attached to claims — that is the [Claim Validator](../claim-validator/)
- You are polishing an existing script into final form — that is the [Script Finalizer](../script-finalizer/)

## The Core Concept

Everyone is at **Point A**, their current situation with all its problems. Everyone has a **Point B**, the situation where those problems are gone. The space between is **the gap**.

Every advertisement that has ever worked painted that gap and positioned the offer as the vehicle across it. This agent paints the gap (component 2), builds the vehicle (component 3), and asks the viewer to get in (component 4).

## What Each Component Produces

**Component 2 — Identify The Gap**
- A plain one-to-two-sentence gap statement, before any elaboration
- 4–5 specific pain points, each marked validated or unvalidated
- 2+ alternatives they have already tried and failed with, each with why this offer is better
- The cost of not bridging the gap, broken into emotional, financial, and social
- Visual ideas throughout — showing the bugs beats talking about the bugs

**Component 3 — How Your Offer Bridges The Gap**
- 3+ specific results and benefits, stacked toward the threshold of logical certainty
- 3+ things that make the offer *unique* — different, not better
- 3+ reasons it is *better* than the competition — performance, not difference
- 4+ visual ideas for helping the viewer see themselves at Point B
- Proof slots, labeled with what each needs to prove, for the Claim Validator to fill

**Component 4 — Call To Action**
- The single funnel step being asked for — the next step, never the final one
- A specific, unambiguous ask
- A restated value proposition connected to the ask
- "The choice" contrast, when it fits

## The Most Common Mistake It Prevents

Rushing out of component 2. Scripts that pitch before the pain is genuinely felt do not convert, and the instinct of every business owner is to get to the pitch as fast as possible. This agent holds the line.

## Model Recommendations

| Model       | Suitability | Notes                                                              |
|-------------|-------------|---------------------------------------------------------------------|
| Claude Code | Excellent   | Reads the avatar profile and writes directly into the storyboard file |
| Cursor      | Excellent   | Same                                                                |
| Claude API  | Good        | Works well; keep the avatar profile pasted in context               |

## Context Requirements

Works best with:

- A completed avatar and offer profile
- Real customer language — reviews, support tickets, sales call notes. Pain points sourced from actual buyers outperform inferred ones by a wide margin.
- The specific next step in your funnel
- Competitor and alternative-solution names, including the DIY option and doing nothing

## Limitations

- Pain points drafted from inference are marked unvalidated, and they should be validated before you spend money on production.
- It will not invent case study numbers, guarantees, credentials, or years in business.
- Output is bullets and fragments by design. Word-for-word prose is Phase 4's job.
- It cannot make an undifferentiated offer differentiated. If the "why we're better" section is genuinely thin, it will say so rather than manufacture reasons.

## Customization

Fork and modify for:

- A fixed funnel structure where the CTA step is always the same
- Industries with mandated disclaimers or regulated claim language
- Longer formats — VSLs that need several gap sections rather than one
- Splitting into separate gap and offer agents if you want deeper work on each
