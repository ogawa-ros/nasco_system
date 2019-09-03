var ros = new ROSLIB.Ros({url : "ws://" + "172.20.0.233" + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});


<!-- hemt_id -->

var hemt_2l_id = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_2l_id",
    messageType : "std_msgs/Float64"
});

var hemt_2r_id = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_2r_id",
    messageType : "std_msgs/Float64"
});

var hemt_3l_id = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_3l_id",
    messageType : "std_msgs/Float64"
});

var hemt_3r_id = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_3r_id",
    messageType : "std_msgs/Float64"
});

var hemt_4l_id = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_4l_id",
    messageType : "std_msgs/Float64"
});

var hemt_4r_id = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_4r_id",
    messageType : "std_msgs/Float64"
});

var hemt_5l_id = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_5l_id",
    messageType : "std_msgs/Float64"
});

var hemt_5r_id = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_5r_id",
    messageType : "std_msgs/Float64"
});

hemt_2l_id.subscribe(function(message) {
    document.getElementById("hemt_2l_id").innerHTML = (message.data).toFixed(3);
});

hemt_2r_id.subscribe(function(message) {
    document.getElementById("hemt_2r_id").innerHTML = (message.data).toFixed(3);
});

hemt_3l_id.subscribe(function(message) {
    document.getElementById("hemt_3l_id").innerHTML = (message.data).toFixed(3);
});

hemt_3r_id.subscribe(function(message) {
    document.getElementById("hemt_3r_id").innerHTML = (message.data).toFixed(3);
});

hemt_4l_id.subscribe(function(message) {
    document.getElementById("hemt_4l_id").innerHTML = (message.data).toFixed(3);
});

hemt_4r_id.subscribe(function(message) {
    document.getElementById("hemt_4r_id").innerHTML = (message.data).toFixed(3);
});

hemt_5l_id.subscribe(function(message) {
    document.getElementById("hemt_5l_id").innerHTML = (message.data).toFixed(3);
});

hemt_5r_id.subscribe(function(message) {
    document.getElementById("hemt_5r_id").innerHTML = (message.data).toFixed(3);
});

<!-- hemt_id -->
