from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql

# Usar PyMySQL como driver
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# Configuração do banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Vini12348@localhost:3306/loja'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definição do modelo Produto
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    fornecedor = db.Column(db.String(100), nullable=False)
    endereco_fornecedor = db.Column(db.String(200), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)

def produto_to_dict(produto):
    return {
        'id': produto.id,
        'nome': produto.nome,
        'fornecedor': produto.fornecedor,
        'endereco_fornecedor': produto.endereco_fornecedor,
        'quantidade': produto.quantidade,
        'endereco': produto.endereco,
        'preco_unitario': produto.preco_unitario
    }

# Rota para testar a conexão com o banco de dados
@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        db.session.execute('SELECT 1')
        return jsonify({'status': 'Conexão com o banco bem-sucedida'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota para listar todos os produtos
@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    print("Produtos encontrados:", produtos)  # Veja se produtos estão sendo retornados no terminal
    return jsonify([produto_to_dict(produto) for produto in produtos])

# Rota para adicionar um novo produto
@app.route('/produtos', methods=['POST'])
def add_produto():
    data = request.get_json()
    novo_produto = Produto(
        nome=data['nome'],
        fornecedor=data['fornecedor'],
        endereco_fornecedor=data['endereco_fornecedor'],
        quantidade=data['quantidade'],
        endereco=data['endereco'],
        preco_unitario=data['preco_unitario']
    )
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify(produto_to_dict(novo_produto)), 201

# Rota para atualizar um produto pelo ID
@app.route('/produtos/<int:id>', methods=['PUT'])
def update_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
    data = request.get_json()
    produto.nome = data['nome']
    produto.fornecedor = data['fornecedor']
    produto.endereco_fornecedor = data['endereco_fornecedor']
    produto.quantidade = data['quantidade']
    produto.endereco = data['endereco']
    produto.preco_unitario = data['preco_unitario']
    
    db.session.commit()
    return jsonify(produto_to_dict(produto))

# Rota para excluir um produto pelo ID
@app.route('/produtos/<int:id>', methods=['DELETE'])
def delete_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
    db.session.delete(produto)
    db.session.commit()
    return '', 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
