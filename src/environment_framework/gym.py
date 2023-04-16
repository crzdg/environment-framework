from typing import Any, Dict, List, Optional, Tuple

import gymnasium as gym

from environment_framework.ilevel import ILevel
from environment_framework.simulator import Simulator


class EnvironmentFrameworkGym(gym.Env):
    metadata = {"render_modes": ["rgb_array"], "render_fps": 4}

    def __init__(
        self,
        level: ILevel,
        render_mode: Any = Optional[None],
    ) -> None:
        super().__init__()

        self.simulator = Simulator(level)

        self.observation_space = self.simulator.observation_space
        self.action_space = self.simulator.action_space

        supported_render_modes: List[str] = EnvironmentFrameworkGym.metadata["render_modes"]
        if render_mode and render_mode not in supported_render_modes:
            raise Exception("Specified unsupported render mode")
        self.render_mode = render_mode

        # We may take steps during the init of the game
        self.simulator.clear_counter()

    def step(
        self,
        action: List,
    ) -> Tuple[Any, float, bool, bool, Dict]:
        action = self.simulator.step(action)
        reward = self.simulator.estimate()
        # TODO: Implement gymnasium specific terminate / truncate strategy
        return self.simulator.observe(), reward, self.simulator.done, False, {}

    def reset(  # pylint: disable=unused-argument
        self, *, seed: Optional[int] = None, options: Optional[Dict] = None
    ) -> Tuple[Any, Dict[str, Any]]:
        super().reset(seed=seed)
        self.simulator.reset()
        return self.simulator.observe(), {}

    def render(self) -> Optional[Any]:
        frame = self.simulator.render()
        return frame
