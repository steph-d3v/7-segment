# ---------------------------------------------------------------------------
# Implémentation d'un afficheur numérique à sept segments
# ---------------------------------------------------------------------------
# Auteur : Steph (https://github.com/steph-d3v/)
# Date   : 11 août 2024
# ---------------------------------------------------------------------------
# Les sept segments sont encodés par les constantes L, C et R
# selon un découpage en colonnes :
#
#              ┌─────────── gauche (L)
#              │   ┌─────── centre (C)
#              │   │    ┌── droite (R)
#              │   │    │
#              ▼   ▼    ▼
#  ####      │ # │ ## │ # │
#  #  #      │ # │    │ # │
#  ####  =>  │ # │ ## │ # │
#  #  #      │ # │    │ # │
#  ####      │ # │ ## │ # │
# ---------------------------------------------------------------------------
# fmt: off

from datetime import datetime

P = "# "
D = "0123456789"
L = ("1:", "1237:", "17:", "134579:", "147:")
C = ("14:", D, "017:", D, "147:")
R = (":", "56:", ":", "2:", ":")
E = lambda t, p: (1 + (t != ":")) * p
Q = lambda t, x: P[t in x] + "\b" * (t == ":")
T = datetime.now().strftime("%H:%M").lstrip("0")

print("\n".join(" " * 6 * (len(T) < 5) + "  ".join(Q(t, l) + E(t, P[t in c]) + Q(t, r) for t in T) for l, c, r in zip(L, C, R)))
