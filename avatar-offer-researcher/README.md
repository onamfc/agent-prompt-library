# Avatar & Offer Researcher

Runs the immersion exercise that every video script is built on — digging beneath what a business sells to why its clients buy. Produces a psychographic avatar profile, a prioritized benefit list, and a language bank.

Phase 1 of the [Video Script Director](../video-script-director/) pipeline. Useful standalone for any positioning or messaging work.

## When to Use

- Before writing any ad, script, landing page, or sales page
- When messaging is not landing and you suspect you are writing to the wrong person
- When you can describe what you sell but not why anyone buys it
- Onboarding a new client whose customers you do not yet understand
- Building the input for [Hook Architect](../hook-architect/) or [Gap & Bridge Architect](../gap-and-bridge-architect/)

## When NOT to Use

- Ad targeting parameters — this agent deliberately avoids demographics and geographics
- Quantitative market sizing or TAM analysis
- Product strategy or feature prioritization
- You already have a completed, validated avatar profile — go straight to Phase 2

## How It Works

**Draft, then confirm.** You give it one line — "pest control in Phoenix, $99 first treatment" — and it drafts a specific, detailed answer to all fifteen immersion questions by reasoning from what it knows about that industry and buyer. Then it walks you through confirming, editing, or replacing each one.

Drafts are always labeled as drafts. Nothing inferred is presented as something you said.

Where an answer would materially change the script and cannot be inferred — real price, real competitors, real results — it asks outright instead of inventing.

**If you run it inside the product's own repository, it reads first.** Marketing copy, pricing config, plan tiers, feature definitions, docs, and any published testimonials feed the offer-side questions, so you confirm a source-grounded draft instead of an industry-average one. Answers are tagged by origin — `[from the codebase]`, `[inferred]`, `[user-confirmed]`.

This is entirely optional. With no codebase the run is identical; it asks instead of reads, and it never requests a repository. Note that code answers the *offer* half of the exercise only — nothing in a repo tells you what humiliates your buyer or what keeps them awake, and the exercise does not get shorter because a codebase was there.

## The Fifteen Questions

| Section | Questions |
|---------|-----------|
| The Offer | What the offer is · Three biggest results · Price point |
| The Pain | Biggest problem or desire (financial + emotional) · What humiliates them · Top 3 daily frustrations · What they complain about to friends and family · What keeps them awake |
| The Stakes | Cost of not buying (emotional / financial / social) · What they want more than anything · What the result is worth to them |
| The Justification | Why the price is a no-brainer, in their voice · What sacred cows you kill |
| The Competition | Top 3 competitors · Why they'd choose you, in their voice |

Followed by a **ranked benefit list** — the offer's benefits ordered by how much the buyer cares about each one, which decides what the script leads with.

## Why Psychographics Only

Demographics and geographics decide who sees the ad. Psychographics decide what the ad says.

Nobody calls a pest control company without a pest problem. The homeowner with rats in the ceiling and the landlord with raccoons in an apartment complex share nothing demographically and everything psychographically. The script is written to the second thing.

## Model Recommendations

| Model       | Suitability | Notes                                                          |
|-------------|-------------|-----------------------------------------------------------------|
| Claude Code | Excellent   | Can write the profile to a file the rest of the pipeline reads   |
| Cursor      | Excellent   | Same, and can mine existing repo or docs content for buyer language |
| Claude API  | Excellent   | Conversational format suits the draft-and-confirm loop well      |

## Context Requirements

Works best with:

- The offer and its price
- Anything real from actual customers: reviews, support tickets, sales call notes, survey responses, recorded objections
- Existing case study numbers or results, if any
- Competitor names

Real customer language is the single biggest quality multiplier here. Inferred language is a competent guess; harvested language is the actual conversation in the buyer's head.

## Limitations

- Industry inference has limits. For niche B2B, regulated, or highly technical offers, the drafts will be noticeably weaker and need heavier correction.
- It will not invent case study numbers, testimonials, review counts, or competitor facts — those come back as blanks for you to fill.
- Produces one avatar per run by design. Multiple segments mean multiple runs and multiple scripts.

## Customization

Fork and modify for:

- Adding industry-specific questions to the fifteen
- Pre-loading an existing brand voice or customer research corpus
- Producing multiple avatars in one pass for offers with genuinely distinct buyer types
- Outputting to a CRM or research repository format instead of markdown
