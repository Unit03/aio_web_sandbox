from aiopg.sa import create_engine
import asyncio
import sqlalchemy as sa
from sqlalchemy import sql

from foo import settings

metadata = sa.MetaData()

bars_table = sa.Table(
    'bar',
    metadata,

    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(50), nullable=False),
    sa.Column("created_at", sa.DateTime),
)


# TODO: This could be async def if not for `engine` (returned by
# `create_engine` that doesn't yet support async/await syntax.
@asyncio.coroutine
def get_some_bar():
    engine = yield from create_engine(settings.DSN)
    with (yield from engine) as connection:
        query = sql.select([bars_table])
        return (yield from (yield from connection.execute(query)).fetchone())
