import pygame
import random


class SimpleSprite(pygame.sprite.Sprite):
    def __init__(self, image, **kwargs):
        super(SimpleSprite, self).__init__()
        self.image = image
        self.rect = image.get_rect(**kwargs)


def new_cloud():
    num_circles = random.randint(4, 5)
    spc = 30
    minr = spc
    maxr = spc * 2
    shad = 10

    # Randomly generate a list of (x, y, r) tuples to draw a cloud
    circles = [((i * spc),
                random.randint(-spc / 2, spc / 2),
                random.randint(minr, maxr))
                for i in range(num_circles)]
    print circles

    # Determine the surface size from the random circles
    # Taking radius and x location into account, find l/r edges
    l_edge = circles[0][0] - circles[0][2]    # x - r of first circle
    r_edge = circles[-1][0] + circles[-1][2]  # x + r of last circle
    # Calculate size, based on edges
    width = r_edge - l_edge
    xoffset = circles[0][2]  # Radius of first circle is xoffset

    # Taking radius and random y location into account, find t/b edges
    t_circ = min(circles, key=lambda c: c[1] - c[2])  # y - r = top edge
    b_circ = max(circles, key=lambda c: c[1] + c[2])  # y + r = bottom edge
    t_edge = t_circ[1] - t_circ[2]  # y - r of top circle
    b_edge = b_circ[1] + b_circ[2]  # y + r of bottom circle
    # Calculate size, based on edges
    height = b_edge - t_edge + shad
    yoffset = -t_edge + shad  # Topmost cloud edge plus shadow is yoffset

    print locals()
    image = pygame.Surface((width, height))
    image.fill((1, 2, 3))
    image.set_colorkey((1, 2, 3))

    for circ in circles:
        x = xoffset + circ[0]
        y = yoffset + circ[1]
        pygame.draw.circle(image, (167, 190, 221), (x, y), circ[2])

    for circ in circles:
        x = xoffset + circ[0]
        y = yoffset + circ[1]
        pygame.draw.circle(image, (255, 255, 255), (x, y - shad), circ[2])

    return image

# Cloud = class()

# function Cloud:init()
#     -- you can accept and set parameters here
#     self.shapes = {}
#     self.position = vec2(0,0)

#     -- Generate random cloud
#     numCircles = math.random(4, 5)
#     spacing = 30

#     for i = 1,numCircles do
#         x = i * spacing - ((numCircles/2)*spacing)
#         y = (math.random() - 0.5) * 30
#         rad = math.random(spacing, 2*spacing)
#         table.insert(self.shapes, {x=x, y=y, r=rad})
#     end

#     self.width = numCircles * spacing + spacing
# end

# function Cloud:isColliding(pos)
#     startp = self.position.x - self.width/2
#     endp = self.position.x + self.width/2

#     if pos.x < endp and pos.x > startp and
#        pos.y < (self.position.y + 30) and
#        pos.y > (self.position.y + 10) then
#         return true
#     end

#     return false
# end

# function Cloud:draw()
#     pushStyle()
#     pushMatrix()

#     translate(self.position.x, self.position.y)

#     noStroke()
#     ellipseMode(RADIUS)
#     fill(167, 190, 221, 255)

#     for i,s in ipairs(self.shapes) do
#         ellipse(s.x, s.y - 5, s.r)
#     end

#     fill(255, 255, 255, 255)

#     for i,s in ipairs(self.shapes) do
#         ellipse(s.x, s.y + 5, s.r)
#     end

#     popMatrix()
#     popStyle()
# end
