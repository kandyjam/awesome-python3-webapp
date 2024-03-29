import asyncio

import www.orm
from www.models import User


async def test(loop):

    await www.orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='ablout:blank')
    await u.save()


# for x in test():
#     pass

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
