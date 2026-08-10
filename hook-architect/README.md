# Hook Architect

Produces the first five to ten seconds of a video ad — in volume, with the visual treatment for every one. Ten to twenty hooks per run, worked systematically across seventeen attention-getting concepts.

Phase 2 of the [Video Script Director](../video-script-director/) pipeline. Frequently used standalone.

## When to Use

- You need hooks. Many of them, fast.
- An ad has good watch-through but poor impressions-to-views — the hook is the problem
- You need hook variants to test against one existing body of an ad
- Someone opened their commercial with a logo animation and needs to be talked out of it

## When NOT to Use

- The rest of the script does not exist yet and you have no avatar profile — hooks written without buyer psychographics are guesses
- Written headlines for pages or emails — related craft, different constraints
- The problem is the offer, not the hook. A hook cannot rescue an offer nobody wants.

## Why This Component Gets Its Own Agent

A hook is five to ten seconds of a sixty-second video and determines the fate of the other fifty. Within those seconds the viewer decides whether to watch or scroll, against a backdrop of roughly 5,000 ads a day. The best offer behind a weak hook is simply never seen.

## The Five Rules

1. **Be different** — name the three most predictable openings in the category and rule them all out first
2. **Call out to your specific audience** — and let it disqualify everyone else. Never open with your name, brand, product, or logo.
3. **Use visuals to engage** — every hook ships with a visual treatment
4. **Ask questions** — "Do you have a pest problem?" calls out precisely to people who have one
5. **Offer value** — people smell a salesman instantly; teaching sidesteps the reflex and proves expertise instead of claiming it

The organizing idea behind all five: **enter the conversation already happening in the prospect's head.**

## The Seventeen Concepts

Big credible promise · Third-party statistics · Shock & awe · Humor · Question · Quote · Big promise · Human interest stories · Value-added content · News or relevant events · Intrigue · Secret systems · Prediction · Dominant emotion/solution · Problem/solution · Invitation · Mutually agreed upon fact

The agent generates at least one hook per plausible concept, then goes deeper on the ones that land.

## Output

A numbered table of hooks with concept, word-for-word line, visual treatment, and estimated seconds — plus top-three recommendations, suggested test pairs that isolate a single variable, and the category clichés it deliberately rejected.

Every hook is written as a spoken line, 12–25 words, inside five to ten seconds.

## Model Recommendations

| Model       | Suitability | Notes                                                            |
|-------------|-------------|-------------------------------------------------------------------|
| Claude Code | Excellent   | Reads the avatar profile from file and appends to the storyboard   |
| Cursor      | Excellent   | Same                                                              |
| Claude API  | Excellent   | Volume generation suits a plain conversation well                 |

## Context Requirements

Works best with:

- A completed avatar and offer profile from the [Avatar & Offer Researcher](../avatar-offer-researcher/)
- The platform the ad runs on (a YouTube pre-roll hook and a vertical social hook are not the same problem)
- Existing ads from the business, and from competitors, if you want clichés reliably avoided

## Limitations

- Without an avatar profile it will ask questions or write generically. Generic hooks are the failure mode this whole method exists to prevent.
- Will not invent statistics for the third-party-statistic concept — it drafts the structure and marks the source as yours to supply.
- Does not evaluate hooks against real performance data. Its top-three picks are informed judgment, not measurement. Test them.

## Customization

Fork and modify for:

- Platform-specific constraints — sound-off captioning, vertical framing, YouTube's 5-second skip point
- A house style that rules certain concepts in or out permanently
- Generating hooks in batches of 50+ for large-scale creative testing
- Adding concepts specific to your category
