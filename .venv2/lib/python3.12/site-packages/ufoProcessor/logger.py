import sys
import time
import os
import logging

class Logger:

    def __init__(self, path, rootDirectory, nest=0):
        self.path = path
        self.rootDirectory = rootDirectory
        self.nest = nest
        if not nest:
            if path is not None:
                if os.path.exists(path):
                    os.remove(path)
                if not os.path.exists(path):
                    f = open(path, "w")
                    f.close()

    def child(self, text=None):
        logger = Logger(
            self.path,
            self.rootDirectory,
            nest=self.nest + 1
        )
        if text:
            logger.info(text)
        return logger

    def relativePath(self, path):
        return os.path.relpath(path, self.rootDirectory)

    def _makeText(self, text):
        if self.nest:
            text = f"{('| ' * self.nest).strip()} {text}"
        return text

    def _toConsole(self, text):
        print(text)

    def _toFile(self, text):
        if self.path is None:
            return
        text += "\n"
        f = open(self.path, "a")
        f.write(text)
        f.close()

    def time(self, prefix=None):
        now = time.strftime("%Y-%m-%d %H:%M")
        if prefix:
            now = prefix + " " + now
        self.info(now)

    def info(self, text):
        text = self._makeText(text)
        self._toConsole(text)
        self._toFile(text)

    def infoItem(self, text):
        text = f"\t- {text}"
        self.info(text)

    def infoPath(self, path):
        text = self.relativePath(path)
        self.infoItem(text)

    def detail(self, text):
        text = self._makeText(text)
        self._toFile(text)

    def detailItem(self, text):
        text = f"- {text}"
        self.detail(text)

    def detailPath(self, path):
        text = self.relativePath(path)
        self.detailItem(text)
