import os
from git.exc import GitCommandError
from git import Repo
import toml
import requests
from rich import print
from rich import progress
from rich.progress import Progress
from rich.progress import TextColumn,TimeElapsedColumn,TaskProgressColumn,SpinnerColumn,BarColumn

cfg_file = toml.load("./depend.toml")

depend_lib = cfg_file["depend"]

def download_release(url,name,path):
    """
    下载release包到指定路径
    """
    ret = requests.get(url,stream=True)

    with open(f'{name}.zip','wb') as fd,Progress(
        TextColumn("[progress.description]{task.description}"),
        SpinnerColumn(),
        TimeElapsedColumn(),
    ) as progress:
        task1 = progress.add_task(f"[Download {name}..]")
        for data in ret.iter_content(chunk_size=1024):
            size = fd.write(data)
            progress.update(task1)

with Progress(
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TaskProgressColumn(),
    TimeElapsedColumn(),
) as progress:
    task1 = progress.add_task("Download lib...", total=len(depend_lib))

    for lib_name in depend_lib:
        lib_url = depend_lib[lib_name]["url"]
        download_path = os.path.join('build','lib',lib_name)
        try:
            Repo.clone_from(lib_url,to_path=download_path)
        except GitCommandError:
            pass
        progress.update(task1,advance=1)
