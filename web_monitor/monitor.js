var ros = new ROSLIB.Ros({url : "ws://" + "192.168.100.236" + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});

var sis_vol_2l = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_2l",
    messageType : "std_msgs/Float64"
});

sis_vol_2l.subscribe(function(message) {
    document.getElementById("sis_vol_2l").innerHTML = message.data
}
