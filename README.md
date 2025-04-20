# Loan Decision Model

**A Machine Learning-Powered Loan Approval Prediction Application**

![Loan Approval Banner](https://images.unsplash.com/photo-1728044849347-ea6ff59d98dd?q=80&w=2070&auto=format&fit=crop)

## 📌 Overview

The Loan Decision Model is a web-based application designed to predict loan approval outcomes using machine learning algorithms. By analyzing applicant data, the system provides instant decisions, streamlining the loan approval process for financial institutions.

## 🚀 Features

- **Interactive Web Interface**: Built with Streamlit for real-time user interaction.
- **Machine Learning Models**: Utilizes both baseline models and XGBoost classifiers for prediction.
- **Data Preprocessing**: Handles categorical and numerical data efficiently.
- **Logging Mechanism**: Records predictions and inputs for auditing and analysis.
- **User-Friendly Design**: Incorporates a professional UI with a banking-themed background.

## 🧠 Machine Learning Models

The application employs two primary models:

1. **Baseline Model**: A simple classifier serving as a benchmark.
2. **XGBoost Classifier**: An advanced model known for its performance on structured data.

Both models are trained on historical loan data, considering features like income, employment length, loan amount, and more.

## 🖥️ Application Interface

The user interface is crafted for clarity and ease of use:

- **Input Fields**: Users can enter applicant details such as loan amount, interest rate, employment length, etc.
- **Prediction Output**: Displays whether the loan is approved or rejected, along with the probability score.
- **Summary Table**: Provides a recap of the entered information for verification.

## 📂 Project Structure

```
loan-decision-model/
├── app/
│   ├── loan_prediction_app.py      # Main Streamlit app
│   ├── model_baseline.pkl          # saved final model
│   └── output.log                  # Log file
├── data/
│   ├── processed/
│   │   └── loan_data_baseline_ready.csv  # Cleaned dataset used in modeling
│       ├── cleaned_loan_data.csv  # Dataset after data preparation
│   └── raw/
│       └── Loan_status_2007-2020Q3-100ksample.csv  # Raw dataset
├── notebooks/
│   ├── 01_data_preparation_and_EDA.ipynb
│   ├── 02_modeling_baseline.ipynb   #baseline model
│   └── 03-modeling_XGBoost.ipynb    #final XGBoost model
├── reports/
│   ├── loan_approval_architecture.png   #Architecture diagramm
│   └── project_summary.md          # Summary or final report
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Yechyn/loan-decision-model.git
   cd loan-decision-model
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   streamlit run app/loan_prediction_app.py
   ```

   The application will open in your default web browser.

## 📝 Logging

All user inputs and prediction results are logged in the `app/output.log` file. This ensures transparency and aids in monitoring application usage.

## 🛠️ Technologies Used

- **Streamlit**: For building the web interface.
- **XGBoost**: Machine learning model for prediction.
- **Pandas & NumPy**: Data manipulation and analysis.
- **Joblib**: Model serialization.
- **Scikit-learn**: Additional machine learning utilities.

## 📈 Future Enhancements

- **Model Interpretability**: Integrate SHAP or LIME for explaining model decisions.
- **Database Integration**: Store user inputs and predictions in a database.
- **Authentication**: Add user login functionality for secure access.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 📬 Contact

For questions or suggestions, please contact [ser.echin92@gmail.com](mailto:your.email@example.com).

---

*This README was inspired by best practices from [Make a README](https://www.makeareadme.com/).*