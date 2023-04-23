from abc import ABC, abstractmethod
from typing import Any, cast

import pygame


class PygameHumanVisualizer(ABC):
    def __init__(self, scale_factor: int) -> None:
        self.clock: pygame.time.Clock = cast(pygame.time.Clock, None)
        self.display: pygame.Surface = cast(pygame.Surface, None)
        self.scale_factor = scale_factor

    @abstractmethod
    def render_rgb(self, _: Any) -> Any:
        pass

    def render_human(self, _: Any, fps: int) -> Any:
        frame = self.render_rgb(None)
        if self.display is None:
            pygame.init()
            pygame.display.init()
            self.display = pygame.display.set_mode(
                (frame.shape[0] * self.scale_factor, frame.shape[1] * self.scale_factor)
            )
        if self.clock is None:
            self.clock = pygame.time.Clock()

        surf = pygame.surfarray.make_surface(frame)
        surf = pygame.transform.scale_by(surf, self.scale_factor)
        self.display.blit(surf, (0, 0))
        pygame.event.pump()
        pygame.display.update()
        self.clock.tick(fps)

    def close(self) -> None:
        if self.display is not None:
            pygame.display.quit()
            pygame.quit()
