# mt5_remote — Remote MetaTrader 5 access

mt5_remote lets you control MetaTrader 5 from any machine by connecting to a remote Windows Python process that runs MT5. Your client script (Linux, macOS, or Windows) sends commands to a server running MetaTrader5 on Windows (native Windows or via Wine).

This project builds on the original mt5linux package, maintaining compatibility with its Linux support while adding generalized remote access. Unlike the original mt5linux, this version works with modern Python versions.

## Purpose

- Run MT5 trading scripts from any machine by connecting to a remote MT5 server
- Keep your trading logic on Linux/macOS while MT5 runs on Windows (locally via Wine/VM or on a remote Windows machine)
- Simple client/server setup that generally allows you to keep your trading logic and MT5 terminals separate

## Install

1. Set up a Windows Python environment that can run the MetaTrader5 package. This can be:
   - Wine + Windows Python on Linux
   - Native Windows OS + Python
   - Windows VM with Python

2. Clone this repository and install from source:

   **On both client and server machines:**
   ```bash
   # Clone the repository
   git clone <repo-url>
   cd mt5linux
   
   # Create virtual environment (recommended: uv)
   uv venv
   source .venv/bin/activate  # Linux/Mac
   # or: .venv\Scripts\activate  # Windows
   
   # Alternative: standard venv
   # python -m venv .venv && source .venv/bin/activate
   
   # Install base requirements and package
   pip install -r requirements.txt
   pip install -e .
   ```

   **Additionally on the remote server only:**
   ```bash
   # In the activated server venv
   pip install -r server-requirements.txt
   ```

   **Note:** Always activate the virtual environment before running client/server commands. `requirements.txt` contains base requirements for both client and server. `server-requirements.txt` adds MT5-specific dependencies only needed on the server.

## How to use

1. Start MetaTrader 5 on the machine with Windows Python (native Windows, Wine, or VM).

2. Start the server that connects to MT5:

```bash
# Make sure server venv is activated first
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
python -m mt5_remote <path/to/windows/python.exe>
```

The `<path/to/windows/python.exe>` parameter is the path to your Windows Python interpreter **inside the virtual environment** where you installed the server requirements. Examples:
- Native Windows: `.venv\Scripts\python.exe`
- Wine on Linux: `--wine wine .venv/Scripts/python.exe` (note the `--wine` flag)
- Windows VM: `.venv/Scripts/python.exe` (or full path to venv within VM)

**Note:** 
- Use the venv's python.exe (not system Python) unless you installed packages globally
- For Wine, you must use the `--wine` argument to specify the Wine command
- Relative paths work fine if you're in the project directory

3. From your client machine (can be the same machine for localhost usage), connect and run your trading logic:

```python
from mt5_remote import MetaTrader5

# Connect to MT5 server (defaults: localhost:18812)
mt5 = MetaTrader5()

mt5.initialize()
info = mt5.terminal_info()
rates = mt5.copy_rates_from_pos('EURUSD', mt5.TIMEFRAME_M1, 0, 1000)
mt5.shutdown()
```

**Common Usage Scenarios:**
- **Linux/macOS development with Wine:** Run the server via Wine locally, develop your trading logic in native Linux/macOS Python
- **Linux/macOS with Windows VM:** Run the server in a Windows VM, connect from Linux/macOS host
- **Remote Windows server:** Run the server on a separate Windows machine, connect from any client

**Server Options:**
Run `python -m mt5_remote --help` for host, port, and other configuration options.

## Credits

Originally created as the `mt5linux` project by Lucas Prett Campagna (github: `lucas-campagna`). This repository repurposes and extends that work — maintained by BigMitchGit.

## License

This project is released under the MIT License. See the `LICENSE.txt` file for details.
