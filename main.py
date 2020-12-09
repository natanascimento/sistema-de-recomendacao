from recomendationSys import recomendationSys

class main(recomendationSys):
    def __init__(self):
        super().__init__()
    
    def recomenda(self):
        for user in self.dataset:
            print('{} -> {}'.format(user, self.getRecomendacoes(user)))

run = main()
run.recomenda()