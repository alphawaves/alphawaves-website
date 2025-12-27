#!/usr/bin/env python3
"""
Generate an executive-level, eye-candy scatter plot showing how a market maker sets
the bid-ask spread over time, using synthetic market data.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patheffects
from datetime import datetime, timedelta
import matplotlib.patches as mpatches

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic time data (100 time points over a trading day)
n_points = 100
start_time = datetime(2025, 1, 15, 9, 30)  # Market open
time_points = [start_time + timedelta(minutes=i*4) for i in range(n_points)]

# Generate mid-price (mean-reverting random walk)
mid_price = 100 + np.cumsum(np.random.normal(0, 0.3, n_points))

# Generate spread based on volatility and inventory risk
volatility = np.abs(np.diff(mid_price, prepend=mid_price[0]))
base_spread = 0.10
spread = base_spread + volatility * 2 + np.random.normal(0, 0.02, n_points)
spread = np.maximum(spread, 0.05)

# Calculate bid and ask prices
bid_price = mid_price - spread / 2
ask_price = mid_price + spread / 2

# ========== LIGHT MODE VERSION - Executive Style ==========
fig, ax = plt.subplots(figsize=(14, 8), facecolor='white')
ax.set_facecolor('#fafafa')

# Create gradient fill between bid and ask
ax.fill_between(time_points, bid_price, ask_price, alpha=0.15, color='#6366f1', label='Spread Zone')

# Plot bid line with gradient effect
bid_line = ax.plot(time_points, bid_price, linewidth=3, color='#10b981',
                   label='Bid Price', zorder=3, alpha=0.9)
bid_line[0].set_path_effects([patheffects.withStroke(linewidth=5, foreground='#d1fae5', alpha=0.5)])

# Plot ask line with gradient effect
ask_line = ax.plot(time_points, ask_price, linewidth=3, color='#ef4444',
                   label='Ask Price', zorder=3, alpha=0.9)
ask_line[0].set_path_effects([patheffects.withStroke(linewidth=5, foreground='#fee2e2', alpha=0.5)])

# Add scatter points with gradients
scatter_bid = ax.scatter(time_points[::5], bid_price[::5], s=120, c='#10b981',
                        edgecolors='white', linewidths=2, alpha=0.9, zorder=4)
scatter_ask = ax.scatter(time_points[::5], ask_price[::5], s=120, c='#ef4444',
                        edgecolors='white', linewidths=2, alpha=0.9, zorder=4)

# Mid-price line (elegant dashed)
ax.plot(time_points, mid_price, color='#6b7280', linewidth=2.5,
        linestyle='--', label='Mid Price', alpha=0.6, zorder=2)

# Professional styling
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_color('#cbd5e1')
ax.spines['bottom'].set_color('#cbd5e1')

# Grid with subtle styling
ax.grid(True, alpha=0.2, linestyle='-', linewidth=1, color='#cbd5e1', zorder=1)
ax.set_axisbelow(True)

# Labels and title
ax.set_xlabel('Trading Time', fontsize=14, fontweight='600', color='#1e293b', family='sans-serif')
ax.set_ylabel('Price ($)', fontsize=14, fontweight='600', color='#1e293b', family='sans-serif')
ax.set_title('Market Maker Bid-Ask Spread Dynamics', fontsize=18, fontweight='700',
             color='#0f172a', pad=25, family='sans-serif')

# Enhanced legend
legend = ax.legend(loc='upper left', frameon=True, shadow=True, fontsize=12,
                  fancybox=True, framealpha=0.95, edgecolor='#cbd5e1')
legend.get_frame().set_facecolor('white')

# Format x-axis
import matplotlib.dates as mdates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, ha='center')
ax.tick_params(axis='both', labelsize=11, colors='#475569', length=6, width=1.5)

fig.autofmt_xdate()
plt.tight_layout()

plt.savefig('/Users/nadya/AlphaWaves/assets/images/bid-ask-spread.png', dpi=200, bbox_inches='tight', facecolor='white')
print("✓ Executive-style light mode plot saved")

# ========== DARK MODE VERSION - High Contrast ==========
fig, ax = plt.subplots(figsize=(14, 8), facecolor='#0f172a')
ax.set_facecolor('#1e293b')

# Create gradient fill between bid and ask
ax.fill_between(time_points, bid_price, ask_price, alpha=0.2, color='#818cf8', label='Spread Zone')

# Plot bid line with glow effect
bid_line = ax.plot(time_points, bid_price, linewidth=3.5, color='#34d399',
                   label='Bid Price', zorder=3, alpha=1.0)
bid_line[0].set_path_effects([patheffects.withStroke(linewidth=6, foreground='#6ee7b7', alpha=0.4)])

# Plot ask line with glow effect
ask_line = ax.plot(time_points, ask_price, linewidth=3.5, color='#fb7185',
                   label='Ask Price', zorder=3, alpha=1.0)
ask_line[0].set_path_effects([patheffects.withStroke(linewidth=6, foreground='#fda4af', alpha=0.4)])

# Add scatter points with strong contrast
scatter_bid = ax.scatter(time_points[::5], bid_price[::5], s=130, c='#34d399',
                        edgecolors='#d1fae5', linewidths=2.5, alpha=1.0, zorder=4)
scatter_ask = ax.scatter(time_points[::5], ask_price[::5], s=130, c='#fb7185',
                        edgecolors='#fecdd3', linewidths=2.5, alpha=1.0, zorder=4)

# Mid-price line (high contrast)
ax.plot(time_points, mid_price, color='#e2e8f0', linewidth=2.5,
        linestyle='--', label='Mid Price', alpha=0.8, zorder=2)

# Professional dark styling
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_color('#475569')
ax.spines['bottom'].set_color('#475569')

# Grid
ax.grid(True, alpha=0.15, linestyle='-', linewidth=1, color='#475569', zorder=1)
ax.set_axisbelow(True)

# High contrast labels
ax.set_xlabel('Trading Time', fontsize=14, fontweight='600', color='#f1f5f9', family='sans-serif')
ax.set_ylabel('Price ($)', fontsize=14, fontweight='600', color='#f1f5f9', family='sans-serif')
ax.set_title('Market Maker Bid-Ask Spread Dynamics', fontsize=18, fontweight='700',
             color='#f8fafc', pad=25, family='sans-serif')

# Enhanced legend with high contrast
legend = ax.legend(loc='upper left', frameon=True, shadow=True, fontsize=12,
                  fancybox=True, framealpha=0.95, edgecolor='#475569')
legend.get_frame().set_facecolor('#0f172a')
for text in legend.get_texts():
    text.set_color('#e2e8f0')

# Format x-axis with high contrast
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, ha='center')
ax.tick_params(axis='both', labelsize=11, colors='#cbd5e1', length=6, width=2)

fig.autofmt_xdate()
plt.tight_layout()

plt.savefig('/Users/nadya/AlphaWaves/assets/images/bid-ask-spread-dark.png', dpi=200, bbox_inches='tight', facecolor='#0f172a')
print("✓ Executive-style dark mode plot saved with high contrast")
