import glob
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'makertai'))
from testreport import DataTable

# read data:
dt = DataTable()
first = True
for file in glob.glob('*/summary.md'):
    with open(file, 'r') as sf:
        for k, line in enumerate(sf):
            if first and k == 0:
                header = [ s.strip() for s in line.split('|') ][1:-1]
                for hs in header:
                    dt.add_column(hs, '1', '%-s')
            first = False
            if k == 2:
                data = [ s.strip() for s in line.split('|') ][1:-1]
                for c, ds in enumerate(data):
                    dt.add_value(ds, c)
                    if ds.isdigit():
                        dt.set_format('%s', c)
                break
dt.adjust_columns()
dt.sort(['mean jitter'])
dt.hide('num')

# read file:
lines = []
with open('README.md', 'r') as sf:
    for line in sf:
        lines.append( line )
        if 'Click on the machine link for details' in line:
            break

# write file:
with open('README.md', 'w') as df:
    df.write(''.join(lines))
    df.write('\n')
    dt.write(df, units='none', table_format='md')

