int LIGHT_SENSOR_PIN = 35; // ESP32 pin GIOP35 (ADC0)

int motor1Pin1 = 21; 
int motor1Pin2 = 19; 
int enable1Pin = 18; 
// Setting PWM properties
const int m_freq = 10000;
const int m_pwmChannel = 0;
const int m_resolution = 8;
int ldrValue;

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    delay(10);
  }
  pinMode(LIGHT_SENSOR_PIN, INPUT);

  // sets the pins as outputs:
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);

  // configure LED PWM functionalitites
  ledcSetup(m_pwmChannel, m_freq, m_resolution);
  
  // attach the channel to the GPIO to be controlled
  ledcAttachPin(enable1Pin, m_pwmChannel);

}

void loop() {
  ldrValue = analogRead(LIGHT_SENSOR_PIN); // read the value on analog pin
    Serial.println(ldrValue);
   // We'll have a few threshholds, qualitatively determined
  if (ldrValue < 40) {
    // Stop the DC motor
    digitalWrite(motor1Pin1, LOW);
    digitalWrite(motor1Pin2, LOW);
    
    digitalWrite(motor1Pin1, LOW);
    digitalWrite(motor1Pin2, HIGH); 
    ledcWrite(m_pwmChannel, 200);

    
  }
  else if (ldrValue > 40 && ldrValue < 2000) {
    digitalWrite(motor1Pin1, HIGH);
    digitalWrite(motor1Pin2, LOW); 
    ledcWrite(m_pwmChannel, 200);   
  }
  else if (ldrValue > 2000 && ldrValue < 2800) {
    digitalWrite(motor1Pin1, LOW);
    digitalWrite(motor1Pin2, HIGH); 
    ledcWrite(m_pwmChannel, 200);   
  }
  else if (ldrValue > 2800 && ldrValue < 3600) {
    digitalWrite(motor1Pin1, LOW);
    digitalWrite(motor1Pin2, HIGH); 
    ledcWrite(m_pwmChannel, 200);   
  }
  else {
    digitalWrite(motor1Pin1, LOW);
    digitalWrite(motor1Pin2, HIGH);
    ledcWrite(m_pwmChannel, 200);   
  }
  delay(100);
}