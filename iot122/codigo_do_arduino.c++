#include <SPI.h>
#include <Ethernet.h>
#include <Ultrasonic.h>
#include <DHT.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// LCD I2C
LiquidCrystal_I2C lcd(0x27, 16, 2); // Endereço comum: 0x27

// Rede
byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x0B};
IPAddress ip(192, 168, 1, 178);
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

// LCD alternância
unsigned long lastLcdUpdate = 0;
const unsigned long lcdInterval = 2000;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("Inicializando...");

  Ethernet.begin(mac, ip);
  server.begin();

  dht.begin();

  // LCD
  lcd.init();
  lcd.backlight();

  Serial.println("Servidor iniciado");
}

void loop() {
  // Exibição cíclica no LCD
  if (millis() - lastLcdUpdate >= lcdInterval) {
    lastLcdUpdate = millis();
    lcd.clear();

    // Se o sensor ultrassônico estiver ligado, mostra a distância
    if (ultrassonicLigado) {
      long distance = ultrasonic.read();
      lcd.setCursor(0, 0);
      lcd.print("Ultrassônico:");
      lcd.setCursor(0, 1);
      lcd.print("Ligado  ");
      lcd.print(distance);
      lcd.print(" cm");
    } 
    // Se o sensor DHT11 estiver ligado, mostra a temperatura e umidade
    else if (dhtLigado) {
      float h = dht.readHumidity();
      float t = dht.readTemperature();

      if (isnan(h) || isnan(t)) {
        lcd.setCursor(0, 0);
        lcd.print("Erro DHT");
        lcd.setCursor(0, 1);
        lcd.print("Falha na leitura");
      } else {
        lcd.setCursor(0, 0);
        lcd.print("DHT11:");
        lcd.setCursor(0, 1);
        lcd.print("Ligado  ");
        lcd.print(t);
        lcd.print(" C");
        lcd.setCursor(10, 1);
        lcd.print(h);
        lcd.print(" %");
      }
    } 
    else {
      lcd.setCursor(0, 0);
      lcd.print("LED:");
      lcd.setCursor(0, 1);
      lcd.print(digitalRead(LED) == HIGH ? "Ligado" : "Desligado");
    }
  }

  // Rede
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
      dhtLigado = false;  // Desliga o DHT ao ligar o ultrassônico
      long distance = ultrasonic.read();
      Serial.println("Sensor ultrassônico ativado.");
      client.println(distance);
    } else if (cmd == "temperatura") {
      dhtLigado = true;
      ultrassonicLigado = false;  // Desliga o ultrassônico ao ligar o DHT
      float t = dht.readTemperature();
      Serial.println("Sensor DHT ativado.");
      client.println(t);
    }

    client.stop();
  }
}
