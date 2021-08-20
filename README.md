# pytiltiot
Azure IoT Hub connectivity

Cloned and rebuilt repo from atlefren/pytilt.  Key contributions are connectivity to Azure IoT Hub.  Future contribution will add ARM templates to build out Azure services and data pipelines and dashboards to view content similar to Pytilt content.

Setup Installation
------------
0. git clone https://github.com/DataSciNAll/pytiltiot.git
1. Install python-bluez: ```sudo apt-get install python-bluez```
2. Make the bluetooth interface accessible witout being root: ```sudo setcap cap_net_raw+eip /usr/bin/python2.7```
3. Install Azure CLI onto device: ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```
4. Create IoT Hub in Azure: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-raspberry-pi-kit-node-get-started#create-an-iot-hub
5. Register device to IoT Hub: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-raspberry-pi-kit-node-get-started#register-a-new-device-in-the-iot-hub
6. Copy Device Connection string and add it to pytilt.service file as ```PYTILT_CONN_STR```: https://devblogs.microsoft.com/iotdev/understand-different-connection-strings-in-azure-iot-hub/#iothubdeviceconn

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
5. sudo reboot


Acknowledgements
----------------
The code in blescan-py is adapted from https://github.com/switchdoclabs/iBeacon-Scanner-
The Tilt UUID-to-color mapping is taken from: https://github.com/tbryant/brewometer-nodejs
Systemd-config here: http://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/
Cloned repo and refactor it for Azure IoT connectivity from: https://github.com/atlefren/pytilt

[1]: https://tilthydrometer.com/