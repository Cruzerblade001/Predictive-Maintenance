// Internal Temperature Sensor
// Example sketch for ATmega328 types.
// www.theorycircuit.com


#include <LiquidCrystal.h> // includes the LiquidCrystal Library 
LiquidCrystal lcd(12, 10, 5, 4, 3, 2); // Creates an LCD object. Parameters: (rs, enable, d4, d5, d6, d7) 

void setup()
{
  Serial.begin(9600);
  lcd.begin(16,2); // Initializes the interface to the LCD screen, and specifies the dimensions (width and height) of the display } 
  analogWrite(11,100); // Generate PWM signal at pin D11, value of 100 (out of 255)
  Serial.println(F("Internal Temperature Sensor"));
}

void loop()
{
  double temperature = GetTemp(); // Get temperature value
  Serial.println(temperature); // Send temperature value over serial
  delay(1000);
  
  if (Serial.available() > 0) 
  {
    String data = Serial.readStringUntil('\n');
    //Serial.print("You sent me: ");
    //Serial.println(data);
    lcd.print(data);   // Prints data on the LCD 
    delay(5000);      //  5 sec delay 
    lcd.clear();     // Clears the LCD screen 
  }
}

double GetTemp(void)
{
  unsigned int wADC;
  double t;

  // The internal temperature has to be used
  // with the internal reference of 1.1V.
  // Channel 8 can not be selected with the analogRead function yet.

  // Set the internal reference and mux.
  ADMUX = (_BV(REFS1) | _BV(REFS0) | _BV(MUX3));
  ADCSRA |= _BV(ADEN);  // enable the ADC

  delay(20);            // wait for voltages to become stable.

  ADCSRA |= _BV(ADSC);  // Start the ADC

  // Detect end-of-conversion
  while (bit_is_set(ADCSRA,ADSC));

  // Reading register "ADCW" takes care of how to read ADCL and ADCH.
  wADC = ADCW;

  // The offset of 324.31 could be wrong. It is just an indication.
  t = (wADC - 324.31 ) / 1.22;
  t = t + 273; // Convert to degree Kelvin
  // The returned temperature is in degrees Kelvin.
  return (t);
}
