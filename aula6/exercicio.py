import sys
import numpy as np

class Perceptron:
    def __init__(self):
        pass

def train(self, inputs, outputs, learning_rate, epochs):
    self.inputs = inputs
    self.outputs = outputs
    self.learning_rate = learning_rate
    self.epochs = epochs
    
    w1, w2, bias = np.random.uniform(-1, 1), np.random.uniform(-1, 1), np.random.uniform(-1, 1)

    for i in range(epochs):
        for j in range(len(inputs)):
            # Aqui definimos a função de ativação, no exemplo citado no início do artigo, foi utilizada a função degrau, mas outras funções podem ser testadas, aqui abaixo utilizaremos a sunção sigmoid
            sigmoid = 1 / (1 + np.exp(- ((inputs[j][0] * w1) + (inputs[j][1] * w2) + bias)))
            
            # Atualizando os pesos após cada iteração
            w1 = w1 + (learning_rate * (outputs[j][0] - sigmoid) * inputs[j][0])
            w2 = w2 + (learning_rate * (outputs[j][0] - sigmoid) * inputs[j][1])
            bias = bias + (learning_rate * (outputs[j][0] - sigmoid))
    return w1, w2, bias

def predict(self, weights, x1, x2):
# Na função degrau devolvemos 1 se o resultado for maior ou igual a 0 e 0 se for menor
# Na função sigmoid devolvemos 1 se o resultado for maior que 0.5 e 0 se for menor ou igual a 0
  return 1 if 1 / (1 + np.exp(- ((x1 * weights[0]) + (x2 * weights[1]) + weights[2]))) > 0.5 else 0

# Cada item da lista dos dados de entrada representa as duas entradas lógicas
# A variável outputs representa a saída esperada da operação lógica, aqui no caso representa a tabela OR
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
outputs = [[0], [1], [1], [1]]

percp = Perceptron()
# Passamos os dados de entrada e de saída, junto com a taxa de aprendizagem e a quantidade de épocas de treinamento
train = percp.train(inputs, outputs, 0.01, 10000)
# Como a função train retorna os 3 pesos, passamos a variável train no método predict juntamente com as duas entradas que queremos testar
predc = percp.predict(train, 1, 0)
predc