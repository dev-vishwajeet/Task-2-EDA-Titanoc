# Task 2: Exploratory Data Analysis (EDA) on Titanic Dataset

##  Objective
The objective of this task is to perform Exploratory Data Analysis (EDA) on the cleaned Titanic dataset. EDA helps in understanding the structure of the dataset, identifying patterns, analyzing feature distributions, detecting outliers, and exploring relationships between variables through visualizations.

##  Tools and Libraries Used
* **Python**
* **Pandas**
* **Matplotlib**
* **Seaborn**

## Dataset
The analysis was performed on the cleaned Titanic dataset:
* `cleaned_titanic.csv`

## ⚙️ Steps Performed

### 1. Dataset Exploration
The following dataset information was examined:
* First 5 rows of the dataset
* Dataset structure and data types
* Summary statistics
* Missing values check

### 2. Numerical Data Analysis
Numerical columns were selected for analysis (excluding `PassengerId`). The following visualizations were created:
* **Histograms:** Used to analyze the distribution of numerical features.
* **Boxplots:** Used to identify the spread of data and detect potential outliers.

### 3. Categorical Data Analysis
The following count plots were generated:
* Overall Survival Count
* Survival by Gender
* Survival by Passenger Class

### 4. Correlation Analysis
A correlation heatmap was generated to examine relationships between numerical features.

### 5. Pairplot Analysis
A pairplot was created to visualize pairwise relationships among numerical variables.

##  Output
All generated visualizations are automatically saved in the `screenshots` folder. Examples include:
* `countplot_survived.png`
* `countplot_survived_sex.png`
* `countplot_survived_pclass.png`
* `histogram_Age.png`
* `histogram_Fare.png`
* `boxplot_Age.png`
* `boxplot_Fare.png`
* `correlation_heatmap.png`
* `pairplot.png`

##  Conclusion
Exploratory Data Analysis was successfully performed on the cleaned Titanic dataset using statistical summaries and visualizations. The generated plots help in understanding feature distributions, categorical relationships, outliers, and correlations within the dataset.
