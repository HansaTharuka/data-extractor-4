# -*- coding: utf-8 -*-
import sys
sys.path.append("Azure")
from getprintedtext import getdataandsavetomongo
from Extractor import extractdata 

extractdata()
getdataandsavetomongo()