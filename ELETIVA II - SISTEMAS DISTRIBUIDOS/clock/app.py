from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Estado global para simular o sistema distribuído
state = {
    "server_time": None,
    "clients": {}, # {id: {local_time, send_time}}
    "sync_results": None
}

def time_to_seconds(t_str):
    try:
        t = datetime.strptime(t_str, "%H:%M:%S")
        return t.hour * 3600 + t.minute * 60 + t.second
    except:
        return 0

def seconds_to_time(secs):
    return str(timedelta(seconds=int(secs)))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
    global state
    state = {
        "server_time": datetime.now().strftime("%H:%M:%S"),
        "clients": {},
        "sync_results": None
    }
    return jsonify(state)

@app.route('/send_client_data', methods=['POST'])
def send_client_data():
    data = request.json
    client_id = data.get('id')
    state['clients'][client_id] = {
        "local_time": data.get('local_time'),
        "send_time": data.get('send_time')
    }
    return jsonify({"status": "success", "client_id": client_id})

@app.route('/synchronize', methods=['POST'])
def synchronize():
    if len(state['clients']) < 3:
        return jsonify({"error": "Aguardando dados de todos os 3 clientes."}), 400

    server_secs = time_to_seconds(state['server_time'])
    client_secs = [time_to_seconds(c['local_time']) for c in state['clients'].values()]
    
    all_times = [server_secs] + client_secs
    avg_secs = sum(all_times) / len(all_times)
    
    adjustments = {
        "S": avg_secs - server_secs,
        "C1": avg_secs - time_to_seconds(state['clients']['1']['local_time']),
        "C2": avg_secs - time_to_seconds(state['clients']['2']['local_time']),
        "C3": avg_secs - time_to_seconds(state['clients']['3']['local_time']),
    }

    # Ordenação por hora de envio (Lógica de Lamport/Eventos)
    sorted_clients = sorted(
        state['clients'].items(), 
        key=lambda x: time_to_seconds(x[1]['send_time'])
    )
    
    order = [f"Cliente {id}" for id, data in sorted_clients]

    state['sync_results'] = {
        "logical_clock": seconds_to_time(avg_secs),
        "adjustments": {k: f"{v:+.0f}s" for k, v in adjustments.items()},
        "order": order
    }
    
    return jsonify(state['sync_results'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)