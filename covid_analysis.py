{
 "metadata": {
  "kernelspec": {
   "language": "python",
   "display_name": "Python 3",
   "name": "python3"
  },
  "language_info": {
   "pygments_lexer": "ipython3",
   "nbconvert_exporter": "python",
   "version": "3.6.4",
   "file_extension": ".py",
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "name": "python",
   "mimetype": "text/x-python"
  },
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "sourceId": 1602919,
     "sourceType": "datasetVersion",
     "datasetId": 946195
    },
    {
     "sourceId": 1602932,
     "sourceType": "datasetVersion",
     "datasetId": 946204
    }
   ],
   "dockerImageVersionId": 30019,
   "isInternetEnabled": false,
   "language": "python",
   "sourceType": "notebook",
   "isGpuEnabled": false
  }
 },
 "nbformat_minor": 4,
 "nbformat": 4,
 "cells": [
  {
   "cell_type": "code",
   "source": [
    "import pandas as pd \n",
    "import numpy as np \n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt "
   ],
   "metadata": {
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "source": [
    "corona_dataset_csv = pd.read_csv('../input/corona/covid19_Confirmed_dataset.csv')\n",
    "corona_dataset_csv.head(10)"
   ],
   "metadata": {
    "_uuid": "d629ff2d2480ee46fbb7e2d37f6b5fab8052498a",
    "_cell_guid": "79c7e3d0-c299-4dcb-8224-4455121ee9b0",
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "source": [
    "corona_dataset_csv.shape"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Delete the useless columns"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "corona_dataset_csv.drop(['Lat','Long'],axis=1,inplace=True)\n"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "source": [
    "corona_dataset_csv.head(10)"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Aggregating the rows by the country"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "corona_dataset_aggregated = corona_dataset_csv.groupby(\"Country/Region\").sum()"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "source": [
    "corona_dataset_aggregated.head(5)"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "source": [
    "corona_dataset_aggregated.shape"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Visualizing data related to a country for example China, Italy,India"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "corona_dataset_aggregated.loc['China'].plot()\n",
    "corona_dataset_aggregated.loc['Italy'].plot()\n",
    "corona_dataset_aggregated.loc['India'].plot()\n",
    "plt.legend()"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# calculating the first derivative of the curve to find maximum infection rate"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "corona_dataset_aggregated.loc['China'].diff().plot()"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Find maxmimum infection rate for China"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "corona_dataset_aggregated.loc['China'].diff().max()"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Find maximum infection rate for all of the countries."
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "countries = list(corona_dataset_aggregated.index)\n",
    "max_infection_rates = []\n",
    "for country in countries :\n",
    "    max_infection_rates.append(corona_dataset_aggregated.loc[country].diff().max())\n",
    "corona_dataset_aggregated['max infection rate'] = max_infection_rates"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "source": [
    "corona_dataset_aggregated.head()"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# create a new dataframe with only needed columns"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "corona_data = pd.DataFrame(corona_dataset_aggregated['max infection rate'])"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "source": [
    "corona_data.head()"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Importing the WorldHappinessReport.csv dataset"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "world_happiness_report = pd.read_csv(\"../input/happiness/worldwide_happiness_report.csv\")\n",
    "world_happiness_report.head()"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "source": [
    "world_happiness_report.shape"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Dropping useless columns"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "columns_to_dropped = ['Overall rank','Score','Generosity','Perceptions of corruption']\n",
    "world_happiness_report.drop(columns_to_dropped,axis=1 , inplace=True)"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "source": [
    "world_happiness_report.head()"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Changing the indices of the dataframe"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "world_happiness_report.set_index(['Country or region'],inplace=True)\n",
    "world_happiness_report.head()"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# joining the two datasets"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "data = world_happiness_report.join(corona_data).copy()\n",
    "data.head()"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "#  correlation matrix"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "data.corr()\n",
    "# it is representing the currelation between every two columns of our dataset "
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Visualising the results"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "data.head()"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Plotting GDP vs maximum Infection rate"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "x = data['GDP per capita']\n",
    "y = data['max infection rate']\n",
    "sns.scatterplot(x,np.log(y))"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "#Linear Regression b/w the two columns"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "sns.regplot(x,np.log(y))   # regplot is a library to plot linearRegression"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Plotting Social support vs maximum Infection rate"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "x = data['Social support']\n",
    "y = data['max infection rate']\n",
    "sns.scatterplot(x,np.log(y))\n"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "source": [
    "sns.regplot(x,np.log(y))"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "markdown",
   "source": [
    "# Plotting Healthy life expectancy vs maximum Infection rate"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "source": [
    "x = data['Healthy life expectancy']\n",
    "y = data['max infection rate']\n",
    "sns.scatterplot(x,np.log(y))"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  },
  {
   "cell_type": "code",
   "source": [
    "sns.regplot(x,np.log(y))"
   ],
   "metadata": {
    "trusted": true
   },
   "execution_count": null,
   "outputs": []
  }
 ]
}
