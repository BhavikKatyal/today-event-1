# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.
import requests
from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'bhavik'

LOGGER = getLogger(__name__)


class TodaySkill(MycroftSkill):
    def __init__(self):
        super(TodaySkill, self).__init__(name="TodaySkill")

    def initialize(self):
            today_event_intent = IntentBuilder("TodayEventIntent"). \
            require("TodayEventKeyword").build()
        self.register_intent(today_event_intent, self.handle_today_event_intent)
    def handle_today_event_intent(self, message):
        url =" http://history.muffinlabs.com/date"
            r=requests.get(url)
            json_output=r.json()
            output=json_output['data']
            events=output["Events"]

            self.speak_dialog("Today in history event {} occured".format(events[0]['text']))


    def stop(self):
        pass


def create_skill():
    return TodaySkill()
