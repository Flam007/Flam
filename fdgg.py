import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    def  __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.AMAZON)
    def setup(self):
        pass
    def on_draw(self):
        arcade.start_render()
    def update(self):
        pass

SPRITE_SCALING_COIN = 0,2
coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)

def setup(self):
    self.player_list = arcade.SpriteList()
    self.coin_list = arcade.SpriteList()
    self. score = 0
    self.player_sprite = arcade.Sprite("images/character.png",SPRITE_SCALING_PLAYER)
    self.player_sprite.center_x = 50
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)
    for i in range(COIN_COUNT):
        coin = arcade.Sprite("images/coin_01.png", SPRITE_SCALING_COIN)
        coin.center_x = random.randrange(SCREEN_WIDTH)
        coin.center_y = random.randrange(SCREEN_HEIGHT)
        self.coin_list.append(coin)
def on_draw(self):
    arcade.start_render()
    self.coin_list.draw()
    self.player_list.draw()
def update(self, delta_time):
    coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.coin_list)
    for coin in coins_hit_list:
        coin.kill()
        self.score += 1
def main():
    game = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT)
    game.setup()
    game.run()
if __name__ == "__main__":
    main()
self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
