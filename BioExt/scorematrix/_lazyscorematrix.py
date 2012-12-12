
from __future__ import division, print_function

from os.path import exists, join

from BioExt.scorematrix._scorematrix import parse_scorematrix


__all__ = []


def _lazyscorematrix(smdir, smfile):
    smpath = join(smdir, smfile)
    if exists(smpath):
        return LazyScoreMatrix(smpath)
    else:
        raise RuntimeError('cannot load Scoring Matrix, data not found!')


class LazyScoreMatrix(object):

    def __init__(self, smpath):
        self._smpath = smpath

    def load(self):
        if exists(self._smpath):
            return parse_scorematrix(self._smpath)
        else:
            msg = "cannot load ScoreMatrix '%s', file missing!" % self._smpath
            raise RuntimeError(msg)
