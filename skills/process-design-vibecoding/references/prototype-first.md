# Prototype-first product review

User-requested addition, 2026-10-27. Required for new user-facing products and material UX changes in the full workflow.

## Create the smallest useful experience

After discovery, record the actor, goal, primary journey, important failure/correction path and assumptions in a short draft of the canonical spec. Then build the interactive preview before full architecture, backend, database, integrations or extensive documentation. Do not require a complete production specification to learn from the prototype.

Default to one coherent concept with a few essential states. Use local HTML/CSS/JavaScript, existing project components or an available preview surface, whichever is cheapest and adequate. For a conversational bot, show an actual chat: user message or synthetic photo, bot response, clarification/retry, and the next user turn. Demonstration controls belong outside the simulated product when the intended product has no menus.

Make the transitions and basic input work. Use realistic synthetic content and prepared replies; label the simulation clearly. Do not copy unrelated branding, menus, dashboards or account flows into the requested experience. Show enough design to judge the journey; avoid elaborate animation, multiple visual directions and production infrastructure.

Use synthetic attachments by default. The prototype creates no paid calls, real authentication, external messages, publication or real sensitive-data processing unless the user separately authorized those operations. Describe an unknown integration as a stub; do not invent its API. Apply the existing documentation checkpoint to technologies actually used.

## Show, learn, then implement

1. Verify the main interaction and the important failure/correction transition. Inspect relevant desktop/mobile sizes if the interface will be used there.
2. Show/open the interactive artifact and provide a screenshot as a convenient supplement. A screenshot, diagram or prose alone does not satisfy this stage.
3. Collect the user's concrete feedback. Record the artifact path, accepted/rejected choices and remaining decisions in the existing spec/plan. Apply material changes to the draft before substantial implementation.
4. Treat existing explicit acceptance as sufficient for unchanged choices. Do not demand a second generic approval. If feedback on material choices is still missing, keep product implementation pending and continue only independent authorized work. Explain that the user-requested prototype review stage is the reason for this boundary; link the skill when it causes a pause.
5. Carry the accepted journey and copy into implementation. Update affected prototype journeys only while synchronization is in scope; respect the handoff decision below. Do not restart discovery or rebuild accepted work.

Prototype delivery and production readiness are separate statuses. Browser checks establish the mock's behavior, not model quality, platform delivery, payment correctness or API integration.

## Handoff after the initial release

At the first release or actual-product testing, ask once whether to maintain both prototype and product or only the product. An explicit prior answer already settles this question. Record the choice and any pending question in existing project memory; never repeat the question automatically.

For `prototype_mode: product_only`, retain the mock as a historical reference and stop its edits, copy synchronization, rebuilds, browser checks, screenshots and refreshes. Later UX feedback is implemented and tested in the real product; stale prototype copy is expected, not a regression or an incomplete delivery item. Initial prototype acceptance remains recorded. Revisit mock work only when the user explicitly requests it, without silently enabling ongoing synchronization.

For `sync`, keep updates focused on affected journeys. If the one-time question is unanswered, leave the prototype untouched and continue independent authorized product work; do not invent an answer or ask again.

## Scope boundaries

- New product: interactive preview and resolved user feedback are required before substantial implementation. Later material changes require this preview only while prototype review remains in scope, not in `product_only` mode.
- Existing accepted prototype, unchanged journey: link and reuse it; do not repeat the review.
- Internal backend/refactor with no changed user journey: record inapplicability; a focused runnable request/response or contract example may demonstrate behavior without inventing a UI.
- Bounded bug fix, typo or formatting: retain the reduced/skip workflow. Do not turn this rule into mandatory redesign.
- Preview tools unavailable: deliver the best concrete local artifact available and state the viewing/check limitation. Do not claim the interactive preview was shown or the review gate passed. No automatic publication or installation workaround is authorized.
