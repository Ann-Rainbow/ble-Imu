/*****************************************************************************/
/*INCLUDES                                                                   */
/*****************************************************************************/
#include "Arduino.h"
/* For the bluetooth funcionality */
#include <ArduinoBLE.h>
/* For the use of the IMU sensor */
#include "Nano33BLEAccelerometer.h"
#include "Nano33BLEGyroscope.h"
/* For Kalman Filter */
#include "GyverFilters.h"
/*****************************************************************************/
/*MACROS                                                                     */
/*****************************************************************************/
/* 
 * We use strings to transmit the data via BLE, and this defines the buffer
 * size used to transmit these strings. Only 20 bytes of data can be 
 * transmitted in one packet with BLE, so a size of 20 is chosen the the data 
 * can be displayed nicely in whatever application we are using to monitor the
 * data.
 */
#define BLE_BUFFER_SIZES             20
/* Device name which can be scene in BLE scanning software. */
#define BLE_DEVICE_NAME                "Arduino Nano 33 BLE Sense"
/* Local name which should pop up when scanning for BLE devices. */
#define BLE_LOCAL_NAME                "Accelerometer And Gyro BLE"

/*****************************************************************************/
/*GLOBAL Data                                                                */
/*****************************************************************************/
/* 
 * Nano33BLEAccelerometerData object which we will store data in each time we read
 * the accelerometer data. 
 */ 
Nano33BLEAccelerometerData accelerometerData;
Nano33BLEGyroscopeData gyroscopeData;

/* 
 * Declares the BLEService and characteristics we will need for the BLE 
 * transfer. The UUID was randomly generated using one of the many online 
 * tools that exist. It was chosen to use BLECharacteristic instead of 
 * BLEFloatCharacteristic was it is hard to view float data in most BLE 
 * scanning software. Strings can be viewed easiler enough. In an actual
 * application you might want to transfer floats directly.
 */
 
BLEService BLEAccelerometerAndGyro("590d65c7-3a0a-4023-a05a-6aaf2f22441c");
BLECharacteristic accelerometerXBLE("84b8e0b2-9778-42de-89ea-0b44bb363c34", BLERead | BLENotify | BLEBroadcast, BLE_BUFFER_SIZES);
BLECharacteristic accelerometerYBLE("db8b6744-e800-40d3-8aec-e6b13ba851e8", BLERead | BLENotify | BLEBroadcast, BLE_BUFFER_SIZES);
BLECharacteristic accelerometerZBLE("b65eff6d-ff7f-45d6-b1b5-6c8b0e2f1770", BLERead | BLENotify | BLEBroadcast, BLE_BUFFER_SIZES);
BLECharacteristic gyroscopeXBLE("3b18a65e-26c7-4c83-b8e2-bd11c06650ee", BLERead | BLENotify | BLEBroadcast, BLE_BUFFER_SIZES);
BLECharacteristic gyroscopeYBLE("1dd4e426-0296-4535-8b20-fac505767d39", BLERead | BLENotify | BLEBroadcast, BLE_BUFFER_SIZES);
BLECharacteristic gyroscopeZBLE("0c1697bd-dc8e-4620-9a4e-9642012311d8", BLERead | BLENotify | BLEBroadcast, BLE_BUFFER_SIZES);
//BLEByteCharacteristic gyroChar("cc74194b-5bda-48fb-9c13-7d7856901a81", BLERead | BLENotify | BLEBroadcast);
//BLEByteCharacteristic accelChar("afdabf98-f498-4313-8dd0-9762238deac0", BLERead | BLENotify | BLEBroadcast);


/* Kalman Filter */
GKalman acXFilter(40, 40, 0.5);
GKalman acYFilter(40, 40, 0.5);
GKalman acZFilter(40, 40, 0.5);
GKalman gyroXFilter(40, 40, 0.5);
GKalman gyroYFilter(40, 40, 0.5);
GKalman gyroZFilter(40, 40, 0.5);
/* Common global buffer will be used to write to the BLE characteristics. */
char bleBuffer[BLE_BUFFER_SIZES];
//int led = 13; // написала

/*****************************************************************************/
/*SETUP (Initialisation)                                                     */
/*****************************************************************************/
void setup()
{
    /* 
     * Serial setup. This will be used to transmit data for viewing on serial 
     * plotter 
     */
    Serial.begin(115200);
    //pinMode(led, OUTPUT); //написала
    while(!Serial);


    /* BLE Setup. For information, search for the many ArduinoBLE examples.*/
    if (!BLE.begin()) 
    {
        while (1);    
    }
    else
    {
        BLE.setDeviceName(BLE_DEVICE_NAME);
        BLE.setLocalName(BLE_LOCAL_NAME);
        BLE.setAdvertisedService(BLEAccelerometerAndGyro);
        /* A seperate characteristic is used for each X, Y, and Z axis. */
        BLEAccelerometerAndGyro.addCharacteristic(accelerometerXBLE);
        BLEAccelerometerAndGyro.addCharacteristic(accelerometerYBLE);
        BLEAccelerometerAndGyro.addCharacteristic(accelerometerZBLE);
        /* A seperate characteristic is used for each X, Y, and Z axis of GyroScope*/
        BLEAccelerometerAndGyro.addCharacteristic(gyroscopeXBLE);
        BLEAccelerometerAndGyro.addCharacteristic(gyroscopeYBLE);
        BLEAccelerometerAndGyro.addCharacteristic(gyroscopeZBLE);
        
        BLE.addService(BLEAccelerometerAndGyro);
        BLE.advertise();
        /* 
         * Initialises the IMU sensor, and starts the periodic reading of the 
         * sensor using a Mbed OS thread. The data is placed in a circular 
         * buffer and can be read whenever.
         */
        Accelerometer.begin();
        Gyroscope.begin();

        /* Plots the legend on Serial Plotter */
        Serial.println("X, Y, Z");
    }
}

/*****************************************************************************/
/*LOOP (runtime super loop)                                                  */
/*****************************************************************************/
void loop()
{
    //digitalWrite(led, HIGH); // написала
    //delay(1000); //написала
    //digitalWrite(led, LOW); // написала
    //delay(1000); //написала
    
    BLEDevice central = BLE.central();
    if(central)
    {
        int writeLength;
        /* 
         * If a BLE device is connected, accelerometer data will start being read, 
         * and the data will be written to each BLE characteristic. The same 
         * data will also be output through serial so it can be plotted using 
         * Serial Plotter. 
         */
        while(central.connected())
        {            
            if(Accelerometer.pop(accelerometerData))
            {
                float ax = acXFilter.filtered(accelerometerData.x);
                float ay = acYFilter.filtered(accelerometerData.y);
                float az = acZFilter.filtered(accelerometerData.z);
                writeLength = sprintf(bleBuffer, "%f", ax);
                accelerometerXBLE.writeValue(bleBuffer, writeLength); 
                writeLength = sprintf(bleBuffer, "%f", ay);
                accelerometerYBLE.writeValue(bleBuffer, writeLength);      
                writeLength = sprintf(bleBuffer, "%f", az);
                accelerometerZBLE.writeValue(bleBuffer, writeLength);      

                Serial.printf("%f,%f,%f\r\n", ax, ay, az); //   txChar.writeValue - вставляла, не работает
            }
            
            if(Gyroscope.pop(gyroscopeData))
            {
                float gx = gyroXFilter.filtered(gyroscopeData.x);
                float gy = gyroYFilter.filtered(gyroscopeData.y);
                float gz = gyroZFilter.filtered(gyroscopeData.z);
                writeLength = sprintf(bleBuffer, "%f", gx);
                gyroscopeXBLE.writeValue(bleBuffer, writeLength); 
                writeLength = sprintf(bleBuffer, "%f", gy);
                gyroscopeYBLE.writeValue(bleBuffer, writeLength);      
                writeLength = sprintf(bleBuffer, "%f", gz);
                gyroscopeZBLE.writeValue(bleBuffer, writeLength);      

                // Serial.printf("%f,%f,%f\r\n", gx, gy, gz); //   txChar.writeValue - вставляла, не работает
            }
        }
    }  else {
       setup();
    }
}
    
