from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SOURCE_API = "https://osint-num-info.gauravcyber0.workers.dev/"

CUSTOM_SELLER = "@xhamsterpaglu"
MY_CHANNEL = "@nightfallhub69"

@app.route("/Get", methods=["GET"])
def num_info():
    mobile = request.args.get("mobile")

    if not mobile or not mobile.isdigit() or len(mobile) != 10:
        return jsonify({
            "success": False,
            "message": "Invalid mobile number"
        }), 400

    try:
        r = requests.get(SOURCE_API, params={"mobile": mobile}, timeout=10)
        data = r.json()

        # remove original seller
        data.pop("seller", None)
        data.pop("API SELL BY", None)
        data.pop("api_seller", None)

        # add your branding
        data["seller"] = CUSTOM_SELLER
        data["channel"] = MY_CHANNEL

        return jsonify({
            "success": True,
            "data": data
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# ❌ app.run() MAT likhna (Vercel serverless hai)
