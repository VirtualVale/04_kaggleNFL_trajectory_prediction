import matplotlib.pyplot as plt
from utils import deg2arrowPosition
from matplotlib.lines import Line2D
import pandas as pd

def plot_single_player(input_df: pd.DataFrame, output_df: pd.DataFrame) -> None:
    """Plots the player movements and infos about the player and supplementary positions.

    Args:
        input_df (pd.DataFrame): Dataframe of a single play of a single player (input)
        output_df (pd.DataFrame): Dataframe of a single play of a single player (output)

    Raises:
        ValueError: Input dataframe is empty.
    """

    plt.figure(figsize=(12, 6))
    plt.xlim(0, 120)
    plt.ylim(0, 54)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Player movements, info and ball landing position')
    plt.grid(True, alpha=0.3)

    dx_o, dy_o = deg2arrowPosition(input_df['o'])
    plt.quiver(input_df['x'], input_df['y'], dx_o, dy_o,
            angles='xy', scale_units='xy', scale=0.5,
            color='C0', alpha=0.8, width=0.002)

    dx_dir, dy_dir = deg2arrowPosition(input_df['dir'])
    plt.quiver(input_df['x'], input_df['y'], dx_dir, dy_dir,
            angles='xy', scale_units='xy', scale=0.5,
            color='C1', alpha=0.8, width=0.002)
    
    plt.scatter(input_df['ball_land_x'], input_df['ball_land_y'], c='red')
    plt.scatter(output_df['x'],output_df['y'], c='green', alpha=0.5, s=10)

    legend_elements = [
        Line2D([0], [0], color='C0', lw=2, label='orientation (o)'),
        Line2D([0], [0], color='C1', lw=2, label='motion (dir)'),
        Line2D([0], [0], color='C2', lw=2, label=f'motion to predict (output)'),
        Line2D([0], [0], color='C3', lw=2, label=f'Ball landing position')
    ]
    plt.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')

    if len(input_df) != 0:
        info_row = input_df.iloc[0]
    else:
        raise ValueError("Input dataframe is empty.")
    
    plt.text(118, 52, f"Identifier: {info_row['game_id']}/{info_row['play_id']}/{info_row['nfl_id']}", ha='right', va='top')
    plt.text(118, 50, f"Player to Predict: {info_row['player_to_predict']}", ha='right', va='top')
    plt.text(118, 46, f"Name: {info_row['player_name']}", ha='right', va='top')
    plt.text(118, 44, f"Height: {info_row['player_height']}", ha='right', va='top')
    plt.text(118, 42, f"Weight: {info_row['player_weight']}", ha='right', va='top')
    plt.text(118, 40, f"Birthdate: {info_row['player_birth_date']}", ha='right', va='top')
    plt.text(118, 38, f"Position: {info_row['player_position']}", ha='right', va='top')
    plt.text(118, 36, f"Side: {info_row['player_side']}", ha='right', va='top')
    plt.text(118, 34, f"Role: {info_row['player_role']}", ha='right', va='top')

    play_direction_symbol = '<-' if info_row['play_direction'] == 'right' else '->' 
    plt.text(59, 52, f"Play direction: {play_direction_symbol}, w. {info_row['absolute_yardline_number']} yards to go", ha='right', va='top')
    plt.show()