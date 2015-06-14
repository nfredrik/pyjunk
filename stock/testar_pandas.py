import pandas as pandas
from pandas import DataFrame

import datetime
import pandas.io.DataFrame
sp500 = pd.io.get_data_yahoo('%5EGSPC', start=datetime.datetime(2000, 10, 1),
										end = datetime.datetime(2014, 6, 11))