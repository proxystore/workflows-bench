from __future__ import annotations

from taps.executor.config import ExecutorConfig
from taps.executor.dask import DaskDistributedConfig

# These imports are needed to ensure the executor
# config registration decorator in each file is run.
from taps.executor.dask import DaskDistributedExecutor
from taps.executor.globus import GlobusComputeConfig
from taps.executor.parsl import ParslConfig
from taps.executor.python import ProcessPoolConfig
from taps.executor.python import ThreadPoolConfig
from taps.executor.ray import RayConfig
from taps.executor.ray import RayExecutor
