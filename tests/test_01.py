import importlib
import sys
import types
from pathlib import Path
from typing import Any, cast


# Provide a lightweight fake rpyc implementation for tests
class _FakeConn:
    def __init__(self):
        self._config = {}

    def execute(self, *args, **kwargs):
        # accept arbitrary arguments from callers (e.g. code string) and ignore
        return None

    def eval(self, *args, **kwargs):
        # accept arbitrary arguments (e.g. expressions) and ignore
        return None


# Create fake modules and register them so importing `mt5_remote` will pick them up
_fake_rpyc = types.ModuleType("rpyc")
_fake_rpyc_classic = types.ModuleType("rpyc.classic")


def _connect(host: str = "localhost", port: int = 18812) -> _FakeConn:
    # explicit use of parameters to avoid "unused" warnings
    del host, port
    return _FakeConn()


# attach the connect function to the fake classic module
# (cast to Any to satisfy static checkers)
cast(Any, _fake_rpyc_classic).connect = _connect

# register modules in sys.modules and attach the classic submodule on the parent module
sys.modules["rpyc"] = _fake_rpyc
sys.modules["rpyc.classic"] = _fake_rpyc_classic
cast(Any, _fake_rpyc).classic = _fake_rpyc_classic


def test_smoke():
    # Ensure repository root is on sys.path so tests can import the package
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

    # Import the package after faking rpyc
    mt5_remote_mod = importlib.import_module("mt5_remote")
    MetaTrader5 = mt5_remote_mod.MetaTrader5

    mt5 = MetaTrader5(port=1235)
    mt5.initialize()
    info = mt5.terminal_info()
    # info may be long, but print is now on its own line
    print(info)
    mt5.shutdown()
    assert True
