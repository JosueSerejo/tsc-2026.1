import {describe, it, expect} from 'vitest';
import { validarEmail } from '../src/funcoes';

describe('Validador de E-mail', () => {
  // Os testes entrarão aqui

it('deve retornar false se o email não contiver o símbolo @', () => {
  const emailInvalido = 'usuario-dominio.com';
  
  const resultado = validarEmail(emailInvalido);
  
  expect(resultado).toBe(false);
});

it('deve retornar true para um e-mail válido', () => {
  const resultado = validarEmail('teste@email.com');
  
  expect(resultado).toBe(true);
});

it('Este e-mail é curto demais', () => {
    // 1. Organize
  const emailCurto = 'josu'; 

  // 2. Agir
  const resultado = validarEmail(emailCurto);

  // 3. Afirmar
  expect(resultado).toBe(false);
});

it('E-mail está vazio', ( )=> { 
    const emailVazio = '';

    const resultado = validarEmail(emailVazio);

    expect(resultado).toBe(false)

})

});