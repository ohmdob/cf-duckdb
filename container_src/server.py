import logging
from flask import Flask, jsonify
import duckdb
from pathlib import Path

app = Flask(__name__)


@app.route('/barcode/<barcode>', methods=['GET'])
def barcode(barcode):
    try:
        conn = duckdb.connect(database=':memory:')
        query = f"SELECT * FROM read_parquet('barcode_th.parquet') WHERE code = '{barcode}' LIMIT 1"
        cursor = conn.execute(query)
        columns = [desc[0] for desc in cursor.description]
        result = cursor.fetchone()
        
        if not result:
            return jsonify({'message': "Can't detect barcode"}), 404
        conn.close()
        return jsonify(dict(zip(columns, result)))
    except Exception as e:
        logging.exception('Barcode failed')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
