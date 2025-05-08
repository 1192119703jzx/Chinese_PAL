import signal
import copy
from collections import Counter

class TimeoutSignal:
    def __init__(self, seconds=1, error_message='Timeout occurred'):
        self.seconds = int(seconds) # alarm requires integers
        self.error_message = error_message
        self._old_handler = None

    def handle_timeout(self, signum, frame):
        """Signal handler that raises the TimeoutError."""
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.alarm(0)

class runtime:
    GLOBAL_DICT = {}
    LOCAL_DICT = None
    HEADERS = []
    def __init__(self):
        self._global_vars = copy.copy(self.GLOBAL_DICT)
        self._local_vars = copy.copy(self.LOCAL_DICT) if self.LOCAL_DICT else None
        
        for c in self.HEADERS:
            self.exec_code(c)
        
    def exec_code(self, code_piece: str):
        exec(code_piece, self._global_vars)
        
    def eval_code(self, expr: str):
        return eval(expr, self._global_vars)
    
    @property
    def answer(self):
        return self._global_vars['answer']

def execute_code(code):
    #code = code[1:-1]
    runtime_instance = runtime()
    runtime_instance.exec_code('\n'.join(code))
    return runtime_instance.eval_code('solution()')


def process_outputs(outputs):
    results = []
    for code in outputs:
        code = code.strip()
        code = code.split('\n')
        if code[0].startswith('```'):
            code = code[1:-1]
        with TimeoutSignal(5):
            try:
                ans = execute_code(code)
                results.append(ans)
            except Exception as e:
                print(e)
                continue

    if len(results) == 0:
        print('No results was produced.')
        return None
    
    counter = Counter(results)
    return counter.most_common(1)[0][0]