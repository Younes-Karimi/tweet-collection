import os
import shutil

path = 'tweets/'
filenames = [int(n.split('.json')[0]) for n in os.listdir(path) if n != '.DS_Store']
for i in sorted(filenames):
  if i % 10000 == 0:
    os.mkdir('../batch-{}'.format(int(i/10000)))
  shutil.move(str(i)+'.json', '../batch-{}/{}'.format(int(i/10000), str(i)+'.json'))

for fname in os.listdir('.'):
  if fname.startswith('batch'):
    shutil.make_archive(fname, 'zip', fname)