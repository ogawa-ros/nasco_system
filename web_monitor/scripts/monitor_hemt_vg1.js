var ros = new ROSLIB.Ros({url : "ws://" + IP_rxobs + ":9000"});

ros.on("connection", function() {console.log("websocket: connected"); });
ros.on("error", function(error) {console.log("websocket error; ", error); });
ros.on('close', function() {
    console.log('websocket: closed, and reconection...');
    var ros = new ROSLIB.Ros({url : 'ws://' + IP_rxobs + ':9000'});
    console.log('websocket: connected')
        });


<!-- hemt_vg1 -->

var hemt_2l_vg1 = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_2l_vg1",
    messageType : "std_msgs/Float64"
});

var hemt_2r_vg1 = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_2r_vg1",
    messageType : "std_msgs/Float64"
});

var hemt_3l_vg1 = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_3l_vg1",
    messageType : "std_msgs/Float64"
});

var hemt_3r_vg1 = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_3r_vg1",
    messageType : "std_msgs/Float64"
});

var hemt_4l_vg1 = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_4l_vg1",
    messageType : "std_msgs/Float64"
});

var hemt_4r_vg1 = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_4r_vg1",
    messageType : "std_msgs/Float64"
});

var hemt_5l_vg1 = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_5l_vg1",
    messageType : "std_msgs/Float64"
});

var hemt_5r_vg1 = new ROSLIB.Topic({
    ros : ros,
    name : "/hemt_5r_vg1",
    messageType : "std_msgs/Float64"
});

hemt_2l_vg1.subscribe(function(message) {
    document.getElementById("hemt_2l_vg1").innerHTML = (message.data).toFixed(3);
});

hemt_2r_vg1.subscribe(function(message) {
    document.getElementById("hemt_2r_vg1").innerHTML = (message.data).toFixed(3);
});

hemt_3l_vg1.subscribe(function(message) {
    document.getElementById("hemt_3l_vg1").innerHTML = (message.data).toFixed(3);
});

hemt_3r_vg1.subscribe(function(message) {
    document.getElementById("hemt_3r_vg1").innerHTML = (message.data).toFixed(3);
});

hemt_4l_vg1.subscribe(function(message) {
    document.getElementById("hemt_4l_vg1").innerHTML = (message.data).toFixed(3);
});

hemt_4r_vg1.subscribe(function(message) {
    document.getElementById("hemt_4r_vg1").innerHTML = (message.data).toFixed(3);
});

hemt_5l_vg1.subscribe(function(message) {
    document.getElementById("hemt_5l_vg1").innerHTML = (message.data).toFixed(3);
});

hemt_5r_vg1.subscribe(function(message) {
    document.getElementById("hemt_5r_vg1").innerHTML = (message.data).toFixed(3);
});

<!-- hemt_vg1 -->
