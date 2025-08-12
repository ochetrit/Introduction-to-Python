from time import sleep
from tqdm import tqdm
import shutil


def progressbar(progress: float, BAR_LENGTH: int) -> str:
    progressbar = ""
    progressbar += int((progress * BAR_LENGTH) / 100) * "█"
    progressbar += int(BAR_LENGTH - ((progress * BAR_LENGTH) / 100)) * " "
    return progressbar


def ft_tqdm(lst: range) -> None:
    """Decorate an iterable object, returning an iterator which acts exactly
like the original iterable, but prints a dynamically updating
progressbar every time a value is requested."""
    size = len(lst) if hasattr(lst, "__len__") else None
    columns = shutil.get_terminal_size().columns
    BAR_LENGTH = columns - 40 if columns > 40 else 50
    if not size:
        print("0it [00:00, ?it/s]")
        return None
    for i, elem in enumerate(lst, 1):
        progress = (i / size) * 100
        print(f"{(i / size) * 100:,.0f}%|{progressbar(progress, BAR_LENGTH)}| {i}/{size}", end = "\r")
        yield elem

