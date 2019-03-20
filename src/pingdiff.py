import argparse
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file',
        help='Ilion CSV file',
        required=True
    )
    args = parser.parse_args()

    # Read CSV file
    df = pd.read_csv(args.file, sep=';')
    df['UTC_DATE'] = pd.to_datetime(df['UTC_DATE'], infer_datetime_format=True)

    # Diff of days    
    diff = (datetime.datetime.utcnow() - df['UTC_DATE']).dt.days

    # Plot
    x = np.array(df['TERMINAL'])
    y = np.array(diff)

    colors = np.random.rand(len(x), 3)
    colors = np.column_stack([colors, np.ones(len(x))])

    plt.bar(x, y, color=colors)
    plt.xlabel('Terminal')
    plt.xticks(rotation=90)
    plt.ylabel('Days')
    plt.title('DAYS SINCE THE LAST PING')
    plt.show()

