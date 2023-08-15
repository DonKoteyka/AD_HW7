from dataclasses import dataclass, field
@dataclass
class Stack:
    input_string : str

    def __str__(self):
        res  = ''.join(self.input_string)
        return res

    def is_empty(self):
        return bool(self.input_string)

    def push(self, item : str):
        self.input_string += item

    def pop(self):
        remove = self.input_string[-1]
        res = self.input_string[:len(self.input_string)-1:]
        self.input_string = res
        return remove
    def peek(self):
        return self.input_string[-1]
    def size(self):
        return len(self.input_string)


    def balance(self):
        unic_simbols = list(set([i for i in self.input_string]))
        pattern = {
            '(':')',
            '{':'}',
            '[':']',
            ')':'(',
            '}':'{',
            ']':'['
        }
        count_unbalance_simbols = 0
        for i in unic_simbols:
            # if i in pattern.values():
            #     continue
            if self.input_string.count(i) != self.input_string.count(pattern[i]):
                count_unbalance_simbols += 1
        if count_unbalance_simbols == 0:
            return 'Сбалансированно'
        else:
            return 'Несбалансированно'



if __name__ == "__main__":
    task_1 = '(((([{}]))))'
    task_2 = '[([])((([[[]]])))]{()}'
    task_3 = '{{[()]}}'
    task_4 = '}{}'
    task_5 = '{{[(])]}}'
    task_6 = '[[{())}]'

    res = Stack(task_2)
    print(res.balance())