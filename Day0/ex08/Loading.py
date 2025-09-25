import os


def ft_tqdm(lst: range) -> None:
    """
    A simple implementation of a progress bar similar to tqdm.
    Using yield to create a generator that yields items from the input list.
    """
    try:
        width = os.get_terminal_size().columns - 30
        total = len(lst)
        for i, item in enumerate(lst):
            percent = (i + 1) / len(lst)
            bar_length = int((width - 10) * percent)
            bar = '█' * bar_length + ' ' * (width - 10 - bar_length)
            print(f"\r{percent:.0%}|{bar}|", end=' ', flush=True)
            print(f"{i + 1}/{total}", end='', flush=True)
            yield item
    except OSError as e:
        print("Terminal size error:", e)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except ValueError as e:
        print("Value error:", e)
    except Exception as e:
        print("Error:", e)
