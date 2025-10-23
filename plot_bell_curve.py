import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from collections import Counter

# Data from the screenshot - 9 Box Rating column
#ratings = [5, 4, 1, 1, 2, 1, 1, 5, 4, 2, 2, 5, 2, 2, 2, 2, 5, 9, 1, 5, 5]
ratings = [4, 4, 1, 2,3, 2, 1, 2,4,3,2,5,3,4,3,3,5,9,1,4,3,3,5,2,4,1,5]

# Remove any NA values and convert to numpy array
ratings_clean = [r for r in ratings if r != 'NA']
ratings_array = np.array(ratings_clean)

# Calculate statistics
mean = np.mean(ratings_array)
std = np.std(ratings_array)
median = np.median(ratings_array)

# Count frequency of each rating
rating_counts = Counter(ratings_array)

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot 1: Histogram with normal distribution overlay
ax1.hist(ratings_array, bins=np.arange(0.5, 10.5, 1), density=True,
         alpha=0.7, color='steelblue', edgecolor='black', label='Actual Distribution')

# Create theoretical normal distribution curve
x = np.linspace(0, 10, 1000)
normal_dist = stats.norm.pdf(x, mean, std)
ax1.plot(x, normal_dist, 'r-', linewidth=2, label=f'Normal Distribution\n(μ={mean:.2f}, σ={std:.2f})')

# Add vertical lines for mean and median
ax1.axvline(mean, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean:.2f}')
ax1.axvline(median, color='green', linestyle='--', linewidth=2, label=f'Median: {median:.2f}')

ax1.set_xlabel('9 Box Rating', fontsize=12, fontweight='bold')
ax1.set_ylabel('Density', fontsize=12, fontweight='bold')
ax1.set_title('Distribution of 9 Box Ratings with Normal Curve Overlay', fontsize=14, fontweight='bold')
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 10)

# Plot 2: Frequency count with bell curve
ax2.bar(rating_counts.keys(), rating_counts.values(),
        color='steelblue', alpha=0.7, edgecolor='black', width=0.6)

# Add count labels on bars
for rating, count in rating_counts.items():
    ax2.text(rating, count, str(count), ha='center', va='bottom', fontweight='bold')

# Overlay theoretical normal distribution (scaled to match counts)
x_discrete = np.arange(1, 10)
total_count = len(ratings_array)
normal_counts = stats.norm.pdf(x_discrete, mean, std) * total_count
ax2.plot(x_discrete, normal_counts, 'r-', linewidth=2, marker='o',
         label=f'Theoretical Normal\n(μ={mean:.2f}, σ={std:.2f})')

ax2.set_xlabel('9 Box Rating', fontsize=12, fontweight='bold')
ax2.set_ylabel('Frequency Count', fontsize=12, fontweight='bold')
ax2.set_title('Frequency Distribution of 9 Box Ratings', fontsize=14, fontweight='bold')
ax2.legend(loc='upper right')
ax2.grid(True, alpha=0.3, axis='y')
ax2.set_xticks(range(1, 10))
ax2.set_xlim(0, 10)

# Add statistics box
stats_text = f'Statistics:\n'
stats_text += f'Sample Size: {len(ratings_array)}\n'
stats_text += f'Mean: {mean:.2f}\n'
stats_text += f'Median: {median:.2f}\n'
stats_text += f'Std Dev: {std:.2f}\n'
stats_text += f'Min: {min(ratings_array)}\n'
stats_text += f'Max: {max(ratings_array)}'

ax2.text(0.98, 0.97, stats_text, transform=ax2.transAxes,
         fontsize=10, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('9_box_rating_bell_curve.png', dpi=300, bbox_inches='tight')
print("Plot saved as '9_box_rating_bell_curve.png'")
print(f"\nStatistics Summary:")
print(f"  Sample Size: {len(ratings_array)}")
print(f"  Mean: {mean:.2f}")
print(f"  Median: {median:.2f}")
print(f"  Standard Deviation: {std:.2f}")
print(f"  Range: {min(ratings_array)} - {max(ratings_array)}")
print(f"\nRating Distribution:")
for rating in sorted(rating_counts.keys()):
    print(f"  Rating {rating}: {rating_counts[rating]} people ({rating_counts[rating]/len(ratings_array)*100:.1f}%)")

plt.show()
