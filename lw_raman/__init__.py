"""
LW_RAMAN - Lamewarden Raman Spectroscopy Tools

A comprehensive Python package for Raman spectroscopy analysis and processing.
"""

__version__ = "0.1.0"
__author__ = "Lamewarden Team"
__email__ = "lamewarden@example.com"

# Import main modules for easy access
try:
    from . import calibration
    from . import preprocessing
except ImportError as e:
    # Handle cases where optional dependencies might not be installed
    import warnings
    warnings.warn(f"Some modules could not be imported: {e}")

__all__ = [
    "calibration",
    "preprocessing",
]
