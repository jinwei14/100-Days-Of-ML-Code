{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['France' 44.0 72000.0]\n",
      " ['Spain' 27.0 48000.0]\n",
      " ['Germany' 30.0 54000.0]\n",
      " ['Spain' 38.0 61000.0]\n",
      " ['Germany' 40.0 nan]\n",
      " ['France' 35.0 58000.0]\n",
      " ['Spain' nan 52000.0]\n",
      " ['France' 48.0 79000.0]\n",
      " ['Germany' 50.0 83000.0]\n",
      " ['France' 37.0 67000.0]]\n",
      "['No' 'Yes' 'No' 'No' 'Yes' 'Yes' 'No' 'Yes' 'No' 'Yes']\n"
     ]
    }
   ],
   "source": [
    "dataset = pd.read_csv('../../../datasets/Data.csv')\n",
    "X = dataset.iloc[ : , :-1].values\n",
    "Y = dataset.iloc[ : , 3].values\n",
    "print(X)\n",
    "\n",
    "print(Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['France' 44.0 72000.0]\n",
      " ['Spain' 27.0 48000.0]\n",
      " ['Germany' 30.0 54000.0]\n",
      " ['Spain' 38.0 61000.0]\n",
      " ['Germany' 40.0 63777.77777777778]\n",
      " ['France' 35.0 58000.0]\n",
      " ['Spain' 38.77777777777778 52000.0]\n",
      " ['France' 48.0 79000.0]\n",
      " ['Germany' 50.0 83000.0]\n",
      " ['France' 37.0 67000.0]]\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/jinweizhang/opt/anaconda3/lib/python3.7/site-packages/sklearn/utils/deprecation.py:66: DeprecationWarning: Class Imputer is deprecated; Imputer was deprecated in version 0.20 and will be removed in 0.22. Import impute.SimpleImputer from sklearn instead.\n",
      "  warnings.warn(msg, category=DeprecationWarning)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.preprocessing import Imputer\n",
    "imputer = Imputer(missing_values = \"NaN\", strategy = \"mean\", axis = 0)\n",
    "imputer = imputer.fit(X[ : , 1:3])\n",
    "X[ : , 1:3] = imputer.transform(X[ : , 1:3])\n",
    "print(X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 44.0 72000.0]\n",
      " [2 27.0 48000.0]\n",
      " [1 30.0 54000.0]\n",
      " [2 38.0 61000.0]\n",
      " [1 40.0 63777.77777777778]\n",
      " [0 35.0 58000.0]\n",
      " [2 38.77777777777778 52000.0]\n",
      " [0 48.0 79000.0]\n",
      " [1 50.0 83000.0]\n",
      " [0 37.0 67000.0]]\n"
     ]
    }
   ],
   "source": [
    "from sklearn.preprocessing import LabelEncoder, OneHotEncoder\n",
    "labelencoder_X = LabelEncoder()\n",
    "X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])\n",
    "print(X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.00000000e+00 1.00000000e+00 0.00000000e+00 0.00000000e+00\n",
      "  4.40000000e+01 7.20000000e+04]\n",
      " [1.00000000e+00 0.00000000e+00 0.00000000e+00 1.00000000e+00\n",
      "  2.70000000e+01 4.80000000e+04]\n",
      " [1.00000000e+00 0.00000000e+00 1.00000000e+00 0.00000000e+00\n",
      "  3.00000000e+01 5.40000000e+04]\n",
      " [1.00000000e+00 0.00000000e+00 0.00000000e+00 1.00000000e+00\n",
      "  3.80000000e+01 6.10000000e+04]\n",
      " [1.00000000e+00 0.00000000e+00 1.00000000e+00 0.00000000e+00\n",
      "  4.00000000e+01 6.37777778e+04]\n",
      " [0.00000000e+00 1.00000000e+00 0.00000000e+00 0.00000000e+00\n",
      "  3.50000000e+01 5.80000000e+04]\n",
      " [1.00000000e+00 0.00000000e+00 0.00000000e+00 1.00000000e+00\n",
      "  3.87777778e+01 5.20000000e+04]\n",
      " [0.00000000e+00 1.00000000e+00 0.00000000e+00 0.00000000e+00\n",
      "  4.80000000e+01 7.90000000e+04]\n",
      " [1.00000000e+00 0.00000000e+00 1.00000000e+00 0.00000000e+00\n",
      "  5.00000000e+01 8.30000000e+04]\n",
      " [0.00000000e+00 1.00000000e+00 0.00000000e+00 0.00000000e+00\n",
      "  3.70000000e+01 6.70000000e+04]]\n",
      "(10, 6)\n",
      "[0 1 0 0 1 1 0 1 0 1]\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/jinweizhang/opt/anaconda3/lib/python3.7/site-packages/sklearn/preprocessing/_encoders.py:415: FutureWarning: The handling of integer data will change in version 0.22. Currently, the categories are determined based on the range [0, max(values)], while in the future they will be determined based on the unique values.\n",
      "If you want the future behaviour and silence this warning, you can specify \"categories='auto'\".\n",
      "In case you used a LabelEncoder before this OneHotEncoder to convert the categories to integers, then you can now use the OneHotEncoder directly.\n",
      "  warnings.warn(msg, FutureWarning)\n",
      "/Users/jinweizhang/opt/anaconda3/lib/python3.7/site-packages/sklearn/preprocessing/_encoders.py:451: DeprecationWarning: The 'categorical_features' keyword is deprecated in version 0.20 and will be removed in 0.22. You can use the ColumnTransformer instead.\n",
      "  \"use the ColumnTransformer instead.\", DeprecationWarning)\n"
     ]
    }
   ],
   "source": [
    "onehotencoder = OneHotEncoder(categorical_features = [0])\n",
    "X = onehotencoder.fit_transform(X).toarray()\n",
    "labelencoder_Y = LabelEncoder()\n",
    "Y =  labelencoder_Y.fit_transform(Y)\n",
    "print(X)\n",
    "print(X.shape)\n",
    "print(Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.00000000e+00 1.00000000e+00 0.00000000e+00 0.00000000e+00\n",
      "  4.40000000e+01 7.20000000e+04]\n",
      " [1.00000000e+00 0.00000000e+00 0.00000000e+00 1.00000000e+00\n",
      "  2.70000000e+01 4.80000000e+04]\n",
      " [1.00000000e+00 0.00000000e+00 1.00000000e+00 0.00000000e+00\n",
      "  3.00000000e+01 5.40000000e+04]\n",
      " [1.00000000e+00 0.00000000e+00 0.00000000e+00 1.00000000e+00\n",
      "  3.80000000e+01 6.10000000e+04]\n",
      " [1.00000000e+00 0.00000000e+00 1.00000000e+00 0.00000000e+00\n",
      "  4.00000000e+01 6.37777778e+04]\n",
      " [0.00000000e+00 1.00000000e+00 0.00000000e+00 0.00000000e+00\n",
      "  3.50000000e+01 5.80000000e+04]\n",
      " [1.00000000e+00 0.00000000e+00 0.00000000e+00 1.00000000e+00\n",
      "  3.87777778e+01 5.20000000e+04]\n",
      " [0.00000000e+00 1.00000000e+00 0.00000000e+00 0.00000000e+00\n",
      "  4.80000000e+01 7.90000000e+04]\n",
      " [1.00000000e+00 0.00000000e+00 1.00000000e+00 0.00000000e+00\n",
      "  5.00000000e+01 8.30000000e+04]\n",
      " [0.00000000e+00 1.00000000e+00 0.00000000e+00 0.00000000e+00\n",
      "  3.70000000e+01 6.70000000e+04]]\n",
      "(10, 6)\n",
      "(8, 6)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size = 0.2, random_state = 0)\n",
    "print(X)\n",
    "print(X.shape)\n",
    "print(X_train.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1.         -1.          2.64575131 -0.77459667  0.26306757  0.12381479]\n",
      " [-1.          1.         -0.37796447 -0.77459667 -0.25350148  0.46175632]\n",
      " [ 1.         -1.         -0.37796447  1.29099445 -1.97539832 -1.53093341]\n",
      " [ 1.         -1.         -0.37796447  1.29099445  0.05261351 -1.11141978]\n",
      " [-1.          1.         -0.37796447 -0.77459667  1.64058505  1.7202972 ]\n",
      " [ 1.         -1.         -0.37796447  1.29099445 -0.0813118  -0.16751412]\n",
      " [-1.          1.         -0.37796447 -0.77459667  0.95182631  0.98614835]\n",
      " [-1.          1.         -0.37796447 -0.77459667 -0.59788085 -0.48214934]]\n",
      "(8, 6)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "sc_X = StandardScaler()\n",
    "X_train = sc_X.fit_transform(X_train)\n",
    "X_test = sc_X.fit_transform(X_test)\n",
    "\n",
    "print(X_train)\n",
    "print(X_train.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "StandardScaler(copy=True, with_mean=True, with_std=True)\n",
      "[0.5 0.5]\n",
      "[0.25 0.25]\n",
      "[[-1. -1.]\n",
      " [-1. -1.]\n",
      " [ 1.  1.]\n",
      " [ 1.  1.]]\n",
      "[[3. 3.]]\n"
     ]
    }
   ],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "data = [[0, 0], [0, 0], [1, 1], [1, 1]]\n",
    "scaler = StandardScaler()\n",
    "print(scaler.fit(data))\n",
    "print(scaler.mean_)\n",
    "print(scaler.var_)\n",
    "print(scaler.transform(data))\n",
    "print(scaler.transform([[2, 2]]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
