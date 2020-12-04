'Sample data for pubsub'

from pprint import pprint
from time import time
from pubsub import post_message, follow

# set_user('raymondh', displayname='Raymond Hettinger', password='superman123',
#          email='python@rcn.com', bio='Former fashion photographer', photo='raymond.jpg')
# set_user('barry', displayname='Barry Warsaw', password='lonelyheart50',
#          email='bw@python.org', bio='Plays in a band', photo='barry_warsaw.jpg')
# set_user('davin', displayname='Davin Potts', password='talltex89',
#          email='davin@appliomics.com', bio='Chemist, Teacher, Father', photo='davin-potts-200.png')
# set_user('selik', displayname='Michael Selik', password='newlywed7',
#          email='mselik@example.com', bio='All problems are data science problems', photo='selik.jpg')

now = time()
post_message('raymondh', '#python tip: use named tuples', now-3600*48)
post_message('barry', 'join a band today', now-3600)
post_message('selik', 'gradient descent save me money on travel', now-2500)
post_message('raymondh', '#python tip: develop interactively', now-500)
post_message('barry', 'learn emacs', now-80)
post_message('davin', '@raymondh teaching #python today', now-50)
post_message('selik', 'have you ever wanted to unpack mappings?', now-46)
post_message('raymondh', '#python tip: have fun programming', now-40)
post_message('davin', '#camping tip:  always take water', now-30)
post_message('barry', 'enums rock', now-20)
post_message('raymondh', '#python tip: never mutate while iterating', now-10)
post_message('davin', 'coriander and cilantro come from the same plant', now)

follow('davin', followed_user='raymondh')
follow('davin', followed_user='barry')
follow('selik', followed_user='davin')
follow('raymondh', followed_user='selik')
follow('raymondh', followed_user='barry')

if __name__ == '__main__':
    from pubsub.pubsub import posts
    pprint(posts)
