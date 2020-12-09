from data.data import setDataset
from math import sqrt

class recomendationSys:
    def __init__(self):
        self.dataset = setDataset()

    def euclideanDistance(self, user1, user2):
        si = {}
        for item in self.dataset[user1]:
            if item in self.dataset[user2]: 
                si[item] = 1

        if len(si) == 0: 
            return 0

        soma = sum([pow(self.dataset[user1][item] - self.dataset[user2][item], 2)
                    for item in self.dataset[user1] 
                        if item in self.dataset[user2]])
        
        return 1/(1 + sqrt(soma))

    def getSimilares(self, user):
        similaridade = [(self.euclideanDistance(user, otherUser), otherUser)
                        for otherUser in self.dataset
                            if otherUser != user]
        similaridade.sort()
        similaridade.reverse()
        return similaridade

    def getRecomendacoes(self, user):
        totais = {}
        somaSimilaridade = {}
        for otherUser in self.dataset:
            if otherUser == user: continue
            similaridade = self.euclideanDistance(user, otherUser)
            if similaridade <= 0: continue
            for item in self.dataset[otherUser]:
                if item not in self.dataset[user]:
                    totais.setdefault(item, 0)
                    totais[item] += self.dataset[otherUser][item] * similaridade
                    somaSimilaridade.setdefault(item, 0)
                    somaSimilaridade[item] += similaridade
        rankings = [(total / somaSimilaridade[item], item) 
                    for item, total in totais.items()]
        rankings.sort()
        rankings.reverse()
        return rankings