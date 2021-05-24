from constants import DISPLAY_HEIGHT, RED
from images import PLAYER_IMAGES, MALE_ZOMBIE_IMAGES
from pygame import draw as pydraw


class Character:
    def __init__(self):
        """
        Class object of generic character model and behavior

        """

        self.id = None  # character identification
        self.y = 0.7 * DISPLAY_HEIGHT  # y position as 70% of display height

        self.x = 0
        self.velocity = 0

        self.hit_box = None
        self.is_attacking = False

        self.current_state = 'IDLE'
        self.state = 'IDLE'
        self.direction = 'RIGHT'
        self.image_set = None

        self.frame = 0
        self.width = 0

    def move(self):
        """
        Changes character velocity according to its direction and moves its
        image.

        :return: None
        """

        # changes character velocity according to its direction
        if self.direction == 'RIGHT' and self.velocity < 0 or \
                self.direction == 'LEFT' and self.velocity > 0:

            self.velocity *= -1

        # adds velocity to position
        self.x += self.velocity

    def draw(self, win, *args, **kwargs):
        """
        Method responsible for selecting and drawing the character image on
        the display.

        :param win: main display.
        :param args: used for modifications in subclasses.
        :param kwargs: used for modifications in subclasses.

        :return: None
        """

        # fetches image set from current state and direction
        current_set = self.image_set[self.current_state][self.direction]
        # getting image width and height
        img_w, img_h = current_set[0].get_size()

        # adjusts image position
        if self.current_state != self.state:
            if self.direction == 'LEFT':
                delta_x = img_w - self.width
                self.x -= delta_x

            if self.current_state == 'THROW' or self.state == 'THROW':
                delta = self.width if self.state == 'THROW' else -img_w
                delta //= 4

                self.x += delta if self.direction == 'RIGHT' else -delta

        # resets frame after a full cycle or a change in state
        if self.frame > len(current_set) - 1 or \
                self.state != self.current_state:
            self.frame = 0

            if self.state == 'ATTACK':
                self.is_attacking = False

            # resets character state
            self.state = self.current_state

        # resets character state
        self.width = img_w

        # resets character hit box according to current character image
        self.hit_box = self.set_hit_box(self.x, self.y, img_w, img_h)
        pydraw.rect(win, RED, self.hit_box, 2)

        # places character on the display
        win.blit(current_set[self.frame], (self.x, self.y))

        # advances one frame
        self.frame += 1

    def set_hit_box(self, x, y, width, height):
        """
        Set character's hit box position and size

        :param x: hit box x position.
        :param y: hit box y position.
        :param width: hit box total width (x axis)
        :param height: hit box total height (y axis)

        :return: list with hit box position and size.
        """

        return [x, y, width, height]

    def __str__(self):
        return self.id


class Ninja(Character):
    def __init__(self):
        """
        Extends Character class with specific behavior for ninja character
        """

        # starts super class init method
        super(Ninja, self).__init__()
        self.id = 'Ninja'
        self.image_set = PLAYER_IMAGES

        # overwrites same class instances
        self.x = 10
        self.velocity = 40

        # instances related to jump movement
        self.is_jumping = False
        self.ground = self.y
        self.impulse = -100

    def jump(self):
        """
        Makes the jumping movement

        :return: None
        """

        # changes character current state
        self.current_state = 'JUMP'

        # keeps the player in motion if it's already jumping
        if self.is_jumping:
            # compares the character y position with the ground position
            if self.y != self.ground:
                # keeps the motion with an negative acceleration
                self.y += self.impulse + 20*self.frame

            else:
                # stops the jumping motion and resets the state to Idle
                self.is_jumping = False
                self.current_state = 'IDLE'

        # starts the player jumping movement
        else:
            self.is_jumping = True
            self.y += self.impulse


class Zombie(Character):
    def __init__(self):
        """
        Extends Character class with specific behavior for zombie character
        """

        # starts super class init method
        super(Zombie, self).__init__()
        self.id = 'Zombie'
        self.image_set = MALE_ZOMBIE_IMAGES

        # overwrites same class instances
        self.y -= 20  # adjusting image y position
        self.x = 750
        self.velocity = 5

    def draw(self, win, player_pos=10, *args, **kwargs):
        """
        Selects and draws the zombie image on the display.

        :param win: main display.
        :param player_pos: position which the zombie will move towards.

        :return: None
        """

        # starts super class draw method
        super(Zombie, self).draw(win, player_pos, *args, **kwargs)
        # calls chase method
        self.chase(player_pos)

    def chase(self, stop_pos):
        """
        Changes Zombie direction and state according to player position.

        :param stop_pos: chase ending position, normally players position.

        :return: None
        """

        # adjusts stop position according to zombie direction
        stop_pos -= (self.hit_box[2] // 100) * 100 \
            if self.direction == 'RIGHT' else 0

        # compares current position to stop position
        if self.x != stop_pos:
            # adjusts direction and state
            self.direction = 'LEFT' if self.x > stop_pos else 'RIGHT'
            self.current_state = 'WALK'
            # calls move method
            self.move()

        else:
            self.current_state = 'ATTACK'

    def set_hit_box(self, x, y, width, height):
        """
        Add small corrections to the zombies hit box position and size.

        :return: super class set_hit_box method with corrected parameters.
        """

        # incrementation values for both axis
        x_increment = width * 0.2  # 20%
        y_increment = height * 0.1  # 10%

        # adjusting x values
        x += x_increment
        width -= 2 * x_increment

        # adjusting y axis
        y += y_increment
        height -= y_increment

        return super(Zombie, self).set_hit_box(x, y, width, height)

