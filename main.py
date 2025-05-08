import tqdm
import json
import re

from run_api import call_deepseek, call_gpt
from code_execute import process_outputs
from prompt.prompt_v1 import MATH_PROMPT_1
from prompt.prompt_v2 import MATH_PROMPT_2
from prompt.prompt_v3 import MATH_PROMPT_3
from prompt.prompt_v4 import MATH_PROMPT_4
from prompt.prompt_COT import MATH_PROMPT_COT
from prompt.system_prompt import SYS_PROMPT_1, SYS_PROMPT_2, SYS_PROMPT_COT
from COT_evaluation import convert_to_float, cot_proprocess


# set parameters for experiment
math_prompt = MATH_PROMPT_1
system_prompt = SYS_PROMPT_1

# model = "deepseek-chat"
model = "gpt-3.5-turbo"
max_tokens = 512
temperature = 0
n = 1

DATA_PATH = f'dataset/math23k_test.jsonl'
OUTPUT_PATH = f'eval_results/prompt_1_gpt3.5.jsonl'

# start experiment
instances = list(map(json.loads, open(DATA_PATH)))
# instances = instances[1:2]
scores = 0
total = len(instances)

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    for x in tqdm.tqdm(instances, total=len(instances)):
        result = {}
        question = x["original_text"]
        target = convert_to_float(x["ans"])
        
        try:
            # outputs = call_deepseek(math_prompt.format(question=question), system_prompt, model=model, max_tokens=max_tokens, temperature=temperature, n=n)
            outputs = call_gpt(math_prompt.format(question=question), system_prompt, model=model, max_tokens=max_tokens, temperature=temperature)
        except Exception as e:
            print(e)
            outputs = []

        try:
            if math_prompt == MATH_PROMPT_COT:
                ans = cot_proprocess(outputs[0])
            else:
                ans = process_outputs(outputs)
            ans = float(ans)
            if abs(ans - target) < 1e-3 or ans == target:
                score = 1
            else:
                score = 0
        except Exception as e:
            print(e)
            ans = ''
            score = 0
        scores += score
        
        result['question'] = question
        result['target'] = target
        result['answer'] = ans
        result['score'] = score
        result['generation'] = outputs
        f.write(json.dumps(result, ensure_ascii=False) + '\n')
        
        f.flush()

print(f'Accuracy - {scores / total}')