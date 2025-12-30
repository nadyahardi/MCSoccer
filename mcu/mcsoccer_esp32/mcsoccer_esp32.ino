#include <PS4Controller.h>

#define IN1 19
#define IN2 18
#define ENA 23 
#define IN3 33
#define IN4 32
#define ENB 25 

#define FREQ 5000
#define RES 8

//use sixasix and getmac
char* mac_address = "14:2B:2F:DB:11:F2"; 

void setup() {
  Serial.begin(115200);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT); pinMode(ENA, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT); pinMode(ENB, OUTPUT);
  
  ledcAttach(ENA, FREQ, RES);
  ledcAttach(ENB, FREQ, RES);

  PS4.begin(mac_address);
  Serial.println("ready, waitiing for PS4");
}

void loop() {
  if (PS4.isConnected()) {
    int ly = PS4.LStickY(); 
    int lx = PS4.LStickX();
    if (abs(lx) < 10) lx = 0; if (abs(ly) < 10) ly = 0;

    int forward = -map(ly, -128, 127, -255, 255); 
    int turn    = map(lx, -128, 127, -255, 255);

    int leftSpeed  = constrain(forward + turn, -255, 255);
    int rightSpeed = constrain(forward - turn, -255, 255);

    controlMotor(IN1, IN2, ENA, leftSpeed);
    controlMotor(IN3, IN4, ENB, rightSpeed);
  } else {
    controlMotor(IN1, IN2, ENA, 0);
    controlMotor(IN3, IN4, ENB, 0);
  }
}

void controlMotor(int pinIn1, int pinIn2, int pinEn, int speed) {
  int pwmValue = abs(speed);
  if (speed > 0) { digitalWrite(pinIn1, HIGH); digitalWrite(pinIn2, LOW); }
  else if (speed < 0) { digitalWrite(pinIn1, LOW); digitalWrite(pinIn2, HIGH); }
  else { digitalWrite(pinIn1, LOW); digitalWrite(pinIn2, LOW); pwmValue = 0; }
  ledcWrite(pinEn, pwmValue);
}
