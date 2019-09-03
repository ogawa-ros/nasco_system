var ros = new ROSLIB.Ros({url : "ws://" + "172.20.0.233" + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on("close", function() {console.log("websocket: closed");});


<!-- hemt_vd -->

var hemt_2l_vd = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_2l_vd",
    messageType : "std_msgs/Float64"
});

var hemt_2r_vd = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_2r_vd",
    messageType : "std_msgs/Float64"
});

var hemt_3l_vd = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_3l_vd",
    messageType : "std_msgs/Float64"
});

var hemt_3r_vd = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_3r_vd",
    messageType : "std_msgs/Float64"
});

var hemt_4l_vd = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_4l_vd",
    messageType : "std_msgs/Float64"
});

var hemt_4r_vd = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_4r_vd",
    messageType : "std_msgs/Float64"
});

var hemt_5l_vd = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_5l_vd",
    messageType : "std_msgs/Float64"
});

var hemt_5r_vd = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_5r_vd",
    messageType : "std_msgs/Float64"
});

hemt_2l_vd.subscribe(function(message) {
    document.getElementById("hemt_2l_vd").innerHTML = (message.data).toFixed(3);
});

hemt_2r_vd.subscribe(function(message) {
    document.getElementById("hemt_2r_vd").innerHTML = (message.data).toFixed(3);
});

hemt_3l_vd.subscribe(function(message) {
    document.getElementById("hemt_3l_vd").innerHTML = (message.data).toFixed(3);
});

hemt_3r_vd.subscribe(function(message) {
    document.getElementById("hemt_3r_vd").innerHTML = (message.data).toFixed(3);
});

hemt_4l_vd.subscribe(function(message) {
    document.getElementById("hemt_4l_vd").innerHTML = (message.data).toFixed(3);
});

hemt_4r_vd.subscribe(function(message) {
    document.getElementById("hemt_4r_vd").innerHTML = (message.data).toFixed(3);
});

hemt_5l_vd.subscribe(function(message) {
    document.getElementById("hemt_5l_vd").innerHTML = (message.data).toFixed(3);
});

hemt_5r_vd.subscribe(function(message) {
    document.getElementById("hemt_5r_vd").innerHTML = (message.data).toFixed(3);
});

<!-- hemt_vd -->
