var bleno = require('bleno');
var exec = require('child_process').exec;

function checkWifiConnection(callback) {
  exec('iwgetid -r', function(error, stdout, stderr) {
    if (error) {
      console.log('Error checking WiFi connection: ' + error);
    } else {
      callback(stdout.trim().length > 0);  // WiFi name is printed if connected.
    }
  });
}

function runScripts() {
  exec('sudo docker exec -it yolo_container python3 tem.py');
  exec('sudo docker exec -it yolo_container python3 light.py');
}

checkWifiConnection(function(connected) {
  if (connected) {
    runScripts();
  }
});

bleno.on('stateChange', function(state) {
  console.log('State change: ' + state);
  if (state === 'poweredOn') {
    bleno.startAdvertising('WiFiConfig', ['12ab']);
  } else {
    bleno.stopAdvertising();
  }
});

bleno.on('advertisingStart', function(error) {
  console.log('Advertising start: ' + (error ? 'error ' + error : 'success'));
  if (!error) {
    bleno.setServices([
      new bleno.PrimaryService({
        uuid: '12ab',
        characteristics: [
          new bleno.Characteristic({
            uuid: '34cd',
            properties: ['write'],
            onWriteRequest: function(data, offset, withoutResponse, callback) {
              var wifiConfig = data.toString().split(',');
              var ssid = wifiConfig[0];
              var password = wifiConfig[1];
              console.log('Received WiFi config: ' + ssid + ', ' + password);
              exec('nmcli dev wifi con ' + ssid + ' password ' + password, function(error, stdout, stderr) {
                console.log('WiFi config change result: ' + (error ? 'error ' + error : 'success'));
                checkWifiConnection(function(connected) {
                  if (connected) {
                    runScripts();
                  } else {
                    console.log('WiFi connection failed.');
                  }
                });
              });
              callback(this.RESULT_SUCCESS);
            }
          })
        ]
      })
    ]);
  }
});
