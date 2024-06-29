from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSessions

from workout_api.configs.database import get_session

DatabaseDependency = Annotated[AsyncSessions, Depends(get_session)]
