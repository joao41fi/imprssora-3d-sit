import pickle

# variável que queremos salvar
#my_variable = {'foo': 'bar', 'baz': [1, 2, 3]}

# nome do arquivo onde queremos salvar a variável
#filename = 'my_variable.pickle'

def save(filename, my_variable):
# salvar a variável no arquivo
 with open(filename, 'wb') as f:
    pickle.dump(my_variable, f)



def tras(filename):    
# carregar a variável do arquivo
  with open(filename, 'rb') as f:
    my_variable = pickle.load(f)
  return my_variable

