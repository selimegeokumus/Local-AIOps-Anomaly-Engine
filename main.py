import json
import time
import requests
from kafka import KafkaConsumer, KafkaProducer

# Kafka / Redpanda Bağlantısı
KAFKA_SERVER = 'localhost:9092'
TOPIC_NAME = 'system-logs'

# Ollama AI Servis Bağlantısı
OLLAMA_URL = 'http://localhost:11434/api/generate'

def analyze_with_ai(log_message):
    print("\n⚠️ [KRİTİK HATA ALGILANDI] Yapay Zeka Kök Neden Analizi Yapıyor...")
    
    prompt = f"""You are a Senior DevOps Engineer. Analyze this critical system log and give a 2-bullet-point root cause analysis and action plan in plain English:
Log: {log_message}"""

    payload = {
        "model": "qwen2.5:1.5b",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        ai_comment = response.json().get('response', 'No response from AI.')
        print("🤖 [AI ANALİZİ VE ÇÖZÜM ÖNERİSİ]:")
        print(ai_comment)
        print("-" * 50)
    except Exception as e:
        print(f"AI Analiz Hatası: {e}")

def run_engine():
    print("🚀 AIOps Anomaly Engine Başlatıldı... Loglar Dinleniyor...")
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=[KAFKA_SERVER],
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        log = message.value
        print(f"📥 [LOG GELDİ]: [{log['level']}] - {log['message']}")
        
        # Eğer log seviyesi ERROR veya CRITICAL ise yapay zekaya gönder
        if log['level'] in ['ERROR', 'CRITICAL']:
            analyze_with_ai(log['message'])

if __name__ == '__main__':
    run_engine()