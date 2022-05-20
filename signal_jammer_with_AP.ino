#include <ESP8266WebServer.h>
#include <ELECHOUSE_CC1101_SRC_DRV.h>

#ifndef APSSID
#define APSSID "ESPap"     //Define access point name
#define APPSK  "123456789" //Define access point passcode
#endif

const char *ssid = APSSID;
const char *password = APPSK;

int gdo0;

void setup() {
    Serial.print("Configuring access point...");
    WiFi.softAP(ssid); //Start the access point, leaving it open, can add pass if needed
    Serial.print("Access point started");

    gdo0 = 5;  // Change gdo0 pin if using esp32 or arduino

    if (ELECHOUSE_cc1101.getCC1101()){         // Check the CC1101 Spi connection.
    Serial.println("Connection OK");
    }else{
    Serial.println("Connection Error");
    }
  
    ELECHOUSE_cc1101.Init();               // initialize the cc1101!
    ELECHOUSE_cc1101.setGDO0(gdo0);       // set lib internal gdo pin (gdo0)
    ELECHOUSE_cc1101.setCCMode(1);       // set config for internal transmission mode.
    ELECHOUSE_cc1101.setModulation(0);  // set modulation mode. 0 = 2-FSK, 1 = GFSK, 2 = ASK/OOK, 3 = 4-FSK, 4 = MSK.
    ELECHOUSE_cc1101.setMHZ(430);      // Here you can set your basic frequency. The lib calculates the frequency automatically (default = 433.92).The cc1101 can: 300-348 MHZ, 387-464MHZ and 779-928MHZ. Read More info from datasheet.
    ELECHOUSE_cc1101.setSyncMode(2);  // Combined sync-word qualifier mode. 0 = No preamble/sync. 1 = 16 sync word bits detected. 2 = 16/16 sync word bits detected. 3 = 30/32 sync word bits detected. 4 = No preamble/sync, carrier-sense above threshold. 5 = 15/16 + carrier-sense above threshold. 6 = 16/16 + carrier-sense above threshold. 7 = 30/32 + carrier-sense above threshold.
    // ELECHOUSE_cc1101.setPA(10);   // set TxPower. The following settings are possible depending on the frequency band.  (-30  -20  -15  -10  -6    0    5    7    10   11   12) Default is max!
    ELECHOUSE_cc1101.setCrc(1);     // 1 = CRC calculation in TX and CRC check in RX enabled. 0 = CRC disabled for TX and RX.
    Serial.println("CC1101 Initiated");
}
void loop() {

    if ((WiFi.softAPgetStationNum()) !=0){ //Start jamming when client connects to the wifi

        ELECHOUSE_cc1101.setMHZ(433.5); //Jamming Frequency
        ELECHOUSE_cc1101.SendData("11111111");
        ELECHOUSE_cc1101.setMHZ(434); // Jamming Frequency
        ELECHOUSE_cc1101.SendData("11111111");
    }
}
