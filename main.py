class Dados_pc:
    def __init__ (self, marca, memoria, placa_video):
        self.marca = marca
        self.memoria = memoria
        self.placa_video = placa_video
       

    def main(self):
        project_name: str = "projetogit"
        print(f"\n====== Bem vindo ao {project_name} =======!")
        

    def ver_dados(self):
        projeto_name: str = 'projetogit'
        print('\n> A seguir dados do pc !!! ')

    def ligar_computador(self):
        print('\nlingando...')

    def informaçoes_pc(self):
        print(f'{self.marca}, {self.memoria}, {self.placa_video}')

    def desligar_pc(self):
        print('desligando.\n')

computador1 = Dados_pc('Asus', '16 gigas','NvDIA')

if __name__ == "__main__":
    computador1 = Dados_pc('Asus', '16 gigas','NvDIA')
    computador1.main()
    computador1.ver_dados()
    computador1.ligar_computador()
    computador1.informaçoes_pc()
    computador1.desligar_pc()

