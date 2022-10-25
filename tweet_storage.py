"""
__author__: y.karimi.324@gmail.com

This script splits large collections of streaming tweets into smaller batches
and zips the batches to reduce the space needed for storing the batches.
"""

import os
import shutil

batch_size = 10000
src_path = '../tweets'
dst_path = '../batch_tweets'

if not os.path.exists(dst_path):
  os.mkdir(dst_path)
if os.path.exists(src_path):
  filenames = [int(n.split('.json')[0]) for n in os.listdir(src_path) if n != '.DS_Store']
  # split tweets into separate batches (folders)
  for i in sorted(filenames)[:-1]: # excluding the last item to preserve the numbering for new collection (if still collecting)
    batch_path = os.path.join(dst_path, 'batch-{}'.format(int(i / batch_size)))
    if not os.path.exists(batch_path):
      os.mkdir(batch_path)
    shutil.move(os.path.join(src_path, str(i) + '.json'), os.path.join(batch_path, str(i) + '.json'))
  print('Finished splitting the tweets into batches!')
else:
  print('Source path was not found! ', src_path)
# zip and remove the batch folders
if os.path.exists(dst_path):
  for batch_name in os.listdir(dst_path):
    if batch_name.startswith('batch') and not batch_name.endswith('.zip'):
      if len([n for n in os.listdir(os.path.join(dst_path, batch_name)) if n != '.DS_Store']) == batch_size:
        if not os.path.exists(os.path.join(dst_path, batch_name + '.zip')):
          shutil.make_archive(batch_name, 'zip', os.path.join(dst_path, batch_name))
          print('Finished zipping: ', batch_name)
        shutil.rmtree(os.path.join(dst_path, batch_name))
else:
  print('Destination path was not found! ', dst_path)
