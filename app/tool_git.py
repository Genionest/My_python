import sys, os
import git
from git import GitCommandError

REPO:git.Repo = None
PATH:str = None

def print_tip(s, command=None, side="-"*10):
    print(side)
    print(s)
    if command:
        print("quit. 退出")
    print(side)


class GitPanel:
    def __init__(self, master, txt):
        self.master = master
        self.txt = txt

    def handle(self):
        tip = self.txt
        print_tip(tip, side="="*12)
        input("按Enter退出")
        self.master.pop()


class GitLogList:
    def __init__(self, master):
        self.master = master

    def handle(self):
        REPO.git.log()


class GitWorkFlow:
    def __init__(self, master):
        self.master = master

    def handle(self):
        abs_path = os.path.abspath(PATH)
        tip = f"仓库:{abs_path}\n"
        tip += "1. fetch\n2. status\n3. add\n4. commit\n5. push"
        print_tip(tip, command=True)
        res = input("")
        if res == "quit":
            self.master.pop()
            return
        if res == "1":
            def progress_update(op_code, cur_count, max_count, message):
                print(f"Progress: {cur_count}/{max_count} - {message}")
            try:
                REPO.remotes.origin.fetch(progress=progress_update)
                print("fetching...")
            except GitCommandError as e:
                print(f"Fetch failed: {e.stderr}")
        elif res == "2":
            handle = GitPanel(self.master, REPO.git.status())
            self.master.push(handle)
        elif res == "3":
            REPO.git.add(".")
        elif res == "4":
            comment = input("输入注释:")
            if not comment:
                comment = "update"
            REPO.git.commit("-m", comment)
        elif res == "5":
            REPO.git.push()
        else:
            print("输入错误")


class GitHandler:
    def __init__(self, master):
        self.master = master

    def handle(self):
        # 获取绝对路径
        abs_path = os.path.abspath(PATH)
        tip = f"仓库:{abs_path}\n"
        tip += f"1. fetch\n2. status\n3. work-flow\n4. log\n5. diff"
        print_tip(tip, command=True)
        res = input("")
        if res == "quit":
            self.master.pop()
            return
        if res == "1":
            def progress_update(op_code, cur_count, max_count, message):
                print(f"Progress: {cur_count}/{max_count} - {message}")
            try:
                REPO.remotes.origin.fetch(progress=progress_update)
                print("fetching...")
            except GitCommandError as e:
                print(f"Fetch failed: {e.stderr}")
        elif res == "2":
            handle = GitPanel(self.master, REPO.git.status())
            self.master.push(handle)
        elif res == "3":
            handle = GitWorkFlow(self.master)
            self.master.push(handle)
        elif res == "4":
            handle = GitPanel(self.master, "log")
            self.master.push(handle)
        elif res == "5":
            handle = GitPanel(self.master, REPO.git.diff())
            self.master.push(handle)
        else:
            print("输入错误")

class GitManager:
    def __init__(self):
        self.stack = []

    def run(self):
        while self.stack:
            handler = self.stack[-1]
            handler.handle()

    def push(self, handler):
        self.stack.append(handler)

    def pop(self):
        return self.stack.pop()
    

if __name__ == "__main__":
    PATH = sys.argv[1]
    try:
        REPO = git.Repo(PATH)
        mgr = GitManager()
        mgr.push(GitHandler(mgr))
        mgr.run()
    except Exception as e:
        print(f"path '{e}' is not a valid repository")
        print(f"You can use 'git clone <url>' to create one repository.")