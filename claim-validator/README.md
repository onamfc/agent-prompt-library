# Claim Validator

Audits every claim in a video script and attaches proof to it — or forces the claim to change. Produces a claim-by-claim verdict table, a proof asset inventory, and a prioritized list of proof worth going out and getting.

Phase 3 of the [Video Script Director](../video-script-director/) pipeline. Valuable standalone against any marketing asset that makes claims.

## When to Use

- Before producing any ad that makes a promise about results, speed, price, or superiority
- Auditing an existing script, landing page, or sales page for unsupported claims
- Planning what proof to collect — which testimonials, which case studies, which research
- Working in a regulated industry where the usual proof techniques are not legal
- Someone's ad is being dismissed as too good to be true

## When NOT to Use

- Legal or regulatory compliance sign-off. This agent flags risk; it is not counsel.
- Fact-checking claims about the world rather than about the offer
- You have no claims yet — build the storyboard first

## Why It Exists

Three things every viewer brings to an ad:

1. **Skepticism glasses.** They are actively looking for incongruency and for anything too good to be true. An unsupported claim gets the entire ad written off.
2. **Your ad is a disturbance, not a welcomed guest.** Nobody was hoping to see it. Engaging is not enough — it has to be believable.
3. **The ad carries the whole burden of belief.** It has to convince someone who has never heard of this business that this offer is the way across their gap.

## The Four Techniques

| Technique | What it is | Best for |
|-----------|-----------|----------|
| **Testimonials** | Real customers on camera | Nearly everything. Organic phone-shot for consumers, produced for B2B, long-form for warm audiences only |
| **Case studies** | Showing results in detail, not just claiming them | Anything quantifiable. Survives the "they hired actors" objection that testimonials cannot |
| **Third-party research** | Statistics, studies, and press from credible outside sources | Nearly every script, sprinkled anywhere |
| **Mutually agreed upon facts** | A verifiable fact the viewer already accepts, built into a logical case | Regulated industries where testimonials and case studies are prohibited |

## What It Delivers

**A claim audit table** with a verdict on every claim:

- **VALIDATED** — proof exists, ready to use, placed
- **SOFTEN** — rewrite to a defensible version (the rewrite is supplied)
- **CUT** — unprovable, remove
- **BLOCKED** — needs something from you, and it says exactly what

Plus a proof asset inventory, a prioritized acquisition list with the fastest route to each item, a started research punch list, and — when you need to collect testimonials — a full capture brief with the fifteen interview questions and the style to shoot in.

## Running It Inside the Product's Repository

Optional, and it sharpens exactly one class of claim: **claims about what the product does.** *"Set up in under two minutes," "works with any CRM," "no code required," "real-time."* Those are checkable against the implementation, and the agent checks them.

The common and most valuable outcome is not a clean pass or a hard fail — it is **SOFTEN**. The integration works with two of the five platforms the script implies. "Real-time" is a 30-second poll. You get the precise, still-compelling version of the claim before it reaches a shoot.

Two limits hold firm. Code proves **capability, never outcomes** — that the software can generate the report is not evidence a customer made $40,000 with it, so every results claim still needs a testimonial, case study, research, or agreed fact. And code is an **internal fact-check, not a fifth technique**: viewers cannot read your source and would not believe it anyway. A verified capability that needs proving on screen becomes a case study — a screen recording of the thing working.

With no codebase, none of this applies and the agent never asks for one.

## The Hard Rule

It does not invent proof. Not a statistic, not a study, not a testimonial, not a case study number, not a press mention — and not as a realistic-looking placeholder. Placeholders read as `[CLIENT NAME]: [RESULT] over [TIMEFRAME] — user to supply`, so nothing fabricated can accidentally survive into a shoot.

## Model Recommendations

| Model       | Suitability | Notes                                                                        |
|-------------|-------------|-------------------------------------------------------------------------------|
| Claude Code | Excellent   | Can maintain the research punch list as a persistent file across projects      |
| Cursor      | Excellent   | Same                                                                          |
| Claude API  | Good        | Full audit works; the punch list has to live outside the conversation          |

## Context Requirements

Works best with:

- The current storyboard or script
- An honest inventory of what proof you actually have: video testimonials, written reviews and their platforms, client results with real numbers, press mentions, guarantees, credentials, years in business, customers served
- Your industry's regulatory constraints, stated up front

## Limitations

- Cannot verify that proof you supply is accurate. It structures and places what you give it.
- Not legal advice. It knows that financial, healthcare, and legal advertising are constrained; it does not know your jurisdiction's specific rules.
- Cannot browse for third-party research unless the host environment provides web access. Otherwise it identifies the *kind* of source needed and you go find it.
- Its verdicts are about believability, not truth. A true claim with no proof still fails with a stranger.

## Customization

Fork and modify for:

- A persistent company-wide research punch list and proof library it draws on automatically
- Industry-specific compliance rules encoded as hard constraints
- Integration with a review platform so live reviews feed in
- A stricter or looser threshold on what counts as validated
