var ros = new ROSLIB.Ros({url : "ws://" + "172.20.0.233" + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});


<!-- sis_vol -->

var sis_vol_2l = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_2l",
    messageType : "std_msgs/Float64"
});

var sis_vol_2r = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_2r",
    messageType : "std_msgs/Float64"
});

var sis_vol_3l = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_3l",
    messageType : "std_msgs/Float64"
});

var sis_vol_3r = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_3r",
    messageType : "std_msgs/Float64"
});

var sis_vol_4l = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_4l",
    messageType : "std_msgs/Float64"
});

var sis_vol_4r = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_4r",
    messageType : "std_msgs/Float64"
});

var sis_vol_5l = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_5l",
    messageType : "std_msgs/Float64"
});

var sis_vol_5r = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_5r",
    messageType : "std_msgs/Float64"
});

var sis_vol_1rl = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_1rl",
    messageType : "std_msgs/Float64"
});

var sis_vol_1ru = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_1ru",
    messageType : "std_msgs/Float64"
});

var sis_vol_1ll = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_1ll",
    messageType : "std_msgs/Float64"
});

var sis_vol_1lu = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_vol_1lu",
    messageType : "std_msgs/Float64"
});

sis_vol_2l.subscribe(function(message) {
    document.getElementById("sis_vol_2l").innerHTML = message.data;
});

sis_vol_2r.subscribe(function(message) {
    document.getElementById("sis_vol_2r").innerHTML = message.data;
});

sis_vol_3l.subscribe(function(message) {
    document.getElementById("sis_vol_3l").innerHTML = message.data;
});

sis_vol_3r.subscribe(function(message) {
    document.getElementById("sis_vol_3r").innerHTML = message.data;
});

sis_vol_4l.subscribe(function(message) {
    document.getElementById("sis_vol_4l").innerHTML = message.data;
});

sis_vol_4r.subscribe(function(message) {
    document.getElementById("sis_vol_4r").innerHTML = message.data;
});

sis_vol_5l.subscribe(function(message) {
    document.getElementById("sis_vol_5l").innerHTML = message.data;
});

sis_vol_5r.subscribe(function(message) {
    document.getElementById("sis_vol_5r").innerHTML = message.data;
});

sis_vol_1rl.subscribe(function(message) {
    document.getElementById("sis_vol_1rl").innerHTML = message.data;
});

sis_vol_1ru.subscribe(function(message) {
    document.getElementById("sis_vol_1ru").innerHTML = message.data;
});

sis_vol_1ll.subscribe(function(message) {
    document.getElementById("sis_vol_1ll").innerHTML = message.data;
});

sis_vol_1lu.subscribe(function(message) {
    document.getElementById("sis_vol_1lu").innerHTML = message.data;
})

<!-- sis_vol -->

