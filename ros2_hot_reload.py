from watchfiles import watch
import pathlib
from pathlib import Path
import subprocess


ws_path = ""
ws_name = pathlib.Path(ws_path).parts[-1]
print(f"start hotreload at {ws_name}")

for changes in watch(ws_path):
    path = Path(list(changes)[0][1]).relative_to(ws_path)
    if(path.parts[0] == "src"):
        print(f"Changes detected at: {path.parts[1]}")
        subprocess.run(["colcon", "build","--packages-select",path.parts[1]])
    
    