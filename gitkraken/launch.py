#!/usr/bin/env python3

import sys
import iterm2
import AppKit

# Launch the app
AppKit.NSWorkspace.sharedWorkspace().launchApplication_("iTerm2")

async def main(connection):
    app = await iterm2.async_get_app(connection)

    # Foreground the app
    await app.async_activate()

    # This will run 'vi' from bash. If you use a different shell, you'll need
    # to change it here. Running it through the shell sets up your $PATH so you
    # don't need to specify a full path to the command.
    cmd = ""
    if len(sys.argv) > 0:
        cmd = sys.argv[1]
    await iterm2.Window.async_create(connection, command=f"/bin/zsh -l -c '{cmd}'")

# Passing True for the second parameter means keep trying to
# connect until the app launches.
iterm2.run_until_complete(main, True)
