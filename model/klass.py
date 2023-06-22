from model.analysis import *
from model.analysis_categorization import *
from model.analysis_method import *
from model.analysis_set import *
from model.data_subset import *
from model.display_section import *
from model.nested_list import *
from model.output import *
from model.reporting_event import *
from model.subject_grouping_factor import *


class Klass():

  def get(name):
    return globals()[name]