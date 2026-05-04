        function formatarHora(hora) {
            hora = hora.trim();
            if (hora.match(/^\d{2}:\d{2}$/)) {
                hora += ':00';
            }
            if (!hora.match(/^\d{2}:\d{2}:\d{2}$/)) {
                throw new Error(`Formato inválido: ${hora}. Use HH:MM:SS`);
            }
            return hora;
        }

        async function sincronizar() {
            try {
                const data = {
                    clientes: [
                        { id: "Cliente 1", hora_local: formatarHora(document.getElementById('c1-local').value), hora_envio: formatarHora(document.getElementById('c1-envio').value) },
                        { id: "Cliente 2", hora_local: formatarHora(document.getElementById('c2-local').value), hora_envio: formatarHora(document.getElementById('c2-envio').value) },
                        { id: "Cliente 3", hora_local: formatarHora(document.getElementById('c3-local').value), hora_envio: formatarHora(document.getElementById('c3-envio').value) }
                    ]
                };
                const response = await fetch('./sync', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });

                if (!response.ok) {
                    throw new Error('Erro na sincronização');
                }

                const res = await response.json();
                
                // Atualizar Interface
                document.getElementById('resultados').style.display = 'block';
                document.getElementById('srv-hora').innerText = res.servidor_atual;
                document.getElementById('r-c1').innerText = data.clientes[0].hora_local;
                document.getElementById('r-c2').innerText = data.clientes[1].hora_local;
                document.getElementById('r-c3').innerText = data.clientes[2].hora_local;
                document.getElementById('r-logico').innerText = res.relogio_logico;

                // Ajustes
                let ajustesHtml = '';
                for (let key in res.ajustes) {
                    ajustesHtml += `<div class="result-item">Ajuste do clock (${key}): <span class="red">${res.ajustes[key]}</span></div>`;
                }
                document.getElementById('ajustes-container').innerHTML = ajustesHtml;

                // Ordem
                let ordemHtml = '';
                res.ordem.forEach((nome, index) => {
                    ordemHtml += `<div>${index + 1}º processo a enviar: ${nome}</div>`;
                });
                document.getElementById('ordem-lista').innerHTML = ordemHtml;
            } catch (error) {
                alert('Erro: ' + error.message);
                console.error(error);
            }
        }
