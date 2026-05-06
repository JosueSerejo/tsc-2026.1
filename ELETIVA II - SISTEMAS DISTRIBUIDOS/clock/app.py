from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Estado global
state = {
    "server_time": "10:00",
    "clients": {},
    "sync_results": None
}

def time_to_minutes(t_str):
    try:
        t = datetime.strptime(t_str, "%H:%M")
        return t.hour * 60 + t.minute
    except:
        return 0

def minutes_to_time(mins):
    hours = int(mins // 60)
    minutes = int(mins % 60)
    return f"{hours:02d}:{minutes:02d}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
    global state
    data = request.json or {}
    manual_time = data.get("server_time") or "10:00"
    state = {
        "server_time": manual_time,
        "clients": {},
        "sync_results": None
    }
    return jsonify(state)

@app.route('/send_client_data', methods=['POST'])
def send_client_data():
    data = request.json
    client_id = str(data.get('id'))
    state['clients'][client_id] = {
        "local_time": data.get('local_time'),
        "send_time": data.get('send_time')
    }
    return jsonify({"status": "success", "client_id": client_id})

@app.route('/synchronize', methods=['POST'])
def synchronize():
    if len(state['clients']) < 3:
        return jsonify({"error": "Aguardando dados de todos os 3 clientes."}), 400

    # Berkeley Algorithm
    server_mins = time_to_minutes(state['server_time'])
    c1_mins = time_to_minutes(state['clients']['1']['local_time'])
    c2_mins = time_to_minutes(state['clients']['2']['local_time'])
    c3_mins = time_to_minutes(state['clients']['3']['local_time'])
    
    # Média: (10:00 + 10:30 + 11:10 + 09:00) / 4 = 610 min (10:10)
    all_times = [server_mins, c1_mins, c2_mins, c3_mins]
    avg_mins = sum(all_times) / len(all_times)
    
    # Ajustes conforme o quadro:
    # S: 10:10 - 10:00 = +10
    # P1: 10:10 - 10:30 = -20
    # P2: 10:10 - 11:10 = -60
    # P3: 10:10 - 09:00 = +70
    adjustments = {
        "S": avg_mins - server_mins,
        "C1": avg_mins - c1_mins,
        "C2": avg_mins - c2_mins,
        "C3": avg_mins - c3_mins,
    }

    # Ordenação por hora de envio:
    # P1: 10:50, P2: 11:20, P3: 10:40
    # Ordem: P3 (10:40), P1 (10:50), P2 (11:20)
    sorted_clients = sorted(
        state['clients'].items(), 
        key=lambda x: time_to_minutes(x[1]['send_time'])
    )
    
    order = [f"Cliente {id}" for id, data in sorted_clients]

    state['sync_results'] = {
        "logical_clock": minutes_to_time(avg_mins),
        "adjustments": {k: f"{v:+.0f} min" for k, v in adjustments.items()},
        "order": order
    }
    
    return jsonify(state['sync_results'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)