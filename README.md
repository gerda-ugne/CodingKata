# CodingKata

Coding Kata was a proposed exercise at Amazon Spring Insights.
We had to develop a system as follows:

# Combat Simulator Coding Kata - Student Notes
## Introduction
A code kata is an exercise in programming which helps programmers hone their skills through practice and repetition.
The word kata (Japanese, meaning "form") refers to a detailed choreographed pattern of martial arts movements made
to be practised alone.
The problem has two tracks, A and B. Two pairs should work on separate tracks. Both tracks should be in the same
programing language.
Complete each iteration before reading the next one.
It is recommended to perform this kata while writing tests. How do I know my code is correct after changes?
Output code should be clean, extensive, and maintainable.
Refactor existing code to add new requirements.
Review other’s code; have your code reviewed and act on feedback. Collaborate with others.

### Iteration 1
All Characters, when created, have:
- Health, starting at 1000
- Level, starting at 1
- May be Alive or Dead, starting Alive (Alive may be a true/false)

Seed code:
Java + Maven: https://github.com/angarg12/rpg-combat-kata-java
Python + pip: https://github.com/angarg12/rpg-combat-kata-python
Javascript/Node + npm: https://github.com/angarg12/rpg-combat-kata-node

### Iteration 2
#### Track A
Characters can Deal Damage to Characters.
- Damage is subtracted from Health
- When damage received exceeds current Health, Health becomes 0 and the character dies
A Character cannot Deal Damage to itself.
#### Track B
A Character can Heal a Character.
- Dead characters cannot be healed
- Healing cannot raise health above 1000

Considerations:
A Character can only Heal itself.
### Iteration 3
#### Track A
Characters have experience, starting at 0.
Characters can gain experience.
Characters can level up. A character levels up when their current experience goes above the requirement for each level.
Experience requirement per level follows the formula level^2*10. E.g. level 10 requires 10^2*10=1000 experience.
Level 20 requires 20^2*10=4000 experience.
When levelling up, experience resets to 0.
Maximum level is 100.
Track B
Characters may belong to one or more Factions.
Newly created Characters belong to no Faction.
A Character may Join or Leave one or more Factions.
Players belonging to the same Faction are considered Allies.
Allies cannot Deal Damage to one another.
Allies can Heal one another.
### Retrospective
- Are you keeping up with the requirements? Has any iteration been a big challenge?
- Do you feel good about your design? Is it scalable and easily adapted to new requirements?
- Is everything tested? Are you confident in your code?

### Iteration 4
#### Track A
Characters have stamina, starting at 100.
- An attack uses 10 stamina.
- If stamina is under 10, a character cannot attack.
- Each turn, stamina goes up by 5.
- Stamina cannot go over 100.
#### Track B
Character have mana, starting at 20.
- Healing uses 10 mana.
- If mana is under 10, a character cannot heal.
- Each turn, mana goes up by 1.
- Mana cannot go over 20.
### Iteration 5
#### Track A
Characters can equip one weapon.
- Weapons have an attack value.
- Weapons can have a level requirement. E.g. you need at least level 10 to equip this weapon.
- Weapons add a damage bonus to the character equals to its attack.
- Weapons can be unequipped.
#### Track B
Characters can equip one piece of armour.
- Armour has a defence value.
- Armours can have a level requirement. E.g. you need at least level 10 to equip this armour.
- Amour reduced damage to the character equal to its defence.
- Amour can be unequipped.
