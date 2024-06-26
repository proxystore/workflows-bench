from __future__ import annotations

from taps.executor.python import ProcessPoolConfig
from taps.executor.python import ThreadPoolConfig
from taps.executor.utils import FutureDependencyExecutor


def test_thread_pool_config() -> None:
    config = ThreadPoolConfig(max_threads=1)
    with config.get_executor() as executor:
        assert isinstance(executor, FutureDependencyExecutor)


def test_process_pool_config() -> None:
    config = ProcessPoolConfig(max_processes=1)
    with config.get_executor() as executor:
        assert isinstance(executor, FutureDependencyExecutor)
