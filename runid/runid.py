#!/usr/bin/env python
# -*- coding: utf-8 -*-


from joblib import load, dump


class RunId(object):

    def __init__(self, path='runid.stored', runid=None):

        # Step size is not an input param,
        # make it instance variable for future flexibility
        self.__step_size = 1
        self.path = path

        # runid as param overwrites previously used and stored runids
        if runid is not None:
            self.runid = runid
        else:
            try:
                self.from_file()
                self.runid += self.__step_size
            except:
                self.runid = 1

        self.to_file()

    def __repr__(self):
        return f"RunId(path='{self.path}', runid={self.runid})"

    def __str__(self):
        return f'RunId ({self.runid}) stored @ {self.path}'

    @property
    def runid(self):
        return self.__runid

    @runid.setter
    def runid(self, new_runid):
        self.__runid = new_runid

    def step(self):
        self.runid += self.__step_size
        self.to_file()

    def reset(self, runid=1):
        self.runid = runid
        self.to_file()

    def to_file(self):
        dump(self.runid, self.path)

    def from_file(self):
        self.runid = load(self.path)

