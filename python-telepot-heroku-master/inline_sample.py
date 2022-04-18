import sys
from time import gmtime, strftime
import logging
logging.basicConfig(filename='inline.log', level=logging.DEBUG)

# Telegram bot api
import telepot
from telepot.delegate import per_inline_from_id, create_open
from telepot.namedtuple import *

"""
$ python inline.py <token>
A bot that only cares about inline stuff.
"""

class InlineHandler(telepot.helper.UserHandler):
    def __init__(self, seed_tuple, timeout):
        super(InlineHandler, self).__init__(seed_tuple, timeout, flavors=['inline_query', 'chosen_inline_result'])
        self._answerer = telepot.helper.Answerer(self.bot)

    def on_inline_query(self, msg):
        def compute_answer():
            global logging
            query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
            # print strftime("%d-%m-%y %H:%M : ",gmtime()),
            # print(self.id, ':', 'Inline Query:', query_id, from_id, query_string)
            logging.debug(strftime("%d-%m-%y %H:%M : ",gmtime()),\
                self.id, ':', 'Inline Query:', query_id, from_id, query_string if query_string else "<emtpy>")
            articles = [InlineQueryResultPhoto(id='123',
                            photo_url='http://www.html5rocks.com/en/tutorials/speed/img-compression/len_std.jpg',
                            thumb_url='http://www.html5rocks.com/en/tutorials/speed/img-compression/len_std.jpg',
                            photo_width=1, photo_height=1,
                            description='Photo answer'),
                        InlineQueryResultArticle(id='abc',
                            title='Text answer',
                            message_text=query_string if query_string else '*Inline bot* _says_: Empty query',
                            parse_mode='Markdown',
                            description=query_string if query_string else 'Empty query'
                        )
                        ]
            # return articles
            return {'results': articles, 'cache_time': 0, 'is_personal': False}

        self._answerer.answer(msg, compute_answer)

    def on_chosen_inline_result(self, msg):
        result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
        print(self.id, ':', 'Chosen Inline Result:', result_id, from_id, query_string)

TOKEN = sys.argv[1]

if len(sys.argv)!=2:
    print 'Usage: python inline_sample.py <bot token>'
    exit(1)

bot = telepot.DelegatorBot(TOKEN, [
    (per_inline_from_id(), create_open(InlineHandler, timeout=20)),
])
print 'Listening...'
bot.notifyOnMessage(run_forever=True)
