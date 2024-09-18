from flask import Blueprint, request, jsonify, render_template
from .models import Contract
from .schemas import ContractSchema
from .database import db

contracts_bp = Blueprint('contracts', __name__)
contract_schema = ContractSchema()
contracts_schema = ContractSchema(many=True)

@contracts_bp.route('/')
def index():
    return render_template('index.html')

@contracts_bp.route('/contracts', methods=['POST'])
def create_contract():
    data = request.get_json()
    errors = contract_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    contract = Contract(
        contract_id=data['contract_id'],
        party_a=data['party_a'],
        party_b=data['party_b'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        terms=data['terms']
    )
    db.session.add(contract)
    db.session.commit()
    return contract_schema.jsonify(contract), 201

@contracts_bp.route('/contracts', methods=['GET'])
def get_contracts():
    contracts = Contract.query.all()
    return contracts_schema.jsonify(contracts), 200

@contracts_bp.route('/contracts/<int:id>', methods=['GET'])
def get_contract(id):
    contract = Contract.query.get_or_404(id)
    return contract_schema.jsonify(contract), 200

@contracts_bp.route('/contracts/<int:id>', methods=['PUT'])
def update_contract(id):
    contract = Contract.query.get_or_404(id)
    data = request.get_json()
    errors = contract_schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400
    
    contract.party_a = data.get('party_a', contract.party_a)
    contract.party_b = data.get('party_b', contract.party_b)
    contract.start_date = data.get('start_date', contract.start_date)
    contract.end_date = data.get('end_date', contract.end_date)
    contract.terms = data.get('terms', contract.terms)
    contract.status = data.get('status', contract.status)
    db.session.commit()
    return contract_schema.jsonify(contract), 200

@contracts_bp.route('/contracts/<int:id>', methods=['DELETE'])
def delete_contract(id):
    contract = Contract.query.get_or_404(id)
    db.session.delete(contract)
    db.session.commit()
    return '', 204
