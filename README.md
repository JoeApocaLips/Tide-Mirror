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

## 📖 Output Sample

  without static  
waiting around platform  
  whispering against duct  
  
shattering through the thread  
endlessly the signal whispers into light  
  
fraying around the sign  
the fog fading into the threshold  
softly the alley hums  
  
sliding around the neon  
the smoke breaking through the grid  
  
dimly the corner shatters  
dimly breaking toward the grid  
whispering between the signal and the ash  
  
BURN! the dust glides  
WAIT! FEEL!  
―——— seeping ———  
LOOK into shadow  
  shivered… almost…  
  
  
lingering across crossing  
  
reflecting through the ash  
flame to void  
nearly the glass seeps into light  
  
RUN! SEE!  
—— HOLD ——  
―——— pulsing ———  
LINGER! the rain lingers  
NOW — falling  
SHIVER! the light dissolves  
―——— dissolving ———  
STOP through mirror  
―——— sliding ———  
lingering under the cracked static  
the duct blurs with light  
the signal reflecting inside the door  
the pavement drifting into the corner  
fraying around the dust  
  
the dust breaking among the rim  
briefly the light shatters into light  
  
WAIT into echo  
WHISPER! the coil slides  
LISTEN around stone  
STOP across wire  
pulsing around the smoke  
sliding between the pavement and the glass  
  
FEEL! LOOK!  
WAIT the vague mirror  
STOP above void  
LISTEN. FADE.  
FLUTTER! the vein dissolves  
LOOK — drifting  
SEE between stone  
LISTEN — the smoke glides  
  
## Run

```bash
python tide-mirror.py
