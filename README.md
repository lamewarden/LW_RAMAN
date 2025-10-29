# LW_RAMAN - Lamewarden Raman Spectroscopy Tools

A comprehensive Python package for Raman spectroscopy analysis and processing.

## Features

### Calibration Tools
- **xcalib**: X-axis calibration tools for Raman spectra using polynomial regression and machine learning models

### Preprocessing Tools
- **despiking**: Remove cosmic ray spikes from Raman spectra
- **normalize**: Normalization utilities for Raman spectral data
- **background_subtraction**: Advanced background subtraction methods including ASLS algorithm
- **baseline_correction**: Baseline correction utilities for improved spectral analysis

## Installation

### From GitHub
```bash
pip install git+https://github.com/lamewarden/LW_RAMAN.git
```

### For development
```bash
git clone https://github.com/lamewarden/LW_RAMAN.git
cd LW_RAMAN
pip install -e .[dev]
```

## Quick Start

### Calibration
```python
from lw_raman.calibration import xcalib

# Calibrate Raman spectrum
calibrator = xcalib.RamanCalibrator()
calibrated_spectrum = calibrator.calibrate(raw_spectrum, reference_peaks)
```

### Preprocessing
```python
from lw_raman.preprocessing import despiking, normalize

# Remove cosmic ray spikes
cleaned_spectrum = despiking.despike(raw_spectrum)

# Normalize spectrum
normalized_spectrum = normalize.normalize_spectrum(cleaned_spectrum)
```

### Background Subtraction
```python
from lw_raman.preprocessing import background_subtraction

# Apply ASLS background subtraction
corrected_spectrum = background_subtraction.asls_baseline(spectrum)
```

## Command Line Tools

The package includes several command-line utilities:

- `raman-calibrate`: Calibrate Raman spectra
- `raman-despike`: Remove cosmic ray spikes
- `raman-normalize`: Normalize Raman spectra

## Requirements

- Python >= 3.8
- NumPy >= 1.20.0
- pandas >= 1.3.0
- SciPy >= 1.7.0
- scikit-learn >= 1.0.0
- matplotlib >= 3.4.0
- nptyping >= 2.0.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## Authors

- **Lamewarden Team** - *Initial work*

## Acknowledgments

- Built for advanced Raman spectroscopy analysis
- Designed for scientific research and analytical chemistry applications