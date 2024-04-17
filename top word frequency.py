import os
import collections
import string

def analyze_segmented_file(file_path):
    """
    Analyzes a segmented file and returns the top frequent segments with counts and percentages.
    Excludes punctuation from the analysis.

    Args:
        file_path (str): Path to the segmented file.

    Returns:
        list: A list of tuples containing the top frequent segments, their counts, and percentages.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    all_segments = []
    for line in lines:
        segments = line.strip().split()
        segments = [segment.translate(str.maketrans('', '', string.punctuation)) for segment in segments]
        all_segments.extend(segments)

    total_segments = len(all_segments)
    segment_counts = collections.Counter(all_segments)
    top_segments = segment_counts.most_common()

    segment_stats = []
    for i, (segment, count) in enumerate(top_segments, start=1):
        percentage = (count / total_segments) * 100
        segment_stats.append((i, segment, count, f"{percentage:.2f}%"))

    return segment_stats[:150]

def main():
    """
    Main function to handle file processing and output the top frequent segments.
    """
    segmented_file_path = "C:\\Users\\bubufafa\\Downloads\\segmented_001 Full Transcription (v3)_LW.txt"
    top_segments = analyze_segmented_file(segmented_file_path)

    # Get the directory and filename from the input file path
    directory, filename = os.path.split(segmented_file_path)
    output_file_path = os.path.join(directory, f"top_segments_{filename.split('.')[0]}.txt")

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("No.\tSegment\tCount\tPercentage\n")
        for rank, segment, count, percentage in top_segments:
            output_file.write(f"{rank}\t{segment}\t{count}\t{percentage}\n")

    print(f"Top frequent segments written to '{output_file_path}'.")

if __name__ == "__main__":
    main()