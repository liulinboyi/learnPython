import sys

sys.path.append("../")  # 追加上级目录的上级目录的上级目录到path路径中

from test_package import hello

# hello.say("usePackage")


def hi():
    hello.say("usePackage")
