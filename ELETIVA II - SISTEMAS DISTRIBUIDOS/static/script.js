let clientCount = 0;

async function resetServer() {
    const res = await fetch('/reset', { method: 'POST' });
    const data = await res.json();
    document.getElementById('server-time').innerText = data.server_time;
    document.getElementById('client-forms').innerHTML = '';
    clientCount = 0;
    clearResults();
}

function addClient() {
    if (clientCount >= 3) {
        alert("Máximo de 3 clientes atingido.");
        return;
    }
    clientCount++;
    const div = document.createElement('div');
    div.className = 'client-box';
    div.innerHTML = `
        <h4>Cliente ${clientCount}</h4>
        <label>Hora local:</label>
        <input type="text" id="c${clientCount}-local" placeholder="12:00:00">
        <label>Hora de envio:</label>
        <input type="text" id="c${clientCount}-send" placeholder="12:00:05">
        <button onclick="sendData(${clientCount})">Enviar</button>
    `;
    document.getElementById('client-forms').appendChild(div);
}

async function sendData(id) {
    const local = document.getElementById(`c${id}-local`).value;
    const send = document.getElementById(`c${id}-send`).value;
    
    const res = await fetch('/send_client_data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: id.toString(), local_time: local, send_time: send })
    });
    
    if (res.ok) {
        document.getElementById(`res-c${id}-time`).innerText = local;
        alert(`Dados do Cliente ${id} enviados!`);
    }
}

async function synchronize() {
    const res = await fetch('/synchronize', { method: 'POST' });
    const data = await res.json();
    
    if (data.error) {
        alert(data.error);
        return;
    }

    document.getElementById('logical-clock').innerText = data.logical_clock;
    document.getElementById('adj-s').innerText = data.adjustments.S;
    document.getElementById('adj-c1').innerText = data.adjustments.C1;
    document.getElementById('adj-c2').innerText = data.adjustments.C2;
    document.getElementById('adj-c3').innerText = data.adjustments.C3;

    document.getElementById('order-1').innerText = data.order[0] || '?';
    document.getElementById('order-2').innerText = data.order[1] || '?';
    document.getElementById('order-3').innerText = data.order[2] || '?';
}

function clearResults() {
    ['res-c1-time', 'res-c2-time', 'res-c3-time', 'logical-clock', 'adj-s', 'adj-c1', 'adj-c2', 'adj-c3'].forEach(id => {
        document.getElementById(id).innerText = '---';
    });
    ['order-1', 'order-2', 'order-3'].forEach(id => {
        document.getElementById(id).innerText = '?';
    });
}