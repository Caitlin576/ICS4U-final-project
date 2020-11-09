//https://gamedev.stackexchange.com/questions/165380/how-to-get-camera-to-follow-car


//instead of scrolling bcakground, this code mkaes the camera follow the player in each direction you go

import pygame
import random

from math import tan, radians, degrees, copysign
from pygame.math import Vector2


pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)
rect = screen.get_rect()
clock = pygame.time.Clock()
BACKGROUND = pygame.Surface(screen.get_size())
# Drawing a grid.
for x in range(screen.get_width()//20):
    pygame.draw.line(BACKGROUND, (160, 90, 0), (x*20, 0), (x*20, 800), 1)
for y in range(screen.get_height()//20):
    pygame.draw.line(BACKGROUND, (160, 90, 0), (0, y*20), (1280, y*20), 1)


class Car:
    def __init__(self, image, x, y, angle=0.0, length=4, max_steering=10, max_acceleration=5.0):
        self.orig_image = image
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = 450
        self.max_steering = max_steering
        self.max_velocity = 220
        self.brake_deceleration = 150
        self.free_deceleration = 100

        self.acceleration = 0.0
        self.steering = 0.0
        self.camera = Vector2(0, 0)  # Assigned the camera as an attribute.

    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))

        if self.steering:
            turning_radius = self.length / tan(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius / 2
        else:
            angular_velocity = 0

        vel = self.velocity.rotate(-self.angle) * dt
        self.position += vel
        self.camera += vel  # Update the camera position as well.
        # If you use the rect as the blit position, you should update it, too.
        self.rect.center = self.position
        self.angle += degrees(angular_velocity) * dt

        self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Project BrmBrm")
        width = 1280
        height = 720
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

    def run(self):
        car_image = pygame.Surface((68, 43), pygame.SRCALPHA)
        pygame.draw.polygon(car_image, pygame.Color('dodgerblue1'), ((0, 0), (68, 20), (0, 41)))
        car = Car(car_image, *self.screen.get_rect().center)  # I center the car.

        while not self.exit:
            dt = self.clock.tick(self.ticks) / 1000
            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            # User input
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_UP]:
                if car.velocity.x < 0:
                    car.acceleration = car.brake_deceleration
                else:
                    car.acceleration += 890 * dt
            elif pressed[pygame.K_DOWN]:
                if car.velocity.x > 0:
                    car.acceleration = -car.brake_deceleration
                else:
                    car.acceleration -= 1 * dt
            elif pressed[pygame.K_SPACE]:
                if abs(car.velocity.x) > dt * car.brake_deceleration:
                    car.acceleration = -copysign(car.brake_deceleration, car.velocity.x)
                else:
                    car.acceleration = -car.velocity.x / dt
            else:
                if abs(car.velocity.x) > dt * car.free_deceleration:
                    car.acceleration = -copysign(car.free_deceleration, car.velocity.x)
                else:
                    if dt != 0:
                        car.acceleration = -car.velocity.x / dt
            car.acceleration = max(-car.max_acceleration, min(car.acceleration, car.max_acceleration))

            if pressed[pygame.K_RIGHT]:
                car.steering -= 20 * dt
            elif pressed[pygame.K_LEFT]:
                car.steering += 20 * dt
            else:
                car.steering = 0
            car.steering = max(-car.max_steering, min(car.steering, car.max_steering))

            # Logic
            car.update(dt)

            # Drawing
            self.screen.fill((30, 30, 30))
            # Now use the camera to adjust the positions of the game objects.
            screen.blit(BACKGROUND, -car.camera)
            self.screen.blit(car.image, car.position - (car.rect.width / 2, car.rect.height / 2)-car.camera)
            # You can blit the car at its rect.topleft position minus the camera as well.
            # self.screen.blit(car.image, car.rect.topleft-car.camera)
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
