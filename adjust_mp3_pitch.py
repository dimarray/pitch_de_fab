import argparse
import librosa
import soundfile as sf
import numpy as np

def adjust_pitch_percentage(input_file, output_file, percentage):
    """
    Adjust the pitch of a song based on a percentage multiplier without affecting its tempo.
    
    Parameters:
        input_file (str): Path to the input audio file.
        output_file (str): Path to save the adjusted audio file.
        percentage (float): Percentage to shift the pitch.
                           Positive values raise the pitch, negative values lower the pitch.
    """
    # Load the audio file
    y, sr = librosa.load(input_file, sr=None)

    # Calculate the number of semitones to shift based on the percentage
    semitones = 12 * np.log2(1 + percentage)
    print(f"Calculated semitones adj: {semitones}")

    # Apply pitch shift (without changing the tempo)
    y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=semitones)
    
    # Save the modified song to the output file
    sf.write(output_file, y_shifted, sr)
    print(f"Pitch adjusted by {percentage}% and saved as: {output_file}")

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Adjust the pitch of a song by a percentage.")
    parser.add_argument('--input_file', type=str, help="Path to the input audio file.")
    parser.add_argument('--output_file', type=str, help="Path to save the adjusted audio file.")
    parser.add_argument('--new_pitch', type=float, help="the target pitch.")

    # Parse the command line arguments
    args = parser.parse_args()

    if (not args.input_file or not args.output_file or not args.new_pitch):
        parser.print_help()
        exit(1)

    # Calculate the percentage
    target_pitch = args.new_pitch / 440.0

    print(f"Pitch shifting to {target_pitch}")

    # Call the adjust_pitch_percentage function with the provided arguments
    adjust_pitch_percentage(args.input_file, args.output_file, target_pitch)

if __name__ == "__main__":
    main()
