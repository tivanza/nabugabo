#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web1.settings")

    from django.core.management import execute_from_command_line

=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dJangoTamgo1.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
>>>>>>> b88def802edd1ea7d854bc1bad5315ba45b157a9
    execute_from_command_line(sys.argv)
