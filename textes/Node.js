const Client = require('ssh2').Client;

const conn = new Client();
conn.on('ready', function() {
  console.log('Conexão estabelecida com sucesso!');
  conn.exec('comando no Raspberry Pi', function(err, stream) {
    if (err) throw err;
    stream.on('close', function(code, signal) {
      console.log('Comando executado com sucesso!');
      conn.end();
    }).on('data', function(data) {
      console.log('Resultado: ' + data);
    }).stderr.on('data', function(data) {
      console.log('Erro: ' + data);
    });
  });
}).connect({
  host: '192.168.1.89',
  port: 3000,
  username: 'joao41',
  password: '852963134'
});