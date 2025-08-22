import pandas as pd
import matplotlib.pyplot as plt
import os

def create_weather_chart(csv_filepath):
    """
    Reads weather data from a CSV file, creates a temperature trend chart,
    and saves it as an image.
    
    Args:
        csv_filepath (str): The full path to the input CSV file.
    """
    # --- 1. Load the dataset using pandas ---
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_filepath)
        print("CSV file loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{csv_filepath}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # --- 2. Data Validation and Preparation ---
    # Check if required columns exist
    if 'Date' not in df.columns or 'Temperature' not in df.columns:
        print("Error: CSV file must contain 'Date' and 'Temperature' columns.")
        return

    # Convert 'Date' column to datetime objects for proper plotting
    # The 'errors='coerce'' will turn any unparseable dates into NaT (Not a Time)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Remove rows with invalid dates or temperatures
    df.dropna(subset=['Date', 'Temperature'], inplace=True)
    
    # Sort data by date to ensure the line chart connects points in chronological order
    df = df.sort_values(by='Date')

    if df.empty:
        print("No valid data to plot after cleaning. Please check your CSV file.")
        return

    # --- 3. Create the Line Chart ---
    print("Generating the temperature trend chart...")
    plt.figure(figsize=(12, 7)) # Set the figure size for better readability

    # Plot the data: Date on X-axis, Temperature on Y-axis
    plt.plot(df['Date'], df['Temperature'], marker='o', linestyle='-', color='b', label='Daily Temperature')

    # --- 4. Customize the Chart ---
    plt.title('Daily Temperature Trends', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.grid(True) # Add a grid for better readability of values
    plt.legend()
    
    # Improve date formatting on the x-axis
    plt.gcf().autofmt_xdate() # Auto-formats the x-axis labels (e.g., rotates them)

    # --- 5. Save the Chart as an Image File ---
    output_filename = 'temperature_trends.png'
    try:
        plt.savefig(output_filename)
        print(f"Chart successfully saved as '{output_filename}'")
    except Exception as e:
        print(f"Error saving chart: {e}")
        return

    # --- 6. Display the Chart ---
    plt.show()


def main():
    """
    Main function to run the weather visualizer program.
    """
    print("--- Weather Trends Visualizer ---")
    
    # --- Prompt user for file input ---
    while True:
        csv_path = input("Please enter the path to the weather CSV file: ")
        
        # Check if the file exists
        if os.path.exists(csv_path):
            create_weather_chart(csv_path)
            break
        else:
            print("File not found. Please provide a valid file path.")

if __name__ == "__main__":
    main()
