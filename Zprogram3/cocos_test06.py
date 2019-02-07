#跟着教程走，幸福天天有
#导入cocos
import cocos
#继承Layer，并在这里定义程序的逻辑
class HelloWorld(cocos.layer.Layer):
    #初始化，调用super构造函数
    def __init__(self):
        super(HelloWorld, self).__init__()

        #要显示文本，我们将创建一个Label,
        #参数用于设置这个Label的字体，位置和对其方式
        label = cocos.text.Label('Hello,World!',
                                 font_name='Time New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        #label将显示在中央
        label.position = 320,240
        #现在label是CocosNode的子类，他可以作为一个子项被添加
        #所有的CocosNode对象知道怎样渲染自己，执行操作和转换
        #添加它作为layer的子项，用CocosNode的add方法
        self.add(label)

#HelloWorld已经定义完了，剩下就是运行了
if __name__ == '__main__':
        #之后定义HelloWorld类，
        #我们需要初始化并创建一个window，为此，我们需要初始化Director
        cocos.director.director.init()
        #然后我们创建一个HelloWorld实例
        hello_layer = HelloWorld()
        #然后我们创建一个Scene，讲HelloWorld layer作为一个图层添加进去
        main_scene = cocos.scene.Scene(hello_layer)
        #最后我们运行一下这个scene
        cocos.director.director.run(main_scene)
        
