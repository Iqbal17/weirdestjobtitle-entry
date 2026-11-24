"""Weirdest Job Title entry — "Chief Vibes Officer for Abandoned Shopping Carts".

Decision record
---------------
Candidates weighed (judge brief: a real-sounding job with one hilariously
specific twist beats a generic oddity; it must read instantly and be
pictureable on the first read):

1. "Senior Vice President of Apologizing to the Cloud" (55 chars)
   KEPT as a contender, then CUT. The corporate frame is real and the
   twist is funny, but "the cloud" is abstract — you cannot picture the
   person doing the job, and the joke needs a beat of thought to land.
   The judge rewards a twist that lands on the first read, so abstraction
   costs more than the seniority joke gains.

2. "Lead Nap Inspector, Night Shift, No Naps Allowed" (50 chars)
   CUT. The contradiction (inspecting naps you may never take) is funny,
   but the title trips over itself: three clauses in one title, and the
   punchline fights the job frame instead of twisting it. It reads like a
   joke wearing a job title as a costume, not like a real job with one
   odd twist.

3. "Professional Queue Stander for Other People's Errands" (54 chars)
   CUT. Real-sounding and specific, and queue-standing is a genuine odd
   job — but the twist is only "for other people", which is the entire
   premise of hired help. It is odd, not weird: no single detail makes
   you laugh, it just makes you nod.

4. "Chief Vibes Officer for Abandoned Shopping Carts" (48 chars) — CHOSEN.
   "Chief ... Officer" is a real corporate title shape (C-suite parody),
   "Vibes" is the gloriously unserious department, and "for Abandoned
   Shopping Carts" is one hilariously specific twist: a senior executive
   whose entire remit is the carts left in parking lots. You can picture
   the person instantly — clipboard, hi-vis vest, solemnly assessing the
   vibe of a stray cart. Funny on the first read, real-sounding, short.

Writing passes
--------------
Pass 1 (draft): "Chief Vibes Officer for Abandoned Shopping Carts".
Critique: the frame and twist both land, but is "for Abandoned Shopping
Carts" the sharpest phrasing? Tried a more corporate variant,
"Chief Vibes Officer, Abandoned Shopping Cart Division" (53 chars):
the "Division" suffix is more bureaucratic-real, but it cools the joke —
the officer now manages a division instead of serving the carts, and
"Cart" singular loses the herd of strays the plural gives you.

Pass 2 (revision): keep the Pass 1 wording. The preposition "for" makes
the carts the officer's constituency, which is the funny part, and the
plural "Carts" keeps the parking-lot image. 48 characters, well inside
the 60-character gate, and it reads in one glance.

Final entry: "Chief Vibes Officer for Abandoned Shopping Carts" (48 chars).
"""

import os

ENTRY = "Chief Vibes Officer for Abandoned Shopping Carts"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
