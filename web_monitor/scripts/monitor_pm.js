var ros = new ROSLIB.Ros({url : "ws://" + IP_rxobs + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});

var power_1 = new ROSLIB.Topic({
    ros : ros,
    name : "/power_1_web",
    messageType : "std_msgs/Float64"
});

var lakeshore_ch2 = new ROSLIB.Topic({
    ros : ros,
    name : "/power_2_web",
    messageType : "std_msgs/Float64"
});

power_1.subscribe(function(message) {
    document.getElementById("power_1").innerHTML = (message.data);
});

power_2.subscribe(function(message) {
    document.getElementById("power_2").innerHTML = (message.data);
});
