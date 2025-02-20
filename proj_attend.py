import matplotlib.pyplot as plt
import numpy as np

# Function to plot the graph
def plot_attendance(n):
    # Generate values for x (total classes held)
    x = np.arange(10, 41)
    
    # Calculate y (projected attendance)
    y = np.array([(x_val - n) / x_val * 100 for x_val in x])

    # Create the plot with a larger figure size
    plt.figure(figsize=(14, 7))
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Projected Attendance')

    # Define the rounding function for coloring
    def round_attendance(value):
        if value % 1 >= 0.5:
            return np.ceil(value)
        else:
            return np.floor(value)

    # Apply the rounding logic for coloring
    y_rounded = np.array([round_attendance(val) for val in y])

    # Define the shaded sections based on attendance criteria
    plt.fill_between(x, y, where=(y_rounded <= 60), color='red', alpha=0.3, edgecolor='none', label='≤ 60%')
    plt.fill_between(x, y, where=(y_rounded > 60) & (y_rounded <= 74), color='yellow', alpha=0.3, edgecolor='none', label='61% - 74%')
    plt.fill_between(x, y, where=(y_rounded > 74) & (y_rounded <= 80), color='#CCFFCC', alpha=0.3, edgecolor='none', label='75% - 80%')
    plt.fill_between(x, y, where=(y_rounded > 80) & (y_rounded <= 85), color='#99FF99', alpha=0.3, edgecolor='none', label='81% - 85%')
    plt.fill_between(x, y, where=(y_rounded > 85) & (y_rounded <= 90), color='#66FF66', alpha=0.3, edgecolor='none', label='86% - 90%')
    plt.fill_between(x, y, where=(y_rounded > 90) & (y_rounded <= 95), color='#33FF33', alpha=0.3, edgecolor='none', label='91% - 95%')
    plt.fill_between(x, y, where=(y_rounded > 95), color='cyan', alpha=0.3, edgecolor='none', label='96% - 100%')

    # Set fixed axis limits
    plt.xlim(10, 40)
    plt.ylim(0, 100)

    # Set x-axis ticks to show every value
    plt.xticks(np.arange(10, 41, 1))

    # Label the axes and title
    plt.xlabel('Total Classes Held')
    plt.ylabel('Projected Attendance (%)')
    plt.title('Projected Attendance Based on Classes Missed')
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()

# Take input for classes missed
n = int(input("Enter the number of classes missed: "))
plot_attendance(n)
