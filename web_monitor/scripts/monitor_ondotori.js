var ros = new ROSLIB.Ros({url : "ws://" + "172.20.0.233" + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});

var tr71w_1_temp_ch1 = new ROSLIB.Topic({
    ros : ros,
    name : "/tr71w_1_temp_ch1",
    messageType : "std_msgs/Float64"
});

var tr71w_2_temp_ch1 = new ROSLIB.Topic({
    ros : ros,
    name : "tr71w_2_temp_ch1",
    messageType : "std_msgs/Float64"
});

var tr71w_3_temp_ch1 = new ROSLIB.Topic({
    ros : ros,
    name : "tr71w_3_temp_ch1",
    messageType : "std_msgs/Float64"
});


tr71w_1_temp_ch1.subscribe(function(message) {
    document.getElementById("tr71w_1_temp_ch1").innerHTML = (message.data);
});

tr71w_2_temp_ch1.subscribe(function(message) {
    document.getElementById("tr71w_2_temp_ch1").innerHTML = (message.data);
});

tr71w_3_temp_ch1.subscribe(function(message) {
    document.getElementById("tr71w_3_temp_ch1").innerHTML = (message.data);
});



