from abc import ABC, abstractmethod

class MetodoDePagamento(ABC): #interface de pagamento
    @abstractmethod
    def pagar(self, pedido):
        pass

class notificar(ABC): #interface de notificação
    @abstractmethod
    def notificar(self, pedido):
        pass

class PagamentoCartaoCredito:
     def pagar(self, pedido):
        print(f"Pagaando R$ {pedido['valor']:.2f} com cartão de crédito.")

class PagamentoBoleto:
    def pagar(self, pedido):
         print(f"Gerando boleto no valor R$ {pedido['valor']:.2f}.") 

        # novo metodo de pagamento com pix
class PagamentoPix(MetodoDePagamento):
    def pagar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} com Pix.")

class NotificadorEmail:
    def notificar(self, pedido):
        print(f"Enviando email de confirmação para o pedido {pedido['cliente_email']}.")

        # Novo notificador com SMS
class NotificadorSMS:
    def notificar(self, pedido):
        print(f"Enviando SMS de confirmação para o pedido {pedido['cliente_telefone']}.")

class ProcessadorDePedidos:
            """Agora esta classe segue os princípios de SOLID
            - Tem uma única responsabilidade (SRP)
            - Depende de abstrações (DIP)
            - Aberta para extensão, fechada para modificação (OCP)"""
            
            def __init__(self, metodo_pagamento: MetodoDePagamento, notificador: notificar):
                self.metodo_pagamento = metodo_pagamento
                self.notificador = notificador

            def processar(self, pedido):
                print(f"Processando pedido para #{pedido['id']} no valor de R$ {pedido['valor']:.2f}")

                self.metodo_pagamento.pagar(pedido)
                self.notificador.notificar(pedido)

                pedido ['status'] = "Processado"
                print("Pedido processado com sucesso.\n")

                #----------------------------------------------
                # exemplo de uso
                #----------------------------------------------

if __name__ == "__main__":
    pedido1 = {
        'id': 123, 
        'valor': 150.75, 
        'cliente_email': 'cliente@exemplo.com',
        'cliente_telefone': '11999999999',
        'status': 'Pendente'
        }
    
    # Pagamento com cartão de crédito e notificação por email
    processador1 = ProcessadorDePedidos(PagamentoCartaoCredito(), NotificadorEmail())
    processador1.processar(pedido1)

    # Pagamento com boleto e notificação por SMS
    pedido2 = pedido1.copy()
    pedido2['id'] = 456
    processador2 = ProcessadorDePedidos(PagamentoBoleto(), NotificadorSMS())
    processador2.processar(pedido2)


    #novo pedido com pix e notificação por email
    pedido3 = pedido1.copy()
    pedido3['id'] = 789
    processador3 = ProcessadorDePedidos(PagamentoPix(), NotificadorEmail())
    processador3.processar(pedido3)
       


                
                
                                        