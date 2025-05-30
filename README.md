# Chinese PAL

Chinese PAL is a Program-Aided Language model implementation adapted for Chinese language tasks. This project explores different prompting strategies to enhance the model's ability to solve problems by generating reasoning steps and code representations.

## Project Structure
chinese-pal/\
├── prompts/                  
│   ├── prompt1.txt \
│   ├── prompt2.txt      
│   └── ...               
├── main.py                
├── run_api.py \
├── reflection.py \
├── code_execute.py \
├── COT_evaluation.py \
└── README.md   

## Usage
To run Chinese PAL:
    
1. **Modify Configuration in `main.py`:**

    Open `main.py` and configure the following:
    - **Input/Output file name**: Make sure the correct input file is specified (e.g., a JSON or JSONL file).
    - **Prompt file**: Select the desired prompt template from the `prompts/` folder.
    - **System prompt**: Customize the system-level prompt as needed. 
    1. SYSTEM_PROMPT_1 is for comtent prompt only with few-shot examples
    2. SYSTEM_PROMPT_2 is for comtent prompt with chinese each line explanation
    - **Content prompt**: Customize the user-level prompt as needed. 
    1. Prompt 1 is random selection for few-shot examples
    2. Prompt 2 is random selection for few-shot examples + chinese each line explanation
    3. Prompt 3 is category-based selection for few-shot examples
    4. Prompt 4 is category-based selection for few-shot examples + chinese each line explanation
    5. Reflection Prompt is for self-refine based on the output generated by the previous prompts.

2. **Set your LLM's API in `main.py`:**

3. **Execute the script:**

   ```bash
   python main.py
   ```
   The script will load the input data, apply the selected prompt strategy, and process it to language model's api.

## Notes
- Ensure all necessary dependencies (e.g., openai) are installed and correctly configured. Install library `google` if you want to generate new category based selection for prompt.

- You can create new prompt formats by adding more .py files to the prompts/ folder and referencing them in main.py.