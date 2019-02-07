import cocos
from cocos.actions import MoveBy,MoveTo,RotateBy,Repeat

class Fly(cocos.layer.Layer):

    def __init__(self):
        super(Fly,self).__init__()

        rocket = cocos.sprite.Sprite('rocket.png')
        rocket.position = 128,128
        rocket.scale = 0.5
        #在5秒内往右上方西东，最终横竖坐标分别增加50
        #rocket.do( MoveBy( (320,240), duration=2) )
        #move = MoveTo( (200,200),2 ) + MoveTo( (400,400),3 )
        move = Repeat( RotateBy(360, 2) )
        rocket.do(move)
        self.add(rocket, z=0)

if __name__ == '__main__':
    cocos.director.director.init()
    scene = cocos.scene.Scene(Fly())
    cocos.director.director.run(scene)
