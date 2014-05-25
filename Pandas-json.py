# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
from pandas import* 
import json

# <codecell>

path = 'text1.json'

# <codecell>

open(path).readline()

# <codecell>

records = [json.loads(line) for line in open(path)]

# <codecell>


print json.dumps(records, sort_keys=True, indent=4)

# <codecell>

import pandas as pd
from pandas import DataFrame, Series
from pandas.io.json import json_normalize

# <codecell>

frame = DataFrame(records)

# <codecell>

frame

# <codecell>

frame['statuses'][0]

# <codecell>

frame['statuses'][0][11]['created_at']

# <codecell>

import numpy as np
from pandas import*
import pandas as pd
import json
path = 'text1.json'
open(path).readline()
records = [json.loads(line) for line in open(path)]
print records
json_normalize(records[0]['statuses'])

# <codecell>


