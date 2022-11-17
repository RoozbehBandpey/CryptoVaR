# Databricks notebook source
# MAGIC %md
# MAGIC # Modeling
# MAGIC 
# MAGIC Let's retrieve last 4 years worth of market cypto data to train a model that could predict our instrument returns. As our portfolio is made of 7 coins, we want to train 7 predictive models in parallel, collecting all weights into a single coefficient matrix for monte carlo simulations.

# COMMAND ----------

# MAGIC %md
# MAGIC ## `STEP0` Configuration

# COMMAND ----------

import pandas as pd
import math
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import mlflow

from pyspark.sql.types import *
from pyspark.sql import functions as F
from pyspark.sql.functions import pandas_udf, PandasUDFType
from datetime import datetime, timedelta

# COMMAND ----------


