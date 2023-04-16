from typing import Any, Protocol

from gymnasium.spaces import Space
from numpy.typing import NDArray


class Observer(Protocol):
    # TODO: Add low and high poperties for the observation space
    @property
    def space(self) -> Space:
        """
        The shape of the observation which is returned by observe().

        Returns
        -------
        shape: Tuple[int, ...]:
            The shape of the observation list.
        """

    def observe(self, observed: Any) -> NDArray:
        """
        Returns an observation of the an observed object.

        Parameters
        ----------
        observed: Any
            The object which is observed.

        Returns
        -------
        observation: List[float]
            Observation of the observed object as an list.
        """
