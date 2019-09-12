var ros = new ROSLIB.Ros({url : "ws://" + "172.20.0.237" + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});


<!-- loatt -->

var loatt_2l = new ROSLIB.Topic({
    ros : ros,
    name : "/loatt_2l",
    messageType : "std_msgs/Float64"
});

var loatt_2r = new ROSLIB.Topic({
    ros : ros,
    name : "/loatt_2r",
    messageType : "std_msgs/Float64"
});

var loatt_3l = new ROSLIB.Topic({
    ros : ros,
    name : "/loatt_3l",
    messageType : "std_msgs/Float64"
});

var loatt_3r = new ROSLIB.Topic({
    ros : ros,
    name : "/loatt_3r",
    messageType : "std_msgs/Float64"
});

var loatt_4l = new ROSLIB.Topic({
    ros : ros,
    name : "/loatt_4l",
    messageType : "std_msgs/Float64"
});

var loatt_4r = new ROSLIB.Topic({
    ros : ros,
    name : "/loatt_4r",
    messageType : "std_msgs/Float64"
});

var loatt_5l = new ROSLIB.Topic({
    ros : ros,
    name : "/loatt_5l",
    messageType : "std_msgs/Float64"
});

var loatt_5r = new ROSLIB.Topic({
    ros : ros,
    name : "/loatt_5r",
    messageType : "std_msgs/Float64"
});

var loatt_1l = new ROSLIB.Topic({
    ros : ros,
    name : "/loatt_1l",
    messageType : "std_msgs/Float64"
});

var loatt_1r = new ROSLIB.Topic({
    ros : ros,
    name : "/loatt_1r",
    messageType : "std_msgs/Float64"
});

loatt_2l.subscribe(function(message) {
    document.getElementById("loatt_2l").innerHTML = (message.data).toFixed(2);
});

loatt_2r.subscribe(function(message) {
    document.getElementById("loatt_2r").innerHTML = (message.data).toFixed(2);
});

loatt_3l.subscribe(function(message) {
    document.getElementById("loatt_3l").innerHTML = (message.data).toFixed(2);
});

loatt_3r.subscribe(function(message) {
    document.getElementById("loatt_3r").innerHTML = (message.data).toFixed(2);
});

loatt_4l.subscribe(function(message) {
    document.getElementById("loatt_4l").innerHTML = (message.data).toFixed(2);
});

loatt_4r.subscribe(function(message) {
    document.getElementById("loatt_4r").innerHTML = (message.data).toFixed(2);
});

loatt_5l.subscribe(function(message) {
    document.getElementById("loatt_5l").innerHTML = (message.data).toFixed(2);
});

loatt_5r.subscribe(function(message) {
    document.getElementById("loatt_5r").innerHTML = (message.data).toFixed(2);
});

loatt_1l.subscribe(function(message) {
    document.getElementById("loatt_1l").innerHTML = (message.data).toFixed(2);
});

loatt_1r.subscribe(function(message) {
    document.getElementById("loatt_1r").innerHTML = (message.data).toFixed(2);
});


<!-- loatt -->
