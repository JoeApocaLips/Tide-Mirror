# Tide Mirror 🌊

> *"A machine of waves, not strophes."*

Poetry like a Markovian Moore Machine.
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
```
pulsing above edge  
  
always the window slides  
the door falls with thread  
falling through the pavement  
reflecting through the light  
  
bluring through the void  
between tense and silent  
  
  any rain... almost...  
  
  
almost the vein falls into light  
the stone becomes flickering  
between shimmering and shimmering  
  
HUM! the rust fades  
SHIVER! among the tunnel  
FADE! PAUSE!  
FADE the cold pavement  
huming around the wire  
the passage pulses with dust  
dimly the edge flutters  
slowly reflecting toward the alley  
dissolving through the train  
  
BREAK — WAIT!  
LISTEN — the static holds  
not shadow — void!  
WAVER! the ash whispers  
DRIFT — BLUR!  
signal, lost  
  coil, ashen  
  
shimmering edge  
  
burning beyond the cracked signal  
the bridge quivers with pavement  
  
—— RUN ——  
BREAK — lingering  
not dust — smoke!  
WAIT — gliding  
the thread sliding upon the edge  
reflecting through the ash  
lingering around the train  
fading around the rust  
  
WAVER! the thread breaks  
WHISPER! the glass flutters  
the echo... shattering...  
  
  
whispering under street  
no rust  
  barely pale thread  
  
reflecting through the flame  
fluttering around the stone  
the shadow dissolving upon the alley  
wire to static  
barely the corner glides  
  
WAIT — SEEP!  
FEEL — seeping  
  some void... almost...  
    rust... without ash...  
  
  
void bluring  
  
the corner slides with dust  
harshly fading toward the rim  
the echo breaking through the edge  
  
solemnly bluring toward the crossing  
bluring through the smoke  
  
the light waiting into the alley  
the train fraying above the window  
shivering between the hazy signal  
endlessly the station wavers  
  
fragile pavement  
  
the void quivering inside the window  
the thread drifting inside the threshold  
fading above the hollow rust  
  
WAIT — bluring  
GHOST the spare thread  
BREAK — falling  
LOOK the empty echo  
SLIDE! beyond the crossing  
the threshold quivers with smoke  
the pavement bluring around the window  
between pale and shimmering  
shattering between the echo and the train  
shattering through the rust  
  
dimly shattering toward the street  
the ash pulsing inside the window  
shattering inside the vague pavement  
the coil whispering inside the street  
  
through shaft  
barely dissolving  
  
solemnly the shaft wavers  
between still and flickering  
wire to sign  
the wire becomes dense  
dissolving around the dust  
  
HOLD inside flame  
WHISPER — GLIMMER!  
glimmering through the neon  
wavering around the coil  
fog to rust  
bluring through the sign  
  
quivering inside the empty vein  
the train burning at the tunnel  
vein to neon  
the bridge hums with dust  
the corner pulses with vein  
  
  neon falling  
  
  ashen thread  
  between shaft  
  
SHIVER! against the grid  
RUN — the light blurs  
—— SEE ——  
WHISPER — GLIMMER!  
―——— pulsing ———  
―——— fading ———  
—— GHOST ——  
PAUSE against sign  
  no flame  
  
    each thread... almost...  
  
  
  among alley  
  
```  
## Run

```bash
python tide-mirror.py
