# Tide Mirror 🌊

> *"A machine of waves, not strophes."*

A procedural poetry generator based on emotional tidal phases. Inspired by Nick Montfort's *Taroko Gorge* (2009), but evolves the linear path metaphor into a living, breathing organism.

## How It Works

Four phases cycle probabilistically via a Markov chain:

| Phase | Effect |
|-------|--------|
| **Breath** | Suspended fragments, static images, no conjugated verbs |
| **Drift** | Fluid motion, continuous flow, gentle movement |
| **Pulse** | Tension peaks, imperatives, ruptures, urgency |
| **Fade** | Dissolution, ellipses, fading into silence |

Typography is semantic: blank lines and delays are part of the poem. Silence breathes.

## Combinatorics

- ~145 root words → ~220 morphological forms (via `ing`/`ed`/`s`)
- 58 templates across 4 phases
- ~489,400 unique lines possible
- ~10^50 to 10^100 unique poems (Markov sequences × variations)
- Practical exhaustion: **Impossible**. Each run is statistically unique.

## Minimalism

- ~100 lines of Python
- 0 dependencies (stdlib only)
- Compact, readable, fork-ready architecture

## Run

```bash
python tide-mirror.py
