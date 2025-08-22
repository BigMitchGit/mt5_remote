# mt5_remote — Remote MetaTrader 5 access

mt5_remote provides cross-platform remote execution and access to MetaTrader 5 terminals. It lets an orchestrator (Linux or Windows) send MT5 operations to a remote Python process running MetaTrader5 on a Windows environment (native Windows or via Wine).

This project repurposes the original mt5linux package to focus on a client/server remote architecture for sending MT5 commands to a remote terminal.

## Purpose

- Allow scripts on one machine (the client/orchestrator) to control MetaTrader 5 running on a remote machine.
- Support Windows-native MT5 Python integration as the remote endpoint; the orchestrator may run on Linux or Windows.
- Keep the transport minimal and secure for closed networks (authentication and encryption improvements may be added later).

## Install

1. Ensure you have a Windows Python that can run the MetaTrader5 package. On Linux you can use Wine + a Windows Python install.

2. Install the MetaTrader5 Python package into the Windows Python environment:

```
pip install MetaTrader5
```

3. Install project dependencies and this package (on the side(s) where you need the client/server code):

```
pip install -r requirements.txt
pip install -e .
```

## How to use

1. Start MetaTrader 5 on the machine that will act as the remote endpoint (Windows or Wine).

2. On the remote machine (Windows/Wine), start the server process that exposes MT5 operations. Example (adjust the module name and path to your Windows python executable as needed):

```
python -m mt5_remote <path/to/python.exe>
```

3. On the orchestrator (client) machine, import the client API and use it much like the regular MetaTrader5 package. Example usage:

```python
# import the remote client API
from mt5_remote import MetaTrader5

# connect to the remote MT5 server
mt5 = MetaTrader5(
    # host='localhost' (default)
    # port=18812           (default)
)

mt5.initialize()
info = mt5.terminal_info()
rates = mt5.copy_rates_from_pos('GOOG', mt5.TIMEFRAME_M1, 0, 1000)
# ... perform operations remotely
mt5.shutdown()
```

Notes:
- Command-line options for the server (host, port, exe path, verbosity) are available; run `python -m mt5_remote --help` on the remote machine.

## Credits

Originally created as the `mt5linux` project by Lucas Prett Campagna (github: `lucas-campagna`). This repository repurposes and extends that work — maintained by BigMitchGit.

## License

This project is released under the MIT License. See the `LICENSE.txt` file for details.
