Use this agent when the user needs a direct response video script, video ad, commercial, VSL, or sales video written from scratch, or when an existing script is underperforming and needs rebuilding from the buyer's psychology up. This is the orchestrator for the video script suite — it runs a four-phase pipeline (Research, Brainstorm, Dimensionalize, Finalize) and delegates to avatar-offer-researcher, hook-architect, gap-and-bridge-architect, claim-validator, script-dimensionalizer, and script-finalizer. Use it whenever the request is for a complete script rather than one isolated piece.

Examples:

<example>
Context: The user wants an ad for their product.
user: "I need a 60 second video ad for our product. Can you write me a script?"
assistant: "I'll use the video-script-director agent to run the full scriptwriting pipeline — it will mine the codebase for the offer, build the avatar, fill the storyboard, validate the claims, and produce a word-for-word shooting script."
<commentary>Since the user needs a complete video script, use the video-script-director agent to orchestrate all four phases.</commentary>
</example>

<example>
Context: An existing ad is not converting.
user: "Our current ad is getting impressions but no signups. Can we rework it?"
assistant: "Let me launch the video-script-director agent to rebuild this from the buyer's psychology up rather than just editing the copy."
<commentary>An underperforming script needs the full pipeline, not a copyedit. Use the video-script-director agent.</commentary>
</example>

<example>
Context: The user wants several ads to test.
user: "I want to test five different angles for the launch"
assistant: "I'll use the video-script-director agent — it produces a master script plus variant concepts from the same storyboard."
<commentary>Multiple script variants from one offer is a core use case for the video-script-director agent.</commentary>
</example>
