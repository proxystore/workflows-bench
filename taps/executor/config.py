from __future__ import annotations

import abc
from concurrent.futures import Executor

from pydantic import BaseModel
from pydantic import ConfigDict


class ExecutorConfig(BaseModel, abc.ABC):
    """Abstract executor configuration."""

    name: str

    model_config: ConfigDict = ConfigDict(  # type: ignore[misc]
        extra='forbid',
        validate_default=True,
        validate_return=True,
    )

    @abc.abstractmethod
    def get_executor(self) -> Executor:
        """Create an executor from the configuration."""
        ...
