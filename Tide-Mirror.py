#!/usr/bin/env python3
#
# Tide Mirror
#  A procedural poetry generator based on emotional tidal phases
#  poetry like a Markovian Moore Machine.
#
# Copyright (c) 2026 Concept & Code by Joe ApocaLips <japocalips@gmail.com>
#
# Inspired by "Taroko Gorge" by Nick Montfort (2009)
#  Evolves the linear path metaphor into a living tide:
#  instead of walking a trail, the poem breathes like an organism.
#
# Four phases cycle probabilistically (Markov chain):
#  Breath  — suspended fragments, static images, no conjugated verbs
#  Drift   — fluid motion, continuous flow, gentle movement
#  Pulse   — tension peaks, imperatives, ruptures, urgency
#  Fade    — dissolution, ellipses, fading into silence
#
# Unlike Taroko Gorge's fixed strophic structure (path→site→cave),
# Tide Mirror uses weighted state transitions to create organic rhythm.
# Typography (blank lines, delays) is semantic — silence is part of the poem.
#
# Lexical economy: verb roots are transformed morphologically
#  (ing/ed/s) for maximum recycling and combinatorial variety.
#
# core — tuple of 4 states: (transition_weights, template_weights, 
#           line_count_range, blank_lines, indent, templates)
#
# Combinatorics: ~145 words → ~489,400 unique lines → ~10^50 to 10^100 unique poems.
#   Practical exhaustion: Impossible. Each run is statistically unique.
#   ~100 lines of code generating astronomical poetic variations.
#
# Run: python tide_mirror.py
#
# "A machine of waves, not strophes."
#
# Source: https://github.com/JoeApocaLips/tide-mirror
#
# Licensed under the MIT License.
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# v1.0 — 27 Feb 2026
import time, pathlib
from random import choices, randint, choice as c

def sp(x): return x.split(',')
def ing(x): return (x[:-1] if x[-1]=='e' else x)+'ing'
def ed(x): return x+'d' if x[-1]=='e' else x+'ed'
def s(x): return x+'es' if x[-1] in 'shchxz' else x+'s'

V = sp('wait,slide,fade,reflect,hold,fall,break,drift,burn,dissolve,linger,glide,shiver,quiver,shatter,glimmer,whisper,flutter,blur,pulse,fray,hum,waver,seep') 
N = sp('neon,pavement,sign,light,shadow,train,glass,rain,fog,smoke,echo,mirror,stone,flame,vein,thread,coil,dust,static,signal,wire,ash,rust,void')
A = sp('wet,distant,empty,silent,pale,ghost,lost,still,hollow,shimmering,dim,fragile,ashen,flickering,muted,cracked,cold,raw,dense,hazy,tense,spare,vague')
prep = sp('under,against,at,between,above,near,through,beyond,inside,across,upon,among,around,into')
PL = sp('bridge,wall,edge,station,street,corner,window,door,platform,tunnel,alley,roof,threshold,passage,crossing,shaft,grid,duct,rim')
det = sp('the,a,this,that,no,each,any,some,one,its,her')
adv = sp('almost,barely,nearly,slowly,quietly,never,always,softly,faintly,briefly,solemnly,dimly,harshly,endlessly,suddenly')
I = sp('STOP,LISTEN,WAIT,NOW,LOOK,HOLD,SEE,FEEL,RUN,PAUSE,BREAK,FADE,GHOST')
    
core = (
        ((.6,.3,.08,.02),
         (.18,.15,.1,.07,.07,.06,.06,.04,.03,.03,.02,.02,.01,.04,.04,.04,.03), (1,3), 1, (0,2), # Breath
         ("{c(A)} {c(N)}",
          "{c(N)} {ing(c(V))}",
          "{c(prep)} {c(PL)}",
          "{c(adv)} {c(A)} {c(N)}",
          "{c(N)}, {c(A)}",
          "without {c(N)}",
          "{ing(c(V))} {c(prep)} {c(PL)}",
          "{c(A)} {c(PL)}",
          "{c(N)} without {c(N)}",
          "{c(adv)} {ing(c(V))}",
          "{c(prep)} the {c(N)}",
          "{c(A)}, {c(A)} {c(N)}",
          "{ing(c(V))}, {c(A)}",
          "{c(A)}... {c(A)}...",
          "{c(N)} or {c(N)}...",
          "no {c(N)}",
          "{c(adv)}...")
        ),
        ((.2,.5,.25,.05),
         (.26,.15,.11,.08,.06,.06,.05,.05,.06,.04,.04,.04), (2,5), 1, (), # Drift
         ("the {c(N)} {ing(c(V))} {c(prep)} the {c(PL)}",
          "{ing(c(V))} through the {c(N)}",
          "the {c(PL)} {s(c(V))} with {c(N)}",
          "{c(adv)} {ing(c(V))} toward the {c(PL)}",
          "{ing(c(V))} between the {c(N)} and the {c(N)}",
          "{c(adv)} the {c(PL)} {s(c(V))}",
          "{c(adv)} the {c(N)} {s(c(V))} into light",
          "{ing(c(V))} {c(prep)} the {c(A)} {c(N)}",
          "{ing(c(V))} around the {c(N)}",
          "the {c(N)} becomes {c(A)}",
          "{c(N)} to {c(N)}",
          "between {c(A)} and {c(A)}")
        ),
        ((.1,.3,.4,.2),
         (.17,.12,.1,.09,.08,.06,.06,.07,.07,.06,.04,.04,.04), (1,4), 0, (), # Pulse
         ("{c(I)} — {ing(c(V))}",
          "{c(V).upper()}! the {c(N)} {s(c(V))}",
          "―——— {ing(c(V))} ———",
          "{c(I)} {c(prep)} {c(N)}",
          "{c(I)} — the {c(N)} {s(c(V))}",
          "{c(V).upper()} — {c(V).upper()}!",
          "{c(I)} the {c(A)} {c(N)}",
          "{c(V).upper()}! {c(prep)} the {c(PL)}",
          "{c(I)}. {c(I)}.",
          "{c(I)}! {c(I)}!",
          "not {c(N)} — {c(N)}!",
          "{c(V).upper()} {c(V).upper()} {c(V).upper()}",
          "—— {c(I)} ——")
        ),
        ((.8,.15,.04,.01),
         (.17,.05,.04,.04,.12,.1,.08,.07,.05,.04,.04,.03,.04,.05,.04,.04), (1,2), 2, (0,2,4), # Fade
         ("{c(adv)} {c(A)}...",
          "ghost of {c(N)}...",
          "trace of {c(N)}...",
          "echo of {ing(c(V))}...",
          "{ed(c(V))} {c(prep)}...",
          "the {c(N)}... {ing(c(V))}...",
          "{c(det)} {c(N)}... almost...",
          "{c(N)}... without {c(N)}...",
          "{ed(c(V))}... almost...",
          "{c(det)} {c(A)} silence...",
          "nothing but {ing(c(V))}...",
          "{c(A)} light... {c(adv)}...",
          "{c(N)} like {c(N)}...",
          "{ed(c(V))} {c(N)}...",
          "{c(A)} into {c(A)}...",
          "only {c(N)}...")
        )
       )

last, cur = '', core[0] # breath first
with (pathlib.Path(__file__).parent/'output'/time.strftime('poem-%y%m%d-%H%M%S.txt')).open('w', encoding='utf-8') as f:
  for _ in range(randint(12, 50)):
      for t in choices(cur[5], cur[1], k=randint(*cur[2])):
          while((ln := eval(f"f'{t}'")) == last): pass
          last = ln
          print(' ' * (c(cur[4]) if cur[4] else 0) + ln, file=f)
      print('\n'*cur[3], end='', file=f)
      cur = choices(core, cur[0])[0]