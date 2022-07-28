import netrc
import time
import json
from urllib import response
from loguru import logger
from service.constants import mensagens
import pandas as pd
import numpy as np
import math


class PA():

    def _init_(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_servico()

    def load_servico(self):

        logger.debug(mensagens.FIM_LOAD_SERVICO)


    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_SERVICO)

        response = self.PA(texts)

        logger.debug(response)

        return response


    def PA(self, texts):

        a1 = texts["a1"][0]
        logger.debug(a1)

        q = texts["q"][0]
        logger.debug(q)
        
        n = texts["n"][0]
        logger.debug(n)

        def soma_progressao_aritmetica(n, a1, q):
            return a1 * (q**n - 1) / (q - 1)

        resultado = soma_progressao_aritmetica(n, a1, q)
        return(resultado)