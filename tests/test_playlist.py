from src.playlist import PlayList
import sys
sys.path.append('../')
import datetime

pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
assert pl.title == "Moscow Python Meetup №81"
assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

duration = pl.total_duration
assert str(duration) == "1:49:52"
assert isinstance(duration, datetime.timedelta)
assert duration.total_seconds() == 6592.0

assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"

pl2 = PlayList('PLPOCJi2Sznkon9RukWZlPx-9JGvy-uBVe')
duration2 = pl2.total_duration
assert str(duration2) == '2:08:46'