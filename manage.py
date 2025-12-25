#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

# === ADD THIS PATCH AT THE VERY TOP ===
import pkgutil
import sys

# Monkey patch for Python 3.13
if not hasattr(pkgutil, 'ImpImporter'):
    print("🔧 Patching pkgutil.ImpImporter for Python 3.13...")
    class ImpImporter:
        pass
    pkgutil.ImpImporter = ImpImporter

# Also patch setuptools
try:
    from setuptools import _distutils
    if not hasattr(_distutils, 'dist'):
        _distutils.dist = lambda: None
except ImportError:
    pass
# === END PATCH ===

import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()