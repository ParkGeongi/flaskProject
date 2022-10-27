import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from matplotlib import font_manager, rc

from ddareung import DdareungModel
from util.dataset import Dataset

warnings.simplefilter(action='ignore', category=FutureWarning)
font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family =font)


class Plot(object):
    dataset = Dataset()
    model = DdareungModel()
    def __int__(self, fname):
        self.entry = self.model.new_model(fname)

    def __str__(self):
        return f""
    def draw_(self):
        this = self.entry
