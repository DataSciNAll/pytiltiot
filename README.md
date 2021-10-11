# pytiltiot
Azure IoT Hub connectivity

Cloned and rebuilt repo from atlefren/pytilt.  Key contributions are connectivity to Azure IoT Hub.  Future contribution will add ARM templates to build out Azure services and data pipelines and dashboards to view content similar to Pytilt content.

Setup Installation
------------
0. Install git ```sudo apt-get install git```
1. git clone https://github.com/DataSciNAll/pytiltiot.git
2. Install python-bluez: ```sudo apt-get install python-bluez```
3. Make the bluetooth interface accessible witout being root: ```sudo setcap cap_net_raw+eip /usr/bin/python2.7```
4. Install Azure CLI onto device: ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```
5. Create IoT Hub in Azure: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-raspberry-pi-kit-node-get-started#create-an-iot-hub
6. Register device to IoT Hub: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-raspberry-pi-kit-node-get-started#register-a-new-device-in-the-iot-hub
7. Copy Device Connection string and add it to pytilt.service file as ```PYTILT_CONN_STR```: https://devblogs.microsoft.com/iotdev/understand-different-connection-strings-in-azure-iot-hub/#iothubdeviceconn

Running
-----------
0. From the directory containing pytilt.py run `python pytilt.py`

Running Pytilt in the background and on System Start
-----------
0. edit pytilt.service, add your key and fix paths
1. copy pytilt.service to /lib/systemd/system/
2. sudo chmod 644 /lib/systemd/system/pytilt.service
3. sudo systemctl daemon-reload
4. sudo systemctl enable pytilt.service
5. Edit your bash profile by running ```nano .bash_profile``` 
6. Enter your iot device connction string as ```export PYTILT_CONN_STR='<enter connection string here>' exit and save.
8. sudo reboot
9. Reconnect to the device and run ```echo $PYTLT_CONN_STR``` to ensure the environment variable is set.


Acknowledgements
----------------
The code in blescan-py is adapted from https://github.com/switchdoclabs/iBeacon-Scanner-
The Tilt UUID-to-color mapping is taken from: https://github.com/tbryant/brewometer-nodejs
Systemd-config here: http://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/
Cloned repo and refactor it for Azure IoT connectivity from: https://github.com/atlefren/pytilt

[1]: https://tilthydrometer.com/

Testing Webhook
