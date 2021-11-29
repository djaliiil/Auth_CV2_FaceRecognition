let {PythonShell} = require('python-shell')
var path = require("path")
var electron = require('electron')



function registration() {
var nom = document.getElementById('nomr').value,
    prenom = document.getElementById('prenomr').value,
    naiss = document.getElementById('naissancer').value,
    email = document.getElementById('emailr').value,
    sexe = document.getElementById("sexer").value;


  var spawn = require('child_process').spawn;
  var python  = spawn('python', ['./engine/register.py', nom, prenom, naiss, email, sexe]);

    python.stdout.on('data',function(data){
      console.log("data: ",data.toString('utf8'));
    });

}


function connection() {

  var spawn = require('child_process').spawnSync;
  var python  = spawn('python', ['./engine/connect.py']);
  console.log(python);

if (python.status !== 0) {
    process.stderr.write(python.stderr);
    process.exit(python.status);
  }
else {
    const {ipcRenderer} = require('electron');
      ipcRenderer.send('Am_I_Ready',"Im ready");

    process.stdout.write(python.stdout);
    process.stderr.write(python.stderr);
  }

}
