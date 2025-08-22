import sys, types

# Provide a lightweight fake rpyc implementation for tests
rpyc = types.ModuleType("rpyc")
class _FakeConn:
    def __init__(self):
        self._config = {}
    def execute(self, *args, **kwargs):
        return None
    def eval(self, *args, **kwargs):
        return None
rpyc.classic = types.SimpleNamespace(connect=lambda host='localhost', port=18812: _FakeConn())
# Insert into sys.modules so mt5linux imports this fake instead of a real rpyc
sys.modules['rpyc'] = rpyc
sys.modules['rpyc.classic'] = rpyc.classic

from mt5linux import MetaTrader5

mt5 = MetaTrader5(port=1235)
mt5.initialize()
print(mt5.terminal_info())
mt5.shutdown()
assert True
