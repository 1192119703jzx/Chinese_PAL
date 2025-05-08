import json
import tqdm

from prompt.reflection_prompt import REFLECTION_PROMPT
from run_api import call_reflection
from code_execute import process_outputs

model = "deepseek-chat"
max_tokens = 512
temperature = 0

DATA_PATH = f'eval_results/prompt4.jsonl'
OUTPUT_PATH = f'eval_results/prompt4_reflection.jsonl'

# start experiment
instances = list(map(json.loads, open(DATA_PATH)))
# instances = instances[1:2]
scores = 0
total = len(instances)

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    for x in tqdm.tqdm(instances, total=len(instances)):
        result = {}
        question = x["question"]
        target = x["target"]
        generated_code = x["generation"][0]
        
        try:
            outputs = call_reflection(REFLECTION_PROMPT.format(question=question, generated_code=generated_code), model=model, max_tokens=max_tokens, temperature=temperature)
            #print(outputs)
        except Exception as e:
            print(e)
            outputs = []

        try:
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
        result['refined_generation'] = outputs
        f.write(json.dumps(result, ensure_ascii=False) + '\n')
        
        f.flush()

print(f'Accuracy - {scores / total}')