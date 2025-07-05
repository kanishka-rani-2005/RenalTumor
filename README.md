# RenalTumor


This project is an end-to-end Machine Learning application designed to classify kidney images into three categories: **Cyst**, **Normal**, and **Tumor**. The entire workflow is version-controlled and reproducible using DVC, and the final model is served via a web interface within a Docker container.

## 🖼️ Demonstration

The model is trained to classify images like the ones below. The web application provides an interface to upload an image and receive a prediction.


| Cyst | Normal | Tumor |
|:----:|:------:|:-----:|

| <img src="DemoImages/Cyst.png" alt="Cyst Example" width="220"> | <img src="DemoImages/Normal.png" alt="Normal Example" width="220"> | <img src="DemoImages/Tumor.png" alt="Tumor Example" width="220"> |



## ✨ Features

- **End-to-End MLOps Workflow**: From data ingestion to model deployment.
- **Data & Model Versioning**: Using **DVC** to ensure reproducibility and track datasets and models.
- **Web Interface**: A user-friendly web app built with **Flask** to interact with the trained model.
- **Containerized Application**: **Dockerized** for easy deployment and scalability.
- **Structured & Modular Code**: Follows industry best practices for clean and maintainable code.




## ⚙️ Tech Stack

- **Backend**: Python, Flask
- **ML/DL Framework**: TensorFlow, Keras
- **MLOps Tools**: DVC (Data Version Control)
- **Deployment**: Docker
- **Frontend**: HTML, CSS, JavaScript



## 📁 Project Structure

The project follows a modular structure to separate concerns:

├── .dvc/ # DVC files, not to be modified manually

├── artifacts/ # Stores all pipeline outputs (data, models, etc.)

├── config/ # Configuration files

├── DemoImages/ # Sample images for demonstration

├── logs/ # Application and pipeline logs

├── research/ # Jupyter notebooks for experimentation

├── src/ # Main source code for the application

├── templates/ # HTML templates for the web application

├── venv/ # Python virtual environment

├── .dvcignore # Files/directories for DVC to ignore

├── app.py # Main entry point for the Flask web application

├── Dockerfile # Instructions to build the Docker image

├── dvc.yaml # Defines the DVC pipeline stages

├── main.py # Main script to trigger the training pipeline

├── params.yaml # Parameters for models and data processing

├── requirements.txt # Python dependencies

├── setup.py # Project setup script



## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- [Git](https://git-scm.com/)
- [Python 3.8+](https://www.python.org/)
- [DVC](https://dvc.org/doc/install)
- [Docker](https://www.docker.com/get-started) (Optional, for containerized deployment)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Pull the data and model using DVC:**
    *This command fetches the version-controlled data and pre-trained models from remote storage (e.g., S3, GCS).*
    ```bash
    dvc pull
    ```

## 🔧 How to Run

### 1. Run the DVC Pipeline

To reproduce the training pipeline (data ingestion, preprocessing, training, and evaluation), run:
```bash
dvc repro


To start the Flask server and interact with the model:

```bash
python app.py


The application will be accessible at http://localhost:8080.




