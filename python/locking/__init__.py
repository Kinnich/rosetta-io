import pathlib
from contextlib import contextmanager

from ilock import ILock


@contextmanager
def lock_for_early_bird(tmp_dir: pathlib.Path, *lock_keys: [str], worker_id = 'worker'):
    """
    A context manager that either:
    - yields True if you are the "early bird" (the first worker to call this function
    with the tmp_dir and lock_keys you provided)
    - yields False only after the the early bird has finished (i.e. exited the managed context).

    The lock that manages who is and isn't the easly bird:
    - is identified by the `tmp_dir` and the `lock_keys`
    - is created if it doesn't exist
    - is saved as a file in the tmp_dir path

    Use like so:

    lock_for_early_bird(mytmp_dir, testrun_id, 'build-image') as should_build:
      if should_build:
        # ... build the image. Other worker will wait until this is done.
      else:
        # ... image is already built
    """

    lock_id = "once-per-" + "--".join(lock_keys)

    lock_file = tmp_dir / f"{lock_id}.lock"

    is_early_bird = None

    # use a file-based lock to ensure only one worker process is the early bird
    with ILock(lock_id):

        # if this file doesn't exist, that means the caller is the early bird
        is_early_bird = not lock_file.is_file()

        if is_early_bird:
            # create the file so that subsequent workers will see the file and
            # know they aren't the early bird
            lock_file.write_text(f"lock acquired by {worker_id}")

            # yield inside the lock so that other workers have to wait until the
            # early bird is finished
            yield is_early_bird

    if not is_early_bird:
        # yield outside the lock so that other worker's aren't delayed
        yield is_early_bird
