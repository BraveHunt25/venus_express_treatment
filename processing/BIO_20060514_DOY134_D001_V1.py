import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def retrieve_data(file_path:str) -> tuple[list[pd.Timestamp], list[float], list[float], list[float], list[float], list[float], list[float], list[float], list[float], list[float], list[float], list[float], list[float]]:
    r"""
    Retrieve data from a text file.

    :param file_path: Path to the text file containing the data.
    :return: A tuple containing lists of data for each column in the file.
    """
    logging.info(f"Retrieving data from {file_path}")
    with open(file_path, 'r') as file:
        data = file.readlines()

    # Process the data and extract relevant columns
    TIME_UTC = []
    BISX = []
    BISY = []
    BISZ = []
    BIST = []
    BOSX = []
    BOSY = []
    BOSZ = []
    BOST = []
    BIS_BOS_X = []
    BIS_BOS_Y = []
    BIS_BOS_Z = []
    BIS_BOS_T = []

    for line in data[1:]:  # Skip header line
        values = line.strip().split(',')
        logging.debug(f"Processing line: {values}")
        TIME_UTC.append(pd.to_datetime(values[0]))
        BISX.append(float(values[1]))
        BISY.append(float(values[2]))
        BISZ.append(float(values[3]))
        BIST.append(float(values[4]))
        BOSX.append(float(values[5]))
        BOSY.append(float(values[6]))
        BOSZ.append(float(values[7]))
        BOST.append(float(values[8]))
        BIS_BOS_X.append(float(values[9]))
        BIS_BOS_Y.append(float(values[10]))
        BIS_BOS_Z.append(float(values[11]))
        BIS_BOS_T.append(float(values[12]))

    logging.info("Data retrieval complete.")
    return (TIME_UTC,BISX,BISY,BISZ,BIST,BOSX,BOSY,BOSZ,BOST,BIS_BOS_X,BIS_BOS_Y,BIS_BOS_Z,BIS_BOS_T)

def plot_data(TIME_UTC, BISX, BISY, BISZ, BIST, BOSX, BOSY, BOSZ, BOST, BIS_BOS_X, BIS_BOS_Y, BIS_BOS_Z, BIS_BOS_T, output_file:str)->None:
    r"""
    Plot the data and save the figure.

    :param TIME_UTC: List of UTC times.
    :param BISX: List of BISX values.
    :param BISY: List of BISY values.
    :param BISZ: List of BISZ values.
    :param BIST: List of BIST values.
    :param BOSX: List of BOSX values.
    :param BOSY: List of BOSY values.
    :param BOSZ: List of BOSZ values.
    :param BOST: List of BOST values.
    :param BIS_BOS_X: List of BIS_BOS_X values.
    :param BIS_BOS_Y: List of BIS_BOS_Y values.
    :param BIS_BOS_Z: List of BIS_BOS_Z values.
    :param BIS_BOS_T: List of BIS_BOS_T values.
    :param output_file: Path to save the output plot.
    :return: None
    """
    logging.info(f"Plotting data and saving to {output_file}")
    plt.figure(figsize=(100, 100))
    plt.plot(TIME_UTC, BISX, label='BISX', color='red')
    logging.debug(f"BISX data: {BISX[:5]}...")
    plt.plot(TIME_UTC, BISY, label='BISY', color='yellow')
    logging.debug(f"BISY data: {BISY[:5]}...")
    plt.plot(TIME_UTC, BISZ, label='BISZ', color='pink')
    logging.debug(f"BISZ data: {BISZ[:5]}...")
    plt.plot(TIME_UTC, BIST, label='BIST', color='green')
    logging.debug(f"BIST data: {BIST[:5]}...")
    plt.plot(TIME_UTC, BOSX, label='BOSX', color='orange')
    logging.debug(f"BOSX data: {BOSX[:5]}...")
    plt.plot(TIME_UTC, BOSY, label='BOSY', color='purple')
    logging.debug(f"BOSY data: {BOSY[:5]}...")
    plt.plot(TIME_UTC, BOSZ, label='BOSZ', color='blue')
    logging.debug(f"BOSZ data: {BOSZ[:5]}...")
    plt.plot(TIME_UTC, BOST, label='BOST', color='cyan')
    logging.debug(f"BOST data: {BOST[:5]}...")
    plt.plot(TIME_UTC, BIS_BOS_X, label='BIS_BOS_X', color='magenta')
    logging.debug(f"BIS_BOS_X data: {BIS_BOS_X[:5]}...")
    plt.plot(TIME_UTC, BIS_BOS_Y, label='BIS_BOS_Y', color='gray')
    logging.debug(f"BIS_BOS_Y data: {BIS_BOS_Y[:5]}...")
    plt.plot(TIME_UTC, BIS_BOS_Z, label='BIS_BOS_Z', color='black')
    logging.debug(f"BIS_BOS_Z data: {BIS_BOS_Z[:5]}...")
    plt.plot(TIME_UTC, BIS_BOS_T, label='BIS_BOS_T', color='lime')
    logging.debug(f"BIS_BOS_T data: {BIS_BOS_T[:5]}...")
    
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.xlabel('Time (UTC)')
    plt.ylabel('Magnetic Field (nT)')
    plt.title('BIS Magnetic Field Components')
    
    plt.legend()
    
    plt.savefig(output_file)
    plt.close()

def plot_differences(TIME_UTC, BIS_BOS_X, BIS_BOS_Y, BIS_BOS_Z, BIS_BOS_T, output_file:str)->None:
    r"""
    Plot the differences between BIS and BOS magnetic field components.
    :param TIME_UTC: List of UTC times.
    :param BIS_BOS_X: List of differences in X component.
    :param BIS_BOS_Y: List of differences in Y component.
    :param BIS_BOS_Z: List of differences in Z component.
    :param BIS_BOS_T: List of differences in T component.
    :param output_file: Path to save the output plot.
    :return: None
    """
    logging.info(f"Plotting differences and saving to {output_file}")
    plt.figure(figsize=(100, 100))
    plt.plot(TIME_UTC, BIS_BOS_X, label='BIS_BOS_X', color='red')
    logging.debug(f"BIS_BOS_X data: {BIS_BOS_X[:5]}...")
    plt.plot(TIME_UTC, BIS_BOS_Y, label='BIS_BOS_Y', color='yellow')
    logging.debug(f"BIS_BOS_Y data: {BIS_BOS_Y[:5]}...")
    plt.plot(TIME_UTC, BIS_BOS_Z, label='BIS_BOS_Z', color='blue')
    logging.debug(f"BIS_BOS_Z data: {BIS_BOS_Z[:5]}...")
    plt.plot(TIME_UTC, BIS_BOS_T, label='BIS_BOS_T', color='black')
    logging.debug(f"BIS_BOS_T data: {BIS_BOS_T[:5]}...")

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.xlabel('Time (UTC)')
    plt.ylabel('Magnetic Field (nT)')
    plt.title('BIS-BOS Magnetic Field Differences')

    plt.legend()

    plt.savefig(output_file)
    plt.close()

def main():
    file_path = 'data/content/BIO_20060514_DOY134_D001_V1.csv'
    output_file = 'data/assets/BIO_20060514_DOY134_D001_V1.png'

    TIME_UTC, BISX, BISY, BISZ, BIST, BOSX, BOSY, BOSZ, BOST, BIS_BOS_X, BIS_BOS_Y, BIS_BOS_Z, BIS_BOS_T = retrieve_data(file_path)

    plot_data(TIME_UTC, BISX, BISY, BISZ, BIST, BOSX, BOSY, BOSZ, BOST, BIS_BOS_X, BIS_BOS_Y, BIS_BOS_Z, BIS_BOS_T, output_file)
    plot_differences(TIME_UTC, BIS_BOS_X, BIS_BOS_Y, BIS_BOS_Z, BIS_BOS_T, 'data/assets/BIO_20060514_DOY134_D001_V1_differences.png')
    logging.info("Plots generated successfully.")

if __name__ == "__main__":
    logging.info("Starting data processing...")
    main()
    logging.info("Processing complete.")