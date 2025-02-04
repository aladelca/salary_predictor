# Job Salary Prediction App

The **Job Salary Prediction App** is a web application that predicts a job's salary based on its description. Built with Django for the backend, the app leverages scikit-learn for data preprocessing and feature extraction, while using CatBoost as the machine learning model for accurate salary predictions.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Training the Model](#training-the-model)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Features

- **Salary Prediction:** Input a job description and get an estimated salary.
- **User-Friendly Interface:** A simple and clean web interface built with Django.
- **Robust Machine Learning Pipeline:** Uses scikit-learn for preprocessing and CatBoost for modeling, ensuring fast and accurate predictions.
- **Extensible Architecture:** Easy to maintain and extend with additional features or improvements.

---

## Technologies Used

- **Django:** Python web framework for building the backend and serving the application.
- **scikit-learn:** Used for data preprocessing, feature extraction, and building ML pipelines.
- **CatBoost:** A gradient boosting algorithm that powers our salary prediction model.
- **Python:** The core programming language for both the web app and the machine learning components.

---

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- **Python 3.10+**
- **pip** (Python package manager)
- **virtualenv** (recommended for creating an isolated Python environment)
- **Git**

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/aladelca/salary_predictor.git
   cd job-salary-prediction-app
