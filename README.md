# Medical Deep Learning Classifiers

> Applying Advanced Deep Learning Architectures for Medical Diagnostics and Patient Assessment.

This repository contains the implementation of two distinct deep learning research tasks:
1. **Pain Level Assessment**: Utilizing sequential data processed through a **BiLSTM** (Bidirectional Long Short-Term Memory) network to evaluate patient pain levels.
2. **Breast Cancer Subtype Classification**: A **CNN** (Convolutional Neural Network) approach utilizing image patching, morphological masks, and Multiple Instance Learning (MIL) to classify breast cancer histopathology/imaging.

## 🧠 Project Architecture

### 1. Pain Level Assessment (BiLSTM)
*   **Objective**: Automate the assessment of patient pain levels based on sequential time-series/clinical data.
*   **Model**: BiLSTM network, capable of capturing backward and forward temporal dependencies.
*   **Key Techniques**: Sequence padding, temporal feature extraction, and optimized recurrent dropout to prevent overfitting.

### 2. Breast Cancer Subtype Classification (CNN)
*   **Objective**: Classify breast cancer subtypes with high precision.
*   **Model**: Deep Convolutional Neural Network (CNN).
*   **Key Techniques**: 
    *   **Patch-based processing**: Handling large resolution medical images via smart patching (`Patching_Smart`).
    *   **Transfer Learning**: Leveraging pre-trained weights for feature extraction.
    *   **Multiple Instance Learning (MIL)**: Aggregating patch-level predictions for slide-level diagnosis.
    *   **Snapshot Ensembling**: Improving generalization through cyclical learning rate schedules.

## 📂 Repository Structure

The project emphasizes a clean separation of concerns, maintaining modularity for both data processing and model training.

- `pain_level_bilstm/`: Source code, notebooks, and models specific to the sequence-based pain assessment task.
    - Main entry point: `notebooks/BiLSTM_Pain_Assessment.ipynb`
- `breast_cancer_cnn/`: Source code, notebooks, and models for image-based cancer subtype classification.
    - Main entry point: `CNN_Cancer_Classification.ipynb`
    - Earlier work and tests: `experiments/` directory
- `shared/`: Utilities and generic preprocessing scripts shared across both environments.

## ⚙️ Setup & Installation

Ensure you have Python 3.8+ installed. It is recommended to use a virtual environment.

```bash
# Clone the repository
git clone https://github.com/your-username/Medical-DL-Classifiers.git
cd Medical-DL-Classifiers

# Create and activate a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## 🚀 How to Run

*Note: For privacy and licensing reasons, the raw medical datasets are not included in this repository.

### Model Training and Inference
Instead of a standalone python script, both tasks currently rely on Jupyter Notebooks as their primary entry points.

- **Pain Level Assessment:**
  Open and run `pain_level_bilstm/notebooks/01_BiLSTM_Pain_Assessment.ipynb`.

- **Breast Cancer Subtype Classification:**
  Open and run `breast_cancer_cnn/CNN_Cancer_Classification.ipynb`. This notebook contains the overarching logic for patching, Convolutional Neural Network definition, and Snapshot Ensembling training.

All legacy tests and iteration steps for the CNN task can be explored inside `breast_cancer_cnn/experiments/`.

