describe('Consulta de registros por CPF', () => {
  it('Consulta registros e exibe resultados', () => {
    cy.visit('http://localhost:5500/index.html'); // ajuste porta conforme seu servidor
    cy.get('input[name="cpf"]').type('12345678900');
    // Simule o envio de um registro primeiro, se necessário
    cy.get('input[name="baseline_value"]').type('120');
    // ... repita para todos os campos ...
    cy.get('input[name="histogram_tendency"]').type('0');
    cy.get('button[type="submit"]').click();
    cy.contains('Resultado:').should('exist');
    // Agora consulta por CPF (pode ser via outro endpoint ou interface)
    cy.request('GET', 'http://localhost:5000/registros?cpf=12345678900').then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.length).to.be.greaterThan(0);
    });
  });

  it('Consulta CPF inexistente retorna vazio', () => {
    cy.request('GET', 'http://localhost:5000/registros?cpf=00000000000').then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body.length).to.eq(0);
    });
  });
}); 