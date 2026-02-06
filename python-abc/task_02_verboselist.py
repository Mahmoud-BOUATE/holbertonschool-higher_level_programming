# task_02_verboselist.py
#!/usr/bin/env python3
"""VerboseList module: extends Python list with notifications."""

class VerboseList(list):
    """Custom list that prints notifications on changes."""

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list by appending elements from iterable and print a notification."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove first occurrence of item and print a notification."""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """Remove and return item at index (default last) and print a notification."""
        item = self[index]
        super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
