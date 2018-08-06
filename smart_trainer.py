# coding: utf-8

"""
程序入口
"""


def parse_commandline():
    pass


def main():
    args = parse_commandline()
    from gui import app

    app.start_app()


main()