import os
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

def plot_sentiment_analysis(file_path, output_counter):
    # Read the sentiment data from the CSV file into a Pandas DataFrame
    combined_df = pd.read_csv(file_path)

    # Categorize sentiments into standard categories (Positive, Negative, Neutral, Other)
    def categorize_sentiment(sentence):
        if "positive" in sentence.lower():
            return "Positive"
        elif "negative" in sentence.lower():
            return "Negative"
        elif "neutral" in sentence.lower():
            return "Neutral"
        else:
            return "Other"  # Handle other cases if needed

    combined_df['Sentiment_Category'] = combined_df['Sentiment'].apply(categorize_sentiment)

    # Sort sentiments based on their order in the original dataframe
    sentiments_order = list(combined_df['Sentiment_Category'].unique())  # Get unique values
    sentiments_order.remove("Other")  # Remove "Other" from the list
    sentiments_order.append("Other")  # Append "Other" to the end of the list

    combined_df['Sentiment_Category'] = pd.Categorical(combined_df['Sentiment_Category'], categories=sentiments_order, ordered=True)
    combined_df = combined_df.sort_values(by='Sentiment_Category')

    # Extract heading from the HTML content of the output file using BeautifulSoup
    output_file_path = os.path.join("Data", "raw", f"output{output_counter}.txt")
    with open(output_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    heading = soup.title.string if soup.title else f"Unknown Heading {output_counter}"

    # Use matplotlib to plot the graph from the combined dataframe
    sentiments = combined_df['Sentiment_Category'].unique()
    sentiment_counts = combined_df['Sentiment_Category'].value_counts()

    #  Create a bar graph with appropriate heading and legend
    colors = {'Positive': 'pink', 'Negative': 'brown', 'Neutral': 'lightskyblue', 'Other': 'lightgrey'}
    plt.bar(sentiments, sentiment_counts, color=[colors[s] for s in sentiments])
    plt.title(f'Sentiment Analysis of Reddit Comments\n({heading})')
    plt.xlabel('Sentiments')
    plt.ylabel('Number of Comments')
    plt.legend(sentiments)

    # Add text annotations to the bars
    for i, count in enumerate(sentiment_counts):
        plt.text(i, count + 1, str(count), ha='center', va='bottom')

    #  Check if the "Plots" directory exists, if not, create it
    plots_directory = os.path.join("Data", "plots")
    os.makedirs(plots_directory, exist_ok=True)

    #  Save the graph in the "Plots" directory with a filename based on the output_counter
    graph_path = os.path.join(plots_directory, f"plots{output_counter}.png")
    plt.savefig(graph_path)

    #  Display the graph
    plt.show()

#  Discover sentiment files in the sentiments directory
sentiments_directory = os.path.join("Data", "sentiments")
file_paths = [os.path.join(sentiments_directory, file) for file in os.listdir(sentiments_directory) if file.endswith(".csv")]

# Iterate over each sentiment file and generate plots
for i, file_path in enumerate(file_paths, start=1):
    plot_sentiment_analysis(file_path, i)
