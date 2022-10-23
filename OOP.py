#class Enemy:
class Enemy:
    pass


class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaing_points = self.hit_points - damage
        if remaing_points >= 0:
            self.hit_points = remaing_points
            print("Total {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1

    def __str__(self):
        return "Name {0.name},Lives: {0.lives},Hit points: {0.hit_points}".format(self)

    class Troll(Enemy):
         pass


class Troll:
    pass