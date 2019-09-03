if(!Listener){
    var Listener = {
        ros : null,
        name : "",
        init : function(){
            this.ros = new ROSLIB.Ros();
            this.ros.on('error', function(error) {
                document.getElementById('state').innerHTML = "Error";
            });
            this.ros.on('connection', function(error) {
                document.getElementById('state').innerHTML = "Connect";
            });
            this.ros.on('close', function(error) {
                document.getElementById('state').innerHTML = "Close";
            });
            this.ros.connect('ws://' + location.hostname + ':9000');
        }
        Listener.init();

        window.onload = function(){
        };
        window.onunload = function(){
            Listener.ros.close();
        }
    }
}


