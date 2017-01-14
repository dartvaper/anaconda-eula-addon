
"""Eula category module"""

N_ = lambda x: x

from pyanaconda.ui.categories import SpokeCategory

__all__ = ["EulaCategory"]

class EulaCategory(SpokeCategory):
    displayOnHubGUI = "SummaryHub"
    displayOnHubTUI = "SummaryHub"
    title = N_("EULA")
