var bleno = require('bleno');
var exec = require('child_process').exec;

function checkWifiConnection(callback) {
  exec('iwgetid -r', function(error, stdout, stderr) {
    if (error) {
      console.log('Error checking WiFi connection: ' + error);
      callback(false);
    } else {
      callback(stdout.trim().length > 0);  // 와이파이 이름이 출력되면 연결된 상태로 판단합니다.
    }
  });
}

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
                    exec('sudo docker exec -it container_name python3 /path/to/tem.py');
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
