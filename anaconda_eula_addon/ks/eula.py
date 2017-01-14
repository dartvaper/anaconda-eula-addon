
"""Module with the EulaData class."""

import os.path

from pyanaconda.addons import AddonData
from pyanaconda.iutil import getSysroot

from pykickstart.options import KSOptionParser
from pykickstart.errors import KickstartParseError, formatErrorMsg

__all__ = ["EulaData"]


class EulaData(AddonData):
    """
    Class parsing and storing data for the EULA addon.

    """

    def __init__(self, name):

        AddonData.__init__(self, name)
        self.accepted = False
        self.RusButtonText = "Read License Agreement in Russian"
        self.EngButtonText = "Read License Agreement in English"
        self.LicenseLang = "Eng"
        self.EngText = ""
        entext = open('/usr/share/anaconda-licenses/eng.txt', 'r')
        for line in entext.readlines():
            self.EngText = self.EngText + line
        self.RusText = ""
        rutext = open('/usr/share/anaconda-licenses/rus.txt', 'r')
        for line in rutext.readlines():
            self.RusText = self.RusText + line


    def __str__(self):

        addon_str = "%%addon %s" % self.name
        return addon_str

    def handle_header(self, lineno, args):

        pass


    def handle_line(self, line):

        pass

    def finalize(self):

        # no actions needed in this addon
        pass

    def setup(self, storage, ksdata, instclass):

        # no actions needed in this addon
        pass

    def execute(self, storage, ksdata, instclass, users):

        # no actions needed in this addon
        pass
