
"""Module with the EulaSpoke class."""


_ = lambda x: x
N_ = lambda x: x

# the path to addons is in sys.path so we can import things from anaconda_eula_addon
from anaconda_eula_addon.categories.eula import EulaCategory
from pyanaconda.ui.gui import GUIObject
from pyanaconda.ui.gui.spokes import NormalSpoke
from pyanaconda.ui.common import FirstbootSpokeMixIn

# export only the spoke, no helper functions, classes or constants
__all__ = ["EulaSpoke"]

class EulaSpoke(FirstbootSpokeMixIn, NormalSpoke):

    ### class attributes defined by API ###

    # list all top-level objects from the .glade file that should be exposed
    # to the spoke or leave empty to extract everything
    builderObjects = []

    # the name of the main window widget
    mainWidgetName = "EulaSpokeWindow"

    # name of the .glade file in the same directory as this source
    uiFile = "eula.glade"

    # category this spoke belongs to
    category = EulaCategory

    # spoke icon (will be displayed on the hub)
    # preferred are the -symbolic icons as these are used in Anaconda's spokes
    icon = "checkbox-checked-symbolic"

    # title of the spoke (will be displayed on the hub)
    title = N_("_EULA")

    ### methods defined by API ###
    def __init__(self, data, storage, payload, instclass):

        NormalSpoke.__init__(self, data, storage, payload, instclass)

    def initialize(self):

        NormalSpoke.initialize(self)
        self._accept_button = self.builder.get_object("AcceptButton")
        self._switch_lang_button = self.builder.get_object("SwitchLangButton")
        self._license_text_area = self.builder.get_object("LicenseTextArea")
        self._license_text_buffer = self.builder.get_object("LicenseTextBuffer")
        self._license_text_buffer.set_text(self.data.addons.anaconda_eula_addon.EngText, length=-1)

    def refresh(self):

        self._accept_button.set_active(self.data.addons.anaconda_eula_addon.accepted)
        if (self.data.addons.anaconda_eula_addon.LicenseLang == "Eng"):
            self._license_text_buffer.set_text(self.data.addons.anaconda_eula_addon.EngText, length=-1)
            self._switch_lang_button.set_label(self.data.addons.anaconda_eula_addon.RusButtonText)
        else:
            self._license_text_buffer.set_text(self.data.addons.anaconda_eula_addon.RusText, length=-1)
            self._switch_lang_button.set_label(self.data.addons.anaconda_eula_addon.EngButtonText)

    def apply(self):

        self.data.addons.anaconda_eula_addon.accepted = self._accept_button.get_active()

    def execute(self):

        # nothing to do here
        pass

    @property
    def ready(self):

        # this spoke is always ready
        return True

    @property
    def completed(self):

        return bool(self.data.addons.anaconda_eula_addon.accepted)

    @property
    def mandatory(self):

        # this is an optional spoke that is not mandatory to be completed
        return True

    @property
    def status(self):

        accept = self._accept_button.get_active()

        if accept:
            return _("License Agreement Accepted")
        else:
            return _("License Agreement Not Accepted")

    
    ### handlers ###
    def on_SwitchLangButton_clicked(self, *args):
        if (self.data.addons.anaconda_eula_addon.LicenseLang == "Eng"):
            self.data.addons.anaconda_eula_addon.LicenseLang = "Rus"
            self._license_text_buffer.set_text(self.data.addons.anaconda_eula_addon.RusText, length=-1)
            self._switch_lang_button.set_label(self.data.addons.anaconda_eula_addon.EngButtonText)
        else:
            self.data.addons.anaconda_eula_addon.LicenseLang = "Eng"
            self._license_text_buffer.set_text(self.data.addons.anaconda_eula_addon.EngText, length=-1)
            self._switch_lang_button.set_label(self.data.addons.anaconda_eula_addon.RusButtonText)

