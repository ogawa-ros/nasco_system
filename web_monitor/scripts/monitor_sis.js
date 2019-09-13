var ros = new ROSLIB.Ros({url : "ws://" + IP_rxobs + ":9000"});

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

sis_vol_2l.subscribe(sleep(1, function(message) {
    document.getElementById("sis_vol_2l").innerHTML = (message.data).toFixed(3);
}));

sis_vol_2r.subscribe(sleep(1, function(message) {
    document.getElementById("sis_vol_2r").innerHTML = (message.data).toFixed(3);
}));

sis_vol_3l.subscribe(sleep(1, function(message) {
    document.getElementById("sis_vol_3l").innerHTML = (message.data).toFixed(3);
}));

sis_vol_3r.subscribe(sleep(1, function(message) {
    document.getElementById("sis_vol_3r").innerHTML = (message.data).toFixed(3);
}));

sis_vol_4l.subscribe(sleep(1, function(message) {
    document.getElementById("sis_vol_4l").innerHTML = (message.data).toFixed(3);
}));

sis_vol_4r.subscribe(sleep(1, function(message) {
    document.getElementById("sis_vol_4r").innerHTML = (message.data).toFixed(3);
}));

sis_vol_5l.subscribe(sleep(1, function(message) {
    document.getElementById("sis_vol_5l").innerHTML = (message.data).toFixed(3);
}));

sis_vol_5r.subscribe(sleep(1, function(message) {
    document.getElementById("sis_vol_5r").innerHTML = (message.data).toFixed(3);
}));

sis_vol_1rl.subscribe(sleep(1, function(message) {
    document.getElementById("sis_vol_1rl").innerHTML = (message.data).toFixed(3);
}));

sis_vol_1ru.subscribe(sleep(1, function(message) {
    document.getElementById("sis_vol_1ru").innerHTML = (message.data).toFixed(3);
}));

sis_vol_1ll.subscribe(sleep(1, function(message) {
    document.getElementById("sis_vol_1ll").innerHTML = (message.data).toFixed(3);
}));

sis_vol_1lu.subscribe(sleep(1, function(message) {
    document.getElementById("sis_vol_1lu").innerHTML = (message.data).toFixed(3);
}));

<!-- sis_vol -->

<!-- sis_cur -->

var sis_cur_2l = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_cur_2l",
    messageType : "std_msgs/Float64"
});

var sis_cur_2r = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_cur_2r",
    messageType : "std_msgs/Float64"
});

var sis_cur_3l = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_cur_3l",
    messageType : "std_msgs/Float64"
});

var sis_cur_3r = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_cur_3r",
    messageType : "std_msgs/Float64"
});

var sis_cur_4l = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_cur_4l",
    messageType : "std_msgs/Float64"
});

var sis_cur_4r = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_cur_4r",
    messageType : "std_msgs/Float64"
});

var sis_cur_5l = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_cur_5l",
    messageType : "std_msgs/Float64"
});

var sis_cur_5r = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_cur_5r",
    messageType : "std_msgs/Float64"
});

var sis_cur_1rl = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_cur_1rl",
    messageType : "std_msgs/Float64"
});

var sis_cur_1ru = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_cur_1ru",
    messageType : "std_msgs/Float64"
});

var sis_cur_1ll = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_cur_1ll",
    messageType : "std_msgs/Float64"
});

var sis_cur_1lu = new ROSLIB.Topic({
    ros : ros,
    name : "/sis_cur_1lu",
    messageType : "std_msgs/Float64"
});

sis_cur_2l.subscribe(sleep(1, function(message) {
    document.getElementById("sis_cur_2l").innerHTML = (message.data).toFixed(3);
}));

sis_cur_2r.subscribe(sleep(1, function(message) {
    document.getElementById("sis_cur_2r").innerHTML = (message.data).toFixed(3);
}));

sis_cur_3l.subscribe(sleep(1, function(message) {
    document.getElementById("sis_cur_3l").innerHTML = (message.data).toFixed(3);
}));

sis_cur_3r.subscribe(sleep(1, function(message) {
    document.getElementById("sis_cur_3r").innerHTML = (message.data).toFixed(3);
}));

sis_cur_4l.subscribe(sleep(1, function(message) {
    document.getElementById("sis_cur_4l").innerHTML = (message.data).toFixed(3);
}));

sis_cur_4r.subscribe(sleep(1, function(message) {
    document.getElementById("sis_cur_4r").innerHTML = (message.data).toFixed(3);
}));

sis_cur_5l.subscribe(sleep(1, function(message) {
    document.getElementById("sis_cur_5l").innerHTML = (message.data).toFixed(3);
}));

sis_cur_5r.subscribe(sleep(1, function(message) {
    document.getElementById("sis_cur_5r").innerHTML = (message.data).toFixed(3);
}));

sis_cur_1rl.subscribe(sleep(1, function(message) {
    document.getElementById("sis_cur_1rl").innerHTML = (message.data).toFixed(3);
}));

sis_cur_1ru.subscribe(sleep(1, function(message) {
    document.getElementById("sis_cur_1ru").innerHTML = (message.data).toFixed(3);
}));

sis_cur_1ll.subscribe(sleep(1, function(message) {
    document.getElementById("sis_cur_1ll").innerHTML = (message.data).toFixed(3);
}));

sis_cur_1lu.subscribe(sleep(1, function(message) {
    document.getElementById("sis_cur_1lu").innerHTML = (message.data).toFixed(3);
}));

<!-- sis_cur -->
