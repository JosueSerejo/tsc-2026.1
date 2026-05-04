from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import os

app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

# Estado do sistema
servidor_info = {"hora_local": "", "clientes": [], "log": []}

def format_time(dt):
    return dt.strftime("%H:%M:%S")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sync', methods=['POST'])
def sync():
    data = request.json
    servidor_time = datetime.now()
    
    clientes = data.get('clientes', [])
    if not clientes:
        return jsonify({"error": "Nenhum cliente para sincronizar"}), 400

    # Converter strings para objetos datetime
    tempos_clientes = []
    for c in clientes:
        # Usamos a data de hoje para o cálculo de diferença de tempo
        t = datetime.strptime(c['hora_local'], "%H:%M:%S").replace(
            year=servidor_time.year, month=servidor_time.month, day=servidor_time.day
        )
        tempos_clientes.append(t)

    # Cálculo da Média (Algoritmo de Berkeley simplificado)
    todos_tempos = tempos_clientes + [servidor_time]
    segundos_totais = sum(t.hour * 3600 + t.minute * 60 + t.second for t in todos_tempos)
    media_segundos = segundos_totais / len(todos_tempos)
    
    hora_media = (datetime.min + timedelta(seconds=media_segundos)).time()
    dt_media = datetime.combine(servidor_time.date(), hora_media)

    # Ordenação por hora de envio (Lógica de Lamport/Eventos)
    # Ordenamos os clientes com base na 'hora_envio' informada
    clientes_ordenados = sorted(clientes, key=lambda x: x['hora_envio'])

    resultado = {
        "servidor_atual": format_time(servidor_time),
        "relogio_logico": format_time(dt_media),
        "ajustes": {
            "S": f"{int((dt_media - servidor_time).total_seconds())}s",
            **{f"C{i+1}": f"{int((dt_media - tempos_clientes[i]).total_seconds())}s" 
               for i in range(len(tempos_clientes))}
        },
        "ordem": [c['id'] for c in clientes_ordenados]
    }
    
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)