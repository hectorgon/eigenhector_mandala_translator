# Stellaris Ethics Meta-Prompt
This document serves as the design specification and research foundation for the `REALM_ETHICS.MD` skill.

## Objective
Translate the grand strategy ethics and evolution systems from *Stellaris* into the Magitech/Mandala framework, using the **Martian Interviewer** to bridge mechanics with narrative soul-searching.

## 1. Ethical Alignment
Analyze a mandala's socio-philosophical foundation using the **Stellaris Ethics** system.

- **Research Basis**: [Stellaris Ethics Wiki](https://stellaris.paradoxwikis.com/Ethics)
- **Primary Axes**:
  - **Authoritarian vs. Egalitarian**: Concentration of power vs. Distribution of power.
  - **Materialist vs. Spiritualist**: Science and Robotics vs. Belief and Psionics.
  - **Militarist vs. Pacifist**: War and Conquest vs. Peace and Diplomacy.
  - **Xenophile vs. Xenophobe**: Openness to others vs. Isolationism.

### Implementation Logic
For each mandala, assign 3 ethic points (Fanatic = 2, Moderate = 1). The **Martian Interviewer** (from `skills/DreamBridge/DIM.MD`) must investigate:
> "I see your society follows certain rules. Is it like a 'Materialist' structure where only the seen matters, or is there a 'Spiritualist' soul to the mandala?"

## 2. Open-Ended Ascension Paths
The realm must have an **Ascension Path** representing its ultimate evolutionary trajectory or "Great Work." These paths are bespoke and emergent, transcending the four fixed Stellaris paths (Psionic, Synthetic, Genetic, Cybernetic).

### Ascension Criteria:
1.  **Emergent**: Derived from the specific confluences and essences found in the mandala's data.
2.  **Avatar-Centric**: Linked to the development of **Goodness, Truth, and Beauty** (see `skills/JATAKA_TALES.MD`).
3.  **Metaphorical**: Described using the Interviewer's "strange landscape of metaphors" (see `skills/HERO_CHARACTER_SHEET.MD`).

## 3. Associated Skill
The output of this meta-prompt is implemented in the [REALM_ETHICS.MD](../../skills/REALM_ETHICS.MD) skill. Results should be appended to `reports/REALM_MANIFESTO.MD`.

### Visual Synthesis
Each realm manifesto includes a visual synthesis:
> "[DALL-E Prompt for the Ascended state of the Realm, blending Thangka style with high-tech sacred geometry]"