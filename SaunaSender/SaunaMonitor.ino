#include "DHT.h"

// the pin number of DHT22 data pin in arduino
#define DHTPIN 2     // what pin we're connected to

#define DHTTYPE DHT22   // DHT 22  (AM2302)

boolean debug=true;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(57600); 
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // check if returns are valid, if they are NaN (not a number) then something went wrong!
  if (isnan(t) || isnan(h)) {
    Serial.println("Failed to read temperature");
  } else {
    if( debug ){
      Serial.print("Humidity: "); 
      Serial.print(h);
      Serial.print(" %\t");
      Serial.print("Temperature: "); 
      Serial.print(t);
      Serial.println(" *C");
    }
    else {
      Serial.print(t);
    }
  }
  
  delay( 3000 );
}
