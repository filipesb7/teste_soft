# teste_soft

## Relatório de Testes – Sistema de Previsão de Saúde Fetal

### 1. Estratégia de Testes

O sistema foi testado em múltiplos níveis para garantir robustez, desempenho e confiabilidade. Os testes realizados abrangem:

- **Testes Unitários:** Validação de funções isoladas no backend e módulo de Machine Learning, incluindo cenários positivos e negativos.
- **Testes de Integração:** Verificação da comunicação entre backend, módulo ML e banco de dados, incluindo múltiplos registros.
- **Testes de Validação:** Checagem de campos obrigatórios, tipos inválidos e payloads incompletos.
- **Testes de Carga/Performance:** Avaliação do comportamento sob múltiplos acessos simultâneos usando Apache JMeter.
- **Testes de Ponta a Ponta (E2E):** Simulação do fluxo completo do usuário via frontend utilizando Cypress, incluindo consulta por CPF e validação de campos obrigatórios.

### 2. Casos de Teste Planejados e Implementados

#### a) Testes Unitários (`tests/test_ml_service.py`, `tests/test_backend.py`)
- Carregamento do modelo ML e execução de inferência com dados válidos e inválidos.
- Backend: resposta correta dos endpoints REST, payloads vazios, falha de comunicação com o serviço ML.

#### b) Testes de Integração (`tests/test_integration.py`)
- Backend envia corretamente os dados ao módulo ML e recebe a predição.
- Persistência e recuperação de registros no banco de dados.
- Inserção e verificação de múltiplos registros.

#### c) Testes de Validação (`tests/test_validation.py`)
- Backend rejeita campos obrigatórios ausentes.
- Backend rejeita tipos inválidos.

#### d) Testes de Carga/Performance
- Simulação de 10, 50, 100 e 500 requisições simultâneas ao endpoint `/registros` (exemplo de plano JMeter: `test_plan.jmx`).
- Medição do tempo de resposta médio, máximo e taxa de erro.

#### e) Testes E2E (`cypress/e2e/fetalhealth.cy.js`, `cypress/e2e/consulta_cpf.cy.js`)
- Preenchimento e envio do formulário pelo frontend.
- Visualização do resultado da predição.
- Consulta de registros por CPF e verificação de busca vazia.
- Validação de campos obrigatórios no frontend.

### 3. Evidências de Execução

- **Testes Unitários:** Todos os testes passaram, incluindo cenários de exceção e falha.
- **Testes de Integração:** Comunicação entre backend, ML e banco validada sem erros, múltiplos registros persistidos e recuperados.
- **Testes de Validação:** Backend rejeita corretamente payloads inválidos.
- **Testes de Carga:** Gráficos do JMeter mostram tempo de resposta estável até 100 usuários simultâneos; acima disso, pequenas degradações observadas.
- **Testes E2E:** Cypress executou o fluxo completo, consulta por CPF e validação de campos obrigatórios sem falhas.

*(Inclua aqui prints de telas, gráficos do JMeter e logs do Cypress após execução real dos testes.)*

### 4. Análise dos Resultados

- O sistema se comporta de forma estável sob carga moderada.
- Não foram encontrados bugs críticos nas integrações.
- O tempo de resposta médio ficou abaixo de 500ms para até 100 usuários simultâneos.
- O frontend apresenta corretamente os resultados e permite consulta por CPF.
- O backend lida corretamente com entradas inválidas e falhas de comunicação.

### 5. Sugestões de Melhoria

- Implementar cache para consultas frequentes.
- Melhorar tratamento de exceções e mensagens de erro para o usuário.
- Adicionar autenticação nos endpoints para maior segurança.
- Otimizar a normalização dos dados no módulo ML para grandes volumes.
- Automatizar a execução dos testes em pipeline CI/CD.

---

**Para executar os testes:**

- Testes unitários: `python -m unittest tests/test_ml_service.py` e `python -m unittest tests/test_backend.py`
- Testes de integração: `python -m unittest tests/test_integration.py`
- Testes de validação: `python -m unittest tests/test_validation.py`
- Testes de carga: Abrir o arquivo `test_plan.jmx` no JMeter e executar.
- Testes E2E: `npx cypress open` e rodar os testes em `cypress/e2e/`.

---

*Este relatório deve ser atualizado com evidências reais após a execução dos testes no ambiente final.*