describe('Fluxo completo do sistema', () => {
  it('Preenche e envia formulário, visualiza resultado', () => {
    cy.visit('http://localhost:5500/index.html'); // ajuste porta conforme seu servidor
    cy.get('input[name="cpf"]').type('12345678900');
    cy.get('input[name="baseline_value"]').type('120');
    // ... repita para todos os campos ...
    cy.get('input[name="histogram_tendency"]').type('0');
    cy.get('button[type="submit"]').click();
    cy.contains('Resultado:').should('exist');
  });

  it('Valida campos obrigatórios', () => {
    cy.visit('http://localhost:5500/index.html');
    cy.get('button[type="submit"]').click();
    cy.on('window:alert', (txt) => {
      expect(txt).to.contains('required');
    });
  });
}); 