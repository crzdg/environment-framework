from typing import Any, Protocol

import numpy as np
from numpy.typing import NDArray

UINT8 = NDArray[np.uint8]


class Visualizer(Protocol):
    def render_rgb(self, visualized: Any) -> UINT8:
        """
        Renders the given visualizee to a visualisation.

        Parameters
        ----------
        visualizee: Any
            Object to visualise.

        Returns
        -------
        visualisation: Any
            The visualisation of the object.
        """

    def render_human(self, visualized: Any, fps: int) -> None:
        pass

    def close(self) -> None:
        pass
