import sys


def clean_weather_data(input_file, output_file):
    try:
        with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
            f_out.write("Day, Temperature, Status\n")
            line_count = 0

            for line in f_in:
                clean_line = line.strip()

                if not clean_line:
                    continue
                try:
                    temp = float(clean_line)

                    if -50 <= temp <= 50:
                        line_count += 1
                        f_out.write(f"{line_count}, {temp}, Valid\n")
                    else:
                        line_count += 1
                        f_out.write(f"{line_count}, {temp}, Outlier\n")
                except ValueError:
                    line_count += 1
                    f_out.write(f"{line_count}, {clean_line}, Invalid string\n")

            print(f"Cleaned weather data saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def weather_analysis(clean_data):
    try:
        with open(clean_data, "r") as file:
            next(file, None)
            temps = []
            errors = 0
            for line in file:
                if "Valid" in line:
                    temp = float(line.split(",")[1].strip())
                    temps.append(temp)
                else:
                    errors += 1
                    continue

        if temps:
            min_temps = min(temps)
            max_temps = max(temps)
            avg_temps = sum(temps) / len(temps)
            range_temps = max_temps - min_temps

            print("\n ---------- Weather Analysis ----------")
            print(f"Minimum Temperature: {min_temps}°C")
            print(f"Maximum Temperature: {max_temps}°C")
            print(f"Average Temperature: {avg_temps:.2f}°C")
            print(f"Temperature Range: {range_temps}°C")
            print(f"Number of Errors: {errors}")
        else:
            print("No valid temperature data to analyze.")
    except FileNotFoundError:
        print(f"Error: The file '{clean_data}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        clean_weather_data(sys.argv[1], "cleaned_data.csv")
        weather_analysis("cleaned_data.csv")
    else:
        print("Usage: python main.py <input_file>")
