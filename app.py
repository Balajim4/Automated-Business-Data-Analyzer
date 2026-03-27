import pandas as pd
import gradio as gr

def analyze_csv(file_obj):
    # 1. Read the uploaded CSV
    df = pd.read_csv(file_obj.name)
    
    # 2. Extract basic shape
    row_count = len(df)
    col_count = len(df.columns)
    
    # 3. Automatically calculate statistics (mean, min, max) and round to 2 decimals
    summary_stats = df.describe().round(2)
    
    # 4. Grab the first 5 rows for a preview
    head_df = df.head()
    
    # 5. Format the text report
    report = f"### 📌 Data Overview\n* **Total Rows:** {row_count}\n* **Total Columns:** {col_count}\n\n"
    report += "The tool has automatically processed the mathematical summary and extracted a data preview below."
    
    return report, summary_stats, head_df

# Building the modern UI 
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📊 Automated Business Data Analyzer")
    gr.Markdown("Upload any raw CSV file to instantly generate a statistical breakdown.")
    
    with gr.Row():
        file_input = gr.File(label="Upload CSV File here", file_types=[".csv"])
        
    with gr.Row():
        text_output = gr.Markdown()
        
    with gr.Row():
        stats_output = gr.Dataframe(label="Mathematical Summary (Averages, Min, Max)")
        
    with gr.Row():
        head_output = gr.Dataframe(label="Raw Data Preview (First 5 Rows)")
        
    # Connect the upload button to the logic function
    file_input.upload(fn=analyze_csv, inputs=file_input, outputs=[text_output, stats_output, head_output])

if __name__ == "__main__":
    demo.launch()