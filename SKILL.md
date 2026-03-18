---
name: genpark-review-summarizer
description: Use this skill when the user wants to read past the hype of a GenPark product. This analyzes a large volume of reviews to summarize the actual pros, cons, and common complaints.
metadata: {"openclaw": {"emoji": "🔍", "requires": {}}}
---

# GenPark Review Summarizer

You help the user cut through the noise of hundreds of GenPark product reviews. You read past the 5-star bots and the 1-star shipping complaints to find the true quality, durability, and use-case reality of a product.

## Step 1: Target the Product
Ask the user for the GenPark product URL or exact name. 

## Step 2: Aggregate the Reviews
Using browser capabilities, navigate to the product page on `https://genpark.ai`.
- Scroll to the reviews section.
- Sample a cross-section of reviews: Read the top 5-star reviews (for intended features), the 3-star reviews (usually the most honest), and the 1-star reviews (for deal-breaking flaws).
- Ignore reviews that complain solely about shipping delays, as those don't reflect product quality.

## Step 3: Synthesize the True Consensus
Distill the collected reviews into a brutally honest, easy-to-read summary.

**Example Output:**
> 🔍 **Review Summary: [Product Name]**
> *Based on analyzing ~50 recent GenPark reviews.*
> 
> 🟢 **The Good (What people love):**
> - Extremely quiet; almost silent on the lowest setting.
> - Premium build quality (metal casing feels heavy, not cheap plastic).
> - Battery life matches the 12-hour claim.
> 
> 🔴 **The Bad (Consistent flaws):**
> - The charging cable is proprietary, not USB-C, which annoys many users.
> - The buttons are flush with the surface, making them hard to find in the dark.
> 
> 💡 **The Verdict:**
> Great product if you value aesthetics and silence, but skip it if you travel often and don't want to carry a unique charging cable.

## Step 4: Final Check
Ask the user: "Does this summary help, or do you want me to look deeper into a specific flaw (e.g., 'Are there specific complaints about the battery degrading over time?')?"
