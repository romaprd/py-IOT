#include <SPI.h>
#include <Ethernet.h>
#include <Ultrasonic.h>
#include <DHT.h>

// Configuração da rede
byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x0B};
IPAddress ip(192, 168, 1, 178); // IP fixo
EthernetServer server(5000);

// LED
const int LED = 7;

// Ultrassônico
const int triggerPin = 4;
const int echoPin = 5;
Ultrasonic ultrasonic(triggerPin, echoPin);
unsigned long lastReadTime = 0;
const unsigned long readInterval = 1000;
bool ultrassonicLigado = false;

// DHT11
#define DHTPIN A1
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
bool dhtLigado = false;
unsigned long lastDhtReadTime = 0;
const unsigned long dhtInterval = 2000;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("Inicializando...");

  Ethernet.begin(mac, ip);
  server.begin();

  dht.begin();

  Serial.println("Servidor iniciado");
}

void loop() {
  EthernetClient client = server.available();
  if (client) {
    String cmd = client.readStringUntil('\n');
    cmd.trim();

    if (cmd == "ligar") {
      digitalWrite(LED, HIGH);
      client.println("led ligado\n");

    } else if (cmd == "desligar") {
      digitalWrite(LED, LOW);
      client.println("led desligado\n");

    } else if (cmd == "distancia") {
      ultrassonicLigado = true;
      Serial.println("Sensor ultrassônico ativado.");

      if (millis() - lastReadTime >= readInterval) {
        lastReadTime = millis();
        long distance = ultrasonic.read();
        Serial.print("Distância em cm: ");
        Serial.println(distance);
        client.println(distance);
      }

    } else if (cmd == "temperatura") {
      dhtLigado = true;
      Serial.println("Sensor DHT ativado.");

      if (millis() - lastDhtReadTime >= dhtInterval) {
        lastDhtReadTime = millis();

        float h = dht.readHumidity();
        float t = dht.readTemperature();

        if (isnan(h) || isnan(t)) {
          Serial.println("Falha na leitura do DHT");
          client.println("Erro ao ler DHT");
        } else {
          Serial.print("Umidade: ");
          Serial.print(h);
          Serial.print(" %\tTemperatura: ");
          Serial.print(t);
          Serial.println(" *C");

          client.print(t);
          client.println(" *C");
        }
      }
    }

    client.stop();
  }
}
