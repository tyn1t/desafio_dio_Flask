from flask import Flask, jsonify, request, json


app = Flask(__name__)

tarefas = [
    {
            'id':0,
            'responsavel':'Rafael',
            'tarefa':'Desenvolver método GET',
            'status':'concluido'
    },
    {
            'id':1,
            'responsavel':'Galleani',
            'tarefa':'Desenvolver método POT',
            'status':'pendente'
    }
]


#ALtera tarefa e status,tambem deleta tarefas
@app.route('/tarefa/<int:id>/', methods=['GET','PUT','DELETE'])
def tipo_tarefa(id):
        if request.method == 'GET':
                try:
                        response = tarefas[id]
                        return jsonify(response)
                except IndexError:
                        mensagem = 'Erro indexErro, Id {} invalido'.format(id)
                        response = {'Status':'Erro','Mensagem':mensagem}
                except Exception:
                        mensagem = 'Desconhecido, procure Suport'
                        response = {'Status':'Erro','Mensagem':mensagem}
                return jsonify(response)
        elif request.method == 'PUT':
                dados = json.loads(request.data)
                tarefas[id]['tarefa'] = dados
                return jsonify({'Tarefa':'Alterada como sucessor'})
        elif request.method == 'DELETE':
                for ids in range(len(tarefas)):
                        try:
                            tarefas.pop(id)
                            return jsonify({'status':'sucessor'})
                        except IndexError:
                                mensagem = 'IndexError, id {} invalidor'.format(id)
                                return jsonify({'Status': 'Erro','mensagem':mensagem})
                        except Exception:
                                mensagem = 'Erro Desconhecido Procure suport'
                                return jsonify({'Status': 'Erro','mensagem':mensagem})

                

@app.route('/tarefa/', methods=['GET', 'POST'])
def  list_tarefa():
        if  request.method == 'POST':
                dados = json.loads(request.data)
                posicao = len(tarefas)
                dados['id'] = posicao
                tarefas.append(dados)
                return jsonify(dados)
        elif request.method == 'GET':
                return jsonify(tarefas)


if  __name__ =="__main__":
    app.run(debug=True)
