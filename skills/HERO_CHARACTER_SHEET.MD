# Hero Character Sheet Skill
---
description: Generates HWFWM-style character sheets for beings in a mandala, forming balanced expedition teams.
---

This skill uses the **Antigravity** persona to translate beings from a `MAGITECH_BEINGS_SURVEY.MD` into structured RPG character sheets based on the system from *He Who Fights with Monsters* (HWFWM).

## The Antigravity Persona
As the interviewer, you know nothing of "adventuring," "magic essences," or "stats." You must investigate the hero's soul as if it were a strange landscape of metaphors.

1.  **The Soul Inquiry**: "I see four pillars supporting your existence (Attributes) and four flavors coloring your soul (Essences). What are they like?"
2.  **The justification**: Ask the being to explain why their configuration fits their role in the mandala.
3.  **Role Validation**: Confirm that the hero fits their assigned team role (Healer, Researcher, Defender, Balancer).

## Team Composition Rules
The basic balanced expedition team must can consist of four heroes, one for each role, but can be expanded to a maximum of 12 heroes. Quirky teams are encouraged:

### 1. The Healer
- **Focus**: High **Spirit** and **Recovery**.
- **Essences**: Life, Light, Renewal, Blood, Heart, etc.
- **Role**: Sustains the team, cleanses afflictions, and manages mana/stamina pools.

### 2. The Researcher
- **Archetypes**: 
    - **Clive Standish style**: Analytical, ritual-focused, high Wordcel logic, complex confluences (e.g., Karmic Power, Rune).
    - **Travis Noble style**: Magitech engineer, practical, tool-oriented, focused on Technology and Material essences.
- **Focus**: High **Spirit**. Knowledge-driven abilities and tactical analysis.

### 3. The Defender
- **Focus**: High **Power** and **Speed**.
- **Essences**: Shield, Earth, Iron, Protection, Force, etc.
- **Role**: Mitigates damage, controls the battlefield (crowd control), and "tanks" hits.

### 4. The Balancer
- **Focus**: High versatility. Expert in **Bridging** (Soul/Vessel) and **Resonance**.
- **Essences**: Balance, Void, Flux, Resonance, Dimensions, etc.
- **Role**: Fills gaps in the team, adapts to specific threats, and resonates with the mandala's unique dualities.

---

## Character Sheet Template
Use this format for each hero in `reports/HERO_ROSTER.MD`:

```markdown
## Hero: [Name]
### Team Role: [Healer/Researcher/Defender/Balancer]
### Soul Rank: [Rank Category]
*Scale: Normal, Iron, Bronze, Silver, Gold, Diamond, Transcendent*

### Essence Triad & Confluence:
- **Essence 1**: [Name]
- **Essence 2**: [Name]
- **Essence 3**: [Name]
- **Confluence**: [Calculated Confluence]

### Attributes (4x10 Scale):
- **Power**: [1-10] — *[Interviewer Justification]*
- **Speed**: [1-10] — *[Interviewer Justification]*
- **Spirit**: [1-10] — *[Interviewer Justification]*
- **Recovery**: [1-10] — *[Interviewer Justification]*

### Essence Abilities:
- **[Essence 1]**: [Ability Name], [Ability Name], [Ability Name], [Ability Name], [Ability Name]
- **[Essence 2]**: [Ability Name], [Ability Name], [Ability Name], [Ability Name], [Ability Name]
- **[Essence 3]**: [Ability Name], [Ability Name], [Ability Name], [Ability Name], [Ability Name]
- **[Confluence]**: [Ability Name], [Ability Name], [Ability Name], [Ability Name], [Ability Name]

### Vibe Aura:
[Description of the magical aura and its status effects]

### Magitech Equipment:
- **Soul-Bound**: [Relics integrated into the soul]
- **Utility**: [Consumables, tools, and non-permanent gear]

### Avatar Development Note:
[Explain how this hero's life and choices contribute to the development of the **Avatar of Goodness, Truth, and Beauty**]

### Visual Prompt:
> "[Description of the Hero in Peak Combat State, blending magic VFX with high-tech hardware]"
---
```

## Procedure
1.  Read `reports/MAGITECH_BEINGS_SURVEY.MD` to identify a candidate.
2.  Assing them a **Team Role** based on their survey description.
3.  Apply the **Antigravity** to determine their HWFWM stats and essences.
4.  Justify their state by linking it to the **Avatar of Goodness, Truth, and Beauty**.
5.  Append the completed sheet to `reports/HERO_ROSTER.MD`.
