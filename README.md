# Music Lyrics Generator & Analysis Project

## Overview

This project is designed to utilize a pre-trained GPT2 model and analyze generated song lyrics using various natural language processing techniques. The main functionalities include word frequency analysis, rhyme density calculation, rhyme scheme detection, and multi-step rhyme scheme analysis. and most importantly Lyrics Generation with a Gradio Interface. Although it uses a trained GPT2 Model we used the following dataset to enhance the output:
Dataset Source : Moura, Luan; Fontelles, Emanuel; Sampaio, Vinicius; França, Mardônio (2020), “Music Dataset: Lyrics and Metadata from 1950 to 2019”, Mendeley Data, V3, doi: 10.17632/3t9vbwxgr5.3

## Features

- **Word Frequency Analysis**: Generates a chart showcasing the top 10 most frequently occurring words in the lyrics.
- **Rhyme Density Calculation**: Displays a pie chart of the distribution of rhyme schemes in the lyrics.
- **Rhyme Scheme Detection**: Identifies and presents the top 10 rhyme schemes by percentage.
- **Multi-step Rhyme Scheme Analysis**: Visualizes the rhyme scheme analysis through a bar chart.

## Graphs

Below are the generated graphs from the analysis:

### 1. Top 10 Word Frequency
![Word Frequency](Graphs/T10%20Word%20Freq.png)

### 2. Rhyme Density Pie Chart
![Rhyme Density](Graphs/Rhyme%20Density.png)

### 3. Top 10 Rhyme Schemes by Percentage
![Rhyme Schemes](Graphs/T10%20Rhyme%20Scheme.png)

### 4. Multi-step Analysis Chart
![Multi-step Analysis]()

## Examples

### Rhyme Density
Output: ![Alt text](Graphs/Rhyme%20Density.png)
>> **Conclusion**: This pie chart illustrates the proportion of rhyme occurrences in the analyzed lyrics, providing insights into the song's structural composition.

### Top 10 Rhyme Schemes
Output: ![Alt text](Graphs/T10%20Rhyme%20Scheme.png)
>> **Conclusion**: The bar chart highlights the most common rhyme schemes, showcasing patterns prevalent in the song.

### Top 10 Word Frequency
Output: ![Alt text](Graphs/T10%20Word%20Freq.png)
>> **Conclusion**: This visualization displays the most frequently used words, helping to identify themes or motifs in the lyrics.

### Generated Lyrics
Output: ![Alt text](Graphs/Generated%20Lyrics.png)
>> **Conclusion**: The generated lyrics offer an example of the creative output, demonstrating the application of NLP techniques in songwriting.

### Rhyme Scheme Analysis
Output: ![Alt text](Graphs/rhymes%20scheme.jpg)
>> **Conclusion**: This analysis provides an overview of rhyme structures, revealing the depth and complexity of lyrical patterns.

## Observations and Conclusions from Graphs

### 1. **Rhyme Density Pie Chart**:
   - **Observation**: The pie chart shows that 81.8% of the generated lyrics are rhyming, while 18.2% are non-rhyming.
   - **Conclusion**: The high proportion of rhyming lyrics indicates a strong focus on maintaining rhyming patterns, which is a key characteristic of many song lyrics. This suggests that the generated lyrics are stylistically aligned with conventional songwriting practices.

### 2. **Top 10 Word Frequencies in Lyrics**:
   - **Observation**: Common words like "the," "to," "I," and "be" dominate the lyrics, reflecting their high frequency.
   - **Conclusion**: The frequent use of these words indicates a typical conversational tone in the lyrics. Words like "I'm," "you're," and "going" suggest themes of personal experiences or storytelling, which are prevalent in many musical genres.

## How to Use

1. **Run the Gradio App**: The app provides an interface to input lyrics and visualize the analyses.
2. **Input Text**: Paste or type in the lyrics you want to analyze.
3. **View Outputs**: The app will display the generated lyrics and the corresponding visual analyses.

## Requirements

- Python 3.x
- Libraries: Gradio, Matplotlib, Pandas, Numpy, Seaborn, and Pronouncing

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sack2116/Final-Class-Team-Project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd lyrics-analysis
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the Gradio interface:
    ```bash
    Run the botebook file
    ```
2. Open the provided local link in your browser to interact with the application.

## License

This project is licensed under the MIT License.

