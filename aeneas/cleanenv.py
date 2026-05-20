import os

clean_env = os.environ.copy()
if "LD_LIBRARY_PATH" in clean_env:
    del clean_env["LD_LIBRARY_PATH"]
