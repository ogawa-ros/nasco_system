var ros = new ROSLIB.Ros({url : "ws://" + IP_rxobs + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});


<!-- patt -->

var patt_2l = new ROSLIB.Topic({
    ros : ros,
    name : "/patt_2l",
    messageType : "std_msgs/Int32"
});

var patt_2r = new ROSLIB.Topic({
    ros : ros,
    name : "/patt_2r",
    messageType : "std_msgs/Int32"
});

var patt_3l = new ROSLIB.Topic({
    ros : ros,
    name : "/patt_3l",
    messageType : "std_msgs/Int32"
});

var patt_3r = new ROSLIB.Topic({
    ros : ros,
    name : "/patt_3r",
    messageType : "std_msgs/Int32"
});

var patt_4l = new ROSLIB.Topic({
    ros : ros,
    name : "/patt_4l",
    messageType : "std_msgs/Int32"
});

var patt_4r = new ROSLIB.Topic({
    ros : ros,
    name : "/patt_4r",
    messageType : "std_msgs/Int32"
});

var patt_5l = new ROSLIB.Topic({
    ros : ros,
    name : "/patt_5l",
    messageType : "std_msgs/Int32"
});

var patt_5r = new ROSLIB.Topic({
    ros : ros,
    name : "/patt_5r",
    messageType : "std_msgs/Int32"
});

var patt_1rl = new ROSLIB.Topic({
    ros : ros,
    name : "/patt_1rl",
    messageType : "std_msgs/Int32"
});

var patt_1ru = new ROSLIB.Topic({
    ros : ros,
    name : "/patt_1ru",
    messageType : "std_msgs/Int32"
});

var patt_1ll = new ROSLIB.Topic({
    ros : ros,
    name : "/patt_1ll",
    messageType : "std_msgs/Int32"
});

var patt_1lu = new ROSLIB.Topic({
    ros : ros,
    name : "/patt_1lu",
    messageType : "std_msgs/Int32"
});

patt_2l.subscribe(function(message) {
    document.getElementById("patt_2l").innerHTML = (message.data);
});

patt_2r.subscribe(function(message) {
    document.getElementById("patt_2r").innerHTML = (message.data);
});

patt_3l.subscribe(function(message) {
    document.getElementById("patt_3l").innerHTML = (message.data);
});

patt_3r.subscribe(function(message) {
    document.getElementById("patt_3r").innerHTML = (message.data);
});

patt_4l.subscribe(function(message) {
    document.getElementById("patt_4l").innerHTML = (message.data);
});

patt_4r.subscribe(function(message) {
    document.getElementById("patt_4r").innerHTML = (message.data);
});

patt_5l.subscribe(function(message) {
    document.getElementById("patt_5l").innerHTML = (message.data);
});

patt_5r.subscribe(function(message) {
    document.getElementById("patt_5r").innerHTML = (message.data);
});

patt_1rl.subscribe(function(message) {
    document.getElementById("patt_1rl").innerHTML = (message.data);
});

patt_1ru.subscribe(function(message) {
    document.getElementById("patt_1ru").innerHTML = (message.data);
});

patt_1ll.subscribe(function(message) {
    document.getElementById("patt_1ll").innerHTML = (message.data);
});

patt_1lu.subscribe(function(message) {
    document.getElementById("patt_1lu").innerHTML = (message.data);
})

<!-- patt -->
