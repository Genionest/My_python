#跑跑cocos，看看可以不

import cocos

class hello(cocos.layer.Layer):
    def __init__(self):
        super(hello,self).__init__()
        #创建标签，这里就是引用pyglet
        label = cocos.text.Label('Hello',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        #获得导演窗口的宽度和高度，是一个二元组
        width, height = cocos.director.director.get_window_size()
        #设置标签位置
        label.position = width // 2, height // 2 # //整数除法，结果没有小数部分
        #添加标签到HelloWorld层
        self.add(label)

if __name__ == '__main__':
    #初始化导演
    cocos.director.director.init(width=640,height=480,caption='hell world')
    #创建层
    layer = hello()
    #创建场景 添加层进来
    main_scence = cocos.scene.Scene(layer)
    #启动场景
    cocos.director.director.run(main_scence)
    #来自有道翻译 scene场面；scence外景地


#可以的
