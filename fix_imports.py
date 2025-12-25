import pkgutil
import sys

# Monkey patch for Python 3.13
if not hasattr(pkgutil, 'ImpImporter'):
    print("Patching pkgutil.ImpImporter for Python 3.13...")
    class ImpImporter:
        pass
    pkgutil.ImpImporter = ImpImporter

# Also patch setuptools if needed
try:
    from setuptools import _distutils
    if not hasattr(_distutils, 'dist'):
        _distutils.dist = lambda: None
except:
    pass

print("✅ Patched for Python 3.13 compatibility")
