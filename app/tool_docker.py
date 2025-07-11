import subprocess
import docker
from docker.errors import NotFound
from docker.errors import APIError
from datetime import datetime

client = docker.from_env()


def print_tip(s, command=None, side="-"*10):
    print(side)
    print(s)
    if command:
        print("quit. 退出")
    print(side)


class ContainerPanel:
    def __init__(self, master, id):
        self.master = master
        self.id = id

    def handle(self):
        container = client.containers.get(self.id)
        created = datetime.strptime(container.attrs["Created"][:19], "%Y-%m-%dT%H:%M:%S")
        s = f"容器:{container.name}\n"
        s += f"ID:{container.id[:12]}\n"
        s += f"状态:{container.status}\n"
        s += f"镜像:{container.image.tags[0]}\n"
        s += f"端口:{container.ports}\n"
        s += f"创建:{created}\n"
        s += f"命令:{" ".join(container.attrs["Config"].get("Cmd", []))}"
        print_tip(s, side="="*12)
        input("按Enter退出")
        self.master.pop()


class ContainerHandler:
    def __init__(self, master, id):
        self.master = master
        self.id = id

    def handle(self):
        container = client.containers.get(self.id)
        tip = f"容器: {container.name}, 状态: {container.status}, 镜像: {container.image.tags[0]}\n"
        tip += "1. 查看\n2. 启动\n3. 停止\n4. 删除"
        print_tip(tip, command=True)
        res = input("")
        if res == "quit":
            self.master.pop()
            return
        if res == "1":
            # self.context.append([cont.id[:12], cont.image.tags[0].split(":")[0], cont.command, cont.created_at, cont.status, cont.ports, cont.attrs['Name']])
            handler = ContainerPanel(self.master, self.id)
            self.master.push(handler)
        elif res == "2":
            try:
                container.start()
                print("启动成功!")
            except Exception as e:
                print(e)
        elif res == "3":
            try:
                container.stop()
                print("停止成功!")
            except Exception as e:
                print(e)
        elif res == "4":
            try:
                container.remove()
                print("删除成功!")
            except Exception as e:
                print(e)
            self.master.pop()
        else:
            print("输入错误")


class ContainerListHandler:
    def __init__(self, master):
        self.master = master

    def handle(self):
        containers = client.containers.list(all=True)
        ids = [cont.id for cont in containers]
        tip = ""
        for i in range(len(containers)):
            cont = containers[i]
            id = cont.id[:12]
            image = cont.image.tags[0].split(":")[0]
            name = cont.attrs['Name']
            status = cont.status
            s = f"{i+1}. 容器:{name}, 状态:{status}, 镜像:{image}"
            if i == len(containers)-1:
                tip += s
            else:
                tip += s + "\n"
        print_tip(tip, command=True)
        res = input("")
        if res == "quit":
            self.master.pop()
            return
        if 1 <= int(res) <= len(containers):
            handler = ContainerHandler(self.master, ids[int(res)-1])
            self.master.push(handler)
        else:
            print("输入错误")


class ImagePanel:
    def __init__(self, master, id):
        self.master = master
        self.id = id
    
    def handle(self):
        image = client.images.get(self.id)
        created = datetime.strptime(image.attrs["Created"][:19], "%Y-%m-%dT%H:%M:%S")
        s = f"镜像:{image.tags[0]}\n"
        s += f"ID:{image.id[7:19]}\n"
        s += f"创建:{created}\n"
        s += f"大小:{round(image.attrs['Size']/(1024**2), 2)}MB\n"
        s += f"命令:{" ".join(image.attrs["Config"].get("Cmd", []))}"
        print_tip(s, side="="*12)
        input("按Enter退出")
        self.master.pop()


class ImageHandler:
    def __init__(self, master, id):
        self.master = master
        self.id = id

    def handle(self):
        image = client.images.get(self.id)
        tip = f"镜像: {image.tags[0]}\n"
        tip += "1. 查看\n2. 删除"
        print_tip(tip, command=True)
        res = input("")
        if res == "quit":
            self.master.pop()
            return
        if res == "1":
            handler = ImagePanel(self.master, self.id)
            self.master.push(handler)
        elif res == "2":
            try:
                image.remove()
                print("删除成功!");
            except Exception as e:
                print(e)
            self.master.pop()
        else:
            print("输入错误")


class ImageListHandler:
    def __init__(self, master):
        self.master = master

    def handle(self):
        images = client.images.list()
        ids = [img.id for img in images]
        tip = ""
        for i in range(len(images)):
            img = images[i]
            name, tag = None, None
            if img.tags:
                name, tag = img.tags[0].split(":")
            else:
                name, tag = "<none>", "<none>"
            size = round(img.attrs['Size']/(1024**2), 2)
            s = f"{i+1}. 镜像:{name}, Tag:{tag}, 大小:{size}MB"
            if i == len(images)-1:
                tip += s
            else:
                tip += s + "\n"
        print_tip(tip, command=True)
        res = input("")
        if res == "quit":
            self.master.pop()
            return
        if 1 <= int(res) <= len(images):
            handler = ImageHandler(self.master, ids[int(res)-1])
            self.master.push(handler)
        else:
            print("输入错误")


class VolumePanel:
    def __init__(self, master, id):
        self.master = master
        self.id = id
    
    def handle(self):
        volume = client.volumes.get(self.id)
        tip = f"名称: {volume.name}\n"
        tip += f"ID: {volume.id}\n"
        tip += f"挂载点: {volume.attrs['Mountpoint']}\n"
        tip += f"驱动: {volume.attrs['Driver']}\n"
        tip += f"创建时间: {volume.attrs['CreatedAt']}\n"
        tip += f"标签: {volume.attrs['Labels']}"
        print_tip(tip, side="="*12)
        input("按Enter退出")
        self.master.pop()


class VolumeHandler:
    def __init__(self, master, id):
        self.master = master
        self.id = id

    def handle(self):
        volume = client.volumes.get(self.id)
        tip = f"数据卷: {volume.name}, 驱动: {volume.attrs['Driver']}\n"
        tip += "1. 查看\n2. 删除"
        print_tip(tip, command=True)
        res = input("")
        if res == "quit":
            self.master.pop()
            return
        if res == "1":
            handler = VolumePanel(self.master, self.id)
            self.master.push(handler)
        elif res == "2":
            try:
                volume.remove()
                print("删除成功!");
            except Exception as e:
                print(e)
            self.master.pop()
        else:
            print("输入错误")


class VolumeListHandler:
    def __init__(self, master):
        self.master = master

    def handle(self):
        volumes = client.volumes.list()
        ids = [v.id for v in volumes]
        tip = ""
        for i in range(len(volumes)):
            volume = volumes[i]
            name = volume.name
            driver = volume.attrs['Driver']
            s = f"{i+1}. 数据卷:{name}, 驱动:{driver}"
            if i == len(volumes)-1:
                tip += s
            else:
                tip += s + "\n"
        print_tip(tip, command=True)
        res = input("")
        if res == "quit":
            self.master.pop()
            return
        if 1 <= int(res) <= len(volumes):
            handler = VolumeHandler(self.master, ids[int(res)-1])
            self.master.push(handler)
        else:
            print("输入错误")


class Handler:
    def __init__(self, master):
        self.master = master

    def handle(self):
        s = "1. 容器\n2. 镜像\n3. 数据卷"
        print_tip(s, command=True)
        res = input("")
        if res == "quit":
            self.master.pop()
            return
        if res == "1":
            handler = ContainerListHandler(self.master)
            self.master.push(handler)
        elif res == "2":
            handler = ImageListHandler(self.master)
            self.master.push(handler)
        elif res == "3":
            handler = VolumeListHandler(self.master)
            self.master.push(handler)
        else:
            print("输入错误")


class DockerManager:
    def __init__(self):
        self.stack = []
        self.context = None

    def run(self):
        while self.stack:
            handler = self.stack[-1]
            handler.handle()

    def push(self, handler):
        self.stack.append(handler)

    def pop(self):
        return self.stack.pop()


if __name__ == "__main__":
    mgr = DockerManager()
    mgr.push(Handler(mgr))
    mgr.run()

