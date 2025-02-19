import numpy as np

# Function to plot the results
def plot_wave_strengths(results):
    """
    Plot the wave strength percentages over time intervals.
    
    Parameters:
    results (dict): Analysis results from analyze_eeg_waves
    """
    import matplotlib.pyplot as plt
    
    # Convert data for plotting
    intervals = list(results["wave_strengths"].keys())
    wave_types = ["Delta", "Theta", "Alpha", "Beta", "Gamma"]
    
    # Create matrix of values
    values = np.array([[float(v) for v in results["wave_strengths"][i]] 
                      for i in intervals])
    
    # Create plot
    plt.figure(figsize=(12, 6))
    for i in range(len(wave_types)):
        plt.plot(range(1, len(intervals) + 1), values[:, i], 
                label=wave_types[i], marker='o')
    
    plt.xlabel('Interval Number')
    plt.ylabel('Wave Strength (%)')
    plt.title('EEG Wave Strengths Over Time')
    plt.legend()
    plt.grid(True)
    plt.savefig('/home/aadityaa/Documents/Programming/capstone_project/Autis_Buddy/analysis/wave_strengths_plot.png')