#include <MQ131.h>

void setup() {
  Serial.begin(115200);
  MQ131.begin(2,A0, LOW_CONCENTRATION, 1000000);
  Serial.println("Calibrating");
  MQ131.calibrate();
  Serial.println("Done");
}

void loop() {
  MQ131.sample();
  Serial.print("Concentration O3 : ");
  Serial.print(MQ131.getO3(PPB));
  Serial.println(" ppb");
  delay(60000);
}
