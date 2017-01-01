# -*- coding:utf-8

from FBRank.parse.League import parse_league_rank
from FBRank.utils.utils import league_configure, league_transformat
from FBRank.utils.exceptions import IllegalNameException


class League(object):
    def __init__(self, pass_name):
        self.name = self._get_name(pass_name)  # to be converted
        self.rank = self._get_webrank()

    def _get_name(self, pass_name):
        for league_list in league_transformat.keys():
            if pass_name in league_list or pass_name.lower() in league_list:
                return league_transformat.get(league_list)

        raise IllegalNameException("")

    def _get_webrank(self, index=0):
        return parse_league_rank(self._get_url(), index)

    def _get_url(self):
        return league_configure[self.name]['rank_url']