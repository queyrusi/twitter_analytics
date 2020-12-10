"""Fetch function.
"""

import twint

c = twint.Config()
c.Lang = 'fr'
c.Search = "#Cyberpunk2077"
# c.Format = "ID {id} | Username {username}"
c.Limit = 20

twint.run.Search(c)

# Tweets_df = twint.storage.panda.Follow_df