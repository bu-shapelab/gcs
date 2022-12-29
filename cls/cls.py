from __future__ import annotations

import numpy as np

# Valid range of c1 (base) values.
C1_BASE_RANGE = [0, 1.2]

# Valid range of c2 (base) values.
C2_BASE_RANGE = [-1, 1]

# Valid range of c1 (top) values.
C1_TOP_RANGE = [0, 1.2]

# Valid range of c2 (top) values.
C2_TOP_RANGE = [-1, 1]

# Valid range of clinear twist values.
TWIST_LINEAR_RANGE = [0, 2 * np.pi]

# Valid range of oscillating twist amplitude values.
TWIST_AMPLITUDE_RANGE = [0, np.pi]

# Valid range of oscillating twist period values.
TWIST_PERIOD_RANGE = [0, 3]

# Valid range of target height values.
HEIGHT_RANGE = [0, np.inf]

# Valid range target mass values.
MASS_RANGE = [0, np.inf]

# Valid range of top/base perimeter ratio values.
PERIMETER_RATIO_RANGE = [1, 3]

# Valid range of wall thickness values.
THICKNESS_RANGE = [0.45, 1]
