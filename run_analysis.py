"""Telco customer churn analysis.

This script keeps the project intentionally compact: clean the public Telco
dataset, create a few EDA charts, calculate interpretable odds ratios and
compare two baseline churn models.

Run:
    python run_analysis.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (RocCurveDisplay, classification_report,
                             roc_auc_score)
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA = Path("data/Telco-Customer-Churn.csv")
OUTPUT_DIR = Path("outputs")
BOOTSTRAP_ROUNDS = 50


# ----------------------------------------------------------------- prepare

def load_and_clean() -> pd.DataFrame:
    """Load the dataset and apply the minimum cleaning needed for modelling."""
    df = pd.read_csv(DATA)

    # TotalCharges comes as text because a few new customers have blank values.
    # For zero-tenure customers, treating the missing total charge as 0 is more
    # useful than dropping the rows.
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    df["Churn"] = (df["Churn"] == "Yes").astype(int)
    return df.drop(columns=["customerID"])


# --------------------------------------------------------------------- EDA

def eda_figures(df: pd.DataFrame) -> None:
    """Create a quick visual overview for the most useful churn signals."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    rate = df.groupby("Contract")["Churn"].mean().sort_values(ascending=False)
    rate.plot.bar(ax=axes[0], color="#c0392b", rot=0)
    axes[0].set_title("Churn rate by contract type")
    axes[0].set_ylabel("Churn rate")

    df[df.Churn == 0]["tenure"].plot.hist(ax=axes[1], bins=30, alpha=0.6,
                                          label="Stayed", color="#2c7fb8")
    df[df.Churn == 1]["tenure"].plot.hist(ax=axes[1], bins=30, alpha=0.6,
                                          label="Churned", color="#c0392b")
    axes[1].set_title("Tenure distribution by churn")
    axes[1].set_xlabel("Tenure (months)")
    axes[1].legend()

    rate2 = df.groupby("InternetService")["Churn"].mean().sort_values(ascending=False)
    rate2.plot.bar(ax=axes[2], color="#e67e22", rot=0)
    axes[2].set_title("Churn rate by internet service")

    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "eda_overview.png", dpi=150)


# ------------------------------------------------------------- statistical

def logistic_odds_ratios(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate odds ratios from logistic regression.

    I use this model mainly for interpretation. The predictive score is not the
    only thing that matters in churn projects; business teams also need to see
    which factors move the risk up or down.
    """
    y = df["Churn"].to_numpy()
    X = df.drop(columns="Churn")
    cat = X.select_dtypes(exclude="number").columns.tolist()
    num = X.select_dtypes("number").columns.tolist()

    pre = ColumnTransformer([
        ("num", StandardScaler(), num),
        ("cat", OneHotEncoder(drop="first", sparse_output=False), cat),
    ])
    Xt = pre.fit_transform(X)
    names = pre.get_feature_names_out()

    lr = LogisticRegression(max_iter=1000, C=1.0, solver="liblinear")
    lr.fit(Xt, y)

    # Bootstrap confidence intervals give a quick stability check for each
    # coefficient without turning this into a long statistical notebook.
    rng = np.random.default_rng(0)
    boots = []
    for _ in range(BOOTSTRAP_ROUNDS):
        idx = rng.integers(0, len(y), len(y))
        b = LogisticRegression(max_iter=1000, C=1.0, solver="liblinear").fit(Xt[idx], y[idx])
        boots.append(b.coef_[0])
    lo, hi = np.percentile(boots, [2.5, 97.5], axis=0)

    table = pd.DataFrame({
        "odds_ratio": np.exp(lr.coef_[0]),
        "ci_low": np.exp(lo),
        "ci_high": np.exp(hi),
    }, index=names)
    table["significant"] = (table.ci_low > 1) | (table.ci_high < 1)
    return table.sort_values("odds_ratio", ascending=False).round(3)


# --------------------------------------------------------------- predictive

def predictive_models(df: pd.DataFrame) -> pd.DataFrame:
    y = df["Churn"].to_numpy()
    X = df.drop(columns="Churn")
    cat = X.select_dtypes(exclude="number").columns.tolist()
    num = X.select_dtypes("number").columns.tolist()
    pre = ColumnTransformer([
        ("num", StandardScaler(), num),
        ("cat", OneHotEncoder(drop="first", sparse_output=False), cat),
    ])

    models = {
        # Logistic regression is the baseline I would show first because it is
        # easy to explain. Gradient boosting is added as a stronger comparison.
        "LogisticRegression": LogisticRegression(max_iter=1000, solver="liblinear"),
        "GradientBoosting": GradientBoostingClassifier(
            random_state=0, n_estimators=60, max_depth=2
        ),
    }
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=42)

    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    results = {}
    for name, clf in models.items():
        pipe = Pipeline([("pre", pre), ("clf", clf)])
        cv_auc = cross_val_score(pipe, X_tr, y_tr, cv=5, scoring="roc_auc")
        pipe.fit(X_tr, y_tr)
        proba = pipe.predict_proba(X_te)[:, 1]
        results[name] = {
            "cv_auc_mean": cv_auc.mean(), "cv_auc_sd": cv_auc.std(),
            "test_auc": roc_auc_score(y_te, proba),
        }
        RocCurveDisplay.from_predictions(y_te, proba, name=name, ax=ax)
        print(f"\n=== {name} (test set) ===")
        print(classification_report(y_te, (proba >= 0.5).astype(int), digits=3))

    ax.plot([0, 1], [0, 1], "k--", alpha=0.4)
    ax.set_title("ROC curves — churn prediction")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "roc_curves.png", dpi=150)
    return pd.DataFrame(results).T.round(3)


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    df = load_and_clean()
    print(f"Dataset: {df.shape[0]} customers, churn rate = {df.Churn.mean():.1%}")

    eda_figures(df)

    odds = logistic_odds_ratios(df)
    odds.to_csv(OUTPUT_DIR / "odds_ratios.csv")
    print("\n=== Top churn drivers (odds ratios, 95% bootstrap CI) ===")
    print(odds.head(8).to_string())
    print("\n=== Strongest protective factors ===")
    print(odds.tail(5).to_string())

    summary = predictive_models(df)
    summary.to_csv(OUTPUT_DIR / "model_comparison.csv")
    print("\n=== Model comparison ===")
    print(summary.to_string())
    print("\nOutputs written to outputs/")


if __name__ == "__main__":
    main()
