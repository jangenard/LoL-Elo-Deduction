from setuptools import setup, find_packages

setup(
    name="rank_deduction",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "opencv-python",
        "matplotlib",
        "setuptools",
        "scikit-learn",
        "easyocr",
        "pandas",
        "torch",
        "xgboost"
    ],
)