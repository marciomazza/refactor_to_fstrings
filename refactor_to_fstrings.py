
from bowler import Query
from bowler.imr import FunctionArgument
from bowler.types import TOKEN, Leaf

pattern = '''
    power< string=STRING
      trailer< '.' 'format' >
      trailer< '(' args=any* ')' >
    >
'''


def modifier(node, capture, filename):
    string = capture['string']
    args = capture['args']
    fargs = FunctionArgument.build_list(args, False)
    values = [f'{{{a.value}}}' for a in fargs]
    f_string = 'f' + str(string).format(*values)
    return Leaf(TOKEN.STRING, f_string)


q = Query('test/example.py')
q.select(pattern)
q.modify(modifier)
q.idiff()
