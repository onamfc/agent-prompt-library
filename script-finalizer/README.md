# Script Finalizer

Turns a crowded storyboard into one finished, word-for-word, production-ready script — then pressure-tests it before anyone spends money shooting. Produces the script, a runtime estimate, a full production shot list, and the variants.

Phase 4 of the [Video Script Director](../video-script-director/) pipeline.

## When to Use

- The storyboard is populated and it is time to write the actual script
- You have a rough script and need it tightened, timed, and turned into a shot list
- You need multiple ad variants from one body of creative work
- A script reads fine on the page and falls apart when spoken aloud

## When NOT to Use

- The storyboard is not populated yet — there is nothing to select from
- You want new creative ideas — this stage deliberately invents nothing
- You need proof attached to claims — send it to the [Claim Validator](../claim-validator/) first
- Copyediting a script that is already final and shot-listed

## The Two Principles

**The 80/20.** A full storyboard holds far more than one video can carry. Roughly 20% of the ideas produce 80% of the result. Finding that 20% is the whole job.

**Never work in isolation.** Everyone holds biases about their own offer, and unchecked biases end up in the script. Two minds produce something two to three times stronger — which is why a complete script is achievable in a single working session by a pair and not by one person. This does not require a business partner; it requires another set of eyes and a refusal to accept "looks great, no changes." The agent supplies the exact ask: three to five objections, in writing.

Fixing a script is far cheaper than fixing a produced video.

## The Seven Steps

1. Read the storyboard several times, highlighting the strongest components
2. Test whether the highlighted pieces cohere — un-highlight the outliers
3. **Duplicate the storyboard, never overwrite it.** Delete non-highlighted material from the copy only
4. Expand bullets into word-for-word sentences and paragraphs
5. Run the read-aloud pass
6. Collect objections from three outside readers and produce round two
7. Generate the variants

## The Read-Aloud Pass

Non-negotiable, and it cannot be done silently. Lines that are perfectly clear in the head routinely collapse when spoken. The agent simulates it line by line — flagging tongue-twisters, run-on breath lines, unnatural stress, accidental repetition, and anything a real person would never say out loud — then instructs you to read it aloud yourself three times, and aloud to three other people.

## Why the Variants Matter

The most commonly skipped and highest-leverage step.

Given everything on the original storyboard, the material supports an enormous number of finished scripts. What was written was not one script — it was the foundation for a year of advertising. Variation is king in digital marketing: more variants means more testing, which means actually learning what sells the offer.

Every run produces at least three variant concepts by recombining what is already on the board — a different hook against the same body, a rotated value stack, a testimonial-led retargeting cut, an objection-handling cut, a compressed 15- or 30-second version.

## What You Get

1. The final storyboard, v2.0
2. The word-for-word script with running timecodes and inline visual direction
3. A runtime estimate at ~150 spoken words per minute
4. A production shot list, grouped into original footage, stock, motion graphics, screen recordings, and existing assets
5. Read-aloud flags with rewrites
6. A feedback brief for your three readers
7. At least three variant concepts
8. An unused-inventory list — everything cut, preserved for the next script

## Model Recommendations

| Model       | Suitability | Notes                                                                    |
|-------------|-------------|---------------------------------------------------------------------------|
| Claude Code | Excellent   | Handles the duplicate-never-overwrite versioning discipline properly       |
| Cursor      | Excellent   | Same                                                                      |
| Claude API  | Good        | Full output works; you manage storyboard versioning yourself               |

## Context Requirements

Works best with:

- A fully populated, dimensionalized storyboard
- The target runtime and the platform
- The avatar profile, so buyer language survives into the final copy
- The Claim Validator's audit, so nothing unsupported slips through

## Limitations

- It genuinely cannot hear the script. Its read-aloud simulation catches most problems; you still have to read it out loud.
- Runtime estimates at 150 wpm are approximate. Delivery pace, pauses, and B-roll sections move real runtimes considerably.
- It selects from what exists. A thin storyboard produces a thin script, and it will say so rather than invent filler.
- Shot lists are descriptive, not visual. No frames or boards.

## Customization

Fork and modify for:

- A house style guide applied at the writing stage
- A different runtime formula matched to your usual talent's delivery pace
- Shot list output in your production team's format
- Platform-specific cutdowns generated automatically — 6s, 15s, 30s, 60s from one master
