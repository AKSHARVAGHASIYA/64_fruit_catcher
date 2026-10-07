import random
import pygame

class Fruit:
    def __init__(self, screen_width, speed_bonus=0.0):
        self.screen_width = screen_width
        self.radius = 14
        self.x = random.randint(30, screen_width - 30)
        self.y = -self.radius * 2
        self.speed = max(4.0, min(random.uniform(4.0, 6.5) + speed_bonus, 9.0))
        self.is_hazard = random.random() < 0.2
        if self.is_hazard:
            self.color = (35, 35, 40)
        else:
            self.color = random.choice([
                (230, 45, 45),   # Apple
                (245, 140, 30),  # Orange
                (160, 60, 200),  # Grape
            ])

    def update(self):
        self.y += self.speed

    def is_missed(self, screen_height):
        return self.y > screen_height

    @property
    def rect(self):
        return pygame.Rect(
            int(self.x - self.radius),
            int(self.y - self.radius),
            self.radius * 2,
            self.radius * 2,
        )

    def render(self, surface):
        center = (int(self.x), int(self.y))
        if self.is_hazard:
            pygame.draw.circle(surface, self.color, center, self.radius)
            pygame.draw.circle(surface, (220, 60, 45), center, self.radius, 2)
            pygame.draw.line(
                surface,
                (170, 120, 65),
                (center[0], center[1] - self.radius),
                (center[0] + 5, center[1] - self.radius - 6),
                3,
            )
            pygame.draw.circle(
                surface,
                (255, 210, 70),
                (center[0] + 7, center[1] - self.radius - 7),
                3,
            )
            return

        pygame.draw.circle(surface, self.color, center, self.radius)
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x - 4), int(self.y - 4)), 3)