import os


def ensure_dir(path):
    """Create directory if it does not exist."""
    os.makedirs(path, exist_ok=True)


def list_files(directory, extension=None):
    """List files in a directory, optionally filtered by extension."""
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory does not exist: {directory}")

    files = os.listdir(directory)
    if extension:
        if not extension.startswith("."):
            extension = f".{extension}"
        files = [f for f in files if f.endswith(extension)]
    return sorted(files)
